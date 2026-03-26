"""子Agent模块 - 并行任务执行

支持将独立任务委托给子Agent并行执行，提高研究效率。

参考 deer-flow subagent 系统架构
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Optional
import asyncio
import logging
import uuid

logger = logging.getLogger(__name__)


class TaskStatus(Enum):
    """任务状态"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    TIMED_OUT = "timed_out"


@dataclass
class TaskResult:
    """任务结果"""
    task_id: str
    status: TaskStatus
    result: Any = None
    error: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


@dataclass
class SubAgentTask:
    """子Agent任务"""
    id: str
    name: str
    description: str
    agent_type: str
    input_data: dict
    max_turns: int = 10
    timeout_seconds: int = 900  # 15分钟默认超时


class BaseSubAgent(ABC):
    """子Agent基类"""

    @property
    @abstractmethod
    def agent_type(self) -> str:
        """Agent类型标识"""
        pass

    @abstractmethod
    async def execute(self, input_data: dict) -> dict:
        """执行任务

        Args:
            input_data: 输入数据

        Returns:
            执行结果
        """
        pass

    def get_max_turns(self) -> int:
        """获取最大轮次"""
        return 10

    def get_timeout(self) -> int:
        """获取超时时间（秒）"""
        return 900


class SubAgentExecutor:
    """
    子Agent执行器

    管理子Agent的生命周期，支持：
    - 任务提交和调度
    - 后台线程执行
    - 并发数限制
    - 超时控制
    """

    def __init__(
        self,
        max_concurrent: int = 3,
        scheduler_pool_size: int = 3,
        execution_pool_size: int = 3,
        default_timeout: int = 900,
    ):
        """初始化执行器

        Args:
            max_concurrent: 最大并发任务数
            scheduler_pool_size: 调度线程池大小
            execution_pool_size: 执行线程池大小
            default_timeout: 默认超时时间（秒）
        """
        self.max_concurrent = max_concurrent
        self.default_timeout = default_timeout

        # 调度线程池
        self._scheduler_pool = asyncio.Semaphore(scheduler_pool_size)
        # 执行线程池
        self._execution_pool = asyncio.Semaphore(execution_pool_size)

        # 任务队列
        self._tasks: dict[str, SubAgentTask] = {}
        self._results: dict[str, TaskResult] = {}

        # 注册的Agent
        self._agents: dict[str, type[BaseSubAgent]] = {}

        # 运行中的任务
        self._running: set[str] = set()
        # 保存asyncio.Task引用以防止被垃圾回收
        self._running_tasks: set[asyncio.Task] = set()

    def register_agent(self, agent_class: type[BaseSubAgent]):
        """注册Agent类

        Args:
            agent_class: BaseSubAgent子类
        """
        agent = agent_class()
        self._agents[agent.agent_type] = agent_class
        logger.info(f"Registered agent: {agent.agent_type}")

    def get_agent(self, agent_type: str) -> Optional[BaseSubAgent]:
        """获取Agent实例

        Args:
            agent_type: Agent类型

        Returns:
            Agent实例
        """
        agent_class = self._agents.get(agent_type)
        if agent_class:
            return agent_class()
        return None

    async def submit(self, task: SubAgentTask) -> str:
        """提交任务

        Args:
            task: 子Agent任务

        Returns:
            任务ID
        """
        if task.agent_type not in self._agents:
            raise ValueError(f"Unknown agent type: {task.agent_type}")

        self._tasks[task.id] = task
        self._results[task.id] = TaskResult(
            task_id=task.id,
            status=TaskStatus.PENDING,
        )

        # 后台调度执行 - 保存Task引用防止被GC
        schedule_task = asyncio.create_task(self._schedule(task))
        self._running_tasks.add(schedule_task)
        schedule_task.add_done_callback(self._running_tasks.discard)

        return task.id

    async def _schedule(self, task: SubAgentTask):
        """调度任务执行"""
        async with self._scheduler_pool:
            # 等待并发槽位
            while len(self._running) >= self.max_concurrent:
                await asyncio.sleep(0.1)

            self._running.add(task.id)
            # 保存Task引用防止被GC
            exec_task = asyncio.create_task(self._execute(task))
            self._running_tasks.add(exec_task)
            exec_task.add_done_callback(self._running_tasks.discard)

    async def _execute(self, task: SubAgentTask):
        """执行任务"""
        agent = self.get_agent(task.agent_type)
        if not agent:
            self._results[task.id] = TaskResult(
                task_id=task.id,
                status=TaskStatus.FAILED,
                error=f"Agent not found: {task.agent_type}",
            )
            return

        self._results[task.id].status = TaskStatus.RUNNING
        self._results[task.id].started_at = datetime.now()

        timeout = min(agent.get_timeout(), task.timeout_seconds)

        try:
            async with self._execution_pool:
                result = await asyncio.wait_for(
                    agent.execute(task.input_data),
                    timeout=timeout
                )

            self._results[task.id].status = TaskStatus.COMPLETED
            self._results[task.id].result = result
            self._results[task.id].completed_at = datetime.now()

        except asyncio.TimeoutError:
            self._results[task.id].status = TaskStatus.TIMED_OUT
            self._results[task.id].error = f"Task timed out after {timeout}s"
            self._results[task.id].completed_at = datetime.now()

        except Exception as e:
            self._results[task.id].status = TaskStatus.FAILED
            self._results[task.id].error = str(e)
            self._results[task.id].completed_at = datetime.now()

        finally:
            self._running.discard(task.id)

    def get_result(self, task_id: str) -> Optional[TaskResult]:
        """获取任务结果

        Args:
            task_id: 任务ID

        Returns:
            任务结果
        """
        return self._results.get(task_id)

    async def wait_for(self, task_id: str, poll_interval: float = 0.5) -> TaskResult:
        """等待任务完成

        Args:
            task_id: 任务ID
            poll_interval: 轮询间隔（秒）

        Returns:
            任务结果
        """
        while True:
            result = self._results.get(task_id)
            if result and result.status in (
                TaskStatus.COMPLETED,
                TaskStatus.FAILED,
                TaskStatus.TIMED_OUT,
            ):
                return result

            await asyncio.sleep(poll_interval)

    def list_tasks(self) -> list[str]:
        """列出所有任务ID"""
        return list(self._tasks.keys())

    def get_running_count(self) -> int:
        """获取运行中的任务数"""
        return len(self._running)


# 全局执行器
_executor: Optional[SubAgentExecutor] = None


def get_subagent_executor() -> SubAgentExecutor:
    """获取全局子Agent执行器"""
    global _executor
    if _executor is None:
        _executor = SubAgentExecutor()
    return _executor


def create_task(
    name: str,
    description: str,
    agent_type: str,
    input_data: dict,
    max_turns: int = 10,
    timeout_seconds: int = 900,
) -> SubAgentTask:
    """创建子Agent任务

    Args:
        name: 任务名称
        description: 任务描述
        agent_type: Agent类型
        input_data: 输入数据
        max_turns: 最大轮次
        timeout_seconds: 超时时间

    Returns:
        子Agent任务
    """
    return SubAgentTask(
        id=str(uuid.uuid4())[:8],
        name=name,
        description=description,
        agent_type=agent_type,
        input_data=input_data,
        max_turns=max_turns,
        timeout_seconds=timeout_seconds,
    )
