AbsoluteTime
============

`WMA link <https://reference.wolfram.com/language/ref/AbsoluteTime.html>`_


:code:`AbsoluteTime[]`
    gives the local time in seconds since epoch January 1, 1900, in your           time zone.

:code:`AbsoluteTime` [{:math:`y`, :math:`m`, :math:`d`, :math:`h`, :math:`m`, :math:`s`}]
    gives the absolute time specification corresponding to a date list.

:code:`AbsoluteTime` [":math:`string`"]
    gives the absolute time specification for a given date string.

:code:`AbsoluteTime` [{":math:`string`",{:math:`e_1`, :math:`e_2`, ...}}]
    takgs the date string to contain the elements ":math:`ei`".





>>> AbsoluteTime[]

    =
:math:`3.94805\text{*${}^{\wedge}$}9`


>>> AbsoluteTime[{2000}]

    =
:math:`3155673600`


>>> AbsoluteTime[{"01/02/03", {"Day", "Month", "YearShort"}}]

    =
:math:`3253046400`


>>> AbsoluteTime["6 June 1991"]

    =
:math:`2885155200`


>>> AbsoluteTime[{"6-6-91", {"Day", "Month", "YearShort"}}]

    =
:math:`2885155200`


