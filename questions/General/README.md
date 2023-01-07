# Python Interview Questions

## 1- Python uses a Global Interpreter Lock. Does that mean it doesn’t use real threads?

No, Python uses actual threads, but the Global Interpreter Lock (GIL) is a mechanism that prevents multiple native threads from executing Python bytecodes at once. This lock is necessary because CPython, the reference implementation of Python, is not thread-safe, meaning that multiple threads can potentially interfere with each other and compromise the integrity of an application.

The GIL makes it easy to write simple, thread-safe Python programs. Still, it can also limit the performance of multithreaded programs, especially ones that rely heavily on CPU-bound operations. In these cases, Python's threading module may not provide the level of parallelism that you need. In such cases, you may consider using an alternative implementation of Python that does not have a GIL, such as PyPy or Jython, or using a different parallel approach, such as the multiprocessing module or using subprocesses.

## 2- Is it possible to have a producer thread reading from the network and a consumer thread writing to a file, really work in parallel? What about the GIL?

Yes, it is possible to have a producer thread that reads from the network and a consumer thread that writes to a file work in parallel in Python, even with the GIL in place. This is because the GIL only prevents multiple native threads from executing Python bytecodes at once. It does not prevent threads from performing other operations, such as waiting for data to be available on a network socket or waiting for a file to be written to disk.

In the case of a producer thread reading from the network and a consumer thread writing to a file, the producer thread can block a network read operation, allowing the consumer thread to run in the meantime. Similarly, the consumer thread can block a file write operation, allowing the producer thread to run. In this way, the two threads can effectively work in parallel, even though only one native thread is executing Python bytecodes at a time due to the GIL.

It is important to note that the GIL can still limit the overall performance of a program that uses multiple threads, especially if the threads are CPU-bound. In such cases, you may want to consider using an alternative implementation of Python that does not have a GIL or using a different approach to parallelism, such as the multiprocessing module or using subprocesses.

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

We create two instances of the `C` class, `c1` and `c2`, and print the value of the `dangerous` attribute for each instance. Since the dangerous attribute is a class attribute, it has the same value for both `c1` and `c2`.

Next, we set the value of the `dangerous` attribute for `c1` to **`3`**. This creates an instance attribute for `c1` that shadows the class attribute of the same name. An instance attribute is a variable that is specific to a particular instance of a class, and it takes precedence over any class attribute of the same name.

We then print the value of the dangerous attribute for `c1` and `c2`. The value for `c1` is **`3`**, because it now has an instance attribute of that name, while the value for `c2` is still **`2`**, because it only has the class attribute of that name.

Next, we delete the instance attribute for `c1` using the del statement. This removes the instance attribute, revealing the underlying class attribute of the same name.

Finally, we set the value of the dangerous class attribute to **`3`**. This changes the value of the class attribute for all instances of the class, including `c2`. When we print the value of the dangerous attribute for `c2`, it is now **`3`**.

## 4- Why are functions considered first class objects in Python?

In Python, functions are considered first-class objects because they have the same properties as other objects in the language. Specifically, this means that functions can be:

1. Assigned to variables and stored in data structures, just like any other object
2. Passed as arguments to functions
3. Returned as values from functions
4. Defined inside other functions  
    The ability to treat functions as first-class objects is a powerful feature of Python that enables several useful programming patterns, such as higher-order functions, decorators, and functional programming.

For example, consider the following code:

```Python
def greet(name):
  return "Hello, " + name

greeting = greet
print(greeting("John"))  # prints "Hello, John"
```

In this code, we define a function called `greet` that takes a single argument and returns a string. We then assign the function to a variable called `greeting`, and call the `greeting` function just like we would call the `greet` function. This demonstrates how a function can be treated as a first-class object and assigned to a variable.

As another example, consider the following code:

```Python
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

```Python
def increment(x):
  x += 1

a = 10
increment(a)
print(a)  # prints 10
```

In this code, the `increment` function takes an argument `x` and increments it by `1`. However, when we pass the value `10` to the function as an argument and then print the value of `a`, it is still `10`. This is because the `increment` function operates on a copy of the value of `a`, rather than modifying the value of `a` itself.

For mutable objects, such as lists and dictionaries, passing by assignment has the same behavior as passing by reference. For example, consider the following code:

```Python
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

   - Pylint: A widely-used linting tool that can detect a wide range of issues in Python code, including syntax errors, style issues, and potential bugs.
   - Flake8: A popular linting tool that combines several other tools, including PyFlakes, pycodestyle, and McCabe.
   - PyCodeStyle (formerly known as pycodestyle): A linting tool that checks code for style issues, such as indentation, line length, and naming conventions.

2. **Debugging**: Debugging is the process of identifying and fixing errors in your code. Some popular tools for debugging Python code include:

   - PDB: The Python debugger is a built-in tool that allows you to step through your code, inspect variables, and set breakpoints.
   - IPython: An interactive Python shell that provides additional debugging features, such as tab completion, object introspection, and history.
   - PyCharm: An integrated development environment (IDE) that includes a powerful debugger and other debugging tools.

3. **Profiling**: ling is the process of measuring the performance of your code and identifying bottlenecks. Some popular tools for profiling Python code include:
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
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # prints [2, 4, 6, 8, 10]

# Use reduce to compute the product of all even numbers
product = reduce(lambda x, y: x * y, even_numbers)
print(product)  # prints 3840

```

In this example, we define a list of numbers and use the `filter` function to select only the even numbers from the list. The `filter` function takes a function and an iterable as arguments and returns an iterator that yields the elements of the iterable for which the function returns `True`. In this case, we pass a `lambda` function that returns `True` if its argument is even and `False` otherwise, and we pass the list of numbers as the iterable.

We then use the `reduce` function from the `functools` module to compute the product of all the even numbers in the `list`. The `reduce` function takes a function and an iterable as arguments and applies the function to the elements of the iterable in a cumulative manner, returning a single result. In this case, we pass a lambda function that multiplies its arguments and passes the iterator returned by `filter` as the iterable.

Both `filter` and `reduce` are higher-order functions, meaning that they take a function as an `argument` and return a new function as a result. They are useful for concisely expressing complex operations on iterable objects in Python.

## 8- What are list and dict comprehensions?

List comprehensions and dictionary comprehensions are concise ways to create new lists and dictionaries, respectively, from existing iterable objects. They are a way to transform one list (or dictionary) into another list (or dictionary) by applying a certain operation to each element in the original list.  
A list comprehension consists of square brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses. The result is a new list that is computed by evaluating the expression in the context of the `for` and `if` clauses.

For example, suppose we have a list of numbers and we want to create a new list that contains only the even numbers from the original list. We could do this using a list comprehension as follows:

```Python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
```

This would create a new list `even_numbers` containing only the even numbers from the original list `numbers`.

A dictionary comprehension is similar to a list comprehension, but it creates a new dictionary instead of a list. It consists of a dictionary key expression followed by a `for` clause, then zero or more `for` or `if` clauses. The result is a new dictionary that is computed by evaluating the key and value expressions in the context of the `for` and `if` clauses.

For example, suppose we have a list of strings and we want to create a new dictionary that maps each string to its length. We could do this using a dictionary comprehension as follows:

```Python
strings = ['cat', 'dog', 'bird']
lengths = {s: len(s) for s in strings}
```

This would create a new dictionary `lengths` that maps each string to its length.

## 9- What do we mean when we say that a certain Lambda expression forms a closure?

A closure is a function that retains access to the variables in the environment in which it was defined, even after the code that defined the function has finished executing. This means that the function can still reference and modify the variables even if the function is called in a different context, such as in a different function or in a different part of the program.

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

3. _Exception handling_: In Python 2.x, the `except` statement can be used to catch exceptions of any type, while in Python 3.x, the `except` statement must specify the type of exception being caught.

   ```Python
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

5. _Unicode support_: In Python 2.x, Unicode support is not fully integrated, and the unicode and str types are separate. In Python 3.x, Unicode is fully integrated, and the str type is used for Unicode strings.

## 11- How is memory managed in python?

In Python, memory management is handled by the Python interpreter itself. When a Python program runs, the interpreter creates and manages a number of objects in memory to store the data used by the program. The interpreter also tracks the objects that are no longer being used and reclaims their memory, a process known as garbage collection.

One of the key features of Python's memory management is its use of reference counting to keep track of the objects that are being used by the program. When an object is created, the interpreter increments a reference count for that object. When the object is no longer needed, the reference count is decremented. When the reference count reaches zero, the interpreter knows that the object is no longer being used and can reclaim its memory.

Python also uses a technique called "generational garbage collection" to improve the efficiency of its garbage collection process. This involves dividing objects into different generations based on how long they have been in use. Newer objects are placed in a "young generation," while older objects are placed in an "old generation." The garbage collector focuses on the young generation first, since it is more likely to contain objects that are no longer being used. This helps to reduce the overall time required for garbage collection.

In addition to these techniques, Python also provides tools for controlling and monitoring the use of memory in a program. For example, the `sys.getsizeof()` function can be used to determine the size of an object in memory, and the `gc` module can be used to manually trigger garbage collection or to tune the garbage collection parameters.

## 12- What will be the output of the following code?

```Python
_list = ['a', 'b', 'c', 'd', 'e']
print _list[10:]
```

_The output:_
the output will be an empty list `[]`.

The slicing syntax `list[start: end]` is used to retrieve a subset of the elements in a list. The `start` index specifies the index of the first element to retrieve, and the `end` index specifies the index of the element after the last element to retrieve. If you omit the `end` index, the slicing syntax will return all elements of the list starting from the `start` index until the end of the list.

In this case, the list `_list` has only five elements, so the valid indices are `0` through `4`. The index `10` is out of bounds for the list, so the slicing syntax \_list`[10:]` will return an empty list.

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

This code defines a function `is_palindrome` that takes a number and returns `True` if the number is a palindrome, and `False` otherwise. It does this by converting the number to a string and checking if the string is equal to its reverse.

The main part of the code then iterates over all pairs of 3-digit numbers and checks the product of each pair. If the product is a palindrome and is larger than the current largest palindrome, it updates the largest palindrome.

Finally, the code prints the largest palindrome.

This code should find the largest palindrome made from the product of two 3-digit numbers.

## 14- What is skeleton code in Python?

Skeleton code in Python is a basic set of code that provides a starting point for a new project. It typically includes a directory structure, basic configuration files, and a set of basic functions and structures that can be used as a foundation for building out the project.

Skeleton code is often used to provide a consistent structure and set of best practices for projects, making it easier to get started and avoid common pitfalls. It can also be used to demonstrate how to set up a basic project or to provide a starting point for learning a new programming concept or framework.

For example, a Python skeleton code might include:

- A directory structure for organizing code, tests, and documentation
- Basic configuration files, such as a `setup.py` file for packaging and distributing the project
- A `requirements.txt` file for specifying the project's dependencies
- A testing framework and sample test cases
- Documentation templates and guidelines

Skeleton code is often created for specific types of projects, such as web applications, command-line tools, or data science projects. There are many open-source skeleton code examples available online that you can use as a starting point for your projects.

Using skeleton code can help you get started with a new project more quickly, and can provide a set of established best practices to follow as you develop your project. However, it's important to understand that skeleton code is only a starting point, and you will need to customize and adapt it to your specific needs as you develop your project.

## 15- In Python classes, what is the difference between class methods and static methods? and when to use them?

In Python, a class method is a method that is bound to the class and not the instance of the class. A class method can be called on the class itself, as well as on any instance of the class. A class method is defined using the `@classmethod` decorator, and it takes the class as its first argument, conventionally named `cls`.

A static method is a method that is bound to a class and not the instance of the class, but it does not receive any additional arguments beyond the self parameter. A static method is defined using the `@staticmethod` decorator.

Here's an example of how to define and use class methods and static methods in Python:

```pthon
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
result = MyClass.class_method(arg)

# Call a static method
result = MyClass.static_method(arg)

# Call a class method on an instance of the class
obj = MyClass(value)
result = obj.class_method(arg)

# Call a static method on an instance of the class
result = obj.static_method(arg)
```

In general, you should use **_class methods_** when you need to define a method that operates on the class itself, rather than on an instance of the class. An example of this might be a factory method that creates a new instance of the class with some default values. You should use **_static methods_** when you need to define a method that operates on an argument or variables that are independent of the class and its instances. An example of this might be a utility function that performs some computation or transformation on its arguments but does not need to access any class or instance attributes.

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
- When the variables `x` and `y` were assigned to 257, they were two different objects in different memory locations because the 257 is not on the small integers caching range.

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

## 19- What is the difference between tuples, sets and lists in Python?

In Python, tuples, sets, and lists are all data types that can be used to store collections of items. Here are the main differences between them:

1. **Tuples** are immutable, which means that you cannot modify the values of the items in a tuple once it has been created. They are defined using parentheses `()` and their items are separated by commas. also, tuples are generally faster and use less memory than lists, because they do not have the overhead of the extra methods and behaviors that are associated with lists. However, the difference in performance between tuples and lists is usually small and may not be noticeable in most cases.

2. **Sets** are also immutable, but unlike tuples, they do not have a specific order and do not allow duplicate items. Sets are defined using curly braces `{}` and their items are separated by commas. also, sets are generally faster and use less memory than lists, because they are implemented using a hash table data structure, which allows for efficient insertion, deletion, and lookup of items. However, sets do not maintain the order of their items, which can be a drawback if you need to preserve the order of the items in your collection.

3. **Lists** are mutable, which means that you can change the values of their items after the list has been created. They are defined using square brackets `[]` and their items are separated by commas. also, Lists are generally slower and use more memory than tuples, because they are mutable and have the overhead of the extra methods and behaviors that are associated with them. However, lists are more flexible than tuples because you can modify their items after the list has been created.

```Python
# Create a tuple
t = (1, 2, 3)

# Create a set
s = {3, 6, 9}

# Create a list
l = [1, 2, 3]

# Modify a value in a list (this is not possible for tuples or sets)
l[1] = 4

# Add an item to a list (this is not possible for tuples or sets)
l.append(5)
```

Tuples and sets are generally used when you want to store a collection of items that should not be modified, while lists are used when you need to store a collection of items that you want to be able to modify.

## 20- What are pickling and unpickling in python?

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

class Base2:
    # Base2 class definition

class Derived(Base1, Base2):
    # Derived class definition
```

In this example, the `Derived` class inherits from both the `Base1` and `Base2` classes.

It is important to note that Python uses a method resolution order (MRO) to determine which method should be called when a method with the same name is inherited from multiple superclasses. The MRO is based on the order in which the superclasses are specified in the class definition, and it is used to resolve conflicts when a method is defined in multiple superclasses.

For more information about multiple inheritance in Python, you can refer to the documentation on class inheritance in the Python tutorial.

## 21- What are the pitfalls and problems of Python language?

Performance and concurrency are two common areas where Python programmers may encounter pitfalls and problems. Here are some specific issues to consider in these areas:

1. **_Performance issues_**: Python is generally slower than compiled languages like C or C++, which means that you may encounter performance issues when running computationally intensive tasks in Python. There are ways to improve the performance of Python code (e.g., using optimized libraries or writing code in Cython), but it is important to be aware of the performance limitations of the language.

2. **_Concurrency issues_**: Python has a global interpreter lock (GIL) that prevents multiple threads from executing Python bytecodes at the same time, which can lead to concurrency issues when running multithreaded programs. There are ways to work around the GIL (e.g., using the `multiprocessing` module), but it is important to be aware of this limitation when writing concurrent programs in Python.

Here are some specific issues that you may encounter when dealing with performance and concurrency in Python:

- **Bottlenecks**: It can be difficult to identify which parts of your code are causing performance issues, especially if you are working with large datasets or complex algorithms. You may need to use profiling tools to identify bottlenecks in your code and optimize the most critical parts.

- **Memory usage**: Memory usage can also be a problem when working with large datasets or complex algorithms in Python. You may need to use memory-efficient data structures and algorithms, or write code in a memory-efficient way, to avoid running out of memory.

- **Lack of parallelism**: Because of the GIL, Python threads are not always able to run in parallel on multiple CPU cores. This can limit the scalability of multithreaded Python programs, especially on systems with many CPU cores.

- **Synchronization issues**: When working with concurrent programs, you may need to synchronize access to shared resources to avoid race conditions and other synchronization issues. This can be challenging in Python, especially if you are not familiar with the tools and techniques available for concurrency control.

To avoid these and other issues related to performance and concurrency in Python, it is important to be aware of the limitations of the language and to plan accordingly when writing and testing your code. You may need to use specialized tools and techniques, such as profiling and optimization tools, to improve the performance and scalability of your Python programs.

## 22- How to achieve multithreading in Python?

Python offers a multi-threading package but it is not good for speeding up the code. The GIL is a great way though it is not multithreading. It executes one at a time but takes turns for different threads fast which makes it seem like processes are running simultaneously.

## 23- What is the use of `with` in Python?

In Python, the with statement is used to wrap the execution of a block of code with methods defined by a context manager. A context manager is an object that defines the methods `__enter__` and `__exit__`, which are called before and after the execution of the block of code, respectively.

The `with` statement is used to manage resources that need to be acquired and released, such as file handles or network connections. It is particularly useful when working with resources that need to be closed or released after they are no longer needed, because it ensures that the resources are properly cleaned up even if an exception is raised during the execution of the block of code.

Here is an example of how to use the `with` statement to open and read a file in Python:

```Python
f = open('filename.txt', 'r')
try:
    contents = f.read()
finally:
    f.close()
```

## 24- How are `.py`, `.pyi`, `.pyd`, and `.pyc` files different?

In Python, there are several different file types that you may encounter when working with the language:

1. **`.py`** files are Python source files that contain the code written in the Python language. These files can be executed by the Python interpreter, and they can be imported as modules in other Python programs.

2. **`.pyi`** files are Python interface files that contain type hints for Python programs. These files are used to provide type information for static type checkers, such as mypy, and they are not intended to be executed by the Python interpreter.

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

In this example, `foo.py` is a Python source file that defines a function called `foo`. `bar.py` is another Python source file that imports the `foo` module and calls the `foo` function. When `bar.py` is executed, the Python interpreter will create a compiled `foo.pyc` file (if it doesn't already exist) and use it to execute the code in `foo.py`.

## 25- What are decorators in Python?

Decorators are functions that are used to modify the behavior of other functions. Decorators are implemented as functions that take a function as an argument and return a modified function. They are often used to add additional functionality to an existing function, such as logging, caching, or input validation.

To use a decorator in Python, you define a decorator function and use the `@` symbol to specify that the function being defined is a decorator. The function being decorated is passed as an argument to the decorator function, and the decorator function returns the modified function.

Here is an example of how to use a decorator in Python:

```Python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling the decorated function")
        result = func(*args, **kwargs)
        print("After calling the decorated function")
        return result
    return wrapper

@my_decorator
def my_function(x, y):
    return x + y

print(my_function(3, 4))
```

In this example, the `my_decorator` function is a decorator that adds additional logging before and after the decorated function is called. The `my_function` function is decorated with the `my_decorator` decorator, which modifies its behavior to include the additional logging. When `my_function` is called, the decorator function is executed first, and then the decorated function is called.

## 26- How to use `self` in Python?

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

## 27- What are namespaces in Python?

In Python, a namespace is a container that holds a set of identifiers (i.e., names) and their corresponding objects. Namespaces are used to avoid name collisions between identifiers that have the same name but are used in different contexts.

There are several types of namespaces in Python:

- **Module namespace**: Each module in Python has its own namespace, which contains the identifiers defined in the module, such as functions, variables, and classes. When you import a module, the identifiers in the module's namespace become available in the current namespace.

- **Class namespace**: Each class in Python has its own namespace, which contains the identifiers defined in the class, such as methods and instance variables. When you create an instance of a class, the instance variables become part of the instance's namespace.

- **Function namespace**: Each function in Python has its own namespace, which contains the identifiers defined in the function, such as local variables and function arguments. The function namespace is created when the function is called and is destroyed when the function returns.

Here is an example of how namespaces are used in Python:

```Python
# Define a global variable in the module namespace
x = 10

def foo():
    # Define a local variable in the function namespace
    y = 20
    print(x)  # Access the global variable from the module namespace

class MyClass:
    def __init__(self):
        # Define an instance variable in the class namespace
        self.z = 30
    def my_method(self):
        print(self.z)  # Access the instance variable from the class namespace

obj = MyClass()
obj.my_method()
```

In this example, the `x` variable is defined in the module namespace and is accessible from the global scope and from the `foo` function. The `y` variable is defined in the function namespace and is only accessible from within the `foo` function. The `z` variable is defined in the class namespace and is accessible from the instance methods of the `MyClass` class.

## 28- What is PEP?

PEP stands for _Python Enhancement Proposal_. PEPs are documents that describe proposed changes, improvements, and new features for Python. They are written by Python developers and are used to communicate ideas and proposals for improving the language to the Python community.

There are different types of PEPs, including:

- **Standards Track PEPs**: These PEPs propose changes to the Python language itself, such as new syntax or built-in functions.

- **Informational PEPs**: These PEPs provide information about Python-related topics, such as best practices or design patterns.

- **Process PEPs**: These PEPs describe changes to the Python development process, such as how PEPs are submitted and reviewed.

PEPs are written in a standard format and are reviewed by the Python community through a process called the PEP process. The PEP process is designed to ensure that proposed changes to Python are well-documented, well-reasoned, and discussed by the community before being accepted and implemented.

## 29- What are dunder methods in python?

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

## 30- What does `super` do in Python? - difference between `super().__init__()` and explicit `superclass.__init__()`

In Python, `super` is a special function that refers to the parent class. It is used to access methods and properties of the parent class from within a child class.

When you use `super().__init__()` in a child class, you are calling the `__init__` method of the parent class. This is equivalent to calling `SomeParentClass.__init__(self)`, where `SomeParentClass` is the name of the parent class.

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

In this example, the `Cat` class is a child class of the `Animal` class. The `Cat` class has its own `__init__` method, which calls the `__init__` method of the `Animal` class using `super().__init__(name, species="Cat")`. This is equivalent to calling `Animal.__init__(self, name, species="Cat")`, which sets the name and species attributes of the `Cat` object.

On the other hand, if you were to use `SomeParentClass.__init__(self)` to call the `__init__` method of the parent class, you would need to explicitly specify the name of the parent class. For example:

```Python
class Cat(Animal):
    def __init__(self, name, breed, toy):
        Animal.__init__(self, name, species="Cat")
        self.breed = breed
        self.toy = toy
```

In this case, the `__init__` method of the `Animal` class is called using the explicit name of the parent class, `Animal`. This is equivalent to using `super().__init__(name, species="Cat")`.

Both `super().__init__()` and `SomeParentClass.__init__(self)` are used to call the `__init__` method of the parent class from within a child class. The main difference is that `super().__init__()` does not require you to explicitly specify the name of the parent class, while `SomeParentClass.__init__(self)` does.

## 31- What is property decorator in python?

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

## 32- What is the difference between Cython and CPython?

Cython is a programming language that is a superset of Python, which means that it is fully compatible with Python and can be used to write Python code. Cython is designed to make it easy to write Python code that can be efficiently compiled into C or C++ code, which can then be compiled into a native machine code executable.

CPython, on the other hand, is the reference implementation of the Python programming language. It is written in C and is the most widely used implementation of Python.

One of the main differences between Cython and CPython is that Cython allows you to write Python code that can be compiled into native machine code, while CPython is an interpreter that executes Python code directly. This means that Cython code can be faster and more efficient than CPython code, especially for computationally intensive tasks.

Another difference is that Cython allows you to include C or C++ code in your Python code, which can be useful if you want to use existing C or C++ libraries or if you want to write low-level code that is not possible in pure Python.

Overall, Cython is a useful tool for optimizing Python code and extending Python with C or C++ code, while CPython is the reference implementation of the Python language and is used for running Python code on most platforms.

## 33- Specify the difference between local and global variables in Python

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

```Pythn
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

## 34- What are Python iterators?

In Python, an iterator is an object that allows you to iterate over a sequence of elements, such as a list, tuple, or string. An iterator has two main methods: `__iter__` and `__next__`.

The `__iter__` method is called when the iterator object is initialized, and it returns the iterator object itself. The `__next__` method is called to retrieve the next element in the sequence. When there are no more elements to iterate over, the `__next__` method raises a `StopIteration` exception to signal that the iteration is complete.

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

# Iterate over the elements of the list using a for loop
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

In this example, the `MyIterator` class defines an iterator that iterates over a list of data. The `__iter__` method returns the iterator object itself, and the `__next__` method returns the next element in

## 35- What are Python generators?

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

## 36- What is the difference between Python's Generators and Iterators?

In Python, generators and iterators are similar in that they both allow you to iterate over a sequence of values. However, there are some important differences between the two.

The main difference is that a generator is a function that generates an iterator, while an iterator is an object that represents a stream of data. A generator function is defined using the `yield` keyword, which allows the generator to pause execution and return a value, but it does not terminate the generator function. An iterator, on the other hand, is an object that has two main methods: `__iter__` and `__next__`. The `__iter__` method is called when the iterator is initialized, and it returns the iterator object itself. The `__next__` method is called to retrieve the next element in the sequence, and it raises a StopIteration exception when there are no more elements to iterate over.

Here is an example of how generators and iterators work in Python:

```Python
# Define a generator function
def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

# Create a generator object
gen = my_range(5)

# Iterate over the generator using a for loop
for i in gen:
    print(i) # prints 0, 1, 2, 3, 4

# Create an iterator object
it = iter(gen)

# Iterate over the iterator using the next function
print(next(it)) # prints 0
print(next(it)) # prints 1
print(next(it)) # prints 2
print(next(it)) # prints 3
print(next(it)) # prints 4
print(next(it)) # This will raise a StopIteration exception
```

In this example, the `my_range` generator function defines a generator that generates a sequence of numbers from `0` to `n-1`. The generator is called to create a generator object, which is then iterated over using a for a loop. The generator object is also converted to an iterator object using the `iter` function, and the iterator is iterated over using the `next` function.

One important difference between generators and iterators is that generators can only be iterated over once. Once the generator has been exhausted, it cannot be used again. Iterators, on the other hand, can be iterated over multiple times.

Another difference is that generators are more memory-efficient than iterators because they do not store all of the values in memory at once.

## 37- What are Python documentation strings?

In Python, documentation strings (also called docstrings) are strings that are used to document a module, class, method, or function. Docstrings are usually placed at the beginning of the code block that they document, and they are typically used to provide a brief description of what the code does and how it can be used.

In Python, docstrings are written using triple quotes (`'''` or `"""`). For example:

```Python
def some_function(arg1, arg2):
    '''
    This is a docstring for the some_function function.

    This function does something with the arguments arg1 and arg2.

    Parameters:
        arg1 (int): The first argument.
        arg2 (int): The second argument.

    Returns:
        int: The result of the function.
    '''
    # Function code goes here
    return result

```

In this example, the docstring for the `some_function` function is a multi-line string that is placed at the beginning of the function definition. It provides a brief description of what the function does and lists the parameters and return value of the function.

Docstrings can be accessed at runtime using the `__doc__` attribute of the object. For example:

```Python
print(some_function.__doc__)
# This will print the docstring for the some_function function.
```

## 38- Explain the use of `subn()`, `sub()`, and `split()` in the `“re”` module

The `re` is a Python module developers use to execute operations that involve expression matching. In particular, it contains three modules to allow editing strings – `subn()`, `sub()`, and `split()`.

1. **`subn()`**: Defines all strings with a matching regex pattern, replaces them with a new one, and returns the number of replacements.
2. **`sub()`**: Defines all strings with a matching regex pattern and replaces them with a new one.
3. **`split()`**: Splits strings into lists using regex patterns

## 39- Define polymorphism in Python

In Python, polymorphism refers to the ability of a function or method to behave differently depending on the data type of the arguments passed to it.

Polymorphism is a key feature of object-oriented programming (OOP) and allows you to write code that is more flexible and reusable. It allows you to define a function or method that can accept different types of arguments and perform different actions based on the type of arguments.

There are two main ways to implement polymorphism in Python:

1. **Method overloading**: This is the ability to define multiple methods with the same name but different signatures (i.e., a different number or types of arguments). Python does not have native support for method overloading, so you have to use function overloading techniques to achieve this.

2. **Method overriding**: This is the ability to define a method in a subclass that has the same name and signature as a method in the superclass, but with different behavior. Method overriding is a key feature of OOP and allows you to customize the behavior of a method in a subclass to suit the needs of the subclass.

Here is an example of polymorphism using method overriding in Python:

```Python
class Shape:
    def area(self):
        raise NotImplementedError

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
        return 3.14 * self.radius * self.radius

# Create a rectangle object
rect = Rectangle(10, 20)

# Print the area of the rectangle
print(rect.area()) # prints
```

## 40- What are the differences between Wheels and Eggs?

In Python, wheels and eggs are two different types of distribution formats for Python packages.

A wheel is a pre-built distribution of a Python package that is built using the `bdist_wheel` command. Wheels are stored in the `.whl` file format and can be installed using the `pip` package manager. Wheels are designed to be a more efficient and faster way to install Python packages, especially for large packages or packages with many dependencies.

An `egg` is an older distribution format for Python packages that are stored in the `.egg` file format. Eggs were originally used by the `easy_install` package manager, but they are now deprecated in favor of wheels.

There are several key differences between wheels and eggs:

- File format: Wheels are stored in the `.whl` file format, while eggs are stored in the `.egg` file format.

- Installation: Wheels can be installed using the pip package manager, while eggs can be installed using the `easy_install` package manager.

- Compatibility: Wheels are compatible with _Python 2.7_ and later versions, while eggs are only compatible with _Python 2.4_ and later versions.

- Efficieny: Wheels are generally more efficient and faster to install than eggs because they do not need to be built from source code.

In summary, wheels are the recommended distribution format for Python packages, while eggs are deprecated and should not be used. If you are installing a Python package, you should look for a wheel package if possible.

## 41- What is the purpose of Python non-local statements?

Non-local statements allow assigning variables to outer-scope statements that are not global. The most common application of the keyword is in nested functions, where there's a need to make sure a variable isn't accessible by the inner function.

## 42- How is Python exception is handled?

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

In this example, the `finally` block will be executed after the `try` block, regardless of whether an exception is raised or not. It will print the message **`'Done'`** to the console.

## 43- Name the differences between functional and object-oriented programming

Functional programming and object-oriented programming are two programming paradigms that are commonly used in Python. Each paradigm has its own set of characteristics and approaches to solving problems, and they can be used in different situations depending on the needs of the project.

Here are some key differences between functional programming and object-oriented programming in Python:

1. **Data model**: In functional programming, data is treated as immutable and functions are used to transform data. In object-oriented programming, data is encapsulated in objects and accessed through methods.

2. **State**: In functional programming, state is typically avoided or minimized, and functions are designed to be pure and side-effect free. In object-oriented programming, objects have internal state that can be modified through methods.

3. **Inheritance**: In object-oriented programming, inheritance is used to create a hierarchy of classes and reuse code between classes. In functional programming, inheritance is not typically used, and functions are composed and combined to create new functionality.

4. **Polymorphism**: In object-oriented programming, polymorphism allows a method or function to behave differently depending on the type of the arguments passed to it. In functional programming, polymorphism is typically achieved through function overloading or currying.

5. **Concurrency**: In functional programming, concurrency is typically easier to achieve because functions are pure and do not depend on state. In object-oriented programming, concurrency can be more challenging because objects have internal state that can be modified concurrently.

## 44- What does the `PYTHONOPTIMIZE` flag do?

The `PYTHONOPTIMIZE` flag is a command-line option for the Python interpreter that enables various optimization techniques. When the `PYTHONOPTIMIZE` flag is set to a non-zero value, the interpreter will apply various optimization techniques to the bytecode of the program, in an attempt to improve its performance.

The optimization techniques that are applied when `PYTHONOPTIMIZE` is set depend on the specific version of Python that you are using. In general, the optimization techniques that may be applied include:

- Inlining of simple functions
  \*Removal of dead code
- Specialization of function calls
- Early binding of global names
- Constant folding and propagation
- Peephole optimization of bytecode

It's important to note that the `PYTHONOPTIMIZE` flag is intended to be used for debugging and profiling purposes, and is not recommended for use in production environments. This is because the optimizations applied by the flag may change the behavior of the program in ways that are difficult to predict, and may even make the program slower in some cases.

To use the `PYTHONOPTIMIZE` flag, you can specify it as an option when running the Python interpreter from the command line, like this:

```Python
python -O script.py
```

This will run the Python interpreter with the `PYTHONOPTIMIZE` flag set to 1. You can also set the flag to a higher value by using the `-OO` flag, which will enable additional optimization techniques:

```Python
python -OO script.py
```

It's worth noting that the optimization techniques applied by the PYTHONOPTIMIZE flag are not as effective as those used by modern just-in-time (JIT) compilers, such as PyPy or Numba. These tools are generally more effective at optimizing Python code, and are typically recommended for use in production environments where performance is critical.

## 45- What are descriptors? Is there a difference between a descriptor and a decorator?

In Python, a descriptor is an object attribute with "binding behavior", which means that it has the ability to define how it is accessed and set. Descriptors are implemented using a set of special methods, known as the descriptor protocol, which consists of the `__get__`, `__set__`, and `__delete__` methods.

Descriptors are a way to define custom attribute access behavior in Python. They can be used to implement properties, methods, or any other attribute type with custom behavior. For example, you might use a descriptor to implement lazy evaluation of an attribute, or to provide read-only access to an attribute.

The descriptor protocol defines how the descriptor's methods are called when the attribute is accessed on an object. When an attribute is accessed on an object, Python first checks to see if the attribute is defined on the object itself. If it is, the attribute is accessed directly. If the attribute is not defined on the object, Python looks for a descriptor with the same name on the object's class or any of its base classes. If a descriptor is found, Python calls the descriptor's `__get__`, `__set__`, or `__delete__` method, depending on the type of attribute access that is being performed.
A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying its code. Decorators are implemented using the `@` syntax in Python, and are used to modify the behavior of a function or method.

There is a difference between a descriptor and a decorator in Python. A descriptor is an object attribute with binding behavior, whereas a decorator is a function that takes another function and extends its behavior. Descriptors are implemented using the descriptor protocol, which consists of the `__get__`, `__set__`, and `__delete__` methods, whereas decorators are implemented as functions that take a function as an argument and return a modified version of the function.

## 46- Generate random number

You can generate a random number using `random` module.

```Python
import random
random_number = random.randint(1, 100)
# Generate a random number between 1 and 100

random_number = random.random()
# Generate a random number i.e. 0.3366241606464734
```

You can set a `seed` for number generation by using `number.seed(x)` where `x` is the value will be used as a **seed** for the randomization.

```Python
import time
import random

# Seed the random number generator with the current time
random.seed(time.time())

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

```

## 47 - What are itertools in Python?

The `itertools` module is a Python module that provides a number of functions that are helpful when working with iterators. Iterators are objects that allow you to iterate over a sequence of values, such as a list or a string.

Here are a few examples of functions that are available in the `itertools` module:

- `count`: This function returns an iterator that produces consecutive integers, starting from a given value.

- `cycle`: This function returns an iterator that repeats a sequence of values indefinitely.

- `permutations`: This function returns an iterator that produces all of the permutations of a given sequence.

- `combinations`: This function returns an iterator that produces all of the combinations of a given sequence.

## 47 - what does itertools.islice do?

`itertools.islice` is a function that returns an iterator that returns selected elements from the input iterator. It works by slicing the input iterator and returning an iterator that produces the sliced elements.

Here's an example of how you can use `itertools.islice`:

```Python
import itertools

# Create a list of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create an iterator using islice that returns every other element
evens = itertools.islice(numbers, 0, 10, 2)

# Print the even numbers
for number in evens:
    print(number)

# This will print the following output:
1 3 5 7 9
```

You can also use `itertools.islice` to slice the input iterator at a specific starting and ending position, and with a specific step size. For example, you could use `itertools.islice(numbers, 2, 6, 1)` to return an iterator that produces the elements at index `2` through `5` (inclusive) of the numbers list, with a step size of `1`. below is an example of output based on various input:

```Python
# itertools.islice(iterable, stop)
# itertools.islice(iterable, start, stop, step)

# islice('ABCDEFG', 2)          --> A B
# islice('ABCDEFG', 2, 4)       --> C D
# islice('ABCDEFG', 2, None)    --> C D E F G
# islice('ABCDEFG', 0, None, 2) --> A C E G
```

## 48 - Why this code will never stop?

```Python
i = 0
while i != 1:
    i += 0.1
    print(i)
```

This code will never stop because the condition `i != 1` will never be satisfied. The value of `i` is incremented by `0.1` each time the loop iterates, but it will never be equal to `1` because `0.1` is a **`float`**, and **`float`** values are usually not represented exactly in memory.

As a result, the value of `i` will get closer and closer to `1`, but it will never be equal to `1` exactly. This means that the loop will run indefinitely.

## 49 - What is the ouput of this code, and why?

```Python
import datetime
from time import sleep
def my_time(time_now = datetime.datetime.now()):
    return time_now

print(my_time())
sleep(3)
print(my_time())
```

The output of this code will be two timestamps that are very close to each other (within a few seconds). This is because the default value of the `time_now` parameter is set to the current time `(datetime.datetime.now())` when the `my_time` function is defined, rather than when it is called.

As a result, the value of `time_now` is fixed at the time that the function is defined, and it is not updated when the function is called. This means that the two calls to `my_time` will both return the same value _(the current time when the function was defined)_, even though several seconds have passed between the two calls.

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

## 50 - Can we chain Multiple Decorators in Python?

Yes, you can chain multiple decorators in Python. Decorators are functions that are used to modify the behavior of another function. They are applied using the `@` symbol, and can be used to add additional functionality to a function without modifying the function's source code.

To chain multiple decorators, you can simply apply them one after the other, using the `@` symbol, like this:

```Python
@decorator1
@decorator2
@decorator3
def function():
    # function code goes here
```

This will apply the decorators in the order that they are listed, so `decorator1` will be applied first, followed by `decorator2`, and then `decorator3`.

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

As you can see, the decorators are applied in the order that they are listed, with `decorator1` being applied first, followed by `decorator2`. The function itself is called last, after the decorators have been applied.

## 51 - Build a recursive function using python

To build a recursive function in Python, you will need to define a function that calls itself with a modified version of its input. Here's an example of how you can build a recursive function to calculate the factorial of a number:

```Python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

In this example, the `factorial` function is defined to take a single argument `n`. The function has a base case (the `if` statement) that returns `1` if `n` is equal to `1`. If `n` is not equal to `1`, the function returns `n` multiplied by the result of calling itself with `n - 1` as the argument.

```Python
# 1st call: return n * factorial(4) "n = 5"
# 2nd call: return n * factorial(3) "n = 4"
# 3rd call: return n * factorial(2) "n = 3"
# 4th call: return n * factorial(1) "n = 2"
# 5th call: return 1                "n = 1"

# The stack will execute in-hold calls
# 4th call: 2 * 1 = 2
# 3rd call: 3 * 2 = 6
# 2nd call: 4 * 6 = 24
# 1st call: 5 * 24 = 120 (5! -> 120)
```

## 52 - How to implement a binary search tree using python?

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

To use these classes, you can create a new `BST` object and use the `insert` method to add nodes to the tree. You can then use the search method to search for a particular value in the tree. If a node with the specified `value` is found, the method returns `True`, otherwise it returns `False`.

## 53 - How to implement a binary search using python?

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

## 54 - How to implement a Linked list using python?

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
my_list.traverse()  # Output: 1 2 3
```

## 55 - what is `collections.OrderedDict`?

it is a class in the Python `collections` module that provides an ordered dictionary implementation. Like a regular dictionary, an `OrderedDict` stores key-value pairs, but it remembers the order that the keys were added.

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

The `OrderedDict` maintains the order in which the keys were added. This can be useful if you need to preserve the order of the items in the dictionary for some reason.

One thing to note is that `OrderedDict` is implemented as a doubly-linked list, which means that it has a slightly larger memory overhead than a regular dictionary. However, the difference in memory usage is usually not significant unless you are working with very large dictionaries.

## 56 - what is `collections.defaultdict`?

it is a class in the Python `collections` module that provides a dictionary with a default value. This can be useful if you want to initialize a dictionary with a default value that is returned whenever a key is not found in the dictionary.

Here's an example of how you can use a `defaultdict`:

```Python
from collections import defaultdict

# Create a defaultdict with a default value of 0
d = defaultdict(int)

# Add some key-value pairs
d['a'] = 1
d['b'] = 2
d['c'] = 3

# Access a key that does not exist in the dictionary
print(d['d'])  # Output: 0

# Output the entire dictionary
print(d)  # Output: defaultdict(int, {'a': 1, 'b': 2, 'c': 3, 'd': 0})
```

In this example, the `defaultdict` is initialized with a default value of `0`, which is returned whenever a `key` is not found in the dictionary. You can see that when we try to access the key `'d'`, which does not exist in the dictionary, the `defaultdict` returns the default value of `0`.

You can use any type as the default value for a `defaultdict`, not just `int`. For example, you can use a `list` as the default value to create a `defaultdict`:

```Python
from collections import defaultdict

# Create a defaultdict with a default value of an empty list
d = defaultdict(list)

# Add some key-value pairs
d['a'].append(1)
d['b'].append(2)
d['c'].append(3)

# Access a key that does not exist in the dictionary
print(d['d'])  # Output: []

# Output the entire dictionary
print(d)  # Output: defaultdict(list, {'a': [1], 'b': [2], 'c': [3], 'd': []})
```

In the previous example, the `defaultdict` is initialized with a default value of an empty `list`, which is returned whenever a `key` is not found in the dictionary. You can see that when we try to access the key `'d'`, which does not exist in the dictionary, the `defaultdict` returns the default value of an empty `list`.

## 57 - Can we implement an `array` using Python?

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

## 58- What is `bytes` type?

The `bytes` type is an immutable sequence of _bytes_. It is similar to the _str_ type, but it is meant to hold raw binary data rather than Unicode text.

You can create a `bytes` object by prefixing a string with the b character and enclosing it in quotes, like this:

```Python
b = b'Hello, world!'
```

You can also create a `bytes` object from a list of integers using the `bytes` function:

```Python
b = bytes([104, 101, 108, 108, 111])  # b'hello'
```

You can access the individual bytes of a `bytes` object using indices, like you would with a string:

```Python
b = b'Hello, world!'
print(b[0])  # Output: 72
print(b[1])  # Output: 101
```

You can also use slicing to extract a sub-sequence of bytes from a `bytes` object:

```Python
b = b'Hello, world!'
print(b[6:11])  # Output: b'world'
```

## 59- How to concatenate tuples in python?

You can use the `+` operator. For example:

```Python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

tuple3 = tuple1 + tuple2
print(tuple3)  # Output: (1, 2, 3, 4, 5, 6)
```

This will create a new tuple that contains the elements of `tuple1` followed by the elements of `tuple2`.

Keep in mind that tuples are **immutable**, which means that you cannot modify an existing `tuple`. If you need to modify a `tuple`, you will need to create a new `tuple` with the modified values.

## 60- How to join two `sets`?

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

## 61- What is the difference between Python's list methods append and extend?

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

In general, `append` is faster than `extend` because it does not have to create a new list and copy over all the elements of the iterable. However, `extend` is more convenient to use if you have an iterable that you want to add to the list, because you don't have to use a loop to add the elements one at a time.

## 62- How to implement bubble sort in Python?

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

- Best case: **O(n)**
- Average case: **O(n<sup>2</sup>)**
- Worst case: **O(n^2)**

## 63- How to implement Heap sort in Python?

```Python
def heap_sort(lst):
  # Create an empty list to store the sorted elements
  sorted_list = []
  # Convert the input list into a max heap
  heapify(lst)
  # Keep extracting the root element (maximum value) from the heap
  # until it is empty
  while lst:
    # Extract the root element from the heap and append it to the
    # sorted list
    sorted_list.append(heappop(lst))
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

**_Time Complexity:_**

- Best case: **O(n log(n))**
- Average case: **O(n log(n))**
- Worst case: **O(n log(n))**

## 64- How to implement Insertion sort in Python?

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

## 65- How to implement Merge sort in Python?

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
    # If the left element is smaller, add it to the merged list
    # and increment the left index
    if left[left_index] < right[right_index]:
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

## 66- How to implement Quick sort in Python?

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

## 67- How to implement Selection sort in Python?

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

## 68- How to implement Shell sort in Python?

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

**_Time Complexity:_**

- Best case: **O(n (log n)<sup>2</sup>)**
- Average case: **O(n<sup>3/2</sup>)**
- Worst case: **O(n)**

## 69- What are the commands that are used to copy an object in Python?

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

## 70- What is the difference between deep and shallow copy?

- Shallow copy is used when a new instance type gets created and it keeps the values that are copied in the new instance. Whereas, deep copy is used to store the values that are already copied.
- Shallow copy is used to copy the reference pointers just like it copies the values. These references point to the original objects and the changes made in any member of the class will also affect the original copy of it. Whereas, deep copy doesn’t copy the reference pointers to the objects. Deep copy makes the reference to an object and the new object that is pointed by some other object gets stored. The changes made in the original copy won’t affect any other copy that uses the object.
- Shallow copy allows faster execution of the program and it depends on the size of the data that is used. Whereas, deep copy makes it slower due to making certain copies for each object that is been called.

## 72- How can the ternary operators be used in python?

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

## 73- What will be the output of the code below?

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

- In the first call to `extendList()`, the default value of list is used, which is an empty list `[]`. The value `10` is appended to this list, and the modified list is returned. This list is assigned to `list1`.

- In the second call to `extendList()`, a new list `[123]` is passed as the value for the list parameter, so the default value is not used. The value `123` is appended to this list, and the modified list is returned and assigned to `list2`.

- In the third call to `extendList()`, the default value of list is used again. This time, the default value is the list that was modified in the first call to the function, which contains the value `10`. The value `'a'` is appended to this list, and the modified list is returned and assigned to `list3`.
  This behavior occurs because default values are evaluated when the function is defined, not when it is called. In this case, the default value of the list parameter is an empty list `[]`, which is evaluated when the `extendList()` function is defined. This means that the same `list` object is used as the default value for the `list` parameter every time the `extendList()` function is called, unless a different value is provided for the list parameter in the function call.

The definition of the `extendList` function could be modified as follows, though, to always begin a new list when no `list` argument is specified, which is more likely to have been the desired behavior:

```Python
def extendList(val, list=None):
    if list is None:
        list = []
  list.append(val)
  return list
```

## 74- What will be the output of the code below?

```Python
def multipliers():
  return [lambda x : i * x for i in range(4)]

print [m(2) for m in multipliers()]
```

The output of the above code will be `[6, 6, 6, 6]`.

The reason for this is that Python’s closures are late binding. This means that the values of variables used in closures are looked up at the time the inner function is called. So as a result, when any of the functions returned by `multipliers()` are called, the value of `i` is looked up in the surrounding scope at that time. By then, regardless of which of the returned functions is called, the `for` loop has completed and `i` is left with its final value of 3. Therefore, every returned function multiplies the value it is passed by `3`, so since a value of `2` is passed in the above code, they all return a value of `6` (i.e., 3 x 2).

## 75- What will be the output of the code below?

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

```Python
1 1 1
1 2 1
3 2 3
```

In Python, class variables are internally handled as dictionaries. If a variable name is not found in the dictionary of the current class, the class hierarchy (i.e., its parent classes) are searched until the referenced variable name is found (if the referenced variable name is not found in the class itself or anywhere in its hierarchy, an `AttributeError` occurs).

Therefore, setting `x = 1` in the `Parent` class makes the class variable `x` (with a value of 1) referenceable in that class and any of its children. That’s why the first `print` statement outputs `1 1 1`.

Subsequently, if any of its child classes overrides that value (for example, when we execute the statement `Child1.x = 2`), then the value is changed in that child only. That’s why the second `print` statement outputs `1 2 1`.

Finally, if the value is then changed in the `Parent` (for example, when we execute the statement `Parent.x = 3`), that change is reflected also by any children that have not yet overridden the value (which in this case would be `Child2`). That’s why the third print statement outputs `3 2 3`

## 76- What is `__slots__` in python?

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

- You can only specify attributes in `__slots__` that are instance variables. You cannot use `__slots__` to define class-level attributes or methods.

- If you define `__slots__` in a class, its instances will not be able to have a dictionary for attributes, so they will not be able to have any additional attributes beyond those listed in `__slots__`.

- Using `__slots__` can improve memory usage and performance, but it also means that you have to explicitly specify all of the attributes that an instance should have, which can be inconvenient if you need to add new attributes to an instance later on.

## 77- What is `__contains__` in python?

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
print(0 in color)  # prints False
print(255 in color)  # prints True
```

In this example, the `Color` class has a `__contains__` method that checks if the given value is one of the `r`, `g`, or `b` values of the `Color` instance. When you use the in operator with an instance of the `Color` class, it will call the `__contains__` method to determine whether the value is contained within the instance.

It's important to note that the `__contains__` method is not the same as the `__len__` method, which is used to implement the `len()` function. The `__len__` method should return the length of the object, while the `__contains__` method should return a boolean indicating whether the object contains a given value.

## 78- What is a "callable"?

A callable is an object we can call - function or an object implementing the `__call__` special method. Any object can be made callable.

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
print(callable(greet))  # prints True
print(callable(g.greet))  # prints True
print(callable(cc))  # prints True
print(callable(1))  # prints False
```

## 79- How would you `XOR` in Python?

1. `(a and not b) or (not a and b)`
2. `bool(a) != bool(b)`
3. `bool(a) ^ bool(b)`
4. `from operator import xor -> xor(bool(a), bool(b))`

## 80- What is introspection/reflection and does Python support it?

Introspection is the ability to examine an object at runtime. Python has a `dir()` function that supports examining the attributes of an object, `type()` to check the object type, `isinstance()`, etc. While introspection is passive examination of the objects, reflection is a more powerful tool where we could modify objects at runtime and access them dynamically. E.g.  

- `setattr()` adds or modifies an object's attribute;  
- `getattr()` gets the value of an attribute of an object.

It can even invoke functions dynamically - `getattr(my_obj, "my_func_name")()`

## 81- What will be the ouput of lines 2, 4, 6, and 8 from the following code, and why?

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

**The ouput:**

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

In the first line, `list` is initialized as a list containing 5 copies of an empty list. When you append `10` to the first element of `list`, you are actually modifying the same empty `list` that is being referenced by all 5 elements of `list`. This is why all elements of `list` are modified when you append to the first element. In the fourth line, you are adding a new element to the end of `list`, which is why `30` is appended to the end of the list rather than being appended to one of the inner lists.

## 82- Write a function that prints the least integer that is not present in a given list and cannot be represented by the summation of the sub-elements of the list

```Python
def find_least_integer(lst):
    # Sort the list in ascending order
    lst.sort()

    # Initialize least integer to 1
    least_int = 1

    # Iterate through the list
    for num in lst:
        # If the current number is greater than least_int, return least_int
        if num > least_int:
            return least_int
        # If the current number is equal to least_int, increment least_int
        elif num == least_int:
            least_int += 1

    # Return least_int if no integer was found that was not present in the list
    # and could not be represented by the summation of the sub-elements of the list
    return least_int
```

This function first sorts the input list in ascending order, then iterates through the list and keeps track of the least integer that is not present in the list and cannot be represented by the summation of the sub-elements of the list. If the current number is greater than `least_int`, the function returns `least_int`. If the current number is equal to `least_int`, the function increments `least_int` and continues iterating through the list. If the loop completes without finding such an integer, the function returns `least_int`.

Here is an example of how to use the function:

```Python
lst = [1, 3, 6, 10, 11, 15]
print(find_least_integer(lst))  # Output: 2
```

## 83- How do you reverse a list? Can you come up with at least three ways?

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

All three of these methods produce the same output: a new list that is the reverse of the original list. The first method modifies the list in place, while the second and third methods create a new list.

## 84- How does Python execute code?

When you run a Python program, the interpreter executes the code you have written in a sequence of steps.

Here is a general outline of how the Python interpreter executes code:

1. The interpreter reads the code you have written and converts it into a series of instructions, called bytecode, that it can execute.
2. The interpreter loads the bytecode into memory and begins executing the instructions.
3. As the interpreter executes the instructions, it may encounter statements that define variables, functions, or classes. When this happens, the interpreter creates the corresponding objects in memory and assigns them to the specified names.
4. The interpreter may also encounter statements that call functions or methods. When this happens, the interpreter looks up the function or method and executes the code it contains.
5. If the interpreter encounters an error while executing the code, it will raise an exception. If the error is not caught by the code, the interpreter will print an error message and stop executing the program.

## 85- What is `__pycache__`?

The `__pycache__` directory is a directory that is created by the Python interpreter to store compiled bytecode files. When you run a Python program, the interpreter converts the source code into a form that is more efficient to execute. This conversion process is known as compiling. The compiled bytecode files are stored in the `__pycache__` directory so that they can be used in future executions of the program without the need to recompile the source code.

The `__pycache__` directory is typically located in the same directory as the Python source files that were used to create it. It is created automatically by the interpreter, and you do not need to worry about managing it manually.

Note that the `__pycache__` directory and the compiled bytecode files it contains are specific to a particular version of Python. This means that if you change the version of Python that you are using, the interpreter will create a new `__pycache__` directory with compiled bytecode files that are compatible with the new version of Python.

## 86- What is the unittest in Python?

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

In this example, the `TestAdd` class defines two test methods, `test_add_two_positive_numbers` and `test_add_two_negative_numbers`, which test the `add` function with different input values. The `unittest.main()` function is used to run the tests and report the results.

## 87- What is the difference between xrange and range?

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

The `xrange` function generates a sequence of numbers in a similar way to range, but it returns a `generator` object rather than a `list`. A generator is an object that produces a sequence of values one at a time, rather than generating the entire sequence at once. This means that `xrange` is more memory-efficient than range when generating large sequences of numbers.

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

The `xrange` function was introduced in **`Python 2`** as a more efficient alternative to range. In **`Python 3`**, the `range` function was redesigned to behave more like `xrange`, and `xrange` was removed from the language.

## 88- What is the use of `//` operator in Python?

In Python, the `//` operator is the floor division operator. It is used to perform division, but it returns the result as an integer rather than a floating-point number.

For example:

```Python
>>> 5 / 2
2.5
>>> 5 // 2
2
>>> 5.0 // 2
2.0
```

In the first example, the `/` operator is used to perform division, and it returns a floating-point number. In the second and third examples, the `//` operator is used to perform floor division, and it returns an integer.

The `//` operator is useful when you want to divide two numbers and you only care about the integer part of the result, rather than the fractional part. For example, you might use the `//` operator to calculate the number of times one number can be divided by another, or to calculate the number of times one number goes into another.

Here are a few more examples of the `//` operator in action:

```Python
>>> 10 // 3
3
>>> 10 // 4
2
>>> 10 // 5
2
>>> 10 // 6
1
```

## 89- How are dict and set implemented internally? What is the complexity of retrieving an item? How much memory do these structures consume?

In Python, both dictionaries (called `dict`) and `sets` are implemented using hash tables. A hash table is a data structure that uses a hash function to map keys to indices in an array, allowing for fast insertion, deletion, and lookup of keys.

In the case of `dict`, each key-value pair is stored in the hash table. The keys are used to calculate a hash value, which is used to determine the index in the array where the key-value pair should be stored. The value is then stored at that index. To retrieve a value from the `dict`, the hash function is used to calculate the index of the key-value pair, and the value is retrieved from that index.

The complexity of retrieving an item from a `dict` or a `set` is typically `O(1)` on average, meaning that it takes a constant amount of time to retrieve an item, regardless of the size of the `dict` or `set`. However, in the worst case, the complexity can be `O(n)`, meaning that it takes linear time to retrieve an item, if the hash function is poorly designed and causes many keys to hash to the same index.

As for memory consumption, the amount of memory that a `dict` or `set` consumes depends on the number of keys it contains and the size of the keys and values. In general, `dict` and `set` objects use more memory than other data structures, such as lists and tuples, because they store the keys and values in addition to the overhead of the hash table data structure. However, the exact amount of memory consumed will depend on the specific keys and values being stored and on the implementation of the Python interpreter.

## 90- What is MRO in Python? How does it work?

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
