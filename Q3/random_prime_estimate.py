"""Q3: Average number of random draws needed to hit a prime in an interval.

Reuses is_prime from Q2/prime_check.py.
"""
import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Q2"))
from prime_check import is_prime  # noqa: E402

INTERVALS = [
    # (label, low, high, experiments)
    ("5,000,000 to 6,000,000", 5_000_000, 6_000_000, 1000),
    ("500 billion to 500 billion + 1 million", 500_000_000_000, 500_001_000_000, 250),
]
SEED = None  # set to an int to reproduce a run


def draws_until_prime(low: int, high: int, rng: random.Random) -> int:
    """Draw random ints in [low, high] until one is prime; return the draw count."""
    count = 0
    while True:
        n = rng.randint(low, high)  # inclusive on both ends
        count += 1
        if is_prime(n):
            return count


def estimate(low: int, high: int, trials: int, rng: random.Random) -> list:
    return [draws_until_prime(low, high, rng) for _ in range(trials)]


def main() -> None:
    rng = random.Random(SEED)
    for label, low, high, trials in INTERVALS:
        print(f"\nInterval: {label}  ({trials} experiments) ... running", flush=True)
        counts = estimate(low, high, trials, rng)
        avg = sum(counts) / len(counts)
        expected = math.log((low + high) / 2)
        print(f"  Experiments run : {len(counts)}")
        print(f"  Average draws   : {avg:.2f}")
        print(f"  Min / Max       : {min(counts)} / {max(counts)}")
        print(f"  ln(midpoint)    : {expected:.2f}  (prime number theorem estimate)")


if __name__ == "__main__":
    main()
