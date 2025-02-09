QuantityQ
=========

`WMA link <https://reference.wolfram.com/language/ref/QuantityQ.html>`_

:code:`QuantityQ` [:math:`expr`]
    return True if :math:`expr` is a valid Association object, and False otherwise.





>>> QuantityQ[Quantity[3, "Meters"]]

    =
:math:`\text{True}`


>>> QuantityQ[Quantity[3, "Maters"]]

    Quantity::unkunit Unable to interpret unit specification Maters.

    =
:math:`\text{False}`


