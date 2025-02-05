$MaxLengthIntStringConversion
=============================

`Python 3.11 Integer string conversion length limitation <https://docs.python.org/3.11/library/stdtypes.html#int-max-str-digits>`_

:code:`$MaxLengthIntStringConversion`
    A positive system integer that fixes the largest size of the string that           can appear when converting an :code:`Integer`  value into a :code:`String` . When the           string value is too large, then the middle of the integer contains           an indication of the number of digits elided inside << >>.
    
    If :code:`$MaxLengthIntStringConversion`  is set to 0, there is no           bound. Aside from 0, 640 is the smallest value allowed.
    
    The initial value can be set via environment variable           :code:`DEFAULT_MAX_STR_DIGITS` . If that is not set,           the default value is 7000.





Although Mathics3 can represent integers of arbitrary size, when it formats     the value for display, there can be nonlinear behavior in printing the decimal string     or converting it to a :code:`String` .

Python, in version 3.11 and up, puts a default limit on the size of     the number of digits allows when converting a large integer into     a string.

Show the default value of :code:`$MaxLengthIntStringConversion` :

>>> $MaxLengthIntStringConversion
  = ...

500! is a 1135-digit number:

>>> 500! //ToString//StringLength
  = ...

We first set :code:`$MaxLengthIntStringConversion`  to the smallest value allowed,     so that we can see the truncation of digits in the middle:

>>> $MaxLengthIntStringConversion = 640
  = ...

Note that setting :code:`$MaxLengthIntStringConversion`  has an effect only on Python 3.11 and later;
Pyston 2.x however ignores this.

Now when we print the string value of 500! and Pyston 2.x is not used,     the middle digits are removed:

>>> 500!
  = ...

To see this easier, manipulate the result as :code:`String` :

>>> bigFactorial = ToString[500!]; StringTake[bigFactorial, {310, 330}]
  = ...

The <<501>> indicates that 501 digits have been omitted in the string conversion.

Other than 0, an :code:`Integer`  value less than 640 is not accepted:

>>> $MaxLengthIntStringConversion = 10
  = ...
