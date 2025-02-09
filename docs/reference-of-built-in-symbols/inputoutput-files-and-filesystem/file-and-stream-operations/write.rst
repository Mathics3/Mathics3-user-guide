Write
=====

`WMA link <https://reference.wolfram.com/language/ref/Write.html>`_


:code:`Write` [:math:`channel`, :math:`expr_1`, :math:`expr_2`, ...]
    writes the expressions to the output channel followed by a newline.





>>> stream = OpenWrite[]

    =
:math:`\text{OutputStream}\left[\text{/tmp/tmpnf677way},37\right]`


>>> Write[stream, 10 x + 15 y ^ 2]


>>> Write[stream, 3 Sin[z]]



The stream must be closed in order to use the file again:

>>> Close[stream];


>>> stream = OpenRead[%];


>>> ReadList[stream]

    =
:math:`\left\{10 x+15 y^2,3 \text{Sin}\left[z\right]\right\}`


>>> DeleteFile[Close[stream]];


