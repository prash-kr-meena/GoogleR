## DsAlgo Resources

#### Recursion & Backtracking

* [Difference b/w recursion and backtracking](https://stackoverflow.com/a/26671095)
* [backtracking](https://www.cis.upenn.edu/~matuszek/cit594-2012/Pages/backtracking.html)
* [Backtracking - Wikipedia](https://en.wikipedia.org/wiki/Backtracking)
* [Iteration, Recursion & Recursive Backtracking](https://sites.fas.harvard.edu/~cscie119/lectures/recursion.pdf) <br>
  Recursive Backtracking in General - Page 22

The idea is that in backtracking, some candidates are abandoned, they are explored first, but once found it did not land
us to correct result we go back to that state and reject that candidate, and choose a different candidate for exploring
<br>
With this, problem like subset_sum_k would then be a backtracking problem I am little confused will see -> Once Aditya
teaches this topic - For now what i have done is clear to me, what we do by making input-ouput diagrams

#### Stack

Learning Stacks from Aditya Verma

## Code Resource

#### Using list as stack

* **POP**  `list.pop()`            Remove element from end
* **PUSH**  `list.append()`        Add element from end
* **TOP/PEEK**  `list[-1]`         Get last element
* **SIZE**  `len(list)`            Get the size

## Python Resources

* [Why Pycharm showing warning about **"Shadows name xyz from outer
  scope"**](https://stackoverflow.com/questions/31575659/shadows-name-xyz-from-outer-scope)
* [Medium : Understanding if ```__name__ == "__main__"``` in Python](https://medium.com/python-features/understanding-if-name-main-in-python-a37a3d4ab0c3)
* [Python 3 has ```float('inf')``` and ```Decimal('Infinity')``` but no ```int('inf')``` ?](https://stackoverflow.com/questions/24587994/infinite-integer-in-python)
* [Python program to convert a list to string](https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/)
* [```swapcase()``` method](https://www.geeksforgeeks.org/python-string-swapcase/)
* [Python 3 String justification  ```ljust()```, ```rjust()```, ```center()```](https://www.geeksforgeeks.org/python-string-ljust-rjust-center/)
* [PythonReal - Itertools](https://realpython.com/python-itertools/#what-is-itertools-and-why-should-you-use-it)
* [List changes unexpectedly after assignment. How do I clone or copy it to prevent this?](https://stackoverflow.com/questions/2612802/list-changes-unexpectedly-after-assignment-how-do-i-clone-or-copy-it-to-prevent) _
  Check Top 2 Answers_
    * 3 Ways
        1. You can use the builtin `list.copy()` method
           <br> `new_list = old_list.copy()`
        2. You can slice it
           <br> `new_list = old_list[:]`
        3. You can use the built in `list()` function
           <br> `new_list = list(old_list)`
        4. You can do List Comprehension
           <br> `[i for i in old_list]`
* [Convert int to ASCII and back in Python](https://stackoverflow.com/questions/3673428/convert-int-to-ascii-and-back-in-python)
  -> [Top Answer](https://stackoverflow.com/a/3673447)
* [Error: RuntimeError: Set changed size during iteration](https://discover.cs.ucsb.edu/commonerrors/error/1008.xml)
* [Method Chaining In Python](https://www.tutorialspoint.com/Explain-Python-class-method-chaining) `Method_Chaining.py`
* [Ways to remove i’th character from string in Python](https://www.geeksforgeeks.org/ways-to-remove-ith-character-from-string-in-python/)
    - Naive
    - String Slicing + Concatenation ✅
    - `str.join()` & list comprehension
* [Enumerate in python - Programiz](https://www.programiz.com/python-programming/methods/built-in/enumerate)
* [Getters & Setter in Python , property method , `@property` Decorator](https://www.geeksforgeeks.org/getter-and-setter-in-python/)
* [How to iterate through two lists in parallel?  `zip()`](https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel) <br>
  checkout the `Maximum_Area_Histogram.py` to see the use of `zip()` in `list-enumeration`
* [`sorted()` method in python, How to provide custom sorting logic](https://www.programiz.com/python-programming/methods/built-in/sorted)
    - Note :    it is not an in-place, ie it doesn't actually change the underlying iterable <br> and returns the new
      sorted iterable
    - `sorted(iterable, key=None, reverse=False)`   key and revers are **optional**
    - In case of list there exists a method `sort()` which is actually inplace, and doesn't return anything
    - The`key` parameter, is actually a function, that you can provide to give your own implementation of the `sorted()`
      method <br>
      Based on the returned value of the `key`Z function, you can sort the given iterable.
    - [Sorted() function in Python - GFG](https://www.geeksforgeeks.org/sorted-function-python/)

* [Python Anonymous/Lambda Function](https://www.programiz.com/python-programming/anonymous-function)
    - syntax : `lambda arguments: expression`
    - Lambda functions can have any number of arguments but only one expression.
    - The expression is evaluated and returned.
    - Lambda functions can be used wherever function objects are required
    - In Python, we generally use it as an argument to a **higher-order function** (a function that takes in other
      functions as arguments).
    - Lambda functions are used along with built-in functions like `filter()`, `map()` etc.
      > check out the example for `filter()` and `map()` using lambda function above

* [Python `map()`](https://www.programiz.com/python-programming/methods/built-in/map)
* [Python `filter()`](https://www.programiz.com/python-programming/methods/built-in/filter)
    - You can see Iterators as just easy list comprehension (list, tuple, set etc) statement
* [Tuples in python - Programiz](https://www.programiz.com/python-programming/tuple)
  <br>[Python Tuple Operations](https://note.nkmk.me/en/python-tuple-operation)
    - What are the advantages of Tuple over List
* [How to sort a set in python?](https://stackoverflow.com/questions/55389165/how-to-sort-a-set-in-python)  **You
  can't**
* [Advanced Sorting in Python Using Lambdas and Custom Functions](https://medium.com/better-programming/advanced-sorting-in-python-using-lambdas-and-custom-functions-410b5780fb07)
* [Magic Methods `__init__` `__lt__`](https://blog.cambridgespark.com/magic-methods-a8d93dc55012) **Great Article** -
  With Implementation examples
* [Python Heapq Module, Using ith with primitive and complex typ of object](https://towardsdatascience.com/introduction-to-python-heapq-module-53534feda625)
* [Python heapq Module: Using heapq to Build Priority Queues in Python](https://www.askpython.com/python-modules/python-heapq-module)
* [Making max heap for Primitive type (by negating the values)](https://www.geeksforgeeks.org/max-heap-in-python/)

- In case of objects, you can overload the `__lt__` method
- But for primitive types we would require to either
    1. wrap it in an object and implement `__lt__`
    2. or we can multiply it by -1

* How to traverse a python dictionary