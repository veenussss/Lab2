# Q7: Checking φ(pq) = (p-1)(q-1)

Tests the formula for products of two distinct primes between 2,000 and 3,000.

## Files
- `totient_verify.py`: the program. It uses `is_prime` (Q2) and `euler_totient` (Q6, which uses Q5's `gcd`).
- `requirements_v1.md`, `requirements_v2.md`: requirements (v2 is the improved version).
- `spec.md`: implementation plan.
- `claude_interrogation.md`: questions asked about this program and the answers.

## How it works
1. Lists the primes in [2000, 3000] with `is_prime` (there are 127).
2. Checks that each chosen pair is distinct, prime and in range.
3. For each pair, computes φ(pq) by brute force and compares it to (p-1)(q-1).
4. Prints a table and a conclusion line.

## Run
```
python totient_verify.py
```
It takes about 15 seconds. Q2, Q5 and Q6 must stay in their sibling folders. Edit `PAIRS` at the top of the file to test other primes.

## Results
| p | q | pq | φ(pq) | (p-1)(q-1) | equal |
|---|---|---|---|---|---|
| 2003 | 2011 | 4028033 | 4024020 | 4024020 | yes |
| 2017 | 2027 | 4088459 | 4084416 | 4084416 | yes |
| 2677 | 2999 | 8028323 | 8022648 | 8022648 | yes |
| 2063 | 2909 | 6001267 | 5996296 | 5996296 | yes |

φ(pq) = (p-1)(q-1) held for all four pairs. Of the numbers below pq, the non-coprime ones are the multiples of p (q-1 of them) and of q (p-1 of them), which gives pq - 1 - (p-1) - (q-1) = (p-1)(q-1).
