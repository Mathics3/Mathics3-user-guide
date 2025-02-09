FileDate
========

`WMA link <https://reference.wolfram.com/language/ref/FileDate.html>`_


:code:`FileDate` [:math:`file`, :math:`types`]
    returns the time and date at which the file was last modified.





>>> FileDate["ExampleData/sunflowers.jpg"]

    =
:math:`\left\{2121,11,10,2,35,29.7753\right\}`


>>> FileDate["ExampleData/sunflowers.jpg", "Access"]

    =
:math:`\left\{2125,2,9,19,30,33.885\right\}`


>>> FileDate["ExampleData/sunflowers.jpg", "Creation"]

    =
:math:`\text{Missing}\left[\text{NotApplicable}\right]`


>>> FileDate["ExampleData/sunflowers.jpg", "Change"]

    =
:math:`\left\{2121,11,10,2,42,43.6376\right\}`


>>> FileDate["ExampleData/sunflowers.jpg", "Modification"]

    =
:math:`\left\{2121,11,10,2,35,29.7753\right\}`


>>> FileDate["ExampleData/sunflowers.jpg", "Rules"]

    =
:math:`\left\{\text{Access}->\left\{2125,2,9,19,30,33.885\right\},\text{Creation}->\text{Missing}\left[\text{NotApplicable}\right],\text{Change}->\left\{2121,11,10,2,42,43.6376\right\},\text{Modification}->\left\{2121,11,10,2,35,29.7753\right\}\right\}`


