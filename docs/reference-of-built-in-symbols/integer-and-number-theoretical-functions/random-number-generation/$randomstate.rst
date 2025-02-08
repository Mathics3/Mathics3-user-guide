$RandomState
============

`WMA link <https://reference.wolfram.com/language/ref/RandomState.html>`_

:code:`$RandomState`
    is a long number representing the internal state of the pseudo-random number generator.





>>> Mod[$RandomState, 10^100]
    =

:math:`9770388145129454895629899890614051928594913728626392343920147894999762814007063933621688869185688622`


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


