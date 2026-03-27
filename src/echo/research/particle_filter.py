"""粒子滤波器"""

import random
from typing import List, Callable, Optional


class ParticleFilter:
    _instance: Optional["ParticleFilter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def filter(self, particles: List[float], weights: List[float], observation: float, likelihood_fn: Callable) -> List[float]:
        if len(particles) == 0:
            return []
        new_weights = [w * likelihood_fn(p, observation) for p, w in zip(particles, weights)]
        total = sum(new_weights)
        if total == 0:
            return particles
        normalized = [w / total for w in new_weights]
        indices = random.choices(range(len(particles)), weights=normalized, k=len(particles))
        return [particles[i] for i in indices]


def get_particle_filter() -> ParticleFilter:
    return ParticleFilter()
