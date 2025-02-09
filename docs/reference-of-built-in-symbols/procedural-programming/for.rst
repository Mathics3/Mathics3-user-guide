For
===

`WMA link <https://reference.wolfram.com/language/ref/For.html>`_


:code:`For` [:math:`start`, :math:`test`, :math:`incr`, :math:`body`]
    evaluates :math:`start`, and then iteratively :math:`body` and :math:`incr` as long as :math:`test`
    evaluates to :code:`True` .

:code:`For` [:math:`start`, :math:`test`, :math:`incr`]
    evaluates only :math:`incr` and no :math:`body`.

:code:`For` [:math:`start`, :math:`test`]
    runs the loop without any body.





Compute the factorial of 10 using :code:`For` :

>>> n := 1


>>> For[i=1, i<=10, i=i+1, n = n * i]


>>> n

    =
:math:`3628800`


>>> n == 10!

    =
:math:`\text{True}`


