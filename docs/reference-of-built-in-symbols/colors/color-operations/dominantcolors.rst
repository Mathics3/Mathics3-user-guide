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
  = -Image-
>>> DominantColors[img]
  = {RGBColor[0.00784314, 0.00784314, 0.0156863], RGBColor[0.996078, 0.803922, 0.721569], RGBColor[0.227451, 0.329412, 0.360784]}
>>> DominantColors[img, 3]
  = {RGBColor[0.00784314, 0.00784314, 0.0156863], RGBColor[0.996078, 0.803922, 0.721569], RGBColor[0.227451, 0.329412, 0.360784]}
>>> DominantColors[img, 3, "Coverage"]
  = {68817 / 103360, 62249 / 516800, 37953 / 516800}
>>> DominantColors[img, 3, "CoverageImage"]
  = {-Image-, -Image-, -Image-}
>>> DominantColors[img, 3, "Count"]
  = {344085, 62249, 37953}
>>> DominantColors[img, 2, "LABColor"]
  = {LABColor[0.00581591, 0.00207458, -0.00760911], LABColor[0.863667, 0.156864, 0.173956]}
>>> DominantColors[img, MinColorDistance -> 0.5]
  = {RGBColor[0.00784314, 0.00784314, 0.0156863], RGBColor[0.996078, 0.803922, 0.721569]}
>>> DominantColors[img, ColorCoverage -> 0.15]
  = {RGBColor[0.00784314, 0.00784314, 0.0156863]}
