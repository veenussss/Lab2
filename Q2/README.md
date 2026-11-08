# Q2: Primality Test

Tests whether a positive integer is prime, using the square-root bound and the 6k±1 observation from Question 1.

## Files
- `prime_check.py`: the program. It exports `is_prime(n)`, which Q3 and Q7 import.
- `requirements_v1.md`, `requirements_v2.md`: requirements (v2 is the improved version).
- `spec.md`: implementation plan.
- `claude_interrogation.md`: questions asked about this program and the answers.

## How it works
1. n < 2 is not prime. 2 and 3 are prime.
2. Multiples of 2 or 3 are composite.
3. Compute `s = isqrt(n)`, the floor of the square root.
4. Test only divisors of the form 6k-1 and 6k+1, in descending order from the largest such value ≤ s down to 5.
5. If any divides n, n is composite. Otherwise it is prime.

## Run
```
python prime_check.py          # interactive: type numbers, 'q' to quit
python prime_check.py --test   # optional self-check against a naive test (n = 1..10,000)
```
Requires Python 3 only (standard library).

## Results (Piazza numbers)
| Number | Result |
|---|---|
| 1000000000000037 | prime |
| 1000000000000223 | prime |
| 1000000000000001 | composite |
| 1000000000000005 | composite |
