# Q7 Specification: Verify φ(pq) = (p−1)(q−1)

Implements `requirements_v2.md` for Q7.

## 1. Deliverable
- File: `Q7/totient_verify.py` (standard library: `time`, `sys`, `pathlib`).
- Reuses `is_prime` (Q2) and `euler_totient` (Q6, which uses Q5's `gcd`).

## 2. Design

### 2.1 Imports
```python
import sys, time
from pathlib import Path
root = Path(__file__).resolve().parents[1]
for q in ("Q2", "Q5", "Q6"):           # Q6 imports gcd_iterative from Q5 itself,
    sys.path.insert(0, str(root / q))  # but Q5 is added here for safety
from prime_check import is_prime
from euler_totient import euler_totient
```

### 2.2 Choosing primes
- `primes_in_range(2000, 3000)`: `[n for n in range(2000, 3001) if is_prime(n)]`. This is 127 primes. Print the count.
- Pairs: a fixed list `PAIRS` at the top, four distinct pairs, chosen from that list, for example `(2003, 2011)`, `(2017, 2027)`, `(2677, 2999)`, `(2063, 2909)`. Assert at startup that every value is in `primes_in_range` and that `p != q`. Fixed pairs make runs repeatable. A random option is not needed.

### 2.3 Per-pair check
```
for (p, q) in PAIRS:
    n = p * q
    print progress ("computing phi(n) ... ")
    t0 = time.time()
    actual   = euler_totient(n)       # brute force from Q6
    expected = (p - 1) * (q - 1)
    record (p, q, n, actual, expected, actual == expected, elapsed)
```

### 2.4 Report
- Print an aligned table: `p, q, pq, phi(pq), (p-1)(q-1), equal?, seconds`.
- Final line: `"phi(pq) == (p-1)(q-1) held for all N tested pairs"`, or list the failures.
- Optional: one short note explaining why the formula is true. Of the numbers 1..pq−1, the ones not coprime to pq are the multiples of p (q−1 of them) and the multiples of q (p−1 of them). Counting these gives pq − 1 − (p−1) − (q−1) = (p−1)(q−1).

## 3. Implementation steps
1. Add the imports and confirm they load without prompts.
2. Build the prime list and validate `PAIRS`.
3. Loop over the pairs, calling `euler_totient`.
4. Print the table and the conclusion.
5. Run it. Expect a few minutes in total.

## 4. Verification
| Check | Expected |
|---|---|
| Primes in [2000, 3000] | 127 |
| Each pair | p ≠ q, both prime, both in range |
| Each result | `phi(pq) == (p-1)(q-1)` is True |
| Output | the table lists all pairs plus the conclusion line |

## 5. Performance
n is roughly 4–9 million, so each `euler_totient` call makes n−1 gcd calls. Expect from several seconds to about a minute per pair, and a few minutes for four pairs. Progress lines and per-pair timing show it is working. Do not shortcut with factorization.

## 6. Risks
- If p = q, the identity does not apply, so it is excluded by assertion.
- Slow runs. They are mitigated by keeping the number of pairs small (4).
