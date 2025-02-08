PolarPlot
=========

`WMA link <https://reference.wolfram.com/language/ref/PolarPlot.html>`_

:code:`PolarPlot` [:math:`r`, {:math:`t`, :math:`t_{min}`, :math:`t_{max}`}]
    creates a polar plot of curve with radius :math:`r` as a function of angle :math:`t`       ranging from :math:`t_{min}` to :math:`t_{max}`.





In a Polar Plot, a `polar coordinate system <https://en.wikipedia.org/wiki/Polar_coordinate_system>`_ is used.

A polar coordinate system is a two-dimensional coordinate system in which     each point on a plane  is determined by a distance from a reference point     and an angle from a reference direction.

Here is a 5-blade propeller, or maybe a flower, using :code:`PolarPlot` :

>>> PolarPlot[Cos[5t], {t, 0, Pi}]
    =

.. image:: tmppi9ebnit.png
    :align: center




The number of blades and be change by adjusting the :math:`t` multiplier.

A slight change adding :code:`Abs`  turns this a clump of grass:

>>> PolarPlot[Abs[Cos[5t]], {t, 0, Pi}]
    =

.. image:: tmpd4jdugo0.png
    :align: center




Coils around a ring:

>>> PolarPlot[{1, 1 + Sin[20 t] / 5}, {t, 0, 2 Pi}]
    =

.. image:: tmp37lo9bk6.png
    :align: center




A spring having 16 turns:

>>> PolarPlot[Sqrt[t], {t, 0, 16 Pi}]
    =

.. image:: tmpuuq596ib.png
    :align: center



