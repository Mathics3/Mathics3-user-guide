$RandomState
============

`WMA link <https://reference.wolfram.com/language/ref/RandomState.html>`_

:code:`$RandomState`
    is a long number representing the internal state of the pseudo-random number generator.





>>> Mod[$RandomState, 10^100]

    =
:math:`5650580858300831602113584755017053560217808237674949468510130756719478043129146569556675201135318062`


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


