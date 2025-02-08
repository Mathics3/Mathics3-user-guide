N
=

`WMA link <https://reference.wolfram.com/language/ref/N.html>`_


:code:`N` [:math:`expr`, :math:`prec`]
    evaluates :math:`expr` numerically with a precision of :math:`prec` digits.





>>> N[Pi, 50]
    =

:math:`3.1415926535897932384626433832795028841971693993751`


>>> N[1/7]
    =

:math:`0.142857`


>>> N[1/7, 5]
    =

:math:`0.14286`



You can manually assign numerical values to symbols.

When you do not specify a precision, :code:`MachinePrecision`  is taken.

>>> N[a] = 10.9
    =

:math:`10.9`


>>> a
    =

:math:`a`



:code:`N`  automatically threads over expressions, except when a symbol has
attributes :code:`NHoldAll` , :code:`NHoldFirst` , or :code:`NHoldRest` .

>>> N[a + b]
    =

:math:`10.9+b`


>>> N[a, 20]
    =

:math:`a`


>>> N[a, 20] = 11;


>>> N[a + b, 20]
    =

:math:`11.000000000000000000+b`


>>> N[f[a, b]]
    =

:math:`f\left[10.9,b\right]`


>>> SetAttributes[f, NHoldAll]


>>> N[f[a, b]]
    =

:math:`f\left[a,b\right]`



The precision can be a pattern:

>>> N[c, p_?(#>10&)] := p


>>> N[c, 3]
    =

:math:`c`


>>> N[c, 11]
    =

:math:`11.000000000`



You can also use :code:`UpSet`  or :code:`TagSet`  to specify values for :code:`N` :

>>> N[d] ^= 5;



However, the value will not be stored in :code:`UpValues` , but
in :code:`NValues`  (as for :code:`Set` ):

>>> UpValues[d]
    =

:math:`\left\{\right\}`


>>> NValues[d]
    =

:math:`\left\{\text{HoldPattern}\left[N\left[d,\text{MachinePrecision}\right]\right]\text{:>}5\right\}`


>>> e /: N[e] = 6;


>>> N[e]
    =

:math:`6.`



Values for :code:`N[:math:`expr`]`  must be associated with the head of :math:`expr`:

>>> f /: N[e[f]] = 7;

    TagSet::tagnfd Tag f not found or too deep for an assigned rule.



You can use :code:`Condition` :

>>> N[g[x_, y_], p_] := x + y * Pi /; x + y > 3


>>> SetAttributes[g, NHoldRest]


>>> N[g[1, 1]]
    =

:math:`g\left[1.,1\right]`


>>> N[g[2, 2]] // InputForm
    =

:math:`8.283185307179586`



The precision of the result is no higher than the precision of the input

>>> N[Exp[0.1], 100]
    =

:math:`1.10517`


>>> % // Precision
    =

:math:`\text{MachinePrecision}`


>>> N[Exp[1/10], 100]
    =

:math:`1.105170918075647624811707826490246668224547194737518718792863289440967966747654302989143318970748654`


>>> % // Precision
    =

:math:`100.`


>>> N[Exp[1.0`20], 100]
    =

:math:`2.7182818284590452354`


>>> % // Precision
    =

:math:`20.`



N can also accept an option "Method". This establishes what is the     prefrered underlying method to compute numerical values:

>>> N[F[Pi], 30, Method->"numpy"]
    =

:math:`F\left[3.14159265358979300000000000000\right]`


>>> N[F[Pi], 30, Method->"sympy"]
    =

:math:`F\left[3.14159265358979323846264338328\right]`


