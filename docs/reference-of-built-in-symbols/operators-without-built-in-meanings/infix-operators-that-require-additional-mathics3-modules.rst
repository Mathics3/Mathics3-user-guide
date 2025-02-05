Infix Operators that require Additional Mathics3 Modules
========================================================

Some Infix operators require loading Mathics3 Modules before the operators is used in a special way.

Right now, this happens for directed and undirected edges of a network graph. Before issuing :code:`LoadModule["pymathics.graph"]` , the operators here have no meaning and can be user defined like other operators that have no pre-set meaning.

.. toctree::
    :maxdepth: 2

    infix-operators-that-require-additional-mathics3-modules/directededge.rst
    infix-operators-that-require-additional-mathics3-modules/undirectededge.rst

