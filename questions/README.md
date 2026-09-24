# 150+ Python Interview Questions

## Table of Contents

- [1- Python uses a Global Interpreter Lock. Does that mean it doesn’t use actual threads?](#1--python-uses-a-global-interpreter-lock-does-that-mean-it-doesnt-use-actual-threads)
- [2- Is it possible to have a producer thread reading from the network and a consumer thread writing to a file work in parallel? What about the GIL?](#2--is-it-possible-to-have-a-producer-thread-reading-from-the-network-and-a-consumer-thread-writing-to-a-file-work-in-parallel-what-about-the-gil)
- [3- What will be the output of the following code in each step?](#3--what-will-be-the-output-of-the-following-code-in-each-step)
- [4- Why are functions considered first-class objects in Python?](#4--why-are-functions-considered-first-class-objects-in-python)
- [5- Do arguments in Python get passed by reference or value?](#5--do-arguments-in-python-get-passed-by-reference-or-value)
- [6- What tools to use for linting, debugging, and profiling?](#6--what-tools-to-use-for-linting-debugging-and-profiling)
- [7- Give an example of filter and reduce over an iterable object](#7--give-an-example-of-filter-and-reduce-over-an-iterable-object)
- [8- What are `list` and `dict` comprehensions?](#8--what-are-list-and-dict-comprehensions)
- [9- What do we mean when we say that a specific Lambda expression forms a closure?](#9--what-do-we-mean-when-we-say-that-a-specific-lambda-expression-forms-a-closure)
- [10- Name a few differences between Python 2.x and 3.x](#10--name-a-few-differences-between-python-2x-and-3x)
- [11- How is memory managed in Python?](#11--how-is-memory-managed-in-python)
- [12- What will be the output of the following code?](#12--what-will-be-the-output-of-the-following-code)
- [13- A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers](#13--a-palindromic-number-reads-the-same-both-ways-the-largest-palindrome-made-from-the-product-of-two-2-digit-numbers-is-9009--91--99-find-the-largest-palindrome-made-from-the-product-of-two-3-digit-numbers)
- [14- What is skeleton code in Python?](#14--what-is-skeleton-code-in-python)
- [15- In Python classes, what is the difference between class methods and static methods? and when to use them](#15--in-python-classes-what-is-the-difference-between-class-methods-and-static-methods-and-when-to-use-them)
- [16- Please explain the following results of the code executed on a Python shell interpreter](#16--please-explain-the-following-results-of-the-code-executed-on-a-python-shell-interpreter)
- [17- In object-oriented programming, there is a concept called abstract classes. How to implement it?](#17--in-object-oriented-programming-there-is-a-concept-called-abstract-classes-how-to-implement-it)
- [18- What are `*args` and `**kwargs` in Python](#18--what-are-args-and-kwargs-in-python)
- [19- What is the difference between tuples, sets, and lists in Python?](#19--what-is-the-difference-between-tuples-sets-and-lists-in-python)
- [20- What are pickling and unpickling in Python?](#20--what-are-pickling-and-unpickling-in-python)
- [21- Does Python support multiple inheritance?](#21--does-python-support-multiple-inheritance)
- [22- What are the pitfalls and problems of Python language?](#22--what-are-the-pitfalls-and-problems-of-python-language)
- [23- How to achieve multithreading in Python?](#23--how-to-achieve-multithreading-in-python)
- [24- What is the use of `with` in Python?](#24--what-is-the-use-of-with-in-python)
- [25- How are `.py`, `.pyi`, `.pyd`, and `.pyc` files different?](#25--how-are-py-pyi-pyd-and-pyc-files-different)
- [26- What are decorators in Python?](#26--what-are-decorators-in-python)
- [27- How to use `self` in Python?](#27--how-to-use-self-in-python)
- [28- What are namespaces in Python?](#28--what-are-namespaces-in-python)
- [29- What is PEP?](#29--what-is-pep)
- [30- What are dunder methods in Python?](#30--what-are-dunder-methods-in-python)
- [31- What does `super` do in Python? and what is the difference between `super().__init__()` and explicit `superclass.__init__()`](#31--what-does-super-do-in-python-and-what-is-the-difference-between-super__init__-and-explicit-superclass__init__)
- [32- What is a property decorator in Python?](#32--what-is-a-property-decorator-in-python)
- [33- What is the difference between Cython and CPython?](#33--what-is-the-difference-between-cython-and-cpython)
- [34- Specify the difference between local and global variables in Python](#34--specify-the-difference-between-local-and-global-variables-in-python)
- [35- What are Python iterators?](#35--what-are-python-iterators)
- [36- What are Python generators?](#36--what-are-python-generators)
- [37- What is the difference between Python's Generators and Iterators?](#37--what-is-the-difference-between-pythons-generators-and-iterators)
- [38- What are Python documentation strings?](#38--what-are-python-documentation-strings)
- [39- Explain the use of `subn()`, `sub()`, and `split()` in the `“re”` module](#39--explain-the-use-of-subn-sub-and-split-in-the-re-module)
- [40- Define polymorphism in Python](#40--define-polymorphism-in-python)
- [41- What are the differences between Wheels and Eggs?](#41--what-are-the-differences-between-wheels-and-eggs)
- [42- What is the purpose of Python non-local statements?](#42--what-is-the-purpose-of-python-non-local-statements)
- [43- How is Python exception is handled?](#43--how-is-python-exception-is-handled)
- [44- Name the differences between functional and object-oriented programming](#44--name-the-differences-between-functional-and-object-oriented-programming)
- [45- What does the `PYTHONOPTIMIZE` flag do?](#45--what-does-the-pythonoptimize-flag-do)
- [46- What are descriptors? Is there a difference between a descriptor and a decorator?](#46--what-are-descriptors-is-there-a-difference-between-a-descriptor-and-a-decorator)
- [47- Generate random number](#47--generate-random-number)
- [48- What are itertools in Python?](#48--what-are-itertools-in-python)
- [49- what does itertools.islice do?](#49--what-does-itertoolsislice-do)
- [50- Why this code will never stop?](#50--why-this-code-will-never-stop)
- [51- What is the output of this code, and why?](#51--what-is-the-output-of-this-code-and-why)
- [52- Can we chain Multiple Decorators in Python?](#52--can-we-chain-multiple-decorators-in-python)
- [53- Build a recursive function using python](#53--build-a-recursive-function-using-python)
- [54- How to implement a binary search tree using Python?](#54--how-to-implement-a-binary-search-tree-using-python)
- [55- How to implement a binary search using Python?](#55--how-to-implement-a-binary-search-using-python)
- [56- How to implement a Linked list using Python?](#56--how-to-implement-a-linked-list-using-python)
- [57- what is `collections.OrderedDict`?](#57--what-is-collectionsordereddict)
- [58- what is `collections.defaultdict`?](#58--what-is-collectionsdefaultdict)
- [59- Can we implement an `array` using Python?](#59--can-we-implement-an-array-using-python)
- [60- What is the `bytes` type?](#60--what-is-the-bytes-type)
- [61- How to concatenate tuples in python?](#61--how-to-concatenate-tuples-in-python)
- [62- How to join two `sets`?](#62--how-to-join-two-sets)
- [63- What is the difference between Python's list methods append and extend?](#63--what-is-the-difference-between-pythons-list-methods-append-and-extend)
- [64- How to implement bubble sort in Python?](#64--how-to-implement-bubble-sort-in-python)
- [65- How to implement Heap sort in Python?](#65--how-to-implement-heap-sort-in-python)
- [66- How to implement Insertion sort in Python?](#66--how-to-implement-insertion-sort-in-python)
- [67- How to implement Merge sort in Python?](#67--how-to-implement-merge-sort-in-python)
- [68- How to implement Quick Sort in Python?](#68--how-to-implement-quick-sort-in-python)
- [69- How to implement Selection sort in Python?](#69--how-to-implement-selection-sort-in-python)
- [70- How to implement Shell sort in Python?](#70--how-to-implement-shell-sort-in-python)
- [71- What are the commands that are used to copy an object in Python?](#71--what-are-the-commands-that-are-used-to-copy-an-object-in-python)
- [72- What is the difference between deep and shallow copy?](#72--what-is-the-difference-between-deep-and-shallow-copy)
- [73- How can the ternary operators be used in Python?](#73--how-can-the-ternary-operators-be-used-in-python)
- [74- What will be the output of the code below?](#74--what-will-be-the-output-of-the-code-below)
- [75- What will be the output of the code below?](#75--what-will-be-the-output-of-the-code-below)
- [76- What will be the output of the code below?](#76--what-will-be-the-output-of-the-code-below)
- [77- What is `__slots__` in python?](#77--what-is-__slots__-in-python)
- [78- What is `__contains__` in python?](#78--what-is-__contains__-in-python)
- [79- What is a "callable"?](#79--what-is-a-callable)
- [80- How would you `XOR` in Python?](#80--how-would-you-xor-in-python)
- [81- What is introspection/reflection and does Python support it?](#81--what-is-introspectionreflection-and-does-python-support-it)
- [82- What will be the output of lines 2, 4, 6, and 8 from the following code, and why?](#82--what-will-be-the-output-of-lines-2-4-6-and-8-from-the-following-code-and-why)
- [83- Write a function that prints the least integer that is not present in a given list and cannot be represented by the summation of the sub-elements of the list](#83--write-a-function-that-prints-the-least-integer-that-is-not-present-in-a-given-list-and-cannot-be-represented-by-the-summation-of-the-sub-elements-of-the-list)
- [84- How do you reverse a list? Can you come up with at least three ways?](#84--how-do-you-reverse-a-list-can-you-come-up-with-at-least-three-ways)
- [85- How does Python execute code?](#85--how-does-python-execute-code)
- [86- What is `__pycache__`?](#86--what-is-__pycache__)
- [87- What is the unittest in Python?](#87--what-is-the-unittest-in-python)
- [88- What is the difference between xrange and range?](#88--what-is-the-difference-between-xrange-and-range)
- [89- What is the use of `//` operator in Python?](#89--what-is-the-use-of--operator-in-python)
- [90- How are dict and set implemented internally? What is the complexity of retrieving an item? How much memory do these structures consume?](#90--how-are-dict-and-set-implemented-internally-what-is-the-complexity-of-retrieving-an-item-how-much-memory-do-these-structures-consume)
- [91- What is MRO in Python? How does it work?](#91--what-is-mro-in-python-how-does-it-work)
- [92- How to distribute Python code?](#92--how-to-distribute-python-code)
- [93- How to work with Python transitive dependencies?](#93--how-to-work-with-python-transitive-dependencies)
- [94- What is the output of this code?](#94--what-is-the-output-of-this-code)
- [95- What is the output of this code?](#95--what-is-the-output-of-this-code)
- [96- What is packing and unpacking in Python?](#96--what-is-packing-and-unpacking-in-python)
- [97- What's the difference between `globals()`, `locals()`, and `vars()`?](#97--whats-the-difference-between-globals-locals-and-vars)
- [98- What is the `__init__.py` module, and what is it for?](#98--what-is-the-__init__py-module-and-what-is-it-for)
- [99- How do I view object methods?](#99--how-do-i-view-object-methods)
- [100- Which is a better practice - global import or local import in Python](#100--which-is-a-better-practice---global-import-or-local-import-in-python)
- [101- what is tilde symbol `(~)` used for in Python?](#101--what-is-tilde-symbol--used-for-in-python)
- [102- What is the difference between `__str__` and `__repr__`?](#102--what-is-the-difference-between-__str__-and-__repr__)
- [103- What is `lru_cache` decorator in Python?](#103--what-is-lru_cache-decorator-in-python)
- [104- What does `__all__` do?](#104--what-does-__all__-do)
- [105- List some of the dunder methods](#105--list-some-of-the-dunder-methods)
- [106- List some of the dunder methods used in Mathematical operations](#106--list-some-of-the-dunder-methods-used-in-mathematical-operations)
- [107- List some of the Dunder variables](#107--list-some-of-the-dunder-variables)
- [108- What are python frameworks for web development?](#108--what-are-python-frameworks-for-web-development)
- [109- Write an API using Django REST](#109--write-an-api-using-django-rest)
- [110- What are the differences between Django Framework and Django REST Framework?](#110--what-are-the-differences-between-django-framework-and-django-rest-framework)
- [111- Create a `LRU Caching` using OrderedDict class](#111--create-a-lru-caching-using-ordereddict-class)
- [112- In a peaceful kingdom, there are houses numbered from 1 to n. The king announces a prize of 100 gold coins to some special group of houses. You have been given the task to determine how many sets of three houses can form a special group, where the sum of the squares of two smaller house numbers is equal to the square of the largest house number](#112--in-a-peaceful-kingdom-there-are-houses-numbered-from-1-to-n-the-king-announces-a-prize-of-100-gold-coins-to-some-special-group-of-houses-you-have-been-given-the-task-to-determine-how-many-sets-of-three-houses-can-form-a-special-group-where-the-sum-of-the-squares-of-two-smaller-house-numbers-is-equal-to-the-square-of-the-largest-house-number)
- [113- Write a solution for the Max Pairwise Product Problem](#113--write-a-solution-for-the-max-pairwise-product-problem)
- [114- What is the difference between `__new__` and `__init__`? And how does object construction work?](#114--what-is-the-difference-between-__new__-and-__init__-and-how-does-object-construction-work)
- [115- How is memory allocated for `list`, `tuple`, and `set`?](#115--how-is-memory-allocated-for-list-tuple-and-set)
- [116- When a list grows beyond its allocated capacity, what happens to the underlying array allocation? And how are the existing elements handled?](#116--when-a-list-grows-beyond-its-allocated-capacity-what-happens-to-the-underlying-array-allocation-and-how-are-the-existing-elements-handled)
- [117- What hashing is used for `dict` keys, and how do `__hash__` and `__eq__` interact?](#117--what-hashing-is-used-for-dict-keys-and-how-do-__hash__-and-__eq__-interact)
- [118- What is `asyncio`, and how do `async`/`await` and the event loop actually work?](#118--what-is-asyncio-and-how-do-asyncawait-and-the-event-loop-actually-work)
- [119- Threading, multiprocessing, or asyncio — how do you choose a concurrency model?](#119--threading-multiprocessing-or-asyncio--how-do-you-choose-a-concurrency-model)
- [120- What is a metaclass, and when would you actually use one?](#120--what-is-a-metaclass-and-when-would-you-actually-use-one)
- [121- Do Python's type hints do anything at runtime?](#121--do-pythons-type-hints-do-anything-at-runtime)
- [122- What is the walrus operator (`:=`) and when is it useful?](#122--what-is-the-walrus-operator--and-when-is-it-useful)
- [123- What is in `functools` beyond `lru_cache`?](#123--what-is-in-functools-beyond-lru_cache)
- [124- What are `dataclasses`, and how do they compare to `NamedTuple`, `TypedDict`, and `attrs`?](#124--what-are-dataclasses-and-how-do-they-compare-to-namedtuple-typeddict-and-attrs)
- [125- How does the `import` system work, and how do you deal with circular imports?](#125--how-does-the-import-system-work-and-how-do-you-deal-with-circular-imports)
- [126- What is `weakref` and when do you need it?](#126--what-is-weakref-and-when-do-you-need-it)
- [127- What is structural pattern matching (`match`/`case`)?](#127--what-is-structural-pattern-matching-matchcase)
- [128- What is the difference between `is` and `==`, and when does object identity trip people up?](#128--what-is-the-difference-between-is-and--and-when-does-object-identity-trip-people-up)
- [129- What is monkey patching, and when is it appropriate?](#129--what-is-monkey-patching-and-when-is-it-appropriate)
- [130- How do operators dispatch to dunder methods, and what is `NotImplemented`?](#130--how-do-operators-dispatch-to-dunder-methods-and-what-is-notimplemented)
- [131- What is exception chaining, and what are `__context__`, `__cause__`, and `__suppress_context__`?](#131--what-is-exception-chaining-and-what-are-__context__-__cause__-and-__suppress_context__)
- [132- What modern exception features did Python 3.11 add (`add_note`, `ExceptionGroup`, `except*`)?](#132--what-modern-exception-features-did-python-311-add-add_note-exceptiongroup-except)
- [133- What is the `warnings` module, and how do `UserWarning`/`DeprecationWarning` differ from exceptions?](#133--what-is-the-warnings-module-and-how-do-userwarningdeprecationwarning-differ-from-exceptions)
- [134- Walk through the full class-creation protocol: `__prepare__`, the metaclass, and how `__call__` controls instantiation](#134--walk-through-the-full-class-creation-protocol-__prepare__-the-metaclass-and-how-__call__-controls-instantiation)
- [135- Reference cycles, `__del__`, `weakref`, and `gc.freeze()`: the practical garbage-collection questions](#135--reference-cycles-__del__-weakref-and-gcfreeze-the-practical-garbage-collection-questions)
- [136- What is `setup.py`, and how has Python packaging changed with `pyproject.toml`?](#136--what-is-setuppy-and-how-has-python-packaging-changed-with-pyprojecttoml)
- [137- What is GraphQL, how does it differ from REST, and how do you serve it from Python?](#137--what-is-graphql-how-does-it-differ-from-rest-and-how-do-you-serve-it-from-python)
- [138- How would you integrate an AI/ML model into a Python service, and what are the engineering concerns?](#138--how-would-you-integrate-an-aiml-model-into-a-python-service-and-what-are-the-engineering-concerns)
- [139- What does a senior engineer need to know about building on LLMs (tokens, context windows, RAG, structured output, hallucination)?](#139--what-does-a-senior-engineer-need-to-know-about-building-on-llms-tokens-context-windows-rag-structured-output-hallucination)
- [140- How do you actually test Python code — pytest fixtures, parametrization, and mocking?](#140--how-do-you-actually-test-python-code--pytest-fixtures-parametrization-and-mocking)
- [141- What is Pydantic, and how does it differ from `dataclasses`?](#141--what-is-pydantic-and-how-does-it-differ-from-dataclasses)
- [142- Beyond basic hints — what are `Protocol`, `TypeVar`/`Generic`, and how do you actually enforce types?](#142--beyond-basic-hints--what-are-protocol-typevargeneric-and-how-do-you-actually-enforce-types)
- [143- How do you find and fix a performance bottleneck in Python?](#143--how-do-you-find-and-fix-a-performance-bottleneck-in-python)
- [144- What are the security footguns every Python engineer must know?](#144--what-are-the-security-footguns-every-python-engineer-must-know)
- [145- How do you write your own context manager, and what's in `contextlib`?](#145--how-do-you-write-your-own-context-manager-and-whats-in-contextlib)
- [146- What does a senior need to know about talking to a database (ORM vs Core, sessions, pooling, transactions, N+1)?](#146--what-does-a-senior-need-to-know-about-talking-to-a-database-orm-vs-core-sessions-pooling-transactions-n1)
- [147- How should logging be done in a production Python service?](#147--how-should-logging-be-done-in-a-production-python-service)
- [148- Concurrency in practice: `concurrent.futures`, thread safety, and synchronization primitives](#148--concurrency-in-practice-concurrentfutures-thread-safety-and-synchronization-primitives)
- [149- What is ASGI vs WSGI, and how does a framework like FastAPI use dependency injection?](#149--what-is-asgi-vs-wsgi-and-how-does-a-framework-like-fastapi-use-dependency-injection)
- [150- What are the concrete steps to publish a library to PyPI with pip (build/twine), Poetry, or uv?](#150--what-are-the-concrete-steps-to-publish-a-library-to-pypi-with-pip-buildtwine-poetry-or-uv)
- [151- Free-threaded Python (PEP 703, no-GIL) and subinterpreters (PEP 684 and 734): what actually changes for concurrency?](#151--free-threaded-python-pep-703-no-gil-and-subinterpreters-pep-684-and-734-what-actually-changes-for-concurrency)
- [152- How does CPython execute bytecode? `dis`, the ceval loop, frames, and the specializing adaptive interpreter (PEP 659)](#152--how-does-cpython-execute-bytecode-dis-the-ceval-loop-frames-and-the-specializing-adaptive-interpreter-pep-659)
- [153- A deeper look at CPython memory: `pymalloc` arenas, pools, and blocks, `tracemalloc`, and diagnosing leaks and fragmentation](#153--a-deeper-look-at-cpython-memory-pymalloc-arenas-pools-and-blocks-tracemalloc-and-diagnosing-leaks-and-fragmentation)
- [154- Generators as coroutines: `send`, `throw`, `close`, and `yield from` — and how they became `async`/`await`](#154--generators-as-coroutines-send-throw-close-and-yield-from--and-how-they-became-asyncawait)
- [155- Customizing classes without a metaclass: `__init_subclass__`, `__set_name__`, and the descriptor protocol in depth](#155--customizing-classes-without-a-metaclass-__init_subclass__-__set_name__-and-the-descriptor-protocol-in-depth)

## 1- Python uses a Global Interpreter Lock. Does that mean it doesn’t use actual threads?

No — Python threads are **real OS threads**. `threading.Thread` maps to a genuine kernel-scheduled thread (a POSIX `pthread` or a Windows thread), not a green/user-space thread. What the Global Interpreter Lock (GIL) does is narrower than "no threads": it is a single mutex that ensures only **one thread executes Python bytecode at any given moment**. The threads are real; their execution of _Python_ code is serialised.

The reason the GIL exists is CPython's memory management. Every object carries a reference count that is mutated constantly (on nearly every assignment, argument pass, and scope exit). Making each of those increments and decrements individually atomic — with fine-grained locks or atomic instructions — would be slow and deadlock-prone. A single interpreter-wide lock sidesteps all of that: it keeps refcounting correct, keeps single-threaded code fast, and makes writing C extensions dramatically simpler because extension authors can assume no other Python code runs concurrently unless they explicitly release the lock.

The practical consequence a senior engineer needs to internalise:

- **CPU-bound work does not scale across threads.** Ten threads doing heavy computation take turns on one core and finish no faster than one — often slightly slower, because of the lock-handoff overhead. The GIL is released roughly every 5 ms (tunable via `sys.setswitchinterval`) to let another thread take a turn.
- **I/O-bound work scales fine**, because a thread **releases the GIL while it waits** on a socket, disk, or subprocess. This is why threading is still the right tool for concurrent network calls or file operations.
- To get true CPU parallelism, sidestep the GIL: use `multiprocessing`/`ProcessPoolExecutor` (separate processes, each with its own interpreter and GIL), or push the hot loop into a C extension that releases the GIL (NumPy, Cython with `nogil`).

Two clarifications that come up constantly:

- **The GIL is a CPython implementation detail, not a language feature.** Jython (JVM) and IronPython (.NET) have no GIL. A very common mistake is to lump PyPy in with them — **PyPy has a GIL too.**
- **The GIL is on its way out (optionally).** PEP 703 introduced a **free-threaded build** of CPython (experimental in 3.13, `python3.13t`), which removes the GIL in favour of fine-grained locking and lets threads run Python code truly in parallel. PEP 684 added per-interpreter GILs so sub-interpreters can run concurrently. These are opt-in and still maturing; the default CPython build you deploy today still has one global GIL.

## 2- Is it possible to have a producer thread reading from the network and a consumer thread writing to a file work in parallel? What about the GIL?

Yes, it is possible to have a producer thread that reads from the network and a consumer thread that writes to a file work in parallel in Python, even with the GIL in place. The GIL prevents multiple native threads from executing Python bytecodes simultaneously. It does not prevent threads from performing other operations, such as waiting for data to be available on a network socket or for a file to be written to disk.

With a producer thread reading from the network and a consumer thread writing to a file, the producer thread can block a network read operation, allowing the consumer thread to run. Similarly, the consumer thread can block a file write operation, allowing the producer thread to run. In this way, the two threads can effectively work in parallel, even though only one native thread executes Python bytecodes at a time due to the GIL.

It is important to note that the GIL can still limit the overall performance of a program that uses multiple threads, especially if the threads are CPU-bound. In such cases, consider using an alternative implementation of Python that does not have a GIL or using a different approach to parallelism, such as the multiprocessing module or using subprocesses.

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

```python
def greet(name):
  return "Hello, " + name

greeting = greet
print(greeting("John"))  # prints "Hello, John"
```

In this code, we define a function called `greet` that takes a single argument and returns a string. We then assign the function to a variable called `greeting` and call the `greeting` function just like we would call the `greet` function. This demonstrates how a function can be treated as a first-class object and assigned to a variable.

As another example, consider the following code:

```python
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

```python
def increment(x):
  x += 1

a = 10
increment(a)
print(a)  # prints 10
```

Here, the variable `a` remains unchanged because the function increment works with a new reference to the value `11`, leaving the original value of `a` intact.

For mutable objects (e.g., lists and dictionaries), the function operates on the original object because the reference to the same object is passed. For example:

```python
def append_one(lst):
  lst.append(1)

a = [1, 2, 3]
append_one(a)
print(a)  # prints [1, 2, 3, 1]
```

In this code, the `append_one` function takes an argument `lst` and appends the value `1` to the end of the list. When we pass the list `[1, 2, 3]` to the function as an argument and then print the value of `a`, the list has been modified to include the value `1` at the end. This is because the `append_one` function operates on the original list rather than a copy of the list.

The precise term for this model is **"call by object reference"** (sometimes "call by sharing"): the parameter name inside the function is bound to the _same object_ the caller passed. This is neither C's pass-by-value (which would copy the object) nor C++'s pass-by-reference (which would let you rebind the caller's variable). The single most important distinction to be able to state is **mutation versus rebinding**:

- **Mutating** the object through the parameter (`lst.append(1)`, `d["k"] = 1`) is visible to the caller, because both names point at the one shared object.
- **Rebinding** the parameter (`lst = [99]`, `x = x + 1`) is _not_ visible to the caller. Assignment binds the local name to a brand-new object; the caller's variable still points at the original.

```python
def mutate(lst):
    lst.append(99)      # mutates the shared object -> caller sees it

def rebind(lst):
    lst = [99]          # rebinds the LOCAL name only -> caller unaffected

a = [1, 2, 3]
mutate(a)
print(a)                # [1, 2, 3, 99]

b = [1, 2, 3]
rebind(b)
print(b)                # [1, 2, 3]  <- unchanged
```

You can see the mechanism with `id()`: inside `mutate`, `id(lst)` equals `id(a)` (same object); inside `rebind`, the assignment makes `id(lst)` change while `id(b)` stays put. Immutable objects behave "like pass-by-value" only because you can never mutate them — you can only rebind — so there is no shared mutation to observe.

It is crucial to understand how Python passes arguments when writing functions, as it can affect the behavior of your code. If you want to modify an object that you pass to a function and have the changes persist outside the function, you must use a mutable object such as a list or a dictionary. If you want to pass an object to a function and ensure that it is not modified, you should use an immutable object such as a number, string, or tuple.

## 6- What tools to use for linting, debugging, and profiling?

**Linting and formatting** (catch problems and enforce style before the code runs):

- **Ruff** — the modern default: an extremely fast (Rust-based) linter that consolidates and replaces Flake8, isort, pydocstyle, pyupgrade, and dozens of plugins, and also ships a formatter (`ruff format`) that is a drop-in for Black. One tool, one config in `pyproject.toml`.
- **Black** — the opinionated, near-zero-config formatter that ended most style debates; Ruff's formatter is compatible with it.
- **Flake8 / Pylint** — the previous generation. Pylint is still valued for its deeper, more opinionated analysis (design smells, refactor hints); Flake8 (PyFlakes + pycodestyle + McCabe) is largely superseded by Ruff.
- **Type checkers** are a distinct and essential category: **mypy** (the reference checker) and **Pyright** (fast, powers Pylance in VS Code) verify type annotations statically and catch a whole class of bugs before runtime.
- In practice these run automatically via **pre-commit** hooks and in CI, so nothing unformatted or unlinted lands on the main branch.

**Debugging:**

- **`breakpoint()`** — the built-in (Python 3.7+) that drops into the debugger at that line; it honours the `PYTHONBREAKPOINT` env var so you can redirect it to another debugger or disable it globally. This has replaced the old `import pdb; pdb.set_trace()`.
- **pdb / ipdb** — the standard library debugger (step, inspect, set breakpoints, post-mortem with `pdb.pm()`); `ipdb` adds IPython's niceties.
- **IDE debuggers** — PyCharm and VS Code offer graphical breakpoints, conditional breakpoints, watch expressions, and remote debugging (`debugpy`).
- Humble but effective: `logging` at DEBUG level, and `rich`/`icecream` for readable inspection output.

**Profiling** (measure before you optimise — never guess):

- **cProfile** (+ `pstats`, or the `snakeviz` visualiser) — the built-in deterministic profiler for _where CPU time goes_ by function.
- **timeit** — for micro-benchmarks of small snippets, handling warm-up and repetition correctly.
- **py-spy** — a sampling profiler that attaches to a _running_ process without modifying or restarting it and emits flame graphs; the go-to for profiling production services (it replaces the abandoned Pyflame).
- **line_profiler** (`@profile`) — line-by-line timing when you need to know which _line_ in a hot function is the cost.
- **Memory profiling** is a separate concern: **tracemalloc** (standard library, snapshots and diffs allocations by line), **memory_profiler** (per-line memory), and **Scalene** (profiles CPU, GPU, and memory together, and separates Python time from native/C time — often the single most informative tool).

The senior mindset behind all this: formatting and linting are automated and non-negotiable (pre-commit + CI), and optimisation is always driven by a profiler on representative data, not by intuition about what is "probably slow".

## 7- Give an example of filter and reduce over an iterable object

Here is an example of using the `filter` and `reduce` functions to process an iterable object in Python:

```python
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

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
```

This would create a new list `even_numbers` containing only the even numbers from the original list `numbers`.

A dictionary comprehension is similar to list comprehension, but it creates a new dictionary instead of a list. It consists of a dictionary key expression followed by a `for` clause, then zero or more `for` or `if` clauses. The result is a new dictionary computed by evaluating the key and value expressions in the context of the `for` and `if` clauses.

For example, suppose we have a list of strings, and we want to create a new dictionary that maps each string to its length. We could do this using a dictionary comprehension as follows:

```python
strings = ['cat', 'dog', 'bird']
lengths = {s: len(s) for s in strings}
```

This would create a new dictionary `lengths` that maps each string to its length.

## 9- What do we mean when we say that a specific Lambda expression forms a closure?

A closure is a function that retains access to the variables in the environment it was defined, even after the code that defined the function has finished executing. This means that the function can still reference and modify the variables even if the function is called in a different context, such as in a different function or a different part of the program.

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

1. _Print statement vs print function_: In Python 2.x, the `print` statement is used to print output, while in Python 3.x, the `print` function is used. For example:

   ```python
   # Python 2.x
   print "Hello, World!"

   # Python 3.x
   print("Hello, World!")

   ```

2. _Division operator_: In Python 2.x, the division operator (`/`) performs floor division for integers and float division for floating-point numbers. In Python 3.x, the division operator always performs float division.

   ```python
   # Python 2.x
   print(10 / 3)  # Output: 3
   print(10 / 3.0)  # Output: 3.3333333333333335

   # Python 3.x
   print(10 / 3)  # Output: 3.3333333333333335
   print(10 / 3.0)  # Output: 3.3333333333333335
   ```

3. _Exception handling_: In Python 2.x, the exception instance is bound with a comma (`except ValueError, e:`), while Python 3.x requires the `as` keyword (`except ValueError as e:`). A bare `except:` that catches every exception type remains valid in both versions, although catching a specific type is the recommended practice.

   ```python
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

5. _Unicode support_: In Python 2.x, Unicode support is not fully integrated, and the Unicode and str types are separate. In Python 3.x, Unicode is fully integrated, and the str type is used for Unicode strings.

## 11- How is memory managed in Python?

CPython manages memory automatically through **two cooperating mechanisms**: reference counting (the primary, always-on system) and a cyclic garbage collector (a backup for reference cycles). Understanding that split is the core of a senior-level answer.

**1. Reference counting — the primary mechanism.** Every object carries a counter of how many references point to it (visible, with caveats, via `sys.getrefcount(obj)`). The count is incremented when a new name binds to the object and decremented when a reference goes away (rebinding, `del`, scope exit). The instant it hits **zero**, the object is deallocated immediately and deterministically — memory is reclaimed the moment the last reference disappears, not at some later sweep.

```python
import sys
a = []
b = a
print(sys.getrefcount(a))   # 3: a, b, and the temporary arg to getrefcount itself
del b
print(sys.getrefcount(a))   # 2
```

Reference counting is simple and prompt, but it has one fatal blind spot: **reference cycles.** Two objects that refer to each other keep each other's count above zero even when nothing else can reach them.

**2. The cyclic garbage collector — the backup.** To reclaim those cycles, CPython adds a second collector (the `gc` module) that periodically finds groups of container objects reachable only through cycles and frees them. Key facts:

- It only tracks **container types** (lists, dicts, sets, class instances) — the only objects that can _form_ cycles. Atomic objects like `int` and `str` are managed by refcounting alone and are never touched by the cyclic collector.
- It is **generational**: objects are grouped into three generations (0, 1, 2). New objects start in generation 0, which is collected most often; survivors are promoted to older generations that are scanned progressively less frequently. This exploits the "most objects die young" observation to keep collection cheap.
- It runs based on allocation-count thresholds (`gc.get_threshold()`), not a timer. You can trigger it (`gc.collect()`), disable it (`gc.disable()` — sometimes done in latency-sensitive or short-lived batch processes), and inspect it.

**3. The allocator layers — where the memory actually comes from.** CPython does not call `malloc` for every object. All Python objects live in a **private heap**, fronted by a layered allocator:

- **pymalloc** is the object allocator for small objects (≤ 512 bytes — the overwhelming majority). It requests big chunks from the OS called **arenas** (256 KB), carves each arena into 4 KB **pools**, and each pool into fixed-size **blocks**. Same-sized small objects are served from the same pool, which cuts fragmentation and avoids constant OS calls.
- Larger allocations bypass pymalloc and go to the system allocator.
- A crucial consequence: **freeing Python objects does not necessarily return memory to the OS.** Freed blocks go back to pymalloc's free lists for reuse; an arena is only released when _entirely_ empty. This is why a process's resident memory often stays high after a big data structure is discarded — the memory is free for reuse by Python, just not handed back.

**4. Caches that reuse objects.** CPython pre-creates and reuses certain immutable objects, so they are never really "allocated" in hot paths: **small integers −5 to 256** are singletons, and many **strings are interned** (identifiers, and short compile-time literals). This is why `256 is 256` is `True` but `257 is 257` may be `False` (see the integer-caching question).

**5. Tools and hooks worth naming:**

- `sys.getsizeof(obj)` — shallow size of one object in bytes (does not follow references).
- `tracemalloc` — the standard-library way to trace allocations by line and diff snapshots; the right tool for finding a memory leak.
- `gc.get_objects()`, `gc.get_referrers()`, and libraries like `objgraph` — for hunting down what is keeping an object alive.
- `weakref` — references that _don't_ increment the count, so they don't keep an object alive (used for caches and to break cycles).
- `__del__` — a finaliser run at deallocation; unreliable for cleanup (timing isn't guaranteed, and it can even resurrect objects), so prefer context managers for releasing resources.

## 12- What will be the output of the following code?

```python
_list = ['a', 'b', 'c', 'd', 'e']
print(_list[10:])
```

_The output:_
the output will be an empty list `[]`.

The slicing syntax `list[start: end]` retrieves a subset of the elements in a list. The `start` index specifies the index of the first element to retrieve, and the `end` index specifies the element's index after the last element to retrieve. If you omit the `end` index, the slicing syntax will return all elements of the list, starting from the `start` index until the end of the list.

In this case, the list `_list` has only five elements, so the valid indices are `0` through `4`. The index `10` is out of bounds for the list, so the slicing syntax `_list[10:]` will return an empty list.

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

```python
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

```python
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

## 17- In object-oriented programming, there is a concept called abstract classes. How to implement it?

In Python, an abstract class is a class that has one or more abstract methods. An abstract method is a method that has a declaration, but no implementation. Abstract methods are defined using the `abc` (abstract base class) module, which is part of the Python standard library.

To create an abstract class in Python, you need to do the following:

1. Import the abc module.
2. Create a class that derives from abc.ABC.
3. Declare one or more abstract methods using the `@abc.abstractmethod` decorator.
   Here is an example of an abstract class in Python:

   ```python
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

The points that separate a textbook answer from a senior one:

- **The real enforcement is at instantiation, and it is a hard failure.** `Animal()` raises `TypeError: Can't instantiate abstract class Animal with abstract method make_sound` — and so does any subclass that _forgets_ to implement every abstract method. That is the whole value: the failure happens loudly at object-creation time, not later as a mysterious `AttributeError` at first call.
- **`@abstractmethod` composes with other decorators**, so you can require an abstract `property`, `classmethod`, or `staticmethod` — always with `@abstractmethod` **innermost** (closest to the method):

  ```python
  class Shape(abc.ABC):
      @property
      @abstractmethod
      def area(self): ...
  ```

- **`register()` creates _virtual_ subclasses.** You can declare that an unrelated existing class satisfies an ABC without editing it or inheriting from it — `MyABC.register(SomeClass)` makes `issubclass`/`isinstance` return `True`. This is exactly how the `collections.abc` hierarchy (`Iterable`, `Sequence`, `Mapping`, …) recognises built-in and third-party types.
- **Prefer inheriting `abc.ABC` over setting `metaclass=abc.ABCMeta`.** `ABC` is just a convenience base class that already uses that metaclass; you only reach for the explicit metaclass form when combining with another metaclass.
- **ABCs are nominal; `typing.Protocol` is structural.** An ABC requires you to explicitly subclass (or `register`). A `Protocol` (PEP 544) matches any object that merely _has_ the right methods — duck typing that a static type checker can verify — with no inheritance required. Reach for an ABC when you want to _share implementation_ and enforce a contract by inheritance; reach for a Protocol when you only want to describe a shape that arbitrary types can satisfy.

## 18- What are `*args` and `**kwargs` in Python

In Python, the `*args` and `**kwargs` syntax is used to pass a variable number of arguments to a function.

`*args` is used to pass a variable number of non-keyworded arguments to a function. It is used to pass a tuple of arguments to the function. For example:

```python
def my_function(arg1, *args):
    print(arg1)
    print(args)

my_function(1, 2, 3, 4, 5)

# Output:
# 1
# (2, 3, 4, 5)
```

`**kwargs` is used to pass a variable number of keyworded arguments to a function. It is used to pass a dictionary of keyword arguments to the function. For example:

```python
def my_function(**kwargs):
    print(kwargs)

my_function(arg1=1, arg2=2, arg3=3)

# Output: {'arg1': 1, 'arg2': 2, 'arg3': 3}
```

Both `*args` and `**kwargs` are commonly used in Python to allow a function to accept a variable number of arguments. They can be useful when you want to write a function that can be flexible and handle a wide range of input parameters.

The senior-level details:

- **The names are convention, not syntax.** It is the `*` and `**` that matter; `*args`/`**kwargs` are just the customary names. `*` collects extra positionals into a **tuple**, `**` collects extra keywords into a **dict**.
- **There is a fixed parameter order**, and getting it wrong is a `SyntaxError`: standard/positional parameters, then `*args`, then **keyword-only** parameters, then `**kwargs`. Anything after `*args` (or a bare `*`) can _only_ be passed by keyword:

  ```python
  def f(a, b, *args, key, **kwargs): ...
  #     └ positional ┘ └ variadic ┘ └ keyword-only ┘ └ variadic kw ┘

  def g(a, b, *, verbose=False):     # bare * -> verbose is keyword-only
      ...
  g(1, 2, verbose=True)              # OK
  # g(1, 2, True)                    # TypeError: too many positional arguments
  ```

- **Positional-only parameters** use a `/` marker (Python 3.8+): everything _before_ the `/` cannot be passed by keyword. The built-ins are written this way (`len(obj, /)`), and it lets you rename a parameter later without breaking callers:

  ```python
  def h(x, y, /, z):     # x, y positional-only; z either way
      ...
  ```

- **`*` and `**` also work at the _call_ site to unpack**, which is the mirror image of collecting them in the signature: `f(*my_list, **my_dict)` spreads a list into positional args and a dict into keyword args. This is why `*args`/`**kwargs` is the standard way to write a **transparent wrapper** (e.g. a decorator) that forwards whatever it received: `def wrapper(*args, **kwargs): return func(*args, **kwargs)`.

## 19- What is the difference between tuples, sets, and lists in Python?

In Python, tuples, sets, and lists are all data types that can be used to store collections of items. Here are the main differences between them:

1. **Tuples** are immutable, which means that you cannot modify the values of the items in a tuple once it has been created. They are defined using parentheses `()` and their items are separated by commas. also, tuples are generally faster and use less memory than lists, because they do not have the overhead of the extra methods and behaviors that are associated with lists. However, the difference in performance between tuples and lists is usually small and may not be noticeable in most cases.

2. **Sets** are mutable, but unlike lists they do not have a specific order and do not allow duplicate items. Sets are defined using curly braces `{}` and their items are separated by commas — note that `{}` on its own creates an empty dictionary, so use `set()` for an empty set. You can add and remove items after creation with `add()`, `remove()`, and `discard()`. Sets provide much faster membership tests (`x in s`) than lists, because they are implemented using a hash table data structure, which allows for efficient insertion, deletion, and lookup of items. Their items must be hashable, which means a set can hold tuples but not lists or other sets. If you need an immutable, hashable set, use `frozenset` instead. However, sets do not maintain the order of their items, which can be a drawback if you need to preserve the order of the items in your collection.

3. **Lists** are mutable, which means that you can change the values of their items after the list has been created. They are defined using square brackets `[]` and their items are separated by commas. also, Lists are generally slower and use more memory than tuples, because they are mutable and have the overhead of the extra methods and behaviors that are associated with them. However, lists are more flexible than tuples because you can modify their items after the list has been created.

```python
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

```python
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

```python
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

```python
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

Python's pitfalls fall into two buckets: **language-level footguns** (surprising semantics that bite everyone eventually) and **platform-level limitations** (structural properties of the runtime). A senior engineer should be able to reel off both.

**Language-level gotchas** (most have a dedicated question elsewhere in this file):

- **Mutable default arguments.** `def f(x, items=[])` shares _one_ list across all calls, because defaults are evaluated once at definition time. Use `items=None` + `if items is None: items = []`.
- **Late-binding closures.** `[lambda: i for i in range(3)]` all capture the _variable_ `i`, not its value, so they all return `2`. Bind with a default arg (`lambda i=i: i`).
- **`is` vs `==`.** `is` compares identity, `==` compares value. Small-int and string caching makes `is` _appear_ to work on values (`256 is 256`) until it suddenly doesn't (`257 is 257`). Only use `is` for `None`/`True`/`False`/sentinels.
- **Floating-point equality.** `0.1 + 0.2 != 0.3`. Never test floats for exact equality; use `math.isclose`.
- **Shared references and aliasing.** `[[0] * 3] * 2` makes two references to one inner list; `b = a` does not copy. Know shallow vs deep copy.
- **Integer division and modulo sign.** `//` floors toward negative infinity, and `%` takes the sign of the divisor — different from C.
- **Truthiness surprises.** Empty containers, `0`, and `""` are falsy; `if my_list:` tests emptiness, not existence. `if x == None` should be `if x is None`.
- **Catch-all `except:`** silently swallows bugs and even `KeyboardInterrupt`. Catch specific exceptions.

**Platform-level limitations:**

- **The GIL** serialises Python bytecode execution, so threads don't give CPU-bound parallelism (use `multiprocessing` or C extensions; see the GIL questions).
- **Raw execution speed.** As a dynamically typed, interpreted language, pure-Python numeric loops are far slower than C — which is why the ecosystem pushes hot paths into NumPy/Cython/native extensions.
- **Memory footprint.** Every value is a full heap object with refcount and type-pointer overhead; a `list` of a million ints costs far more than a C array (mitigate with `array`, `__slots__`, NumPy, or generators).
- **Dynamic typing defers errors to runtime.** A typo or type mismatch may only surface on the code path that hits it — the reason type hints + mypy/Pyright and good test coverage matter so much on large codebases.
- **Packaging and dependency management** are historically painful (multiple competing tools, environment isolation, transitive-dependency conflicts), though `pyproject.toml`, lock files, and tools like uv/Poetry have improved it a lot.
- **Startup time and distribution.** Shipping Python to machines without an interpreter needs PyInstaller/containers; interpreter start-up is non-trivial for short-lived CLIs.

The balanced senior take: none of these make Python a poor choice — its readability, ecosystem, and development speed usually dominate. The skill is knowing _when_ a limitation actually bites (a tight CPU-bound inner loop, a memory-constrained service) and reaching for the right escape hatch, rather than avoiding Python or fighting it prematurely.

## 23- How to achieve multithreading in Python?

Multithreading in Python is achieved with the built-in `threading` module, either by instantiating `threading.Thread` with a target callable or by using `concurrent.futures.ThreadPoolExecutor` for a higher-level pool interface.

```python
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

```python
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

```python
with open('filename.txt', 'r') as f:
    contents = f.read()

# the file is closed automatically here, even if f.read() raised an exception
```

Without the `with` statement you would have to release the resource yourself in a `try`/`finally` block. The following code is equivalent to the example above, which shows what `with` saves you from writing:

```python
f = open('filename.txt', 'r')
try:
    contents = f.read()
finally:
    f.close()
```

You can also write your own context manager, either by implementing `__enter__` and `__exit__` on a class or by using the `@contextlib.contextmanager` decorator:

```python
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

```python
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

```python
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

```python
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

```python
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

```python
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

```python
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

```python
class Cat(Animal):
    def __init__(self, name, breed, toy):
        Animal.__init__(self, name, species="Cat")
        self.breed = breed
        self.toy = toy
```

In this single-inheritance example the two forms happen to produce the same result, but **they are not equivalent in general**. There are three real differences:

**1. `super()` follows the MRO; an explicit call hard-codes one class.** With multiple inheritance, the next class in the MRO is not necessarily the class you named. Explicit calls can therefore run a shared base class more than once — the classic diamond problem:

```python
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

```python
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

```python
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

```python
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

```python
x = 10

def some_function():
    x = 5
    print(x) # prints 5

some_function()
print(x) # prints 10
```

In this case, the `x` variable within the `some_function` function is a local variable and takes precedence over the global `x` variable. When you print `x` within the `some_function` function, it will print the value of the local `x` variable, which is **`5`**. When you print `x` outside of the function, it will print the value of the global `x` variable, which is **`10`**.

To access the global variable from within a function, you can use the global keyword to specify that you want to access the global variable, like this:

```python
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

```python
my_list = [1, 2, 3]          # an ITERABLE, not an iterator

print(list(my_list))         # [1, 2, 3]
print(list(my_list))         # [1, 2, 3] - a fresh iterator each time

it = iter(my_list)           # an ITERATOR
print(list(it))              # [1, 2, 3]
print(list(it))              # []  <- exhausted, and it stays that way
```

Here is an example of how you can use an iterator to iterate over a list in Python:

```python
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

```python
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

```python
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

```python
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

```python
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

```python
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

```python
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

```python
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

```python
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

```python
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

```python
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

```python
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

```python
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

```python
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

```python
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

```python
try:
    # Code that might cause an exception goes here
    x = int('foo')
except ValueError:
    # Code to handle the exception goes here
    print('Invalid input')
```

In this example, the `try` block contains code that might cause a _ValueError_ exception to be raised (in this case, attempting to convert the string 'foo' to an integer). If the exception is raised, the execution of the `try` block is halted, and control is transferred to the `except` block. The `except` block contains code that is executed to handle the exception. In this case, it prints an error message to the console.

You can also specify multiple `except` blocks to handle different types of exceptions:

```python
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

```python
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

```python
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

```python
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

```python
try:
    result = 10 / 0
except (ValueError, TypeError) as e:   # one handler for several types
    print(f"Bad input: {e}")
except ZeroDivisionError as e:
    print(f"Division error: {e}")
```

Handlers are checked in order, and the first matching one wins. Because `except` matches subclasses too, always order handlers from most specific to most general — putting `except Exception` first would swallow everything below it.

**Raising exceptions**, including your own:

```python
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

Custom exceptions should subclass `Exception` (not `BaseException`, which also covers `KeyboardInterrupt` and `SystemExit` — signals you almost never want to intercept). By convention (PEP 8) name them with an **`Error` suffix**, not `Exception` — `InsufficientFundsError`, not `InsufficientFundsException` (a habit worth unlearning if you come from Java). Whatever arguments you pass to an exception's constructor are stored on its **`.args`** tuple, so `e.args[0]` retrieves the original message even when you didn't define custom attributes.

**Re-raising and chaining.** A bare `raise` inside a handler re-raises the current exception with its original traceback intact, which is the right way to log and pass along. `raise ... from e` records the original cause:

```python
try:
    config = load_config()
except FileNotFoundError as e:
    raise RuntimeError("Configuration missing") from e   # preserves the cause
```

(For the full mechanics of chaining — `__context__`, `__cause__`, `__suppress_context__`, and `raise ... from None` — see the dedicated exception-chaining question later in this file.)

**Antipatterns to avoid:**

- `except:` or `except Exception:` with an empty or `pass` body — this hides real bugs and makes failures silent. Catch only what you can actually handle.
- A bare `except:` also catches `KeyboardInterrupt` and `SystemExit`, making a program impossible to interrupt with Ctrl-C. Use `except Exception:` if you really must be broad.
- **Returning from a `finally` block.** A `return` (or `break`/`continue`) inside `finally` overrides any `return` value — or any in-flight exception — coming from the `try`/`except`, silently swallowing errors. Keep `finally` for cleanup only.
- Using exceptions for ordinary control flow where a simple conditional is clearer.

That said, Python idiom favours **EAFP** — "easier to ask forgiveness than permission" — over defensive pre-checks. Attempting the operation and handling the exception is usually preferred to checking first, since the check can race or miss cases:

```python
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

Despite the name, it performs very little optimization. It does exactly three things:

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

```python
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

```python
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

```python
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

```python
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

```python
import random

random.seed(42)
print([random.randint(1, 10) for _ in range(3)])   # e.g. [2, 1, 5]

random.seed(42)                                     # same seed...
print([random.randint(1, 10) for _ in range(3)])   # ...same sequence
```

Seeding with the current time (`random.seed(time.time())`) is unnecessary — the generator already seeds itself from the operating system's entropy at import time, so you only call `seed()` when you specifically want reproducibility.

One important caveat worth raising in an interview: **`random` is not cryptographically secure.** It uses a Mersenne Twister, which is fast and statistically excellent but fully predictable — an observer who sees enough output can recover the internal state and predict all future values. For passwords, tokens, session IDs, or anything security-related, use the `secrets` module instead:

```python
import secrets

secrets.randbelow(100)        # cryptographically secure integer in [0, 100)
secrets.token_hex(16)         # secure random hex string, e.g. for a token
secrets.choice(['a', 'b'])    # secure choice from a sequence
```

## 48- What are itertools in Python?

The `itertools` module is a Python module that provides a number of functions that are helpful when working with iterators. Iterators are objects that allow you to iterate over a sequence of values, such as a list or a string.

Here are a few examples of functions that are available in the `itertools` module:

Everything in `itertools` returns a **lazy iterator**, so values are produced on demand rather than built up in a list. That is what makes it usable with infinite sequences and large data sets.

```python
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

```python
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

```python
import itertools

# Works on an infinite iterator - ordinary slicing cannot do this
first_five_evens = itertools.islice(itertools.count(0, 2), 5)
print(list(first_five_evens))    # [0, 2, 4, 6, 8]
```

Two practical caveats: `islice` does not accept negative indices (it cannot count from the end without consuming everything), and it **consumes** the underlying iterator, so elements it skips are gone for good.

You can also use `itertools.islice` to slice at a specific starting and ending position with a specific step size. For example, `itertools.islice(numbers, 2, 6, 1)` returns an iterator producing the elements at indices `2` through `5`. Below are examples of output based on various inputs:

```python
# itertools.islice(iterable, stop)
# itertools.islice(iterable, start, stop, step)

# islice('ABCDEFG', 2)          --> A B
# islice('ABCDEFG', 2, 4)       --> C D
# islice('ABCDEFG', 2, None)    --> C D E F G
# islice('ABCDEFG', 0, None, 2) --> A C E G
```

## 50- Why this code will never stop?

```python
i = 0
while i != 1:
    i += 0.1
    print(i)
```

This code will never stop because the condition `i != 1` is never satisfied. `0.1` cannot be represented exactly in binary floating point — it is stored as a value very slightly different from one tenth — so adding it repeatedly accumulates a small error:

```python
i = 0
for _ in range(10):
    i += 0.1
print(repr(i))    # 0.9999999999999999
print(i == 1)     # False
```

After ten additions `i` is `0.9999999999999999`, not `1.0`. The eleventh addition takes it to `1.0999999999999999`, so the loop **steps straight over `1`** without ever hitting it.

It is worth being precise about what happens next: `i` does not converge on `1` or hover near it. It keeps increasing without bound — past 2, past 100, forever — because nothing in the loop stops it. The loop is infinite not because `i` approaches `1` too slowly, but because it passes `1` and never comes back.

The general lesson is to **never test floating-point values for exact equality**. Use one of these instead:

```python
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

```python
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

```python
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

```python
@decorator1
@decorator2
@decorator3
def function():
    ...  # function code goes here
```

Stacked decorators are applied **bottom-up**: the decorator closest to the `def` wraps the function first. The stack above is exactly equivalent to:

```python
function = decorator1(decorator2(decorator3(function)))
```

So at definition time `decorator3` is applied first and `decorator1` last — `decorator1` ends up as the outermost wrapper. At **call** time the order reverses: the outermost wrapper (`decorator1`) runs first, then delegates inward. Keeping these two orders straight — bottom-up application, top-down execution — is the point interviewers usually probe.

```python
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

```python
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

```python
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

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

This `Node` class has three instance variables: `value`, `left`, and `right`. The `value` variable stores the value of the `node`, and the `left` and `right` variables are references to the `left` and `right` child nodes, respectively.

To implement the `BST` itself, you will need to create a `BST` class that has methods for inserting and searching for nodes in the `tree`. Here is an example of how you could implement a `BST` class in Python:

```python
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

```python
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

```python
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

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

This `Node` class has two instance variables: `value` and `next`. The `value` variable holds the value of the `node`, and the `next` variable holds a reference to the `next` node in the linked list.

Next, you can define the `LinkedList` class, which will contain methods for inserting nodes into the linked list and searching for specific values:

```python
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

```python
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

```python
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

  ```python
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

```python
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

```python
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

```python
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

```python
b = b'Hello, world!'
```

You can also create a `bytes` object from a list of integers using the `bytes` function:

```python
b = bytes([104, 101, 108, 108, 111])  # b'hello'
```

You can access the individual bytes of a `bytes` object using indices like you would with a string:

```python
b = b'Hello, world!'
print(b[0])  # Output: 72
print(b[1])  # Output: 101
```

You can also use slicing to extract a sub-sequence of bytes from a `bytes` object:

```python
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

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

tuple3 = tuple1 + tuple2
print(tuple3)  # Output: (1, 2, 3, 4, 5, 6)
```

This will create a new tuple that contains the elements of `tuple1` followed by the elements of `tuple2`. Unpacking gives the same result and generalises to any number of inputs, including other iterables:

```python
tuple3 = (*tuple1, *tuple2)        # (1, 2, 3, 4, 5, 6)
```

Keep in mind that tuples are **immutable**, which means that you cannot modify an existing `tuple`. Even `tuple1 += tuple2` does not mutate anything — it builds a brand-new tuple and rebinds the name, an O(n) copy each time. For that reason, concatenating many tuples in a loop is quadratic; collect into a `list` (or use `itertools.chain`) and convert once at the end instead.

## 62- How to join two `sets`?

To join two sets in Python, you can use the `union` method, which returns a new `set` that contains all the elements from both sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set3 = set1.union(set2)
print(set3)  # Output: {1, 2, 3, 4, 5}
```

If you want to modify an existing set in place, you can use the `update` method. This method adds all the elements from one set to another set, without creating a new set:

```python
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

```python
list1 = [1, 2, 3]
list1.append(4)
print(list1)  # prints [1, 2, 3, 4]

list2 = [5, 6, 7]
list1.extend(list2)
print(list1)  # prints [1, 2, 3, 4, 5, 6, 7]
```

Neither method creates a new list — both mutate the existing list in place and return `None`. The real performance distinction is simply how much work there is to do: `append` is amortised O(1) because it adds exactly one element, while `extend(iterable)` is O(k) for k elements added — and calling `extend` once is faster than calling `append` k times in a loop, since it avoids k method-call round-trips.

The gotcha interviewers fish for is what happens when you pass a _list_ to `append`:

```python
lst = [1, 2, 3]
lst.append([4, 5])
print(lst)  # [1, 2, 3, [4, 5]]  <- the list goes in as ONE nested element

lst = [1, 2, 3]
lst.extend([4, 5])
print(lst)  # [1, 2, 3, 4, 5]    <- the elements are added individually
```

Also note that `extend` accepts any iterable — a tuple, set, generator, or string. That last one is a classic accident: `lst.extend("ab")` adds `'a'` and `'b'` as two separate elements. `lst += iterable` is equivalent to `extend` (in-place), whereas `lst + other` builds a new list and requires both operands to be lists.

## 64- How to implement bubble sort in Python?

```python
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

```python
sorted_list = bubble_sort([5, 2, 8, 1, 9])
print(sorted_list)  # [1, 2, 5, 8, 9]
```

**_Time Complexity:_**

- Best case: **O(n)** — the `swap` flag makes one clean pass over already-sorted input enough to stop
- Average case: **O(n<sup>2</sup>)**
- Worst case: **O(n<sup>2</sup>)**

Bubble sort is a teaching algorithm; its one redeeming property is the O(n) early exit on nearly-sorted data. In real code, `sorted()` / `list.sort()` use Timsort — a hybrid stable sort that is O(n log n) worst case and also exploits existing order for O(n) best case.

## 65- How to implement Heap sort in Python?

```python
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

```python
sorted_list = heap_sort([5, 2, 8, 1, 9])
print(sorted_list)  # [1, 2, 5, 8, 9]
```

Without the final `reverse()`, a max-heap pops its largest element first, so the extracted order is descending — `[9, 8, 5, 2, 1]`. (The textbook in-place variant avoids the second list entirely: swap the root with the last element, shrink the heap boundary, and sift down — the array ends up ascending with O(1) extra space.)

In practice, use the standard library's `heapq`, which implements a **min**-heap, so popping yields ascending order directly:

```python
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

```python
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

```python
sorted_list = insertion_sort([5, 2, 8, 1, 9])
print(sorted_list)  # [1, 2, 5, 8, 9]
```

**_Time Complexity:_**

- Best case: **O(n)**
- Average case: **O(n<sup>2</sup>)**
- Worst case: **O(n<sup>2</sup>)**

## 67- How to implement Merge sort in Python?

```python
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

```python
sorted_list = merge_sort([5, 2, 8, 1, 9])
print(sorted_list)  # [1, 2, 5, 8, 9]
```

**_Time Complexity:_**

- Best case: **O(n log(n))**
- Average case: **O(n log(n))**
- Worst case: **O(n log(n))**

Merge sort is **stable** (equal elements keep their original relative order — guaranteed by the `<=` in `merge`) at the cost of O(n) auxiliary space. Python's built-in Timsort is a heavily optimised merge-sort/insertion-sort hybrid, which is why stability is guaranteed for `sorted()` and `list.sort()`.

## 68- How to implement Quick Sort in Python?

```python
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

```python
sorted_list = quick_sort([5, 2, 8, 1, 9])
print(sorted_list)  # [1, 2, 5, 8, 9]
```

**_Time Complexity:_**

- Best case: **O(n log(n))**
- Average case: **O(n log(n))**
- Worst case: **O(n<sup>2</sup>)**

Two things to say about this elegant version: it is **not in place** (each level builds new lists, so O(n) extra space per level), and choosing the **first element as pivot** makes already-sorted input the worst case — every partition is maximally lopsided, degrading to O(n²) and deep recursion. Picking a random pivot (or median-of-three) makes that pathological case vanishingly unlikely; the in-place Lomuto/Hoare partition schemes are the standard follow-up whiteboard exercise.

## 69- How to implement Selection sort in Python?

```python
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

```python
sorted_list = selection_sort([5, 2, 8, 1, 9])
print(sorted_list)  # [1, 2, 5, 8, 9]
```

**_Time Complexity:_**

- Best case: **O(n<sup>2</sup>)**
- Average case: **O(n<sup>2</sup>)**
- Worst case: **O(n<sup>2</sup>)**

## 70- How to implement Shell sort in Python?

```python
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

```python
sorted_list = shell_sort([3, 4, 2, 1, 6, 5])
print(sorted_list)  # [1, 2, 3, 4, 5, 6]
```

**_Time Complexity:_** (for the gap sequence used here — halving the gap each round, Shell's original sequence)

- Best case: **O(n log n)** — already-sorted input
- Average case: depends on the gap sequence; roughly **O(n<sup>3/2</sup>)** for this one
- Worst case: **O(n<sup>2</sup>)**

The shell sort is insertion sort performed over progressively smaller gaps, so far-apart elements move long distances early. Its complexity is governed entirely by the gap sequence — better sequences (Knuth's `3k+1`, Ciura's empirical sequence) improve the worst case to below O(n²) — and no gap sequence makes it beat O(n log n) sorts asymptotically. It is unstable, in place, and mostly of historical/embedded interest.

## 71- What are the commands that are used to copy an object in Python?

There are several ways to copy an object in Python. Here are some of the most common methods:

- Using the `copy` module:

  ```python
  import copy
  new_object = copy.copy(old_object)
  ```

  This creates a shallow copy of the object. If the object contains references to other objects, the copy will contain references to the same objects as the original.

- Using the `deepcopy` function:

  ```python
  import copy
  new_object = copy.deepcopy(old_object)
  ```

  This creates a deep copy of the object. If the object contains references to other objects, the copy will contain copies of those objects as well, rather than references to the same objects.

- Using the `copy()` method:

  ```python
  new_object = old_object.copy()
  ```

  This creates a shallow copy of the object. This method is available for objects that support the `copy` protocol (e.g., lists, dictionaries, sets, etc.).

A few equivalent idioms you will meet in real code: `lst[:]` and `list(lst)` shallow-copy a list, `dict(d)` and `d | {}` shallow-copy a dict, and since Python 3.3 sequences also expose `.copy()` directly. All of these are shallow — for anything nested, only `copy.deepcopy` duplicates the inner objects. Custom classes can hook into the mechanism by defining `__copy__` and `__deepcopy__`.

## 72- What is the difference between deep and shallow copy?

Both produce a new outer object; the difference is what happens to the objects **inside** it.

- A **shallow copy** creates a new container whose slots hold references to the _same_ inner objects as the original. Only the top level is duplicated.
- A **deep copy** recursively duplicates everything reachable, so the copy shares no mutable state with the original.

The distinction only matters when the container holds **mutable** objects. Watch what happens to a nested list:

```python
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

```python
result = expression1 if condition else expression2
```

Here, `expression1` and `expression2` are the results that are returned if the condition is true or false, respectively.

Here's an example of how you can use the ternary operator to assign a value to a variable based on a condition:

```python
x = 10
y = 20
max_value = x if x > y else y
print(max_value)
```

In this example, the condition `x > y` is false, so `y` is assigned to `max_value`. The output of this code will be **`20`**.

You can also use the ternary operator to return a value from a function based on a condition:

```python
def get_max_value(x, y):
    return x if x > y else y

max_value = get_max_value(10, 20)
print(max_value)
```

In this example, the function `get_max_value()` returns `x` if `x` is greater than `y`, and returns `y` if `x` is not greater than `y`. When called with the arguments `(10, 20)`, the function will return `20`.

## 74- What will be the output of the code below?

```python
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

```python
list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']
```

- In the first call to `extendList()`, the default value of the list is used, which is an empty list `[]`. The value `10` is appended to this list, and the modified list is returned. This list is assigned to `list1`.

- In the second call to `extendList()`, a new list `[123]` is passed as the value for the list parameter, so the default value is not used. The value `123` is appended to this list, and the modified list is returned and assigned to `list2`.

- In the third call to `extendList()`, the default value of the list is used again. This time, the default value is the list that was modified in the first call to the function, which contains the value `10`. The value `'a'` is appended to this list, and the modified list is returned and assigned to `list3`.
  This behavior occurs because default values are evaluated when the function is defined, not when it is called. In this case, the default value of the list parameter is an empty list `[]`, which is evaluated when the `extendList()` function is defined. This means that the same `list` object is used as the default value for the `list` parameter every time the `extendList()` function is called, unless a different value is provided for the list parameter in the function call.

The definition of the `extendList` function could be modified as follows, though, to always begin a new list when no `list` argument is specified, which is more likely to have been the desired behavior:

```python
def extendList(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list
```

The `list=None` / `if list is None` pattern is the standard idiom for mutable defaults. (Separately, naming a parameter `list` shadows the built-in `list` type inside the function — harmless here, but poor practice; `items` or `lst` would be better.)

## 75- What will be the output of the code below?

```python
def multipliers():
  return [lambda x : i * x for i in range(4)]

print([m(2) for m in multipliers()])
```

The output of the above code will be `[6, 6, 6, 6]`.

The reason for this is that Python’s closures are late binding. This means that the values of variables used in closures are looked up at the time the inner function is called. So as a result, when any of the functions returned by `multipliers()` are called, the value of `i` is looked up in the surrounding scope at that time. By then, regardless of which of the returned functions is called, the `for` loop has been completed, and `i` is left with its final value of 3. Therefore, every returned function multiplies the value it is passed by `3`, so since a value of `2` is passed in the above code, they all return a value of `6` (i.e., 3 x 2).

The standard fix exploits the fact that **default arguments are evaluated at definition time** (the very behaviour that causes the previous question's bug is the cure here) — bind the current `i` as a default:

```python
def multipliers():
    return [lambda x, i=i: i * x for i in range(4)]

print([m(2) for m in multipliers()])   # [0, 2, 4, 6]
```

Alternatives that achieve the same early binding: `functools.partial(operator.mul, i)`, or a factory function whose parameter captures each value in its own scope.

## 76- What will be the output of the code below?

```python
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

```python
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

```python
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

  ```python
  def greet(name):
      print(f"Hello, {name}!")

  greet("Alice")  # prints "Hello, Alice!"
  ```

- Methods:

  ```python
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

  ```python
  class CallableClass:
      def __call__(self, *args, **kwargs):
          print("Called with arguments:", args, kwargs)

  cc = CallableClass()
  cc(1, 2, 3, a=4, b=5)  # prints "Called with arguments: (1, 2, 3) {'a': 4, 'b': 5}"
  ```

You can check if an object is callable using the `callable()` built-in function:

```python
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

```python
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

```python
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

```python
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

```python
grid = [[] for _ in range(5)]
grid[0].append(10)
print(grid)   # [[10], [], [], [], []]
```

The rule of thumb: `[x] * n` is fine when `x` is immutable (numbers, strings), and a latent bug when `x` is mutable. (The snippet also shadows the built-in `list` type by using it as a variable name — after line 1, `list()` no longer constructs lists in that scope. Avoid that in real code.)

## 83- Write a function that prints the least integer that is not present in a given list and cannot be represented by the summation of the sub-elements of the list

This is the classic "smallest unrepresentable sum" problem: given a list of positive integers, find the smallest positive integer that cannot be written as the sum of any subset of the list. There is a beautiful greedy O(n log n) solution:

```python
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

```python
print(find_least_integer([1, 3, 6, 10, 11, 15]))  # Output: 2  (no way to form 2)
print(find_least_integer([1, 1, 3]))              # Output: 6
print(find_least_integer([1, 2, 4, 8]))           # Output: 16 (powers of two cover 1-15)
```

## 84- How do you reverse a list? Can you come up with at least three ways?

Here are three ways to reverse a list in Python:

1. Using the `reverse()` method:

   ```python
   lst = [1, 2, 3, 4, 5]
   lst.reverse()
   print(lst)  # Output: [5, 4, 3, 2, 1]
   ```

2. Using slicing with a step of -1:

   ```python
   lst = [1, 2, 3, 4, 5]
   lst = lst[::-1]
   print(lst)  # Output: [5, 4, 3, 2, 1]
   ```

3. Using a `for` loop:

   ```python
   lst = [1, 2, 3, 4, 5]
   reversed_lst = []
   for i in range(len(lst)-1, -1, -1):
       reversed_lst.append(lst[i])
   print(reversed_lst)  # Output: [5, 4, 3, 2, 1]
   ```

All three produce the same _ordering_, but they differ in an important way: `reverse()` mutates the original list **in place and returns `None`** (so `lst = lst.reverse()` is a classic bug that leaves you with `None`), while slicing and the loop build a _new_ list and leave the original untouched.

A fourth way — often the best — is the built-in `reversed()`:

```python
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

```python
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

```python
class TestDivide(unittest.TestCase):
    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0
```

Worth saying in an interview: `unittest` is the standard library's xUnit-style framework, but much of the Python world uses **pytest**, which runs `unittest` suites unchanged while offering plain-`assert` tests, fixtures, and parametrisation with far less boilerplate.

## 88- What is the difference between xrange and range?

`range` and `xrange` are both functions that are used to generate a sequence of numbers. However, they differ in how they generate the numbers and in the type of object they return.

The `range` function generates a sequence of numbers by creating a list object that contains all of the numbers in the sequence. For example:

```python
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

```python
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

```python
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

```python
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

```python
>>> -7 // 2
-4          # floor(-3.5) = -4, NOT -3
>>> 7 // -2
-4
>>> int(-7 / 2)
-3          # int() truncates toward zero - a different operation
```

Floor division pairs with the modulo operator through the invariant `a == (a // b) * b + (a % b)`, which is why `%` in Python always returns a result with the sign of the _divisor_ (`-7 % 2` is `1`, handy for wrapping indices). `divmod(a, b)` returns both at once. Typical uses: splitting into whole units and remainder (`minutes, seconds = divmod(total, 60)`), integer midpoints (`mid = (lo + hi) // 2`), and digit extraction (`n // 10`, `n % 10`).

```python
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

```python
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

```python
D.__mro__ == (D, B, C, A, object)
```

This means that when looking up a method on an instance of the `D` class, the interpreter will first search the `D` class, then the `B` class, then the `C` class, then the `A` class, and finally the object class, which is the base class of all classes in Python.

The MRO is an important concept in Python because it determines the order in which methods are inherited and how conflicts are resolved when a class has multiple inheritance. Understanding how the MRO works is essential to understanding how multiple inheritance works in Python.

Three follow-ups an interviewer is likely to reach for:

- **C3 is more than left-to-right.** The linearization satisfies two constraints at once: a class always precedes its own bases, and the left-to-right order of the bases listed in every class definition is preserved. In diamond hierarchies this means a shared base appears _after_ all its subclasses, not immediately after the first parent (see the `super` question earlier in this file for a worked diamond).
- **Not every hierarchy has a valid MRO.** If the constraints contradict each other, Python refuses to create the class at all:

  ```python
  class X(A, B): pass
  class Y(B, A): pass       # opposite order
  class Z(X, Y): pass       # TypeError: Cannot create a consistent MRO
  ```

- **`super()` is MRO traversal.** `super()` does not mean "my parent" — it means "the next class after mine in the MRO of the instance's actual type". That is what allows cooperative multiple inheritance and mixins to compose: each class calls `super()`, and the MRO threads one call through every class exactly once. Inspect it any time with `D.__mro__` or `D.mro()`.

## 92- How to distribute Python code?

There are several ways to distribute Python code, depending on the specific needs of your project. Here are a few common options:

1. **Packaging for PyPI (the modern workflow)**: Declare the package metadata in a `pyproject.toml` file — this has replaced the old `setup.py`/`distutils` approach (`distutils` was removed from the standard library in Python 3.12). Then build and upload:

   ```bash
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

```bash
pip install A
```

This will install both packages `A` and its transitive dependency, package `B`.

If you want to specify the exact version of a package and its transitive dependencies that you want to install, you can use the `-r` flag to specify a requirements file. A `requirements` file is a text file that lists the packages and their versions that your project depends on. For example:

```python
A==1.0
B==2.0
```

To install the packages and their transitive dependencies from this requirements file, you can use the following command:

```bash
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

```python
def Foo():
    yield 42;
    return 666
```

Strictly speaking this code produces **no output** — it only defines a function. The interesting question is what happens when you use it.

`Foo` is a generator function, as indicated by the `yield` keyword. Calling it returns a generator object without executing the body. Iterating runs the body up to `yield`, producing `42` and suspending; resuming continues to the `return` statement.

Here is the part worth knowing: `return 666` inside a generator does **not** produce `666` as an iteration value. It terminates the generator by raising `StopIteration`, and the returned value is carried on the exception as its `.value` attribute (PEP 380):

```python
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

```python
_MangledGlobal__mangled = 23

class MangledGlobal:
    def test(self):
        return __mangled
```

The `MangledGlobal` class contains a reference to a global variable with a name that has been "`mangled`" to avoid name conflicts with other variables in the global namespace.

In Python, the name `mangling` is a technique that is used to protect instance variables in a class from being accidentally overwritten by derived classes. Name `mangling` works by adding a double underscore prefix to the name of an instance variable, which causes the interpreter to automatically rename the variable in a way that is unique to the class.

The detail this puzzle turns on: mangling is applied **at compile time to any identifier of the form `__name` appearing anywhere in a class body** — not just to attribute access through `self`. So the bare reference `__mangled` inside `test()` is textually rewritten to `_MangledGlobal__mangled` before the code ever runs. At call time, ordinary name lookup then proceeds (local → global): there is no local by that name, but the _global_ `_MangledGlobal__mangled = 23` matches the rewritten name, so `test()` returns `23`.

Here is the example in action:

```python
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

```python
my_tuple = (1, "hello", True)
```

Unpacking, on the other hand, refers to the process of taking a data structure and splitting it into multiple values or items. This is often done using tuples, lists, or dictionaries. For example, we can unpack a tuple into multiple variables like this:

```python
my_tuple = (1, "hello", True)
a, b, c = my_tuple
```

Also, the asterisk (\*) symbol can be used in unpacking expressions to represent a variable number of elements. This is sometimes referred to as "extended unpacking".

The asterisk can be used in several ways:

1. Unpacking into individual variables: If you have a list or tuple with an unknown number of elements, you can use the asterisk to unpack the elements into individual variables. For example:

   ```python
   my_list = [1, 2, 3, 4, 5]
   a, b, *rest = my_list
   print(a) # 1
   print(b) # 2
   print(rest) # [3, 4, 5]
   ```

2. Unpacking in function calls: The asterisk can also be used to unpack arguments in function calls. For example:

   ```python
   def my_function(a, b, c):
       print(a, b, c)

   my_list = [1, 2, 3]
   my_function(*my_list)
   ```

In this example, the elements of `my_list` are unpacked and passed as arguments to the function `my_function`.

The picture is completed by the double asterisk and the packing side of function signatures:

1. **Packing in function signatures**: `*args` packs surplus positional arguments into a tuple and `**kwargs` packs surplus keyword arguments into a dict — packing and unpacking are the same syntax viewed from opposite ends:

   ```python
   def report(*args, **kwargs):
       print(args, kwargs)

   report(1, 2, flag=True)   # (1, 2) {'flag': True}
   ```

2. **`**` unpacking in calls and literals**: a dict can be unpacked into keyword arguments, and both `*` and `**` work inside literals to merge collections:

   ```python
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

```python
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

## 98- What is the `__init__.py` module, and what is it for?

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

```python
import my_package.module1
```

When this `import` statement is executed, Python will execute the code in `my_package/__init__.py` before it loads `module1`.

The `__init__.py` file can be an empty file, and typical non-empty uses are: re-exporting the package's public API so users can write `from my_package import Thing` instead of digging into submodules, defining `__all__`, and setting package-level metadata.

The modern nuance: since Python 3.3 (PEP 420), a directory **without** `__init__.py` still imports — it becomes an implicit _namespace package_, whose parts can even be spread across multiple `sys.path` locations. So "it must be present" is no longer strictly true. In practice you should still add `__init__.py` to every ordinary package: it makes the package explicit, imports marginally faster, plays better with some tools, and prevents two unrelated directories from silently merging into one package — reserving namespace packages for the rare plugin-style layouts that genuinely need them.

## 99- How do I view object methods?

To view the methods of an object in Python, you can use the `dir()` function. This function returns a `list` of all the attributes and methods of an object, including special attributes like `__dict__` and `__doc__`.

For example, consider the following object:

```python
class MyClass:
    def __init__(self):
        self.x = 10

    def my_method(self):
        pass
```

To view the methods of this object, you could do the following:

```python
obj = MyClass()
methods = dir(obj)
print(methods)
```

This would output the following list:

```bash
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_method', 'x']
```

You can then filter this list to only include methods by using a list comprehension — note that filtering on `callable` alone is not enough, because the dunder methods (`__init__`, `__eq__`, …) are callable too and would flood the result:

```python
obj_methods = [m for m in dir(obj)
               if callable(getattr(obj, m)) and not m.startswith("__")]
print(obj_methods)
```

This would output the following list:

```python
['my_method']
```

Other tools for the same job: `help(obj)` renders methods with their signatures and docstrings; `inspect.getmembers(obj, inspect.ismethod)` returns `(name, method)` pairs and is the robust programmatic option (`inspect.isfunction` for the unbound functions on the class itself); and `vars(type(obj))` shows what the class defines directly, excluding what it merely inherits. One caution: `dir()` calls are a _convention_, not a guarantee — a class can override `__dir__`, and dynamic attributes served by `__getattr__` will not appear.

## 100- Which is a better practice - global import or local import in Python

The convention — codified in PEP 8 — is the opposite of what this question often tempts people to say: **imports belong at the top of the module** (global imports). Top-level imports make a module's dependencies visible at a glance, fail fast at import time rather than deep inside a call at 3 a.m., and cost nothing on reuse — Python caches every imported module in `sys.modules`, so repeated imports are just a dictionary hit, and a function-local import actually _adds_ a small lookup cost on every call.

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

```python
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

```python
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

```python
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

```python
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

```python
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

```python
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

```python
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

```python
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

```python
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

```python
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

## 114- What is the difference between `__new__` and `__init__`? And how does object construction work?

They are two distinct steps of a two-phase construction protocol, and conflating them is a common source of confusion.

- **`__new__(cls, ...)` is the actual constructor**: a static method that **allocates and returns** the new instance. It runs _first_, and its job is to produce the object.
- **`__init__(self, ...)` is the initialiser**: it receives the _already-created_ instance as `self`, configures its attributes, and **returns `None`**. It never creates anything.

When you call `MyClass(args)`, it is the metaclass's `type.__call__` that orchestrates the sequence: it calls `__new__` to get the instance, and then — **only if `__new__` returned an instance of `cls`** — calls `__init__` on it.

```python
class Demo:
    def __new__(cls, *args, **kwargs):
        print("1. __new__ - creating the instance")
        instance = super().__new__(cls)     # object.__new__ does the allocation
        return instance

    def __init__(self, value):
        print("2. __init__ - initialising the instance")
        self.value = value

d = Demo(42)
# 1. __new__ - creating the instance
# 2. __init__ - initialising the instance
```

The subtle rule to state explicitly: **if `__new__` returns an object that is not an instance of `cls`, `__init__` is skipped entirely.** This is the mechanism behind returning a cached or different object.

You rarely override `__new__` — `__init__` covers almost every case. The legitimate reasons to reach for it:

- **Subclassing an immutable type** (`int`, `str`, `tuple`, `bytes`, `frozenset`). Because the value is fixed at creation, there is no way for `__init__` to set it — it runs too late. You must intercept `__new__`:

  ```python
  class PositiveInt(int):
      def __new__(cls, value):
          if value <= 0:
              raise ValueError("must be positive")
          return super().__new__(cls, value)   # value must be baked in here

  print(PositiveInt(5) + 10)   # 15  - behaves as an int
  ```

- **Singletons / instance caching / object pools** — return an existing instance instead of a fresh one (note the caveat that `__init__` still re-runs on the returned instance if it _is_ a `cls` instance, so guard against re-initialising):

  ```python
  class Singleton:
      _instance = None
      def __new__(cls):
          if cls._instance is None:
              cls._instance = super().__new__(cls)
          return cls._instance

  print(Singleton() is Singleton())   # True
  ```

- **Metaclasses** (`type.__new__` customises class creation), and factory patterns that return a subclass chosen at runtime.

Two footnotes worth mentioning: `dataclasses`, `NamedTuple`, and most everyday classes never touch `__new__`; and `__new__` is implicitly a static method even though you don't decorate it, which is why it takes `cls` explicitly rather than receiving it like a classmethod.

## 115- How is memory allocated for `list`, `tuple`, and `set`?

The unifying idea first: **all three store _references_ (pointers) to objects, never the objects inline.** `sys.getsizeof(container)` therefore measures the container's own bookkeeping and pointer array, not the elements it points at — a list of a million ints and a list of a million huge strings have the _same_ `getsizeof`.

**`list` — a dynamic array with a separately-allocated buffer.** A `PyListObject` is a small fixed header holding: a pointer to a heap-allocated **array of `PyObject*`**, `ob_size` (the number of elements in use), and `allocated` (the array's current capacity). Because the buffer is separate and resizable, a list can grow and shrink; it **over-allocates** spare capacity so appends are amortised O(1) (see the next question). Indexing is O(1) pointer arithmetic; inserting/deleting at the front is O(n) because everything shifts.

**`tuple` — a fixed array stored inline.** A `PyTupleObject` stores its pointer array **in the same single allocation** as the header (a variable-length object), with no separate buffer and, crucially, **no `allocated` slack** — an immutable tuple is sized exactly once at creation and never grows. That makes a tuple **smaller and slightly faster to build and access** than an equivalent list. CPython goes further: it keeps **free lists** of small tuples for fast reuse, and tuples of constants are cached/interned in compiled code.

```python
import sys
print(sys.getsizeof([1, 2, 3]))    # e.g. 88  - header + pointer buffer + slack
print(sys.getsizeof((1, 2, 3)))    # e.g. 64  - header + inline pointers, no slack
```

**`set` — a hash table without values.** A `set` is essentially a `dict` that stores only keys: an open-addressing hash table of slots, each holding a reference and the element's cached hash. It resizes when it passes a load-factor threshold (roughly 3/5 full), trading memory for O(1) membership. Consequences: elements must be **hashable**, there is **no order** guarantee, and a set uses **more** memory than a list of the same elements because most slots sit empty to keep collisions rare. That empty space is exactly what buys O(1) `in` versus a list's O(n).

The practical takeaway for a senior engineer: reach for a **tuple** for fixed, immutable records (smaller, hashable, usable as dict keys), a **list** when you need to grow/mutate an ordered sequence, and a **set** the moment you do repeated membership tests or need de-duplication. For large homogeneous numeric data, none of these are ideal — `array.array` (inline C values, no per-element object) or NumPy (contiguous typed buffer) avoid the per-element pointer-and-object overhead entirely.

## 116- When a list grows beyond its allocated capacity, what happens to the underlying array allocation? And how are the existing elements handled?

This is the mechanism that makes `list.append` **amortised O(1)**, and it is worth being precise about.

A list keeps two numbers: `ob_size` (elements currently used) and `allocated` (slots the backing buffer can hold). As long as `ob_size < allocated`, an append just writes into the next free slot — genuinely O(1). The interesting case is when `ob_size == allocated` and you append again:

1. CPython computes a **new, larger capacity** — it does _not_ grow by one. The growth formula (`list_resize` in CPython) is roughly:

   ```python
   new_allocated = new_size + (new_size >> 3) + 6   # then rounded
   ```

   i.e. about **12.5% headroom** on top of what's needed, plus a small constant, with the result rounded to a multiple of 4. The resulting capacity progression is 0, 4, 8, 16, 24, 32, 40, 52, 64, 76, 92, 108, … — geometric-ish growth, not linear.

2. It calls **`realloc`** on the pointer buffer to that new capacity. Two things can happen under the hood: the allocator may **extend the block in place** (no copy needed), or, if the adjacent memory is taken, it **allocates a fresh, larger block, copies the existing pointers over, and frees the old block.**

3. **What gets copied is only the array of pointers — never the elements themselves.** The objects the list points to are untouched: same objects, same memory, same `id()`. So a resize is a shallow O(n) copy of _N machine-word pointers_, which is cheap and does not deep-copy or re-create any element.

```python
import sys
lst = []
prev = None
for i in range(20):
    cap = sys.getsizeof(lst)
    if cap != prev:
        print(f"len={len(lst):2d}  getsizeof={cap}")   # buffer grows: cap 0,4,8,16,24...
        prev = cap
    lst.append(i)
```

**Why this gives amortised O(1):** because capacity grows geometrically, the total cost of the occasional O(n) copies across `n` appends sums to O(n), so the _average_ cost per append is O(1). Any single append that triggers a resize is O(n), but those are rare and get rarer as the list grows — the classic amortised-analysis result.

Senior-level corollaries:

- **Identity is preserved for elements, not for the buffer.** After a resize, `lst[0] is original_first_element` is still `True`, but the internal buffer address changed — which is why holding a raw pointer into a list from a C extension across an append is a bug.
- **Pre-size when you know the length.** Building `[None] * n` and assigning by index, or using a list comprehension, avoids repeated regrowth. `list.extend(iterable)` also grows once (using the iterable's length hint) rather than reallocating per element.
- **Lists also shrink**: deletions that drop usage well below capacity trigger a realloc to a smaller buffer, so a list that was huge and is now small releases most of its buffer.
- **This is why front operations are the wrong tool.** `insert(0, x)` and `pop(0)` are O(n) regardless of capacity because they shift every pointer. For a queue, use `collections.deque`, which is a linked list of fixed-size blocks with O(1) appends/pops at both ends and never does this whole-array copy.

## 117- What hashing is used for `dict` keys, and how do `__hash__` and `__eq__` interact?

A `dict` (and `set`) is a **hash table**, so every key must be **hashable**: it must implement `__hash__()` returning an int, and `__eq__()` for comparison. The two are a contract, not independent methods.

**How a lookup actually works.** For `d[key]`, CPython:

1. Computes `hash(key)` and uses the low bits to pick a slot in the table.
2. If the slot is occupied, it compares the stored key to `key` — first with an `is` **identity** short-circuit (fast path: the same object is trivially equal), then with `==`. This comparison is what resolves **collisions**: two different keys can land in the same slot, and `__eq__` decides whether you found your key or a colliding neighbour.
3. On a collision-and-mismatch, it **probes** further slots (CPython perturbs the probe sequence with more hash bits, an open-addressing scheme) until it finds the key or an empty slot.

So both methods are used on every lookup: `__hash__` to _locate_ the bucket, `__eq__` to _confirm_ the match.

**The invariant you must not break:**

> If `a == b`, then `hash(a) == hash(b)`.

The converse is _not_ required — unequal objects may share a hash (that's just a collision, handled by probing). But if two "equal" objects hash differently, one becomes invisible: it gets stored in one bucket and searched for in another, so `d[a] = 1; d[b]` raises `KeyError` even though `a == b`.

**The consequence for custom classes.** If you override `__eq__`, Python **sets `__hash__` to `None`**, making instances unhashable — a deliberate safeguard, because a custom equality almost always needs a matching hash. You must define both together, typically over the same fields:

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, other):
        return isinstance(other, Point) and (self.x, self.y) == (other.x, other.y)
    def __hash__(self):
        return hash((self.x, self.y))     # hash the same fields eq compares

pts = {Point(1, 2): "a"}
print(pts[Point(1, 2)])   # 'a' - a different object, equal value, found correctly
```

`@dataclass(frozen=True)` and `typing.NamedTuple` generate this consistent pair for you, which is the idiomatic way to make a value object usable as a key.

**Why mutable objects are unhashable.** `list`, `dict`, and `set` deliberately have no `__hash__`. If a key could mutate after insertion, its hash would change and it could never be found again — so Python forbids them as keys. The immutable counterparts (`tuple` of hashables, `frozenset`) _are_ hashable, which is exactly how you build **composite keys**.

**Two facts a senior is expected to know:**

- **String and bytes hashing is randomised per process** (SipHash, since Python 3.3, controlled by `PYTHONHASHSEED`). This defends against algorithmic-complexity (hash-flooding) DoS attacks, where an attacker sends keys engineered to collide and degrade a dict to O(n). It also means `hash("x")` differs between runs — never persist or depend on raw hash values across processes. (Dict _insertion order_ is still preserved regardless; that's unrelated to hashing.)
- **Average lookup is O(1); worst case is O(n)** if hashing degenerates and everything collides. Small integers hash to themselves (`hash(5) == 5`), and `hash(-1)` is special-cased to `-2` because `-1` signals an error in the C API.

## 118- What is `asyncio`, and how do `async`/`await` and the event loop actually work?

`asyncio` is Python's framework for **single-threaded concurrency via cooperative multitasking**. The whole model turns on one distinction: it gives you concurrency _without_ threads by letting one thread juggle thousands of tasks, switching between them only at explicit `await` points.

- An **`async def`** function is a **coroutine function**; calling it does _not_ run it — it returns a **coroutine object**, much as calling a generator function returns a generator. Nothing executes until the coroutine is driven by an event loop.
- **`await`** suspends the current coroutine until the awaited awaitable completes, and — this is the key part — **hands control back to the event loop** so it can run other ready tasks meanwhile. `await` is a cooperative yield point, not a blocking wait.
- The **event loop** is the scheduler: a single-threaded loop that keeps a queue of ready tasks, runs each until it hits an `await` that isn't ready, parks it, and (typically via an OS `select`/`epoll`/`kqueue` call) waits for I/O readiness before resuming whichever task's I/O completed.

```python
import asyncio

async def fetch(name, delay):
    print(f"{name} start")
    await asyncio.sleep(delay)     # yields to the loop; does NOT block the thread
    print(f"{name} done")
    return name

async def main():
    # gather runs them concurrently on ONE thread
    results = await asyncio.gather(fetch("A", 2), fetch("B", 1), fetch("C", 3))
    print(results)

asyncio.run(main())   # ~3s total, not 6 - the sleeps overlap
```

The three `sleep`s overlap because each `await asyncio.sleep` yields control, so the loop starts the next task instead of waiting. Total time is the _longest_ task, not the sum — that's the payoff.

**The non-negotiable rule:** the event loop runs on one thread, so **a blocking call blocks everything.** A plain `time.sleep(2)`, a synchronous `requests.get`, or a CPU-heavy loop inside a coroutine freezes _all_ tasks, because nothing yields back to the loop. You must use async-aware equivalents (`asyncio.sleep`, `aiohttp`/`httpx`, async database drivers), or offload blocking work with `await asyncio.to_thread(func)` (thread pool) or a process pool for CPU-bound work.

Where it fits:

- **Ideal for high-concurrency I/O-bound workloads** — thousands of simultaneous network connections, API calls, or socket clients — where threads would waste memory (each thread has a full stack) and the GIL makes their parallelism moot anyway. One event-loop thread handling 10,000 sockets is the canonical win.
- **Useless for CPU-bound work.** Coroutines don't sidestep the GIL and there's only one thread; heavy computation needs `multiprocessing`.
- **`await` composes; `create_task` fans out.** `await coro` runs sequentially; `asyncio.create_task(coro)` schedules it to run concurrently and returns a `Task` you can await later; `asyncio.gather`/`asyncio.TaskGroup` (3.11+) run many concurrently and collect results.

Mental model to close on: `asyncio` is **not parallelism** — it's one worker interleaving many jobs by never sitting idle during I/O. It trades the OS scheduler's preemptive thread switching for explicit, cheap, cooperative switching at `await`, which is why it scales to far more concurrent I/O operations than threads while sidestepping the data races that preemptive threading invites.

## 119- Threading, multiprocessing, or asyncio — how do you choose a concurrency model?

The decision reduces to one question first — **is the work I/O-bound or CPU-bound?** — and the GIL is the reason the answer matters.

| Model | Parallelism | Best for | Cost |
| --- | --- | --- | --- |
| **`threading`** | No (GIL serialises bytecode) | I/O-bound, moderate concurrency, blocking libraries | preemptive → needs locks; ~MBs per thread stack |
| **`multiprocessing`** | **Yes** (separate interpreters) | **CPU-bound** work | Process overhead; data must be pickled/IPC'd |
| **`asyncio`** | No (one thread) | I/O-bound, **very high** concurrency | Needs async-native libraries; one blocking call stalls all |

**CPU-bound work → `multiprocessing` (or a native extension).** Number crunching, image processing, and parsing gain nothing from threads because the GIL lets only one thread run Python bytecode at a time. Separate _processes_ each have their own interpreter and GIL, so they genuinely run in parallel on multiple cores. The price is that they don't share memory — arguments and results are **pickled** and shipped over IPC — so it pays off only when the compute per task dwarfs that transfer cost. (The alternative is to keep threads but do the heavy lifting in a C extension that releases the GIL, which is exactly what NumPy does.)

**I/O-bound work → `threading` or `asyncio`.** While a thread waits on a socket, disk, or subprocess, it releases the GIL, so other threads make progress. Both models overlap I/O effectively; the choice between them is about scale and ecosystem:

- **`threading`** is the pragmatic choice for **moderate** concurrency (tens to low hundreds of tasks) and, decisively, when you must use **blocking libraries** (a synchronous DB driver, `requests`, legacy SDKs). Its downside is preemptive switching, which can interrupt between any two bytecodes, so shared mutable state needs `Lock`/`Queue` and invites race conditions.
- **`asyncio`** wins at **massive** concurrency (thousands of simultaneous connections) because tasks are cheap (no per-thread stack) and switching is explicit at `await`. But it demands an **async-native stack top to bottom** (`aiohttp`/`httpx`, async DB drivers); a single blocking call anywhere stalls the whole event loop.

The high-level interface for the first two is **`concurrent.futures`**, whose `ThreadPoolExecutor` and `ProcessPoolExecutor` share an identical API — so you can write pool code once and switch models by changing one class name:

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# I/O-bound: threads
with ThreadPoolExecutor(max_workers=16) as pool:
    pages = list(pool.map(download, urls))

# CPU-bound: processes - same API, real parallelism
with ProcessPoolExecutor() as pool:
    results = list(pool.map(crunch, big_inputs))
```

A senior would add: these are not mutually exclusive — a real service often combines them (an `asyncio` web layer that offloads CPU work to a `ProcessPoolExecutor` via `loop.run_in_executor`), and the honest first step is always to **measure** whether the bottleneck is I/O wait or CPU before picking a model. And on the horizon, the free-threaded (no-GIL) builds from PEP 703 will eventually let `threading` deliver true CPU parallelism, changing this calculus.

## 120- What is a metaclass, and when would you actually use one?

The one-line definition: **a metaclass is the class of a class.** Just as an object is an instance of a class, a class is an instance of a metaclass. By default every class is an instance of **`type`**, and `type` is the built-in metaclass.

```python
class Foo: pass
print(type(Foo))            # <class 'type'>  - Foo is an instance of type
print(type(Foo()))          # <class 'Foo'>   - Foo() is an instance of Foo
print(isinstance(Foo, type))  # True
```

Because `type` is callable, you can even create classes dynamically without the `class` statement — `type(name, bases, namespace)` is what the `class` block desugars to:

```python
Dog = type("Dog", (), {"sound": "woof", "speak": lambda self: self.sound})
print(Dog().speak())        # 'woof'
```

**How a custom metaclass hooks in.** You subclass `type` and override `__new__` (to alter the class object as it is built) or `__init__` (to configure it afterward), then attach it with `metaclass=`. The metaclass runs **once, at class-definition time**, letting you inspect or rewrite the class body:

```python
class AutoRepr(type):
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if "__repr__" not in namespace:            # inject a default repr
            cls.__repr__ = lambda self: f"{name}({vars(self)})"
        return cls

class Point(metaclass=AutoRepr):
    def __init__(self, x, y):
        self.x, self.y = x, y

print(Point(1, 2))   # Point({'x': 1, 'y': 2})
```

**When you'd actually use one — and when you wouldn't.** Metaclasses solve exactly one problem: **customising class creation itself** (validating or registering classes, injecting methods, enforcing conventions across a whole class hierarchy). The canonical real-world users are frameworks: Django's and SQLAlchemy's ORMs use metaclasses to turn declarative `class Model` bodies into database-mapped objects, ABCs use `ABCMeta`, and enums use `EnumMeta`.

But for application code the honest senior answer is **"almost never — reach for something simpler first"**:

- **`__init_subclass__`** (Python 3.6+) handles most "do something whenever this class is subclassed" needs (auto-registration, validation) without a metaclass at all.
- **`__set_name__`** covers descriptor-naming needs.
- **Class decorators** can rewrite a class after creation and are far easier to read and compose than a metaclass.

The famous Tim Peters line captures the judgement expected of a senior: _"If you wonder whether you need metaclasses, you don't."_ Know what they are and how the `type`/instance chain works — the mechanism underpins ORMs and is a favourite interview probe — but treat writing one in ordinary code as a red flag rather than a flex. One practical gotcha to mention: metaclass conflicts. If two base classes have different (non-subclass-related) metaclasses, Python refuses to create the derived class.

## 121- Do Python's type hints do anything at runtime?

The blunt answer that separates people who've _used_ type hints from people who've only read about them: **by default, no — the interpreter does not enforce them at all.** Annotations are hints for humans and _external_ tools; passing the "wrong" type runs happily until something unrelated breaks.

```python
def add(a: int, b: int) -> int:
    return a + b

print(add("x", "y"))   # 'xy' - no error; the hints are not checked at runtime
```

What type hints actually give you:

- **Static analysis.** Tools like **mypy** and **Pyright** (which powers Pylance in VS Code) read the annotations _before_ the code runs and flag mismatches, catching a whole class of bugs early. This is where the real value is, and why annotating large codebases pays off.
- **Editor tooling.** Autocomplete, inline documentation, and safe refactoring all lean on annotations.
- **Runtime _availability_, if you choose to use it.** The hints _are_ stored — accessible via `__annotations__` or, more robustly, `typing.get_type_hints()` — so libraries can opt in to reading and acting on them. **Pydantic** and **FastAPI** validate and coerce data against annotations at runtime, `dataclasses` uses them to generate `__init__`, and `functools.singledispatch` can dispatch on them. But that enforcement is those libraries' own doing, not the language's.

```python
def greet(name: str) -> str:
    return "hi " + name

print(greet.__annotations__)   # {'name': <class 'str'>, 'return': <class 'str'>}
```

Details a senior is expected to have hit in practice:

- **Annotations can be strings (lazy evaluation).** `from __future__ import annotations` (PEP 563) makes _all_ annotations strings that aren't evaluated at definition time — which fixes forward references (referring to a class not yet defined) and circular-import issues, but means anything reading them at runtime must use `get_type_hints()` to resolve them. This is a genuine friction point with Pydantic and other introspecting libraries.
- **Generics and the typing toolkit:** `list[int]`, `dict[str, int]`, `Optional[X]` (= `X | None`), `Union` / the `X | Y` syntax (3.10+), `TypeVar` and `Generic` for parametric code, `Protocol` for structural typing, `Callable`, `Any`, `Literal`, `TypedDict`, and `cast`. `typing.TYPE_CHECKING` guards imports needed only for hints.
- **`Any` disables checking** for that value — useful as an escape hatch, dangerous as a habit.
- **Hints don't affect performance** meaningfully; they're metadata, not runtime checks.

The senior framing: type hints are **gradual and optional** — you add them where they earn their keep (public APIs, complex data flows, large teams) and a static checker in CI turns them into a real safety net. But never assume the interpreter is validating them; if you need runtime guarantees, that's a job for Pydantic, explicit checks, or `assert isinstance(...)`.

## 122- What is the walrus operator (`:=`) and when is it useful?

The walrus operator `:=` (named for its resemblance to a walrus's eyes and tusks), introduced in Python 3.8 by PEP 572, performs **assignment inside an expression**. Ordinary `=` is a statement and cannot appear where a value is expected; `:=` both assigns to a name _and_ evaluates to that value, so it can live inside an `if`, `while`, comprehension, or function call.

Its value is eliminating the choice between **computing something twice** and **adding an extra line** — the "assign, then test" and "assign, then use" patterns:

```python
# Without walrus: either call len() twice, or add a setup line before the if
if (n := len(data)) > 10:
    print(f"too long: {n} items")   # n is available here, computed once

# The classic loop: read-until-sentinel, with no duplicated read
while (line := file.readline()):
    process(line)

# In a comprehension: compute an expensive value once, filter and use it
results = [y for x in data if (y := expensive(x)) is not None]
```

Where it genuinely shines is **avoiding a redundant expensive call** in a filter-and-use comprehension (the last example — without `:=` you'd call `expensive(x)` twice or fall back to a loop), and **loop conditions that consume input** (reading lines, chunks, or a queue until a sentinel).

The senior perspective is as much about **restraint** as capability:

- Use it when it removes a real duplication or an awkward `while True: ... break`. Don't use it to cram two ideas onto one line where a plain statement reads better — readability wins, and the operator is easy to abuse into dense, clever-looking code.
- It has **deliberate syntactic limits**: you can't use it as a bare top-level statement (`x := 5` is a `SyntaxError`; that's just `x = 5`), and around some constructs it requires parentheses, which nudges you away from misuse.
- Scope note: in a comprehension, the walrus target **leaks into the enclosing scope**, unlike the comprehension's own loop variable — occasionally handy, occasionally a surprise.

## 123- What is in `functools` beyond `lru_cache`?

`functools` is the standard library's toolkit for **higher-order functions** — utilities that act on or return other functions. Beyond `lru_cache`/`cache` (covered separately), the pieces a senior reaches for regularly:

- **`functools.wraps`** — the decorator you apply to a wrapper so it copies the wrapped function's `__name__`, `__doc__`, `__qualname__`, etc. Without it, every decorated function reports itself as `wrapper`, breaking introspection, `help()`, and debuggers. Non-optional in real decorators.

- **`functools.partial`** — freezes some arguments of a callable, returning a new callable with fewer parameters. The clean way to pre-configure a function for an API that wants a zero/one-arg callback:

  ```python
  from functools import partial
  int_base2 = partial(int, base=2)
  print(int_base2("1010"))          # 10
  ```

- **`functools.reduce`** — folds an iterable into a single value by repeatedly applying a binary function (`reduce(operator.mul, nums, 1)` for a product). Powerful but often less readable than a loop or `sum`/`math.prod`; use it when the fold is genuinely the clearest expression.

- **`functools.singledispatch`** — turns a function into one that dispatches on the **type of its first argument**, giving you clean type-based overloading without an `if/elif isinstance` ladder. This is Python's answer to "function overloading" (which the language otherwise lacks):

  ```python
  from functools import singledispatch

  @singledispatch
  def describe(x): return f"generic: {x}"

  @describe.register
  def _(x: list): return f"a list of {len(x)}"

  @describe.register
  def _(x: int): return f"the integer {x}"

  print(describe(5), "|", describe([1, 2]))   # the integer 5 | a list of 2
  ```

  (`singledispatchmethod` does the same for methods.)

- **`functools.cached_property`** — computes a property **once per instance** and caches the result in the instance `__dict__`, so subsequent accesses are free. The right tool for a derived value that's expensive but stable for the object's lifetime — and it avoids the `lru_cache`-on-a-method leak of keeping `self` alive in a global cache.

- **`functools.total_ordering`** — a class decorator: define `__eq__` plus **any one** of `__lt__`/`__le__`/`__gt__`/`__ge__`, and it fills in the rest. Saves writing all six rich-comparison methods.

- **`functools.cmp_to_key`** — adapts an old-style two-argument comparison function into a `key=` function for `sorted`/`min`/`max`, the bridge from Python 2's `cmp` sorting to Python 3's key-based sorting.

The through-line: `functools` is where Python's functional-programming and metaprogramming conveniences live, and `wraps` + `partial` + `singledispatch` + `cached_property` in particular show up constantly in production library and framework code.

## 124- What are `dataclasses`, and how do they compare to `NamedTuple`, `TypedDict`, and `attrs`?

`@dataclass` (Python 3.7+, PEP 557) is a decorator that **generates boilerplate methods from class-level annotated fields** — `__init__`, `__repr__`, and `__eq__` by default, and optionally more. It's the idiomatic modern way to write a class whose purpose is to _hold data_:

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: int
    y: int = 0                       # default value
    tags: list = field(default_factory=list)   # mutable default done safely

p = Point(1, 2)
print(p)                 # Point(x=1, y=2, tags=[])  <- generated __repr__
print(p == Point(1, 2))  # True                       <- generated __eq__
```

The features worth knowing, because they map straight to real needs:

- **`field(default_factory=...)`** is the sanctioned fix for the mutable-default trap — dataclasses actively **reject** a bare mutable default (`tags: list = []` raises `ValueError`), which is a nice guardrail.
- **`frozen=True`** makes instances immutable and hashable — the correct way to build a value object usable as a dict key or set member.
- **`slots=True`** (3.10+) generates `__slots__`, cutting per-instance memory and speeding attribute access for classes instantiated in bulk.
- **`order=True`** generates the comparison methods (`<`, `<=`, …) so instances sort by field order.
- **`__post_init__`** runs after the generated `__init__` for validation or derived fields, and `field(init=False)` / `field(repr=False)` fine-tune per field.

**How it compares to the alternatives** — the senior skill is picking the right one:

| Type | Mutable? | Stored as | Reach for it when… |
| --- | --- | --- | --- |
| **`@dataclass`** | Yes (unless `frozen`) | a normal class instance | general-purpose data holder with methods, defaults, validation |
| **`NamedTuple`** | **No** (immutable tuple) | a `tuple` subclass | a lightweight immutable record that should also behave like a tuple (unpackable, indexable) |
| **`TypedDict`** | Yes (it _is_ a dict) | a plain `dict` at runtime | annotating the **shape of a dict** (e.g. a JSON payload) for the type checker, with zero runtime class overhead |
| **`attrs`** | configurable | a normal class instance | you need more power than dataclasses (validators, converters, richer field control) — it's the third-party library dataclasses was inspired by |

Key distinctions to articulate: a **`NamedTuple`** is still a tuple — it's immutable, iterable, and unpackable (`x, y = point`), which dataclasses aren't unless you add it; use it for small fixed records where tuple behaviour is a feature. A **`TypedDict`** creates _no class at all_ at runtime — it's purely a static-typing annotation over an ordinary dict, ideal for typing external JSON without changing how you access it. **`attrs`** predates and outclasses dataclasses in flexibility (field validators, converters, `__slots__` by default), so it's the answer when the stdlib dataclass hits its limits. And when you also need **runtime validation and parsing** of external input, the real production answer is often **Pydantic**, which looks like a dataclass but coerces and validates every field against its annotations.

Rule of thumb: `@dataclass` by default; `NamedTuple` for immutable tuple-like records; `TypedDict` to type a dict's shape; `attrs`/Pydantic when you outgrow the standard library.

## 125- How does the `import` system work, and how do you deal with circular imports?

Importing is not textual inclusion — it **executes a module top to bottom exactly once** and binds the result to a name. Knowing the mechanism is what lets you reason about circular imports and `__pycache__`.

**What `import mymod` does, step by step:**

1. **Check `sys.modules` first** — a process-wide cache (dict) of every already-imported module. If `mymod` is there, the cached module object is returned immediately; the file is **not** re-executed. This is why repeated imports are cheap and why a module's top-level code runs only once per process.
2. **Find the module.** If it's not cached, the import system walks a chain of **finders** on `sys.meta_path`, which search `sys.path` (and package `__path__`) to locate the source and produce a **loader**.
3. **Load and execute.** The loader creates a new empty module object, **inserts it into `sys.modules` _before_ executing it** (crucial — see below), then runs the module body, populating its namespace. Compiled bytecode is cached in `__pycache__` to skip recompilation next time.
4. **Bind the name** in the importing namespace (`import x` binds `x`; `from x import y` binds `y`).

**Why circular imports break — and why they sometimes don't.** Because a module is registered in `sys.modules` _before_ its body finishes running, a cycle (A imports B, B imports A) doesn't infinitely recurse — but it can hand you a **half-initialised module**. If A is mid-execution when it triggers B, and B does `from A import thing`, `thing` may not exist yet, giving `ImportError: cannot import name 'thing'` or an `AttributeError`.

The senior toolkit for circular imports, in order of preference:

- **Restructure** — the cycle usually signals a design problem. Extract the shared piece into a third module both depend on, so the dependency graph becomes acyclic.
- **Import the _module_, not the name.** `import a` and later reference `a.thing` (resolved at call time) instead of `from a import thing` (resolved at import time). This defers the lookup past initialisation.
- **Move the import inside the function** that needs it (a deliberate local import — see the local-vs-global-imports question), so it runs after both modules are fully loaded.
- **For type hints only**, guard the import with `if typing.TYPE_CHECKING:` and use a string annotation — the import never runs at runtime, so it can't cycle.

Two related facts worth mentioning: an implicit **namespace package** (a directory without `__init__.py`, PEP 420) is discovered by a different finder and can span multiple `sys.path` entries; and `importlib` is the programmatic API (`importlib.import_module`, `importlib.reload`) when you need to import by name computed at runtime or force a re-execution.

## 126- What is `weakref` and when do you need it?

A **weak reference** points to an object **without incrementing its reference count**, so it does not, by itself, keep the object alive. If the only remaining references to an object are weak, the object is still collected, and the weak references "die" (start returning `None`). This is the escape hatch for the situations where ordinary strong references cause problems.

```python
import weakref

class Resource:
    pass

r = Resource()
ref = weakref.ref(r)      # a weak reference

print(ref() is r)         # True  - dereference by CALLING it
del r                     # drop the only strong reference
print(ref())              # None  - the object was collected; the weakref is dead
```

**The two problems weak references solve:**

1. **Caches that shouldn't keep their contents alive.** An ordinary dict used as a cache holds a strong reference to every cached object, so nothing it caches can ever be garbage-collected — a classic memory leak. `weakref.WeakValueDictionary` (values are weak) and `WeakKeyDictionary` (keys are weak) let entries **disappear automatically** once the rest of the program stops using them:

   ```python
   import weakref
   cache = weakref.WeakValueDictionary()
   def get(key):
       obj = cache.get(key)
       if obj is None:
           obj = expensive_load(key)
           cache[key] = obj          # cached, but not kept alive by the cache
       return obj
   ```

2. **Breaking reference cycles** — parent/child, observer/subject, or doubly-linked back-pointers. If a child holds a strong reference back to its parent, the two form a cycle that reference counting alone can't reclaim (it needs the slower cyclic GC). Making the **back-reference weak** breaks the cycle so plain refcounting collects both promptly, which matters for objects whose cleanup timing you care about.

Details a senior would add:

- You **dereference by calling** the weakref (`ref()`), and it returns the object or `None` — always check for `None`, because the object may have vanished between calls.
- **`weakref.finalize(obj, callback)`** registers a cleanup to run when the object is collected — a more reliable pattern than `__del__` for "do X when this dies".
- **Not everything is weak-referenceable.** Common built-ins — `int`, `str`, `tuple`, `list`, and `dict` — **cannot** be weakly referenced (though a _subclass_ of them can, because subclassing adds a `__weakref__` slot). A class using `__slots__` also loses weakref support unless it includes `'__weakref__'` in the slots. Ordinary custom classes support it out of the box.

The mental model: use a weak reference whenever you want to _observe or cache_ an object without _owning_ it — when its lifetime should be decided by someone else, and you want to be notified (via `None`) once it's gone.

## 127- What is structural pattern matching (`match`/`case`)?

`match`/`case` (Python 3.10+, PEP 634) is **structural pattern matching** — and the word "structural" is the whole point. It is emphatically **not** a C-style `switch`: rather than just comparing a value against constants, it **destructures** data by shape and **binds** the pieces to variables in one step.

```python
def handle(command):
    match command.split():
        case ["go", direction]:                 # matches a 2-element list, binds direction
            return f"moving {direction}"
        case ["drop", *items]:                  # binds the rest into a list
            return f"dropping {items}"
        case ["quit" | "exit"]:                 # OR pattern
            return "bye"
        case _:                                 # wildcard - the default
            return "unknown"

print(handle("go north"))    # moving north
print(handle("drop a b c"))  # dropping ['a', 'b', 'c']
```

The kinds of patterns are what make it powerful:

- **Sequence patterns** destructure lists/tuples, including `*rest` capture.
- **Mapping patterns** match dict shape: `case {"type": "user", "name": name}:` matches any dict with those keys and binds `name` (extra keys are allowed).
- **Class patterns** match by type _and_ pull out attributes positionally or by name: `case Point(x=0, y=y):` matches a `Point` on the y-axis and binds `y`. (Positional matching uses the class's `__match_args__`.)
- **Capture, wildcard, OR, and guards:** a bare name captures; `_` matches anything without binding; `|` combines alternatives; and an `if` **guard** adds a condition — `case Point(x, y) if x == y:`.

Two traps that separate a careful answer from a naïve one:

- **A bare name is a capture, not a comparison.** `case foo:` does **not** test "is the value equal to `foo`?" — it matches _anything_ and rebinds `foo`, shadowing any outer variable. To match against an existing constant you need a **dotted name** (`case Color.RED:`) or a literal; this is why enums and module-qualified constants are the idiom.
- It's most valuable for **decomposing complex, nested, heterogeneous data** — parsing an AST, dispatching on the shape of a JSON message, handling command objects. For a simple "one of N constants" branch, a plain `if/elif` or a dict dispatch table is clearer, and `match` is overkill.

The honest senior framing: `match`/`case` earns its place when you'd otherwise write a tangle of nested `if isinstance(...)` and index/key checks to pull a structure apart; it turns that into a flat, declarative, readable set of shapes. It doesn't replace `if` for ordinary conditionals.

## 128- What is the difference between `is` and `==`, and when does object identity trip people up?

`==` asks **"are these equal in value?"** (it calls `__eq__`). `is` asks **"are these the exact same object in memory?"** (it compares identity — effectively `id(a) == id(b)` — and can never be overridden). Two distinct objects can be equal; the same object is trivially both.

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True  - same contents
print(a is b)   # False - two separate list objects
c = a
print(a is c)   # True  - c is just another name for the same object
```

**The one rule that matters in practice:** use `is` **only** for comparing against singletons — `None`, `True`, `False`, and sentinel objects. The idiom is `if x is None:`, never `if x == None:`, because a pathological `__eq__` could make `== None` lie, and `is None` is faster and unambiguous. For everything else — numbers, strings, containers — use `==`.

**Where identity trips people up: caching makes `is` _appear_ to work on values, until it doesn't.** CPython pre-allocates and reuses certain immutable objects, so identity accidentally coincides with equality for them:

```python
print(256 is 256)     # True  - small ints (-5..256) are cached singletons
print(257 is 257)     # often False - 257 is outside the cached range
x = "hello"; y = "hello"
print(x is y)         # often True - compile-time string interning
z = "".join(["h", "i"]); print(z is "hi")  # often False - built at runtime, not interned
```

These results are **implementation details** — they vary by Python version, by whether values are literals in the same code object, and between CPython/PyPy. Relying on `is` for value comparison produces bugs that pass in testing (small numbers, short literals) and fail in production (larger numbers, computed strings). That fragility is precisely _why_ the "`is` only for singletons" rule exists.

Senior-level footnotes:

- **String interning** can be forced with `sys.intern(s)`, occasionally worth it when you compare many long strings repeatedly — interned strings compare by identity first, making `==` short-circuit.
- `id()` returns an object's identity (its address in CPython); it's unique only among _live_ objects, so a freed object's id can be reused.
- A subtle gotcha: `float('nan') != float('nan')` is `True` (NaN is not equal to itself), yet `x = float('nan'); x is x` is `True` — a case where `is` and `==` genuinely diverge, and why containers use an identity check _before_ equality when searching.

## 129- What is monkey patching, and when is it appropriate?

**Monkey patching** is replacing or extending code — a method, function, attribute, or whole class — **at runtime**, dynamically, by reassigning it. Python allows it because classes and modules are just mutable objects: you can rebind their attributes after they're defined.

```python
import some_library

def patched(self, *args, **kwargs):
    ...  # your replacement behaviour

some_library.SomeClass.method = patched   # swap the method out at runtime
```

**Where it's legitimate:**

- **Testing** — the single most defensible use. `unittest.mock.patch` is monkey patching with a safety net: it temporarily swaps a dependency for a mock/stub, then **restores the original automatically** when the test ends. Replacing a network call, a clock (`time.time`), or a database with a fake is standard practice.
- **Hotfixing a third-party bug** you can't wait for upstream to fix or can't fork — patch the broken method in your own startup code as a stopgap.
- **Compatibility shims / backporting** — polyfilling a missing method so old and new versions of a library present the same interface.
- **Framework instrumentation** — some profilers, tracers, and greenlet libraries (e.g. `gevent`'s `monkey.patch_all()`) patch the standard library to inject their behaviour transparently.

**Why it's dangerous, and the senior's caution:**

- It's **action at a distance.** A patch applied in one module silently changes behaviour everywhere that code is used, so a reader of the affected class has no local indication that it was altered — nightmarish to debug.
- It's **fragile against upgrades.** You're reaching into another library's internals; the next version can rename or restructure what you patched, breaking your code with no warning.
- **Ordering and global state matter** — two patches of the same target, or a patch applied after the target is already used, produce order-dependent bugs.

The rule a senior applies: **prefer the ordinary extension mechanisms first** — subclassing, composition, dependency injection, decorators, registering a plugin/hook. Those are explicit and local. Treat monkey patching as a last resort for the specific cases above (and always as the _normal_ tool in tests via `mock.patch`, where the patch is scoped and auto-reverted). If you must patch production code, isolate it in one clearly named module, comment _why_, and pin the dependency version you patched against.

## 130- How do operators dispatch to dunder methods, and what is `NotImplemented`?

When you write `a + b`, Python doesn't have a single "add" — it dispatches to **`a.__add__(b)`**, and there's a fallback protocol that senior engineers are expected to understand, centred on the special sentinel **`NotImplemented`**.

**The dispatch sequence for a binary operator `a + b`:**

1. Python calls **`a.__add__(b)`**. If `a`'s type knows how to add a `b`, it returns the result.
2. If `a.__add__` doesn't know how to handle `b`, it should **`return NotImplemented`** (not raise, not return `None`). This is a signal, not a result.
3. Python then tries the **reflected** method **`b.__radd__(a)`** — giving the _right_ operand a chance. This is how `2 + my_object` can work even though `int.__add__` has never heard of your class: `int.__add__` returns `NotImplemented`, so Python calls `my_object.__radd__(2)`.
4. If both return `NotImplemented`, Python raises `TypeError: unsupported operand type(s)`.

```python
class Money:
    def __init__(self, cents): self.cents = cents
    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.cents + other.cents)
        return NotImplemented          # let Python try other.__radd__
    __radd__ = __add__                 # so sum([...]) and int+Money can work
    def __repr__(self): return f"Money({self.cents})"

print(Money(100) + Money(50))          # Money(150)
```

**The critical distinctions to get right:**

- **`NotImplemented` is a singleton sentinel; `NotImplementedError` is an exception.** They are unrelated. Operator methods **return** `NotImplemented` to say "I don't handle this — try the other operand." Abstract methods **raise** `NotImplementedError` to say "a subclass must implement this." Confusing them is a classic mistake, and returning `NotImplementedError` (the class) from `__add__` silently breaks the fallback because it's a truthy object, not the sentinel.
- **Reflected methods** (`__radd__`, `__rmul__`, `__rsub__`, …) exist for every binary operator and are what make your type interoperate with built-in types on the left. `__rsub__` must remember the operands are swapped: `a - b` failing over calls `b.__rsub__(a)`, i.e. "compute a − b" from b's perspective.
- **In-place operators** (`__iadd__` for `+=`, etc.) let mutable types mutate themselves and return `self`; if absent, `a += b` falls back to `a = a + b`, rebinding the name.
- **Rich comparisons** (`__eq__`, `__lt__`, …) follow the same `NotImplemented` fallback, and returning `NotImplemented` from `__eq__` lets Python fall back to identity comparison rather than forcing a wrong answer.

The takeaway: implement operators so that they **return `NotImplemented` for types they don't recognise** rather than raising or guessing — that single discipline is what lets Python's reflected-operator machinery compose your types cleanly with each other and with the built-ins.

## 131- What is exception chaining, and what are `__context__`, `__cause__`, and `__suppress_context__`?

When a new exception is raised while another is being handled, Python **links the two** so the traceback tells the whole story. Formalised in PEP 3134, every exception carries three attributes that govern this: `__context__`, `__cause__`, and `__suppress_context__`. Understanding them is what lets you read — and control — multi-exception tracebacks.

**Implicit chaining.** Raising inside an `except` (or `finally`, or `with`) automatically sets the new exception's `__context__` to the one being handled:

```python
try:
    open("foo.bar")
except OSError:
    raise RuntimeError("oops")
```

The traceback prints both, joined by **"During handling of the above exception, another exception occurred:"** — Python is telling you the `RuntimeError` surfaced _while_ dealing with the `OSError`, without claiming one caused the other.

**Explicit chaining with `raise ... from`.** To state deliberately that one exception _caused_ another, use `from`:

```python
try:
    open("foo.bar")
except OSError as e:
    raise RuntimeError("oops") from e
```

`from e` additionally sets `__cause__` to `e` and flips `__suppress_context__` to `True`. The traceback now reads the stronger **"The above exception was the direct cause of the following exception:"**. This is the right tool when translating a low-level error into a domain-specific one.

**Suppressing the chain with `from None`.** What does this print?

```python
try:
    1 / 0
except ZeroDivisionError:
    raise RuntimeError("zero!") from None
```

Only the `RuntimeError`. `from None` sets `__cause__` to `None` and `__suppress_context__` to `True`, and the display rule then hides the context.

**The traceback display rule**, worth memorising:

- If `__cause__` is present, **always** show it ("direct cause").
- Otherwise, show `__context__` **only if** `__suppress_context__` is `False` ("during handling").

**The crucial subtlety:** `from None` (and `from e`) only change what is _printed_. The original exception is still stored in `__context__` — ignored for display, not discarded. That is the practical lever: if a library swallows a detailed error and re-raises a vague one, you can recover the original from the chain **without touching the library**:

```python
try:
    token = Token(raw)                 # library raises DecodeError("could not decode")
except DecodeError as e:
    original = e.__context__           # the detailed TokenError the library hid
    detail = e.__context__.args[0]     # its original message
```

Rule of thumb: use `raise ... from e` when the new exception is genuinely caused by the old one, and `raise ... from None` when the original is noise you deliberately want to hide from users.

## 132- What modern exception features did Python 3.11 add (`add_note`, `ExceptionGroup`, `except*`)?

**Exception notes (`add_note`).** Since Python 3.11 you can attach extra context to an existing exception _without_ wrapping or re-raising it with a new type. Notes accumulate in the exception's `__notes__` list and are printed beneath the traceback:

```python
try:
    try:
        raise ValueError
    except Exception as e:
        e.add_note("while parsing the config file")
        raise
except Exception as e:
    e.add_note("during application startup")
    raise

# Traceback (most recent call last):
#   ...
# ValueError
# while parsing the config file
# during application startup
```

This is often cleaner than re-raising with a different message: you enrich the _original_ exception in place, keeping its type and traceback intact. It shines for adding "which item / which file / which retry" context as an exception bubbles up through layers.

**`ExceptionGroup` and `except*`.** An `ExceptionGroup` packs several exceptions into a single object — essential when concurrent operations can each fail independently. The new `except*` syntax matches and handles **by type across the group**, peeling out the matching sub-exceptions and letting the rest propagate:

```python
try:
    raise ExceptionGroup(
        "multiple failures",
        [ValueError("bad value"), KeyError("missing key")],
    )
except* ValueError as eg:
    print("value errors:", eg.exceptions)   # handles only the ValueError branch
except* KeyError as eg:
    print("key errors:", eg.exceptions)     # handles only the KeyError branch
```

Each `except*` clause receives a _sub-group_ containing only the matching exceptions, and — unlike plain `except`, where the first match wins and the rest are lost — **multiple `except*` clauses can fire for one group**. The place you'll actually meet this is `asyncio.TaskGroup` (also 3.11+), which collects the failures of several child tasks and raises them together as an `ExceptionGroup`.

## 133- What is the `warnings` module, and how do `UserWarning`/`DeprecationWarning` differ from exceptions?

The built-in `Warning` classes — `UserWarning`, `DeprecationWarning`, `PendingDeprecationWarning`, and others — inherit from `Warning`, which itself inherits from `Exception`. But despite being in the exception hierarchy, they are **not meant to be raised**. They are _categories_ for the `warnings` module, which reports non-fatal issues without stopping the program:

```python
import warnings

def foo():
    warnings.warn("Don't use me anymore!", DeprecationWarning)  # explicit category
    warnings.warn("bar")                                        # defaults to UserWarning
```

The value is that the _user_, not the library author, controls what gets reported, via the **warning filter**:

```python
warnings.simplefilter("ignore")   # silence every warning
warnings.simplefilter("error")    # promote warnings to exceptions -> foo() now raises
```

Two behaviors to know:

- By default each distinct warning is shown **once per location** and then suppressed (the `"default"` filter), which is why calling `foo()` a second time prints nothing new.
- The `"error"` filter turns warnings into real exceptions — and this is _precisely why_ the hierarchy roots at `Exception`: promoting a warning to an error is just raising it. Enabling `-W error` (or `filterwarnings = error` in pytest) is the standard way to make `DeprecationWarning`s **fail the build** in CI, catching deprecated usage before it breaks on an upgrade.

When to use which: **raise an exception** for a problem the caller must handle right now; **emit a warning** for something that still works but shouldn't be relied on — deprecations, or suspicious-but-legal usage — leaving the final decision (ignore, show, or escalate to an error) to the user.

## 134- Walk through the full class-creation protocol: `__prepare__`, the metaclass, and how `__call__` controls instantiation

Question 120 covered _what_ a metaclass is; the senior follow-up is _what actually happens_ when a `class` statement runs, and how that differs from what happens when you later call the class to make an instance. These are two separate events driven by two different hooks, and conflating them is the classic mistake.

**Class-definition time — the four steps behind `class Foo(Base): ...`:**

1. **Determine the metaclass.** Python uses the explicit `metaclass=` if given, otherwise the most-derived metaclass among the bases, otherwise `type`.
2. **Prepare the namespace.** Python calls `metaclass.__prepare__(name, bases, **kwds)`, which returns the mapping used to execute the class body. The default is an ordinary `dict`, but returning a custom mapping lets you _record definition order_ or _forbid duplicate names_ — this is exactly how `EnumMeta` rejects two members with the same name.
3. **Execute the class body** into that namespace — every method `def` and class variable becomes a key.
4. **Create the class object** by calling `metaclass(name, bases, namespace)`, which runs the metaclass's `__new__` (builds the class) then `__init__` (configures it).

```python
class OrderedMeta(type):
    @classmethod
    def __prepare__(mcs, name, bases, **kwds):
        return {}                         # a real impl might return OrderedDict / a duplicate-guard
    def __new__(mcs, name, bases, ns):
        cls = super().__new__(mcs, name, bases, ns)
        cls._fields = [k for k in ns if not k.startswith("__")]
        return cls
```

**Instance-creation time — a _different_ hook.** When you write `Foo(1, 2)`, Python does **not** call `Foo.__new__` directly. It calls `type(Foo).__call__` — i.e. the **metaclass's `__call__`** — and _that_ is what orchestrates the usual `instance = cls.__new__(cls, ...)` then `cls.__init__(instance, ...)` dance. Overriding the metaclass `__call__` is therefore the clean way to control instantiation itself — the correct way to build a true Singleton or an instance cache, avoiding the well-known pitfalls of hijacking `__new__`:

```python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Config(metaclass=Singleton):
    pass

assert Config() is Config()   # same object every time
```

**The distinction to state crisply:** metaclass `__new__`/`__init__` run **once, when the class is defined**; metaclass `__call__` runs **every time you instantiate the class**. And as question 120 stressed, for almost all real needs the lighter hooks — `__init_subclass__` (react to subclassing) and `__set_name__` (descriptors learn their attribute name) — are the right tools; reach for `__prepare__` and a custom `__call__` only when you genuinely need to reshape the namespace or intercept construction.

## 135- Reference cycles, `__del__`, `weakref`, and `gc.freeze()`: the practical garbage-collection questions

Question 11 laid out the two mechanisms — always-on reference counting plus a cyclic collector for the cycles refcounting can't see. The senior-level follow-ups probe the _interactions_ between those mechanisms and the tools you use to tame them.

**`__del__` and cycles — the historical trap.** A finaliser (`__del__`) that participates in a reference cycle used to be poison: before **PEP 442 (Python 3.4)** the collector couldn't decide a safe order to run finalisers in a cycle, so it gave up and dumped those objects into `gc.garbage`, leaking them forever. Since 3.4 finalisers _do_ run even inside cycles, but `gc.garbage` still exists and `__del__` remains unreliable for other reasons: its timing is tied to refcount reaching zero, it may **not run at all** at interpreter shutdown, and it can even _resurrect_ the object by creating a new reference to `self`. The rule: **never use `__del__` for resource cleanup** — use a context manager (`with`) or `weakref.finalize`, which is explicitly designed for this.

**`weakref` — references that don't keep objects alive.** A weak reference does _not_ increment the refcount, so it never prevents collection. Three canonical uses:

- **Caches** that shouldn't pin their entries in memory — `weakref.WeakValueDictionary` / `WeakKeyDictionary`.
- **Breaking cycles** — e.g. a child holding a _weak_ back-reference to its parent so the pair can be collected by refcounting alone, no cyclic pass needed.
- **Death callbacks** — `weakref.ref(obj, callback)` or `weakref.finalize(obj, cleanup)` to run code when the object goes away.

**Tuning the collector.** It runs on **allocation-count thresholds** (`gc.get_threshold()`), not a clock. Practical levers:

- `gc.disable()` in a **short-lived batch job** (the process exits before cycles matter) or in a **latency-sensitive request path** where you can't afford an unpredictable pause — then `gc.collect()` manually at a quiet moment.
- **`gc.freeze()` (Python 3.7+)** is the pre-fork server trick: call it _after_ loading your app but _before_ forking workers (gunicorn/uWSGI). It moves all currently-tracked objects into a permanent generation the collector ignores, so subsequent collections don't touch their GC headers — which keeps the shared, copy-on-write memory pages _clean_ across `fork()` instead of being dirtied by refcount/GC bookkeeping. This is the famous optimisation Instagram used to cut memory.

**Diagnosing a leak in a long-running service:** reach for `tracemalloc` (snapshot + diff allocations by line), `gc.get_referrers(obj)` / `gc.get_objects()` to find what is holding an object alive, `objgraph` to visualise reference chains, and `gc.set_debug(gc.DEBUG_LEAK)` to log uncollectable objects. Remember the allocator subtlety from Q11: freeing objects returns memory to pymalloc's free lists, **not** always to the OS, so flat-but-high RSS is not necessarily a leak.

## 136- What is `setup.py`, and how has Python packaging changed with `pyproject.toml`?

`setup.py` is the historical build script of a Python package: a plain Python file that calls `setuptools.setup(...)` with the project's metadata and dependencies. Because it is _executable code run at build/install time_, it was both powerful and problematic — a tool couldn't even learn a package's name or dependencies without **executing arbitrary code**, which hurt security, reproducibility, and speed.

```python
# setup.py  (the legacy style)
from setuptools import setup, find_packages
setup(
    name="mypkg", version="1.0.0",
    packages=find_packages(),
    install_requires=["requests>=2"],
    entry_points={"console_scripts": ["mycli = mypkg.cli:main"]},
)
```

**The modern, standards-based workflow** replaces that with **static declaration in `pyproject.toml`**, defined by three PEPs a senior should be able to name:

- **PEP 518** — the `[build-system]` table declares which **build backend** to use and what it needs to build, so tools stop assuming setuptools.
- **PEP 517** — a standard _interface_ between front-end tools (`pip`, `build`) and the backend, decoupling them.
- **PEP 621** — the `[project]` table for **static metadata** (name, version, dependencies, scripts) that tools can read _without executing code_.

```toml
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "mypkg"
version = "1.0.0"
dependencies = ["requests>=2"]

[project.scripts]
mycli = "mypkg.cli:main"
```

**Key points to land:**

- **`setup.py` is not dead, but its role shrank.** It's now just one possible _configuration file_ for the setuptools backend, still useful for **compiled C/Rust extensions (`ext_modules`)** or genuinely dynamic metadata. But invoking it directly (`python setup.py install`, `sdist`, `bdist_wheel`) is **deprecated** — use `python -m build` and `pip` instead. `distutils` itself was **removed from the stdlib in Python 3.12**.
- **Build backends are pluggable:** `setuptools`, `hatchling`, `flit-core`, `pdm-backend`, `maturin` (Rust). Tools like Poetry, Hatch, PDM, and uv wrap this same PEP 517/518/621 flow.
- **Editable installs** (`pip install -e .`) — for live development — now work for `pyproject.toml`-only projects thanks to **PEP 660**, no `setup.py` required.
- **Entry points** declared here power both **console scripts** (CLI commands) and **plugin discovery** at runtime via `importlib.metadata.entry_points()`.
- Building produces an **sdist** (source) and a **wheel** (the installable built distribution — see the wheel-vs-egg question); publish with `twine upload dist/*`.

The one-line takeaway: **declare metadata statically in `pyproject.toml` and let a PEP 517 backend build it; keep `setup.py` only for legacy projects or native extensions.**

## 137- What is GraphQL, how does it differ from REST, and how do you serve it from Python?

GraphQL is a **query language for APIs plus a runtime** that executes those queries against your data. Instead of many endpoints each returning a fixed shape, a GraphQL service exposes **one endpoint** (typically `POST /graphql`) backed by a **strongly typed schema**, and the **client specifies exactly which fields it wants** in the response.

**How it differs from REST:**

- **Response shape is client-controlled.** REST returns a server-defined payload, which leads to **over-fetching** (you get fields you don't need) or **under-fetching** (you must call three endpoints to assemble one screen). A GraphQL query returns precisely the requested fields, and can traverse nested/related data in **one round trip**.
- **One typed schema, introspectable.** The schema (queries, mutations, subscriptions) is self-documenting and tooling-friendly (auto-complete, GraphiQL).
- **Trade-offs the interviewer wants to hear:** HTTP **caching is harder** (everything is a `POST` to one URL, versus REST's cacheable `GET`s and CDNs); **rate-limiting and observability** are trickier because one URL hides wildly different costs; and you must **defend against expensive queries** (depth/complexity limits, persisted queries) and the **N+1 problem**.

**Serving it from Python.** The main libraries are **Strawberry** (modern, uses type hints/dataclasses, first-class FastAPI integration), **Graphene** (older, class-based), and **Ariadne** (schema-first SDL). A minimal Strawberry + FastAPI service:

```python
import strawberry
from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI

@strawberry.type
class Book:
    title: str
    author: str

@strawberry.type
class Query:
    @strawberry.field
    def books(self) -> list[Book]:
        return [Book(title="Dune", author="Herbert")]

schema = strawberry.Schema(Query)
app = FastAPI()
app.include_router(GraphQLRouter(schema), prefix="/graphql")
```

**Resolvers and the N+1 problem.** Every field is backed by a **resolver** function. The classic performance trap: a query for 100 authors whose resolver each issues one DB query for that author's books → **101 queries**. The standard fix is a **DataLoader**, which **batches** the individual lookups made during one request into a single query and **caches** within that request.

**When to choose which:** GraphQL shines for **many clients with divergent data needs** (web + mobile), bandwidth-constrained clients, and **deeply nested/graph-like** data. REST is often the better default for **simple CRUD**, when you need **HTTP caching/CDNs**, file uploads, or a **public, cacheable** API. The two also coexist happily behind the same service.

## 138- How would you integrate an AI/ML model into a Python service, and what are the engineering concerns?

Most application engineers do **inference, not training** — the job is to take a trained model and serve its predictions reliably inside a normal service. There are two integration patterns:

- **Call a hosted model API** (OpenAI, Vertex, Bedrock): no infrastructure, pay per call, but you inherit **network latency, rate limits, cost per request, and data-privacy** constraints (you're sending data to a third party).
- **Self-host the model**: load the weights **in-process** (PyTorch/`transformers`/scikit-learn) or behind a dedicated serving layer (**Triton, TorchServe, vLLM**, or a `FastAPI` wrapper). You control latency and data, but own the GPU/CPU capacity and ops.

**The concern that trips people up in an async service:** model inference is **CPU/GPU-bound and synchronous**. In FastAPI/`asyncio`, running it directly in an `async def` handler **blocks the event loop** and stalls _every_ concurrent request. Offload it — `await loop.run_in_executor(pool, model.predict, x)` for a thread/process pool, or hand it to a **Celery worker** (exactly the `worker` mode this repo runs). This ties back to the GIL: heavy native libraries (PyTorch, NumPy) **release the GIL** during compute, so a thread pool genuinely helps; pure-Python pre/post-processing does not and needs processes.

**Lifecycle and operational concerns:**

- **Load the model once at startup**, keep it warm in memory (e.g. in the app lifespan), never per-request — loading weights is expensive.
- **Version the model artifact** independently of code; store it in a registry/S3, not the repo, and log which version served each prediction.
- **Throughput vs latency:** dynamic **batching** of requests, **caching** results/embeddings, streaming where possible.
- **Resilience for external calls:** timeouts, **retries with exponential backoff**, circuit breakers, and hard **cost/quota controls**.
- **Observability & correctness:** monitor latency and error rates, watch for **data/model drift**, log inputs/outputs with **PII care**, and pin the _preprocessing_ alongside the model so results stay reproducible.

The senior framing: treat the model as an **unreliable, expensive, versioned dependency** — isolate it behind a service boundary, keep it off the event loop, and wrap it in the same timeouts, retries, caching, and monitoring you'd give any external system.

## 139- What does a senior engineer need to know about building on LLMs (tokens, context windows, RAG, structured output, hallucination)?

At the API level an LLM is a **next-token predictor**: you send a prompt, it samples output tokens one at a time. The single most important mental model is that it is **stateless** — it has no memory between calls, so a "conversation" is an illusion you maintain by **resending the entire history** every request.

**Tokens and the context window.** Text is split into **tokens** (~4 characters / ¾ of a word in English). You are billed per **input + output** token and bounded by the **context window** — the maximum tokens for a single request (prompt _and_ completion). Count them with `tiktoken`; inputs that exceed the window must be **truncated, summarised, or chunked**. Runaway history is the usual cause of surprise bills and `context_length_exceeded` errors.

**Sampling controls:** `temperature` / `top_p` govern randomness (near-0 for extraction/classification, higher for creative text), `max_tokens` caps output, `stop` sequences end generation, and `seed` gives _best-effort_ determinism. Streaming tokens back (SSE) is a UX necessity for anything long.

**Hallucination.** LLMs produce **fluent, confident, and sometimes false** output, and they cannot reliably tell when they're wrong. You mitigate — never fully eliminate — with grounding, asking for citations, constraining the output, external verification, and **human-in-the-loop** for high-stakes decisions.

**RAG (Retrieval-Augmented Generation) — the dominant grounding pattern:** **embed** your documents into vectors and store them in a **vector database** (pgvector, Pinecone, FAISS, Qdrant); at query time, embed the user's question, **retrieve the top-k most similar chunks**, and inject them into the prompt as context. This grounds answers in _your_ data, sidesteps the context-window and knowledge-staleness limits, and is how "chat over your documents" is built.

**Structured output — don't parse prose.** For anything programmatic, force the model into a machine-readable shape via **JSON mode / function (tool) calling / a schema**, validate it (e.g. with **pydantic**), and retry on validation failure. Libraries like `instructor` and the OpenAI SDK's structured outputs do exactly this; orchestration frameworks (LangChain, LlamaIndex) help but can over-abstract — reach for them deliberately.

**Security and engineering discipline:** treat **model output and any retrieved/third-party content as untrusted input** — **prompt injection** is the LLM-era injection attack, so never let raw model output trigger privileged actions unchecked. Round it out with cost controls (cache, right-size the model, trim history), rate-limit/retry handling, and **evals** — regression tests for prompts, because a model or prompt change can silently degrade quality with no stack trace to warn you.

## 140- How do you actually test Python code — pytest fixtures, parametrization, and mocking?

Question 87 introduced `unittest`; in practice most modern teams reach for **`pytest`**, and a senior is expected to know _why_ and to test with discipline. Pytest replaces `unittest`'s ceremony (subclass `TestCase`, `self.assertEqual`) with **plain `assert`** — its rewritten assertion introspection prints the actual operands on failure — plus **fixtures**, **parametrization**, and a rich plugin ecosystem.

**Fixtures are dependency injection for tests.** A fixture is a function that builds something a test needs; the test requests it by naming it as a parameter. `yield` splits setup from teardown, and **scopes** (`function`, `class`, `module`, `session`) control how often it runs. Shared fixtures live in `conftest.py`, discovered automatically without imports:

```python
import pytest

@pytest.fixture
def db():
    conn = connect()          # setup
    yield conn                # hand it to the test
    conn.close()             # teardown, even if the test fails

def test_user_count(db):      # pytest injects the fixture by name
    assert db.count("users") == 0
```

**Parametrization** turns one test into a table of cases — far better than a loop, because each row reports pass/fail independently:

```python
@pytest.mark.parametrize("value, expected", [(2, 4), (3, 9), (-1, 1)])
def test_square(value, expected):
    assert square(value) == expected
```

**Mocking — isolate the unit from the world.** Use `unittest.mock` (or the `mocker` fixture from `pytest-mock`) to replace slow/external dependencies. The single most common mistake is **patching where the object is _defined_ instead of where it is _used_** — you must patch the name in the module under test (`myapp.service.requests`, not `requests`). Configure behaviour with `return_value`/`side_effect` and assert interactions with `assert_called_once_with`:

```python
def test_fetch(mocker):
    m = mocker.patch("myapp.service.requests.get")
    m.return_value.json.return_value = {"ok": True}
    assert fetch() == {"ok": True}
    m.assert_called_once_with("https://api/health", timeout=5)
```

Know the vocabulary — **stub** (canned answers), **mock** (asserts on calls), **fake** (a working lightweight implementation, e.g. an in-memory DB) — and the `monkeypatch` fixture for env vars and attributes. Round it out with **markers** (`@pytest.mark.skip`, `xfail`, custom markers, `-k` selection), **coverage** (`pytest --cov`, aim >80%), and **property-based testing** (`Hypothesis`) to generate edge cases you'd never enumerate by hand. The senior framing: keep tests **fast, isolated, and deterministic**, follow the **test pyramid** (many unit, fewer integration, few E2E), and mock at the boundaries — not the internals.

## 141- What is Pydantic, and how does it differ from `dataclasses`?

**Pydantic** is a **runtime data-validation and parsing** library driven by type hints — the backbone of FastAPI and the standard way to turn untrusted external input (JSON bodies, config, env vars) into trusted, typed Python objects. You declare a model with annotations; Pydantic **validates, coerces, and (de)serializes** for you, raising a structured `ValidationError` when the data doesn't fit.

```python
from pydantic import BaseModel, Field, field_validator

class User(BaseModel):
    id: int
    name: str = Field(min_length=1)
    email: str

    @field_validator("email")
    @classmethod
    def must_have_at(cls, v: str) -> str:
        if "@" not in v:
            raise ValueError("invalid email")
        return v

User.model_validate({"id": "42", "name": "Ada", "email": "a@b.com"})  # id coerced "42"->42
```

**The crucial distinction from `dataclasses` (Q124):** a dataclass is _only_ a boilerplate reducer — it will happily store `User(id="not-an-int")` because annotations are **not enforced at runtime** (Q121). Pydantic exists precisely to **enforce** them: parse, validate, coerce, and serialize. Rule of thumb — **dataclasses for trusted internal data, Pydantic at the boundaries** where data arrives from outside.

Points a senior should land:

- **v1 vs v2 matters.** Pydantic 2 rewrote the core in Rust (`pydantic-core`) for a large speedup and **renamed the API**: `.dict()`→`.model_dump()`, `.json()`→`.model_dump_json()`, `parse_obj`→`model_validate`, and the `@validator`/`@root_validator` decorators became `@field_validator`/`@model_validator`. Mixing v1 and v2 idioms is a common migration bug.
- **`Field(...)`** adds constraints (`gt`, `max_length`, `default_factory`, aliases) and doc metadata that flows into the auto-generated **JSON Schema / OpenAPI**.
- **`pydantic-settings`** (`BaseSettings`) reads and validates configuration from environment variables — the typed alternative to scattering `os.getenv` calls.
- Validation isn't free; for hot paths over already-trusted data, a `dataclass` or `NamedTuple` is lighter.

## 142- Beyond basic hints — what are `Protocol`, `TypeVar`/`Generic`, and how do you actually enforce types?

Questions 121 and 124 established that hints don't run and introduced `dataclasses`; the senior-level material is the **static** type system you build for tools like **mypy** and **pyright**, and the two features that make it powerful: **Protocols** and **generics**.

**`Protocol` — structural (duck) typing, statically.** Instead of requiring inheritance from a base class (nominal typing), a `Protocol` matches **any object that has the right shape**. This types Python's actual duck-typing idiom without forcing an inheritance hierarchy:

```python
from typing import Protocol

class Readable(Protocol):
    def read(self) -> bytes: ...

def consume(src: Readable) -> bytes:   # accepts files, sockets, BytesIO — anything with read()
    return src.read()
```

Decorate with `@runtime_checkable` to allow `isinstance` against it (shallow — checks method presence only).

**`TypeVar`/`Generic` — parametric polymorphism.** A `TypeVar` lets a function or class be typed _in terms of_ the caller's type, so a container preserves element type instead of collapsing to `Any`. Python 3.12 (**PEP 695**) added clean built-in syntax:

```python
# classic
from typing import TypeVar, Generic
T = TypeVar("T")
class Stack(Generic[T]):
    def push(self, item: T) -> None: ...
    def pop(self) -> T: ...

# PEP 695 (3.12+) — no TypeVar import
class Stack[T]:
    def push(self, item: T) -> None: ...
    def pop(self) -> T: ...
```

TypeVars can be **bounded** (`TypeVar("T", bound=Number)`) or **constrained** (`TypeVar("S", str, bytes)`), and variance matters for correctness. Round out the toolbox: **`Optional[X]` / `X | None`**, **`Union` / `X | Y`**, **`Literal`** (exact values), **`Final`**, **`@overload`** (multiple typed signatures), **`ParamSpec`** (typing decorators that forward args), **`Self`**, **`Annotated`** (attach metadata — how FastAPI/Pydantic carry validation), and **`TypedDict`** for structured dicts.

**Enforcement is a _tooling_ decision, not a runtime one.** Run **mypy** or **pyright** in CI, ideally in **strict mode**, to catch type errors before runtime; guard import-cycle-only imports behind `if TYPE_CHECKING:`; and ship **stub files (`.pyi`)** for typing code you can't annotate inline. The payoff a senior emphasises: types are executable documentation that a machine verifies — most valuable on large, long-lived codebases and public APIs.

## 143- How do you find and fix a performance bottleneck in Python?

The senior answer begins with discipline, not tricks: **measure before you optimise.** Knuth's "premature optimization is the root of all evil" is the rule — profile to find the real hot spot, because it is almost never where you guess, and un-profiled "optimisations" trade readability for nothing.

**Know which tool answers which question:**

- **`timeit`** — microbenchmark a single expression or snippet, correctly (many loops, best-of-N).
- **`cProfile` + `pstats`** — deterministic, function-level profile: _which functions_ dominate cumulative/total time. The standard first pass.
- **`line_profiler`** — line-by-line timing _inside_ the hot function `cProfile` fingered.
- **`py-spy`** — a **sampling** profiler that attaches to a **running production process without modifying or restarting it** — the tool for "prod is slow right now." Can emit flame graphs.
- **Memory**: `tracemalloc` (stdlib, snapshot/diff allocations by line), `memory_profiler`, and `memray` / `scalene` (which profiles CPU _and_ memory together).

**Then optimise in order of leverage:**

1. **Algorithm and data structure first** — the biggest wins are almost always Big-O. Swapping a repeated `x in some_list` (O(n)) for a `set` (O(1)) beats any micro-tuning (ties to Q90).
2. **Use the interpreter's fast paths** — built-ins and C-implemented libraries: `str.join` over `+=` in a loop, comprehensions over manual loops, and **vectorise with NumPy/pandas** to push loops into C (which also _releases the GIL_, Q1).
3. **Avoid repeated work** — hoist invariants out of loops, bind hot attribute/global lookups to locals, and **cache** (`functools.cache`/`lru_cache`, Q103).
4. **Reduce memory pressure** — `__slots__` (Q77) for many small objects, **generators** to stream instead of materialising large lists.
5. **Only then reach for heavy machinery** — `Cython`, `numba` (JIT), a C/Rust extension, or **concurrency** (choosing the right model per Q119, remembering the GIL means threads help I/O, processes help CPU).

The takeaway: **profile → fix the biggest thing → re-measure**, and stop when it's fast enough. A clear O(n) beating a clever O(n log n) with a huge constant is often the right engineering call.

## 144- What are the security footguns every Python engineer must know?

Security is where senior engineers earn their title, and Python has a specific set of traps worth naming precisely:

- **Deserialising untrusted data = remote code execution.** **`pickle`**, `marshal`, and `yaml.load` can **execute arbitrary code** while loading. Never unpickle data you didn't produce; for untrusted input use **JSON**, and always **`yaml.safe_load`**. This is the single most dangerous, most-overlooked Python-specific footgun.
- **`eval` / `exec` / `compile` on any input derived from a user** is code injection. Almost always avoidable with `ast.literal_eval`, a real parser, or a lookup table.
- **Injection generally.** **SQL injection** — use **parameterised queries / bound parameters**, _never_ f-strings or `%` into SQL (an ORM helps but you can still foot-gun with raw SQL). **Command injection** — call `subprocess` with an **argument list and `shell=False`**, never `shell=True` on interpolated strings. **Path traversal** — validate/normalise paths against a base directory.
- **Randomness for security.** `random` is a **predictable PRNG** — never use it for tokens, passwords, or session IDs. Use the **`secrets`** module (`secrets.token_urlsafe`). Hash passwords with **bcrypt/argon2/scrypt**, never plain `md5`/`sha256`, and compare secrets with **`hmac.compare_digest`** to avoid timing attacks.
- **`assert` is stripped under `-O`.** Optimised bytecode (`python -O`) removes `assert` statements, so **never use `assert` for a security or validation check** in production code — the check silently vanishes.
- **Supply chain.** Pin dependencies, scan them (**`pip-audit`**, Safety, GitHub Dependabot), and beware **typosquatting** on PyPI. `pip install` can run arbitrary code from a malicious `setup.py` (Q136) — this is why static-metadata wheels are safer.
- **XML** — the stdlib parsers are vulnerable to entity-expansion/XXE attacks; use **`defusedxml`** for untrusted XML.

The mindset to convey: **treat every byte crossing a trust boundary as hostile** — deserialisation, subprocess arguments, SQL parameters, file paths, template inputs — and prefer the safe API by default.

## 145- How do you write your own context manager, and what's in `contextlib`?

Question 24 covered _using_ `with`; a senior is expected to _author_ context managers and know the toolkit. The protocol is two dunder methods: **`__enter__`** (runs on entry, its return value binds to `as x`) and **`__exit__`** (runs on exit — normally _or_ via exception — guaranteeing cleanup, which is why `with` beats manual try/finally and the unreliable `__del__` from Q135).

```python
class Timer:
    def __enter__(self):
        self.t0 = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.t0
        return False          # False => don't suppress an exception; True would swallow it
```

The subtlety interviewers probe: **`__exit__` returning `True` suppresses the exception**; returning `False`/`None` lets it propagate. `__exit__` always runs, so it's the place to release locks, connections, or transactions.

**The generator style is usually cleaner** — `@contextlib.contextmanager` turns a single-`yield` generator into a context manager, with setup before the `yield` and teardown after (wrap in try/finally so cleanup survives exceptions):

```python
from contextlib import contextmanager

@contextmanager
def transaction(conn):
    tx = conn.begin()
    try:
        yield conn
        tx.commit()
    except Exception:
        tx.rollback()
        raise
```

**`contextlib` toolbox worth naming:** `suppress(Exception)` (a clean "ignore this error"), `closing(obj)` (call `.close()` on exit), `redirect_stdout`/`redirect_stderr`, `nullcontext` (a no-op stand-in for optional CMs), and **`ExitStack`** — the power tool for entering a **dynamic/variable number** of context managers (e.g. opening a list of files) and unwinding them all correctly. And for `asyncio` (Q118) there's the async mirror: **`__aenter__`/`__aexit__`**, **`@asynccontextmanager`**, and **`async with`** — essential for async DB sessions and HTTP clients.

## 146- What does a senior need to know about talking to a database (ORM vs Core, sessions, pooling, transactions, N+1)?

Most services live or die on their database layer, and **SQLAlchemy** is Python's dominant toolkit, so the interview centres there. The first distinction is **Core vs ORM**: **Core** is a Pythonic SQL expression language (you compose queries, rows come back as tuples/mappings); the **ORM** maps Python classes to tables and gives you objects with identity and change-tracking. They share one engine, and mixing them is normal.

**Connection pooling — the performance fundamental.** Opening a DB connection is expensive, so the **engine holds a pool** and hands out/returns connections. A senior can speak to `pool_size`, `max_overflow`, `pool_timeout`, and especially **`pool_pre_ping`** (validate a connection before use so a firewall-dropped or DB-restarted connection doesn't blow up the next request). Getting pool sizing wrong — too small starves throughput, too large exhausts the DB's connection limit — is a classic production incident.

**The Session and the Unit of Work.** The ORM `Session` batches your changes and tracks objects via an **identity map** (one object per primary key per session). The distinctions that matter:

- **`flush`** pushes pending SQL to the DB (so it's visible within the transaction) but doesn't end it; **`commit`** flushes _and_ commits the transaction; **`rollback`** discards it.
- Wrap work in a transaction and keep sessions **short-lived and request-scoped** — a long-lived shared session is a common bug (this repo's `RequestContextMiddleware` attaching `request.state.db` per request reflects that discipline).

**The N+1 query problem** (also raised for GraphQL, Q137): lazily loading a relationship inside a loop fires one query per parent → hundreds of round trips. Fix with **eager loading** (`selectinload`, `joinedload`). Other essentials: **Alembic** for schema **migrations**, **async** drivers (`asyncpg` + SQLAlchemy's async engine) so DB I/O doesn't block the event loop (Q118), and the maturity to know **an ORM isn't always right** — raw parameterised SQL (Q144) or a lighter query builder can be the better tool for complex analytical queries.

## 147- How should logging be done in a production Python service?

The headline a senior states immediately: **use the `logging` module, never `print`.** `print` gives you no levels, no timestamps, no routing, and no way for operators to turn detail up or down. `logging` is a configurable framework built from four pieces: **Loggers** (what you call), **Handlers** (where records go — console, file, syslog, HTTP), **Formatters** (how they're rendered), and **Filters**.

**The idioms that separate juniors from seniors:**

- **Get a module-level logger by name:** `logger = logging.getLogger(__name__)`. This builds the **dotted logger hierarchy** (`myapp.services.db`), so you can raise/lower verbosity per subsystem. Never log through the root logger directly.
- **Configure once, at the application entry point** — typically with `logging.config.dictConfig(...)`. **Libraries must not configure logging**; a well-behaved library only adds a `NullHandler` so it stays silent until the _application_ opts in.
- **Use lazy `%`-style formatting**, not f-strings: `logger.info("user %s did %s", uid, action)`. The string is only interpolated **if that level is enabled**, saving work on suppressed `DEBUG` lines — and it keeps the message template stable for structured/aggregated logs.
- **Log exceptions with the traceback:** inside an `except`, call `logger.exception("failed")` (or `logger.error(..., exc_info=True)`) to capture the stack.

**For real services, go structured.** Emit **JSON logs** (via `python-json-logger` or `structlog`) so a log aggregator (ELK, Loki, Datadog) can index fields, and attach a **correlation/request ID** — often propagated with **`contextvars`** (which, unlike thread-locals, work correctly across `async` tasks, Q118) — so you can trace one request across many log lines. Pitfalls to mention: **duplicate log lines** from adding handlers more than once or from **propagation** to ancestor loggers, and the cost of logging in tight loops. The takeaway: logging is an **operability feature** — design it so problems in production are diagnosable without a redeploy.

## 148- Concurrency in practice: `concurrent.futures`, thread safety, and synchronization primitives

Questions 1, 23, and 119 covered the GIL and _choosing_ a concurrency model; this is the _how_. The modern high-level API is **`concurrent.futures`**, which unifies threads and processes behind one interface: **`ThreadPoolExecutor`** (I/O-bound) and **`ProcessPoolExecutor`** (CPU-bound), both offering `submit()` (returns a **`Future`**) and `map()`, with `as_completed()` to consume results as they finish. Prefer it over hand-managing `Thread`/`Process` objects.

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

with ThreadPoolExecutor(max_workers=8) as pool:
    futures = [pool.submit(fetch, url) for url in urls]
    for f in as_completed(futures):
        result = f.result()     # re-raises any exception from the worker
```

**Thread safety — the misconception to correct:** the GIL does **not** make your code thread-safe. It guarantees a single _bytecode_ runs at a time, but a high-level operation like `counter += 1` is **read-modify-write across several bytecodes**, so two threads can interleave and lose an update. Any **check-then-act** or **compound** operation over shared mutable state is a race.

**The synchronization toolbox** (`threading`): **`Lock`** (mutual exclusion — always use `with lock:`), **`RLock`** (re-entrant, same thread can re-acquire), **`Semaphore`** (limit N concurrent), **`Event`** (signal between threads), **`Condition`** (wait-for-predicate), and **`Barrier`**. But the senior's preferred design is to **avoid shared mutable state altogether**: hand work between threads through a **`queue.Queue`**, which is itself thread-safe, turning locking into a producer/consumer pipeline. Know **deadlock** (two threads each holding a lock the other wants — prevent with consistent lock ordering) and **`threading.local`** for per-thread state.

**Two `ProcessPoolExecutor` gotchas** to mention: arguments and return values must be **picklable** (Q144's pickle caveats apply), and on Windows/macOS-spawn you must guard the entry point with **`if __name__ == "__main__":`** or you'll fork-bomb yourself. And the async equivalent (Q118) lives in `asyncio` — `asyncio.Lock`/`Semaphore`/`Queue` — which coordinate _tasks_ on one thread, not OS threads.

## 149- What is ASGI vs WSGI, and how does a framework like FastAPI use dependency injection?

The foundational split is the **server-to-application interface**. **WSGI** is the classic **synchronous** standard (one request occupies a worker thread/process start to finish) behind Flask and traditional Django. **ASGI** is its **asynchronous** successor: it supports `async` handlers, long-lived connections (WebSockets, SSE), and lets **one worker juggle thousands of concurrent I/O-bound requests** on an event loop (Q118). **FastAPI** (on Starlette) is ASGI; you serve it with **`uvicorn`**, often managed by **`gunicorn`** running multiple uvicorn workers to use all CPU cores. This is exactly this repo's `api` mode.

**Why FastAPI is the modern default:** it's **type-hint driven** — request/response bodies are declared as **Pydantic models** (Q141), so you get validation, serialization, and an **auto-generated OpenAPI/Swagger** spec for free from the same annotations.

**Dependency injection via `Depends`** is FastAPI's signature feature. You declare a dependency as a parameter; FastAPI **resolves and injects** it, caching per-request and unwinding any cleanup:

```python
from fastapi import Depends, FastAPI

async def get_db():
    db = Session()
    try:
        yield db                 # injected into the endpoint
    finally:
        db.close()               # teardown after the response

app = FastAPI()

@app.get("/users/{uid}")
async def read_user(uid: int, db=Depends(get_db)):
    return db.get(User, uid)
```

The wins a senior highlights: dependencies are **reusable and composable** (auth, DB session, pagination, this repo's `auth.dependency`), and **overridable in tests** via `app.dependency_overrides` — which is why the codebase can swap in `BASF_FEDERATION_DEBUG_USER` to bypass auth under test.

**The trap that ties it all together:** in an ASGI app, a **blocking call inside an `async def`** (a synchronous DB driver, `requests`, `time.sleep`, heavy CPU or model inference from Q138) **stalls the entire event loop and every concurrent request**. The fixes: use **async-native libraries** (`httpx`, `asyncpg`), or declare the handler as a plain **`def`** (FastAPI runs it in a threadpool), or offload heavy work to a **process pool or a Celery worker** (this repo's `worker` mode). Rounding out the picture: **middleware** (cross-cutting concerns like CORS and this repo's `RequestContextMiddleware`), **background tasks**, and the **lifespan** hook for startup/shutdown (opening the Mongo/Redis/S3 connections). This layered discipline — thin HTTP handlers, injected dependencies, business logic and I/O pushed into services — is precisely the router → service → helper architecture this project enforces.

## 150- What are the concrete steps to publish a library to PyPI with pip (build/twine), Poetry, or uv?

Questions 92 and 136 covered the _concepts_ — distribution options and the `setup.py`→`pyproject.toml` shift. This is the _procedure_. The key insight that de-mystifies it: **all three tools do the same thing** — turn your project into the two standard artifacts (an **sdist** `.tar.gz` and a **wheel** `.whl`, Q41) and upload them to the same index, **PyPI**. They differ only in ergonomics. So learn the shared pipeline once, then the three command sets.

**The shared pipeline (tool-agnostic):**

1. **Pick a unique, available name** — check `https://pypi.org/project/<name>/`; names are first-come and can't clash.
2. **Create accounts on both PyPI and TestPyPI**, enable 2FA, and create an **API token** (or set up Trusted Publishing, below).
3. **Lay out the project** with a `src/` layout and declare **static metadata in `pyproject.toml`** (PEP 621), plus a `README`, `LICENSE`, and a version:

   ```toml
   [build-system]
   requires = ["hatchling"]          # or setuptools / flit-core / pdm-backend / maturin
   build-backend = "hatchling.build"

   [project]
   name = "mylib"
   version = "0.1.0"
   description = "A short, searchable summary"
   readme = "README.md"
   requires-python = ">=3.12"
   license = "MIT"
   authors = [{ name = "You", email = "you@example.com" }]
   dependencies = ["httpx>=0.27"]
   classifiers = ["Programming Language :: Python :: 3.12"]

   [project.urls]
   Homepage = "https://github.com/you/mylib"

   [project.scripts]
   mycli = "mylib.cli:main"          # entry point -> installs a CLI command
   ```

4. **Build** → produces `dist/*.whl` and `dist/*.tar.gz`.
5. **Verify** — check the metadata, and install the built wheel into a _fresh_ virtualenv to confirm it imports and runs.
6. **Upload to TestPyPI first, then to real PyPI.**

**A — The standards toolchain (`build` + `twine`, the "pip world"):** the most transparent, no extra framework.

```bash
python -m pip install --upgrade build twine
python -m build                                     # -> dist/ (sdist + wheel)
python -m twine check dist/*                         # validate long-description/metadata
python -m twine upload --repository testpypi dist/*  # dry-run on TestPyPI
python -m twine upload dist/*                         # publish to real PyPI
```

Authenticate with an API token: username `__token__`, password `pypi-…` (set `TWINE_USERNAME`/`TWINE_PASSWORD` env vars or a `~/.pypirc`).

**B — Poetry (integrated deps + build + publish):**

```bash
poetry new mylib                 # scaffold (or `poetry init` in an existing project)
poetry version patch             # bump SemVer: 0.1.0 -> 0.1.1
poetry build                     # -> dist/
poetry config pypi-token.pypi pypi-xxxx
poetry publish                   # (add --build to build+publish in one step)
```

**C — uv (the fast, newer all-in-one, Rust-based):**

```bash
uv init --lib mylib              # scaffold a library (pyproject + src layout)
uv build                         # -> dist/ (sdist + wheel)
uv publish --publish-url https://test.pypi.org/legacy/  --token <testpypi-token>   # test
uv publish --token <pypi-token>  # real PyPI (or set UV_PUBLISH_TOKEN)
```

**The cross-cutting essentials a senior stresses:**

- **A version is immutable and single-use.** Once `mylib 0.1.0` is uploaded, PyPI will **never** let you overwrite or re-upload that filename — you must **bump the version** for every release. Follow **SemVer**, keep **one source of truth** for the version (read it at runtime with `importlib.metadata.version("mylib")`), and remember you can _yank_ a bad release but not replace it. This is exactly why you **test on TestPyPI first** — so a mistake doesn't burn a real version number.
- **Trusted Publishing (OIDC) is the modern, secure CI path.** Instead of storing a long-lived API token in CI secrets, you configure PyPI to _trust_ your GitHub Actions/GitLab pipeline; it mints a **short-lived token per run**. The `pypa/gh-action-pypi-publish` action is the standard way. In real projects, **publishing runs in CI on a version tag** — build, test, then publish — not from a laptop.
- **The build backend is your choice** (Q136), independent of the publish tool: `setuptools`, `hatchling`, `flit-core`, `pdm-backend`, or `maturin` for Rust/native extensions. Poetry uses `poetry-core`; uv defaults to `hatchling` but honours whatever `[build-system]` you declare.
- **Metadata quality = a good PyPI page.** Fill `description`, `readme`, `license`, `classifiers`, `requires-python`, `[project.urls]`, and `[project.scripts]`/`[project.entry-points]` for CLIs and plugins.

The takeaway: the mechanics are identical — **`pyproject.toml` → build an sdist + wheel → upload to PyPI**. Pick **one** tool for ergonomics: **`build` + `twine`** for maximum transparency and control, **Poetry** for an integrated dependency-plus-publish workflow, or **uv** for speed and a single modern toolchain — then automate it in CI with **Trusted Publishing** and a tag-triggered release.

## 151- Free-threaded Python (PEP 703, no-GIL) and subinterpreters (PEP 684 and 734): what actually changes for concurrency?

This is the deep end of the GIL thread that runs through Q1, Q2, Q23, and the "how do I pick a concurrency model" question (Q119). For roughly three decades the answer to "can Python threads run CPU-bound code in parallel?" was **no, because of the GIL**. Two _separate_ CPython efforts are now changing that answer, and the senior insight is that they attack the same problem **from opposite ends** — one removes the lock, the other replicates it.

**Free-threaded CPython (PEP 703)** ships as an experimental build starting in 3.13 — the "`t`" ABI (`python3.13t`) — and **removes the GIL entirely**, so multiple threads execute Python bytecode truly in parallel across cores. Keeping reference counting correct without one big lock required real machinery: **biased reference counting** (a cheap fast path for the object's owning thread plus an atomic shared counter), **immortal objects** (PEP 683 — `None`, `True`/`False`, small ints, and interned strings never touch their refcount), per-object locking, and a thread-safe variant of the pymalloc allocator (Q153). The costs are real: single-threaded code gets somewhat slower (the fast-path refcount checks and lost specialization from Q152), **C extensions must be recompiled and audited** for thread-safety because they can no longer assume the GIL serializes them, and it stays opt-in/experimental through 3.13–3.14. But it finally makes plain `threading` a legitimate answer for CPU-bound work.

**Per-interpreter GIL and subinterpreters (PEP 684 for the runtime, PEP 734 for the stdlib API)** take the opposite route: **keep a GIL, but give each subinterpreter its own** so they stop contending. 3.12 moved most interpreter state to be per-interpreter; 3.13 exposes the `interpreters` module and a `concurrent.futures.InterpreterPoolExecutor`. Each subinterpreter is an isolated Python — its own imports, modules, and GIL — closer to `multiprocessing`'s isolation but living **in one process** (no `fork`, no child-process startup). You communicate over **queues/channels** that share only a narrow set of objects rather than passing arbitrary references around.

So the mental model for choosing today refines Q119: **free-threading = shared memory, you manage the locks** (maximum performance, maximum footguns — data races are back), while **subinterpreters = isolated memory, you pass messages** (safer, but with marshaling overhead). For a service like this one, most parallelism is still I/O-bound and is pushed onto **Celery workers** (separate OS processes — the boring, robust answer), but the free-threaded build is why "just use a thread pool" may finally become viable for a CPU-bound endpoint without spawning processes.

**The trap** is assuming "no-GIL makes my existing threaded code faster/parallel." That is only true on the special build **and** only if every C-extension dependency supports it; on a normal build, nothing changes. Worse, removing the GIL **exposes latent races the GIL was accidentally hiding** — a non-atomic `counter += 1` on a shared object, or a check-then-act on a dict — so code that "worked" for years can start corrupting data. The synchronization discipline from Q148 (locks, `queue.Queue`, immutability) stops being optional.

The takeaway: two PEPs, two philosophies — **PEP 703 removes the lock (shared-memory parallelism, bring your own synchronization)** and **PEP 684/734 replicates the lock per interpreter (message-passing isolation inside one process)** — and together they finally give CPython an in-process story for CPU-bound parallelism that used to force you into `multiprocessing`.

## 152- How does CPython execute bytecode? `dis`, the ceval loop, frames, and the specializing adaptive interpreter (PEP 659)

Q85 walked the pipeline (source → AST → bytecode → run) and Q86 covered `__pycache__`. This goes one level deeper: **what actually runs the bytecode**, and why it matters for performance and tracebacks.

**Compilation produces a code object.** The compiler turns each function into a **code object** reachable as `func.__code__`, holding `co_code` (the raw bytecode), `co_consts`, `co_varnames`, `co_names`, the required stack size, and flags. `dis.dis(func)` disassembles it into readable opcodes:

```python
import dis
def f(a, b):
    return a + b
dis.dis(f)
# LOAD_FAST   a
# LOAD_FAST   b
# BINARY_OP   0 (+)
# RETURN_VALUE
```

**A stack machine runs it.** CPython is a **stack-based bytecode virtual machine**: the core is `_PyEval_EvalFrameDefault` in `ceval.c`, a large dispatch loop that reads one instruction at a time and pushes/pops an **evaluation stack**. There are no registers — `a + b` is literally "push `a`, push `b`, pop both and push their sum." That simplicity is why the bytecode is portable and why the interpreter is (relatively) easy to reason about.

**Frames tie calls together.** Each call creates a **frame** capturing the locals, the value stack, the instruction pointer (`f_lasti`), and a link to the caller (`f_back`). That `f_back` chain **is** your traceback, and it's what `sys._getframe()`, `sys.settrace`, debuggers, and profilers walk. Python 3.11 made frames dramatically cheaper — they live lazily as C structs on a per-thread data stack and are only materialized into full Python `frame` objects when something actually needs one — a major reason 3.11 was ~10–60% faster than 3.10.

**PEP 659 — the specializing adaptive interpreter (3.11+)** is the big modern idea: **quickening plus inline caching**. The interpreter observes which _types_ actually flow through a generic opcode and rewrites it in place into a **specialized** form — `BINARY_OP` on two ints becomes an int-add fast path; a `LOAD_ATTR` that keeps hitting the same class layout becomes a cached, guard-checked lookup. If an assumption breaks (a different type shows up), it **deoptimizes** back to the generic opcode. This is adaptive, JIT-_like_ behavior without a full JIT — and 3.13 added an experimental copy-and-patch JIT layered on top.

**Why a senior cares:** it explains _why_ micro-optimizations behave as they do — **monomorphic code** (the same types every call) specializes and runs faster than polymorphic code; it's why `dis` output on modern Python shows adaptive/specialized opcodes; and it demystifies tracebacks and tooling (they walk the frame chain). It also frames the free-threading trade-off in Q151, since specialization interacts with removing the GIL.

The takeaway: CPython compiles to a **code object**, then a **stack machine (`_PyEval_EvalFrameDefault`) executes it frame by frame**, and since 3.11 the **specializing adaptive interpreter** rewrites hot opcodes into type-specialized fast paths (deoptimizing when guards fail) — so `dis`, monomorphic code, and the frame chain are the three concepts to hold when reasoning about performance and stack traces.

## 153- A deeper look at CPython memory: `pymalloc` arenas, pools, and blocks, `tracemalloc`, and diagnosing leaks and fragmentation

Q11 covered the private heap plus refcount/GC, Q90/Q115/Q116 covered the `dict`/`list`/`tuple` layouts, and Q135 covered the cyclic collector. This is the **allocator layer underneath all of them** — the thing that decides where an object's bytes come from.

**CPython does not call `malloc` per object.** It layers allocators: a raw domain (`PyMem_RawMalloc` → the system `malloc`), an object domain, and for small objects a dedicated allocator called **pymalloc (obmalloc)**. Objects **≤ 512 bytes** are served by pymalloc; anything larger goes straight to the system allocator.

**Arenas → pools → blocks.** pymalloc grabs memory from the OS in big **arenas** (256 KiB). Each arena is sliced into **pools** of 4 KiB (one OS page). A pool serves a **single size class** — block sizes are rounded up to a multiple of 8 (16 on 64-bit) bytes — so allocating an object is just a **free-list pop** of a fixed-size block: no syscall and minimal fragmentation _within_ a size class.

**Why memory often doesn't go back to the OS.** An arena is only released when **all** of its pools and blocks are free. A single surviving object can pin an entire 256 KiB arena — the classic **fragmentation** surprise where RSS stays high long after you `del` most of your data. Freed blocks aren't returned to the OS either; they go on a free list to be reused by the same process. This is why "my long-running Python process never gives memory back" is usually _expected_ behavior, not a bug.

**Immortal singletons tie in.** Small ints (−5..256), interned strings, and `None`/`True`/`False` are effectively permanent — and in 3.12+ literally _immortal_ (PEP 683), never refcounted or freed. That's by design: they're shared singletons (the identity gotchas of Q128), so pinning them costs nothing meaningful.

**Tooling to diagnose:**

- `sys.getsizeof(obj)` — the shallow size of one object (it does **not** recurse into contents).
- **`tracemalloc`** — the built-in that snapshots allocations grouped by traceback; the first tool to reach for on a suspected leak because it tells you **what grew between two points**.
- `gc` — `gc.get_objects()`, `gc.get_referrers(obj)` to find who still holds a reference; `gc.set_debug(gc.DEBUG_LEAK)`; the third-party `objgraph` to visualize reference chains.
- OS view via `psutil` (RSS) versus the Python view — the gap between them _is_ the fragmentation/allocator caching described above.

```python
import tracemalloc
tracemalloc.start()
snap1 = tracemalloc.take_snapshot()
# ... run the suspected work ...
snap2 = tracemalloc.take_snapshot()
for stat in snap2.compare_to(snap1, "lineno")[:10]:
    print(stat)      # the biggest growth by source line
```

**"Leaks" in a garbage-collected language are almost always unintended references** (Q135): a module-level cache or list that only ever grows, an `lru_cache` with no `maxsize` pinning large results, a closure or callback that captured `self` and outlived it, or `__del__` on members of a reference cycle. The fixes are `weakref` (Q126), bounded caches, and explicitly breaking cycles.

**Repo-relevant:** a long-running FastAPI or Celery worker that slowly climbs in memory is the textbook case. Wrap a request or task in `tracemalloc` snapshots, look for unbounded caches, and remember that even after you fix the real leak, **RSS may not fall** because of arena fragmentation.

The takeaway: small objects flow through **pymalloc's arena → pool → block hierarchy** (a free-list fast path, no per-object `malloc`), which is fast but means **memory returns to the OS only when a whole arena empties** — so high RSS is frequently fragmentation, while true leaks are lingering references best hunted with **`tracemalloc` snapshots plus `gc` referrer inspection** and fixed with `weakref` and bounded caches.

## 154- Generators as coroutines: `send`, `throw`, `close`, and `yield from` — and how they became `async`/`await`

Q36 and Q37 introduced generators and iterators; Q118 covered asyncio. This connects them, because the senior insight is that **native coroutines are generators grown up** — the `async`/`await` machinery is the generator protocol productized.

**A generator is a two-way, resumable coroutine — not just a lazy iterator.** Beyond `next()`, `yield` is an _expression_ that can receive a value:

- `gen.send(x)` — resume the generator, and the paused `yield` **evaluates to `x`** inside it. `send(None)` is equivalent to `next()`, and you must "prime" a generator with `next()`/`send(None)` before you can send a real value.
- `gen.throw(exc)` — resume by **raising `exc` at the yield point**, which the generator can catch and handle.
- `gen.close()` — raise `GeneratorExit` at the yield point so `finally`/cleanup runs; this is exactly how `contextlib.contextmanager` (Q145) tears down after the `yield`.

```python
def averager():
    total = count = 0
    avg = None
    while True:
        x = yield avg          # receives the value from .send(x)
        total += x
        count += 1
        avg = total / count

a = averager()
next(a)                        # prime it
print(a.send(10))              # 10.0
print(a.send(20))              # 15.0
a.close()                      # raises GeneratorExit inside, runs cleanup
```

**`yield from` (PEP 380)** delegates to a sub-generator: it transparently forwards `send`, `throw`, and `close` to the inner generator **and returns the inner generator's `return` value** (`result = yield from sub()`). Crucially it is _not_ just `for x in sub: yield x` — it wires up the full two-way protocol, which is precisely what you need to _compose_ coroutines out of smaller ones.

**The bridge to async/await.** Historically (3.4), asyncio coroutines literally _were_ generators — you wrote `@asyncio.coroutine` and drove them with `yield from`. Python 3.5 introduced **native coroutines** (`async def`/`await`) as a distinct type, but the underlying machinery is the same: `await` is the successor to `yield from` for driving awaitables, and the **event loop (Q118) repeatedly `.send()`s values into a coroutine and receives back the awaitable it suspended on**. The final result is carried out via `StopIteration.value`. In other words, the event loop is "just" a scheduler that drives many coroutine objects through `send`/`throw`.

Knowing they're generator-derived explains the rest of asyncio: **cancellation** is `coro.throw(CancelledError)` (the same mechanism as `gen.throw`), **cleanup on cancel** runs through `GeneratorExit`/`finally`, and a bare `yield` inside an `async def` produces an **async generator** consumed with `async for`.

**Gotchas:** forgetting to prime a `send`-based coroutine (you'll get `TypeError: can't send non-None value to a just-started generator`); swallowing `GeneratorExit` and then `yield`-ing again (Python raises `RuntimeError: generator ignored GeneratorExit`); and assuming `yield from`/`await` parallelize — they do not. One coroutine runs at a time on the loop; parallelism comes from `asyncio.gather`/`TaskGroup` (Q118, Q148).

The takeaway: a generator is a **two-way, resumable coroutine** — `send` feeds values in, `throw` injects exceptions, `close` triggers cleanup via `GeneratorExit`, and `yield from` composes generators while forwarding all three plus the `return` value — and **`async`/`await` is that exact protocol productized**, with the event loop acting as the scheduler that `.send()`s coroutines forward.

## 155- Customizing classes without a metaclass: `__init_subclass__`, `__set_name__`, and the descriptor protocol in depth

Q120 and Q134 covered metaclasses, Q46 introduced descriptors, and Q32 covered `property`. The senior insight here is that **you rarely actually need a metaclass**: Python 3.6 (PEP 487) added two hooks that cover most real use cases with far less complexity and none of the metaclass-conflict pain.

**`__init_subclass__` — a classmethod on the _parent_ that runs once per subclass definition.** It lets a base class inspect, validate, or **register** its subclasses without a metaclass, and it receives keyword arguments passed in the class header. This is the clean way to build plugin registries or enforce that subclasses declare required attributes:

```python
class PluginBase:
    registry = {}

    def __init_subclass__(cls, /, key, **kwargs):
        super().__init_subclass__(**kwargs)
        PluginBase.registry[key] = cls          # auto-register every subclass

class CsvLoader(PluginBase, key="csv"):
    ...
# PluginBase.registry == {"csv": CsvLoader}
```

**`__set_name__` — the hook that lets a descriptor learn its own attribute name.** When a class body assigns a descriptor to a name, Python calls `descriptor.__set_name__(owner, name)` **at class-creation time**, solving the old annoyance where a descriptor had no idea what attribute it was bound to (and you had to repeat the name). This is exactly how modern field libraries — SQLAlchemy 2.0 mapped columns, Pydantic-style models, dataclass-adjacent field systems — discover their attribute names:

```python
class Field:                                     # a data descriptor
    def __set_name__(self, owner, name):
        self.storage = "_" + name                # learns its own name
    def __get__(self, obj, objtype=None):
        return self if obj is None else getattr(obj, self.storage)
    def __set__(self, obj, value):
        setattr(obj, self.storage, value)
```

**The descriptor protocol, deeper than Q46.** The three hooks are `__get__(self, obj, objtype)`, `__set__(self, obj, value)`, and `__delete__(self, obj)`. The critical distinction is **data descriptor** (defines `__set__` or `__delete__`) versus **non-data descriptor** (only `__get__`), because it drives attribute-lookup precedence:

> **data descriptor on the type > instance `__dict__` > non-data descriptor > plain class attribute.**

That single rule explains a lot: **`property` is a data descriptor, so an instance attribute can't shadow it** (the property always intercepts). A plain **method is a non-data descriptor** — a function's `__get__` is precisely what **binds `self`** — which is why you _can_ override a method on a single instance by assigning to its `__dict__`. And **`functools.cached_property` is a non-data descriptor _on purpose_**: it computes once, writes the result into the instance `__dict__`, and thereafter the instance attribute shadows the descriptor so there's no recompute — a direct, practical consequence of the precedence rules.

**Put together**, a typed/validating field implemented as a descriptor that learns its name via `__set_name__`, collected by a base class that uses `__init_subclass__`, is the _entire_ pattern behind modern data and ORM libraries — achieved with **no metaclass at all**.

**When you still genuinely need a metaclass (Q120/Q134):** when you must change what a class fundamentally _is_ — customizing `__prepare__` (the namespace used while the class body executes), altering the MRO, controlling `isinstance`/`__call__`, or transforming the class object before `__init_subclass__` even runs. Otherwise prefer the hooks: they **compose across multiple base classes** (metaclasses conflict and force you to write a combined metaclass), and they're far easier to read.

The takeaway: reach for **`__init_subclass__`** (react to subclass creation — registries and validation) and **`__set_name__`** (let a descriptor discover its own attribute name) before ever writing a metaclass; combined with the **data vs non-data descriptor precedence** — the rule that explains why `property` beats an instance attribute while `cached_property` deliberately doesn't — these PEP 487 hooks cover the vast majority of "I thought I needed a metaclass" situations with dramatically less complexity.
