Alphabet
========

`WMA link <https://reference.wolfram.com/language/ref/Alphabet.html>`_

:code:`Alphabet` []
    gives the list of lowercase letters a-z in the English alphabet .

:code:`Alphabet` [:math:`type`]
    gives the alphabet for the language or class :math:`type`.





>>> Alphabet[]
  = {a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z}
>>> Alphabet["German"]
  = {a, ä, b, c, d, e, f, g, h, i, j, k, l, m, n, o, ö, p, q, r, s, ß, t, u, ü, v, w, x, y, z}

Some languages are aliases. "Russian" is the same letter set as "Cyrillic"

>>> Alphabet["Russian"] == Alphabet["Cyrillic"]
  = True
