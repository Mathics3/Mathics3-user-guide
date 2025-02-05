FirstCase
=========

`WMA link <https://reference.wolfram.com/language/ref/FirstCase.html>`_


FirstCase[{:math:`e_1`, :math:`e_2`, ...}, :math:`pattern`]
    gives the first :math:`ei` to match :math:`pattern`, or :math:`Missing["NotFound"]` if none matching pattern is found.

FirstCase[{:math:`e_1`,:math:`e_2`, ...}, :math:`pattern` -> :math:`rhs`]
    gives the value of :math:`rhs` corresponding to the first :math:`ei` to match pattern.

FirstCase[:math:`expr`, :math:`pattern`, :math:`default`]
    gives :math:`default` if no element matching :math:`pattern` is found.

FirstCase[:math:`expr`, :math:`pattern`, :math:`default`, :math:`levelspec`]
    finds only objects that appear on levels specified by :math:`levelspec`.

FirstCase[:math:`pattern`]
    represents an operator form of FirstCase that can be applied to an expression.



