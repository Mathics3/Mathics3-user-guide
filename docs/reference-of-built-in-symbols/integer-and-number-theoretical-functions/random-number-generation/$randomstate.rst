$RandomState
============

`WMA link <https://reference.wolfram.com/language/ref/RandomState.html>`_

:code:`$RandomState`
    is a long number representing the internal state of the pseudo-random number generator.





>>> Mod[$RandomState, 10^100]

    =
:math:`6456603649926297054891154013344556988584349294092355407797578608082017023813771069506608516625110062`


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


