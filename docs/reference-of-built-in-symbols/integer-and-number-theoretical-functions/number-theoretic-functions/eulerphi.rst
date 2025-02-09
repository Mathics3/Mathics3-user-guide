EulerPhi
========

`Euler's totient function <https://en.wikipedia.org/wiki/Euler%27s_totient_function>`_ (`SymPy <https://docs.sympy.org/latest/modules/ntheory.html#sympy.ntheory.factor_.totient>`_, `WMA <https://reference.wolfram.com/language/ref/EulerPhi.html>`_)
This function counts positive integers up to :math:`n` that are relatively prime to :math:`n`.
It is typically used in cryptography and in many applications in elementary number theory.

:code:`EulerPhi` [:math:`n`]
    returns the Euler totient function .





Compute the Euler totient function:

>>> EulerPhi[9]

    =
:math:`6`



:code:`EulerPhi`  of a negative integer is same as its positive counterpart:

>>> EulerPhi[-11] == EulerPhi[11]

    =
:math:`\text{True}`


>>> EulerPhi[0]

    =
:math:`0`



Large arguments are computed quickly:

>>> EulerPhi[40!]

    =
:math:`121343746763281707274905415180804423680000000000`



:code:`EulerPhi`  threads over lists:

>>> EulerPhi[Range[1, 17, 2]]

    =
:math:`\left\{1,2,4,6,6,10,12,8,16\right\}`



Above, we get consecutive even numbers when the input is prime.

Compare the results above with:

>>> EulerPhi[Range[1, 17]]

    =
:math:`\left\{1,1,2,2,4,2,6,4,6,4,10,4,12,6,8,8,16\right\}`


