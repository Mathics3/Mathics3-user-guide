FileNames
=========

`WMA link <https://reference.wolfram.com/language/ref/FileNames.html>`_


:code:`FileNames[]`
    Returns a list with the filenames in the current working folder.

:code:`FileNames` [:math:`form`]
    Returns a list with the filenames in the current working folder that matches with :math:`form`.

:code:`FileNames` [{:math:`form_1`, :math:`form_2`, ...}]
    Returns a list with the filenames in the current working folder that matches with one of :math:`form_1`, :math:`form_2`, ....

:code:`FileNames` [{:math:`form_1`, :math:`form_2`, ...},{:math:`dir_1`, :math:`dir_2`, ...}]
    Looks into the directories :math:`dir_1`, :math:`dir_2`, ....

:code:`FileNames` [{:math:`form_1`, :math:`form_2`, ...},{:math:`dir_1`, :math:`dir_2`, ...}]
    Looks into the directories :math:`dir_1`, :math:`dir_2`, ....

:code:`FileNames` [{:math:`forms`, :math:`dirs`, :math:`n`]
    Look for files up to the level :math:`n`.





>>> SetDirectory[$InstallationDirectory <> "/autoload"];


>>> FileNames["*.m", "formats"]//Length
    =

:math:`0`


>>> FileNames["*.m", "formats", 3]//Length
    =

:math:`14`


>>> FileNames["*.m", "formats", Infinity]//Length
    =

:math:`14`


