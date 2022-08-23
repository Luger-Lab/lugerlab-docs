# Python packages

[Return to the Advanced Python - Conda, packages, and scripting mainpage](https://luger-lab.github.io/coding-tutorials/advanced_python_code/)

## [&larr; Back to Python packages](https://luger-lab.github.io/coding-tutorials/advanced_python_code/python_packages/)

## Running scripts
Running a Python script is very easy, simply call:
```
python script.py [arguments]
```
You can try it with one of mine.

## Genereal strucuture
This is the script we just ran. In general:
- import things at the top
- define your main function
- define all of your other functions
    - should be as small as possible
    - should take as few inputs as possible
- call the main function using: `if __name__ == '__main__':`

    ```
    import random
    import sys

    def main():   
        goal_gcs = calc_goal_gcs(length, gc_content)
        bases = make_rand_oligo(length, goal_gcs)
        gc_count = count_gc(bases)
        new_oligo = check_gc(gc_count, goal_gcs, bases)

    def calc_goal_gcs(length, gc_content):
        goal_gcs = int(length*gc_content)
        return goal_gcs

    def make_rand_oligo(length, goal_gcs):
        bases = []
        for i in range(length):
            rand_int = random.randint(1, length)
            if rand_int <= goal_gcs:
                if rand_int % 2 == 0:
                    new_base = 'G'
                else:
                    new_base = 'C'
            else:
                if rand_int % 2 == 0:
                    new_base = 'A'
                else:
                    new_base = 'T'
            bases.append(new_base)
        return bases

    def count_gc(bases):
        gc_count = 0
        for base in bases:
            if base == 'G':
                gc_count += 1
            elif base == 'C':
                gc_count += 1
            else:
                continue
        return gc_count    

    def check_gc(gc_count, goal_gcs, bases):
        if gc_count == goal_gcs:
            new_oligo = ''.join(bases)
            print(new_oligo)
            return new_oligo
        else:
            main()

    if __name__ == '__main__':
        length = int(sys.argv[1])
        gc_content = (float(sys.argv[2]))/100
        main()
    ```

## Arguments
There are two main ways to input arguments into your script. Either as positional arguments (as above) or with [argparse](https://docs.python.org/3/library/argparse.html)(preferred way)
0. Positional arguments are simply inputed after the name of the script and then can be called inside the script using `sys.argv[1]`. The 0 index is the script name itself.
0. Argparse takes a little more time to set up, but allows you to make flags, require arguments and types, and easily collect all of your inputs. There are plenty of examples online of how to use this.
## PEP8
If you are really concerned about your code being "up to snuff", you can adhere to the [PEP8](https://pep8.org/) guidelines. There are even programs that will check your work to see if you are adhering to them.

## [Continue to Practice &rarr;](https://luger-lab.github.io/coding-tutorials/advanced_python_code/practice/)
