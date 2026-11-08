"""Q5: Iterative (non-recursive) Euclidean GCD.

Usage:
    python gcd_iterative.py          # interactive
    python gcd_iterative.py --test   # run self-test
"""
import random
import sys
from math import gcd as _math_gcd  # used ONLY in tests


def gcd(a: int, b: int) -> int:
    """Greatest common divisor by the iterative Euclidean algorithm.

    If a < b, the first pass swaps them (a % b == a), so 'assume a > b'
    is not required.
    """
    while b != 0:
        a, b = b, a % b
    return a


def gcd_rec(a: int, b: int) -> int:
    """The lab's recursive version -- for testing only (requires b != 0)."""
    if a % b == 0:
        return b
    return gcd_rec(b, a % b)


def self_test() -> None:
    fixed = {(48, 18): 6, (100, 75): 25, (17, 5): 1, (12, 12): 12,
             (35, 18): 1, (7, 0): 7, (0, 7): 7, (9, 1): 1}
    for (a, b), expected in fixed.items():
        assert gcd(a, b) == expected, f"gcd({a},{b}) != {expected}"
    rng = random.Random(1)
    for _ in range(1000):
        a, b = rng.randint(1, 10**9), rng.randint(1, 10**9)
        assert gcd(a, b) == _math_gcd(a, b) == gcd_rec(a, b), f"mismatch {a},{b}"
    f1, f2 = 1, 1  # Fibonacci worst case
    fib = [f1, f2]
    while len(fib) < 90:
        fib.append(fib[-1] + fib[-2])
    assert gcd(fib[89], fib[88]) == 1
    print("self-test passed")


def main() -> None:
    if "--test" in sys.argv:
        self_test()
        return
    try:
        a = int(input("a = "))
        b = int(input("b = "))
    except ValueError:
        print("Please enter whole numbers.")
        return
    print(f"gcd({a}, {b}) = {gcd(a, b)}")


if __name__ == "__main__":
    main()
