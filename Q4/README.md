# Q4: Percentage of Primes up to N

Finds primes using the 6k-1 and 6k+1 pattern and plots the percentage of integers in [0, N] that are prime, for N from 5,000 to 5,000,000.

## Files
- `prime_density.py`: the program.
- `prime_percentage.png`: the graph it produces.
- `requirements_v1.md`, `requirements_v2.md`: requirements (v2 is the improved version).
- `spec.md`: implementation plan.
- `claude_interrogation.md`: questions asked about this program and the answers.

## How it works
- One pass over the candidates 6k-1 and 6k+1 (k = 1, 2, ...), with 2 and 3 added by hand.
- Each candidate is tested by trial division against the primes already found (up to its square root). No sieve is used.
- A running prime count is recorded at each sampled N (every 5,000), so nothing restarts from 0 for each N.
- P(N) = (primes in [0, N]) / (N + 1) × 100.

## Run
```
pip install matplotlib
python prime_density.py             # saves the graph and opens a plot window
python prime_density.py --no-show   # saves the graph without opening a window
```
It takes about 10 seconds.

## Results
- Primes up to 5,000: 669, which is 13.38%.
- Primes up to 5,000,000: 348,513, which is 6.97%.

## Observation
The percentage of primes falls steadily as N grows, and the decline slows down. This matches prime density of about 1/ln(N).
