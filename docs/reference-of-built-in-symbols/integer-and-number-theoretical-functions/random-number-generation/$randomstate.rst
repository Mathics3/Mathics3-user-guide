$RandomState
============

`WMA link <https://reference.wolfram.com/language/ref/RandomState.html>`_

:code:`$RandomState`
    is a long number representing the internal state of the pseudo-random number generator.





>>> Mod[$RandomState, 10^100]

    =
:math:`1372200521109094304993475461974210200069735145393897568911163623769160707149198947125147496556565550`


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


