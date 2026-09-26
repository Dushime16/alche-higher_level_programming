The ``0-add_integer`` module

===========================
Import function
===========================

    >>> add_integer = __import__('0-add_integer').add_integer

===========================
Basic addition
===========================

    >>> add_integer(2, 3)
    5

    >>> add_integer(2)
    100

===========================
Floats are cast to int
===========================

    >>> add_integer(2.9, 3.1)
    5

    >>> add_integer(5.7, 2.3)
    7

===========================
Negative numbers
===========================

    >>> add_integer(-2, -3)
    -5

    >>> add_integer(-2.5, 3.9)
    1

===========================
Type errors
===========================

    >>> add_integer("2", 3)
    Traceback (most recent call last):
    TypeError: a must be an integer

    >>> add_integer(2, "3")
    Traceback (most recent call last):
    TypeError: b must be an integer

    >>> add_integer(None)
    Traceback (most recent call last):
    TypeError: a must be an integer

===========================
Edge cases
===========================

    >>> add_integer(0, 0)
    0
