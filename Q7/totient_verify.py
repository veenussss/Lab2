"""Q7: Verify phi(pq) == (p-1)(q-1) for primes p != q in [2000, 3000].

Uses is_prime (Q2) and euler_totient (Q6, which uses the iterative gcd of Q5).
"""
import sys
import time
from pathlib import Path

root = Path(__file__).resolve().parents[1]
for q in ("Q2", "Q5", "Q6"):
    sys.path.insert(0, str(root / q))
from prime_check import is_prime  # noqa: E402
from euler_totient import euler_totient  # noqa: E402

LOW, HIGH = 2000, 3000
PAIRS = [(2003, 2011), (2017, 2027), (2677, 2999), (2063, 2909)]


def primes_in_range(low: int, high: int) -> list:
    return [n for n in range(low, high + 1) if is_prime(n)]


def main() -> None:
    primes = set(primes_in_range(LOW, HIGH))
    print(f"Primes between {LOW} and {HIGH}: {len(primes)}")
    for p, q in PAIRS:
        assert p != q, f"p and q must differ: {p}"
        assert p in primes and q in primes, f"({p}, {q}) not both prime in range"

    rows = []
    for p, q in PAIRS:
        n = p * q
        print(f"Computing phi({n}) for p={p}, q={q} ...", flush=True)
        t0 = time.time()
        actual = euler_totient(n)
        expected = (p - 1) * (q - 1)
        rows.append((p, q, n, actual, expected, actual == expected, time.time() - t0))

    header = f"{'p':>6} {'q':>6} {'pq':>10} {'phi(pq)':>10} {'(p-1)(q-1)':>11} {'equal?':>7} {'sec':>7}"
    print("\n" + header)
    print("-" * len(header))
    for p, q, n, actual, expected, ok, secs in rows:
        print(f"{p:>6} {q:>6} {n:>10} {actual:>10} {expected:>11} {str(ok):>7} {secs:>7.1f}")

    failures = [(r[0], r[1]) for r in rows if not r[5]]
    if failures:
        print(f"\nFormula FAILED for: {failures}")
    else:
        print(f"\nphi(pq) == (p-1)(q-1) held for all {len(rows)} tested pairs.")


if __name__ == "__main__":
    main()
