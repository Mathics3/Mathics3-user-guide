Precision
=========

`Precision <https://en.wikipedia.org/wiki/Accuracy_and_precision>`_ `WMA link <https://reference.wolfram.com/language/ref/Precision.html>`_


:code:`Precision` [:math:`expr`]
    examines the number of significant digits of :math:`expr`.





*Note that the result could be slightly different than the obtained     in WMA, due to differences in the internal representation of the real numbers.*

The precision of an exact number, e.g., an Integer, is :code:`Infinity` :

>>> Precision[1]

    =
:math:`\infty`



A fraction is an exact number too, so its Precision is :code:`Infinity` :

>>> Precision[1/2]

    =
:math:`\infty`



Numbers entered in the form :math:`digits``:math:`p` are taken to have precision :math:`p`:

>>> Precision[1.23`10]

    =
:math:`10.`



Precision of a machine‐precision number is :code:`MachinePrecision` :

>>> Precision[0.5]

    =
:math:`\text{MachinePrecision}`



In compound expressions, the :code:`Precision`  is fixed by the number with     the lowest :code:`Precision` :

>>> Precision[{{1, 1.`},{1.`5, 1.`10}}]

    =
:math:`5.`



In general, :code:`Accuracy` [:math:`z`] == :code:`Precision` [:math:`z`] + :code:`Log` [:math:`z`]     for non-zero Real values:

>>> (Accuracy[z] == Precision[z] + Log[z])/.z-> 37.`

    =
:math:`\text{True}`



Following WMA, values in Machine Real representation starting with :code:`0.`  are values are special:

>>> Precision[0.]

    =
:math:`\text{MachinePrecision}`



On the other hand, for a Precision Real with fixed accuracy, the precision is evaluated to :code:`0.` :

>>> Precision[0.``3]

    =
:math:`0.`



See also `:code:`Accuracy`  </doc/reference-of-built-in-symbols/atomic-elements-of-expressions/representation-of-numbers/accuracy/>`_.