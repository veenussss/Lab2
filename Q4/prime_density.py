"""Q4: Percentage of integers in [0, N] that are prime, N from 5,000 to 5,000,000.

Primes are found with the 6k-1 / 6k+1 candidate pattern in a SINGLE pass;
the running prime count is recorded at each sampled N (no restart per N).

Primality of each candidate is tested by trial division against the primes
already found (up to sqrt(candidate)) -- this reuses earlier work in the same
pass. No sieve is used.
"""
from pathlib import Path

import matplotlib

import sys
if "--no-show" in sys.argv:
    matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

N_MIN, N_MAX, N_STEP = 5_000, 5_000_000, 5_000


def is_prime_by_primes(c: int, primes: list) -> bool:
    """Trial-divide c by stored primes p with p*p <= c (c is never divisible by 2 or 3)."""
    for p in primes:
        if p < 5:
            continue  # skip 2 and 3
        if p * p > c:
            break
        if c % p == 0:
            return False
    return True


def prime_counts(checkpoints: list) -> tuple:
    """Single pass; return (counts at each checkpoint, list of all primes found)."""
    primes = [2, 3]  # not of the form 6k+-1 for k >= 1, so add by hand
    counts = []
    ci = 0
    last = checkpoints[-1]
    k = 1
    done = False
    while not done:
        for c in (6 * k - 1, 6 * k + 1):
            # close out every checkpoint strictly below this candidate
            while ci < len(checkpoints) and checkpoints[ci] < c:
                counts.append(len(primes))
                ci += 1
            if c > last:
                done = True
                break
            if is_prime_by_primes(c, primes):
                primes.append(c)
        k += 1
    while ci < len(checkpoints):  # remaining checkpoints
        counts.append(len(primes))
        ci += 1
    return counts, primes


def main() -> None:
    checkpoints = list(range(N_MIN, N_MAX + 1, N_STEP))
    counts, primes = prime_counts(checkpoints)
    pct = [100.0 * c / (n + 1) for c, n in zip(counts, checkpoints)]

    print(f"Total primes up to {N_MAX:,}: {len(primes):,}")
    print(f"pi({checkpoints[0]:,}) = {counts[0]:,}  -> {pct[0]:.2f}%")
    print(f"pi({checkpoints[-1]:,}) = {counts[-1]:,}  -> {pct[-1]:.2f}%")
    if counts[0] != 669:
        print(f"WARNING: expected pi(5,000) = 669, got {counts[0]}")
    if counts[-1] != 348_513:
        print(f"WARNING: expected pi(5,000,000) = 348,513, got {counts[-1]}")

    plt.figure(figsize=(9, 5))
    plt.plot(checkpoints, pct)
    plt.title("Percentage of integers in [0, N] that are prime")
    plt.xlabel("N")
    plt.ylabel("Percentage prime (%)")
    plt.grid(True)
    out = Path(__file__).resolve().parent / "prime_percentage.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    print(f"Graph saved to {out}")

    print("\nObservation: the percentage of primes falls steadily as N grows "
          f"(about {pct[0]:.1f}% at N=5,000 to about {pct[-1]:.1f}% at N=5,000,000). "
          "The decline slows down, consistent with prime density ~ 1/ln(N).")
    if "--no-show" not in sys.argv:
        plt.show()


if __name__ == "__main__":
    main()
