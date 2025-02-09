Formatting Output
=================

The way results are formatted for output in \Mathics is rather sophisticated, compatibility with \Mathematica is one of the design goals. It can be summed up in the following procedure:


1. The result of the query is calculated.

2. The result is stored in :code:`Out`  (which :code:`%`  is a shortcut for).

3. Any :code:`Format`  rules for the desired output form are applied to the result. In the console version of \Mathics, the result is formatted as :code:`OutputForm` ; :code:`MathMLForm`  for the :code:`StandardForm`  is used in the interactive Web version; and :code:`TeXForm`  for the :code:`StandardForm`  is used to generate the \LaTeX version of this documentation.

4. :code:`MakeBoxes`  is applied to the formatted result, again given either :code:`OutputForm` , :code:`MathMLForm` , or :code:`TeXForm`  depending on the execution context of \Mathics. This yields a new expression consisting of "box constructs".

5. The boxes are turned into an ordinary string and displayed in the console, sent to the browser, or written to the documentation \LaTeX file.



As a consequence, there are various ways to implement your own formatting strategy for custom objects.

You can specify how a symbol shall be formatted by assigning values to :code:`Format` :

>>> Format[x] = "y";


>>> x

    =
:math:`\text{y}`



This will apply to :code:`MathMLForm` , :code:`OutputForm` , :code:`StandardForm` , :code:`TeXForm` , and :code:`TraditionalForm` .

>>> x // InputForm

    =
:math:`x`



You can specify a specific form in the assignment to :code:`Format` :

>>> Format[x, TeXForm] = "z";


>>> x // TeXForm

    =
:math:`\text{$\backslash$text\{z\}}`



Special formats might not be very relevant for individual symbols, but rather for custom functions (objects):

>>> Format[r[args___]] = "<an r object>";


>>> r[1, 2, 3]

    =
:math:`\text{<an r object>}`



You can use several helper functions to format expressions:

:code:`Infix` [:math:`expr`, :math:`op`]
    formats the arguments of :math:`expr` with infix operator :math:`op`.

:code:`Prefix` [:math:`expr`, :math:`op`]
    formats the argument of :math:`expr` with prefix operator :math:`op`.

:code:`Postfix` [:math:`expr`, :math:`op`]
    formats the argument of :math:`expr` with postfix operator :math:`op`.

:code:`StringForm` [:math:`form`, :math:`arg1`, :math:`arg2`, ...]
    formats arguments using a format string.





>>> Format[r[args___]] = Infix[{args}, "~"];


>>> r[1, 2, 3]

    =
:math:`1\sim{}2\sim{}3`


>>> StringForm["`1` and `2`", n, m]

    =
:math:`n\text{ and }m`



There are several methods to display expressions in 2-D:

:code:`Row[{...}]`
    displays expressions in a row.

:code:`Grid[{{...}}]`
    displays a matrix in two-dimensional form.

:code:`Subscript` [:math:`expr`, :math:`i_1`, :math:`i_2`, ...]
    displays :math:`expr` with subscript indices :math:`i_1`, :math:`i_2`, ...

:code:`Superscript` [:math:`expr`, :math:`exp`]
    displays :math:`expr` with superscript (exponent) :math:`exp`.





>>> Grid[{{a, b}, {c, d}}]

    =
:math:`\begin{array}{cc} a & b\\ c & d\end{array}`


>>> Subscript[a, 1, 2] // TeXForm

    =
:math:`\text{a\_\{1,2\}}`



If you want even more low-level control over expression display, override :code:`MakeBoxes` :

>>> MakeBoxes[b, StandardForm] = "c";


>>> b

    =
:math:`c`



This will even apply to :code:`TeXForm` , because :code:`TeXForm`  implies :code:`StandardForm` :

>>> b // TeXForm

    =
:math:`c`



Except some other form is applied first:

>>> b // OutputForm // TeXForm

    =
:math:`b`



:code:`MakeBoxes`  for another form:

>>> MakeBoxes[b, TeXForm] = "d";


>>> b // TeXForm

    =
:math:`d`



You can cause a much bigger mess by overriding :code:`MakeBoxes`  than by sticking to :code:`Format` , e.g. generate invalid XML:

>>> MakeBoxes[c, MathMLForm] = "<not closed";


>>> c // MathMLForm

    =
:math:`\text{<not closed}`



However, this will not affect formatting of expressions involving :code:`c` :

>>> c + 1 // MathMLForm

    =
:math:`\text{<math display="block"><mrow><mn>1</mn> <mo>+</mo> <mi>c</mi></mrow></math>}`



That's because :code:`MathMLForm`  will, when not overridden for a special case, call :code:`StandardForm`  first.
:code:`Format`  will produce escaped output:

>>> Format[d, MathMLForm] = "<not closed";


>>> d // MathMLForm

    =
:math:`\text{<math display="block"><mtext>\&lt;not\&nbsp;closed</mtext></math>}`


>>> d + 1 // MathMLForm

    =
:math:`\text{<math display="block"><mrow><mn>1</mn> <mo>+</mo> <mtext>\&lt;not\&nbsp;closed</mtext></mrow></math>}`



For instance, you can override :code:`MakeBoxes`  to format lists in a different way:

>>> MakeBoxes[{items___}, StandardForm] := RowBox[{"[", Sequence @@ Riffle[MakeBoxes /@ {items}, " "], "]"}]


>>> {1, 2, 3}

    =
:math:`\left[1 2 3\right]`


>>> {1, 2, 3} // TeXForm
    = \left[1 2 3\right]`


However, this will not be accepted as input to \Mathics anymore:

>>> [1 2 3]

    Syntax::sntxb Expression cannot begin with "[1 2 3]" (line 1 of "").


>>> Clear[MakeBoxes]



By the way, :code:`MakeBoxes`  is the only built-in symbol that is not protected by default:

>>> Attributes[MakeBoxes]

    =
:math:`\left\{\text{HoldAllComplete}\right\}`



:code:`MakeBoxes`  must return a valid box construct:

>>> MakeBoxes[squared[args___], StandardForm] := squared[args] ^ 2


>>> squared[1, 2]

>>> squared[1, 2] // TeXForm


=

The desired effect can be achieved in the following way:

>>> MakeBoxes[squared[args___], StandardForm] := SuperscriptBox[RowBox[{MakeBoxes[squared], "[", RowBox[Riffle[MakeBoxes[#]& /@ {args}, ","]], "]"}], 2]


>>> squared[1, 2]

    =
:math:`\text{squared}\left[1,2\right]^2`


>>> squared[1, 2] // TeXForm
    = \text{squared}\left[1,2\right]^2`


You can view the box structure of a formatted expression using :code:`ToBoxes` :

>>> ToBoxes[m + n]

    =
:math:`\text{RowBox}\left[\left\{\text{m},\text{+},\text{n}\right\}\right]`



The list elements in this :code:`RowBox`  are strings, though string delimiters are not shown in the default output form:

>>> InputForm[%]

    =
:math:`\text{RowBox}\left[\left\{\text{\`{}\`{}m''}, \text{\`{}\`{}+''}, \text{\`{}\`{}n''}\right\}\right]`


