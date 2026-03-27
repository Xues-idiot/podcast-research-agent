"""质数查找器"""

from typing import List, Optional


class PrimeFinder:
    _instance: Optional["PrimeFinder"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def primes_up_to(self, n: int) -> List[int]:
        if n < 2:
            return []
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(2, n + 1) if sieve[i]]

    def nth_prime(self, n: int) -> Optional[int]:
        if n < 1:
            return None
        if n == 1:
            return 2
        primes = [2]
        candidate = 3
        while len(primes) < n:
            is_prime = True
            for p in primes:
                if p * p > candidate:
                    break
                if candidate % p == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(candidate)
            candidate += 2
        return primes[-1]


def get_prime_finder() -> PrimeFinder:
    return PrimeFinder()
