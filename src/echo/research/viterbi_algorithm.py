"""维特比算法工具"""

import math
from typing import List, Optional


class ViterbiAlgorithm:
    _instance: Optional["ViterbiAlgorithm"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def decode(self, obs: List[int], states: List[int], init_prob: List[float], trans_prob: List[List[float]], emit_prob: List[List[float]]) -> Optional[List[int]]:
        n_obs = len(obs)
        n_states = len(states)
        if n_obs == 0:
            return None
        viterbi = [[0.0] * n_states for _ in range(n_obs)]
        path = [[0] * n_states for _ in range(n_obs)]
        for s in range(n_states):
            viterbi[0][s] = init_prob[s] * emit_prob[s][obs[0]]
        for t in range(1, n_obs):
            for s in range(n_states):
                max_prob = max(viterbi[t-1][s0] * trans_prob[s0][s] for s0 in range(n_states))
                viterbi[t][s] = max_prob * emit_prob[s][obs[t]]
                path[t][s] = max(range(n_states), key=lambda s0: viterbi[t-1][s0] * trans_prob[s0][s])
        last_state = max(range(n_states), key=lambda s: viterbi[n_obs-1][s])
        result = [last_state]
        for t in range(n_obs - 1, 0, -1):
            result.insert(0, path[t][result[0]])
        return result


def get_viterbi_algorithm() -> ViterbiAlgorithm:
    return ViterbiAlgorithm()
