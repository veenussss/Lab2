# Q2 Specification: Primality Test (square-root bound + 6k±1)

Implements `requirements_v2.md` for Q2. Source of truth for behavior is that file. This document says how to build it.

## 1. Deliverable
- File: `Q2/prime_check.py` (standard library only: `math`).
- Public API: `is_prime(n: int) -> bool`. Q3 and Q7 import it.
- CLI behavior lives under `if __name__ == "__main__":`.

## 2. Design

### 2.1 `is_prime(n)`
Pure function, no I/O.

```
is_prime(n):
    if n < 2:            return False
    if n in (2, 3):      return True
    if n % 2 == 0 or n % 3 == 0: return False      # steps 1-3 of the lab paragraph
    s = isqrt(n)                                    # floor of sqrt, exact for big ints
    # largest 6k+-1 value <= s, then walk down to 5
    k = (s + 1) // 6                                # 6k-1 <= s+... see note below
    for each k from kmax down to 1:
        for d in (6k+1, 6k-1):                      # descending within a block
            if d > s: continue                      # only top block can overshoot
            if n % d == 0: return False
    return True
```

Note on the top block: take `kmax = (s + 1) // 6`. This is the largest k with 6k-1 ≤ s. Then 6k+1 may exceed s, so skip it with the `d > s` guard. The loop ends at k = 1, so the smallest divisors tested are 7 and 5, which satisfies "down to 5".

Why this is correct: any composite n has a divisor ≤ √n. After removing 2 and 3, the smallest prime factor is ≥ 5 and so is ≡ ±1 mod 6. Testing all 6k±1 values in [5, s] covers it, and it can include non-prime d, which is harmless.

### 2.2 CLI (`main`)
- Loop: prompt for an integer, `q` or empty input to quit.
- Parse with `int()` inside `try/except ValueError`. Reject n < 1 with a message and re-prompt.
- Print `"<n> is prime"` or `"<n> is composite"`. Print `"1 is neither prime nor composite"` for n = 1.

### 2.3 Self-check (`self_test`)
- Reference function `_naive_is_prime(n)`: trial division by every integer from 2 to `isqrt(n)`.
- Assert `is_prime(n) == _naive_is_prime(n)` for n = 1..10,000. Also assert a set of known values: 1→F, 2→T, 3→T, 4→F, 5→T, 25→F, 49→F, 97→T, 500000000003→T. Verify the last value against the reference at runtime. Do not hardcode it unchecked.
- Run via the command line flag `--test`, and print `"self-test passed"`.

## 3. Implementation steps
1. Write `is_prime` with comments labeling each step to the requirements list.
2. Write `_naive_is_prime` and `self_test`.
3. Write `main` with the prompt loop and the `--test` flag.
4. Run `python prime_check.py --test`. Then run it interactively on the Piazza numbers.

## 4. Verification
| Check | Expected |
|---|---|
| `--test` | all 10,000 agree with the naive reference |
| 1, 0 | not prime |
| 2, 3, 5, 7 | prime |
| 25, 49, 121 | composite (square equals tested divisor) |
| 500000000003 | matches the naive reference, runs in well under a second |
| Input `abc`, `-4` | clear message, no crash |

Verification of the lab requirement "verify Claude implements it this way": read the code against §2.1. It must contain the n<2, 2, 3 checks, an `isqrt`, and a descending 6k±1 loop to 5. It must not contain a `range(2, ...)` full scan or a sieve, apart from the test reference.

## 5. Risks
- Off-by-one on the top k block. This is covered by the tests on 25, 49, 121, 169 (13²), which check the inclusive bound.
- Floating-point `sqrt` on large n. This is avoided by using `isqrt`.
