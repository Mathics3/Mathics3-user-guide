OpenAppend
==========

`WMA link <https://reference.wolfram.com/language/ref/OpenAppend.html>`_


:code:`OpenAppend["file"]`
    opens a file and returns an OutputStream to which writes are appended.





>>> OpenAppend[]

    =
:math:`\text{OutputStream}\left[\text{/tmp/tmpt0iwakwb},17\right]`


>>> DeleteFile[Close[%]];


