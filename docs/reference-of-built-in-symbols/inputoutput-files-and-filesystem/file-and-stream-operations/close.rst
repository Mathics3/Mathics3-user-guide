Close
=====

`WMA link <https://reference.wolfram.com/language/ref/Close.html>`_


:code:`Close` [:math:`obj`]
    Closes a stream or socket.
    
    :math:`obj` can be an :code:`InputStream` , or an :code:`OutputStream`  object, or a :code:`String` .       When :math:`obj` is a string file path, one of the channels associated with it is closed.





>>> Close[StringToStream["123abc"]]
  = String
>>> file=Close[OpenWrite[]]
  = ...

Closing a file doesn't delete it from the filesystem.

>>> DeleteFile[file];

>>> Clear[file]


If two streams are open with the same file, then     a :code:`Close`  by file path closes only one of the streams:

>>> stream1 = OpenRead["ExampleData/numbers.txt"]
  = InputStream[ExampleData/numbers.txt, ...]
>>> stream2 = OpenRead["ExampleData/numbers.txt"]
  = InputStream[ExampleData/numbers.txt, ...]
>>> Close["ExampleData/numbers.txt"]
  = ExampleData/numbers.txt

Usually, the most-recent stream is closed, while the earlier-opened     stream still persists:

>>> Read[stream1]
  = 8205.79

However, one of the streams *is* closed:

>>> Read[stream2]
  = $Failed
>>> Close["ExampleData/numbers.txt"]
  = ExampleData/numbers.txt
>>> Read[stream1]
  = $Failed
