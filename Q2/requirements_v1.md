**Objective**: Implement a Python program that determines whether a given positive integer is prime.

**Requirements**
**Input**
Accept a positive integer n from the user.

**Processing**
1. Check whether n is less than 2. If so, it is not prime.
2. Check whether n is divisible by 2. If it is, it is prime only if n == 2.
3. Check whether n is divisible by 3. If it is, it is prime only if n == 3.
4. Calculate the floor of the square root of n.
5. Test whether n is divisible by any integer starting from the floor of the square root and descending to 5.
6. Use the \(6k+1\) and \(6k-1\) observation from Question 1 to restrict the divisors being tested:
   - Only test potential divisors of the form \(6k-1\) or \(6k+1\).
   - Do not test numbers divisible by 2 or 3.
7. If any tested divisor divides n exactly, classify n as composite. Otherwise, classify it as prime.

**Output**
Display whether the input number is prime or composite.