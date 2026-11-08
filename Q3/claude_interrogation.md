**Venus**: In Q3 folder, how comes you only called "prime_check" when they are in different folders?

**Claude**: Python can only import prime_check if it knows where to look, and these lines in Q3/random_prime_estimate.py:9-10 tell it:


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Q2"))
from prime_check import is_prime
Search list: when you write import X, Python searches the folders in sys.path. By default that's the script's own folder (Q3) plus the installed libraries. prime_check.py is in Q2, so a plain import would fail with ModuleNotFoundError.
Building the path: Path(__file__).resolve() is the full path of the Q3 script. .parents[1] goes up one level to the Lab2 folder, and / "Q2" points to the Q2 folder.
Adding it: sys.path.insert(0, ...) puts the Q2 folder at the front of the search list. After that, from prime_check import is_prime finds the file there.
I only wrote the file name, prime_check, because Python's import takes the module name without the folder or .py. The folder was already handled by the sys.path line above.

The same trick is used in Q6, which imports from Q5, and in Q7, which imports from Q2, Q5 and Q6.

It only works while the folders stay laid out as they are. If you moved Q2, the import would break. The if __name__ == "__main__": guard in prime_check.py stops its prompt from starting when it's imported.

**Venus**: Why was it necessary to assign SEED = None

**Claude**: It wasn't necessary. The program would run fine without it. I added it as an optional convenience.

SEED is passed to random.Random(SEED) in Q3/random_prime_estimate.py. It controls whether the random numbers are repeatable:

SEED = None: Python seeds the generator from the system (time or OS randomness), so every run gives different numbers and slightly different averages. This is what the lab wants, since it asks for random numbers.
SEED = 42, or any integer: the generator produces the same sequence every time, so you get identical averages on every run.
I put it in for two reasons:

Repeatability: if you want to show or re-run the exact same result for your submission, you can set a number.
Debugging: a repeatable run makes it easier to check changes to the code.
None is the default that means "no fixed seed". I used a named constant at the top so you can change it without hunting through the code. If you don't need that, you can delete SEED and use random.Random() instead, which behaves the same.