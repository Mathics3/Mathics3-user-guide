InputStream
===========

`WMA link <https://reference.wolfram.com/language/ref/InputStream.html>`_


:code:`InputStream` [:math:`name`, :math:`n`]
    represents an input stream for functions such as :code:`Read`  or :code:`Find` .





:code:`StringToStream`  opens an input stream:

>>> stream = StringToStream["Mathics is cool!"]
    =

:math:`\text{InputStream}\left[\text{String},17\right]`


>>> Close[stream]
    =

:math:`\text{String}`


