**Objective**: Verify the relationship between the Euler Totient of the product of two distinct prime numbers and the product of their individual totients.

The assignment asks you to investigate whether:
\[
\phi(pq)=(p-1)(q-1)
\]

**Requirements**
**Input**
- Find two distinct prime numbers between 2,000 and 3,000.
- Assign them to variables p and q.
- Identify a few different combinations of prime numbers for testing.

**Processing**
For each combination of prime numbers:

1. Calculate their product:
\[
n=p\times q
\]

2. Calculate the Euler Totient of the product using the function developed in Question 6:
\[
\phi(n)=\text{EulerTotient}(n)
\]

3. Calculate the theoretical value:
\[
(p-1)(q-1)
\]
4. Compare the two results.
5. Check whether the results are equal.
6. Repeat the process for a few different combinations of prime numbers.

**Output**
- Display the selected prime numbers p and q.
- Display their product pq.
- Display the calculated Euler Totient value.
- Display the theoretical value \((p-1)(q-1)\).
- Indicate whether the two values are equal.
- Present the results for multiple combinations.