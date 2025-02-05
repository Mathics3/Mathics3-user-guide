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
  = {1, 2}
>>> f[a]
  = {a, 1}

Note that :code:`:math:`symb` : :math:`pattern``  represents a :code:`Pattern`  object. However, there is no
disambiguity, since :math:`symb` has to be a symbol in this case.

>>> x:_ // FullForm
  = Pattern[x, Blank[]]
>>> _:d // FullForm
  = Optional[Blank[], d]
>>> x:_+y_:d // FullForm
  = Pattern[x, Plus[Blank[], Optional[Pattern[y, Blank[]], d]]]

:code:`s_.`  is equivalent to :code:`Optional[s_]`  and represents an optional parameter which, if omitted,
gets its value from :code:`Default` .

>>> FullForm[s_.]
  = Optional[Pattern[s, Blank[]]]
>>> Default[h, k_] := k

>>> h[a] /. h[x_, y_.] -> {x, y}
  = {a, 2}
