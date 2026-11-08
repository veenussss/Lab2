**Objective**: Implement a Python function that calculates the Euler Totient function, \(\phi(n)\), using the non-recursive GCD function developed in Question 5.

**Requirements**

**Dependencies and structure (new in v2)**
- Import `gcd` from the Q5 program file. Do not rewrite it, and do not use `math.gcd` inside the totient function.
- Define `euler_totient(n)` as a standalone function that returns the result and does no input or printing.
- Put user interaction under `if __name__ == "__main__":` so Q7 can import the function without side effects.

**Input**
- Accept a positive integer n.
- Validate the input. Reject non-integers and values below 1 with a clear message.

**Processing**
1. Initialize a counter to zero.
2. Iterate through all integers i from 1 to \(n-1\).
3. For each i:
   - Calculate `gcd(i, n)` using the function from Question 5. Note that i < n here, which the Q5 function must handle.
   - Check whether the result is equal to 1.
   - If it is, increment the counter.
4. After checking all integers, return the counter.

**Edge case (new in v2)**
- By the loop definition, \(n = 1\) gives 0, because the range is empty. By convention \(\phi(1)=1\). Return 1 for n = 1 explicitly, and add a comment saying so.

**Known values to test (new in v2)**
- \(\phi(1)=1\)
- \(\phi(2)=1\)
- \(\phi(12)=4\), the example given in the lab.
- \(\phi(9)=6\)
- \(\phi(10)=4\)
- \(\phi(13)=12\)
- For a prime p, \(\phi(p)=p-1\).

Add assertions for these, and print whether they pass.

**Performance notes (new in v2)**
- The method makes \(n-1\) gcd calls, so the time is linear in n. It is instant for n in the thousands.
- For the product of two primes between 2,000 and 3,000, n is about 4–9 million, so each call may take several seconds to a minute. This is acceptable for Q7. Do not replace it with a factorization shortcut, because the lab's point is to test the formula against the brute-force count.

**Output**
- Return \(\phi(n)\) from the function.
- In the main program, display the value, for example `phi(12) = 4`, which is the number of positive integers less than n that are relatively prime to n.
