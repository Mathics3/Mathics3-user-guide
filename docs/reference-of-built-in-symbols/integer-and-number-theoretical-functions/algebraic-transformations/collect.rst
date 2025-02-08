Collect
=======

`WMA link <https://reference.wolfram.com/language/ref/Collect.html>`_


:code:`Collect` [:math:`expr`, :math:`x`]
    Expands :math:`expr` and collect together terms having the same power of :math:`x`.

:code:`Collect` [:math:`expr`, {:math:`x_1`, :math:`x_2`, ...}]
    Expands :math:`expr` and collect together terms having the same powers of          :math:`x_1`, :math:`x_2`, ....

:code:`Collect` [:math:`expr`, {:math:`x_1`, :math:`x_2`, ...}, :math:`filter`]
    After collect the terms, applies :math:`filter` to each coefficient.





>>> Collect[(x+y)^3, y]
    =

:math:`x^3+3 x^2 y+3 x y^2+y^3`


>>> Collect[2 Sin[x z] (x+2 y^2 + Sin[y] x), y]
    =

:math:`2 x \text{Sin}\left[x z\right]+2 x \text{Sin}\left[x z\right] \text{Sin}\left[y\right]+4 y^2 \text{Sin}\left[x z\right]`


>>> Collect[3 x y+2 Sin[x z] (x+2 y^2 + x) + (x+y)^3, y]
    =

:math:`4 x \text{Sin}\left[x z\right]+x^3+y \left(3 x+3 x^2\right)+y^2 \left(3 x+4 \text{Sin}\left[x z\right]\right)+y^3`


>>> Collect[3 x y+2 Sin[x z] (x+2 y^2 + x) + (x+y)^3, {x,y}]
    =

:math:`4 x \text{Sin}\left[x z\right]+x^3+3 x y+3 x^2 y+4 y^2 \text{Sin}\left[x z\right]+3 x y^2+y^3`


>>> Collect[3 x y+2 Sin[x z] (x+2 y^2 + x) + (x+y)^3, {x,y}, h]
    =

:math:`x h\left[4 \text{Sin}\left[x z\right]\right]+x^3 h\left[1\right]+x y h\left[3\right]+x^2 y h\left[3\right]+y^2 h\left[4 \text{Sin}\left[x z\right]\right]+x y^2 h\left[3\right]+y^3 h\left[1\right]`


