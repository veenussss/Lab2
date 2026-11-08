# Q3: Average Draws Until a Random Prime

Estimates how many random numbers must be generated in an interval before one is prime.

## Files
- `random_prime_estimate.py`: the program. It imports `is_prime` from `../Q2/prime_check.py`.
- `requirements_v1.md`, `requirements_v2.md`: requirements (v2 is the improved version).
- `spec.md`: implementation plan.
- `claude_interrogation.md`: questions asked about this program and the answers.

## How it works
For each interval, one experiment draws random integers (inclusive of both ends) and counts draws until `is_prime` returns True. The counts from all experiments are averaged.

| Interval | Experiments |
|---|---|
| 5,000,000 to 6,000,000 | 1,000 |
| 500,000,000,000 to 500,001,000,000 | 250 |

## Run
```
python random_prime_estimate.py
```
Needs Python 3 only. Q2 must stay in its sibling folder, since the import path points there. Set `SEED` at the top of the file to an integer for a repeatable run. `None` gives a different result each run.

## Results (one run)
| Interval | Average draws | ln(midpoint) |
|---|---|---|
| 5M to 6M | 15.75 | 15.52 |
| 500 billion range | 25.38 | 26.94 |

The averages change from run to run because the numbers are random. They sit near ln(n), as the prime number theorem predicts.
