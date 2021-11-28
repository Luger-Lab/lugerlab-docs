# Loops

[Return to the Basic Python mainpage](https://luger-lab.github.io/coding-tutorials/basic_python/)

## [&larr; Back to Basic commands](https://luger-lab.github.io/coding-tutorials/basic_python/basic_commands/)

## Description
Loops in Python and other coding languages are used to perform functions multiple times. In Python, there are two main types of loops: For and While. These are similar to their counterparts in Bash, but much easier to use and understand.

## For loops
For loops iterate through iterable objects and perform the same function on each item until the end of the object or the loop is exited somehow. The general structure of a for loop is:
```
for i in list:
  print(i)
```
Where each time through the loop, the next item will be assigned to the variable `i` and any function within loop will act on that item as `i`.
You can use any variable you like and include as many functions inside the loop as possible. You can even nest loops inside of loops. **Tab spacing matters inside of loops.**

## While loops
While loops perform a function (or set of functions) over and over until a [logic](https://luger-lab.github.io/coding-tutorials/basic_python/logic/) check is satisfied. In order to make sure a while loop doesn't run forever, you need to make sure the variable in your logic check changes over time and that it will eventually satisfy the logic check.
```
j = 25
while j > 15:
  print("j is greater than 15")
  j -= 1
```

## [Continue to Logic &rarr;](https://luger-lab.github.io/coding-tutorials/basic_python/logic/)
