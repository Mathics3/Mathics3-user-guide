FromCharacterCode
=================

`WMA link <https://reference.wolfram.com/language/ref/FromCharacterCode.html>`_


:code:`FromCharacterCode` [:math:`n`]
    returns the character corresponding to Unicode codepoint :math:`n`.

:code:`FromCharacterCode` [{:math:`n_1`, :math:`n_2`, ...}]
    returns a string with characters corresponding to :math:`n_i`.

:code:`FromCharacterCode` [{{:math:`n_{11}`, :math:`n_{12}`, ...}, {:math:`n_{21}`, :math:`n_{22}`, ...}, ...}]
    returns a list of strings.





>>> FromCharacterCode[100]
  = d
>>> FromCharacterCode[228, "ISO8859-1"]
  = ä
>>> FromCharacterCode[{100, 101, 102}]
  = def
>>> ToCharacterCode[%]
  = {100, 101, 102}
>>> FromCharacterCode[{{97, 98, 99}, {100, 101, 102}}]
  = {abc, def}
>>> ToCharacterCode["abc 123"] // FromCharacterCode
  = abc 123
