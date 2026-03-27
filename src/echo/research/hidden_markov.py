"""隐马尔可夫模型工具"""

import math
from typing import List, Optional, Tuple


class HiddenMarkov:
    _instance: Optional["HiddenMarkov"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def forward(self, obs: List[int], states: List[int], init_prob: List[float], trans_prob: List[List[float]], emit_prob: List[List[float]]) -> Optional[float]:
        n_obs = len(obs)
        n_states = len(states)
        if n_obs == 0:
            return None
        alpha = [init_prob[i] * emit_prob[i][obs[0]] for i in range(n_states)]
        for t in range(1, n_obs):
            new_alpha = []
            for j in range(n_states):
                total = sum(alpha[i] * trans_prob[i][j] for i in range(n_states))
                new_alpha.append(total * emit_prob[j][obs[t]])
            alpha = new_alpha
        return sum(alpha)


def get_hidden_markov() -> HiddenMarkov:
    return HiddenMarkov()
