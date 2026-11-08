# Q6 Specification: Euler Totient via Non-recursive GCD

Implements `requirements_v2.md` for Q6.

## 1. Deliverable
- File: `Q6/euler_totient.py` (standard library).
- Public API: `euler_totient(n: int) -> int`. Q7 imports it.
- Depends on `gcd` from `Q5/gcd_iterative.py`.

## 2. Design

### 2.1 Import of Q5
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Q5"))
from gcd_iterative import gcd
```

### 2.2 `euler_totient(n)`
```python
def euler_totient(n):
    if n == 1:
        return 1          # convention phi(1) = 1; the loop below would give 0
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:    # note i < n; Q5's gcd handles a < b
            count += 1
    return count
```
- Brute force by design. Do not use factorization, because Q7 checks the formula against this count.
- Does not use `math.gcd`.

### 2.3 Self-test
Assertions: φ(1)=1, φ(2)=1, φ(9)=6, φ(10)=4, φ(12)=4, φ(13)=12. For every prime p below 100, `phi(p) == p-1`. Optionally cross-check n = 1..500 against a count that uses `math.gcd`. Print `"self-test passed"`.

### 2.4 CLI
Under `__main__`: prompt for a positive integer (validate; reject n < 1), print `phi(n) = value`. `--test` runs the self-test.

## 3. Implementation steps
1. Add the Q5 import.
2. Write `euler_totient` with the n = 1 special case.
3. Write `self_test` and the CLI.
4. Run `--test`, then `phi(12)`.

## 4. Verification
| Input | Expected |
|---|---|
| 12 | 4 (the lab's example) |
| 1 | 1 |
| 13 | 12 |
| 9 | 6 |
| import | no prompt from Q5 or Q6 |

## 5. Performance
Time is linear in n, with one gcd call per integer. It is instant for n in the thousands. For Q7's n of about 4–9 million, expect on the order of ten seconds to a minute per call in CPython. This is expected, and Q7 prints progress for it.

## 6. Risks
- The n = 1 convention. It is documented in a comment and tested.
- The `sys.path` trick depends on the folder layout. It breaks if Q5 is moved.
