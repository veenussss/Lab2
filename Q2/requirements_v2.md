**Objective**: Implement a Python program that determines whether a given positive integer is prime, using the square-root bound and the \(6k\pm1\) observation from Question 1.

**Requirements**

**Structure (new in v2)**
- Put the primality logic in a reusable function `is_prime(n)` that returns `True` or `False` and does no input or printing.
- The user-interaction code must sit under `if __name__ == "__main__":` so Q3, Q4 and Q7 can import `is_prime` without triggering a prompt.
- Use only the Python standard library (`math.isqrt` for the integer square root, to avoid floating-point error on large n).

**Input**
- Accept a positive integer n from the user.
- Validate the input. If it is not an integer, or is less than 1, print a clear message and ask again or exit. Do not crash.
- Allow testing several numbers in one run (for example, a loop until the user quits), so the numbers posted on Piazza can be checked quickly.

**Processing** (inside `is_prime`)
1. If n < 2, return `False`.
2. If n == 2 or n == 3, return `True`.
3. If n is divisible by 2 or by 3, return `False`. These are the only even and multiple-of-3 primes, so they are handled before this step.
4. Compute `s = isqrt(n)`, the floor of the square root of n.
5. Build the divisors to test using the \(6k\pm1\) pattern from Question 1: every candidate d must satisfy `d % 6 == 1` or `d % 6 == 5`. Never test a multiple of 2 or 3.
6. Test these divisors in **descending** order, starting from the largest \(6k\pm1\) value that is ≤ s and ending at 5 inclusive. A concrete way to do this is to start at the largest k with \(6k+1 \le s\) or \(6k-1 \le s\), then step through \(6k+1\), \(6k-1\), \(6(k-1)+1\), and so on down to 5.
7. If any tested divisor divides n exactly, return `False` (composite).
8. If none divides n, return `True` (prime).
9. Do not use a full range scan, a library primality function, or a sieve. The algorithm must follow the steps above, and the code should include comments mapping each step to this list so the implementation can be verified.

**Edge cases that must behave correctly**
- 1 is not prime, and neither is 0.
- 2 and 3 are prime. 4 is composite.
- 5 and 7 are prime. With n=5 the divisor range is empty, so the answer is prime.
- 25 and 49 are composite. These are squares of 5 and 7, so s equals the divisor, which checks the inclusive bound.
- Large inputs must work, for example 500,000,000,003 (the divisor loop is at most about 236,000 iterations).

**Output**
- For each input, display the number and whether it is **prime** or **composite**. Use "neither prime nor composite" for 1, or a clear equivalent.

**Verification (new in v2)**
- Include a self-check that compares `is_prime` against a naive reference test (trial division by every integer from 2 up to √n) for all n from 1 to 10,000. Both must agree for every n.
- Print the result of the self-check.
- Show the output for the numbers posted on Piazza.
