ImageResize
===========

`WMA link <https://reference.wolfram.com/language/ref/ImageResize.html>`_


:code:`ImageResize` [:math:`image`, :math:`width`]
    

:code:`ImageResize` [:math:`image`, {:math:`width`, :math:`height`}]
    





The Resampling option can be used to specify how to resample the image. Options are:


- Automatic

- Bicubic

- Bilinear

- Box

- Hamming

- Lanczos

- Nearest




See `Pillow Filters <https://pillow.readthedocs.io/en/stable/handbook/concepts.html#filters>`_    for a description of these.

>>> alice = Import["ExampleData/MadTeaParty.gif"]
  = -Image-
>>> shape = ImageDimensions[alice]
  = {640, 487}
>>> ImageResize[alice, shape / 2]
  = -Image-

The default sampling method is "Bicubic" which has pretty good upscaling     and downscaling quality. However "Box" is the fastest:

>>> ImageResize[alice, shape / 2, Resampling -> "Box"]
  = -Image-
