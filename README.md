# 100 Python Interview Questions

## 1- Python uses a Global Interpreter Lock. Does that mean it doesn’t use real threads?

No, Python uses real threads, but the Global Interpreter Lock (GIL) is a mechanism that prevents multiple native threads from executing Python bytecodes at once. This lock is necessary because CPython, the reference implementation of Python, is not thread-safe, meaning that multiple threads can potentially interfere with each other and compromise the integrity of an application.

The GIL makes it easy to write simple, thread-safe Python programs, but it can also limit the performance of multi-threaded programs, especially ones that rely heavily on CPU-bound operations. In these cases, Python's threading module may not provide the level of parallelism that you need. In such cases, you may want to consider using an alternative implementation of Python that does not have a GIL, such as PyPy or Jython, or using a different approach to parallelism, such as the multiprocessing module or using subprocesses.

## 2- Is it possible to have a producer thread reading from the network and a consumer thread writing to a file, really work in parallel? What about the GIL?

Yes, it is possible to have a producer thread that reads from the network and a consumer thread that writes to a file work in parallel in Python, even with the GIL in place. This is because the GIL only prevents multiple native threads from executing Python bytecodes at once. It does not prevent threads from performing other operations, such as waiting for data to be available on a network socket or waiting for a file to be written to disk.

In the case of a producer thread reading from the network and a consumer thread writing to a file, the producer thread can block on a network read operation, allowing the consumer thread to run in the meantime. Similarly, the consumer thread can block on a file write operation, allowing the producer thread to run. In this way, the two threads can effectively work in parallel, even though only one native thread is executing Python bytecodes at a time due to the GIL.

It is important to note that the GIL can still limit the overall performance of a program that uses multiple threads, especially if the threads are CPU-bound. In such cases, you may want to consider using an alternative implementation of Python that does not have a GIL, or using a different approach to parallelism, such as the multiprocessing module or using subprocesses.

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

We then use the `reduce` function from the `functools` module to compute the product of all the even numbers in the `list`. The `reduce` function takes a function and an iterable as arguments and applies the function to the elements of the iterable in a cumulative manner, returning a single result. In this case, we pass a lambda function that multiplies its arguments and pass the iterator returned by `filter` as the iterable.

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

1. *Print statement vs print function*: In Python 2.x, the `print` statement is used to print output, while in Python 3.x, the `print` function is used. For example:

    ```Python
    # Python 2.x
    print "Hello, World!"

    # Python 3.x
    print("Hello, World!")

    ```

2. *Division operator*: In Python 2.x, the division operator (`/`) performs floor division for integers and float division for floating-point numbers. In Python 3.x, the division operator always performs float division.

    ```Python
    # Python 2.x
    print(10 / 3)  # Output: 3
    print(10 / 3.0)  # Output: 3.3333333333333335

    # Python 3.x
    print(10 / 3)  # Output: 3.3333333333333335
    print(10 / 3.0)  # Output: 3.3333333333333335
    ```

3. *Exception handling*: In Python 2.x, the `except` statement can be used to catch exceptions of any type, while in Python 3.x, the `except` statement must specify the type of exception being caught.

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

4. *Iterators*: In Python 2.x, the `iteritems` method is used to iterate over the keys and values of a dictionary, while in Python 3.x, the `items` method is used.

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

5. *Unicode support*: In Python 2.x, Unicode support is not fully integrated, and the unicode and str types are separate. In Python 3.x, Unicode is fully integrated, and the str type is used for Unicode strings.

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

*The output:*
the output will be an empty list `[]`.

The slicing syntax `list[start:end]` is used to retrieve a subset of the elements in a list. The `start` index specifies the index of the first element to retrieve, and the `end` index specifies the index of the element after the last element to retrieve. If you omit the `end` index, the slicing syntax will return all elements of the list starting from the `start` index until the end of the list.

In this case, the list `_list` has only five elements, so the valid indices are `0` through `4`. The index `10` is out of bounds for the list, so the slicing syntax _list`[10:]` will return an empty list.

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

* A directory structure for organizing code, tests, and documentation
* Basic configuration files, such as a `setup.py` file for packaging and distributing the project
* A `requirements.txt` file for specifying the project's dependencies
* A testing framework and sample test cases
* Documentation templates and guidelines

Skeleton code is often created for specific types of projects, such as web applications, command-line tools, or data science projects. There are many open-source skeleton code examples available online that you can use as a starting point for your own projects.

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

In general, you should use ***class methods*** when you need to define a method that operates on the class itself, rather than on an instance of the class. An example of this might be a factory method that creates a new instance of the class with some default values. You should use ***static methods*** when you need to define a method that operates on an argument or variables that are independent of the class and its instances. An example of this might be a utility function that performs some computation or transformation on its arguments, but does not need to access any class or instance attributes.

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

*The output:*

This is because of the integer caching mechanism in Python. To save time and memory costs, Python always pre-loads all the small integers in the range of [-5, 256].

Therefore, all the integers in [-5, 256] have been already saved in the memory. When a new integer variable in this range is declared, Python just references the cached integer to it and won’t create any new object.

Therefore, the explanations of the results are:

* When the variables `a` and `b` were assigned to 256, they were referenced to the same memory location where the 256 was stored. They pointed to the same object.
* When the variables `x` and `y` were assigned to 257, they were two different objects in different memory locations because the 257 is not on the small integers caching range.

Since the `is` operator is to compare the memory locations of two variables, the `a is b` should output `True`, and the `x is y` should output `False`.

## 17- In objective-oriented programming, there is a concept called abstract classes. Does Python support abstract classes as well?

Yes, Python does support abstract classes. In Python, an abstract class is a class that has one or more abstract methods. An abstract method is a method that has a declaration, but no implementation. Abstract methods are defined using the `abc` (abstract base class) module, which is part of the Python standard library.

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

In Python, "pickling" refers to the process of converting an object hierarchy (e.g., a list, dictionary, or user-defined object) into a byte stream, and "unpickling" refers to the process of reconstructing the object hierarchy from the byte stream.

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

Pickling is useful for storing complex objects to a file or for sending them over a network connection. However, it is important to note that the pickle module is not intended to be secure, and it is possible to construct malicious pickle data that can execute arbitrary code when unpickled. Therefore, it is generally not recommended to use pickle to serialize and transmit sensitive data over untrusted networks or to unserialize pickle data from untrusted sources.

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

1. ***Performance issues***: Python is generally slower than compiled languages like C or C++, which means that you may encounter performance issues when running computationally intensive tasks in Python. There are ways to improve the performance of Python code (e.g., using optimized libraries or writing code in Cython), but it is important to be aware of the performance limitations of the language.

2. ***Concurrency issues***: Python has a global interpreter lock (GIL) that prevents multiple threads from executing Python bytecodes at the same time, which can lead to concurrency issues when running multithreaded programs. There are ways to work around the GIL (e.g., using the `multiprocessing` module), but it is important to be aware of this limitation when writing concurrent programs in Python.

Here are some specific issues that you may encounter when dealing with performance and concurrency in Python:

* **Bottlenecks**: It can be difficult to identify which parts of your code are causing performance issues, especially if you are working with large datasets or complex algorithms. You may need to use profiling tools to identify bottlenecks in your code and optimize the most critical parts.

* **Memory usage**: Memory usage can also be a problem when working with large datasets or complex algorithms in Python. You may need to use memory-efficient data structures and algorithms, or write code in a memory-efficient way, to avoid running out of memory.

* **Lack of parallelism**: Because of the GIL, Python threads are not always able to run in parallel on multiple CPU cores. This can limit the scalability of multithreaded Python programs, especially on systems with many CPU cores.

* **Synchronization issues**: When working with concurrent programs, you may need to synchronize access to shared resources to avoid race conditions and other synchronization issues. This can be challenging in Python, especially if you are not familiar with the tools and techniques available for concurrency control.

To avoid these and other issues related to performance and concurrency in Python, it is important to be aware of the limitations of the language and to plan accordingly when writing and testing your code. You may need to use specialized tools and techniques, such as profiling and optimization tools, to improve the performance and scalability of your Python programs.

## 22- How to achieve multithreading in Python?

Python offers a multi-threading package but it is not really good for speeding up the code. The GIL is a great way though it is not really multithreading. It executes one at a time but takes turns for different threads really fast which makes it seem like processes are running simultaneously.

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

## 26- How to use self in Python?

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

* **Module namespace**: Each module in Python has its own namespace, which contains the identifiers defined in the module, such as functions, variables, and classes. When you import a module, the identifiers in the module's namespace become available in the current namespace.

* **Class namespace**: Each class in Python has its own namespace, which contains the identifiers defined in the class, such as methods and instance variables. When you create an instance of a class, the instance variables become part of the instance's namespace.

* **Function namespace**: Each function in Python has its own namespace, which contains the identifiers defined in the function, such as local variables and function arguments. The function namespace is created when the function is called and is destroyed when the function returns.

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

PEP stands for *Python Enhancement Proposal*. PEPs are documents that describe proposed changes, improvements, and new features for Python. They are written by Python developers and are used to communicate ideas and proposals for improving the language to the Python community.

There are different types of PEPs, including:

* **Standards Track PEPs**: These PEPs propose changes to the Python language itself, such as new syntax or built-in functions.

* **Informational PEPs**: These PEPs provide information about Python-related topics, such as best practices or design patterns.

* **Process PEPs**: These PEPs describe changes to the Python development process, such as how PEPs are submitted and reviewed.

PEPs are written in a standard format and are reviewed by the Python community through a process called the PEP process. The PEP process is designed to ensure that proposed changes to Python are well-documented, well-reasoned, and discussed by the community before being accepted and implemented.

## 29- What are dunder methods in python?

In Python, dunder methods (also known as "magic methods") are methods that are defined with double underscores (e.g., `__init__`, `__len__`) and are used to implement special behavior for objects. These methods are called "dunder" because they are surrounded by double underscores (i.e., "double underscore" or "dunder").

Dunder methods are used to define the behavior of various built-in operations in Python, such as arithmetic operations, attribute access, and object creation and destruction. For example, the `__init__` dunder method is used to initialize an object when it is created, the `__add__` dunder method is used to define the behavior of the `+` operator for an object, and the `__str__` dunder method is used to define the string representation of an object.

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

