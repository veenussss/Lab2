**Objective**: Verify the relationship between the Euler Totient of the product of two distinct prime numbers and the product of their individual totients.

The assignment asks you to investigate whether:
\[
\phi(pq)=(p-1)(q-1)
\]

**Requirements**

**Dependencies (new in v2)**
- Import `is_prime` from the Q2 program file.
- Import `euler_totient` from the Q6 program file. Q6 in turn uses the non-recursive `gcd` from Q5.
- Do not copy or rewrite these functions, and do not use `math.gcd` or any library totient function.

**Input**
- Find two distinct prime numbers between 2,000 and 3,000.
- Use `is_prime` to find them. For example, build the list of primes in [2000, 3000], or check each chosen number.
- Assign them to variables p and q, and require p ≠ q. For p = q the formula would be \(p(p-1)\), not \((p-1)^2\), which is a different case.
- Identify a few different combinations for testing. Use at least 3 pairs, up to 5. Choose the pairs either from a fixed list defined at the top of the file or at random, and state which. A fixed list makes runs repeatable.

**Processing**
For each combination of primes:
1. Verify that both p and q are prime, and that both are within [2000, 3000].
2. Calculate their product:
\[
n=p\times q
\]
3. Calculate the Euler Totient of the product using the function developed in Question 6:
\[
\phi(n)=\text{EulerTotient}(n)
\]
4. Calculate the theoretical value:
\[
(p-1)(q-1)
\]
5. Compare the two results and check whether they are equal.
6. Repeat for each combination.

**Performance notes (new in v2)**
- n is roughly 4 to 9 million. The brute-force totient makes n−1 gcd calls, so each pair may take several seconds to a minute.
- Print a progress message before each computation, and optionally the elapsed time, so the program does not look frozen.

**Output**
For each combination, display:
- The selected primes p and q.
- Their product pq.
- The calculated Euler Totient value.
- The theoretical value \((p-1)(q-1)\).
- Whether the two values are equal.

Present the results for all combinations in a single table or aligned list. End with a one-line conclusion stating whether the formula \(\phi(pq)=(p-1)(q-1)\) held for every tested pair.
