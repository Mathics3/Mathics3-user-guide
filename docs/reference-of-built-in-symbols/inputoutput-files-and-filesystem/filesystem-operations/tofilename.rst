ToFileName
==========

`WMA link <https://reference.wolfram.com/language/ref/ToFileName.html>`_


:code:`ToFileName` [{":math:`dir_1`", ":math:`dir_2`", ...}]
    joins the :math:`dir_i` together into one path.





:code:`ToFileName`  has been superseded by :code:`FileNameJoin` .

>>> ToFileName[{"dir1", "dir2"}, "file"]
  = dir1...dir2...file
>>> ToFileName["dir1", "file"]
  = dir1...file
>>> ToFileName[{"dir1", "dir2", "dir3"}]
  = dir1...dir2...dir3
