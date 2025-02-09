Precision and Accuracy
======================

\Mathics handles relative and absolute uncertainty in numerical quantities. The `<precision>`_ or relative accuracy, is set by adding a RawBackquote character (:code:``` ) and the number of digits of precision in the mantissa. For example:

>>> 3.1416`3

    =
:math:`3.14`



Above, two decimal places are shown in the output after the decimal point, but three places of precision are stored.

The relative uncertainty of :code:`3.1416`3`  is 10^-3. It is numerically equivalent, in three places after the decimal point, to 3.1413`4:

>>> 3.1416`3 == 3.1413`4

    =
:math:`\text{True}`



We can get the precision of the number by using the \Mathics Built-in function `:code:`Precision`  </doc/reference-of-built-in-symbols/atomic-elements-of-expressions/representation-of-numbers/precision>`_:

>>> Precision[3.1413`4]

    =
:math:`4.`



While 3.1419 is not the closest approximation to Pi in 4 digits after the decimal point (or with precision 4), for 3 digits of precision it is:

>>> Pi == 3.141987654321`3

    =
:math:`\text{True}`



The absolute accuracy of a number is set by adding two RawBackquotes :code:````  and the number digits.

For example:

>>> 13.1416``4

    =
:math:`13.142`



is a number having an absolute uncertainty of :math:`10^-4`.

This number is numerically equivalent to :code:`13.1413``4` :

>>> 13.1416``4 == 13.1413``4

    =
:math:`\text{True}`



The absolute accuracy for the value 0 is a fixed-precision Real number:

>>> 0``4

    =
:math:`0.0000`



See also `Accuracy and precision <https://en.wikipedia.org/wiki/Accuracy_and_precision>`_.