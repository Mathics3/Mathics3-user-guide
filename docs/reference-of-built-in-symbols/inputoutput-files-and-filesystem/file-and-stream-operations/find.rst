Find
====

`WMA link <https://reference.wolfram.com/language/ref/Find.html>`_


:code:`Find` [:math:`stream`, :math:`text`]
    find the first line in :math:`stream` that contains :math:`text`.





>>> stream = OpenRead["ExampleData/EinsteinSzilLetter.txt", CharacterEncoding->"UTF8"];


>>> Find[stream, "uranium"]
    =

:math:`\text{in manuscript, leads me to expect that the element uranium may be turned into}`


>>> Find[stream, "uranium"]
    =

:math:`\text{become possible to set up a nuclear chain reaction in a large mass of uranium,}`


>>> Close[stream]
    = ...`

>>> stream = OpenRead["ExampleData/EinsteinSzilLetter.txt", CharacterEncoding->"UTF8"];


>>> Find[stream, {"energy", "power"} ]
    =

:math:`\text{a new and important source of energy in the immediate future. Certain aspects}`


>>> Find[stream, {"energy", "power"} ]
    =

:math:`\text{by which vast amounts of power and large quantities of new radium-like}`


>>> Close[stream]
    = ...`

