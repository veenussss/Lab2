**Objective**: Implement a Python function that calculates the greatest common divisor (GCD) of two integers using the iterative Euclidean algorithm.

**Requirements**
**Input**
- Accept two integers, a and b.
- Assume \(a>b\), as specified in the assignment.

**Processing**
1. While b is not equal to zero:
   - Calculate the remainder:
     \[
     r=a\bmod b
     \]
   - Replace a with the current value of b.
   - Replace b with the remainder r.
2. Continue until the remainder becomes zero.
3. Return the final value of a as the GCD.

**Output**
Return and display the GCD of the two input integers.