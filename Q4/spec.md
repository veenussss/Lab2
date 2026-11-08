# Q4 Specification: Prime Percentage Graph via 6k±1 (single pass)

Implements `requirements_v2.md` for Q4.

## 1. Deliverable
- File: `Q4/prime_density.py` (standard library plus `matplotlib`).
- Output image: `Q4/prime_percentage.png`.

## 2. Design

### 2.1 Configuration
```python
N_MIN, N_MAX, N_STEP = 5_000, 5_000_000, 5_000     # 1,000 sample points
```

### 2.2 Algorithm: one pass with checkpoints
The prime count is accumulated once up to `N_MAX`. At each sampled N, the running count is saved.

```
primes = [2, 3]                          # not of form 6k+-1, add by hand
checkpoints = [N_MIN, N_MIN+N_STEP, ..., N_MAX]
counts = []                              # counts[i] = pi(checkpoints[i])
ci = 0
k = 1
while ci < len(checkpoints):
    for c in (6k-1, 6k+1):
        # before handling candidate c, close out every checkpoint below c
        while ci < len(checkpoints) and checkpoints[ci] < c:
            counts.append(len(primes)); ci += 1
        if ci == len(checkpoints): break
        if is_prime_by_primes(c, primes): primes.append(c)
    k += 1
```
After the loop, any remaining checkpoints (if the loop ended early) get the final count. A checkpoint that equals a candidate is handled correctly, because the checkpoint is closed only when `checkpoints[ci] < c`, so c is included in that count.

`is_prime_by_primes(c, primes)`: trial division by stored primes p with `p*p <= c`, skipping 2 and 3, since c is never divisible by them. Stop at the first divisor. This reuses the primes found so far in the same pass, which is the single-pass efficiency requirement. A comment must state this choice, as the requirements ask.

Using a sieve is not allowed.

### 2.3 Percentage
`pct[i] = 100 * counts[i] / (checkpoints[i] + 1)`, using the lab's interval size N+1.

### 2.4 Plot
- `matplotlib.pyplot.plot(checkpoints, pct)`.
- Title: "Percentage of integers in [0, N] that are prime". X label: "N". Y label: "Percentage prime (%)".
- Grid on. Save to `prime_percentage.png` at 150 dpi, then `plt.show()`.

### 2.5 Checks and observation
- Assert `counts[0] == 669` (π(5,000)) and `counts[-1] == 348_513` (π(5,000,000)). If a check fails, print a warning with the actual value. Do not hide it.
- Print the total primes found, and the percentage at the first and last N.
- Print the observation: the percentage falls steadily as N grows (roughly 13.4% to about 7.0%), the decline slows, and this matches density about 1/ln N.

## 3. Implementation steps
1. Write the candidate generator and `is_prime_by_primes`.
2. Write the checkpoint loop (§2.2). Test it on a small range first, e.g. N up to 100, where π(100) = 25.
3. Compute the percentages and the plot, then save the image.
4. Run the full range and check the two assertions.

## 4. Verification
| Check | Expected |
|---|---|
| N up to 100 (test run) | 25 primes |
| π(5,000) | 669 |
| π(5,000,000) | 348,513 |
| Graph shape | decreasing, concave-up, no jumps |
| Runs without restarting per N | one candidate loop in the code |

## 5. Performance
About 1.67M candidates. Composites exit early, and primes need at most about 330 divisions (primes up to 2,236). Estimated runtime is 10–60 seconds in CPython. Do not call the plain Q2 `is_prime` per candidate, because it would be roughly twice as slow. If done that way, state it.

## 6. Risks
- Forgetting 2 and 3 makes every count short by 2 (caught by the π(5,000) assertion).
- A checkpoint boundary off-by-one. Caught by the small-range test and the two assertions.
- `matplotlib` missing: install with `pip install matplotlib`.
