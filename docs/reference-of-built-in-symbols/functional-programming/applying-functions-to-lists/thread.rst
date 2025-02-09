Thread
======

`WMA link <https://reference.wolfram.com/language/ref/Thread.html>`_


:code:`Thread[:math:`f`` [:math:`args`]]
    threads :math:`f` over any lists that appear in :math:`args`.

:code:`Thread[:math:`f`` [:math:`args`], :math:`h`]
    threads over any parts with head :math:`h`.





>>> Thread[f[{a, b, c}]]

    =
:math:`\left\{f\left[a\right],f\left[b\right],f\left[c\right]\right\}`


>>> Thread[f[{a, b, c}, t]]

    =
:math:`\left\{f\left[a,t\right],f\left[b,t\right],f\left[c,t\right]\right\}`


>>> Thread[f[a + b + c], Plus]

    =
:math:`f\left[a\right]+f\left[b\right]+f\left[c\right]`



Functions with attribute :code:`Listable`  are automatically threaded over lists:

>>> {a, b, c} + {d, e, f} + g

    =
:math:`\left\{a+d+g,b+e+g,c+f+g\right\}`


