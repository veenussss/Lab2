"""Q6: Euler totient by brute force, using the non-recursive gcd from Q5.

Usage:
    python euler_totient.py          # interactive
    python euler_totient.py --test   # run self-test
"""
import sys
from math import gcd as _math_gcd  # used ONLY in tests
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Q5"))
from gcd_iterative import gcd  # noqa: E402


def euler_totient(n: int) -> int:
    """Count integers i in 1..n-1 with gcd(i, n) == 1."""
    if n == 1:
        return 1  # convention phi(1) = 1; the loop below would give 0
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:  # i < n here; Q5's gcd handles a < b
            count += 1
    return count


def self_test() -> None:
    known = {1: 1, 2: 1, 9: 6, 10: 4, 12: 4, 13: 12}
    for n, expected in known.items():
        assert euler_totient(n) == expected, f"phi({n}) != {expected}"
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
              61, 67, 71, 73, 79, 83, 89, 97):
        assert euler_totient(p) == p - 1
    for n in range(2, 501):
        ref = sum(1 for i in range(1, n) if _math_gcd(i, n) == 1)
        assert euler_totient(n) == ref, f"mismatch at {n}"
    print("self-test passed")


def main() -> None:
    if "--test" in sys.argv:
        self_test()
        return
    try:
        n = int(input("n = "))
    except ValueError:
        print("Please enter a whole number.")
        return
    if n < 1:
        print("Please enter a positive integer.")
        return
    print(f"phi({n}) = {euler_totient(n)}")


if __name__ == "__main__":
    main()
