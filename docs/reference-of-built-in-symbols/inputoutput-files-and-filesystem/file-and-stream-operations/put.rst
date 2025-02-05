Put
===

`WMA link <https://reference.wolfram.com/language/ref/Put.html>`_


:code:`:math:`expr` >> :math:`filename``
    write :math:`expr` to a file.

:code:`Put` [:math:`expr_1`, :math:`expr_2`, ..., ":math:`filename`"]
    write a sequence of expressions to a file.





>>> Put[40!, fortyfactorial]
  = 815915283247897734345611269596115894272000000000 >> fortyfactorial
>>> filename = $TemporaryDirectory <> "/fortyfactorial";

>>> Put[40!, filename]

>>> FilePrint[filename]

>>> Get[filename]
  = 815915283247897734345611269596115894272000000000
>>> DeleteFile[filename]

>>> filename = $TemporaryDirectory <> "/fiftyfactorial";

>>> Put[10!, 20!, 30!, filename]

>>> FilePrint[filename]

>>> DeleteFile[filename]


=

>>> filename = $TemporaryDirectory <> "/example_file";

>>> Put[x + y, 2x^2 + 4z!, Cos[x] + I Sin[x], filename]

>>> FilePrint[filename]

>>> DeleteFile[filename]

