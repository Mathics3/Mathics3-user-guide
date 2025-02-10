DominantColors
==============

`WMA link <https://reference.wolfram.com/language/ref/DominantColors.html>`_


:code:`DominantColors` [:math:`image`]
    gives a list of colors which are dominant in the given image.

:code:`DominantColors` [:math:`image`, :math:`n`]
    returns at most :math:`n` colors.

:code:`DominantColors` [:math:`image`, :math:`n`, :math:`prop`]
    returns the given property :math:`prop`, which may be:
    

    - "Color": return RGB colors,
    
-  "LABColor": return  LAB colors,
    
-  "Count": return the number of pixels a dominant color covers,
    
-  "Coverage": return the fraction of the image a dominant color                  covers, or
    
-  "CoverageImage": return a black and white image indicating with                  white the parts that are covered by a dominant color.
    







The option "ColorCoverage" specifies the minimum amount of coverage needed to     include a dominant color in the result.

The option "MinColorDistance" specifies the distance (in LAB color space) up     to which colors are merged and thus regarded as belonging to the same dominant color.

>>> img = Import["ExampleData/hedy.tif"]

    =
.. image:: tmpw86mlwom.png
    :align: center



>>> DominantColors[img]

    =
.. image:: eq_Reference_of_Built-in_Symbols_Colors_DominantColors_6daswery.png
    :align: center



>>> DominantColors[img, 3]

    =
.. image:: eq_Reference_of_Built-in_Symbols_Colors_DominantColors_xk5yoept.png
    :align: center



>>> DominantColors[img, 3, "Coverage"]

    =
:math:`\left\{\frac{68817}{103360},\frac{62249}{516800},\frac{37953}{516800}\right\}`


>>> DominantColors[img, 3, "CoverageImage"]

>>> DominantColors[img, 3, "Count"]

    =
:math:`\left\{344085,62249,37953\right\}`


>>> DominantColors[img, 2, "LABColor"]

    =
.. image:: eq_Reference_of_Built-in_Symbols_Colors_DominantColors_d13rnb0k.png
    :align: center



>>> DominantColors[img, MinColorDistance -> 0.5]

    =
.. image:: eq_Reference_of_Built-in_Symbols_Colors_DominantColors_9dpf0fyg.png
    :align: center



>>> DominantColors[img, ColorCoverage -> 0.15]

    =
.. image:: eq_Reference_of_Built-in_Symbols_Colors_DominantColors_exzbtpb5.png
    :align: center



