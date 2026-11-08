# Q5: Iterative GCD

A non-recursive Euclidean algorithm for the greatest common divisor.

## Files
- `gcd_iterative.py`: the program. It exports `gcd(a, b)`, which Q6 imports.
- `requirements_v1.md`, `requirements_v2.md`: requirements (v2 is the improved version).
- `spec.md`: implementation plan.
- `claude_interrogation.md`: questions asked about this program and the answers.

## How it works
```python
while b != 0:
    a, b = b, a % b
return a
```
It does not need a > b. If a < b, the first pass swaps them. Q6 relies on this.

## Run
```
python gcd_iterative.py          # asks for a and b
python gcd_iterative.py --test   # optional self-check
```
The self-check compares results with `math.gcd` and the lab's recursive version on fixed cases and 1,000 random pairs. Requires Python 3 only.

## Example
`gcd(48, 18) = 6`
