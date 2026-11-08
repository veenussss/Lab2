"""Q2: Primality test using the square-root bound and the 6k+/-1 observation.

Usage:
    python prime_check.py          # interactive
    python prime_check.py --test   # run self-test
"""
import sys
from math import isqrt


def is_prime(n: int) -> bool:
    """Return True if n is prime, following the lab's algorithm."""
    # Steps 1-3: small cases, then evens and multiples of 3.
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Step 4: floor of the square root (exact integer arithmetic).
    s = isqrt(n)

    # Steps 5-6: test only divisors of the form 6k-1 / 6k+1, in descending
    # order from the largest such value <= s down to 5 (inclusive).
    # kmax is the largest k with 6k-1 <= s; 6k+1 may overshoot s, so guard it.
    kmax = (s + 1) // 6
    for k in range(kmax, 0, -1):
        for d in (6 * k + 1, 6 * k - 1):
            if d > s:
                continue
            # Step 7: an exact divisor means composite.
            if n % d == 0:
                return False
    # Step 8: no divisor found.
    return True


def _naive_is_prime(n: int) -> bool:
    """Reference: trial division by every integer from 2 to isqrt(n)."""
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def self_test() -> None:
    for n in range(1, 10_001):
        assert is_prime(n) == _naive_is_prime(n), f"mismatch at {n}"
    known = {0: False, 1: False, 2: True, 3: True, 4: False, 5: True, 7: True,
             25: False, 49: False, 121: False, 169: False, 97: True}
    for n, expected in known.items():
        assert is_prime(n) == expected, f"known value failed at {n}"
    big = 500_000_000_003
    assert is_prime(big) == _naive_is_prime(big), "large value mismatch"
    print("self-test passed (1..10000 agree with naive reference)")


def describe(n: int) -> str:
    if n == 1:
        return "1 is neither prime nor composite"
    return f"{n} is {'prime' if is_prime(n) else 'composite'}"


def main() -> None:
    if "--test" in sys.argv:
        self_test()
        return
    print("Primality test. Enter a positive integer (or 'q' to quit).")
    while True:
        text = input("n = ").strip()
        if text == "" or text.lower() == "q":
            break
        try:
            n = int(text)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if n < 1:
            print("Please enter a positive integer (>= 1).")
            continue
        print(describe(n))


if __name__ == "__main__":
    main()
