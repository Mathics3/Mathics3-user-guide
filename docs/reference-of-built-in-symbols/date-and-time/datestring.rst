DateString
==========

`WMA link <https://reference.wolfram.com/language/ref/DateString.html>`_


:code:`DateString[]`
    returns the current local time and date as a string.

:code:`DateString` [:math:`elem`]
    returns the time formatted according to :math:`elems`.

:code:`DateString` [{:math:`e_1`, :math:`e_2`, ...}]
    concatenates the time formatted according to elements :math:`ei`.

:code:`DateString` [:math:`time`]
    returns the date string of an AbsoluteTime.

:code:`DateString` [{:math:`y`, :math:`m`, :math:`d`, :math:`h`, :math:`m`, :math:`s`}]
    returns the date string of a date list specification.

:code:`DateString` [:math:`string`]
    returns the formatted date string of a date string specification.

:code:`DateString` [:math:`spec`, :math:`elems`]
    formats the time in turns of :math:`elems`. Both :math:`spec` and :math:`elems` can take any of the above formats.





The current date and time:

>>> DateString[];


>>> DateString[{1991, 10, 31, 0, 0}, {"Day", " ", "MonthName", " ", "Year"}]
    =

:math:`\text{31 October 1991}`


>>> DateString[{2007, 4, 15, 0}]
    =

:math:`\text{Sun 15 Apr 2007 00:00:00}`


>>> DateString[{1979, 3, 14}, {"DayName", "  ", "Month", "-", "YearShort"}]
    =

:math:`\text{Wednesday  03-79}`



Non-integer values are accepted too:

>>> DateString[{1991, 6, 6.5}]
    =

:math:`\text{Thu 6 Jun 1991 12:00:00}`


