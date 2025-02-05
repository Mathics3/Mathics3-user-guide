ReadList
========

`WMA link <https://reference.wolfram.com/language/ref/ReadList.html>`_


:code:`ReadList` [":math:`file`"]
    Reads all the expressions until the end of file.

:code:`ReadList` [":math:`file`", :math:`type`]
    Reads objects of a specified type until the end of file.

:code:`ReadList` [":math:`file`", {:math:`type_1`, :math:`type_2`, ...}]
    Reads a sequence of specified types until the end of file.





To read all the numbers in a file and return a list of them:

>>> ReadList["ExampleData/numbers.txt", Number]
  = {11.1, 22.2, 33.3, 44.4, 55.5, 66.6}

(Use `:code:`FilePrint[]`  </doc/reference-of-built-in-symbols/inputoutput-files-and-filesystem/file-and-stream-operations/fileprint/>`_    to get the raw data for the examples above and below.)

This does the same, but groups the numbers in to a pairs:

>>> ReadList["ExampleData/numbers.txt", {Number, Number}]
  = {{11.1, 22.2}, {33.3, 44.4}, {55.5, 66.6}}

Now let us read and put blocks of 3 numbers in its own list:

>>> ReadList["ExampleData/numbers.txt", Table[Number, {3}]]
  = {{11.1, 22.2, 33.3}, {44.4, 55.5, 66.6}}

Like `:code:`Read[]`  </doc/reference-of-built-in-symbols/inputoutput-files-and-filesystem/file-and-stream-operations/read/>`_,       :code:`ReadList`  handles types of objects other than numbers.
We can read a list of characters in a file putting each character as an item in a list:

>>> ReadList["ExampleData/strings.txt", Character]
  = ...

And now, here are the integer codes corresponding to each of the bytes in the file:

>>> ReadList["ExampleData/strings.txt", Byte]
  = {72, 101, 114, 101, 32, 105, 115, 32, 116, 101, 120, 116, 46, 10, 65, 110, 100, 32, 109, 111, 114, 101, 32, 116, 101, 120, 116, 46, 10}

But the data can also be read by "words":

>>> ReadList["ExampleData/strings.txt", Word]
  = {Here, is, text., And, more, text.}

The above uses the default value which is space of some sort., However you can     set your own value:

>>> ReadList["ExampleData/strings.txt", Word, WordSeparators -> {"e", "."}]
  = {H, r,  is t, xt, And mor,  t, xt}

See `WordSeparators <https://reference.wolfram.com/language/ref/WordSeprators.html>`_     for more information.

Reading by records uses the separators found in

>>> ReadList["ExampleData/strings.txt", Record]
  = {Here is text., And more text.}

See `RecordSeparators <https://reference.wolfram.com/language/ref/RecordSeprators.html>`_     works analgously for records as :code:`WordSeparators`  does for words.

To allow both periods and newlines as record separators:

>>> ReadList["ExampleData/sentences.txt", Record, RecordSeparators -> {".", "\n"}]
  = {Here is text,  And more, And a second line}

See also `Reading Textual Data <https://reference.wolfram.com/language/tutorial/FilesStreamsAndExternalOperations.html#3333>`_.