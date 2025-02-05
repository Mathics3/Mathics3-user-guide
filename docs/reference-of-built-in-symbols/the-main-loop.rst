The Main Loop
=============

An interactive session operates a loop, called the "main loop" in this way:



- read input

- process input

- format and print results

- repeat




As part of this loop, various global objects in this section are consulted.

There are a variety of "hooks" that allow you to insert functions to be applied to the expressions at various stages in the main loop.

If you assign a function to the global variable :code:`$PreRead`  it will be applied with the input that is read in the first step listed above.

Similarly, if you assign a function to global variable :code:`$Pre` , it will be applied with the input before processing the input, the second step listed above.

.. toctree::
    :maxdepth: 2

    the-main-loop/$historylength.rst
    the-main-loop/$line.rst
    the-main-loop/$post.rst
    the-main-loop/$pre.rst
    the-main-loop/$preprint.rst
    the-main-loop/$preread.rst
    the-main-loop/$syntaxhandler.rst
    the-main-loop/in.rst

