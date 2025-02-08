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

.. image:: tmpt8gkuhrc.png
    :align: center



>>> DominantColors[img]
    =


.. math::
    \left\{
    \includegraphics[]{/tmp/tmpk1nrfbal.png}
    ,
    \includegraphics[]{/tmp/tmpgwm_otks.png}
    ,
    \includegraphics[]{/tmp/tmp89cbzgxr.png}
    \right\}



>>> DominantColors[img, 3]
    =


.. math::
    \left\{
    \includegraphics[]{/tmp/tmph0mk3oh3.png}
    ,
    \includegraphics[]{/tmp/tmp__643hee.png}
    ,
    \includegraphics[]{/tmp/tmpnjtmj3as.png}
    \right\}



>>> DominantColors[img, 3, "Coverage"]
    =

:math:`\left\{\frac{68817}{103360},\frac{62249}{516800},\frac{37953}{516800}\right\}`


>>> DominantColors[img, 3, "CoverageImage"]

>>> DominantColors[img, 3, "Count"]
    =

:math:`\left\{344085,62249,37953\right\}`


>>> DominantColors[img, 2, "LABColor"]
    =


.. math::
    \left\{\text{LABColor}\left[0.00581591,0.00207458,-0.00760911\right],
    \includegraphics[]{/tmp/tmpltpvuyjw.png}
    \right\}



>>> DominantColors[img, MinColorDistance -> 0.5]
    =


.. math::
    \left\{
    \includegraphics[]{/tmp/tmpmvl3wfp2.png}
    ,
    \includegraphics[]{/tmp/tmpw4gwrhmm.png}
    \right\}



>>> DominantColors[img, ColorCoverage -> 0.15]
    =


.. math::
    \left\{
    \includegraphics[]{/tmp/tmpasnrivkp.png}
    \right\}



