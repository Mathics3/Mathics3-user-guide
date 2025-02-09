Optional
========

`WMA link <https://reference.wolfram.com/language/ref/Optional.html>`_


:code:`Optional` [:math:`pattern`, :math:`default`]
    same as

:code:`:math:`pattern` : :math:`default``
    is a pattern which matches :math:`pattern`, which if omitted
    should be replaced by :math:`default`.





>>> f[x_, y_:1] := {x, y}


>>> f[1, 2]

    =
:math:`\left\{1,2\right\}`


>>> f[a]

    =
:math:`\left\{a,1\right\}`



Note that :code:`:math:`symb` : :math:`pattern``  represents a :code:`Pattern`  object. However, there is no
disambiguity, since :math:`symb` has to be a symbol in this case.

>>> x:_ // FullForm

    =
:math:`\text{Pattern}\left[x, \text{Blank}\left[\right]\right]`


>>> _:d // FullForm

    =
:math:`\text{Optional}\left[\text{Blank}\left[\right], d\right]`


>>> x:_+y_:d // FullForm

    =
:math:`\text{Pattern}\left[x, \text{Plus}\left[\text{Blank}\left[\right], \text{Optional}\left[\text{Pattern}\left[y, \text{Blank}\left[\right]\right], d\right]\right]\right]`



:code:`s_.`  is equivalent to :code:`Optional[s_]`  and represents an optional parameter which, if omitted,
gets its value from :code:`Default` .

>>> FullForm[s_.]

    =
:math:`\text{Optional}\left[\text{Pattern}\left[s, \text{Blank}\left[\right]\right]\right]`


>>> Default[h, k_] := k


>>> h[a] /. h[x_, y_.] -> {x, y}

    =
:math:`\left\{a,2\right\}`


