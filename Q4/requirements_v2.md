**Objective**: Generate all prime numbers using the \(6k-1\) and \(6k+1\) pattern, and plot the percentage of integers in \([0,N]\) that are prime as N varies from 5,000 to 5,000,000.

**Requirements**

**Dependencies (new in v2)**
- Python standard library plus `matplotlib` for the graph. List `matplotlib` as the one install requirement (`pip install matplotlib`).
- Primality testing may reuse `is_prime` from Q2, or test each candidate only against the already-found primes up to its square root. Either choice must be stated in a code comment. A full sieve of Eratosthenes must not replace the \(6k\pm1\) approach.

**Input / Configuration**
- N ranges from 5,000 to 5,000,000 inclusive.
- Define the sampled N values explicitly, for example every 5,000 (5,000, 10,000, ..., 5,000,000, which gives 1,000 points). Keep the start, end and step as named constants.

**Processing**
1. Handle 2 and 3 explicitly. They are prime but are not of the form \(6k\pm1\) for k ≥ 1, so seed the prime list or count with them. Otherwise every count is short by 2.
2. Initialize k = 1.
3. Generate candidates in order: \(6k-1\), then \(6k+1\), then increment k. This produces 5, 7, 11, 13, 17, 19, and so on, up to 5,000,000. Stop once a candidate exceeds the largest N. Every number that could be prime must be tested.
4. Test each candidate for primality and store the primes found, in increasing order.
5. **Single pass, no restarts (new in v2).** Do the generation once over the full range. Do not recompute from 0 for each N. Keep a running prime count, and as the candidates pass each sampled N, record the count at that point. Use a pointer, or a count recorded at each checkpoint. Do not re-scan the prime list for every N.
6. For each sampled N:
   - The count of primes ≤ N is the running count at that checkpoint, including 2 and 3.
   - The number of integers in \([0,N]\) is N + 1.
   - Compute
   \[
   P(N)=\frac{\text{Number of primes in }[0,N]}{N+1}\times100
   \]
7. Plot P(N) against N.

**Correctness checks (new in v2)**
- The count of primes ≤ 5,000 must be 669. The count ≤ 5,000,000 must be 348,513. Assert these as checks, and print a warning if they fail.
- Print the total number of primes found.

**Output**
- A graph showing P(N) (percentage prime) against N from 5,000 to 5,000,000, with:
  - A title.
  - Axis labels: "N" and "Percentage of integers in [0, N] that are prime".
  - A readable scale. Optionally use a logarithmic x-axis, and state it if so.
- Save the graph to a file, for example `prime_percentage.png`, so it can be submitted, and also display it.
- Print a brief observation about the trend. The percentage decreases steadily as N grows, from about 13.4% at N = 5,000 to about 7.0% at N = 5,000,000. Primes become sparser, and the decline slows. This is consistent with density near \(1/\ln N\) from the prime number theorem. The decline is gradual and not abrupt.
