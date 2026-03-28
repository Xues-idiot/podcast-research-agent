"""隐马尔可夫模型"""

import math
from typing import List, Optional


class HiddenMarkovModel:
    _instance: Optional["HiddenMarkovModel"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def forward(self, obs: List[int], init: List[float], trans: List[List[float]], emit: List[List[float]]) -> float:
        alpha = [init[i] * emit[i][obs[0]] for i in range(len(init))]
        for t in range(1, len(obs)):
            new_alpha = []
            for j in range(len(init)):
                new_alpha.append(sum(alpha[i] * trans[i][j] for i in range(len(alpha))) * emit[j][obs[t]])
            alpha = new_alpha
        return sum(alpha)

    def viterbi(self, obs: List[int], init: List[float], trans: List[List[float]], emit: List[List[float]]) -> List[int]:
        V = [{i: init[i] * emit[i][obs[0]] for i in range(len(init))}]
        path = {i: [i] for i in range(len(init))}
        for t in range(1, len(obs)):
            new_V = {}
            new_path = {}
            for j in range(len(init)):
                (prob, state) = max((V[t - 1][i] * trans[i][j] * emit[j][obs[t]], i) for i in range(len(init)))
                new_V[j] = prob
                new_path[j] = path[state] + [j]
            V.append(new_V)
            path = new_path
        return path[max(V[-1], key=V[-1].get)]


def get_hidden_markov_model() -> HiddenMarkovModel:
    return HiddenMarkovModel()
