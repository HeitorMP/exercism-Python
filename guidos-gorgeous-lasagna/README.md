# Guido's Gorgeous Lasagna

Welcome to Guido's Gorgeous Lasagna on Exercism's Python Track.
If you need help running the tests or submitting your code, check out `HELP.md`.
If you get stuck on the exercise, check out `HINTS.md`, but try and solve it without using those first :)

## Introduction

Python is a [dynamic and strongly][dynamic typing in python] typed [object-oriented][object oriented programming] programming language.
It employs both [duck typing][duck typing] and [gradual typing][gradual typing], via [type hints][type hints].
Imperative, declarative (e.g., functional), and object-oriented programming _styles_ are all supported, but internally [everything in Python is an object][everythings an object].

This exercise introduces 4 major Python language features: Name Assignment (_variables and constants_), Functions (_and the return keyword_), Comments, and Docstrings.


~~~~exercism/note

In general, content, tests, and analyzer tooling for the Python track follow the style conventions outlined in [PEP 8](https://www.python.org/dev/peps/pep-0008/) and [PEP 257](https://www.python.org/dev/peps/pep-0257/) for Python code style, with the additional (strong) suggestion that there be no single letter variable names.

~~~~


## Name Assignment and Re-assignment

In Python, there are no keywords to define variables or constants.
Both are [_names_][facts-and-myths-about-python-names] that help programmers reference values (_objects_) in a program and are written differently only by convention.
On Exercism, [variables][variables] are always written in [`snake_case`][snake case], and _constants_ in `SCREAMING_SNAKE_CASE`.

Names are assigned to values using `=`, or the [_assignment operator_][assignment statements] (`<name> = <value>`).
A name (_variable or constant_) can be re-assigned over its lifetime to different values/object types.

For example, `my_first_variable` can be re-assigned many times using `=`, and can refer to different object types with each re-assignment:

```python
# Assigning my_first_variable to a numeric value.
>>> my_first_variable = 1
>>> print(type(my_first_variable))
<class 'int'>

>>> print(my_first_variable)
1

# Reassigning my_first_variable to a new string value.
>>> my_first_variable = "Now, I'm a string."
>>> print(type(my_first_variable))
<class 'str'>

>>> print(my_first_variable)
"Now, I'm a string."
```


### Constants

Constants are typically defined at a [module][module] level, being values that are accessible outside function or class scope.
Constant names **_can be reassigned to new values_**, but they are _intended_ to be named only once.
Using `SCREAMING_SNAKE_CASE` warns other programmers that these names should not be mutated or reassigned.

```python
# All caps signal that this is intended as a constant.
MY_FIRST_CONSTANT = 16

# Re-assignment will be allowed by the compiler & interpreter,
# but this is VERY strongly discouraged.
# Please don't: MY_FIRST_CONSTANT = "Some other value"
```


## Functions

The keyword `def` begins a [function definition][function definition].
It must be followed by the function name and a parenthesized list of zero or more formal [parameters][parameters].
Parameters can be of several different varieties, and can even [vary][more on functions] in length.

The `def` line is terminated with a colon:

```python
# Function definition.
def my_function_name(parameter, second_parameter):
    <function body>

```


Statements for the _body_ of the function begin on the line following `def` and must be _indented in a block_.
There is no strict indentation amount (_either space **OR** [tab] characters are acceptable_), but [indentation][indentation] must be _consistent_ for all indented statements.


```python
# Function definition on first line.
def add_two_numbers(number_one, number_two):
  print(number_one + number_two)  # Prints the sum of the numbers, and is indented by 2 spaces.

>>> add_two_numbers(3, 4)
7
```


Functions explicitly return a value or object via the [`return`][return] keyword.

```python
# Function definition on first line.
def add_two_numbers(number_one, number_two):
  return number_one + number_two  # Returns the sum of the numbers.

>>> add_two_numbers(3, 4)
7
```


Functions that do not have an explicit `return` expression will return [`None`][none].

```python
# This function will return None.
def add_two_numbers(number_one, number_two):
  result = number_one + number_two

>>> print(add_two_numbers(5, 7))
None
```


While you may choose any indentation depth, _inconsistent_ indentation in your code blocks will raise an error:

```python
# The return statement line does not match the first line indent.
>>> def add_three_numbers_misformatted(number_one, number_two, number_three):
...     result = number_one + number_two + number_three   # Indented by 4 spaces.
...    return result     #this was only indented by 3 spaces
...
...
  File "<stdin>", line 3
    return result
                ^
IndentationError: unindent does not match any outer indentation level
```


### Calling Functions

Functions are [_called_][calls] or invoked using their name followed by `()`.
The number of arguments passed in the parentheses must match the number of parameters in the original function definition.

```python
>>> def number_to_the_power_of(number_one, number_two):
        return number_one ** number_two
...

>>> number_to_the_power_of(3,3)
27
```


A mis-match between the number of parameters and the number of arguments will raise an error:

```python
>>> number_to_the_power_of(4,)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: number_to_the_power_of() missing 1 required positional argument: 'number_two'

```


Calling functions defined inside a class (_methods_) use `<class name>.<method name>(<parameters>)`, otherwise known as dot (.) notation:

```python
# This is an example of a method call of the built in str class.
# Define a variable and assign it to a string.
>>> start_text = "my silly sentence for examples."

# Uppercase the string by calling the upper method from the str class.
>>> str.upper(start_text)
"MY SILLY SENTENCE FOR EXAMPLES."


# Below is an example of a method call of the built in list class.
# Define an empty list
>>> my_list = []

# Add an element to the list by calling the append method from the list class.
>>> my_list.append(start_text)
>>> print(my_list)
["my silly sentence for examples."]
```


## Comments

[Comments][comments] in Python start with a `#` that is not part of a string, and end at line termination.
Unlike many other programming languages, Python **does not support** multi-line comment marks.
Each line of a comment block must start with the `#` character.

Comments are ignored by the interpreter:


```python
# This is a single line comment.

x = "foo"  # This is an in-line comment.

# This is a multi-line
# comment block over multiple lines --
# these should be used sparingly.
```


## Docstrings

The first statement of a function body can optionally be a [_docstring_][docstring], which concisely summarizes the function or object's purpose.
Docstrings are declared using triple double quotes (""") indented at the same level as the code block:


```python

# An example from PEP257 of a multi-line docstring.
def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """

    if imag == 0.0 and real == 0.0:
        return complex_zero

```


Docstrings are read by automated documentation tools and are returned by calling the special attribute `.__doc__` on the function, method, or class name.
They are recommended for programs of any size where documentation is needed, and their conventions are laid out in [PEP257][pep257].

Docstrings can also function as [lightweight unit tests][doctests], which will be covered in a later exercise.


```python
# An example on a user-defined function.
>>> def number_to_the_power_of(number_one, number_two):
        """Raise a number to an arbitrary power.

        :param number_one: int the base number.
        :param number_two: int the power to raise the base number to.
        :return: int - number raised to power of second number

        Takes number_one and raises it to the power of number_two, returning the result.
        """

        return number_one ** number_two
...

# Calling the .__doc__ attribute of the function and printing the result.
>>> print(number_to_the_power_of.__doc__)
Raise a number to an arbitrary power.

    :param number_one: int the base number.
    :param number_two: int the power to raise the base number to.
    :return: int - number raised to power of second number

    Takes number_one and raises it to the power of number_two, returning the result.



# Printing the __doc__ attribute for the built-in type: str.
>>> print(str.__doc__)
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
```

[pep257]: https://www.python.org/dev/peps/pep-0257/
[assignment statements]: https://docs.python.org/3/reference/simple_stmts.html#assignment-statements
[calls]: https://docs.python.org/3/reference/expressions.html#calls
[comments]: https://realpython.com/python-comments-guide/#python-commenting-basics
[docstring]: https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings
[doctests]: https://docs.python.org/3/library/doctest.html
[duck typing]: https://en.wikipedia.org/wiki/Duck_typing
[dynamic typing in python]: https://stackoverflow.com/questions/11328920/is-python-strongly-typed
[everythings an object]: https://docs.python.org/3/reference/datamodel.html
[facts-and-myths-about-python-names]: https://nedbatchelder.com/text/names.html
[function definition]: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
[gradual typing]: https://en.wikipedia.org/wiki/Gradual_typing
[indentation]: https://docs.python.org/3/reference/lexical_analysis.html#indentation
[module]: https://docs.python.org/3/tutorial/modules.html
[more on functions]: https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
[none]: https://docs.python.org/3/library/constants.html
[object oriented programming]: https://en.wikipedia.org/wiki/Object-oriented_programming
[parameters]: https://docs.python.org/3/glossary.html#term-parameter
[return]: https://docs.python.org/3/reference/simple_stmts.html#return
[snake case]: https://en.wikipedia.org/wiki/Snake_case
[type hints]: https://docs.python.org/3/library/typing.html
[variables]: https://realpython.com/python-variables/

## Instructions

You're going to write some code to help you cook a gorgeous lasagna from your favorite cookbook.

You have five tasks, all related to cooking your recipe.

## 1. Define expected bake time in minutes

Define an `EXPECTED_BAKE_TIME` constant that returns how many minutes the lasagna should bake in the oven.
According to your cookbook, the Lasagna should be in the oven for 40 minutes:

```python
>>> import lasagna
>>> lasagna.EXPECTED_BAKE_TIME
40
```

## 2. Calculate remaining bake time in minutes

Implement the `bake_time_remaining()` function that takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake based on the `EXPECTED_BAKE_TIME`.

```python
>>> from lasagna import bake_time_remaining
>>> bake_time_remaining(30)
10
```

## 3. Calculate preparation time in minutes

Implement the `preparation_time_in_minutes()` function that takes the number of layers you want to add to the lasagna as an argument and returns how many minutes you would spend making them.
Assume each layer takes 2 minutes to prepare.

```python
>>> from lasagna import preparation_time_in_minutes
>>> preparation_time_in_minutes(2)
4
```

## 4. Calculate total elapsed cooking time (prep + bake) in minutes

Implement the `elapsed_time_in_minutes()` function that has two parameters: `number_of_layers` (_the number of layers added to the lasagna_) and `elapsed_bake_time` (_the number of minutes the lasagna has been baking in the oven_).
This function should return the total number of minutes you've been cooking, or the sum of your preparation time and the time the lasagna has already spent baking in the oven.

```python
>>> from lasagna import elapsed_time_in_minutes
>>> elapsed_time_in_minutes(3, 20)
26
```

## 5. Update the recipe with notes

Go back through the recipe, adding notes in the form of function docstrings.

```python
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
```

## Source

### Created by

- @BethanyG