Inner
=====

`WMA link <https://reference.wolfram.com/language/ref/Inner.html>`_


:code:`Inner` [:math:`f`, :math:`x`, :math:`y`, :math:`g`]
    computes a generalised inner product of :math:`x` and :math:`y`, using
    a multiplication function :math:`f` and an addition function :math:`g`.





>>> Inner[f, {a, b}, {x, y}, g]

    =
:math:`g\left[f\left[a,x\right],f\left[b,y\right]\right]`



:code:`Inner`  can be used to compute a dot product:

>>> Inner[Times, {a, b}, {c, d}, Plus] == {a, b} . {c, d}

    =
:math:`\text{True}`



The inner product of two boolean matrices:

>>> Inner[And, {{False, False}, {False, True}}, {{True, False}, {True, True}}, Or]

    =
:math:`\left\{\left\{\text{False},\text{False}\right\},\left\{\text{True},\text{True}\right\}\right\}`



Inner works with tensors of any depth:

>>> Inner[f, {{{a, b}}, {{c, d}}}, {{1}, {2}}, g]

    =
:math:`\left\{\left\{\left\{g\left[f\left[a,1\right],f\left[b,2\right]\right]\right\}\right\},\left\{\left\{g\left[f\left[c,1\right],f\left[d,2\right]\right]\right\}\right\}\right\}`


