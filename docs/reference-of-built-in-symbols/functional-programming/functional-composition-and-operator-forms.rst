Functional Composition and Operator Forms
=========================================

`Functional Composition <https://en.wikipedia.org/wiki/Function_composition_(computer_science)>`_ is a way to combine simple functions to build more complicated ones.
Like the usual composition of functions in mathematics, the result of each function is passed as the argument of the next, and the result of the last one is the result of the whole.

The symbolic structure of Mathics3 makes it easy to create "operators" that can be composed and manipulated symbolically—forming "pipelines" of operations—and then applied to arguments.

Some built-in functions also directly support a "curried" form, in which they can immediately be given as symbolic operators.

.. toctree::
    :maxdepth: 2

    functional-composition-and-operator-forms/composition.rst
    functional-composition-and-operator-forms/identity.rst

