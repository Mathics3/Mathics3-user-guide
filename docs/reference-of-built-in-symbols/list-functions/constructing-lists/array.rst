Array
=====

`WMA link <https://reference.wolfram.com/language/ref/Array.html>`_


:code:`Array` [:math:`f`, :math:`n`]
    returns the :math:`n`-element list :code:`{:math:`f`[1], ..., :math:`f`[:math:`n`]}` .

:code:`Array` [:math:`f`, :math:`n`, :math:`a`]
    returns the :math:`n`-element list :code:`{:math:`f`[:math:`a`], ..., :math:`f`[:math:`a` + :math:`n`]}` .

:code:`Array` [:math:`f`, {:math:`n`, :math:`m`}, {:math:`a`, :math:`b`}]
    returns an :math:`n`-by-:math:`m` matrix created by applying :math:`f` to indices           ranging from :code:`(:math:`a`, :math:`b`)`  to :code:`(:math:`a` + :math:`n`, :math:`b` + :math:`m`)` .

:code:`Array` [:math:`f`, :math:`dims`, :math:`origins`, :math:`h`]
    returns an expression with the specified dimensions and index origins,           with head :math:`h` (instead of :code:`List` ).





>>> Array[f, 4]
    =

:math:`\left\{f\left[1\right],f\left[2\right],f\left[3\right],f\left[4\right]\right\}`


>>> Array[f, {2, 3}]
    =

:math:`\left\{\left\{f\left[1,1\right],f\left[1,2\right],f\left[1,3\right]\right\},\left\{f\left[2,1\right],f\left[2,2\right],f\left[2,3\right]\right\}\right\}`


>>> Array[f, {2, 3}, 3]
    =

:math:`\left\{\left\{f\left[3,3\right],f\left[3,4\right],f\left[3,5\right]\right\},\left\{f\left[4,3\right],f\left[4,4\right],f\left[4,5\right]\right\}\right\}`


>>> Array[f, {2, 3}, {4, 6}]
    =

:math:`\left\{\left\{f\left[4,6\right],f\left[4,7\right],f\left[4,8\right]\right\},\left\{f\left[5,6\right],f\left[5,7\right],f\left[5,8\right]\right\}\right\}`


>>> Array[f, {2, 3}, 1, Plus]
    =

:math:`f\left[1,1\right]+f\left[1,2\right]+f\left[1,3\right]+f\left[2,1\right]+f\left[2,2\right]+f\left[2,3\right]`


