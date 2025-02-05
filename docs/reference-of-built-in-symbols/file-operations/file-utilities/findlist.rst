FindList
========

`WMA link <https://reference.wolfram.com/language/ref/FindList.html>`_


:code:`FindList` [:math:`file`, :math:`text`]
    returns a list of all lines in :math:`file` that contain :math:`text`.

:code:`FindList` [:math:`file`, {:math:`text_1`, :math:`text_2`, ...}]
    returns a list of all lines in :math:`file` that contain any of the specified           string.

:code:`FindList` [{:math:`file_1`, :math:`file_2`, ...}, ...]
    returns a list of all lines in any of the :math:`filei` that contain the specified           strings.





>>> stream = FindList["ExampleData/EinsteinSzilLetter.txt", "uranium"];

>>> Length[stream]
  = 7
>>> FindList["ExampleData/EinsteinSzilLetter.txt", "uranium", 1]
  = {in manuscript, leads me to expect that the element uranium may be turned into}
