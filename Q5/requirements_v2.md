**Objective**: Implement a non-recursive (iterative) Python function that calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

**Requirements**

**Structure (new in v2)**
- Define `gcd(a, b)` as a standalone function that returns the result and does no input or printing.
- Put any user interaction under `if __name__ == "__main__":` so Q6 and Q7 can import `gcd` without side effects.
- The function must be iterative. It must not call itself, and a `while` loop is expected.
- Do not use `math.gcd`.

**Input**
- Accept two integers a and b from the user.
- The lab assumes a > b, but the function must not rely on it. Q6 calls `gcd(i, n)` with i < n. The first loop pass swaps the two values (since `a % b == a` when a < b), so the algorithm still works. State this in a comment.
- Validate the input. Reject non-integers with a clear message.
- Negative inputs are not required. If handled, take absolute values first.

**Processing**
1. While b is not equal to zero:
   - Calculate the remainder:
     \[
     r=a\bmod b
     \]
   - Replace a with the current value of b.
   - Replace b with the remainder r.
2. Continue until b is zero (the remainder is zero).
3. Return the final value of a as the GCD.

**Edge cases (new in v2)**
- `gcd(a, 0)` returns a, since the loop does not run.
- `gcd(0, b)` returns b.
- `gcd(n, 1)` returns 1.
- `gcd(a, a)` returns a.
- Coprime inputs return 1, for example `gcd(35, 18)`.
- Large integers must work with no recursion-depth issue, for example consecutive Fibonacci numbers, the worst case for the number of steps.

**Verification (new in v2)**
- Compare results against the lab's recursive version:
  ```python
  def gcd_rec(a, b):
      if a % b == 0: return b
      else: return gcd_rec(b, a % b)
  ```
  This is for testing only, and requires b ≠ 0.
- Compare against `math.gcd` as an independent check.
- Run at least these: `gcd(48, 18) = 6`, `gcd(100, 75) = 25`, `gcd(17, 5) = 1`, `gcd(12, 12) = 12`. Also test 1,000 random pairs for agreement with `math.gcd`, and print the result.

**Output**
- Return the GCD from the function.
- In the main program, display the GCD of the two input integers, for example `gcd(48, 18) = 6`.
