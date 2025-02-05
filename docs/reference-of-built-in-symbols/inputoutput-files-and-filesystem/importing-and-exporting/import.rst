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
  = {Data, Lines, Plaintext, String, Words}
>>> Import["ExampleData/ExampleData.txt", "Lines"]
  = ...
>>> Import["ExampleData/colors.json"]
  = {colorsArray -> {{colorName -> black, rgbValue -> (0, 0, 0), hexValue -> #000000}, {colorName -> red, rgbValue -> (255, 0, 0), hexValue -> #FF0000}, {colorName -> green, rgbValue -> (0, 255, 0), hexValue -> #00FF00}, {colorName -> blue, rgbValue -> (0, 0, 255), hexValue -> #0000FF}, {colorName -> yellow, rgbValue -> (255, 255, 0), hexValue -> #FFFF00}, {colorName -> cyan, rgbValue -> (0, 255, 255), hexValue -> #00FFFF}, {colorName -> magenta, rgbValue -> (255, 0, 255), hexValue -> #FF00FF}, {colorName -> white, rgbValue -> (255, 255, 255), hexValue -> #FFFFFF}}}
