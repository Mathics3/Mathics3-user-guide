SetOptions
==========

`WMA link <https://reference.wolfram.com/language/ref/SetOptions.html>`_


:code:`SetOptions` [:math:`s`, name1 -> value1, name2 -> value2, ...]
    sets the specified default options for a symbol :math:`s`.       The entire set of options for :math:`s` is returned.





One way to find the default options for a symbol is to use     :code:`SetOptions`  passing no association pairs:

>>> SetOptions[Plot]
    =

:math:`\left\{\text{AspectRatio}->\frac{1}{\text{GoldenRatio}},\text{Axes}->\text{True},\text{AxesStyle}->\left\{\right\},\text{Background}->\text{Automatic},\text{Exclusions}->\text{Automatic},\text{ImageSize}->\text{Automatic},\text{LabelStyle}->\left\{\right\},\text{MaxRecursion}->\text{Automatic},\text{Mesh}->\text{None},\text{PlotPoints}->\text{None},\text{PlotRange}->\text{Automatic},\text{PlotRangePadding}->\text{Automatic},\text{TicksStyle}->\left\{\right\}\right\}`


