Basic calculations
==================

\Mathics can be used to calculate basic stuff:

>>> 1 + 2
  = 3

To submit a command to \Mathics, press :code:`Shift+Return`  in the Web interface or :code:`Return`  in the console interface. The result will be printed in a new line below your query.

The result of the previous query to \Mathics can be accessed by :code:`%` :

>>> % ^ 2
  = 9

\Mathics understands all basic arithmetic operators and applies the usual operator precedence. Use parentheses when needed:

>>> 1 - 2 * (3 + 5) / 4
  = -3

The multiplication can be omitted:

>>> 1 - 2 (3 + 5) / 4
  = -3
>>> 2 4
  = 8

Powers can be entered using :code:`^` :

>>> 3 ^ 4
  = 81

Integer divisions yield rational numbers:

>>> 6 / 4
  = 3 / 2

To convert the result to a floating point number, apply the function :code:`N` :

>>> N[6 / 4]
  = 1.5

As you can see, functions are applied using square braces :code:`[`  and :code:`]` , in contrast to the common notation of :code:`(`  and :code:`)` . At first hand, this might seem strange, but this distinction between function application and precedence change is necessary to allow some general syntax structures, as you will see later.

\Mathics provides many common mathematical functions and constants, e.g.:

>>> Log[E]
  = 1
>>> Sin[Pi]
  = 0
>>> Cos[0.5]
  = 0.877583

When entering floating point numbers in your query, \Mathics will perform a numerical evaluation and present a numerical result, pretty much like if you had applied :code:`N` .

Of course, \Mathics has complex numbers:

>>> Sqrt[-4]
  = 2 I
>>> I ^ 2
  = -1
>>> (3 + 2 I) ^ 4
  = -119 + 120 I
>>> (3 + 2 I) ^ (2.5 - I)
  = 43.663 + 8.28556 I
>>> Tan[I + 0.5]
  = 0.195577 + 0.842966 I

:code:`Abs`  calculates absolute values:

>>> Abs[-3]
  = 3
>>> Abs[3 + 4 I]
  = 5

\Mathics can operate with pretty huge numbers:

>>> 55! (* Also known as Factorial[55] *)
  = 12696403353658275925965100847566516959580321051449436762275840000000000000

We could easily use a number larger than 55, but the digits will just run off the page.

The precision of numerical evaluation can be set:

>>> N[Pi, 30]
  = 3.14159265358979323846264338328

Division by zero gives an error:

>>> 1 / 0
  = ComplexInfinity

But zero division returns value `:code:`ComplexInfinity`  </doc/reference-of-built-in-symbols/integer-and-number-theoretical-functions/mathematical-constants/complexinfinity>`_ and that can be used as a value:

>>> Cos[ComplexInfinity]
  = Indeterminate

:code:`ComplexInfinity`  is a shorthand though for :code:`DirectedInfinty[]` .

Similarly, expressions using `:code:`Infinity`  </doc/reference-of-built-in-symbols/integer-and-number-theoretical-functions/mathematical-constants/complexinfinity>`_  as a value are allowed and are evaluated:

>>> Infinity + 2 Infinity
  = Infinity

There is also the value, `:code:`Indeterminate`  </doc/reference-of-built-in-symbols/integer-and-number-theoretical-functions/mathematical-constants/indeterminate>`_:

>>> 0 ^ 0
  = Indeterminate
