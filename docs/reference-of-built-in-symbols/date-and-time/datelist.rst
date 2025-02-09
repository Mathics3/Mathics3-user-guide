DateList
========

`WMA link <https://reference.wolfram.com/language/ref/DateList.html>`_


:code:`DateList[]`
    returns the current local time in the form {:math:`year`, :math:`month`, :math:`day`, :math:`hour`, :math:`minute`, :math:`second`}.

:code:`DateList` [:math:`time`]
    returns a formatted date for the number of seconds :math:`time` since epoch Jan 1 1900.

:code:`DateList` [{:math:`y`, :math:`m`, :math:`d`, :math:`h`, :math:`m`, :math:`s`}]
    converts an incomplete date list to the standard representation.





>>> DateList[0]

    =
:math:`\left\{1900,1,1,0,0,0.\right\}`


>>> DateList[3155673600]

    =
:math:`\left\{2000,1,1,0,0,0.\right\}`


>>> DateList[{2003, 5, 0.5, 0.1, 0.767}]

    =
:math:`\left\{2003,4,30,12,6,46.02\right\}`


>>> DateList[{2012, 1, 300., 10}]

    =
:math:`\left\{2012,10,26,10,0,0.\right\}`


>>> DateList["31/10/1991"]

    =
:math:`\left\{1991,10,31,0,0,0.\right\}`


>>> DateList["1/10/1991"]

    DateList::ambig The interpretation of 1/10/1991 is ambiguous.

    =
:math:`\left\{1991,1,10,0,0,0.\right\}`


>>> DateList[{"31/10/91", {"Day", "Month", "YearShort"}}]

    =
:math:`\left\{1991,10,31,0,0,0.\right\}`


>>> DateList[{"31 10/91", {"Day", " ", "Month", "/", "YearShort"}}]

    =
:math:`\left\{1991,10,31,0,0,0.\right\}`



If not specified, the current year assumed

>>> DateList[{"5/18", {"Month", "Day"}}]

    =
:math:`\left\{2025,5,18,0,0,0.\right\}`


