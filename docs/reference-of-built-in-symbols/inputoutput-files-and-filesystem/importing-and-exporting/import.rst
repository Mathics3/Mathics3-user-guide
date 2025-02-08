Import
======

`WMA link <https://reference.wolfram.com/language/ref/Import.html>`_


:code:`Import` [":math:`file`"]
    imports data from a file.

:code:`Import` [":math:`file`", ":math:`fmt`"]
    imports file assuming the specified file format.

:code:`Import` [":math:`file`", :math:`elements`]
    imports the specified elements from a file.

:code:`Import` [":math:`file`", {":math:`fmt`", :math:`elements`}]
    imports the specified elements from a file assuming the specified file format.

:code:`Import` ["http://:math:`url`", ...] and :code:`Import` ["ftp://:math:`url`", ...]
    imports from a URL.





>>> Import["ExampleData/ExampleData.txt", "Elements"]
    =

:math:`\left\{\text{Data},\text{Lines},\text{Plaintext},\text{String},\text{Words}\right\}`


>>> Import["ExampleData/ExampleData.txt", "Lines"]
    =

:math:`\left\{\text{Example File Format},\text{Created by Angus},\text{0.629452	0.586355},\text{0.711009	0.687453},\text{0.246540	0.433973},\text{0.926871	0.887255},\text{0.825141	0.940900},\text{0.847035	0.127464},\text{0.054348	0.296494},\text{0.838545	0.247025},\text{0.838697	0.436220},\text{0.309496	0.833591}\right\}`


>>> Import["ExampleData/colors.json"]
    =

:math:`\left\{\text{colorsArray}->\left\{\left\{\text{colorName}->\text{black},\text{rgbValue}->\text{(0, 0, 0)},\text{hexValue}->\text{\#000000}\right\},\left\{\text{colorName}->\text{red},\text{rgbValue}->\text{(255, 0, 0)},\text{hexValue}->\text{\#FF0000}\right\},\left\{\text{colorName}->\text{green},\text{rgbValue}->\text{(0, 255, 0)},\text{hexValue}->\text{\#00FF00}\right\},\left\{\text{colorName}->\text{blue},\text{rgbValue}->\text{(0, 0, 255)},\text{hexValue}->\text{\#0000FF}\right\},\left\{\text{colorName}->\text{yellow},\text{rgbValue}->\text{(255, 255, 0)},\text{hexValue}->\text{\#FFFF00}\right\},\left\{\text{colorName}->\text{cyan},\text{rgbValue}->\text{(0, 255, 255)},\text{hexValue}->\text{\#00FFFF}\right\},\left\{\text{colorName}->\text{magenta},\text{rgbValue}->\text{(255, 0, 255)},\text{hexValue}->\text{\#FF00FF}\right\},\left\{\text{colorName}->\text{white},\text{rgbValue}->\text{(255, 255, 255)},\text{hexValue}->\text{\#FFFFFF}\right\}\right\}\right\}`


