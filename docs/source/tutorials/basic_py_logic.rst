# Logic

[Return to the Basic Python mainpage](https://luger-lab.github.io/coding-tutorials/basic_python/)

## [&larr; Back to Loops](https://luger-lab.github.io/coding-tutorials/basic_python/loops/)

## Description
There are many times when coding that you'll want to make a logic check. In Python there are a few types of logic checks: boolean, is/is not, and comparisons.

## Boolean
Boolean means True or False, in Python these are denoted as capitalized `True` or `False` and are not strings, so do not need quotes. In fact, using quotes will return a string, not a boolean. You can set variables equal to booleans or return them after logical operations.

## is/is not
`is` compares whether or not a variable refer to the same memory reference. It returns `True` if two variables reference the same memory location.
```
a = "happy"
b = "unhappy"
c = a
a is c
True
```
You can check the memory location using `id`.
```
id(a)
140241117068272
id(c)
140241117068272
```
`is not` is the opposite of is and will return `True` if the variables reference different memory loactions.
```
c is not b
True
```
## Value comparisons
You can also use value operators like `>` greater than, `<` less than, `==` equal to, or `!=` not equal to to compare the values of two items. The value returned will be a boolean.
```
15 < 14
False
```
The `==` and `!=` operators differ from is and is not, in that they compare values and not memory assignments.

```
d = 15
15 == d
True
```
## If statements
All of these comparisons are useful for starting and ending loops. They can also be used in `if statements`. And `if statement` executes an operation if a logical operation returns `True`.
```
d = 15
if d == 15:
  print("d equals 15")
d equals 15
```
If your logical operation is not `True`, you can execute an operation when the if statement fails using `else`.
```
d = 14
if d == 15:
  print("d equals 15")
else:
  print("d doesn't equal 15")
d doesn't equal 15
```
Third option is to execute an addition conditional operation when the if statement is `False` using `elif` (else-if).
```
d = 14
if d == 15:
  print("d equals 15")
elif d == 14:
  print("d equals 14")
else:
  print("d doesn't equal 15")
d doesn't equal 14
```
**You can use as many `if` and `elif` conditions as you want per if statement, but only one else statement. Tabs matter.**

## [Back to Coding tutorials mainpage &rarr;](https://luger-lab.github.io/coding-tutorials/)
