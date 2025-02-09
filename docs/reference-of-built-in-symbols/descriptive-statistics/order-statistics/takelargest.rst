TakeLargest
===========

`WMA link <https://reference.wolfram.com/language/ref/TakeLargest.html>`_


:code:`TakeLargest` [:math:`list`, :math:`f`, :math:`n`]
    returns the a sorted list of the :math:`n` largest items in :math:`list`.





List the largest two numbers of a list:

>>> TakeLargest[{100, -1, 50, 10}, 2]

    =
:math:`\left\{100,50\right\}`



None, Null, Indeterminate and expressions with head Missing are ignored     by default:

>>> TakeLargest[{-8, 150, Missing[abc]}, 2]

    =
:math:`\left\{150,-8\right\}`



You may specify which items are ignored using the option :code:`ExcludedForms` :

>>> TakeLargest[{-8, 150, Missing[abc]}, 2, ExcludedForms -> {}]

    =
:math:`\left\{\text{Missing}\left[\text{abc}\right],150\right\}`


