OptionsPattern
==============

`WMA link <https://reference.wolfram.com/language/ref/OptionsPattern.html>`_


:code:`OptionsPattern` [:math:`f`]
    is a pattern that stands for a sequence of options given         to a function, with default values taken from :code:`Options[:math:`f`]` .         The options can be of the form :code:`:math:`opt`->:math:`value``  or         :code:`:math:`opt`:>:math:`value`` , and might be in arbitrarily nested lists.

:code:`OptionsPattern` [{:math:`opt_1`->:math:`value_1`, ...}]
    takes explicit default values from the given list. The         list may also contain symbols :math:`f`, for which :code:`Options[:math:`f`]`  is         taken into account; it may be arbitrarily nested.         :code:`OptionsPattern[{}]`  does not use any default values.





The option values can be accessed using :code:`OptionValue` .

>>> f[x_, OptionsPattern[{n->2}]] := x ^ OptionValue[n]


>>> f[x]
    =

:math:`x^2`


>>> f[x, n->3]
    =

:math:`x^3`



Delayed rules as options:

>>> e = f[x, n:>a]
    =

:math:`x^a`


>>> a = 5;


>>> e
    =

:math:`x^5`



Options might be given in nested lists:

>>> f[x, {{{n->4}}}]
    =

:math:`x^4`


