# Q3 Specification: Average Draws Until a Random Prime

Implements `requirements_v2.md` for Q3.

## 1. Deliverable
- File: `Q3/random_prime_estimate.py` (standard library: `random`, `sys`, `pathlib`).
- Reuses `is_prime` from `Q2/prime_check.py`. No copied logic.

## 2. Design

### 2.1 Import of Q2
Q2 is a sibling folder, not a package, so extend `sys.path` at the top:

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Q2"))
from prime_check import is_prime
```

This works because Q2 has a `__main__` guard and so produces no prompt on import.

### 2.2 Configuration (module constants)
```python
INTERVALS = [
    # (label, low, high, experiments)
    ("5,000,000 to 6,000,000",              5_000_000,        6_000_000,        1000),
    ("500 billion to 500 billion + 1M", 500_000_000_000, 500_001_000_000, 250),
]
SEED = None   # set an int to reproduce a run
```

### 2.3 Functions
- `draws_until_prime(low, high, rng) -> int`
  ```
  count = 0
  while True:
      n = rng.randint(low, high)   # inclusive both ends
      count += 1
      if is_prime(n): return count
  ```
- `estimate(low, high, trials, rng) -> list[int]`: calls `draws_until_prime` `trials` times and returns the counts.
- `main()`:
  - Create `rng = random.Random(SEED)`.
  - For each interval, print a progress line, run `estimate`, then print the average (`sum/len`), the trial count, and the min and max.
  - Print the expected-value comparison: `ln((low+high)/2)`, computed with `math.log`.

## 3. Implementation steps
1. Add the import block and the constants.
2. Implement `draws_until_prime` and `estimate`.
3. Implement `main`, with output formatted to 2 decimals.
4. Run it. Record the two averages for submission.

## 4. Verification
| Check | Expected |
|---|---|
| Each recorded count | ≥ 1 |
| Interval 1 average | close to ln(5.5M) ≈ 15.6 (plausible range about 14–17 over 1000 trials) |
| Interval 2 average | close to ln(5×10¹¹) ≈ 27 (plausible range about 22–32 over 250 trials) |
| Fixed seed | two runs give identical output |
| Import | no prompt appears from Q2 |

## 5. Performance
- Interval 2: at most about 236,000 divisor tests per prime test. The expected number of draws is about 27 per experiment, so there are about 6,700 tests in all. Composites mostly exit early. Total runtime is expected to be seconds to a minute or so.
- Print a progress message at the start of each interval.

## 6. Risks
- `randint` is inclusive, matching the requirements. `randrange` would not be.
- The 250-trial average has a larger variance, so the sanity range above is wide on purpose.
