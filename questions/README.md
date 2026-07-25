# 100+ Python Interview Questions

## 1- Python uses a Global Interpreter Lock. Does that mean it doesn’t use actual threads?

No, Python uses actual threads, but the Global Interpreter Lock (GIL) is a mechanism that prevents multiple native threads from executing Python bytecodes at once. This lock is necessary because CPython, the reference implementation of Python, is not thread-safe, meaning that multiple threads can potentially interfere with each other and compromise the integrity of an application.

The GIL makes it easy to write simple, thread-safe Python programs. Still, it can also limit the performance of multithreaded programs, especially ones that rely heavily on CPU-bound operations. In these cases, Python's threading module may need to provide a different level of parallelism. In such cases, consider using an alternative implementation of Python that does not have a GIL, such as PyPy or Jython, or using a different parallel approach, such as the multiprocessing module or subprocesses.

## 2- Is it possible to have a producer thread reading from the network and a consumer thread writing to a file work in parallel? What about the GIL?

Yes, it is possible to have a producer thread that reads from the network and a consumer thread that writes to a file work in parallel in Python, even with the GIL in place. The GIL prevents multiple native threads from executing Python bytecodes simultaneously. It does not prevent threads from performing other operations, such as waiting for data to be available on a network socket or for a file to be written to disk.

With a producer thread reading from the network and a consumer thread writing to a file, the producer thread can block a network read operation, allowing the consumer thread to run. Similarly, the consumer thread can block a file write operation, allowing the producer thread to run. In this way, the two threads can effectively work in parallel, even though only one native thread executes Python bytecodes at a time due to the GIL.

It is important to note that the GIL can still limit the overall performance of a program that uses multiple threads, especially if the threads are CPU-bound. In such cases, consider using an alternative implementation of Python that does not have a GIL or using a different approach to parallelism, such as the multiprocessing module or using subprocesses.

## 3- What will be the output of the following code in each step?

```Python
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

_The output:_

In this code, `C` is a class that defines a class attribute called `dangerous`. A class attribute is a variable that is shared by all instances of the class.

We create two instances of the `C` class, `c1` and `c2`, and print the value of the `dangerous` attribute for each instance. Since the dangerous attribute is a class attribute, it has the same value for `c1` and `c2`.

Next, we set the value of the `dangerous` attribute for `c1` to **`3`**. This creates an instance attribute for `c1` that shadows the class attribute of the same name. An instance attribute is a variable specific to a particular instance of a class, and it takes precedence over any class attribute of the same name.

We then print the value of the dangerous attribute for `c1` and `c2`. The value for `c1` is **`3`** because it now has an instance attribute of that name, while the value for `c2` is still **`2`** because it only has the class attribute of that name.

Next, we delete the instance attribute for `c1` using the del statement. This removes the instance attribute, revealing the underlying class attribute of the same name.

Finally, we set the value of the dangerous class attribute to **`3`**. This changes the value of the class attribute for all class instances, including `c2`. When we print the value of the dangerous attribute for `c2`, it is now **`3`**.

## 4- Why are functions considered first-class objects in Python?

In Python, functions are considered first-class objects because they have the same properties as other objects in the language. Specifically, this means that functions can be:

1. Assigned to variables and stored in data structures, just like any other object
2. Passed as arguments to functions
3. Returned as values from functions
4. Defined inside other functions  
   The ability to treat functions as first-class objects is a powerful feature of Python that enables several functional programming patterns, such as higher-order functions, decorators, and functional programming.

For example, consider the following code:

```Python
def greet(name):
  return "Hello, " + name

greeting = greet
print(greeting("John"))  # prints "Hello, John"
```

In this code, we define a function called `greet` that takes a single argument and returns a string. We then assign the function to a variable called `greeting` and call the `greeting` function just like we would call the `greet` function. This demonstrates how a function can be treated as a first-class object and assigned to a variable.

As another example, consider the following code:

```Python
def apply_twice(func, arg):
  return func(func(arg))

def add_two(x):
  return x + 2

print(apply_twice(add_two, 10))  # prints 14
```

In this code, we define a function called `apply_twice` that takes another function as an argument and applies it twice to a given argument. We then define a function called `add_two` that adds two to its argument. We pass the `add_two` function to `apply_twice` as an argument, and it is used to increment the value of `10` by two twice, resulting in a final value of `14`. This demonstrates how a function can be passed as an argument to another function.

## 5- Do arguments in Python get passed by reference or value?

In Python, arguments are passed by object reference. This means that when you pass an object to a function, a reference to the object is passed rather than a copy of the object. The behavior depends on whether the object is mutable or immutable.

The function cannot modify the original object for immutable objects (e.g., numbers, strings, and tuples) because such objects cannot be changed. Instead, any operation that seems to "modify" the object creates a new object, leaving the original one unaffected. For example:

```Python
def increment(x):
  x += 1

a = 10
increment(a)
print(a)  # prints 10
```

Here, the variable `a` remains unchanged because the function increment works with a new reference to the value `11`, leaving the original value of `a` intact.

For mutable objects (e.g., lists and dictionaries), the function operates on the original object because the reference to the same object is passed. For example:

```Python
def append_one(lst):
  lst.append(1)

a = [1, 2, 3]
append_one(a)
print(a)  # prints [1, 2, 3, 1]
```

In this code, the `append_one` function takes an argument `lst` and appends the value `1` to the end of the list. When we pass the list `[1, 2, 3]` to the function as an argument and then print the value of `a`, the list has been modified to include the value `1` at the end. This is because the `append_one` function operates on the original list rather than a copy of the list.

It is crucial to understand how Python passes arguments when writing functions, as it can affect the behavior of your code. If you want to modify an object that you pass to a function and have the changes persist outside the function, you must use a mutable object such as a list or a dictionary. If you want to pass an object to a function and ensure that it is not modified, you should use an immutable object such as a number, string, or tuple.

## 6- What tools to use for linting, debugging, and profiling?

Several tools are available for linting, debugging, and profiling in Python. Here are a few popular options:

1. **Linting**: Linting checks code for syntax and style errors. A linting tool can help you identify and fix issues with your code before you run it. Some popular linting tools for Python include:

   - Pylint: A widely-used linting tool that can detect various issues in Python code, including syntax errors, style issues, and potential bugs.
   - Flake8: A popular linting tool that combines several other tools, including `PyFlakes`, `pycodestyle`, and `McCabe`.
   - pycodestyle (formerly known as `pep8`): A linting tool that checks code for style issues, such as indentation, line length, and naming conventions.

2. **Debugging**: Debugging is the process of identifying and fixing errors in your code. Some popular tools for debugging Python code include:

   - PDB: The Python debugger is a built-in tool that allows you to step through your code, inspect variables, and set breakpoints.
   - IPython: An interactive Python shell that provides additional debugging features, such as tab completion, object introspection, and history.
   - PyCharm: An integrated development environment (IDE) with a powerful debugger and other tools.

3. **Profiling**: is the process of measuring the performance of your code and identifying bottlenecks. Some popular tools for profiling Python code include:
   - cProfile: A built-in module that provides a simple interface for profiling Python code.
   - perf: A command-line tool that provides detailed performance information about Python programs.
   - Pyflame: A tool that generates a flame graph of Python program execution, showing where time is being spent.

## 7- Give an example of filter and reduce over an iterable object

Here is an example of using the `filter` and `reduce` functions to process an iterable object in Python:

```Python
from functools import reduce

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter to select only even numbers
# filter returns a lazy iterator, so wrap it in list() to be able to reuse it below
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # prints [2, 4, 6, 8, 10]

# Use reduce to compute the product of all even numbers
product = reduce(lambda x, y: x * y, even_numbers)
print(product)  # prints 3840
```

In this example, we define a list of numbers and use the `filter` function to select only the even numbers from the list. The `filter` function takes a function and an iterable as arguments and returns an iterator that yields the elements of the iterable for which the function returns `True`. In this case, we pass a `lambda` function that returns `True` if its argument is even and `False` otherwise, and we pass the list of numbers as the iterable.

We then use the `reduce` function from the `functools` module to compute the product of all the even numbers in the `list`. The `reduce` function takes a function and an iterable as arguments and applies the function to the elements of the iterable in a cumulative manner, returning a single result. In this case, we pass a lambda function that multiplies its arguments and pass the list of even numbers as the iterable.

Note the `list()` call around `filter`. In Python 3 `filter` returns a lazy iterator that can only be consumed once. Had we kept the raw iterator and printed it with `print(list(even_numbers))` first, that call would have exhausted it, and the later `reduce` would raise `TypeError: reduce() of empty iterable with no initial value` instead of returning `3840`. This one-shot behaviour of iterators is a common interview gotcha.

Both `filter` and `reduce` are higher-order functions, meaning they take another function as an argument. (A higher-order function is one that takes a function as an argument, returns a function, or both — `filter` returns an iterator and `reduce` returns a single accumulated value, so neither returns a new function here.) They are helpful for concisely expressing complex operations on iterable objects in Python.

## 8- What are `list` and `dict` comprehensions?

List comprehensions and dictionary comprehensions are concise ways to create new lists and dictionaries, respectively, from existing iterable objects. They are a way to transform one list (or dictionary) into another list (or dictionary) by applying a specific operation to each element in the original list.  
A list comprehension consists of square brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses. The result is a new list computed by evaluating the expression in the context of the `for` and `if` clauses.

For example, suppose we have a list of numbers, and we want to create a new list that contains only the even numbers from the original list. We could do this using a list comprehension as follows:

```Python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
```

This would create a new list `even_numbers` containing only the even numbers from the original list `numbers`.

A dictionary comprehension is similar to list comprehension, but it creates a new dictionary instead of a list. It consists of a dictionary key expression followed by a `for` clause, then zero or more `for` or `if` clauses. The result is a new dictionary computed by evaluating the key and value expressions in the context of the `for` and `if` clauses.

For example, suppose we have a list of strings, and we want to create a new dictionary that maps each string to its length. We could do this using a dictionary comprehension as follows:

```Python
strings = ['cat', 'dog', 'bird']
lengths = {s: len(s) for s in strings}
```

This would create a new dictionary `lengths` that maps each string to its length.

## 9- What do we mean when we say that a specific Lambda expression forms a closure?

A closure is a function that retains access to the variables in the environment it was defined, even after the code that defined the function has finished executing. This means that the function can still reference and modify the variables even if the function is called in a different context, such as in a different function or a different part of the program.

In the context of lambda expressions, a lambda expression forms a closure if it references variables from the environment in which it was defined. For example, consider the following code:

```Python
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)

```

Here, the `make_multiplier` function returns a lambda expression that takes a single argument `x` and returns `x * n`, where `n` is the argument passed to `make_multiplier`. The lambda expression formed by `make_multiplier` is a closure because it references the variable `n` from the environment in which it was defined, even though `make_multiplier` has already returned.

We can see this in action by calling the `lambda` expressions returned by `make_multiplier`:

```Python
print(double(10))  # Output: 20
print(triple(10))  # Output: 30
```

The lambda expression returned by `make_multiplier(2)` multiplies its argument by `2`, while the lambda expression returned by `make_multiplier(3)` multiplies its argument by `3`. This is possible because the lambda expressions formed closures and retained access to the variables in the environment in which they were defined.

## 10- Name a few differences between Python 2.x and 3.x

1. _Print statement vs print function_: In Python 2.x, the `print` statement is used to print output, while in Python 3.x, the `print` function is used. For example:

   ```Python
   # Python 2.x
   print "Hello, World!"

   # Python 3.x
   print("Hello, World!")

   ```

2. _Division operator_: In Python 2.x, the division operator (`/`) performs floor division for integers and float division for floating-point numbers. In Python 3.x, the division operator always performs float division.

   ```Python
   # Python 2.x
   print(10 / 3)  # Output: 3
   print(10 / 3.0)  # Output: 3.3333333333333335

   # Python 3.x
   print(10 / 3)  # Output: 3.3333333333333335
   print(10 / 3.0)  # Output: 3.3333333333333335
   ```

3. _Exception handling_: In Python 2.x, the exception instance is bound with a comma (`except ValueError, e:`), while Python 3.x requires the `as` keyword (`except ValueError as e:`). A bare `except:` that catches every exception type remains valid in both versions, although catching a specific type is the recommended practice.

   ```Python
   # Python 2.x
   try:
       x = 1 / 0
   except ZeroDivisionError, e:
       print("An exception occurred: %s" % e)

   # Python 3.x
   try:
       x = 1 / 0
   except ZeroDivisionError as e:
       print("An exception occurred: {}".format(e))
   ```

4. _Iterators_: In Python 2.x, the `iteritems` method is used to iterate over the keys and values of a dictionary, while in Python 3.x, the `items` method is used.

   ```Python
       # Python 2.x
   d = {'a': 1, 'b': 2}
   for key, value in d.iteritems():
       print(key, value)

   # Python 3.x
   d = {'a': 1, 'b': 2}
   for key, value in d.items():
       print(key, value)
   ```

5. _Unicode support_: In Python 2.x, Unicode support is not fully integrated, and the Unicode and str types are separate. In Python 3.x, Unicode is fully integrated, and the str type is used for Unicode strings.

## 11- How is memory managed in Python?

In Python, memory management is handled by the Python interpreter itself. When a Python program runs, the interpreter creates and manages several objects in memory to store the data used by the program. The interpreter also tracks the objects that are no longer being used and reclaims their memory, a process known as garbage collection.

One of the critical features of Python's memory management is its use of reference counting to keep track of the objects the program uses. When an object is created, the interpreter increments a reference count for that object. When the object is no longer needed, the reference count is decremented. When the reference count reaches zero, the interpreter knows the object is no longer being used and can reclaim its memory.

Python also uses a technique called "generational garbage collection" to improve the efficiency of its garbage collection process. This involves dividing objects into different generations based on how long they have been in use. Newer objects are placed in a "young generation," while older objects are placed in an "old generation." The garbage collector focuses on the young generation first since it is more likely to contain objects no longer being used. This helps to reduce the overall time required for garbage collection.

In addition to these techniques, Python also provides tools for controlling and monitoring the use of memory in a program. For example, the `sys.getsizeof()` function can be used to determine the size of an object in memory, and the `gc` module can be used to trigger garbage collection manually or to tune the garbage collection parameters.

## 12- What will be the output of the following code?

```Python
_list = ['a', 'b', 'c', 'd', 'e']
print(_list[10:])
```

_The output:_
the output will be an empty list `[]`.

The slicing syntax `list[start: end]` retrieves a subset of the elements in a list. The `start` index specifies the index of the first element to retrieve, and the `end` index specifies the element's index after the last element to retrieve. If you omit the `end` index, the slicing syntax will return all elements of the list, starting from the `start` index until the end of the list.

In this case, the list `_list` has only five elements, so the valid indices are `0` through `4`. The index `10` is out of bounds for the list, so the slicing syntax `_list[10:]` will return an empty list.

## 13- A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers

```Python
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

This code defines a function `is_palindrome` that takes a number and returns `True` if the number is a palindrome and `False` otherwise. It does this by converting the number to a string and checking if the string is equal to its reverse.

The central part of the code then iterates over all pairs of 3-digit numbers and checks the product of each pair. If the product is a palindrome and is larger than the current largest palindrome, it updates the largest palindrome.

Finally, the code prints the largest palindrome.

This code should find the largest palindrome made from the product of two 3-digit numbers.

## 14- What is skeleton code in Python?

Skeleton code in Python is a basic set of code that provides a starting point for a new project. It typically includes a directory structure, basic configuration files, and a set of essential functions and structures that can be used as a foundation for building out the project.

Skeleton code is often used to provide a consistent structure and set of best practices for projects, making it easier to get started and avoid common pitfalls. It can also be used to demonstrate how to set up a basic project or to provide a starting point for learning a new programming concept or framework.

For example, a Python skeleton code might include:

- A directory structure for organizing code, tests, and documentation
- Basic configuration files, such as a `setup.py` file for packaging and distributing the project
- A `requirements.txt` file for specifying the project's dependencies
- A testing framework and sample test cases
- Documentation templates and guidelines

Skeleton code is often created for specific types of projects, such as web applications, command-line tools, or data science projects. There are many open-source skeleton code examples available online that you can use as a starting point for your projects.

Using skeleton code can help you get started with a new project more quickly and can provide a set of established best practices to follow as you develop your project. However, it's important to understand that skeleton code is only a starting point, and you will need to customize and adapt it to your specific needs as you develop your project.

## 15- In Python classes, what is the difference between class methods and static methods? and when to use them

In Python, a class method is a method that is bound to the class and not the instance of the class. A class method can be called on the class itself, as well as on any instance of the class. A class method is defined using the `@classmethod` decorator, and it takes the class as its first argument, conventionally named `cls`.

A static method is also bound to the class rather than to an instance, but unlike a class method it receives no implicit first argument at all — neither `self` nor `cls`. It behaves like a plain function that happens to live in the class namespace. A static method is defined using the `@staticmethod` decorator.

Here's an example of how to define and use class methods and static methods in Python:

```Python
class MyClass:
    def __init__(self, value):
        self.value = value

    @classmethod
    def class_method(cls, arg):
        # do something with the class and the arg
        return arg

    @staticmethod
    def static_method(arg):
        # do something with the arg
        return arg

# Call a class method
result = MyClass.class_method("hello")

# Call a static method
result = MyClass.static_method("hello")

# Call a class method on an instance of the class
obj = MyClass(42)
result = obj.class_method("hello")

# Call a static method on an instance of the class
result = obj.static_method("hello")
```

In general, you should use **_class methods_** when defining a method that operates on the class itself rather than on an instance of the class. An example of this might be a factory method that creates a new class instance with some default values. You should use **_static methods_** when you need to define a method that operates on an argument or variables that are independent of the class and its instances. An example of this might be a utility function that performs some computation or transformation on its arguments but does not need to access any class or instance attributes.

## 16- Please explain the following results of the code executed on a Python shell interpreter

```Python
>>> a=256
>>> b=256
>>> a is b
True
>>> x=257
>>> y=257
>>> x is y
False
```

_The output:_

This is because of the integer caching mechanism in Python. To save time and memory costs, Python always pre-loads all the small integers in the range of [-5, 256].

Therefore, all the integers in [-5, 256] have been already saved in the memory. When a new integer variable in this range is declared, Python just references the cached integer to it and won’t create any new object.

Therefore, the explanations of the results are:

- When the variables `a` and `b` were assigned to 256, they were referenced to the same memory location where the 256 was stored. They pointed to the same object.
- When the variables `x` and `y` were assigned to 257, they were two different objects in different memory locations because 257 is not on the small integers caching range.

Since the `is` operator is to compare the memory locations of two variables, the `a is b` should output `True`, and the `x is y` should output `False`.

## 17- In objective-oriented programming, there is a concept called abstract classes. How to implement it?

In Python, an abstract class is a class that has one or more abstract methods. An abstract method is a method that has a declaration, but no implementation. Abstract methods are defined using the `abc` (abstract base class) module, which is part of the Python standard library.

To create an abstract class in Python, you need to do the following:

1. Import the abc module.
2. Create a class that derives from abc.ABC.
3. Declare one or more abstract methods using the `@abc.abstractmethod` decorator.
   Here is an example of an abstract class in Python:

   ```Python
   import abc

   class Animal(abc.ABC):
       @abc.abstractmethod
       def make_sound(self):
           pass

   class Dog(Animal):
       def make_sound(self):
           print("Woof!")

   class Cat(Animal):
       def make_sound(self):
           print("Meow!")

   dog = Dog()
   dog.make_sound()  # Output: "Woof!"

   cat = Cat()
   cat.make_sound()  # Output: "Meow!"
   ```

In this example, the `Animal` class is an abstract class because it has an abstract method called `make_sound()`. The `Dog` and `Cat` classes are concrete classes because they provide an implementation for the `make_sound()` method. The `dog` and `cat` objects are instances of the `Dog` and `Cat` classes, respectively, and they can be used to call the `make_sound()` method.

## 18- What are `*args` and `**kwargs` in Python

In Python, the `*args` and `**kwargs` syntax is used to pass a variable number of arguments to a function.

`*args` is used to pass a variable number of non-keyworded arguments to a function. It is used to pass a tuple of arguments to the function. For example:

```Python
def my_function(arg1, *args):
    print(arg1)
    print(args)

my_function(1, 2, 3, 4, 5)

# Output:
# 1
# (2, 3, 4, 5)
```

`**kwargs` is used to pass a variable number of keyworded arguments to a function. It is used to pass a dictionary of keyword arguments to the function. For example:

```Python
def my_function(**kwargs):
    print(kwargs)

my_function(arg1=1, arg2=2, arg3=3)

# Output: {'arg1': 1, 'arg2': 2, 'arg3': 3}
```

Both `*args` and `**kwargs` are commonly used in Python to allow a function to accept a variable number of arguments. They can be useful when you want to write a function that can be flexible and handle a wide range of input parameters.

## 19- What is the difference between tuples, sets, and lists in Python?

In Python, tuples, sets, and lists are all data types that can be used to store collections of items. Here are the main differences between them:

1. **Tuples** are immutable, which means that you cannot modify the values of the items in a tuple once it has been created. They are defined using parentheses `()` and their items are separated by commas. also, tuples are generally faster and use less memory than lists, because they do not have the overhead of the extra methods and behaviors that are associated with lists. However, the difference in performance between tuples and lists is usually small and may not be noticeable in most cases.

2. **Sets** are mutable, but unlike lists they do not have a specific order and do not allow duplicate items. Sets are defined using curly braces `{}` and their items are separated by commas — note that `{}` on its own creates an empty dictionary, so use `set()` for an empty set. You can add and remove items after creation with `add()`, `remove()`, and `discard()`. Sets provide much faster membership tests (`x in s`) than lists, because they are implemented using a hash table data structure, which allows for efficient insertion, deletion, and lookup of items. Their items must be hashable, which means a set can hold tuples but not lists or other sets. If you need an immutable, hashable set, use `frozenset` instead. However, sets do not maintain the order of their items, which can be a drawback if you need to preserve the order of the items in your collection.

3. **Lists** are mutable, which means that you can change the values of their items after the list has been created. They are defined using square brackets `[]` and their items are separated by commas. also, Lists are generally slower and use more memory than tuples, because they are mutable and have the overhead of the extra methods and behaviors that are associated with them. However, lists are more flexible than tuples because you can modify their items after the list has been created.

```Python
# Create a tuple
t = (1, 2, 3)

# Create a set
s = {3, 6, 9}

# Create a list
l = [1, 2, 3]

# Modify a value at an index in a list (not possible for tuples, which are
# immutable, nor for sets, which are unordered and cannot be indexed)
l[1] = 4

# Add an item to a list (not possible for tuples, which are immutable)
l.append(5)

# Sets are mutable too, but they are unordered, so items are added with add()
s.add(12)
s.discard(3)

# A frozenset is the immutable counterpart of a set
fs = frozenset([3, 6, 9])
```

Tuples are generally used when you want to store a collection of items that should not be modified, lists when you need an ordered collection that you want to be able to modify, and sets when you need fast membership tests and automatic removal of duplicates and do not care about order.

## 20- What are pickling and unpickling in Python?

In Python, "pickling" refers to the process of converting an object hierarchy (e.g., a list, dictionary, or a user-defined object) into a byte stream, and "unpickling" refers to the process of reconstructing the object hierarchy from the byte stream.

The `pickle` module in Python provides functions for pickling and unpickling objects. To pickle an object, you can use the `pickle.dump` function, which takes the object to be pickled and a file-like object (such as a file or a byte stream) as arguments and writes the pickled object to the file-like object. To unpickle an object, you can use the `pickle.load` function, which takes a file-like object as an argument and returns the unpickled object.

Here is an example of how to use the `pickle` module to pickle and unpickle a simple object in Python:

```Python
import pickle

# Define a simple object to be pickled
data = {'a': [1, 2.0, 3, 4+6j],
        'b': ('string', u'Unicode string'),
        'c': None}

# Pickle the object
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# Unpickle the object
with open('data.pkl', 'rb') as f:
    data_loaded = pickle.load(f)
```

Pickling is useful for storing complex objects in a file or for sending them over a network connection. However, it is important to note that the pickle module is not intended to be secure, and it is possible to construct malicious pickle data that can execute arbitrary code when unpickled. Therefore, it is generally not recommended to use pickle to serialize and transmit sensitive data over untrusted networks or to unserialize pickle data from untrusted sources.

## 21- Does Python support multiple inheritance?

Yes, Python supports multiple inheritance, which means that a class can inherit from multiple superclasses (also called base classes or parent classes). Multiple inheritance can be useful when you want to define a class that inherits behavior from more than one parent class.

To use multiple inheritance in Python, you can specify multiple superclasses in the class definition, separated by commas. For example:

```Python
class Base1:
    # Base1 class definition
    pass

class Base2:
    # Base2 class definition
    pass

class Derived(Base1, Base2):
    # Derived class definition
    pass
```

In this example, the `Derived` class inherits from both the `Base1` and `Base2` classes.

Note that a class body cannot be empty in Python, which is why each class above uses `pass`; a comment alone is not enough and raises an `IndentationError`.

It is important to note that Python uses a method resolution order (MRO) to determine which method should be called when a method with the same name is inherited from multiple superclasses. The MRO is computed with the C3 linearisation algorithm. It respects the order in which the superclasses are listed, but it also guarantees that a class always appears before its own parents, so it is not a simple left-to-right search. You can inspect it at any time with `ClassName.__mro__` or `ClassName.mro()`:

```Python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print([cls.__name__ for cls in D.__mro__])
# Output: ['D', 'B', 'C', 'A', 'object']
```

Here `A` comes after both `B` and `C`, even though `B` inherits from `A`, because C3 places every class ahead of its ancestors.

For more information about multiple inheritance in Python, you can refer to the documentation on class inheritance in the Python tutorial.

## 22- What are the pitfalls and problems of Python language?

Performance and concurrency are two common areas where Python programmers may encounter pitfalls and problems. Here are some specific issues to consider in these areas:

1. **_Performance issues_**: Python is generally slower than compiled languages like C or C++, which means that you may encounter performance issues when running computationally intensive tasks in Python. There are ways to improve the performance of Python code (e.g., using optimized libraries or writing code in Cython), but it is important to be aware of the performance limitations of the language.

2. **_Concurrency issues_**: Python has a global interpreter lock (GIL) that prevents multiple threads from executing Python bytecodes at the same time, which can lead to concurrency issues when running multithreaded programs. There are ways to work around the GIL (e.g., using the `multiprocessing` module), but it is important to be aware of this limitation when writing concurrent programs in Python.

Here are some specific issues that you may encounter when dealing with performance and concurrency in Python:

- **Bottlenecks**: It can be difficult to identify which parts of your code are causing performance issues, especially if you are working with large datasets or complex algorithms. You may need to use profiling tools to identify bottlenecks in your code and optimize the most critical parts.

- **Memory usage**: Memory usage can also be a problem when working with large datasets or complex algorithms in Python. You may need to use memory-efficient data structures and algorithms, or write code in a memory-efficient way, to avoid running out of memory.

- **Lack of parallelism**: Because of the GIL, Python threads are not always able to run in parallel on multiple CPU cores. This can limit the scalability of multithreaded Python programs, especially on systems with many CPU cores.

- **Synchronization issues**: When working with concurrent programs, you may need to synchronize access to shared resources to avoid race conditions and other synchronization issues. This can be challenging in Python, especially if you are not familiar with the tools and techniques available for concurrency control.

To avoid these and other issues related to performance and concurrency in Python, it is important to be aware of the limitations of the language and to plan accordingly when writing and testing your code. You may need to use specialized tools and techniques, such as profiling and optimization tools, to improve the performance and scalability of your Python programs.

## 23- How to achieve multithreading in Python?

Multithreading in Python is achieved with the built-in `threading` module, either by instantiating `threading.Thread` with a target callable or by using `concurrent.futures.ThreadPoolExecutor` for a higher-level pool interface.

```Python
import threading

def worker(name):
    print(f"worker {name} running")

threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]

for t in threads:
    t.start()   # begin execution

for t in threads:
    t.join()    # wait for completion
```

The same thing with a pool, which handles starting and joining for you:

```Python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(worker, range(3)))
```

It is important to understand what this does and does not buy you. Because of the Global Interpreter Lock, only one thread executes Python bytecode at a time, so threads take rapid turns rather than truly running Python code in parallel on multiple cores. This means threading does **not** speed up CPU-bound work such as number crunching, and may even slow it down slightly because of the switching overhead.

Threads are still very effective for I/O-bound work — reading from the network, querying a database, or writing files — because a thread releases the GIL while it waits on I/O, allowing other threads to run. For CPU-bound work, use the `multiprocessing` module or `ProcessPoolExecutor` instead, which run separate processes each with their own interpreter and GIL.

## 24- What is the use of `with` in Python?

In Python, the with statement is used to wrap the execution of a block of code with methods defined by a context manager. A context manager is an object that defines the methods `__enter__` and `__exit__`, which are called before and after the execution of the block of code, respectively.

The `with` statement is used to manage resources that need to be acquired and released, such as file handles or network connections. It is particularly useful when working with resources that need to be closed or released after they are no longer needed because it ensures that the resources are properly cleaned up even if an exception is raised during the execution of the block of code.

Here is an example of how to use the `with` statement to open and read a file in Python:

```Python
with open('filename.txt', 'r') as f:
    contents = f.read()

# the file is closed automatically here, even if f.read() raised an exception
```

Without the `with` statement you would have to release the resource yourself in a `try`/`finally` block. The following code is equivalent to the example above, which shows what `with` saves you from writing:

```Python
f = open('filename.txt', 'r')
try:
    contents = f.read()
finally:
    f.close()
```

You can also write your own context manager, either by implementing `__enter__` and `__exit__` on a class or by using the `@contextlib.contextmanager` decorator:

```Python
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"acquiring {name}")
    resource = {"name": name}
    try:
        yield resource          # the value bound by "as"
    finally:
        print(f"releasing {name}")

with managed_resource("db connection") as res:
    print(f"using {res['name']}")
```

## 25- How are `.py`, `.pyi`, `.pyd`, and `.pyc` files different?

In Python, there are several different file types that you may encounter when working with the language:

1. **`.py`** files are Python source files that contain the code written in the Python language. These files can be executed by the Python interpreter, and they can be imported as modules in other Python programs.

2. **`.pyi`** files are Python interface files that contain type hints for Python programs. These files are used to provide type information for static type checkers, such as `mypy`, and they are not intended to be executed by the Python interpreter.

3. **`.pyd`** files (also known as Python dynamic libraries) are compiled binary files that contain compiled code written in C, C++, or other languages that can be imported and used by Python programs. These files are typically used to extend the functionality of Python by providing access to compiled code that is not written in Python.

4. **`.pyc`** files are compiled Python bytecode files that contain the bytecode version of Python source files. These files are not intended to be edited by hand and are usually generated automatically by the Python interpreter when a Python module is imported.

Here is an example of how these file types may be used in a Python program:

```Python
# foo.py
def foo():
    print("Hello from foo")

# bar.py
import foo
foo.foo()
```

In this example, `foo.py` is a Python source file that defines a function called `foo`. `bar.py` is another Python source file that imports the `foo` module and calls the `foo` function. When `bar.py` is executed, the Python interpreter compiles the imported module to bytecode and caches it (if a current cached copy does not already exist), then executes that bytecode. In Python 3 this cache is not written next to the source as `foo.pyc`; it goes into a `__pycache__` directory with the interpreter version in the name, for example `__pycache__/foo.cpython-312.pyc`. Note that only imported modules are cached this way — the script you run directly is not.

## 26- What are decorators in Python?

Decorators are functions that are used to modify the behavior of other functions. Decorators are implemented as functions that take a function as an argument and return a modified function. They are often used to add additional functionality to an existing function, such as logging, caching, or input validation.

To use a decorator in Python, you define a decorator function and use the `@` symbol to specify that the function being defined is a decorator. The function being decorated is passed as an argument to the decorator function, and the decorator function returns the modified function.

Here is an example of how to use a decorator in Python:

```Python
import functools

def my_decorator(func):
    @functools.wraps(func)          # preserves func's name, docstring and signature
    def wrapper(*args, **kwargs):
        print("Before calling the decorated function")
        result = func(*args, **kwargs)
        print("After calling the decorated function")
        return result
    return wrapper

@my_decorator
def my_function(x, y):
    """Add two numbers."""
    return x + y

print(my_function(3, 4))   # 7
print(my_function.__name__)  # 'my_function'
```

In this example, the `my_decorator` function is a decorator that adds additional logging before and after the decorated function is called. The `my_function` function is decorated with the `my_decorator` decorator, which modifies its behavior to include the additional logging.

Two points are worth getting right, because they are common interview follow-ups:

- **`@my_decorator` is just syntactic sugar for `my_function = my_decorator(my_function)`.** The decorator itself runs **once, at definition time**, not on every call. What runs on every call is the `wrapper` function it returned. So the decorated name is rebound to `wrapper`, and calling `my_function(3, 4)` really calls `wrapper(3, 4)`, which in turn calls the original function.

- **Always apply `functools.wraps`.** Without it the wrapper replaces the original's metadata, so `my_function.__name__` would be `'wrapper'`, the docstring would be lost, and tooling such as `help()`, debuggers, and documentation generators would report the wrong thing. `functools.wraps` copies `__name__`, `__doc__`, `__module__`, `__qualname__`, and sets `__wrapped__` so the original is still reachable.

Decorators are not limited to plain functions. A decorator can also take arguments (which requires an extra level of nesting, a function returning a decorator), be implemented as a class that defines `__call__`, or be applied to a class rather than a function. The standard library uses all of these: `functools.lru_cache`, `functools.cached_property`, `dataclasses.dataclass`, and `staticmethod` / `classmethod` / `property` are all decorators.

## 27- How to use `self` in Python?

In Python, the `self` keyword is used to refer to the current instance of a class. It is used inside the methods of a class to access instance variables and instance methods.

Here is an example of how to use `self` in a class definition in Python:

```Python
class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value

obj = MyClass(10)
print(obj.my_method())
```

In this example, the `MyClass` class defines an `__init__` method that takes an argument value and assigns it to the instance variable `self.value`. The `my_method` method returns the value of self.value.

When the `MyClass` class is instantiated with the `MyClass(10)` statement, a new instance of the class is created, and the `__init__` method is called to initialize the instance. The `obj` variable is assigned to the new instance of the class, and the `obj.my_method()` statement calls the `my_method` method on the instance, which returns the value of self.value.

It is important to note that the `self` keyword is not a reserved word in Python and it is not required to use it in your code. However, it is a common convention in Python to use `self` to refer to the current instance of a class, and it is recommended to follow this convention when writing Python code.

## 28- What are namespaces in Python?

In Python, a namespace is a container that holds a set of identifiers (i.e., names) and their corresponding objects. Namespaces are used to avoid name collisions between identifiers that have the same name but are used in different contexts.

There are several types of namespaces in Python:

- **Module namespace**: Each module in Python has its own namespace, which contains the identifiers defined in the module, such as functions, variables, and classes. When you import a module, the identifiers in the module's namespace become available in the current namespace.

- **Class namespace**: Each class in Python has its own namespace, which contains the identifiers defined in the class body, such as methods and class attributes.

- **Instance namespace**: Each instance has its own namespace, held in its `__dict__`. Attributes assigned through `self` (for example `self.z = 30`) live here, not in the class namespace. This is why two instances can hold different values for the same attribute name.

- **Function (local) namespace**: Each call to a function creates its own namespace, which contains local variables and function arguments. It is created when the function is called and destroyed when the function returns.

- **Built-in namespace**: This contains the names that are always available, such as `len`, `print`, and `ValueError`. It is created when the interpreter starts and lasts until it exits.

Name lookup follows the **LEGB rule**, searching in this order: **L**ocal, then **E**nclosing (the scope of any enclosing function), then **G**lobal (module level), then **B**uilt-in. The first match wins, and a `NameError` is raised if the name is found nowhere.

Here is an example of how namespaces are used in Python:

```Python
# Define a global variable in the module namespace
x = 10

def foo():
    # Define a local variable in the function namespace
    y = 20
    print(x)   # 10 - found in the global namespace via LEGB
    print(y)   # 20 - found in the local namespace

def outer():
    e = "enclosing"
    def inner():
        print(e)   # 'enclosing' - found in the enclosing namespace
    inner()

class MyClass:
    class_attr = "shared"        # lives in the CLASS namespace

    def __init__(self):
        self.z = 30              # lives in the INSTANCE namespace

    def my_method(self):
        print(self.z)

foo()
outer()

obj = MyClass()
obj.my_method()                  # 30

print(obj.__dict__)              # {'z': 30}          <- instance namespace
print(MyClass.__dict__['class_attr'])  # 'shared'     <- class namespace
print(len)                       # <built-in function len>
```

In this example, `x` is defined in the module namespace and is accessible from the global scope and from inside `foo`. `y` is local to `foo` and is not accessible outside it. `e` lives in the enclosing namespace of `inner`. `class_attr` belongs to the class namespace and is shared by every instance, whereas `z` belongs to the individual instance's namespace, which is why it appears in `obj.__dict__` rather than in `MyClass.__dict__`.

## 29- What is PEP?

PEP stands for _Python Enhancement Proposal_. PEPs are documents that describe proposed changes, improvements, and new features for Python. They are written by Python developers and are used to communicate ideas and proposals for improving the language to the Python community.

There are different types of PEPs, including:

- **Standards Track PEPs**: These PEPs propose changes to the Python language itself, such as new syntax or built-in functions.

- **Informational PEPs**: These PEPs provide information about Python-related topics, such as best practices or design patterns.

- **Process PEPs**: These PEPs describe changes to the Python development process, such as how PEPs are submitted and reviewed.

PEPs are written in a standard format and are reviewed by the Python community through a process called the PEP process. The PEP process is designed to ensure that proposed changes to Python are well-documented, well-reasoned, and discussed by the community before being accepted and implemented.

## 30- What are dunder methods in Python?

In Python, dunder methods (also known as "magic methods") are methods that are defined with double underscores (e.g., `__init__`, `__len__`) and are used to implement special behavior for objects. These methods are called "dunder" because they are surrounded by double underscores (i.e., "double underscore" or "dunder").

Dunder methods are used to define the behavior of various built-in operations in Python, such as arithmetic operations, attribute access, and object creation and destruction. For example, the `__init__` dunder method is used to initialize an object when it is created, and the `__add__` dunder method is used to define the behavior of the `+` operator for an object, and the `__str__` dunder method is used to define the string representation of an object.

Here is an example of how dunder methods are used in Python:

```Python
class MyClass:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __str__(self):
        return f"MyClass({self.value})"

obj1 = MyClass(10)
obj2 = MyClass(20)
print(obj1 + obj2)  # Calls the __add__ method
print(str(obj1))   # Calls the __str__ method

```

In this example, the `MyClass` class defines the `__init__`, `__add__`, and `__str__` dunder methods to customize the behavior of object creation, the `+` operator, and the `str` function for instances of the class.

For more information about dunder methods and how they are used in Python, you can refer to the documentation.

## 31- What does `super` do in Python? and what is the difference between `super().__init__()` and explicit `superclass.__init__()`

`super()` returns a proxy object that delegates method calls to the **next class in the method resolution order (MRO)**, starting after the current class. In the common case of single inheritance that next class is simply the parent, which is why `super()` is usually described as "referring to the parent class" — but that description is a simplification that breaks down under multiple inheritance, and the distinction is the whole point of this question.

When you use `super().__init__()` in a child class, you are calling the `__init__` of whichever class comes next in the MRO of the _actual_ object being constructed.

For example, consider the following code:

```Python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

cat1 = Cat("Kitty", "Siamese", "Ball")
```

In this example, the `Cat` class is a child class of the `Animal` class. The `Cat` class has its own `__init__` method, which calls the `__init__` method of the `Animal` class using `super().__init__(name, species="Cat")`, setting the `name` and `species` attributes of the `Cat` object.

You could instead name the parent class explicitly:

```Python
class Cat(Animal):
    def __init__(self, name, breed, toy):
        Animal.__init__(self, name, species="Cat")
        self.breed = breed
        self.toy = toy
```

In this single-inheritance example the two forms happen to produce the same result, but **they are not equivalent in general**. There are three real differences:

**1. `super()` follows the MRO; an explicit call hard-codes one class.** With multiple inheritance, the next class in the MRO is not necessarily the class you named. Explicit calls can therefore run a shared base class more than once — the classic diamond problem:

```Python
class Base:
    def __init__(self):
        print("Base.__init__")

class Left(Base):
    def __init__(self):
        print("Left.__init__")
        super().__init__()

class Right(Base):
    def __init__(self):
        print("Right.__init__")
        super().__init__()

class Child(Left, Right):
    def __init__(self):
        print("Child.__init__")
        super().__init__()

Child()
# Child.__init__
# Left.__init__
# Right.__init__
# Base.__init__      <- runs exactly once

print([c.__name__ for c in Child.__mro__])
# ['Child', 'Left', 'Right', 'Base', 'object']
```

Note that `super().__init__()` inside `Left` calls `Right.__init__`, **not** `Base.__init__`, even though `Right` is not a parent of `Left`. The next class is determined by the MRO of the object actually being created. Had `Left` and `Right` each called `Base.__init__(self)` explicitly, `Base.__init__` would have executed **twice** — a real source of bugs when the base class opens files, increments counters, or appends to a list.

**2. `super()` keeps the class name out of the method body.** If you rename the parent, or insert a class into the hierarchy, code using `super()` keeps working while explicit calls must be updated by hand.

**3. Explicit calls are still occasionally the right tool.** When you deliberately want one specific implementation — for example to skip a class in the MRO, or when combining classes that were never designed to cooperate — naming it explicitly is the clearer choice.

The practical rule: use `super()` consistently throughout a hierarchy. Mixing `super()` in one class with explicit base calls in a sibling is what produces the "why did this run twice?" bugs. Note also that Python 2 required the verbose `super(Cat, self).__init__(...)`; the zero-argument `super()` shown here is Python 3 only.

## 32- What is a property decorator in Python?

In Python, the `property` decorator is a built-in function that is used to create a special kind of attribute called a "property." A property is a special kind of attribute that is defined as a method, but it is accessed like a regular attribute.

Here is an example of how the `property` decorator is used to define a property in a class:

```Python
class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @full_name.setter
    def full_name(self, name):
        first_name, last_name = name.split(" ")
        self._first_name = first_name
        self._last_name = last_name

person1 = Person("John", "Doe")
print(person1.full_name) # prints "John Doe"
person1.full_name = "Jane Doe"
print(person1.full_name) # prints "Jane Doe"

```

In this example, the `full_name` attribute is defined as a `property` using the `@property` decorator. The `full_name` property is defined as a method that returns the full name of the person, which is the combination of the `_first_name` and `_last_name` attributes.

The `full_name` property also has a setter, which is defined using the `@full_name.setter` decorator. The setter allows you to set the value of the `full_name` property, which in turn sets the values of the `_first_name` and `_last_name` attributes.

To use the `full_name` property, you can access it like a regular attribute, using dot notation. For example, `person1.full_name` returns the **full name** of the person, and `person1.full_name = "Jane Doe"` sets the full name of the person.

Properties are useful because they allow you to define methods that are accessed like attributes, which can make your code more readable and easier to use. They also allow you to add additional behavior to attribute access, such as data validation or type checking.

Note that the setter above is deliberately simple; `name.split(" ")` raises a `ValueError` on a single name or a three-part name. A realistic setter validates its input, and a property can also define a **deleter**:

```Python
class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @full_name.setter
    def full_name(self, name):
        parts = name.split(" ")
        if len(parts) != 2:
            raise ValueError(f"Expected 'First Last', got {name!r}")
        self._first_name, self._last_name = parts

    @full_name.deleter
    def full_name(self):
        self._first_name = self._last_name = ""

p = Person("John", "Doe")
p.full_name = "Jane Roe"
print(p.full_name)        # Jane Roe
# p.full_name = "Cher"    # ValueError: Expected 'First Last', got 'Cher'
```

The real value of `property` is that it lets you **start with a plain attribute and add behaviour later without changing the calling code**. In languages without this feature, developers write `get_x()`/`set_x()` accessors up front just in case; in Python you write `self.x` and convert it to a property only if validation or computation becomes necessary. Callers never notice the difference. Under the hood `property` is implemented as a data descriptor, which is what allows it to intercept every read and write (see the descriptors question).

## 33- What is the difference between Cython and CPython?

Cython is a programming language that is a superset of Python, which means that it is fully compatible with Python and can be used to write Python code. Cython is designed to make it easy to write Python code that can be efficiently compiled into C or C++ code, which can then be compiled into a native machine code executable.

CPython, on the other hand, is the reference implementation of the Python programming language. It is written in C and is the most widely used implementation of Python.

One of the main differences is that Cython compiles to native machine code ahead of time, whereas CPython compiles your source to **bytecode** and then executes that bytecode in a virtual machine. (CPython does not interpret the source text line by line — the `.pyc` files in `__pycache__` are the cached bytecode.) The extra step of dispatching bytecode at runtime is a large part of why pure Python is slower than C.

It is worth being precise about where Cython's speed actually comes from: simply renaming a `.py` file to `.pyx` and compiling it typically yields only a modest gain, because the code still uses dynamically typed Python objects. The significant speedups come from adding static type declarations (`cdef int i`), which let Cython emit plain C operations instead of manipulating Python objects — often an order of magnitude or more on tight numeric loops.

Another difference is that Cython allows you to include C or C++ code in your Python code, which can be useful if you want to use existing C or C++ libraries or if you want to write low-level code that is not possible in pure Python.

Overall, Cython is a useful tool for optimizing Python code and extending Python with C or C++ code, while CPython is the reference implementation of the Python language and is used for running Python code on most platforms.

## 34- Specify the difference between local and global variables in Python

In Python, a local variable is a variable that is defined within a function or method and is only accessible within that function or method. A global variable is a variable that is defined outside of any function or method and is accessible from anywhere in the program.

Here is an example of how local and global variables work in Python:

```Python
# Global variable
x = 10

def some_function():
    # Local variable
    y = 5
    print(y) # prints 5

some_function()
print(x) # prints 10
print(y) # This will cause an error because y is a local variable and is not accessible outside of the some_function() function

```

In this example, `x` is a global variable because it is defined outside of any function or method. It is accessible from anywhere in the program, so it can be printed both inside and outside of the `some_function` function.

`y` is a local variable because it is defined within the `some_function` function. It is only accessible within the `some_function` function and is not accessible outside of it. If you try to access `y` outside of the `some_function` function, it will cause an error because `y` is not defined in the global scope.

It is important to note that local variables take precedence over global variables with the same name. For example:

```Python
x = 10

def some_function():
    x = 5
    print(x) # prints 5

some_function()
print(x) # prints 10
```

In this case, the `x` variable within the `some_function` function is a local variable and takes precedence over the global `x` variable. When you print `x` within the `some_function` function, it will print the value of the local `x` variable, which is **`5`**. When you print `x` outside of the function, it will print the value of the global `x` variable, which is **`10`**.

To access the global variable from within a function, you can use the global keyword to specify that you want to access the global variable, like this:

```Python
x = 10

def some_function():
    global x
    x = 5
    print(x) # prints 5

some_function()
print(x) # prints 5
```

In this case, the global `x` statement tells Python that you want to access the global `x` variable within the `some_function` function. This allows you to modify the value of the global `x` variable from within the function.

## 35- What are Python iterators?

In Python, an iterator is an object that produces the elements of a sequence one at a time. An iterator implements two methods, together called the **iterator protocol**: `__iter__` and `__next__`.

`__iter__` is called when iteration begins (by the `iter()` built-in, or implicitly by a `for` loop) and returns the iterator itself. `__next__` is called to retrieve the next element. When there are no more elements, `__next__` raises a `StopIteration` exception to signal that iteration is complete.

It is important to distinguish an **iterable** from an **iterator**, because interviewers ask about this constantly:

- An **iterable** is anything you can loop over — a list, tuple, string, or dict. It implements `__iter__`, which returns a **fresh** iterator each time. Iterables can be looped over repeatedly.
- An **iterator** is the object doing the actual walking. It implements both `__iter__` (returning itself) and `__next__`. An iterator is **one-shot**: once exhausted it stays exhausted, and looping over it again yields nothing.

```Python
my_list = [1, 2, 3]          # an ITERABLE, not an iterator

print(list(my_list))         # [1, 2, 3]
print(list(my_list))         # [1, 2, 3] - a fresh iterator each time

it = iter(my_list)           # an ITERATOR
print(list(it))              # [1, 2, 3]
print(list(it))              # []  <- exhausted, and it stays that way
```

Here is an example of how you can use an iterator to iterate over a list in Python:

```Python
# Define a list
my_list = [1, 2, 3, 4]

# Create an iterator object
it = iter(my_list)

# Iterate over the elements of the list
print(next(it)) # prints 1
print(next(it)) # prints 2
print(next(it)) # prints 3
print(next(it)) # prints 4
print(next(it)) # This will raise a StopIteration exception

```

In this example, the `iter` function is used to create an iterator object for the `my_list` list. The `next` function is then used to retrieve the elements of the list one by one. When there are no more elements to iterate over, the next function raises a _`StopIteration`_ exception.

You can also use a for loop to iterate over an iterator in Python. The for loop will automatically call the `__next__` method of the iterator and will stop when a `StopIteration` exception is raised. For example:

```Python
# Define a list
my_list = [1, 2, 3, 4]

# Create an iterator object
it = iter(my_list)

# Iterate over the elements of the list using a for-loop
for i in it:
    print(i) # prints 1, 2, 3, 4
```

Iterators are useful because they allow you to iterate over a sequence of elements in a memory-efficient way. Instead of loading the entire sequence into memory at once, an iterator loads the elements one by one as they are needed, which can save a lot of memory for large sequences.

You can also create your own iterators by defining the `__iter__` and `__next__` methods in a class. For example:

```Python
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result

# Create an instance of the MyIterator class
it = MyIterator([1, 2, 3, 4])

# Iterate over the elements of the iterator
for i in it:
    print(i) # prints 1, 2, 3, 4

```

In this example, the `MyIterator` class defines an iterator that walks over a list of data. The `__iter__` method returns the iterator object itself, and the `__next__` method returns the next element in the sequence, raising `StopIteration` once `self.index` runs past the end of the data.

Note that `MyIterator` is its own iterator, so it inherits the one-shot behaviour described above: a second `for` loop over the same instance produces nothing, because `self.index` is already at the end. If you want an object that can be iterated many times, make it an _iterable_ instead — have `__iter__` return a new iterator (or simply be a generator function) rather than returning `self`.

## 36- What are Python generators?

In Python, a generator is a special type of function that allows you to create an iterator that generates a sequence of values on the fly. Generators are similar to iterators, but they are more memory-efficient because they do not store all of the values in memory at once. Instead, they generate the values one by one as they are needed.

To create a generator in Python, you use the `yield` keyword instead of the `return` keyword. The `yield` keyword causes the generator to pause execution and return a value, but it does not terminate the generator function. When the generator is called again, it will resume execution from the point where it left off.

Here is an example of a simple generator function in Python:

```Python
def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

# Create a generator object
gen = my_range(5)

# Iterate over the generator
for i in gen:
    print(i) # prints 0, 1, 2, 3, 4
```

In this example, the `my_range` generator function generates a sequence of numbers from `0` to `n-1`. When the generator is called, it returns an iterator object that can be used to iterate over the generated values.

You can also create a generator using a generator expression, which is a compact syntax for creating a generator. A generator expression is similar to a list comprehension, but it uses parentheses instead of square brackets and returns a generator object instead of a list.

Here is an example of a generator expression:

```Python
# Create a generator object using a generator expression
gen = (i for i in range(5))

# Iterate over the generator
for i in gen:
    print(i) # prints 0, 1, 2, 3, 4

```

Generators are useful when you want to generate a large sequence of values that you do not need to store in memory all at once. They allow you to generate the values one by one as they are needed, which can save a lot of memory and make your program more efficient.

## 37- What is the difference between Python's Generators and Iterators?

The key thing to state up front is that these are **not two competing categories**: every generator _is_ an iterator. `isinstance(my_range(5), collections.abc.Iterator)` returns `True`. The real distinction is between the _protocol_ and the _convenient way to implement it_.

- An **iterator** is any object implementing the iterator protocol — `__iter__` returning itself and `__next__` returning the next value or raising `StopIteration`. Writing one by hand means creating a class and managing the traversal state yourself in attributes such as `self.index`.

- A **generator** is an iterator that Python builds for you. Calling a generator _function_ (one containing `yield`) returns a generator _object_; Python supplies `__iter__` and `__next__` automatically, and the local variables of the function body hold the state. Each `yield` suspends the function, preserving its local state, and the next `next()` call resumes exactly where it left off.

So a generator is a special case of an iterator, not an alternative to one. The practical difference is how much code you write:

Here are the same semantics written both ways:

```Python
# As a hand-written iterator: a class with explicit state
class MyRange:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        result = self.i
        self.i += 1
        return result

# As a generator: Python writes the protocol for you
def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

print(list(MyRange(5)))   # [0, 1, 2, 3, 4]
print(list(my_range(5)))  # [0, 1, 2, 3, 4]

import collections.abc as abc
print(isinstance(my_range(5), abc.Iterator))  # True - a generator IS an iterator
```

Both produce identical results; the generator just replaces roughly fifteen lines of boilerplate with three.

A point that is easy to get wrong: **both are one-shot**. Exhausting either one leaves it exhausted, and calling `iter()` on an already-consumed generator returns that same spent object rather than restarting it:

```Python
gen = my_range(5)
print(list(gen))    # [0, 1, 2, 3, 4]
print(list(gen))    # []  <- exhausted

it = iter(gen)
print(it is gen)    # True - iter() on an iterator returns the SAME object
print(list(it))     # []  <- still exhausted, NOT restarted
```

It is therefore wrong to say that iterators can be re-iterated while generators cannot; neither can. What _can_ be re-iterated is an **iterable** such as a list or a range, because its `__iter__` hands out a brand-new iterator on each call. If you need to traverse generated values more than once, either call the generator function again to get a fresh object, or materialise the results with `list()`.

Likewise, memory efficiency is not a generator-versus-iterator distinction — both are lazy and hold only their current state. The meaningful comparison is against a **materialised sequence**: `sum(x * x for x in range(10_000_000))` holds one value at a time, while `sum([x * x for x in range(10_000_000)])` builds a ten-million-element list first.

In short: reach for a generator by default, and write the class form only when you need behaviour a generator cannot express, such as an object that is re-iterable, introspectable, or has methods beyond iteration.

## 38- What are Python documentation strings?

In Python, documentation strings (also called docstrings) are strings that are used to document a module, class, method, or function. Docstrings are usually placed at the beginning of the code block that they document, and they are typically used to provide a brief description of what the code does and how it can be used.

In Python, docstrings are written using triple quotes (`'''` or `"""`). For example:

```Python
def some_function(arg1, arg2):
    '''
    Add two numbers together.

    Parameters:
        arg1 (int): The first argument.
        arg2 (int): The second argument.

    Returns:
        int: The sum of arg1 and arg2.
    '''
    return arg1 + arg2
```

In this example, the docstring for the `some_function` function is a multi-line string that is placed at the beginning of the function definition. It provides a brief description of what the function does and lists the parameters and return values of the function.

Docstrings can be accessed at runtime using the `__doc__` attribute of the object. For example:

```Python
print(some_function.__doc__)
# This will print the docstring for the some_function function.

help(some_function)   # the interactive help system reads __doc__ too
```

A few things worth knowing beyond the basics:

- **A docstring must be the first statement** in the module, class, or function body. A string placed anywhere else is just an expression that is evaluated and discarded, and `__doc__` will be `None`.
- **PEP 257** defines the conventions: use `"""triple double quotes"""`, write the summary line in the imperative mood ("Return the sum", not "Returns the sum"), and leave a blank line before a multi-line description.
- Docstrings differ from comments in purpose. A comment (`#`) explains implementation to someone reading the source; a docstring documents the interface and is retained at runtime for `help()`, IDEs, and documentation generators such as Sphinx.
- Common formats include Google style, NumPy style, and reStructuredText. Pick one and apply it consistently.
- Running Python with `-OO` **strips docstrings** from the bytecode, so avoid relying on `__doc__` for program logic.
- Docstrings in the `>>>` prompt format can be executed as tests by the `doctest` module, which keeps examples honest:

```Python
def add(a, b):
    """Return the sum of a and b.

    >>> add(2, 3)
    5
    """
    return a + b

# python -m doctest yourfile.py   ->  runs the example and checks the output
```

## 39- Explain the use of `subn()`, `sub()`, and `split()` in the `“re”` module

`re` is the Python module for regular expression matching. Among its functions (not modules — they are all functions inside the single `re` module) are three used for editing strings: `sub()`, `subn()`, and `split()`.

1. **`sub(pattern, repl, string)`**: Finds every non-overlapping match of `pattern` and replaces it with `repl`, returning the resulting **string**.
2. **`subn(pattern, repl, string)`**: Does exactly the same substitution, but returns a **tuple** of `(new_string, number_of_substitutions)` — not just the count.
3. **`split(pattern, string)`**: Splits the string at every match of `pattern` and returns a **list** of the pieces.

```Python
import re

text = "one1two22three333four"

# sub() -> returns the new string
print(re.sub(r"\d+", "-", text))
# 'one-two-three-four'

# subn() -> returns (new_string, count)
print(re.subn(r"\d+", "-", text))
# ('one-two-three-four', 3)

new_text, count = re.subn(r"\d+", "-", text)
print(count)   # 3

# split() -> returns a list
print(re.split(r"\d+", text))
# ['one', 'two', 'three', 'four']

# All three accept an optional maxsplit/count limit
print(re.sub(r"\d+", "-", text, count=1))    # 'one-two22three333four'
print(re.split(r"\d+", text, maxsplit=1))    # ['one', 'two22three333four']

# If the pattern contains a capturing group, split() keeps the separators
print(re.split(r"(\d+)", "a1b2c"))
# ['a', '1', 'b', '2', 'c']
```

A practical note: if you use the same pattern repeatedly, compile it once with `re.compile()` and call the methods on the resulting pattern object. `re` does cache compiled patterns internally, but compiling explicitly is clearer and avoids re-parsing the pattern string on every call.

## 40- Define polymorphism in Python

In Python, polymorphism refers to the ability of a function or method to behave differently depending on the data type of the arguments passed to it.

Polymorphism is a key feature of object-oriented programming (OOP) and allows you to write code that is more flexible and reusable. It allows you to define a function or method that can accept different types of arguments and perform different actions based on the type of arguments.

There are two main ways to implement polymorphism in Python:

1. **Method overriding**: Defining a method in a subclass with the same name as one in the superclass, but with different behaviour. This is the most common form of polymorphism in Python.

2. **Duck typing**: The most Pythonic form. Python does not require a shared base class at all — if an object provides the method being called, it can be used. "If it walks like a duck and quacks like a duck, it is a duck." What matters is the interface an object supports at runtime, not its position in a class hierarchy.

Python does **not** support method overloading in the C++/Java sense: defining two methods with the same name simply means the second definition replaces the first. The same flexibility is achieved with default arguments, `*args`/`**kwargs`, or `functools.singledispatch` for type-based dispatch.

Here is an example of polymorphism using method overriding. Note that the point of polymorphism is calling the _same_ method on _different_ types and getting type-appropriate behaviour, so the loop below is the part that matters:

```Python
import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# The same call, area(), dispatches to a different implementation per type
for shape in [Rectangle(10, 20), Circle(5)]:
    print(f"{type(shape).__name__}: {shape.area():.2f}")

# Rectangle: 200.00
# Circle: 78.54
```

Duck typing means the shared `Shape` base class is not actually required for that loop to work:

```Python
class Triangle:            # note: does NOT inherit from Shape
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

for shape in [Rectangle(10, 20), Circle(5), Triangle(6, 4)]:
    print(f"{type(shape).__name__}: {shape.area():.2f}")

# Rectangle: 200.00
# Circle: 78.54
# Triangle: 12.00
```

The base class is still useful as documentation and to fail loudly when a subclass forgets to implement `area()` — using `abc.ABC` with `@abstractmethod` makes that failure happen at instantiation time rather than at first call. Built-in polymorphism works the same way: `len()` works on lists, strings, and dicts because each type implements `__len__`.

## 41- What are the differences between Wheels and Eggs?

In Python, wheels and eggs are two different types of distribution formats for Python packages.

A **wheel** (`.whl`) is the modern standard built-distribution format, defined by **PEP 427**. It is a ZIP archive containing the package files plus a `.dist-info` metadata directory, laid out so that installing amounts to unpacking files into place. Wheels are produced today with `python -m build` (historically `setup.py bdist_wheel`) and installed with `pip`.

An **egg** (`.egg`) is the older, `setuptools`-specific format that predates any packaging standard. Eggs were created and installed by `easy_install`, which has since been removed from `setuptools`.

The key differences:

- **Standardisation**: The wheel format is a documented interoperable standard (PEP 427). The egg format was never standardised — it was whatever `setuptools` happened to implement.

- **Code execution at install time**: This is the most important practical difference. Installing an egg could execute arbitrary code by running the package's `setup.py`. Installing a wheel does not run any project code; `pip` simply unpacks the archive and moves files into place. That makes installation faster, reproducible, and safer.

- **Importable vs. install-only**: Eggs were designed to be importable directly — an `.egg` file could be placed on `sys.path` and imported without being unpacked, and eggs carried runtime machinery such as `pkg_resources` entry points. A wheel is purely a _distribution_ format: it is never imported directly, only installed.

- **Build isolation and compiled code**: Wheels encode the target Python version, ABI, and platform in the filename (for example `numpy-1.26.0-cp312-cp312-win_amd64.whl`), so `pip` can pick the correct prebuilt binary and skip compiling C extensions from source. This is why installing packages such as NumPy or Pandas is now near-instant rather than requiring a compiler.

- **Tooling support**: `pip` installs wheels. `easy_install`, the only installer for eggs, no longer exists in current `setuptools`.

In summary, wheels are the standard and only recommended distribution format; eggs are obsolete and should not be produced for new projects. You may still encounter `.egg-info` directories or `pkg_resources` in older codebases, but new packaging should target wheels — and `importlib.metadata` has replaced `pkg_resources` for reading package metadata at runtime.

## 42- What is the purpose of Python non-local statements?

The `nonlocal` statement lets an inner function **rebind** a variable that belongs to an enclosing (but not global) scope. Without it, any assignment inside a function creates a brand-new local variable, shadowing the outer one and leaving the original untouched.

Reading an enclosing variable never needs `nonlocal` — that works automatically through the LEGB lookup rule. You only need `nonlocal` when you want to **assign** to it.

```Python
def counter():
    count = 0                 # belongs to counter's scope

    def increment():
        nonlocal count        # rebind counter's variable, don't create a new one
        count += 1
        return count

    return increment

c = counter()
print(c())   # 1
print(c())   # 2
print(c())   # 3
```

Without `nonlocal`, the `count += 1` line reads `count` before assigning to it, and since the assignment makes `count` local to `increment`, the read fails:

```Python
def broken_counter():
    count = 0

    def increment():
        count += 1            # no nonlocal -> count is local here
        return count

    return increment

broken_counter()()
# UnboundLocalError: cannot access local variable 'count'
# where it is not associated with a value
```

`nonlocal` differs from `global` in what it targets: `global` rebinds a name in the module namespace, while `nonlocal` rebinds a name in the nearest enclosing _function_ scope. `nonlocal` also requires the name to already exist in an enclosing scope — if it does not, you get a `SyntaxError` at compile time rather than silently creating one.

This matters most for closures that accumulate state, such as counters, memoisation caches, and accumulator callbacks. That said, a class or a `functools` helper is often clearer than a closure that mutates captured state, so reach for `nonlocal` when it genuinely simplifies the code.

## 43- How is Python exception is handled?

In Python, exceptions are handled using the `try` and except statements.

Here's an example of how you can use the `try` and except statements to handle an exception:

```Python
try:
    # Code that might cause an exception goes here
    x = int('foo')
except ValueError:
    # Code to handle the exception goes here
    print('Invalid input')
```

In this example, the `try` block contains code that might cause a _ValueError_ exception to be raised (in this case, attempting to convert the string 'foo' to an integer). If the exception is raised, the execution of the `try` block is halted, and control is transferred to the `except` block. The `except` block contains code that is executed to handle the exception. In this case, it prints an error message to the console.

You can also specify multiple `except` blocks to handle different types of exceptions:

```Python
try:
    # Code that might cause an exception goes here
    x = int('foo')
except ValueError:
    # Code to handle the ValueError exception goes here
    print('Invalid input')
except TypeError:
    # Code to handle the TypeError exception goes here
    print('Invalid type')

```

You can also use the `else` clause to specify a block of code that should be executed if no exceptions are raised in the try block:

```Python
try:
    # Code that might cause an exception goes here
    x = int('3')
except ValueError:
    # Code to handle the ValueError exception goes here
    print('Invalid input')
else:
    # Code to be executed if no exceptions are raised goes here
    print(x)

```

In this example, the `else` block will be executed if the `try` block completes successfully (i.e. if no exceptions are raised), and it will print the value of `x` to the console.

Finally, you can use the `finally` clause to specify a block of code that should always be executed, regardless of whether an exception is raised or not:

```Python
try:
    # Code that might cause an exception goes here
    x = int('foo')
except ValueError:
    # Code to handle the ValueError exception goes here
    print('Invalid input')
finally:
    # Code to always be executed goes here
    print('Done')
```

In this example, the `finally` block will be executed after the `try` block, regardless of whether an exception is raised or not. It will print the message **`'Done'`** to the console. `finally` runs even if the exception is _not_ caught and propagates upward, and even if the `try` block exits early via `return`, `break`, or `continue` — which is what makes it reliable for cleanup.

Putting the four clauses together, the full form reads:

```Python
try:
    value = int(user_input)      # code that might raise
except ValueError as e:          # 'as e' binds the exception object
    print(f"Could not convert: {e}")
else:
    print(f"Success: {value}")   # runs only if NO exception was raised
finally:
    print("Always runs")         # cleanup, runs no matter what
```

Keep the `try` block as small as possible and put the follow-up work in `else`. If you place it inside `try`, an exception raised by that follow-up code gets caught by your handler too, hiding bugs you never meant to catch.

**Catching several types**, and inspecting the exception:

```Python
try:
    result = 10 / 0
except (ValueError, TypeError) as e:   # one handler for several types
    print(f"Bad input: {e}")
except ZeroDivisionError as e:
    print(f"Division error: {e}")
```

Handlers are checked in order, and the first matching one wins. Because `except` matches subclasses too, always order handlers from most specific to most general — putting `except Exception` first would swallow everything below it.

**Raising exceptions**, including your own:

```Python
class InsufficientFundsError(Exception):
    """Raised when an account lacks the funds for a withdrawal."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Balance {balance} is less than requested {amount}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(50, 100)
except InsufficientFundsError as e:
    print(e)              # Balance 50 is less than requested 100
    print(e.balance)      # 50 - custom attributes survive
```

Custom exceptions should subclass `Exception` (not `BaseException`, which also covers `KeyboardInterrupt` and `SystemExit` — signals you almost never want to intercept).

**Re-raising and chaining.** A bare `raise` inside a handler re-raises the current exception with its original traceback intact, which is the right way to log and pass along. `raise ... from e` records the original cause:

```Python
try:
    config = load_config()
except FileNotFoundError as e:
    raise RuntimeError("Configuration missing") from e   # preserves the cause
```

**Anti-patterns to avoid:**

- `except:` or `except Exception:` with an empty or `pass` body — this hides real bugs and makes failures silent. Catch only what you can actually handle.
- A bare `except:` also catches `KeyboardInterrupt` and `SystemExit`, making a program impossible to interrupt with Ctrl-C. Use `except Exception:` if you really must be broad.
- Using exceptions for ordinary control flow where a simple conditional is clearer.

That said, Python idiom favours **EAFP** — "easier to ask forgiveness than permission" — over defensive pre-checks. Attempting the operation and handling the exception is usually preferred to checking first, since the check can race or miss cases:

```Python
# EAFP - idiomatic Python
try:
    value = my_dict["key"]
except KeyError:
    value = default

# LBYL - "look before you leap", more common in other languages
if "key" in my_dict:
    value = my_dict["key"]
else:
    value = default
```

## 44- Name the differences between functional and object-oriented programming

Functional programming and object-oriented programming are two programming paradigms that are commonly used in Python. Each paradigm has its own set of characteristics and approaches to solving problems, and they can be used in different situations depending on the needs of the project.

Here are some key differences between functional programming and object-oriented programming in Python:

1. **Data model**: In functional programming, data is treated as immutable and functions are used to transform data. In object-oriented programming, data is encapsulated in objects and accessed through methods.

2. **State**: In functional programming, the state is typically avoided or minimized, and functions are designed to be pure and side-effect-free. In object-oriented programming, objects have an internal state that can be modified through methods.

3. **Inheritance**: In object-oriented programming, inheritance is used to create a hierarchy of classes and reuse code between classes. In functional programming, inheritance is not typically used, and functions are composed and combined to create new functionality.

4. **Polymorphism**: In object-oriented programming, polymorphism is usually achieved by overriding methods in subclasses, so the same call dispatches to different implementations depending on the object's type. In functional programming, the same flexibility comes from higher-order functions and generic functions that work across any type supporting the required operations — in Python, `functools.singledispatch` provides exactly this type-based dispatch without a class hierarchy. (Currying, sometimes cited here, is about partial application of arguments rather than polymorphism; `functools.partial` is Python's version.)

5. **Concurrency**: In functional programming, concurrency is typically easier to achieve because functions are pure and do not depend on state. In object-oriented programming, concurrency can be more challenging because objects have an internal state that can be modified concurrently.

## 45- What does the `PYTHONOPTIMIZE` flag do?

`PYTHONOPTIMIZE` is an **environment variable**; the equivalent command-line flags are `-O` and `-OO`. Setting `PYTHONOPTIMIZE=1` is the same as passing `-O`, and `PYTHONOPTIMIZE=2` is the same as `-OO`.

Despite the name, it performs very little optimisation. It does exactly three things:

**At level 1 (`-O` or `PYTHONOPTIMIZE=1`):**

- Sets the built-in `__debug__` constant to `False`.
- Removes all `assert` statements from the compiled bytecode.
- Skips the body of any `if __debug__:` block.

**At level 2 (`-OO` or `PYTHONOPTIMIZE=2`):**

- Everything from level 1, plus **docstrings are stripped** from the compiled bytecode (`__doc__` becomes `None`).

That is the complete list. It does **not** inline functions, specialise calls, or eliminate dead code in any general sense. Optimisations such as constant folding and peephole optimisation are performed by the compiler on every run regardless of this setting, so they are not something `-O` turns on.

```bash
python -O script.py    # strip asserts, __debug__ = False
python -OO script.py   # the above, plus strip docstrings
```

```bash
PYTHONOPTIMIZE=1 python script.py    # same effect as -O
```

You can observe the whole effect directly:

```Python
def f():
    """A docstring."""
    return 1

print(__debug__)     # True normally, False under -O
print(f.__doc__)     # 'A docstring.' normally, None under -OO

assert False, "boom" # raises AssertionError normally, silently skipped under -O
```

The practical caution is the opposite of what is often assumed. This flag is aimed at production use — trimming assertion overhead and shrinking bytecode — not at debugging or profiling. The danger is that **stripping asserts changes behaviour if any assert is doing real work.** Code such as `assert user.is_authenticated` or an assert with a side effect silently stops running under `-O`. Assertions are for catching programmer errors during development; never use them to validate user input, enforce permissions, or perform any check your program depends on at runtime — raise a real exception instead. Similarly, `-OO` breaks any library that inspects `__doc__` at runtime, such as some CLI frameworks and doctest.

The speed benefit is marginal in most programs. If performance is the real goal, profile first, then consider algorithmic fixes, optimised libraries, or an alternative runtime such as PyPy — all of which will matter far more than this flag.

## 46- What are descriptors? Is there a difference between a descriptor and a decorator?

In Python, a descriptor is an object attribute with "binding behavior", which means that it has the ability to define how it is accessed and set. Descriptors are implemented using a set of special methods, known as the descriptor protocol, which consists of the `__get__`, `__set__`, and `__delete__` methods.

Descriptors are a way to define custom attribute access behavior in Python. They can be used to implement properties, methods, or any other attribute type with custom behavior. For example, you might use a descriptor to implement a lazy evaluation of an attribute or to provide read-only access to an attribute.

Descriptors come in two kinds, and the difference determines lookup precedence:

- A **data descriptor** defines `__set__` and/or `__delete__` (usually alongside `__get__`).
- A **non-data descriptor** defines only `__get__`.

The attribute lookup order for `obj.x` is:

1. **Data descriptors** found on the type (or its bases) — these win over everything.
2. The **instance `__dict__`**.
3. **Non-data descriptors** and ordinary class attributes.
4. `__getattr__`, if defined, as a last resort.

The common misconception is that the instance dictionary always takes priority. It does not: a data descriptor beats the instance `__dict__`, which is precisely what makes `property` able to intercept every read and write even after something has been assigned to the instance. A non-data descriptor, by contrast, _is_ shadowed by an entry in the instance dictionary:

```Python
class DataDesc:
    def __get__(self, obj, objtype=None):
        return "from data descriptor"
    def __set__(self, obj, value):
        obj.__dict__['x'] = value          # store it, but keep control of reads

class NonDataDesc:
    def __get__(self, obj, objtype=None):
        return "from non-data descriptor"

class T:
    x = DataDesc()        # data descriptor: has __set__
    y = NonDataDesc()     # non-data descriptor: only __get__

t = T()
t.x = "instance value"
t.__dict__['y'] = "instance value"

print(t.x)              # 'from data descriptor'  <- descriptor wins
print(t.__dict__['x'])  # 'instance value'        <- the value really is stored
print(t.y)              # 'instance value'        <- instance dict wins
```

Descriptors are not an exotic corner of the language — they are the mechanism behind features you already use. `property`, `classmethod`, `staticmethod`, `functools.cached_property`, and ordinary Python functions becoming bound methods are all implemented as descriptors. ORM fields in Django and SQLAlchemy are descriptors too.

Since Python 3.6, `__set_name__(self, owner, name)` is called automatically when the class body is executed, letting a descriptor learn the attribute name it was assigned to — useful for storing per-instance values without hard-coding a key:

```Python
class Positive:
    def __set_name__(self, owner, name):
        self.name = name                    # learns 'width' / 'height' automatically

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self.name} must be positive, got {value}")
        obj.__dict__[self.name] = value

class Rect:
    width = Positive()
    height = Positive()

    def __init__(self, width, height):
        self.width = width
        self.height = height

r = Rect(3, 4)
print(r.width)          # 3
# Rect(-1, 4)           # ValueError: width must be positive, got -1
```

A **decorator**, by contrast, is a callable that takes a function (or class) and returns a replacement, applied with the `@` syntax to extend behaviour without modifying the original source.

There is a difference between a descriptor and a decorator in Python. A descriptor is an object attribute with binding behavior, whereas a decorator is a function that takes another function and extends its behavior. Descriptors are implemented using the descriptor protocol, which consists of the `__get__`, `__set__`, and `__delete__` methods, whereas decorators are implemented as functions that take a function as an argument and return a modified version of the function.

## 47- Generate random number

You can generate a random number using the `random` module.

```Python
import random

random.randint(1, 100)      # random integer, 1 and 100 both included
random.randrange(0, 100, 2) # random even integer in [0, 100)
random.random()             # random float in [0.0, 1.0), e.g. 0.3366241606464734
random.uniform(1.0, 10.0)   # random float in [1.0, 10.0]
random.choice([1, 2, 3])    # a random element from a sequence
random.sample(range(100), 5)# 5 distinct elements, without replacement
random.shuffle(my_list)     # shuffles a list in place, returns None
```

You can set a seed with `random.seed(x)`, where `x` is the value used to initialise the generator. Seeding makes the sequence **reproducible**, which is what you want in tests and simulations:

```Python
import random

random.seed(42)
print([random.randint(1, 10) for _ in range(3)])   # e.g. [2, 1, 5]

random.seed(42)                                     # same seed...
print([random.randint(1, 10) for _ in range(3)])   # ...same sequence
```

Seeding with the current time (`random.seed(time.time())`) is unnecessary — the generator already seeds itself from the operating system's entropy at import time, so you only call `seed()` when you specifically want reproducibility.

One important caveat worth raising in an interview: **`random` is not cryptographically secure.** It uses a Mersenne Twister, which is fast and statistically excellent but fully predictable — an observer who sees enough output can recover the internal state and predict all future values. For passwords, tokens, session IDs, or anything security-related, use the `secrets` module instead:

```Python
import secrets

secrets.randbelow(100)        # cryptographically secure integer in [0, 100)
secrets.token_hex(16)         # secure random hex string, e.g. for a token
secrets.choice(['a', 'b'])    # secure choice from a sequence
```

## 48- What are itertools in Python?

The `itertools` module is a Python module that provides a number of functions that are helpful when working with iterators. Iterators are objects that allow you to iterate over a sequence of values, such as a list or a string.

Here are a few examples of functions that are available in the `itertools` module:

Everything in `itertools` returns a **lazy iterator**, so values are produced on demand rather than built up in a list. That is what makes it usable with infinite sequences and large data sets.

```Python
import itertools

# count: consecutive values from a start, forever
for i in itertools.count(10, 2):
    if i > 16:
        break
    print(i, end=" ")          # 10 12 14 16
print()

# cycle: repeats a sequence indefinitely
cycler = itertools.cycle("AB")
print([next(cycler) for _ in range(5)])       # ['A', 'B', 'A', 'B', 'A']

# repeat: the same value, n times (or forever)
print(list(itertools.repeat("x", 3)))         # ['x', 'x', 'x']

# permutations: ordered arrangements
print(list(itertools.permutations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# combinations: unordered selections, no repeats
print(list(itertools.combinations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 3)]

# chain: treat several iterables as one continuous sequence
print(list(itertools.chain([1, 2], [3, 4])))  # [1, 2, 3, 4]

# groupby: group CONSECUTIVE equal items - sort first if you want global grouping
data = [("a", 1), ("a", 2), ("b", 3)]
for key, group in itertools.groupby(data, key=lambda pair: pair[0]):
    print(key, list(group))
# a [('a', 1), ('a', 2)]
# b [('b', 3)]

# accumulate: running totals
print(list(itertools.accumulate([1, 2, 3, 4])))   # [1, 3, 6, 10]
```

Note that `count` and `cycle` are **infinite** — never call `list()` on them directly, or the program will hang and eventually exhaust memory. Pair them with `islice`, `zip`, or an explicit `break`. Note too the common `groupby` trap: it only groups _adjacent_ items, so sort by the same key first if you want all matching items grouped together.

## 49- what does itertools.islice do?

`itertools.islice` is a function that returns an iterator that returns selected elements from the input iterator. It works by slicing the input iterator and returning an iterator that produces the sliced elements.

Here's an example of how you can use `itertools.islice`:

```Python
import itertools

# Create a list of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Take every other element, starting at index 0
every_other = itertools.islice(numbers, 0, 10, 2)

for number in every_other:
    print(number, end=" ")
# Output: 1 3 5 7 9
```

Note what the output actually shows: `islice` selects by **position**, not by value. Indices 0, 2, 4, 6, 8 hold the values 1, 3, 5, 7, 9 — the elements at even _indices_, which in this list happen to be the odd _numbers_.

The crucial difference from ordinary slicing is that `islice` works on any iterable, including generators and infinite iterators, and consumes it lazily. `numbers[0:10:2]` requires a sequence that supports indexing and builds a new list immediately; `islice` does neither:

```Python
import itertools

# Works on an infinite iterator - ordinary slicing cannot do this
first_five_evens = itertools.islice(itertools.count(0, 2), 5)
print(list(first_five_evens))    # [0, 2, 4, 6, 8]
```

Two practical caveats: `islice` does not accept negative indices (it cannot count from the end without consuming everything), and it **consumes** the underlying iterator, so elements it skips are gone for good.

You can also use `itertools.islice` to slice at a specific starting and ending position with a specific step size. For example, `itertools.islice(numbers, 2, 6, 1)` returns an iterator producing the elements at indices `2` through `5`. Below are examples of output based on various inputs:

```Python
# itertools.islice(iterable, stop)
# itertools.islice(iterable, start, stop, step)

# islice('ABCDEFG', 2)          --> A B
# islice('ABCDEFG', 2, 4)       --> C D
# islice('ABCDEFG', 2, None)    --> C D E F G
# islice('ABCDEFG', 0, None, 2) --> A C E G
```

## 50- Why this code will never stop?

```Python
i = 0
while i != 1:
    i += 0.1
    print(i)
```

This code will never stop because the condition `i != 1` is never satisfied. `0.1` cannot be represented exactly in binary floating point — it is stored as a value very slightly different from one tenth — so adding it repeatedly accumulates a small error:

```Python
i = 0
for _ in range(10):
    i += 0.1
print(repr(i))    # 0.9999999999999999
print(i == 1)     # False
```

After ten additions `i` is `0.9999999999999999`, not `1.0`. The eleventh addition takes it to `1.0999999999999999`, so the loop **steps straight over `1`** without ever hitting it.

It is worth being precise about what happens next: `i` does not converge on `1` or hover near it. It keeps increasing without bound — past 2, past 100, forever — because nothing in the loop stops it. The loop is infinite not because `i` approaches `1` too slowly, but because it passes `1` and never comes back.

The general lesson is to **never test floating-point values for exact equality**. Use one of these instead:

```Python
# 1. Use an inequality so overshooting still terminates the loop
i = 0
while i < 1:
    i += 0.1

# 2. Compare with a tolerance
import math
print(math.isclose(0.1 + 0.2, 0.3))            # True
print(0.1 + 0.2 == 0.3)                        # False

# 3. Iterate over integers and scale, avoiding float accumulation entirely
for n in range(10):
    i = n / 10

# 4. Use decimal.Decimal when exact decimal arithmetic matters, as with money
from decimal import Decimal
i = Decimal("0")
while i != Decimal("1"):
    i += Decimal("0.1")        # terminates: Decimal("0.1") is exact
```

This is not a Python quirk — it is the IEEE 754 standard used by essentially every language.

## 51- What is the output of this code, and why?

```Python
import datetime
from time import sleep
def my_time(time_now = datetime.datetime.now()):
    return time_now

print(my_time())
sleep(3)
print(my_time())
```

The output of this code will be two **identical** timestamps, even though three seconds pass between the calls. The default value of the `time_now` parameter is evaluated exactly once — when the `def` statement runs — not on each call.

As a result, the value of `time_now` is fixed at the moment the function is defined. Both calls return the very same `datetime` object (`my_time() is my_time()` is `True`), which is why the printed values match to the microsecond. This is the classic "mutable/evaluated-once default argument" pitfall: default values live on the function object itself (inspect `my_time.__defaults__`), so anything computed or mutable there is shared across all calls.

To fix this issue, you could remove the default value for the `time_now` parameter, and set it to the current time inside the function using `datetime.datetime.now()`, like this:

```Python
import datetime
from time import sleep
def my_time(time_now = None):
    if time_now is None:
        time_now = datetime.datetime.now()
    return time_now

print(my_time())
sleep(3)
print(my_time())
```

## 52- Can we chain Multiple Decorators in Python?

Yes, you can chain multiple decorators in Python. Decorators are functions that are used to modify the behavior of another function. They are applied using the `@` symbol and can be used to add additional functionality to a function without modifying the function's source code.

To chain multiple decorators, you can simply apply them one after the other, using the `@` symbol, like this:

```Python
@decorator1
@decorator2
@decorator3
def function():
    ...  # function code goes here
```

Stacked decorators are applied **bottom-up**: the decorator closest to the `def` wraps the function first. The stack above is exactly equivalent to:

```Python
function = decorator1(decorator2(decorator3(function)))
```

So at definition time `decorator3` is applied first and `decorator1` last — `decorator1` ends up as the outermost wrapper. At **call** time the order reverses: the outermost wrapper (`decorator1`) runs first, then delegates inward. Keeping these two orders straight — bottom-up application, top-down execution — is the point interviewers usually probe.

```Python
def decorator1(func):
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def function():
    print('Function')

function()

# This will produce the following output:

# Decorator 1
# Decorator 2
# Function
```

Here `function = decorator1(decorator2(function))`: `decorator2` wrapped the function first, `decorator1` wrapped the result. When called, `decorator1`'s wrapper prints first, calls `decorator2`'s wrapper, which finally calls the original function — producing the top-down output shown. As with any decorator, apply `functools.wraps` in real code so the chain preserves the original function's name and docstring.

## 53- Build a recursive function using python

To build a recursive function in Python, you will need to define a function that calls itself with a modified version of its input. Here's an example of how you can build a recursive function to calculate the factorial of a number:

```Python
def factorial(n):
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    if n <= 1:          # base case: covers both 0! == 1 and 1! == 1
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
```

In this example, the `factorial` function is defined to take a single argument `n`. Every recursive function needs two things: a **base case** that terminates the recursion, and a **recursive case** that moves toward it. Here the base case returns `1` for `n <= 1`, and the recursive case returns `n * factorial(n - 1)`.

Two details matter more than they look:

- **The base case must cover every terminating input.** With the common `if n == 1` base case, `factorial(0)` never terminates — each call passes a smaller negative number until Python raises `RecursionError: maximum recursion depth exceeded`. `0! == 1` by definition, so the guard should be `n <= 1`, with an explicit `ValueError` for negatives.
- **Python does not optimise tail calls**, and the default recursion limit is about 1000 frames (`sys.getrecursionlimit()`), so `factorial(3000)` raises `RecursionError` even though the maths is fine. For depths like that, prefer an iterative version — or `math.factorial`, which is what production code should call anyway.

```Python
# 1st call: return n * factorial(4) "n = 5"
# 2nd call: return n * factorial(3) "n = 4"
# 3rd call: return n * factorial(2) "n = 3"
# 4th call: return n * factorial(1) "n = 2"
# 5th call: return 1                "n = 1"

# The held calls then resolve as the stack unwinds:
# 4th call: 2 * 1 = 2
# 3rd call: 3 * 2 = 6
# 2nd call: 4 * 6 = 24
# 1st call: 5 * 24 = 120 (5! -> 120)
```

## 54- How to implement a binary search tree using Python?

To implement a binary search tree (BST) in Python, you will need to create a `Node` class to represent the nodes of the tree, and a `BST` class to represent the `BST` itself.

Here is an example of how you could implement a `Node` class in Python:

```Python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

This `Node` class has three instance variables: `value`, `left`, and `right`. The `value` variable stores the value of the `node`, and the `left` and `right` variables are references to the `left` and `right` child nodes, respectively.

To implement the `BST` itself, you will need to create a `BST` class that has methods for inserting and searching for nodes in the `tree`. Here is an example of how you could implement a `BST` class in Python:

```Python
class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, value):
        if self.root is None:
            return False
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False
```

The `BST` class has a `root` variable to store the `root` node of the `tree`, and two methods: `insert` and `search`. The `insert` method is used to insert a new node into the tree, and the `search` method is used to search for a node with a particular value.

To use these classes, you can create a new `BST` object and use the `insert` method to add nodes to the tree. You can then use the search method to search for a particular value in the tree. If a node with the specified `value` is found, the method returns `True`, otherwise it returns `False`. (As written, duplicates go to the right subtree; stating that policy explicitly is worth a sentence in an interview.)

An in-order traversal visits a BST's values in sorted order, which is both the standard way to read the tree back and a quick sanity check of the invariant:

```Python
def in_order(node):
    if node is not None:
        yield from in_order(node.left)
        yield node.value
        yield from in_order(node.right)

tree = BST()
for v in [8, 3, 10, 1, 6]:
    tree.insert(v)

print(list(in_order(tree.root)))   # [1, 3, 6, 8, 10]
print(tree.search(6))              # True
print(tree.search(7))              # False
```

Complexity: `insert` and `search` are **O(h)** where `h` is the tree height — O(log n) on average for random insertion order, but **O(n) in the worst case**, because inserting already-sorted data degenerates the tree into a linked list. Self-balancing variants (AVL, red-black trees — the structure behind `sorted containers` in other languages) guarantee O(log n); Python's standard library instead offers the `bisect` module over a sorted list for the common cases.

## 55- How to implement a binary search using Python?

```Python
# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
```

The non-negotiable precondition: **the input must already be sorted** — binary search on unsorted data silently returns wrong answers. Each comparison halves the search space, giving O(log n) time; this recursive version also uses O(log n) stack space, while a `while`-loop version brings that down to O(1).

In production code, reach for the standard library instead of hand-rolling: `bisect.bisect_left(arr, x)` returns the insertion point in O(log n), and `arr[i] == x` at that index confirms membership.

## 56- How to implement a Linked list using Python?

You will need to define a `Node` class to represent the nodes of the linked list, and a `LinkedList` class to represent the linked list itself.

```Python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

This `Node` class has two instance variables: `value` and `next`. The `value` variable holds the value of the `node`, and the `next` variable holds a reference to the `next` node in the linked list.

Next, you can define the `LinkedList` class, which will contain methods for inserting nodes into the linked list and searching for specific values:

```Python
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
```

The `LinkedList` class has two methods: `append` and `traverse`. The `append` method takes a value as an argument, creates a new `Node` object with that value, and appends it to the end of the linked list. The `traverse` method traverses the linked list and prints the value of each node to the console.

You can use these classes to create and manipulate a linked list like this:

```Python
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.traverse()  # Output: 1 2 3 (one value per line)
```

Note that this `append` walks the whole list each time, making it O(n) per call; keeping a `tail` reference alongside `head` makes appends O(1). The general trade-off versus a Python `list`: linked lists give O(1) insertion/removal at a known node without shifting elements, but O(n) indexed access, worse cache behaviour, and per-node object overhead. That is why `collections.deque` (a doubly-linked structure of blocks, with O(1) appends and pops at both ends) is almost always the right practical choice, and hand-written linked lists appear mainly in interviews.

## 57- what is `collections.OrderedDict`?

it is a class in the Python `collections` module that provides an ordered dictionary implementation. Like a regular dictionary, an `OrderedDict` stores key-value pairs, but it remembers the order which the keys were added.

Here's an example of how you can use an `OrderedDict`:

```Python
from collections import OrderedDict

# Create an OrderedDict
d = OrderedDict()

# Add some key-value pairs
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

# Iterate over the OrderedDict
for key, value in d.items():
    print(key, value)

# Output:
# a 1
# b 2
# c 3
# d 4
```

The `OrderedDict` maintains the order in which the keys were added.

The senior-level nuance: since **Python 3.7, plain `dict` also preserves insertion order** as a language guarantee (and did so as an implementation detail in CPython 3.6). So "remembers insertion order" is no longer a reason to reach for `OrderedDict`. What it still offers over `dict`:

- **Order-sensitive equality.** Two `OrderedDict`s with the same items in different order compare unequal; plain dicts compare equal regardless of order:

  ```Python
  from collections import OrderedDict

  OrderedDict(a=1, b=2) == OrderedDict(b=2, a=1)   # False
  dict(a=1, b=2) == dict(b=2, a=1)                 # True
  ```

- **`move_to_end(key, last=True)`** — reposition a key at either end in O(1), the operation that makes an LRU cache trivial to build (see the LRU question later in this file).
- **`popitem(last=False)`** — pop from _either_ end; `dict.popitem()` only pops the most recently inserted item.

Internally it maintains a doubly-linked list alongside the hash table to support those reordering operations, so it costs more memory than a plain dict. Today the practical rule is: use `dict` by default, and `OrderedDict` only when you need reordering operations or order-sensitive equality.

## 58- what is `collections.defaultdict`?

it is a class in the Python `collections` module — a `dict` subclass that takes a **default factory**: a zero-argument callable invoked to produce a value whenever a missing key is accessed. Note the distinction: you pass a _callable that builds_ the default (`int`, `list`, or your own function), not a default value itself. `int()` returns `0`, `list()` returns `[]`, which is where the defaults come from.

Here's an example of how you can use a `defaultdict`:

```Python
from collections import defaultdict

# int() -> 0 is the default
d = defaultdict(int)

# Add some key-value pairs
d['a'] = 1
d['b'] = 2
d['c'] = 3

# Access a key that does not exist in the dictionary
print(d['d'])  # Output: 0

# Output the entire dictionary
print(d)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2, 'c': 3, 'd': 0})
```

Notice the last line: accessing `d['d']` did not just _return_ `0`, it **inserted** the key `'d'` with value `0`. Reads of missing keys mutate a `defaultdict`, which can surprise you if you probe it with `in`-style logic afterwards.

The factory is triggered **only by `d[key]` lookups** (the `__missing__` hook). `d.get('missing')` still returns `None`, and `'missing' in d` is still `False` — neither touches the factory.

The `defaultdict(int)` pattern is a counter (`d[word] += 1` — though `collections.Counter` is more idiomatic for that job), and `defaultdict(list)` is the standard way to group items:

```Python
from collections import defaultdict

words = ["apple", "avocado", "banana", "blueberry", "cherry"]

by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)   # no need to check if the key exists yet

print(by_letter)
# defaultdict(<class 'list'>, {'a': ['apple', 'avocado'],
#                              'b': ['banana', 'blueberry'],
#                              'c': ['cherry']})
```

Any zero-argument callable works as the factory — including a `lambda` for a non-trivial default (`defaultdict(lambda: "N/A")`) or even a nested `defaultdict` for auto-vivifying trees. With a plain `dict`, the closest equivalents are `d.setdefault(key, []).append(...)` or `dict.get(key, default)`, both of which are noisier in a loop.

## 59- Can we implement an `array` using Python?

Yes! By using the `array` module. Python’s `array` module provides space-efficient storage of basic C-style data types like **`bytes, 32-bit integers, floating-point numbers, and so on`**.

Arrays created with the `array.array` class are mutable and behave similarly to lists except for one important difference: they’re **`typed arrays`** constrained to a single data type.

Because of this constraint, `array.array` objects with many elements are more space efficient than `lists` and `tuples`. The elements stored in them are tightly packed, and this can be useful if you need to store many elements of the same type.

Also, arrays support many of the same methods as regular lists, and you might be able to use them as a drop-in replacement without requiring other changes to your application code.

```Python
>>> import array
>>> arr = array.array("f", (1.0, 1.5, 2.0, 2.5))
>>> arr[1]
1.5

>>> # Arrays have a nice repr:
>>> arr
array('f', [1.0, 1.5, 2.0, 2.5])

>>> # Arrays are mutable:
>>> arr[1] = 23.0
>>> arr
array('f', [1.0, 23.0, 2.0, 2.5])

>>> del arr[1]
>>> arr
array('f', [1.0, 2.0, 2.5])

>>> arr.append(42.0)
>>> arr
array('f', [1.0, 2.0, 2.5, 42.0])

>>> # Arrays are "typed":
>>> arr[1] = "hello"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be real number, not str
```

## 60- What is the `bytes` type?

The `bytes` type is an immutable sequence of _bytes_. It is similar to the _str_ type, but it is meant to hold raw binary data rather than Unicode text.

You can create a `bytes` object by prefixing a string with the b character and enclosing it in quotes, like this:

```Python
b = b'Hello, world!'
```

You can also create a `bytes` object from a list of integers using the `bytes` function:

```Python
b = bytes([104, 101, 108, 108, 111])  # b'hello'
```

You can access the individual bytes of a `bytes` object using indices like you would with a string:

```Python
b = b'Hello, world!'
print(b[0])  # Output: 72
print(b[1])  # Output: 101
```

You can also use slicing to extract a sub-sequence of bytes from a `bytes` object:

```Python
b = b'Hello, world!'
print(b[6:11])  # Output: b' worl'
print(b[7:12])  # Output: b'world'
```

Note the asymmetry that trips people up: **indexing a `bytes` object yields an `int`** (`b[0]` is `72`, not `b'H'`), while **slicing yields `bytes`** (`b[0:1]` is `b'H'`).

Two related points complete the picture:

- **`bytes` vs `str` is the binary/text boundary.** You convert between them explicitly with an encoding: `"héllo".encode("utf-8")` produces `bytes`, and `data.decode("utf-8")` produces `str`. Mixing them (`b'a' + 'a'`) raises `TypeError` — Python 3 refuses to guess an encoding, which is precisely what made Python 2's implicit conversions a bug factory.
- **`bytearray` is the mutable counterpart** — same interface, but you can modify it in place (`ba[0] = 72`), which matters when building or patching binary buffers without copying.

You meet `bytes` at every I/O edge: files opened in `'rb'` mode, sockets, `subprocess` pipes, HTTP bodies, and hashing (`hashlib` consumes bytes).

## 61- How to concatenate tuples in python?

You can use the `+` operator. For example:

```Python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

tuple3 = tuple1 + tuple2
print(tuple3)  # Output: (1, 2, 3, 4, 5, 6)
```

This will create a new tuple that contains the elements of `tuple1` followed by the elements of `tuple2`. Unpacking gives the same result and generalises to any number of inputs, including other iterables:

```Python
tuple3 = (*tuple1, *tuple2)        # (1, 2, 3, 4, 5, 6)
```

Keep in mind that tuples are **immutable**, which means that you cannot modify an existing `tuple`. Even `tuple1 += tuple2` does not mutate anything — it builds a brand-new tuple and rebinds the name, an O(n) copy each time. For that reason, concatenating many tuples in a loop is quadratic; collect into a `list` (or use `itertools.chain`) and convert once at the end instead.

## 62- How to join two `sets`?

To join two sets in Python, you can use the `union` method, which returns a new `set` that contains all the elements from both sets.

```Python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set3 = set1.union(set2)
print(set3)  # Output: {1, 2, 3, 4, 5}
```

If you want to modify an existing set in place, you can use the `update` method. This method adds all the elements from one set to another set, without creating a new set:

```Python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}
```

The operator spellings are equally idiomatic: `set1 | set2` is union, and `set1 |= set2` updates in place. The same pairing covers the other set operations — `&`/`intersection`, `-`/`difference`, `^`/`symmetric_difference`. One practical difference worth knowing: the methods accept any iterable (`set1.union([4, 5])` works), while the operators require both operands to be sets.

## 63- What is the difference between Python's list methods append and extend?

The `append` method adds an element to the end of a list. It takes a single element as an argument and does not return a new list.

The `extend` method adds all the elements of an iterable (such as a list) to the end of the list. It takes an iterable as an argument and does not return a new list.

Here is an example:

```Python
list1 = [1, 2, 3]
list1.append(4)
print(list1)  # prints [1, 2, 3, 4]

list2 = [5, 6, 7]
list1.extend(list2)
print(list1)  # prints [1, 2, 3, 4, 5, 6, 7]
```

Neither method creates a new list — both mutate the existing list in place and return `None`. The real performance distinction is simply how much work there is to do: `append` is amortised O(1) because it adds exactly one element, while `extend(iterable)` is O(k) for k elements added — and calling `extend` once is faster than calling `append` k times in a loop, since it avoids k method-call round-trips.

The gotcha interviewers fish for is what happens when you pass a _list_ to `append`:

```Python
lst = [1, 2, 3]
lst.append([4, 5])
print(lst)  # [1, 2, 3, [4, 5]]  <- the list goes in as ONE nested element

lst = [1, 2, 3]
lst.extend([4, 5])
print(lst)  # [1, 2, 3, 4, 5]    <- the elements are added individually
```

Also note that `extend` accepts any iterable — a tuple, set, generator, or string. That last one is a classic accident: `lst.extend("ab")` adds `'a'` and `'b'` as two separate elements. `lst += iterable` is equivalent to `extend` (in-place), whereas `lst + other` builds a new list and requires both operands to be lists.

## 64- How to implement bubble sort in Python?

```Python
def bubble_sort(lst):
  # Set swap to True to enter the loop
  swap = True
  # Repeat the loop until no swaps are needed
  while swap:
    # Set swap to False to start the loop
    swap = False
    # Iterate through the list
    for i in range(len(lst) - 1):
      # Check if the current element is greater than the next element
      if lst[i] > lst[i + 1]:
        # Swap the elements
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
        # Set swap to True to continue the loop
        swap = True
  # Return the sorted list
  return lst
```

**Function call:**

```Python
sorted_list = bubble_sort([5, 2, 8, 1, 9])
print(sorted_list)  # [1, 2, 5, 8, 9]
```

**_Time Complexity:_**

- Best case: **O(n)** — the `swap` flag makes one clean pass over already-sorted input enough to stop
- Average case: **O(n<sup>2</sup>)**
- Worst case: **O(n<sup>2</sup>)**

Bubble sort is a teaching algorithm; its one redeeming property is the O(n) early exit on nearly-sorted data. In real code, `sorted()` / `list.sort()` use Timsort — a hybrid stable sort that is O(n log n) worst case and also exploits existing order for O(n) best case.

## 65- How to implement Heap sort in Python?

```Python
def heap_sort(lst):
  # Create an empty list to store the extracted elements
  sorted_list = []
  # Convert the input list into a max heap
  heapify(lst)
  # Keep extracting the root element (maximum value) from the heap
  # until it is empty
  while lst:
    # Extract the root element from the heap and append it to the
    # sorted list
    sorted_list.append(heappop(lst))
  # The elements were extracted largest-first, so reverse for ascending order
  sorted_list.reverse()
  # Return the sorted list
  return sorted_list

def heapify(lst):
  # Start from the last parent node
  start = (len(lst) - 2) // 2
  # Sift down each node to create a max heap
  while start >= 0:
    sift_down(lst, start, len(lst) - 1)
    start -= 1

def sift_down(lst, start, end):
  # Set the root as the starting element
  root = start
  # While the root has a child
  while root * 2 + 1 <= end:
    # Set the child as the root's left child
    child = root * 2 + 1
    # If the child has a sibling and the sibling is greater than the
    # child, set the sibling as the child
    if child + 1 <= end and lst[child] < lst[child + 1]:
      child += 1
    # If the child is greater than the root, swap them
    if lst[root] < lst[child]:
      lst[root], lst[child] = lst[child], lst[root]
      # Set the child as the new root
      root = child
    # If no swap is needed, exit the loop
    else:
      return

def heappop(lst):
  # Save the root (maximum value) and the last element
  root = lst[0]
  last = lst.pop()
  # If the heap is not empty, set the last element as the root and
  # sift it down
  if lst:
    lst[0] = last
    sift_down(lst, 0, len(lst) - 1)
  # Return the root
  return root
```

**Function call:**

```Python
sorted_list = heap_sort([5, 2, 8, 1, 9])
print(sorted_list)  # [1, 2, 5, 8, 9]
```

Without the final `reverse()`, a max-heap pops its largest element first, so the extracted order is descending — `[9, 8, 5, 2, 1]`. (The textbook in-place variant avoids the second list entirely: swap the root with the last element, shrink the heap boundary, and sift down — the array ends up ascending with O(1) extra space.)

In practice, use the standard library's `heapq`, which implements a **min**-heap, so popping yields ascending order directly:

```Python
import heapq

def heap_sort_stdlib(lst):
    heapq.heapify(lst)                                   # O(n), in place
    return [heapq.heappop(lst) for _ in range(len(lst))]  # n pops, O(log n) each

print(heap_sort_stdlib([5, 2, 8, 1, 9]))  # [1, 2, 5, 8, 9]
```

**_Time Complexity:_**

- Best case: **O(n log(n))**
- Average case: **O(n log(n))**
- Worst case: **O(n log(n))**

Building the heap is O(n); each of the n extractions costs O(log n). Heap sort is not stable, but it is the classic answer when you need guaranteed O(n log n) with O(1) auxiliary space (in the in-place variant).

## 66- How to implement Insertion sort in Python?

```Python
def insertion_sort(lst):
  # Iterate through the list, starting from the second element
  for i in range(1, len(lst)):
    # Save the current element
    current = lst[i]
    # Set the position (j) as the index of the previous element
    j = i - 1
    # Keep moving the current element to the left as long as it is
    # smaller than the elements to its left
    while j >= 0 and current < lst[j]:
      lst[j + 1] = lst[j]
      j -= 1
    # When the correct position is found, insert the current element
    lst[j + 1] = current
  # Return the sorted list
  return lst

```

**Function call:**

```Python
sorted_list = insertion_sort([5, 2, 8, 1, 9])
print(sorted_list)  # [1, 2, 5, 8, 9]
```

**_Time Complexity:_**

- Best case: **O(n)**
- Average case: **O(n<sup>2</sup>)**
- Worst case: **O(n<sup>2</sup>)**

## 67- How to implement Merge sort in Python?

```Python
def merge_sort(lst):
  # If the input list is empty or has only one element, return it
  if len(lst) <= 1:
    return lst
  # Split the list into two halves
  mid = len(lst) // 2
  left = lst[:mid]
  right = lst[mid:]
  # Recursively sort the two halves
  left = merge_sort(left)
  right = merge_sort(right)
  # Merge the sorted halves and return the result
  return merge(left, right)

def merge(left, right):
  # Create an empty list to store the merged elements
  merged = []
  # Set the indices for the left and right lists
  left_index = 0
  right_index = 0
  # While there are elements in both lists
  while left_index < len(left) and right_index < len(right):
    # If the left element is smaller or equal, take it first: taking from
    # the LEFT on ties is what makes the sort stable
    if left[left_index] <= right[right_index]:
      merged.append(left[left_index])
      left_index += 1
    # If the right element is smaller, add it to the merged list
    # and increment the right index
    else:
      merged.append(right[right_index])
      right_index += 1
  # Add the remaining elements (if any) to the merged list
  merged.extend(left[left_index:])
  merged.extend(right[right_index:])
  # Return the merged list
  return merged

```

**Function call:**

```Python
sorted_list = merge_sort([5, 2, 8, 1, 9])
print(sorted_list)  # [1, 2, 5, 8, 9]
```

**_Time Complexity:_**

- Best case: **O(n log(n))**
- Average case: **O(n log(n))**
- Worst case: **O(n log(n))**

Merge sort is **stable** (equal elements keep their original relative order — guaranteed by the `<=` in `merge`) at the cost of O(n) auxiliary space. Python's built-in Timsort is a heavily optimised merge-sort/insertion-sort hybrid, which is why stability is guaranteed for `sorted()` and `list.sort()`.

## 68- How to implement Quick Sort in Python?

```Python
def quick_sort(lst):
  # If the input list has fewer than 2 elements, return it
  if len(lst) < 2:
    return lst
  # Set the pivot as the first element in the list
  pivot = lst[0]
  # Create the lists for elements less than and greater than the pivot
  less_than = [element for element in lst[1:] if element <= pivot]
  greater_than = [element for element in lst[1:] if element > pivot]
  # Recursively sort the two lists and return the result
  return quick_sort(less_than) + [pivot] + quick_sort(greater_than)
```

**Function call:**

```Python
sorted_list = quick_sort([5, 2, 8, 1, 9])
print(sorted_list)  # [1, 2, 5, 8, 9]
```

**_Time Complexity:_**

- Best case: **O(n log(n))**
- Average case: **O(n log(n))**
- Worst case: **O(n<sup>2</sup>)**

Two things to say about this elegant version: it is **not in place** (each level builds new lists, so O(n) extra space per level), and choosing the **first element as pivot** makes already-sorted input the worst case — every partition is maximally lopsided, degrading to O(n²) and deep recursion. Picking a random pivot (or median-of-three) makes that pathological case vanishingly unlikely; the in-place Lomuto/Hoare partition schemes are the standard follow-up whiteboard exercise.

## 69- How to implement Selection sort in Python?

```Python
def selection_sort(lst):
  # Iterate through the list, starting from the first element
  for i in range(len(lst)):
    # Set the minimum element as the current element
    minimum = i
    # Find the minimum element in the remaining list
    for j in range(i + 1, len(lst)):
      if lst[j] < lst[minimum]:
        minimum = j
    # If the minimum element is not the current element, swap them
    if minimum != i:
      lst[i], lst[minimum] = lst[minimum], lst[i]
  # Return the sorted list
  return lst
```

**Function call:**

```Python
sorted_list = selection_sort([5, 2, 8, 1, 9])
print(sorted_list)  # [1, 2, 5, 8, 9]
```

**_Time Complexity:_**

- Best case: **O(n<sup>2</sup>)**
- Average case: **O(n<sup>2</sup>)**
- Worst case: **O(n<sup>2</sup>)**

## 70- How to implement Shell sort in Python?

```Python
def shell_sort(arr):
  gap = len(arr) // 2
  while gap > 0:
    for i in range(gap, len(arr)):
      temp = arr[i]
      j = i
      while j >= gap and arr[j - gap] > temp:
        arr[j] = arr[j - gap]
        j -= gap
      arr[j] = temp
    gap //= 2
  return arr
```

**Function call:**

```Python
sorted_list = shell_sort([3, 4, 2, 1, 6, 5])
print(sorted_list)  # [1, 2, 3, 4, 5, 6]
```

**_Time Complexity:_** (for the gap sequence used here — halving the gap each round, Shell's original sequence)

- Best case: **O(n log n)** — already-sorted input
- Average case: depends on the gap sequence; roughly **O(n<sup>3/2</sup>)** for this one
- Worst case: **O(n<sup>2</sup>)**

Shell sort is insertion sort performed over progressively smaller gaps, so far-apart elements move long distances early. Its complexity is governed entirely by the gap sequence — better sequences (Knuth's `3k+1`, Ciura's empirical sequence) improve the worst case to below O(n²) — and no gap sequence makes it beat O(n log n) sorts asymptotically. It is unstable, in place, and mostly of historical/embedded interest.

## 71- What are the commands that are used to copy an object in Python?

There are several ways to copy an object in Python. Here are some of the most common methods:

- Using the `copy` module:

  ```Python
  import copy
  new_object = copy.copy(old_object)
  ```

  This creates a shallow copy of the object. If the object contains references to other objects, the copy will contain references to the same objects as the original.

- Using the `deepcopy` function:

  ```Python
  import copy
  new_object = copy.deepcopy(old_object)
  ```

  This creates a deep copy of the object. If the object contains references to other objects, the copy will contain copies of those objects as well, rather than references to the same objects.

- Using the `copy()` method:

  ```Python
  new_object = old_object.copy()
  ```

  This creates a shallow copy of the object. This method is available for objects that support the `copy` protocol (e.g., lists, dictionaries, sets, etc.).

A few equivalent idioms you will meet in real code: `lst[:]` and `list(lst)` shallow-copy a list, `dict(d)` and `d | {}` shallow-copy a dict, and since Python 3.3 sequences also expose `.copy()` directly. All of these are shallow — for anything nested, only `copy.deepcopy` duplicates the inner objects. Custom classes can hook into the mechanism by defining `__copy__` and `__deepcopy__`.

## 72- What is the difference between deep and shallow copy?

Both produce a new outer object; the difference is what happens to the objects **inside** it.

- A **shallow copy** creates a new container whose slots hold references to the _same_ inner objects as the original. Only the top level is duplicated.
- A **deep copy** recursively duplicates everything reachable, so the copy shares no mutable state with the original.

The distinction only matters when the container holds **mutable** objects. Watch what happens to a nested list:

```Python
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0].append(99)       # mutate an INNER list

print(shallow[0])   # [1, 2, 99]  <- shallow copy sees the change (shared inner object)
print(deep[0])      # [1, 2]      <- deep copy is unaffected

original.append([5, 6])      # mutate the OUTER list

print(len(shallow))  # 2  <- the outer level WAS duplicated, so this is not shared
```

Practical notes a senior engineer is expected to add:

- **Cost**: shallow copy is O(n) over the top level only; `deepcopy` walks the entire object graph, allocating as it goes, and is dramatically slower on large structures. Don't deep-copy defensively "just in case".
- **Cycles and sharing**: `copy.deepcopy` handles self-referencing structures correctly — it keeps a `memo` dict of already-copied objects, so cycles don't recurse forever and internal sharing is preserved in the copy.
- **Immutables are not really copied**: for ints, strings, and tuples of immutables, both copy forms may return the same objects — that is safe precisely because those objects can never change.
- The multiplication trap is the same bug in disguise: `[[0] * 3] * 2` builds two references to _one_ inner list; use a comprehension (`[[0] * 3 for _ in range(2)]`) to get independent rows.

## 73- How can the ternary operators be used in Python?

In Python, the ternary operator is known as the conditional operator or ternary conditional operator. It is an operator that takes three arguments: a condition, a result for the condition being true, and a result for the condition being false.

The syntax for the ternary operator is:

```Python
result = expression1 if condition else expression2
```

Here, `expression1` and `expression2` are the results that are returned if the condition is true or false, respectively.

Here's an example of how you can use the ternary operator to assign a value to a variable based on a condition:

```Python
x = 10
y = 20
max_value = x if x > y else y
print(max_value)
```

In this example, the condition `x > y` is false, so `y` is assigned to `max_value`. The output of this code will be **`20`**.

You can also use the ternary operator to return a value from a function based on a condition:

```Python
def get_max_value(x, y):
    return x if x > y else y

max_value = get_max_value(10, 20)
print(max_value)
```

In this example, the function `get_max_value()` returns `x` if `x` is greater than `y`, and returns `y` if `x` is not greater than `y`. When called with the arguments `(10, 20)`, the function will return `20`.

## 74- What will be the output of the code below?

```Python
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)
```

**The output:**

```Python
list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']
```

- In the first call to `extendList()`, the default value of the list is used, which is an empty list `[]`. The value `10` is appended to this list, and the modified list is returned. This list is assigned to `list1`.

- In the second call to `extendList()`, a new list `[123]` is passed as the value for the list parameter, so the default value is not used. The value `123` is appended to this list, and the modified list is returned and assigned to `list2`.

- In the third call to `extendList()`, the default value of the list is used again. This time, the default value is the list that was modified in the first call to the function, which contains the value `10`. The value `'a'` is appended to this list, and the modified list is returned and assigned to `list3`.
  This behavior occurs because default values are evaluated when the function is defined, not when it is called. In this case, the default value of the list parameter is an empty list `[]`, which is evaluated when the `extendList()` function is defined. This means that the same `list` object is used as the default value for the `list` parameter every time the `extendList()` function is called, unless a different value is provided for the list parameter in the function call.

The definition of the `extendList` function could be modified as follows, though, to always begin a new list when no `list` argument is specified, which is more likely to have been the desired behavior:

```Python
def extendList(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list
```

The `list=None` / `if list is None` pattern is the standard idiom for mutable defaults. (Separately, naming a parameter `list` shadows the built-in `list` type inside the function — harmless here, but poor practice; `items` or `lst` would be better.)

## 75- What will be the output of the code below?

```Python
def multipliers():
  return [lambda x : i * x for i in range(4)]

print([m(2) for m in multipliers()])
```

The output of the above code will be `[6, 6, 6, 6]`.

The reason for this is that Python’s closures are late binding. This means that the values of variables used in closures are looked up at the time the inner function is called. So as a result, when any of the functions returned by `multipliers()` are called, the value of `i` is looked up in the surrounding scope at that time. By then, regardless of which of the returned functions is called, the `for` loop has been completed, and `i` is left with its final value of 3. Therefore, every returned function multiplies the value it is passed by `3`, so since a value of `2` is passed in the above code, they all return a value of `6` (i.e., 3 x 2).

The standard fix exploits the fact that **default arguments are evaluated at definition time** (the very behaviour that causes the previous question's bug is the cure here) — bind the current `i` as a default:

```Python
def multipliers():
    return [lambda x, i=i: i * x for i in range(4)]

print([m(2) for m in multipliers()])   # [0, 2, 4, 6]
```

Alternatives that achieve the same early binding: `functools.partial(operator.mul, i)`, or a factory function whose parameter captures each value in its own scope.

## 76- What will be the output of the code below?

```Python
class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)
```

**The output of the above code will be:**

```text
1 1 1
1 2 1
3 2 3
```

In Python, class variables are internally handled as dictionaries. If a variable name is not found in the dictionary of the current class, the class hierarchy (i.e., its parent classes) is searched until the referenced variable name is found (if the referenced variable name is not found in the class itself or anywhere in its hierarchy, an `AttributeError` occurs).

Therefore, setting `x = 1` in the `Parent` class makes the class variable `x` (with a value of 1) referenceable in that class and any of its children. That’s why the first `print` statement outputs `1 1 1`.

Subsequently, if any of its child classes overrides that value (for example, when we execute the statement `Child1.x = 2`), then the value is changed in that child only. That’s why the second `print` statement outputs `1 2 1`.

Finally, if the value is then changed in the `Parent` (for example, when we execute the statement `Parent.x = 3`), that change is reflected also by any children that have not yet overridden the value (which in this case would be `Child2`). That’s why the third print statement outputs `3 2 3`

## 77- What is `__slots__` in python?

It is a feature of Python classes that allows you to specify the attributes that an instance of the class should have. By default, Python classes create a dictionary for each instance to store its attributes. This dictionary takes up more memory than is necessary for most objects and can cause performance problems, especially for objects with a large number of attributes.

Using `__slots__` can help mitigate this issue by allowing you to specify exactly which attributes an instance should have, and the Python interpreter will use a more efficient representation for the instance. This can save memory and improve performance.

Here's an example of how you might use `__slots__` in a Python class:

```Python
class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y
```

In this example, the Point class has two attributes: `x` and `y`. By specifying these attributes in `__slots__`, we are telling the Python interpreter that instances of the Point class should only have these two attributes and no others.

There are a few things to note about using `__slots__`:

- `__slots__` lists instance attributes only; methods and class attributes are defined as usual in the class body.

- If you define `__slots__` in a class, its instances will not have a `__dict__`, so assigning any attribute not listed raises `AttributeError` — and instances also lose `__weakref__` unless you include it in the slots. Under the hood, slotted attributes are implemented as descriptors backed by fixed storage in the instance, which is where both the memory saving and the small attribute-access speedup come from.

- **Inheritance is the classic trap**: if any class in the hierarchy lacks `__slots__` (including the case where a subclass simply doesn't declare one), its instances get a `__dict__` anyway and the memory benefit silently evaporates. Every class in the chain must declare `__slots__` (an empty tuple `__slots__ = ()` is fine for mixins), and each class should list only its _new_ attributes.

- Using `__slots__` means committing to a fixed attribute set, which trades away Python's usual dynamism — no monkey-patching attributes onto instances, and tools that expect `vars(obj)` will not work. Reserve it for classes instantiated in large numbers (think millions of points, nodes, or rows), where the per-instance saving is real; measure with `sys.getsizeof` + `tracemalloc` rather than assuming. For plain data records, `dataclasses.dataclass(slots=True)` (Python 3.10+) generates the slots for you, and `NamedTuple` is a slot-like immutable alternative.

## 78- What is `__contains__` in python?

The `__contains__` method is a special method in Python that is used to implement the `in` operator. If a class defines a `__contains__` method, you can use the in operator to check if an instance of the class contains a particular value.

Here's an example of how you might use the `__contains__` method in a Python class:

```Python
class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __contains__(self, value):
        return value in (self.r, self.g, self.b)

color = Color(255, 0, 0)
print(100 in color)  # prints False
print(255 in color)  # prints True
print(0 in color)    # prints True - g and b are both 0
```

In this example, the `Color` class has a `__contains__` method that checks if the given value is one of the `r`, `g`, or `b` values of the `Color` instance. When you use the in operator with an instance of the `Color` class, it will call the `__contains__` method to determine whether the value is contained within the instance.

Worth knowing for the follow-up question: `in` works even **without** `__contains__`. If the method is absent, Python falls back to iterating the object (`__iter__`), comparing each element; failing that, it tries the old `__getitem__` integer-indexing protocol. Defining `__contains__` is therefore an optimisation and a semantic statement — e.g. `dict` and `set` implement it as an O(1) hash lookup rather than a linear scan. The result of `__contains__` is also interpreted as a boolean, and `not in` simply negates it.

## 79- What is a "callable"?

A callable is any object that can be invoked with parentheses — `obj(...)`. That covers functions, methods, classes themselves (calling a class constructs an instance), and instances of any class that defines the `__call__` special method.

Here are a few examples of callables in Python:

- Functions:

  ```Python
  def greet(name):
      print(f"Hello, {name}!")

  greet("Alice")  # prints "Hello, Alice!"
  ```

- Methods:

  ```Python
  class Greeter:
      def __init__(self, name):
          self.name = name

      def greet(self):
          print(f"Hello, {self.name}!")

  g = Greeter("Bob")
  g.greet()  # prints "Hello, Bob!"
  ```

- Classes — `Greeter` itself is callable; calling it runs `__new__` then `__init__` and returns the new instance. This is also why `int`, `str`, and `list` can be "called": they are classes.

- Objects with the `__call__` method:

  ```Python
  class CallableClass:
      def __call__(self, *args, **kwargs):
          print("Called with arguments:", args, kwargs)

  cc = CallableClass()
  cc(1, 2, 3, a=4, b=5)  # prints "Called with arguments: (1, 2, 3) {'a': 4, 'b': 5}"
  ```

You can check if an object is callable using the `callable()` built-in function:

```Python
print(callable(greet))    # prints True
print(callable(g.greet))  # prints True
print(callable(Greeter))  # prints True - classes are callable
print(callable(cc))       # prints True
print(callable(1))        # prints False
```

Callable instances via `__call__` are the idiomatic way to build **stateful functions** — objects that behave like functions but carry configuration or accumulated state (rate limiters, counters, decorators-with-arguments implemented as classes). `functools.partial` objects and `lambda`s are callables too; "accepts any callable" is exactly the flexibility that lets APIs like `sorted(key=...)`, `map`, and framework route handlers take all of these interchangeably.

## 80- How would you `XOR` in Python?

The answer depends on whether you mean **bitwise** XOR on integers or **logical** XOR on truth values — Python has an operator for the first and idioms for the second.

**Bitwise XOR** uses the `^` operator (there is no `^^`):

```Python
print(0b1100 ^ 0b1010)   # 6, i.e. 0b0110 - differing bits set
print(5 ^ 3)             # 6
x = 12
x ^= 10                  # augmented assignment works too
```

`^` also has non-integer uses: on sets it is symmetric difference (`{1, 2} ^ {2, 3}` → `{1, 3}`), and XOR-ing a value with itself is `0` — the basis of the classic "find the element that appears an odd number of times" trick: `functools.reduce(operator.xor, nums)`.

**Logical XOR** ("exactly one of the two is truthy") has no dedicated operator; the idioms are:

1. `bool(a) != bool(b)` — the clearest and most common
2. `bool(a) ^ bool(b)` — works because `bool` is an `int` subclass (`True ^ False` → `True`)
3. `(a and not b) or (not a and b)` — spelled out with logic operators

`operator.xor(a, b)` is simply a function version of `^`, so it is _bitwise_ — `operator.xor(2, 4)` is `6`, not a truth test. Wrap the arguments in `bool()` if you want it to behave logically.

## 81- What is introspection/reflection and does Python support it?

Introspection is the ability to examine an object at runtime. Python has a `dir()` function that supports examining the attributes of an object, `type()` to check the object type, `isinstance()`, etc. While introspection is a passive examination of the objects, reflection is a more powerful tool where we can modify objects at runtime and access them dynamically. E.g.

- `setattr()` adds or modifies an object's attribute;
- `getattr()` gets the value of an attribute of an object.

It can even invoke functions dynamically - `getattr(my_obj, "my_func_name")()`

Rounding out the toolbox: `hasattr()` probes for an attribute, `vars(obj)` returns the instance `__dict__`, `id()` gives the object's identity, and the `inspect` module goes deeper — `inspect.signature()` reads a function's parameters, `inspect.getsource()` retrieves its source code, and `inspect.getmembers()` enumerates attributes with filters. This runtime openness is what makes frameworks possible: ORMs discover model fields, pytest finds `test_*` functions, and serialisers walk objects — all via introspection rather than code generation.

## 82- What will be the output of lines 2, 4, 6, and 8 from the following code, and why?

```Python
list = [ [ ] ] * 5
list  # output?
list[0].append(10)
list  # output?
list[1].append(20)
list  # output?
list.append(30)
list  # output?
```

**The output:**

```Python
list = [ [ ] ] * 5
list  # output: [[], [], [], [], []]
list[0].append(10)
list  # output: [[10], [10], [10], [10], [10]]
list[1].append(20)
list  # output: [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
list.append(30)
list  # output: [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]
```

In the first line, `list` is initialized with 5 references to the **same** single empty list — `*` copies references, it does not clone objects. When you append `10` through the first reference, you are modifying the one shared inner list, which is why the change shows through all five elements. In the fourth line, you are appending to the _outer_ list, which is why `30` lands at the end rather than inside any inner list.

The fix is a comprehension, which evaluates `[]` freshly on every iteration:

```Python
grid = [[] for _ in range(5)]
grid[0].append(10)
print(grid)   # [[10], [], [], [], []]
```

The rule of thumb: `[x] * n` is fine when `x` is immutable (numbers, strings), and a latent bug when `x` is mutable. (The snippet also shadows the built-in `list` type by using it as a variable name — after line 1, `list()` no longer constructs lists in that scope. Avoid that in real code.)

## 83- Write a function that prints the least integer that is not present in a given list and cannot be represented by the summation of the sub-elements of the list

This is the classic "smallest unrepresentable sum" problem: given a list of positive integers, find the smallest positive integer that cannot be written as the sum of any subset of the list. There is a beautiful greedy O(n log n) solution:

```Python
def find_least_integer(lst):
    # Sort the list in ascending order
    lst = sorted(lst)

    # Invariant: every value in [1, reach) is representable as a subset sum
    reach = 1

    for num in lst:
        # If the next number leaves a gap below it, reach can never be filled
        if num > reach:
            break
        # Otherwise every value in [1, reach + num) is now representable
        reach += num

    return reach
```

The key insight is the invariant: after processing some prefix of the sorted list, if every integer in `[1, reach)` is achievable, then a new number `num <= reach` extends that range to `[1, reach + num)` — take any existing sum and optionally add `num`. But if `num > reach`, then `reach` itself can never be formed: all remaining numbers are at least `num`, which is already too big, so `reach` is the answer.

Note that a simpler "walk until a number is missing" loop (incrementing only when `num == least_int`) answers a _different_ question — the smallest **missing** integer — and gets this problem wrong: for `[1, 1, 3]` it would return `2`, yet `1 + 1 = 2` is clearly representable; the true answer is `6` (`1+1+3 = 5`, and `6` cannot be formed).

Here is an example of how to use the function:

```Python
print(find_least_integer([1, 3, 6, 10, 11, 15]))  # Output: 2  (no way to form 2)
print(find_least_integer([1, 1, 3]))              # Output: 6
print(find_least_integer([1, 2, 4, 8]))           # Output: 16 (powers of two cover 1-15)
```

## 84- How do you reverse a list? Can you come up with at least three ways?

Here are three ways to reverse a list in Python:

1. Using the `reverse()` method:

   ```Python
   lst = [1, 2, 3, 4, 5]
   lst.reverse()
   print(lst)  # Output: [5, 4, 3, 2, 1]
   ```

2. Using slicing with a step of -1:

   ```Python
   lst = [1, 2, 3, 4, 5]
   lst = lst[::-1]
   print(lst)  # Output: [5, 4, 3, 2, 1]
   ```

3. Using a `for` loop:

   ```Python
   lst = [1, 2, 3, 4, 5]
   reversed_lst = []
   for i in range(len(lst)-1, -1, -1):
       reversed_lst.append(lst[i])
   print(reversed_lst)  # Output: [5, 4, 3, 2, 1]
   ```

All three produce the same _ordering_, but they differ in an important way: `reverse()` mutates the original list **in place and returns `None`** (so `lst = lst.reverse()` is a classic bug that leaves you with `None`), while slicing and the loop build a _new_ list and leave the original untouched.

A fourth way — often the best — is the built-in `reversed()`:

```Python
lst = [1, 2, 3, 4, 5]
for x in reversed(lst):      # lazy iterator: no copy made at all
    print(x)

rev = list(reversed(lst))    # materialise when you actually need a list
```

`reversed()` returns a lazy iterator over the existing list, so it costs O(1) memory — the right choice when you only need to _iterate_ backwards. Use `lst.reverse()` when you want the list itself permanently flipped, and `lst[::-1]` when you need a reversed copy as an expression (it also works on strings and tuples, which have no `.reverse()` method).

## 85- How does Python execute code?

When you run a Python program, the interpreter executes the code you have written in a sequence of steps.

Here is a general outline of how the Python interpreter executes code:

1. The source is **parsed** — tokenised and built into an abstract syntax tree (AST); syntax errors surface at this stage, before anything runs.
2. The AST is **compiled to bytecode**, a compact instruction set for CPython's stack-based virtual machine (you can inspect it with the `dis` module). For imported modules the bytecode is cached on disk in `__pycache__` to skip recompilation next time.
3. The **Python virtual machine** (the eval loop) then executes the bytecode instruction by instruction.
4. As the interpreter executes the instructions, it may encounter statements that define variables, functions, or classes. When this happens, the interpreter creates the corresponding objects in memory and assigns them to the specified names — `def` and `class` are executable statements, not declarations.
5. The interpreter may also encounter statements that call functions or methods. When this happens, the interpreter looks up the function or method and executes the code it contains.
6. If the interpreter encounters an error while executing the code, it will raise an exception. If the error is not caught by the code, the interpreter will print a traceback and stop executing the program.

So Python is neither purely "interpreted" nor compiled to machine code: CPython compiles to bytecode and interprets that. (CPython 3.13+ additionally ships an experimental JIT, and alternative implementations like PyPy have JIT-compiled hot paths to machine code for years.)

## 86- What is `__pycache__`?

The `__pycache__` directory is a directory that is created by the Python interpreter to store compiled bytecode files. When you run a Python program, the interpreter converts the source code into a form that is more efficient to execute. This conversion process is known as compiling. The compiled bytecode files are stored in the `__pycache__` directory so that they can be used in future executions of the program without the need to recompile the source code.

The `__pycache__` directory is typically located in the same directory as the Python source files that were used to create it. It is created automatically by the interpreter, and you do not need to worry about managing it manually.

Note that the `__pycache__` directory and the compiled bytecode files it contains are specific to a particular version of Python. This means that if you change the version of Python that you are using, the interpreter will create a new `__pycache__` directory with compiled bytecode files that are compatible with the new version of Python.

## 87- What is the unittest in Python?

`unittest` is a unit testing framework in Python. It is a part of the Python Standard Library, and it is used to test small units of code, such as individual functions or methods.

The `unittest` framework provides a set of tools for organizing and running tests, as well as for verifying the correctness of the code being tested. It includes a set of assertion methods that you can use to check the output of your code and ensure that it is correct.

To use the `unittest` framework, you define a series of test cases, which are individual units of testing that each test a specific aspect of your code. Each test case is a subclass of the `unittest.TestCase` class, and it includes a series of test methods that define the tests to be run. You can then use the `unittest` test runner to discover and run the tests in your test cases.

Here is a simple example of how to use the `unittest` framework to test a function:

```Python
import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add_two_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_two_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)

if __name__ == '__main__':
    unittest.main()
```

In this example, the `TestAdd` class defines two test methods, `test_add_two_positive_numbers` and `test_add_two_negative_numbers`, which test the `add` function with different input values. The `unittest.main()` function is used to run the tests and report the results. Test discovery is name-based: the runner executes methods whose names start with `test_`, and `python -m unittest discover` finds test modules across a project.

Beyond `assertEqual`, the pieces used daily are: `setUp`/`tearDown` (fresh fixtures before/after every test method), `assertRaises` as a context manager for expected exceptions, `assertAlmostEqual` for floats, and `unittest.mock` for patching out dependencies:

```Python
class TestDivide(unittest.TestCase):
    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0
```

Worth saying in an interview: `unittest` is the standard library's xUnit-style framework, but much of the Python world uses **pytest**, which runs `unittest` suites unchanged while offering plain-`assert` tests, fixtures, and parametrisation with far less boilerplate.

## 88- What is the difference between xrange and range?

`range` and `xrange` are both functions that are used to generate a sequence of numbers. However, they differ in how they generate the numbers and in the type of object they return.

The `range` function generates a sequence of numbers by creating a list object that contains all of the numbers in the sequence. For example:

```Python
>>> range(5)
[0, 1, 2, 3, 4]
>>> range(2, 5)
[2, 3, 4]
>>> range(2, 10, 2)
[2, 4, 6, 8]
```

The `range` function is useful when you need to generate a sequence of numbers and you need to access the numbers multiple times or perform operations on them. However, it can be inefficient when generating large sequences of numbers, as it creates a new list object in memory to hold the numbers.

The `xrange` function generates the numbers lazily instead, returning an `xrange` object rather than a `list`. It is a common mistake to call it a generator — it is a lazy **sequence**: it computes values on demand like a generator would, but it also supports `len()`, indexing, and repeated iteration, none of which a generator allows. The point stands that `xrange` is far more memory-efficient than Python 2's `range` for large spans, since it never materialises the whole sequence.

For example:

```Python
>>> xrange(5)
xrange(5)
>>> list(xrange(5))
[0, 1, 2, 3, 4]
>>> xrange(2, 5)
xrange(2, 5)
>>> list(xrange(2, 5))
[2, 3, 4]
>>> xrange(2, 10, 2)
xrange(2, 10, 2)
>>> list(xrange(2, 10, 2))
[2, 4, 6, 8]
```

The `xrange` function was introduced in **`Python 2`** as a more efficient alternative to the `range`. In **`Python 3`**, the `range` function was redesigned along `xrange`'s lines, and `xrange` was removed from the language.

Python 3's `range` is in fact better than `xrange` ever was — it is a full lazy, immutable sequence:

```Python
r = range(1_000_000_000)   # instant: no billion-element list is built
print(len(r))              # 1000000000
print(r[500])              # 500 - O(1) indexing, computed arithmetically
print(999 in r)            # True - O(1) membership test for integers
print(list(r[:5]))         # [0, 1, 2, 3, 4] - slicing returns another range
```

Because it is a sequence (not a generator), a `range` can be iterated any number of times, and its `in` test for integers is constant-time arithmetic rather than a scan.

## 89- What is the use of `//` operator in Python?

In Python, the `//` operator is the floor division operator: it divides and then applies `floor()`, rounding the result **down toward negative infinity**.

For example:

```Python
>>> 5 / 2
2.5
>>> 5 // 2
2
>>> 5.0 // 2
2.0
```

Two precise points that the loose description "returns an integer" gets wrong:

- **The result type follows the operands, not the operation.** `int // int` gives an `int`, but if either operand is a float the result is a _float_ — `5.0 // 2` is `2.0`, not `2`.
- **Flooring is not truncation.** For negative results, `//` keeps rounding _down_, which surprises people expecting C-style truncation toward zero:

```Python
>>> -7 // 2
-4          # floor(-3.5) = -4, NOT -3
>>> 7 // -2
-4
>>> int(-7 / 2)
-3          # int() truncates toward zero - a different operation
```

Floor division pairs with the modulo operator through the invariant `a == (a // b) * b + (a % b)`, which is why `%` in Python always returns a result with the sign of the _divisor_ (`-7 % 2` is `1`, handy for wrapping indices). `divmod(a, b)` returns both at once. Typical uses: splitting into whole units and remainder (`minutes, seconds = divmod(total, 60)`), integer midpoints (`mid = (lo + hi) // 2`), and digit extraction (`n // 10`, `n % 10`).

```Python
>>> 10 // 3
3
>>> divmod(125, 60)
(2, 5)
>>> -7 % 2
1
```

## 90- How are dict and set implemented internally? What is the complexity of retrieving an item? How much memory do these structures consume?

In Python, both dictionaries (called `dict`) and `sets` are implemented using hash tables. A hash table is a data structure that uses a hash function to map keys to indices in an array, allowing for fast insertion, deletion, and lookup of keys.

In the case of `dict`, each key-value pair is stored in the hash table. The keys are used to calculate a hash value, which is used to determine the index in the array where the key-value pair should be stored. The value is then stored at that index. To retrieve a value from the `dict`, the hash function is used to calculate the index of the key-value pair, and the value is retrieved from that index.

The complexity of retrieving an item from a `dict` or a `set` is typical `O(1)` on average, meaning that it takes a constant amount of time to retrieve an item, regardless of the size of the `dict` or `set`. However, in the worst case, the complexity can be `O(n)`, meaning that it takes linear time to retrieve an item if the hash function is poorly designed and causes many keys to hash to the same index.

As for memory consumption, the amount of memory that a `dict` or `set` consumes depends on the number of keys it contains and the size of the keys and values. In general, `dict` and `set` objects use more memory than other data structures, such as lists and tuples, because they store the keys and values in addition to the overhead of the hash table data structure. However, the exact amount of memory consumed will depend on the specific keys and values being stored and on the implementation of the Python interpreter.

Implementation details worth knowing at a senior level:

- **Collisions are handled by open addressing**, not chaining: on a collision, CPython probes other slots in the same table (with a perturbation scheme that mixes in more hash bits), rather than hanging linked lists off buckets.
- **The table resizes by load factor.** A dict keeps at most ~2/3 of its slots occupied; passing that threshold triggers a grow-and-rehash. This is why inserts are _amortised_ O(1) — an individual insert can pay for a full O(n) rehash.
- **Modern dicts are "compact"** (CPython 3.6+): entries live in a dense array in insertion order, with the sparse hash table holding only small indices into it. This cut memory ~20-25% and is exactly why dicts preserve insertion order (guaranteed since 3.7). A `set` is essentially the same table without the values array — and sets do _not_ guarantee any order.
- **Keys must be hashable** (immutable built-ins, or objects defining a consistent `__hash__`/`__eq__` pair). Mutable containers like lists are unhashable precisely because a mutated key could never be found again.
- You can measure the overhead directly: `sys.getsizeof({})` versus `sys.getsizeof([])` shows the empty-container difference, and the gap grows with the sparse-slot overhead as items are added.

The practical consequence: membership tests are O(1) on dict/set versus O(n) on list/tuple, so the moment code does repeated `x in collection` checks over meaningful data sizes, converting the collection to a `set` is usually the single highest-value micro-optimisation available.

## 91- What is MRO in Python? How does it work?

In Python, MRO stands for "Method Resolution Order." It is a mechanism that is used to determine the order in which the methods of a class should be inherited when a class is derived from multiple base classes.

In Python, a class can be derived from multiple base classes, creating a class hierarchy. When a class is derived from multiple base classes, it is said to have multiple inheritance. In multiple inheritance, a class can inherit methods from multiple base classes, and it is important to determine the order in which these methods should be inherited to avoid conflicts.

The MRO of a class is the order in which the methods of the class and its base classes are searched when looking up a method. In Python, the MRO of a class is determined using the C3 linearization algorithm, which produces a linear order that preserves the local precedence order of the base classes.

Here is an example of a class hierarchy with multiple inheritance in Python:

```Python
class A:
    def foo(self):
        print("A.foo")

class B:
    def foo(self):
        print("B.foo")

class C:
    def foo(self):
        print("C.foo")

class D(B, C, A):
    pass
```

In this example, the class `D` is derived from the classes `B`, `C`, and `A`, in that order. The MRO of the `D` class is determined using the C3 linearization algorithm, and it is as follows:

```Python
D.__mro__ == (D, B, C, A, object)
```

This means that when looking up a method on an instance of the `D` class, the interpreter will first search the `D` class, then the `B` class, then the `C` class, then the `A` class, and finally the object class, which is the base class of all classes in Python.

The MRO is an important concept in Python because it determines the order in which methods are inherited and how conflicts are resolved when a class has multiple inheritance. Understanding how the MRO works is essential to understanding how multiple inheritance works in Python.

Three follow-ups an interviewer is likely to reach for:

- **C3 is more than left-to-right.** The linearization satisfies two constraints at once: a class always precedes its own bases, and the left-to-right order of the bases listed in every class definition is preserved. In diamond hierarchies this means a shared base appears _after_ all its subclasses, not immediately after the first parent (see the `super` question earlier in this file for a worked diamond).
- **Not every hierarchy has a valid MRO.** If the constraints contradict each other, Python refuses to create the class at all:

  ```Python
  class X(A, B): pass
  class Y(B, A): pass       # opposite order
  class Z(X, Y): pass       # TypeError: Cannot create a consistent MRO
  ```

- **`super()` is MRO traversal.** `super()` does not mean "my parent" — it means "the next class after mine in the MRO of the instance's actual type". That is what allows cooperative multiple inheritance and mixins to compose: each class calls `super()`, and the MRO threads one call through every class exactly once. Inspect it any time with `D.__mro__` or `D.mro()`.

## 92- How to distribute Python code?

There are several ways to distribute Python code, depending on the specific needs of your project. Here are a few common options:

1. **Packaging for PyPI (the modern workflow)**: Declare the package metadata in a `pyproject.toml` file — this has replaced the old `setup.py`/`distutils` approach (`distutils` was removed from the standard library in Python 3.12). Then build and upload:

   ```Bash
   python -m build        # produces a source distribution (.tar.gz) and a wheel (.whl)
   python -m twine upload dist/*
   ```

   Users then install it with `pip install your-package`. Tools like Poetry, Hatch, and uv wrap this same standards-based flow (PEP 517/518/621) with dependency management on top. `setuptools` still works fine as the build backend — but configured via `pyproject.toml`, with `setup.py` kept only for legacy or complex native builds.

2. **Distributing within a team without PyPI**: `pip` can install straight from a git URL (`pip install git+https://github.com/org/repo.git`), from a private index (`--index-url`, e.g. an internal devpi/Artifactory), or from a local wheel file. Wheels are the unit of distribution either way (see the wheels-vs-eggs question earlier).

3. **Distributing as a standalone executable**: To ship to users who do not have Python installed, bundle the interpreter and dependencies into one artifact with **PyInstaller** (the de facto standard, cross-platform), or alternatives like cx_Freeze, Briefcase (GUI apps), Nuitka (compiles to C), or `shiv`/`pex` (self-contained zipapps building on the stdlib `zipapp` module). The older `py2exe`/`py2app` tools fill the same niche but are platform-specific.

4. **Containers**: For services, the answer in practice is often a Docker image — the dependency story (OS libraries included) is pinned once and runs anywhere a container runtime exists.

## 93- How to work with Python transitive dependencies?

Transitive dependencies are dependencies that are required by a package that your code depends on. For example, if your code depends on the package `A`, and package `A` depends on package `B`, then package `B` is a transitive dependency of your code.

To work with transitive dependencies in Python, you typically use a package manager like `pip` to install and manage your dependencies. When you install a package using `pip`, it will automatically install any transitive dependencies that the package requires.

For example, suppose you have a Python project that depends on package `A`, which in turn depends on package `B`. To install these dependencies using `pip`, you can use the following command:

```Bash
pip install A
```

This will install both packages `A` and its transitive dependency, package `B`.

If you want to specify the exact version of a package and its transitive dependencies that you want to install, you can use the `-r` flag to specify a requirements file. A `requirements` file is a text file that lists the packages and their versions that your project depends on. For example:

```Python
A==1.0
B==2.0
```

To install the packages and their transitive dependencies from this requirements file, you can use the following command:

```Bash
pip install -r requirements.txt
```

This will install package `A` version **`1.0`** and its transitive dependency, package `B` version **`2.0`**.

Using a package manager like `pip` to manage your transitive dependencies is a good way to ensure that your code has the correct dependencies installed and to keep them up to date. It also makes it easier to share your code with others, as they can use the requirements file to install the correct dependencies for your project.

The senior-level practice is to separate **direct** dependencies from the **fully pinned** set:

- Declare only your direct dependencies with loose constraints (in `pyproject.toml`, or a hand-edited `requirements.in`).
- Generate a **lock file** pinning every transitive dependency to an exact version for reproducible deploys — `pip freeze > requirements.txt` is the crude form; `pip-compile` (pip-tools), Poetry, or uv produce proper lock files with hashes.
- `pip install` resolves the whole graph and refuses genuinely conflicting constraints (since the 2020 resolver); `pip check` verifies an existing environment, and `pipdeptree` visualises who pulls in what — the first tool to reach for when a mystery package appears in your environment.
- Do all of this inside a **virtual environment** (`python -m venv`), so project graphs cannot contaminate each other or the system Python.

## 94- What is the output of this code?

```Python
def Foo():
    yield 42;
    return 666
```

Strictly speaking this code produces **no output** — it only defines a function. The interesting question is what happens when you use it.

`Foo` is a generator function, as indicated by the `yield` keyword. Calling it returns a generator object without executing the body. Iterating runs the body up to `yield`, producing `42` and suspending; resuming continues to the `return` statement.

Here is the part worth knowing: `return 666` inside a generator does **not** produce `666` as an iteration value. It terminates the generator by raising `StopIteration`, and the returned value is carried on the exception as its `.value` attribute (PEP 380):

```Python
print(list(Foo()))    # [42] - iteration only ever sees yielded values

g = Foo()
print(next(g))        # 42
try:
    next(g)
except StopIteration as e:
    print(e.value)    # 666
```

A `for` loop swallows the `StopIteration` silently, so the `666` is invisible to ordinary iteration. The mechanism exists for **generator delegation**: inside another generator, `result = yield from Foo()` re-yields the `42` and binds `result` to `666`. This is the foundation coroutines were originally built on, and it is why "what does `return` do in a generator?" is a favourite senior-level probe. (The trailing semicolon after `yield 42;` is legal but un-Pythonic.)

## 95- What is the output of this code?

```Python
_MangledGlobal__mangled = 23

class MangledGlobal:
    def test(self):
        return __mangled
```

The `MangledGlobal` class contains a reference to a global variable with a name that has been "`mangled`" to avoid name conflicts with other variables in the global namespace.

In Python, the name `mangling` is a technique that is used to protect instance variables in a class from being accidentally overwritten by derived classes. Name `mangling` works by adding a double underscore prefix to the name of an instance variable, which causes the interpreter to automatically rename the variable in a way that is unique to the class.

The detail this puzzle turns on: mangling is applied **at compile time to any identifier of the form `__name` appearing anywhere in a class body** — not just to attribute access through `self`. So the bare reference `__mangled` inside `test()` is textually rewritten to `_MangledGlobal__mangled` before the code ever runs. At call time, ordinary name lookup then proceeds (local → global): there is no local by that name, but the _global_ `_MangledGlobal__mangled = 23` matches the rewritten name, so `test()` returns `23`.

Here is the example in action:

```Python
_MangledGlobal__mangled = 23

class MangledGlobal:
    def test(self):
        return __mangled   # compiled as: return _MangledGlobal__mangled

mg = MangledGlobal()
print(mg.test())  # Output: 23
print(_MangledGlobal__mangled)  # Output: 23
```

(Note that `self.__mangled` would _not_ work here — that mangles to `self._MangledGlobal__mangled`, an attribute lookup on the instance, which raises `AttributeError` because no such attribute was ever set. The trick works precisely because the reference is a bare name, which falls through to the global namespace.)

Mangling applies only to identifiers with **two leading underscores and at most one trailing underscore** — so `__x` is mangled, while `__x__` (dunders) and `_x` are not. Its intended purpose is to keep a base class's private attributes from being accidentally overridden in subclasses, since each class mangles to its own name.

Note that while the name `mangling` is intended to protect instance variables from being overwritten by derived classes, it is not a security feature and should not be relied upon to protect sensitive data. The name `mangling` can be easily bypassed by using the mangled name directly, as shown in the example above.

## 96- What is packing and unpacking in Python?

In Python, packing and unpacking refer to two related concepts involving the conversion of data between different structures.

Packing refers to the process of taking multiple values or items and combining them into a single data structure. This is often done using tuples, which are a type of immutable data structure in Python. For example, we can create a tuple that contains three elements like this:

```Python
my_tuple = (1, "hello", True)
```

Unpacking, on the other hand, refers to the process of taking a data structure and splitting it into multiple values or items. This is often done using tuples, lists, or dictionaries. For example, we can unpack a tuple into multiple variables like this:

```Python
my_tuple = (1, "hello", True)
a, b, c = my_tuple
```

Also, the asterisk (\*) symbol can be used in unpacking expressions to represent a variable number of elements. This is sometimes referred to as "extended unpacking".

The asterisk can be used in several ways:

1. Unpacking into individual variables: If you have a list or tuple with an unknown number of elements, you can use the asterisk to unpack the elements into individual variables. For example:

   ```Python
   my_list = [1, 2, 3, 4, 5]
   a, b, *rest = my_list
   print(a) # 1
   print(b) # 2
   print(rest) # [3, 4, 5]
   ```

2. Unpacking in function calls: The asterisk can also be used to unpack arguments in function calls. For example:

   ```Python
   def my_function(a, b, c):
       print(a, b, c)

   my_list = [1, 2, 3]
   my_function(*my_list)
   ```

In this example, the elements of `my_list` are unpacked and passed as arguments to the function `my_function`.

The picture is completed by the double asterisk and the packing side of function signatures:

1. **Packing in function signatures**: `*args` packs surplus positional arguments into a tuple and `**kwargs` packs surplus keyword arguments into a dict — packing and unpacking are the same syntax viewed from opposite ends:

   ```Python
   def report(*args, **kwargs):
       print(args, kwargs)

   report(1, 2, flag=True)   # (1, 2) {'flag': True}
   ```

2. **`**` unpacking in calls and literals**: a dict can be unpacked into keyword arguments, and both `*` and `**` work inside literals to merge collections:

   ```Python
   def connect(host, port, timeout):
       print(host, port, timeout)

   config = {"host": "db1", "port": 5432, "timeout": 10}
   connect(**config)                       # keys become keyword arguments

   merged = {**config, "port": 6432}       # dict merge; later keys win
   combined = [*range(3), *"ab"]           # [0, 1, 2, 'a', 'b']
   ```

3. **Swap and starred assignment**: the idiomatic `a, b = b, a` is packing and unpacking in one statement — the right side packs into a tuple, the left side unpacks it. Unpacking also works in `for` loops over pairs (`for key, value in d.items():`).

## 97- What's the difference between `globals()`, `locals()`, and `vars()`?

In Python, the `globals()`, `locals()`, and `vars()` functions are `built-in` functions that can be used to retrieve the global, local, and instance variables in a program, respectively.

The `globals()` function returns a dictionary that contains the `global` variables in the current program. **Global variables** are variables that are defined at the top level of a module or script and are accessible from anywhere in the program.

The `locals()` function returns a dictionary that contains the local variables in the current function or method. **Local variables** are variables that are defined within a function or method and are only accessible within that function or method.

The `vars()` function has two distinct behaviours. **Without arguments, `vars()` is equivalent to `locals()`** — it returns the current local namespace. **With an argument, `vars(obj)` returns `obj.__dict__`** — the attribute dictionary of a module, class, or instance. It is the "with an argument" form that makes `vars()` interesting: `vars(some_instance)` shows an object's instance attributes, which neither `globals()` nor `locals()` can do. (An object with no `__dict__` — for example one using `__slots__`, or a plain `int` — makes `vars(obj)` raise `TypeError`.)

Here is an example of how you might use these functions:

```Python
x = 10
y = 20

class Point:
    def __init__(self, px, py):
        self.px = px
        self.py = py

def my_function():
    z = 30
    print(f"locals: {locals()}")
    print(f"vars() is the same: {vars() == locals()}")
    print(f"globals has x: {'x' in globals()}, z: {'z' in globals()}")
    print(f"vars(Point(1, 2)): {vars(Point(1, 2))}")

my_function()
```

The output of this code would be:

```text
locals: {'z': 30}
vars() is the same: True
globals has x: True, z: False
vars(Point(1, 2)): {'px': 1, 'py': 2}
```

(`globals()` itself returns the full module namespace — `x`, `y`, `Point`, `my_function`, plus dunder entries like `__name__` and `__builtins__`.)

Two cautions that matter in practice:

- **Writing to `globals()` works but is a design smell; writing to `locals()` inside a function does not work at all.** Function locals are stored in optimised slots, and (in 3.13+, per PEP 667) `locals()` returns a _snapshot_ — mutating the returned dict never changes the actual variables.
- These tools are for debugging and framework plumbing (e.g. `str.format_map(vars(obj))`); reaching for them in ordinary application logic usually signals that a plain dict should have been used instead.

## 98- What is the `__init__.py` module? What it's for?

The `__init__.py` file is used to mark directories on disk as Python package directories. It is required for Python to treat the directories as containing packages; otherwise, the directories are just treated as directories and are not searched for modules.

The `__init__.py` file can contain code that initializes the package or sets up any additional functionality that the package provides. It is executed when the package is imported.

For example, consider the following directory structure:

```text
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        submodule1.py
```

To import `module1` from the `my_package` package, you would use the following import statement:

```Python
import my_package.module1
```

When this `import` statement is executed, Python will execute the code in `my_package/__init__.py` before it loads `module1`.

The `__init__.py` file can be an empty file, and typical non-empty uses are: re-exporting the package's public API so users can write `from my_package import Thing` instead of digging into submodules, defining `__all__`, and setting package-level metadata.

The modern nuance: since Python 3.3 (PEP 420), a directory **without** `__init__.py` still imports — it becomes an implicit _namespace package_, whose parts can even be spread across multiple `sys.path` locations. So "it must be present" is no longer strictly true. In practice you should still add `__init__.py` to every ordinary package: it makes the package explicit, imports marginally faster, plays better with some tools, and prevents two unrelated directories from silently merging into one package — reserving namespace packages for the rare plugin-style layouts that genuinely need them.

## 99- How do I view object methods?

To view the methods of an object in Python, you can use the `dir()` function. This function returns a `list` of all the attributes and methods of an object, including special attributes like `__dict__` and `__doc__`.

For example, consider the following object:

```Python
class MyClass:
    def __init__(self):
        self.x = 10

    def my_method(self):
        pass
```

To view the methods of this object, you could do the following:

```Python
obj = MyClass()
methods = dir(obj)
print(methods)
```

This would output the following list:

```Bash
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_method', 'x']
```

You can then filter this list to only include methods by using a list comprehension — note that filtering on `callable` alone is not enough, because the dunder methods (`__init__`, `__eq__`, …) are callable too and would flood the result:

```Python
obj_methods = [m for m in dir(obj)
               if callable(getattr(obj, m)) and not m.startswith("__")]
print(obj_methods)
```

This would output the following list:

```Python
['my_method']
```

Other tools for the same job: `help(obj)` renders methods with their signatures and docstrings; `inspect.getmembers(obj, inspect.ismethod)` returns `(name, method)` pairs and is the robust programmatic option (`inspect.isfunction` for the unbound functions on the class itself); and `vars(type(obj))` shows what the class defines directly, excluding what it merely inherits. One caution: `dir()` calls are a _convention_, not a guarantee — a class can override `__dir__`, and dynamic attributes served by `__getattr__` will not appear.

## 100- Which is a better practice - global import or local import in Python

The convention — codified in PEP 8 — is the opposite of what this question often tempts people to say: **imports belong at the top of the module** (global imports). Top-level imports make a module's dependencies visible at a glance, fail fast at import time rather than deep inside a call at 3 a.m., and cost nothing on re-use — Python caches every imported module in `sys.modules`, so repeated imports are just a dictionary hit, and a function-local import actually _adds_ a small lookup cost on every call.

Local (function-level) imports are the exception, justified in a few specific situations:

1. **Breaking a circular import**, when two modules genuinely need each other and restructuring is not yet feasible — moving one import inside a function defers it past module initialisation.
2. **Deferring a heavy dependency** to speed up program start-up: if `import pandas` costs seconds and only one rarely-used command needs it, importing it inside that function keeps the CLI snappy.
3. **Optional dependencies**: a feature that needs an extras-installed package imports it locally (typically inside a `try`/`except ImportError`) so the rest of the module works without it.
4. **Platform- or context-specific modules** that may not exist everywhere (`fcntl` on Windows, test-only helpers).

Note that "avoiding name conflicts" is _not_ a good reason — aliasing handles that at the top of the file (`import json as std_json`). The practical rule: top-level imports by default; a local import is a deliberate, commented exception, not a style choice.

## 101- what is tilde symbol `(~)` used for in Python?

In a `requirements` file for Python packages, the tilde symbol `(~)` is used to specify a version constraint. For example, if a package `foo` requires version `bar` equal to or greater than `1.2.3` but less than `1.3.0`, the constraint could be specified as `foo~=1.2.3`.

This syntax is used to specify a minimum version of the package, as well as allow for updates that might be made to the package that is compatible with the project's requirements. It allows for patch-level updates (e.g. `1.2.3` to `1.2.4`) but not for updates that might introduce backward-incompatible changes (e.g. `1.2.3` to `1.3.0`).

For example, a `requirements` file might contain the following line:

```text
foo~=1.2.3
```

This would install the latest version of `foo` that is equal to or greater than `1.2.3` and less than `1.3.0`.

Also, the tilde symbol `(~)` is the bitwise `NOT` operator (implemented by the `__invert__` dunder). On an integer it inverts all bits, which under two's-complement arithmetic means **`~x` equals `-x - 1`**:

```Python
>>> x = 0b1100      # 12
>>> y = ~x
>>> y
-13
>>> bin(y)
'-0b1101'
>>> ~0, ~-1
(-1, 0)
```

In this example, the value of `x` is `12` (`1100` in binary), and `~x` is `-13` (the REPL displays the integer `-13`; `bin()` shows its binary form).

The `-x - 1` identity gives rise to a neat indexing idiom: `~i` mirrors an index from the other end of a sequence, since `lst[~0]` is the last element, `lst[~1]` the second-to-last, and in general `lst[~i] == lst[-i - 1]`. It also makes `~` the go-to _element-wise_ NOT in the scientific stack — in NumPy and pandas, `df[~mask]` selects the rows where a boolean mask is `False` (plain `not` cannot be overloaded for arrays). On Python's own `bool` values, though, beware: `~True` is `-2`, not `False` — use `not` for scalar logic.

## 102- What is the difference between `__str__` and `__repr__`?

Both `__str__` and `__repr__` are special methods in Python that can be used to represent objects as strings. However, there are some differences between them:

1. `__str__` is used to return a human-readable string representation of an object. It is intended to be used for display purposes, such as printing the object to the console or displaying it in a GUI. `__str__` should be easy to read and understand for humans, and it should not contain unnecessary technical details.

2. `__repr__` is used to return an unambiguous string representation of an object. It is intended to be used for debugging purposes, such as inspecting the object's state or reproducing the object in code. `__repr__` should be a valid Python expression that can be used to recreate the object, and it should contain all the relevant technical details about the object.

In summary, `__str__` is used for display purposes and should be easy to read, while `__repr__` is used for debugging purposes and should contain all the relevant technical details.

The fallback is **one-directional**: if `__str__` is missing, `str()` and `print()` fall back to `__repr__` — but if `__repr__` is missing, `repr()` does _not_ use `__str__`; it uses the default `<module.Class object at 0x...>`. That asymmetry is why the standard advice is: **always implement `__repr__` first** (every class benefits), and add `__str__` only when you want a different user-facing form.

```Python
import datetime

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"   # unambiguous, ideally eval()-able

    def __str__(self):
        return f"({self.x}, {self.y})"            # friendly

p = Point(1, 2)
print(p)          # (1, 2)          <- print uses __str__
print(repr(p))    # Point(x=1, y=2)
print([p])        # [Point(x=1, y=2)]  <- containers ALWAYS use repr of elements
print(f"{p} vs {p!r}")   # (1, 2) vs Point(x=1, y=2)

today = datetime.date(2026, 7, 25)
print(str(today), "|", repr(today))
# 2026-07-25 | datetime.date(2026, 7, 25)   <- the stdlib models the distinction
```

Note the container behaviour: printing a list of objects shows each element's `__repr__`, never its `__str__` — a frequent source of "why is my nice string not showing?" confusion. In f-strings, `!r` requests the repr explicitly. `dataclasses.dataclass` generates a sensible `__repr__` for free, which is one more reason to reach for it for data-holding classes.

## 103- What is `lru_cache` decorator in Python?

`lru_cache` is a decorator provided by the Python Standard Library's functools module that is used to cache the results of a function. It stands for "Least Recently Used Cache" and is a technique that can be used to speed up the execution of a function by caching its results.

The `lru_cache` decorator works by storing the results of the function in a cache dictionary. If the same set of arguments is passed to the function again, the cached result is returned instead of executing the function again. This can be useful when the function takes a long time to execute, or when the same set of arguments are used repeatedly.

The `lru_cache` decorator has several optional arguments, such as `maxsize` which determines the maximum number of results to cache, and `typed` which determines whether to treat arguments of different types separately. By default, the `lru_cache` decorator uses a maximum cache size of `128`.

Here's an example of how to use the `lru_cache` decorator in Python:

```Python
from functools import lru_cache

@lru_cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(30))
```

In this example, the memoisation transforms the algorithm's complexity: naive recursive Fibonacci recomputes the same subproblems exponentially many times — O(2<sup>n</sup>) — while with `lru_cache` each `fibonacci(k)` is computed once and every repeat becomes a cache hit, collapsing the cost to O(n). A second call to `fibonacci(30)` doesn't even recurse; it is a single dictionary lookup.

Operational details a senior engineer should have ready:

- **Arguments must be hashable** — they form the cache key. Passing a list raises `TypeError`; and `f(1, 2)` vs `f(a=1, b=2)` are cached as different keys.
- **Inspect and reset** with `fibonacci.cache_info()` (hits, misses, maxsize, currsize) and `fibonacci.cache_clear()` — `cache_info()` is also handy in tests to assert caching actually happens.
- `maxsize=None` means an unbounded cache with no LRU eviction bookkeeping; `functools.cache` (Python 3.9+) is a clearer alias for exactly that. `typed=True` caches `f(1)` and `f(1.0)` separately.
- **Two classic traps**: decorating a _method_ keeps `self` in every cache key, so instances are never garbage-collected while cached (prefer `functools.cached_property`, or a cache scoped inside the instance); and caching a function that returns a **mutable** object hands every caller the same instance — mutate it and you have poisoned the cache.
- The cache is per-process and thread-safe for CPython's purposes, but it is not shared across processes — web workers each warm their own.

## 104- What does `__all__` do?

In Python, `__all__` is a special variable that can be defined at the top of a module, which is a list of strings that defines what symbols (e.g., functions, classes, and variables) the module exports when other modules import it using the `from module import *` syntax.

When a module is imported using the `from module import *` syntax, Python only imports the names listed in the module's `__all__` list (if it is defined). If `__all__` is not defined, Python will import all names that do not start with an underscore (_).

Defining `__all__` can be useful for controlling the public interface of a module, especially for large modules with many symbols. By specifying a list of only the public symbols, the module author can prevent accidental imports of internal or private symbols, which can reduce naming conflicts and make the code easier to understand.

Here's an example of how `__all__` can be used:

```Python
# my_module.py

def foo():
    pass

def _bar():
    pass

__all__ = ['foo']
```

In this example, `my_module` defines two functions foo and `_bar`. `_bar` is intended to be used only within the module and is not meant to be part of the module's public API. By setting `__all__` to `['foo']`, we tell Python to only export the foo function when other modules import `my_module` using the `from my_module import *` syntax.

## 105- List some of the dunder methods

1. `__init__`: Initializer, called on a freshly created instance to set it up (the object is actually _created_ by `__new__`, which is the rarely-overridden true constructor)
2. `__repr__`: Method that returns a printable representation of an object
3. `__str__`: Method that returns a string representation of an object
4. `__len__`: Method that returns the length of an object
5. `__getitem__`: Method that allows you to access an item in an object using the square bracket notation (`[]`)
6. `__setitem__`: Method that allows you to set an item in an object using the square bracket notation (`[]`)
7. `__delitem__`: Method that allows you to delete an item from an object using the square bracket notation (`[]`)
8. `__iter__`: Method that returns an iterator for an object
9. `__next__`: Method that returns the next value from an iterator
10. `__call__`: Method that allows you to call an object as if it were a function
11. `__getattr__`: Method that is called when an attribute is not found in an object
12. `__setattr__`: Method that is called when an attribute is set in an object
13. `__delattr__`: Method that is called when an attribute is deleted from an object
14. `__enter__`: Method that is called when a context manager is entered
15. `__exit__`: Method that is called when a context manager is exited
16. `__hash__`: Method that returns a hash value for an object
17. `__bool__`: Method that defines the boolean value of an object
18. `__format__`: Method that returns a formatted string representation of an object

## 106- List some of the dunder methods used in Mathematical operations

- `__add__`: Method that defines the behavior of the + operator
- `__sub__`: Method that defines the behavior of the - operator
- `__mul__`: Method that defines the behavior of the * operator
- `__truediv__`: Method that defines the behavior of the / operator (`__div__` was the Python 2 name; it is never called in Python 3)
- `__floordiv__`: Method that defines the behavior of the // operator
- `__mod__`: Method that defines the behavior of the % operator
- `__pow__`: Method that defines the behavior of the ** operator
- `__matmul__`: Method that defines the behavior of the @ operator (matrix multiplication)
- `__neg__`: Method that defines the behavior of unary minus (`-x`)

Each binary operator also has a reflected form (`__radd__`, `__rsub__`, …), tried when the left operand doesn't know how to handle the right one, and an in-place form (`__iadd__` for `+=`, …).

Comparison operators get their own dunders (not strictly "mathematical", but usually asked together):

- `__eq__`: Method that defines the behavior of the == operator
- `__ne__`: Method that defines the behavior of the != operator
- `__lt__`: Method that defines the behavior of the < operator
- `__le__`: Method that defines the behavior of the <= operator
- `__gt__`: Method that defines the behavior of the > operator
- `__ge__`: Method that defines the behavior of the >= operator

(`functools.total_ordering` fills in the rest if you define `__eq__` plus any one ordering method.)

## 107- List some of the Dunder variables

- `__name__`: The name of the current module
- `__file__`: The path to the file that the module was loaded from
- `__doc__`: The docstring for the module, function, class, or method
- `__annotations__`: A dictionary containing type annotations for the module, function, class, or method
- `__package__`: The name of the package that the module belongs to
- `__loader__`: The loader that loaded the module
- `__spec__`: The specification of the module
- `__path__`: The path to the package that the module belongs to (if it is a package)
- `__builtins__`: Access to the built-in names (a CPython implementation detail: it is the `builtins` module itself in `__main__`, but a plain dict inside imported modules — `import builtins` is the portable way to reach it)
- `__all__`: A list of strings containing the names of the symbols that should be exported when using the `from module import *` syntax
- `__dict__`: A dictionary or other mapping object used to store an object’s  attributes.

## 108- What are python frameworks for web development?

1. **Django**: A high-level, open-source web framework following the MTV (model-template-view) pattern — Django's own naming of what is essentially MVC, with the framework itself acting as controller. It's a batteries-included framework (ORM, migrations, admin interface, auth, forms) known for its robust and scalable approach to web development.

2. **Flask**: A lightweight, micro web framework that is easy to use and great for small to medium-sized web applications. It is easy to learn and start with and gives developers more control over the application's structure and behavior.

3. **Pyramid**: A web framework designed for small and large web applications. It provides a lot of flexibility and can be used for a wide range of applications, from small personal blogs to large enterprise applications.

4. **Tornado**: A web framework for building web applications that are highly concurrent and perform well under heavy loads. It is ideal for building real-time applications, such as web sockets and long polling applications.

5. **FastAPI**: A modern, fast, web framework for building APIs with Python 3.6+ based on standard Python type hints. FastAPI is built on top of Starlette for web parts and Pydantic for data parts.

6. **Flask-RESTful**: A simple but flexible extension for Flask that makes it easy to handle RESTful API requests.

7. **Sanic**: A Flask like Python 3.5+ web server that's written to go fast. It allows the usage of the async/await syntax added in Python 3.5, which makes your code non-blocking and speedy.

## 109- Write an API using Django REST

```Python
# myapp/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

# myapp/serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'published_date', 'price')

# myapp/views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

This example defines a simple `Book` model with fields for (`title, author, published date, and price`). The `BookSerializer` class is used to convert the `Book` model into a format that can be returned by the API. The `BookViewSet` class is a view that handles the logic for creating, reading, updating, and deleting books. The URL routing is handled by the `DefaultRouter` class, which automatically generates the appropriate URLs for the API based on the views and models.

Wiring it up requires adding `'rest_framework'` and `'myapp'` to `INSTALLED_APPS`, including `myapp.urls` from the project's root `urls.py`, and running `python manage.py makemigrations && python manage.py migrate` to create the table.

You can now run the development server and access the API endpoints at `http://localhost:8000/books/`. Because `ModelViewSet` bundles all the CRUD actions, the router exposes the full REST surface: `GET /books/` (list), `POST /books/` (create), and `GET/PUT/PATCH/DELETE /books/<id>/` (retrieve, update, partial update, delete) — plus the browsable HTML API for free during development.

## 110- What are the differences between Django Framework and Django REST Framework?

Django Framework and Django REST Framework are both web frameworks built on top of the Python programming language. However, they have different purposes and use different approaches to building web applications. **Django Framework** is a general-purpose web framework that can be used to build any type of web application.  
**Django REST Framework** is a framework specifically designed for building RESTful APIs. It provides a number of features that make it easy to build APIs that follow the REST architectural style.

In practice DRF adds, on top of plain Django: **serializers** (declarative conversion and validation between models and JSON), **generic views/viewsets + routers** (CRUD endpoints in a few lines), **authentication schemes** (token, session, and easy JWT integration), fine-grained **permissions and throttling**, **pagination and filtering**, content negotiation, and the **browsable API** — an HTML interface for exploring endpoints during development.

The contrast shows in code. Hand-rolling a JSON endpoint in plain Django (note how serialization, and eventually validation, pagination, and auth, are all yours to write):

```Python
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views import View

from .models import MyObj


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = MyObj.objects.all()
        json_data = serialize("json", qs, fields=('my_field', 'my_other_field'))
        return HttpResponse(json_data, content_type='application/json')
```

The equivalent in Django REST Framework — list **and** create, with validation, auth and pagination hooked in by configuration:

```Python
from rest_framework import generics, permissions

from .models import MyObj
from .serializers import MyObjSerializer


class MyObjListCreateAPIView(generics.ListCreateAPIView):
    queryset = MyObj.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = MyObjSerializer
```

The rule of thumb: server-rendered HTML sites need only Django; the moment the deliverable is a JSON API consumed by a SPA or mobile app, DRF (or a framework like FastAPI) earns its place.

## 111- Create a `LRU Caching` using OrderedDict class

```Python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the accessed key to the end to show that it was recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and move to the end to mark as recently used
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # Pop the first item from the OrderedDict (the least recently used item)
            self.cache.popitem(last=False)
        # Insert the item as the most recently used
        self.cache[key] = value

# Example usage
lru_cache = LRUCache(2)  # capacity of 2
lru_cache.put(1, 1)
lru_cache.put(2, 2)
print(lru_cache.get(1))  # Returns 1
lru_cache.put(3, 3)      # Evicts key 2
print(lru_cache.get(2))  # Returns -1 (not found)
lru_cache.put(4, 4)      # Evicts key 1
print(lru_cache.get(1))  # Returns -1 (not found)
print(lru_cache.get(3))  # Returns 3
print(lru_cache.get(4))  # Returns 4
```

Every operation is O(1): the dict lookup, `move_to_end` (a doubly-linked-list splice — the exact capability `OrderedDict` retains over a plain dict), and `popitem(last=False)` for evicting the least-recently-used entry at the front. This is the standard interview implementation; when you just need function-result caching rather than an explicit cache object, `functools.lru_cache` gives you the same policy as a decorator.

## 112- In a peaceful kingdom, there are houses numbered from 1 to n. The king announces a prize of 100 gold coins to some special group of houses. You have been given the task to determine how many sets of three houses can form a special group, where the sum of the squares of two smaller house numbers is equal to the square of the largest house number

```Python
#Example 1:
#Input: n = 10
#Output: 4
#Explanation: Among the houses numbered 1 to 10, four groups of houses (3, 4, 5), (4, 3, 5), (6, 8, 10), and (8, 6, 10) form special group where sum of square of two smaller houses is equal to the square of larger house.

#Example 2:
#Input: n = 5
#Output: 2
#Explanation: (3,4,5) and (4,3,5).


def count_special_groups(n):
    squares = {i*i: True for i in range(1, n+1)}
    count = 0

    for c in range(1, n+1):
        c_sq = c * c
        for a in range(1, c):
            a_sq = a * a
            b_sq = c_sq - a_sq
            if b_sq in squares:
                count += 1

    return count

# Example usage:
n = 10
result = count_special_groups(n)
print(result)  # Output: 4

# Time Complexity: O(n^2) | Space Complexity: O(n)

# Another solution - same O(n^2) time but O(1) space: instead of a
# precomputed set of squares, check "is b_sq a perfect square?" directly
# with math.isqrt (exact integer sqrt, no float rounding issues).
import math

def count_special_groups_v2(n):
    count = 0
    for c in range(1, n + 1):        # candidate hypotenuse
        c_sq = c * c
        for a in range(1, c):        # one leg; the other is determined
            b_sq = c_sq - a * a
            b = math.isqrt(b_sq)
            if b * b == b_sq:        # b < c and b >= 1 hold automatically
                count += 1
    return count

# Example usage:
result = count_special_groups_v2(10)
print(result)  # Output: 4

# Time Complexity: O(n^2) | Space Complexity: O(1)
```

Note that each Pythagorean triple is counted twice — `(3, 4, 5)` and `(4, 3, 5)` are distinct ordered groups per the problem statement's own examples. Counting unordered triples instead just means iterating `a` only up to `math.isqrt(c_sq // 2)` (i.e. requiring `a < b`), which for `n = 10` gives `2`: `(3, 4, 5)` and `(6, 8, 10)`. Use `math.isqrt` rather than `int(math.sqrt(...))` for exactness — floating-point `sqrt` misclassifies large perfect squares.

## 113- Write a solution for the Max Pairwise Product Problem

```Python
def max_pairwise_product(arr):
    if len(arr) < 2:
        raise ValueError("Array must have at least two elements.")
    
    # Track two largest positive and two smallest negative numbers
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
        
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    
    return max(max1 * max2, min1 * min2)
    # Time Complexity: O(n) | Space Complexity: O(1)
```

This code handles primary case and edge cases like:

- Array with less than two elements.
- Array with negative numbers (e.g., −10, −20, −30 → product of two smallest negatives is the largest positive).
- Array with duplicates (e.g., 5, 5, 5 → product of two largest is 25).

The reasoning behind `max(max1 * max2, min1 * min2)`: the maximum pairwise product comes either from the two largest values or — when large-magnitude negatives exist — from the two smallest, whose product is positive. A single O(n) pass tracking those four values beats the two obvious alternatives: the brute-force double loop, O(n²), and sorting first, O(n log n) — though the sorted version `max(a[0] * a[1], a[-1] * a[-2])` (or `heapq.nlargest(2, ...)`/`nsmallest(2, ...)`) is a fine first answer before optimising. In the classic statement of this problem the inputs are non-negative, where the two largest alone suffice; the negative-number handling here generalises it.
