Automatic
=========

`WMA link <https://reference.wolfram.com/language/ref/Automatic.html>`_


:code:`Automatic`
    is used to specify an automatically computed option value.





:code:`Automatic`  is the default for :code:`PlotRange` , :code:`ImageSize` , and other
graphical options:

>>> Cases[Options[Plot], HoldPattern[_ :> Automatic]]
  = {Background :> Automatic, Exclusions :> Automatic, ImageSize :> Automatic, MaxRecursion :> Automatic, PlotRange :> Automatic, PlotRangePadding :> Automatic}
