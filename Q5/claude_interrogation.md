**Venus**: The lab says to assume a > b. Why does your gcd function still work when a is smaller than b?

**Claude**: Because the first pass of the loop swaps the two numbers. If a < b, then a % b is just a, so the line a, b = b, a % b turns (a, b) into (b, a). After that the larger number is in the first position, and the algorithm continues as normal.

For example, gcd(12, 18): the first pass gives a = 18, b = 12 % 18 = 12. The next pass gives a = 12, b = 18 % 12 = 6, then a = 6, b = 0, so the answer is 6.

This matters for Q6, which calls gcd(i, n) with i always smaller than n. The function needs no special case for it. The code has a comment about this, and the self-test includes cases with a < b.

---

**Venus**: Why do you write a, b = b, a % b in one line instead of using a temporary variable?

**Claude**: Python evaluates the whole right-hand side first and only then assigns to the names on the left. So b and a % b are both computed using the old values of a and b, and then a and b are updated together.

If you wrote it as two separate lines, a = b followed by b = a % b, the second line would use the new a, which is already equal to b. You would get b % b = 0 and the wrong answer. A temporary variable would also work, for example r = a % b, then a = b, then b = r. That is what the lab's step description does (r1 = a % b), and it behaves the same. The one-line version is just shorter.
