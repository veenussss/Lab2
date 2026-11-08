# Q6: Euler Totient

Computes φ(n), the number of integers from 1 to n-1 whose gcd with n is 1, using the non-recursive `gcd` from Q5.

## Files
- `euler_totient.py`: the program. It exports `euler_totient(n)`, which Q7 imports.
- `requirements_v1.md`, `requirements_v2.md`: requirements (v2 is the improved version).
- `spec.md`: implementation plan.
- `claude_interrogation.md`: questions asked about this program and the answers.

## How it works
Loop i from 1 to n-1 and count how many have `gcd(i, n) == 1`. This is a brute-force count on purpose, so Q7 can check the formula against it. φ(1) is returned as 1 by convention.

## Run
```
python euler_totient.py          # asks for n
python euler_totient.py --test   # optional self-check
```
The self-check covers known values such as φ(12) = 4, φ(p) = p-1 for primes, and n = 2..500 against a `math.gcd` count. Requires Python 3 only. Q5 must stay in its sibling folder.

## Speed
The time grows linearly with n. It is instant for small n. For n of about 4–9 million (Q7), it takes a few seconds per call.

## Example
`phi(12) = 4`
