**Objective**: Implement a Python function that calculates the Euler Totient function, \(\phi(n)\), using the non-recursive GCD function developed in Question 5.

**Requirements**
**Input**
Accept a positive integer n.

**Processing**
1. Initialize a counter to zero.
2. Iterate through all integers from 1 to \(n-1\).
3. For each integer i:
   - Calculate gcd(i, n) using the function from Question 5.
   - Check whether the result is equal to 1.
   - If the GCD is 1, increment the counter.
4. After checking all integers, return the counter.

**Output**
Return and display the value of \(\phi(n)\), representing the number of positive integers less than n that are relatively prime to n.