# Q5 Specification: Iterative Euclidean GCD

Implements `requirements_v2.md` for Q5.

## 1. Deliverable
- File: `Q5/gcd_iterative.py` (standard library; `math.gcd` is used only in tests).
- Public API: `gcd(a: int, b: int) -> int`. Q6 imports it.

## 2. Design

### 2.1 `gcd(a, b)`
```python
def gcd(a, b):
    # Iterative Euclid. If a < b, the first pass swaps them (a % b == a),
    # so the lab's "assume a > b" is not required.
    while b != 0:
        a, b = b, a % b
    return a
```
- Returns `a` when `b == 0`, so `gcd(a, 0) = a`. `gcd(0, b)` gives `b` after one pass.
- No recursion and no `math.gcd`.
- Negative inputs are not required. If added, apply `abs()` first.

### 2.2 Reference and tests
- `gcd_rec(a, b)`: the lab's recursive version, used for tests only. It requires b ≠ 0.
- `self_test()`:
  - Fixed cases: `gcd(48,18)=6`, `gcd(100,75)=25`, `gcd(17,5)=1`, `gcd(12,12)=12`, `gcd(35,18)=1`, `gcd(7,0)=7`, `gcd(0,7)=7`, `gcd(9,1)=1`.
  - 1,000 random pairs (values up to 10⁹), each compared against `math.gcd` and, for b ≠ 0, against `gcd_rec`.
  - Fibonacci worst case: `gcd(F_90, F_89) = 1`. It runs about 89 iterations, with no recursion limit issue.
  - Print `"self-test passed"`.

### 2.3 CLI
Under `__main__`: prompt for two integers (validate with `try/except ValueError`) and print `gcd(a, b) = r`. Provide `--test` to run `self_test()`.

## 3. Implementation steps
1. Write `gcd`.
2. Write `gcd_rec` and `self_test`.
3. Write the CLI, with `--test`.
4. Run `python gcd_iterative.py --test`, then try a few manual inputs.

## 4. Verification
| Check | Expected |
|---|---|
| Fixed cases above | match |
| 1,000 random pairs | all agree with `math.gcd` |
| Fibonacci pair | 1, no error |
| a < b input | correct (Q6 depends on this) |
| Source inspection | a `while` loop and no self-call |

## 5. Risks
- Calling the function with b = 0 in the recursive reference raises `ZeroDivisionError`, so the test skips b = 0 for it.
