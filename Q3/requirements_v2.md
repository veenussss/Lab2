**Objective**: Estimate how many random numbers must be generated, on average, before finding a prime number in two specified intervals, reusing the primality test from Question 2.

**Requirements**

**Dependencies (new in v2)**
- Import `is_prime` from the Q2 program file. Do not copy or rewrite the primality logic.
- Use the standard library `random` module.
- The Q2 file must be importable without running its input prompt. This is guaranteed by the `__main__` guard required in Q2 v2.

**Input / Configuration**
- First interval: 5,000,000 to 6,000,000, inclusive of both ends.
- Second interval: 500,000,000,000 to 500,001,000,000, inclusive of both ends. This is 500 billion to 500 billion plus 1 million.
- Number of experiments:
  - 1,000 for the first interval.
  - 250 for the second interval.
- Keep the intervals and experiment counts as named constants or a configuration table at the top of the file.
- Use `random.randint(low, high)` so both endpoints are possible. Optionally allow an integer seed so runs can be reproduced.

**Processing**
For each interval:
1. Initialize a list to store the number of random generations required in each experiment.
2. Repeat the experiment the specified number of times.
3. For each experiment:
   - Initialize a generation counter to zero.
   - Generate a random integer within the interval.
   - Increment the generation counter.
   - Test the number with `is_prime` from Question 2.
   - If it is not prime, generate another random integer and repeat. The same counter continues.
   - Stop when a prime is found.
   - Record the counter. The final, successful draw counts, so the minimum possible value is 1.
4. Calculate the average of the recorded counts (sum divided by the number of experiments).

**Performance notes (new in v2)**
- The second interval needs trial division up to about 707,000. Each prime test takes at most about 236,000 iterations, which is fine for about 250 experiments. Do not add a precomputed sieve.
- Print a progress message per interval so the run is visibly working.

**Output**
- The average number of random generations needed to find a prime in the first interval.
- The average number of random generations needed to find a prime in the second interval.
- Also show the number of experiments run, and optionally the minimum and maximum counts observed.
- Add a short sanity comparison. By the prime number theorem, the expected average is roughly \(\ln(n)\) for a random n near the interval, which is about 15.6 for 5.5 million and about 27 for 5×10¹¹. State whether the measured averages are close to these.
- The averages vary between runs because the numbers are random. Report the averages from the final submitted run.
