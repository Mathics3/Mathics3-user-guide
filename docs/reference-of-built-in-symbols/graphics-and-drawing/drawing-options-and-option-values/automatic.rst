Automatic
=========

`WMA link <https://reference.wolfram.com/language/ref/Automatic.html>`_


:code:`Automatic`
    is used to specify an automatically computed option value.





:code:`Automatic`  is the default for :code:`PlotRange` , :code:`ImageSize` , and other
graphical options:

>>> Cases[Options[Plot], HoldPattern[_ :> Automatic]]

    =
:math:`\left\{\text{Background}\text{:>}\text{Automatic},\text{Exclusions}\text{:>}\text{Automatic},\text{ImageSize}\text{:>}\text{Automatic},\text{MaxRecursion}\text{:>}\text{Automatic},\text{PlotRange}\text{:>}\text{Automatic},\text{PlotRangePadding}\text{:>}\text{Automatic}\right\}`


