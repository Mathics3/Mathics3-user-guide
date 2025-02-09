Alphabet
========

`WMA link <https://reference.wolfram.com/language/ref/Alphabet.html>`_

:code:`Alphabet` []
    gives the list of lowercase letters a-z in the English alphabet .

:code:`Alphabet` [:math:`type`]
    gives the alphabet for the language or class :math:`type`.





>>> Alphabet[]

    =
:math:`\left\{\text{a},\text{b},\text{c},\text{d},\text{e},\text{f},\text{g},\text{h},\text{i},\text{j},\text{k},\text{l},\text{m},\text{n},\text{o},\text{p},\text{q},\text{r},\text{s},\text{t},\text{u},\text{v},\text{w},\text{x},\text{y},\text{z}\right\}`


>>> Alphabet["German"]

    =
:math:`\left\{\text{a},\text{ä},\text{b},\text{c},\text{d},\text{e},\text{f},\text{g},\text{h},\text{i},\text{j},\text{k},\text{l},\text{m},\text{n},\text{o},\text{ö},\text{p},\text{q},\text{r},\text{s},\text{ß},\text{t},\text{u},\text{ü},\text{v},\text{w},\text{x},\text{y},\text{z}\right\}`



Some languages are aliases. "Russian" is the same letter set as "Cyrillic"

>>> Alphabet["Russian"] == Alphabet["Cyrillic"]

    =
:math:`\text{True}`


