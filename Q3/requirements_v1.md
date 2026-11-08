**Objective**: Estimate how many random numbers must be generated, on average, before finding a prime number in two specified intervals.

**Requirements**
**Input / Configuration**
- Define the first interval: 5,000,000 to 6,000,000.
- Define the second interval: 500,000,000,000 to 500,001,000,000.
- Set the number of experiments:
- 1,000 attempts for the first interval.
- 250 attempts for the second interval.

**Processing**
For each interval:
1. Initialize a list or accumulator to store the number of random generations required in each experiment.
2. Repeat the experiment the specified number of times.
3. For each experiment:
   - Initialize a generation counter to zero.
   - Generate a random integer within the specified interval.
   - Increment the generation counter.
   - Test whether the generated number is prime using the function from Question 2.
   - If it is not prime, generate another random integer and repeat.
   - Stop when a prime number is found.
   - Record the number of generations required.
4. Calculate the average number of generations across all experiments.

**Output**
- Display the average number of random generations required to find a prime in the first interval.
- Display the average number of random generations required to find a prime in the second interval.