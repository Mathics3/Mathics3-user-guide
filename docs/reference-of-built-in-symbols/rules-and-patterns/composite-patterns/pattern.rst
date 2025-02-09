Pattern
=======

`WMA link <https://reference.wolfram.com/language/ref/Pattern.html>`_


:code:`Pattern` [:math:`symb`, :math:`pat`]
    same as

:math:`symb` :code:`:`  :math:`pat`
    assigns the name :math:`symb` to the pattern :math:`pat`.

:math:`symb`:code:`_` :math:`head`
    is equivalent to :math:`symb`:code:` : _` :math:`head` (accordingly with :code:`__`          and :code:`___` ).

:math:`symb`:code:` : ` :math:`pat`:code:` : ` :math:`default`
    is a pattern with name :math:`symb` and default value :math:`default`,         equivalent to :code:`Optional` [:math:`pat` : :math:`symb`, :math:`default`].





>>> FullForm[a_b]

    =
:math:`\text{Pattern}\left[a, \text{Blank}\left[b\right]\right]`


>>> FullForm[a:_:b]

    =
:math:`\text{Optional}\left[\text{Pattern}\left[a, \text{Blank}\left[\right]\right], b\right]`



:code:`Pattern`  has attribute :code:`HoldFirst` , so it does not evaluate its name:

>>> x = 2

    =
:math:`2`


>>> x_

    =
:math:`\text{x\_}`



Nested :code:`Pattern`  assigns multiple names to the same pattern. Still,     the last parameter is the default value.

>>> f[y] /. f[a:b,_:d] -> {a, b}

    =
:math:`f\left[y\right]`



This is equivalent to:

>>> f[a] /. f[a:_:b] -> {a, b}

    =
:math:`\left\{a,b\right\}`



:code:`FullForm` :

>>> FullForm[a:b:c:d:e]

    =
:math:`\text{Optional}\left[\text{Pattern}\left[a, b\right], \text{Optional}\left[\text{Pattern}\left[c, d\right], e\right]\right]`


>>> f[] /. f[a:_:b] -> {a, b}

    =
:math:`\left\{b,b\right\}`


