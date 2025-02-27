Clear
=====

`WMA link <https://reference.wolfram.com/language/ref/Clear.html>`_


:code:`Clear` [:math:`symb_1`, :math:`symb_2`, ...]
    clears all values of the given symbols. The arguments can also be given as strings containing symbol names.





>>> x = 2;


>>> Clear[x]


>>> x

    =
:math:`x`


>>> x = 2;


>>> y = 3;


>>> Clear["Global`*"]


>>> x

    =
:math:`x`


>>> y

    =
:math:`y`



:code:`ClearAll`  may not be called for :code:`Protected`  symbols.

>>> Clear[Sin]

    Clear::wrsym Symbol Sin is Protected.



The values and rules associated with built-in symbols will not get lost when applying :code:`Clear` 
(after unprotecting them):

>>> Unprotect[Sin]


>>> Clear[Sin]


>>> Sin[Pi]

    =
:math:`0`



:code:`Clear`  does not remove attributes, messages, options, and default values associated with the symbols. Use :code:`ClearAll`  to do so.

>>> Attributes[r] = {Flat, Orderless};


>>> Clear["r"]


>>> Attributes[r]

    =
:math:`\left\{\text{Flat},\text{Orderless}\right\}`


