# Basic commands

[Return to the Basic Python mainpage](https://luger-lab.github.io/coding-tutorials/basic_python/)

## [&larr; Back to Getting started](https://luger-lab.github.io/coding-tutorials/basic_python/getting_started/)

## Description
Once running Python (on the command line, through and IDE or a notebook), you can try running some basic commands. Remember the commands you are able to run and even syntax can change based on the version of Python you are working, we will work with the newest version of Python (3.9.7). To execute code in the command line, simply press `enter`. In an IDE or notebook, use `shift+enter`.

## Print
One of the most basic commands and one of the most helpful for debugging your code is the `print` command. It is functionally similar to `echo` in Bash, however the syntax is different.
```
print("hello world")
```
The quotes here specify that "hello world" is a string and not another object that Python should look for the value of. **You can use either single (') or double (") quotes, but they must be paired with the same one on the other end. You can also use the other set of quotes inside the opposite quotes if nesting quotes are needed** You should be able to print the value of any string, int, float, variable, list, dictionary or other object using this syntax.

## Variables
To assign a variable simply type the name of the variable, the equals sign and then the value you wish to assign. This variable can be: a integer, floating point, string, or boolean.
```
var1 = 15
print(var1)
15
```
You can change the value of a variable by using the same syntax again and simply imputing a new value.
```
var1 = "hello world"
print(var1)
hello world
```
You can check the type of a variable using:
```
type(var1)
<class 'str'>
```
## Tuples
Tuples are used to store multiple items as a single, ordered, unchangable variable. They are created by making a collection of items inside parenthesis and assigning them to a variable.
```
tup1 = ("red", 2, True)
```
You can turn another collection of items into a tuple using"
```
tuple(other_collection)
```
## Sets
Set store data in an unordered collection. They are made using curly brackets and assigning them to a variable.
```
set1 = {"red", 2, True}
```
You can add an item to a set using:
```
set1.add(5)
print(set1)
{"red", 2, True, 5}
```
Similarly to tuples, you can make another collection into a set using:
```
set(tup1)
```
## Lists
Lists are one of the most common collections in Python and other programming languages (array in Bash). They are ordered and changeable collection. You can assign a list using square brackets:
```
list1 = ["red", 2, True]
```
Or make an empty list by using empty brackets:
```
list2 = []
```
Because lists are ordered, you can call values of specific items in the list by calling their index. **Lists are indexed starting from 0.** You can also index from the back of the list using negative numbers (-1 gives you the last item in a list).
```
list1[0]
red
```
You can also 'slice' a list using a `:`. Slicing will show you a part of the list, either the beginning up until an index:
```
list1[:2]
```
From an index to the end of the list:
```
list1[2:]
```
Or between two indices:
```
list1[1:3]
```
Again, you can convert other items into lists using the `list()` function.

## Dictionaries
Another powerful way to store data is with a dictionary, which is essentially a combination of variables and lists. You can assign a value (or values) to a key and they search the dictionary to return the value of the key. To make a dictionary, make an empty dictionary:
```
dict1 = {}
```
Then add key, value pairs to it using:
```
dict1["red"] = {15}
```
You can add values to keys using:
```
dict1["red"].add(16)
```
Return the value of a key by using it like and index of a list:
```
dict1["red"]
{15, 16}
```

## [Continue to Loops &rarr;](https://luger-lab.github.io/coding-tutorials/basic_python/loops/)
