$RandomState
============

`WMA link <https://reference.wolfram.com/language/ref/RandomState.html>`_

:code:`$RandomState`
    is a long number representing the internal state of the pseudo-random number generator.





>>> Mod[$RandomState, 10^100]

    =
:math:`3164369059336638785776926379539912730290284204332833950669612893930235804113718126328240795884491822`


>>> IntegerLength[$RandomState]

    =
:math:`6440`



So far, it is not possible to assign values to :code:`$RandomState` .

>>> $RandomState = 42

    $RandomState::rndst It is not possible to change the random state.

    =
:math:`42`



Not even to its own value:

>>> $RandomState = $RandomState;

    $RandomState::rndst It is not possible to change the random state.


