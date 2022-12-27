# 100 Python Interview Questions

## 1- Python uses a Global Interpreter Lock. Does that mean it doesn’t use real threads?

No, Python uses real threads, but the Global Interpreter Lock (GIL) is a mechanism that prevents multiple native threads from executing Python bytecodes at once. This lock is necessary because CPython, the reference implementation of Python, is not thread-safe, meaning that multiple threads can potentially interfere with each other and compromise the integrity of an application.

The GIL makes it easy to write simple, thread-safe Python programs, but it can also limit the performance of multi-threaded programs, especially ones that rely heavily on CPU-bound operations. In these cases, Python's threading module may not provide the level of parallelism that you need. In such cases, you may want to consider using an alternative implementation of Python that does not have a GIL, such as PyPy or Jython, or using a different approach to parallelism, such as the multiprocessing module or using subprocesses.

## 2- Is it possible to have a producer thread reading from the network and a consumer thread writing to a file, really work in parallel? What about the GIL?

Yes, it is possible to have a producer thread that reads from the network and a consumer thread that writes to a file work in parallel in Python, even with the GIL in place. This is because the GIL only prevents multiple native threads from executing Python bytecodes at once. It does not prevent threads from performing other operations, such as waiting for data to be available on a network socket or waiting for a file to be written to disk.

In the case of a producer thread reading from the network and a consumer thread writing to a file, the producer thread can block on a network read operation, allowing the consumer thread to run in the meantime. Similarly, the consumer thread can block on a file write operation, allowing the producer thread to run. In this way, the two threads can effectively work in parallel, even though only one native thread is executing Python bytecodes at a time due to the GIL.

It is important to note that the GIL can still limit the overall performance of a program that uses multiple threads, especially if the threads are CPU-bound. In such cases, you may want to consider using an alternative implementation of Python that does not have a GIL, or using a different approach to parallelism, such as the multiprocessing module or using subprocesses.

## 3- What will be the output of the following code in each step?

```python
class C:
    dangerous = 2
c1 = C()
c2 = C()
print (c1.dangerous)
c1.dangerous = 3
print (c1.dangerous)
print (c2.dangerous)
del c1.dangerous
print (c1.dangerous)
C.dangerous = 3
print (c2.dangerous)
```

*The output:*

In this code, `C` is a class that defines a class attribute called `dangerous`. A class attribute is a variable that is shared by all instances of the class.

We create two instances of the `C` class, `c1` and `c2`, and print the value of the `dangerous` attribute for each instance. Since the dangerous attribute is a class attribute, it has the same value for both `c1` and `c2`.

Next, we set the value of the `dangerous` attribute for `c1` to **`3`**. This creates an instance attribute for `c1` that shadows the class attribute of the same name. An instance attribute is a variable that is specific to a particular instance of a class, and it takes precedence over any class attributes of the same name.

We then print the value of the dangerous attribute for `c1` and `c2`. The value for `c1` is **`3`**, because it now has an instance attribute of that name, while the value for `c2` is still **`2`**, because it only has the class attribute of that name.

Next, we delete the instance attribute for `c1` using the del statement. This removes the instance attribute, revealing the underlying class attribute of the same name.

Finally, we set the value of the dangerous class attribute to **`3`**. This changes the value of the class attribute for all instances of the class, including `c2`. When we print the value of the dangerous attribute for `c2`, it is now **`3`**.

## 4- Why are functions considered first class objects in Python?

In Python, functions are considered first-class objects because they have the same properties as other objects in the language. Specifically, this means that functions can be:

 1. Assigned to variables and stored in data structures, just like any other object
 2. Passed as arguments to functions
 3. Returned as values from functions
 4. Defined inside other functions  
The ability to treat functions as first-class objects is a powerful feature of Python that enables a number of useful programming patterns, such as higher-order functions, decorators, and functional programming.

For example, consider the following code:

```python
def greet(name):
  return "Hello, " + name

greeting = greet
print(greeting("John"))  # prints "Hello, John"
```

In this code, we define a function called `greet` that takes a single argument and returns a string. We then assign the function to a variable called `greeting`, and call the `greeting` function just like we would call the `greet` function. This demonstrates how a function can be treated as a first-class object and assigned to a variable.

As another example, consider the following code:

```python
def apply_twice(func, arg):
  return func(func(arg))

def add_two(x):
  return x + 2

print(apply_twice(add_two, 10))  # prints 14
```

In this code, we define a function called `apply_twice` that takes another function as an argument and applies it twice to a given argument. We then define a function called `add_two` that adds two to its argument. We pass the `add_two` function to `apply_twice` as an argument, and it is used to increment the value of `10` by two twice, resulting in a final value of `14`. This demonstrates how a function can be passed as an argument to another function.

## 5- Do arguments in Python get passed by reference or by value?

In Python, arguments are passed by assignment. This means that when you pass an object to a function as an argument, a reference to the object is passed, rather than a copy of the object itself.

For immutable objects, such as numbers, strings, and tuples, this has the same behavior as passing by value. For example, consider the following code:

```python
def increment(x):
  x += 1

a = 10
increment(a)
print(a)  # prints 10
```

In this code, the `increment` function takes an argument `x` and increments it by `1`. However, when we pass the value `10` to the function as an argument and then print the value of `a`, it is still `10`. This is because the `increment` function operates on a copy of the value of `a`, rather than modifying the value of `a` itself.

For mutable objects, such as lists and dictionaries, passing by assignment has the same behavior as passing by reference. For example, consider the following code:

```python
def append_one(lst):
  lst.append(1)

a = [1, 2, 3]
append_one(a)
print(a)  # prints [1, 2, 3, 1]
```

In this code, the `append_one` function takes an argument `lst` and appends the value `1` to the end of the list. When we pass the list `[1, 2, 3]` to the function as an argument and then print the value of `a`, the list has been modified to include the value `1` at the end. This is because the `append_one` function operates on the original list, rather than a copy of the list.

It is important to understand how Python passes arguments when writing functions, as it can affect the behavior of your code. If you want to modify an object that you pass to a function and have the changes persist outside the function, you will need to use a mutable object such as a list or a dictionary. If you want to pass an object to a function and ensure that it is not modified, you should use an immutable object such as a number, string, or tuple.

## 6- What tools to use for linting, debugging, and profiling?

There are several tools available for linting, debugging, and profiling in Python. Here are a few popular options:

1. **Linting**: Linting is the process of checking code for syntax and style errors. A linting tool can help you identify and fix issues with your code before you run it. Some popular linting tools for Python include:
    * Pylint: A widely-used linting tool that can detect a wide range of issues in Python code, including syntax errors, style issues, and potential bugs.
    * Flake8: A popular linting tool that combines several other tools, including PyFlakes, pycodestyle, and McCabe.
    * PyCodeStyle (formerly known as pycodestyle): A linting tool that checks code for style issues, such as indentation, line length, and naming conventions.

2. **Debugging**: Debugging is the process of identifying and fixing errors in your code. Some popular tools for debugging Python code include:
    * PDB: The Python debugger is a built-in tool that allows you to step through your code, inspect variables, and set breakpoints.
    * IPython: An interactive Python shell that provides additional debugging features, such as tab completion, object introspection, and history.
    * PyCharm: An integrated development environment (IDE) that includes a powerful debugger and other debugging tools.

3. **Profiling**: ling is the process of measuring the performance of your code and identifying bottlenecks. Some popular tools for profiling Python code include:
    * cProfile: A built-in module that provides a simple interface for profiling Python code.
    * perf: A command-line tool that provides detailed performance information about Python programs.
    * Pyflame: A tool that generates a flame graph of Python program execution, showing where time is being spent.

## 7- Give an example of filter and reduce over an iterable object

Here is an example of using the `filter` and `reduce` functions to process an iterable object in Python:

```python
from functools import reduce

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter to select only even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # prints [2, 4, 6, 8, 10]

# Use reduce to compute the product of all even numbers
product = reduce(lambda x, y: x * y, even_numbers)
print(product)  # prints 3840

```

In this example, we define a list of numbers and use the `filter` function to select only the even numbers from the list. The `filter` function takes a function and an iterable as arguments and returns an iterator that yields the elements of the iterable for which the function returns `True`. In this case, we pass a `lambda` function that returns `True` if its argument is even and `False` otherwise, and we pass the list of numbers as the iterable.

We then use the `reduce` function from the `functools` module to compute the product of all the even numbers in the `list`. The `reduce` function takes a function and an iterable as arguments and applies the function to the elements of the iterable in a cumulative manner, returning a single result. In this case, we pass a lambda function that multiplies its arguments and pass the iterator returned by `filter` as the iterable.

Both `filter` and `reduce` are higher-order functions, meaning that they take a function as an `argument` and return a new function as a result. They are useful for concisely expressing complex operations on iterable objects in Python.

## 8- What are list and dict comprehensions?

List comprehensions and dictionary comprehensions are concise ways to create new lists and dictionaries, respectively, from existing iterable objects. They are a way to transform one list (or dictionary) into another list (or dictionary) by applying a certain operation to each element in the original list.  
A list comprehension consists of square brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses. The result is a new list that is computed by evaluating the expression in the context of the `for` and `if` clauses.

For example, suppose we have a list of numbers and we want to create a new list that contains only the even numbers from the original list. We could do this using a list comprehension as follows:

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
```

This would create a new list `even_numbers` containing only the even numbers from the original list `numbers`.

A dictionary comprehension is similar to a list comprehension, but it creates a new dictionary instead of a list. It consists of a dictionary key expression followed by a `for` clause, then zero or more `for` or `if` clauses. The result is a new dictionary that is computed by evaluating the key and value expressions in the context of the `for` and `if` clauses.

For example, suppose we have a list of strings and we want to create a new dictionary that maps each string to its length. We could do this using a dictionary comprehension as follows:

```python
strings = ['cat', 'dog', 'bird']
lengths = {s: len(s) for s in strings}
```

This would create a new dictionary `lengths` that maps each string to its length.

## 9- What do we mean when we say that a certain Lambda expression forms a closure?

A closure is a function that retains access to the variables in the environment in which it was defined, even after the code that defined the function has finished executing. This means that the function can still reference and modify the variables even if the function is called in a different context, such as in a different function or in a different part of the program.

In the context of lambda expressions, a lambda expression forms a closure if it references variables from the environment in which it was defined. For example, consider the following code:

```python
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)

```

Here, the `make_multiplier` function returns a lambda expression that takes a single argument `x` and returns `x * n`, where `n` is the argument passed to `make_multiplier`. The lambda expression formed by `make_multiplier` is a closure because it references the variable `n` from the environment in which it was defined, even though `make_multiplier` has already returned.

We can see this in action by calling the `lambda` expressions returned by `make_multiplier`:

```python
print(double(10))  # Output: 20
print(triple(10))  # Output: 30
```

The lambda expression returned by `make_multiplier(2)` multiplies its argument by `2`, while the lambda expression returned by `make_multiplier(3)` multiplies its argument by `3`. This is possible because the lambda expressions formed closures and retained access to the variables in the environment in which they were defined.

## 10- Name a few differences between Python 2.x and 3.x

1. *Print statement vs print function*: In Python 2.x, the `print` statement is used to print output, while in Python 3.x, the `print` function is used. For example:

    ```python
    # Python 2.x
    print "Hello, World!"

    # Python 3.x
    print("Hello, World!")

    ```

2. *Division operator*: In Python 2.x, the division operator (`/`) performs floor division for integers and float division for floating-point numbers. In Python 3.x, the division operator always performs float division.

    ```python
    # Python 2.x
    print(10 / 3)  # Output: 3
    print(10 / 3.0)  # Output: 3.3333333333333335

    # Python 3.x
    print(10 / 3)  # Output: 3.3333333333333335
    print(10 / 3.0)  # Output: 3.3333333333333335
    ```

3. *Exception handling*: In Python 2.x, the `except` statement can be used to catch exceptions of any type, while in Python 3.x, the `except` statement must specify the type of exception being caught.

    ```python
    # Python 2.x
    try:
        x = 1 / 0
    except:
        print("An exception occurred")

    # Python 3.x
    try:
        x = 1 / 0
    except Exception:
        print("An exception occurred")
    ```

4. *Iterators*: In Python 2.x, the `iteritems` method is used to iterate over the keys and values of a dictionary, while in Python 3.x, the `items` method is used.

    ```python
        # Python 2.x
    d = {'a': 1, 'b': 2}
    for key, value in d.iteritems():
        print(key, value)

    # Python 3.x
    d = {'a': 1, 'b': 2}
    for key, value in d.items():
        print(key, value)
    ```

5. *Unicode support*: In Python 2.x, Unicode support is not fully integrated, and the unicode and str types are separate. In Python 3.x, Unicode is fully integrated, and the str type is used for Unicode strings.

## 11- How is memory managed in python?

In Python, memory management is handled by the Python interpreter itself. When a Python program runs, the interpreter creates and manages a number of objects in memory to store the data used by the program. The interpreter also tracks the objects that are no longer being used and reclaims their memory, a process known as garbage collection.

One of the key features of Python's memory management is its use of reference counting to keep track of the objects that are being used by the program. When an object is created, the interpreter increments a reference count for that object. When the object is no longer needed, the reference count is decremented. When the reference count reaches zero, the interpreter knows that the object is no longer being used and can reclaim its memory.

Python also uses a technique called "generational garbage collection" to improve the efficiency of its garbage collection process. This involves dividing objects into different generations based on how long they have been in use. Newer objects are placed in a "young generation," while older objects are placed in an "old generation." The garbage collector focuses on the young generation first, since it is more likely to contain objects that are no longer being used. This helps to reduce the overall time required for garbage collection.

In addition to these techniques, Python also provides tools for controlling and monitoring the use of memory in a program. For example, the `sys.getsizeof()` function can be used to determine the size of an object in memory, and the `gc` module can be used to manually trigger garbage collection or to tune the garbage collection parameters.

## 12- What will be the output of the following code?

```python
_list = ['a', 'b', 'c', 'd', 'e']
print _list[10:]
```

*The output:*
the output will be an empty list `[]`.

The slicing syntax `list[start:end]` is used to retrieve a subset of the elements in a list. The `start` index specifies the index of the first element to retrieve, and the `end` index specifies the index of the element after the last element to retrieve. If you omit the `end` index, the slicing syntax will return all elements of the list starting from the `start` index until the end of the list.

In this case, the list `_list` has only five elements, so the valid indices are `0` through `4`. The index `10` is out of bounds for the list, so the slicing syntax _list`[10:]` will return an empty list.

## 13- A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers

```python
def is_palindrome(n):
    # Convert the number to a string and check if it is equal to its reverse
    return str(n) == str(n)[::-1]

largest_palindrome = 0

# Check the product of all pairs of 3-digit numbers
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        # If the product is a palindrome and is larger than the current largest palindrome, update the largest palindrome
        if is_palindrome(product) and product > largest_palindrome:
            largest_palindrome = product

print(largest_palindrome)
```

This code defines a function `is_palindrome` that takes a number and returns `True` if the number is a palindrome, and `False` otherwise. It does this by converting the number to a string and checking if the string is equal to its reverse.

The main part of the code then iterates over all pairs of 3-digit numbers and checks the product of each pair. If the product is a palindrome and is larger than the current largest palindrome, it updates the largest palindrome.

Finally, the code prints the largest palindrome.

This code should find the largest palindrome made from the product of two 3-digit numbers.

## 14- What is skeleton code in Python?

Skeleton code in Python is a basic set of code that provides a starting point for a new project. It typically includes a directory structure, basic configuration files, and a set of basic functions and structures that can be used as a foundation for building out the project.

Skeleton code is often used to provide a consistent structure and set of best practices for projects, making it easier to get started and avoid common pitfalls. It can also be used to demonstrate how to set up a basic project or to provide a starting point for learning a new programming concept or framework.

For example, a Python skeleton code might include:

* A directory structure for organizing code, tests, and documentation
* Basic configuration files, such as a `setup.py` file for packaging and distributing the project
* A `requirements.txt` file for specifying the project's dependencies
* A testing framework and sample test cases
* Documentation templates and guidelines

Skeleton code is often created for specific types of projects, such as web applications, command-line tools, or data science projects. There are many open-source skeleton code examples available online that you can use as a starting point for your own projects.

Using skeleton code can help you get started with a new project more quickly, and can provide a set of established best practices to follow as you develop your project. However, it's important to understand that skeleton code is only a starting point, and you will need to customize and adapt it to your specific needs as you develop your project.
