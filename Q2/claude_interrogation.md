**Venus**: why did you include python prime_check.py --test in the documentation, isn't python prime_check.py enough to run the program?

**Claude**: python prime_check.py is enough to run the program. The --test flag is an extra I added, and the lab doesn't ask for it.

Normal run: python prime_check.py starts the interactive prompt, where you type numbers and get prime or composite. This is what you use for the Piazza numbers.
--test: this runs the self-check instead of the prompt. It compares is_prime against a plain trial-division test for every n from 1 to 10,000. It also checks a few known values and prints "self-test passed".
I added it because the lab says to "verify Claude implements the algorithm" correctly, and the self-test is automatic evidence that it does. The spec.md and requirements_v2.md for Q2 also call for a self-check, so the flag follows from those.

If you'd rather not have it, I can do either of these:

Remove the --test flag, and the self-test code with it. The program would then only have the interactive prompt.
Keep the self-test but run it automatically at startup, so there's no flag to remember.
Q5 and Q6 have the same --test flag, and I'd change them the same way.

**Venus**: what is this sign:"->" how comes it isn't bringing about errors

**Claude**: -> in def is_prime(n: int) -> bool: is a return type annotation. It says the function returns a bool. It's documentation only, and Python doesn't enforce it, which is why it causes no errors.

n: int is the same idea for the parameter. It says n should be an int.
Python stores these hints and ignores them when the code runs. Calling is_prime("hello") wouldn't be blocked by the hint. It would fail later, at n < 2, because a string can't be compared with a number.
Editors and tools like mypy read the hints to catch mistakes and give better autocomplete.
The syntax has been valid since Python 3.5. You'd only see an error on a very old Python version. The program works the same with the hints removed, so def is_prime(n): would behave identically.