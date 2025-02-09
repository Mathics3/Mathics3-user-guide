WordCloud
=========

`WMA link <https://reference.wolfram.com/language/ref/WordCloud.html>`_


:code:`WordCloud` [{:math:`word_1`, :math:`word_2`, ...}]
    Gives a word cloud with the given list of words.

:code:`WordCloud` [{:math:`weight_1` -> :math:`word_1`, :math:`weight_2` -> :math:`word_2`, ...}]
    Gives a word cloud with the words weighted using the given weights.

:code:`WordCloud` [{:math:`weight_1`, :math:`weight_2`, ...} -> {:math:`word_1`, :math:`word_2`, ...}]
    Also gives a word cloud with the words weighted using the given weights.

:code:`WordCloud` [{{:math:`word_1`, :math:`weight_1`}, {:math:`word_2`, :math:`weight_2`}, ...}]
    Gives a word cloud with the words weighted using the given weights.





>>> WordCloud[StringSplit[Import["ExampleData/EinsteinSzilLetter.txt", CharacterEncoding->"UTF8"]]]

    =
.. image:: tmpsrxzf782.png
    :align: center



>>> WordCloud[Range[50] -> ToString /@ Range[50]]

    =
.. image:: tmptb77rlq4.png
    :align: center



