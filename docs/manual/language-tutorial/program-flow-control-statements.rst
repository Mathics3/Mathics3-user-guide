Program-Flow Control Statements
===============================

Like most programming languages, \Mathics has common program-flow control statements for conditions, loops, etc.:

:code:`If` [:math:`cond`, :math:`pos`, :math:`neg`]
    returns :math:`pos` if :math:`cond` evaluates to :code:`True` , and :math:`neg` if it evaluates to :code:`False` .

:code:`Which` [:math:`cond_1`, :math:`expr_1`, :math:`cond_2`, :math:`expr_2`, ...]
    yields :math:`expr_1` if :math:`cond_1` evaluates to :code:`True` , :math:`expr_2` if :math:`cond_2` evaluates to :code:`True` , etc.

:code:`Do` [:math:`expr`, {:math:`i`, :math:`max`}]
    evaluates :math:`expr` :math:`max` times, substituting :math:`i` in :math:`expr` with values from 1 to :math:`max`.

:code:`For` [:math:`start`, :math:`test`, :math:`incr`, :math:`body`]
    evaluates :math:`start`, and then iteratively :math:`body` and :math:`incr` as long as :math:`test` evaluates to :code:`True` .

:code:`While` [:math:`test`, :math:`body`]
    evaluates :math:`body` as long as :math:`test` evaluates to :code:`True` .

:code:`Nest` [:math:`f`, :math:`expr`, :math:`n`]
    returns an expression with :math:`f` applied :math:`n` times to :math:`expr`.

:code:`NestWhile` [:math:`f`, :math:`expr`, :math:`test`]
    applies a function :math:`f` repeatedly on an expression :math:`expr`, until
    applying :math:`test` on the result no longer yields :code:`True` .

:code:`FixedPoint` [:math:`f`, :math:`expr`]
    starting with :math:`expr`, repeatedly applies :math:`f` until the result no longer changes.





>>> If[2 < 3, a, b]
  = a
>>> x = 3; Which[x < 2, a, x > 4, b, x < 5, c]
  = c

Compound statements can be entered with :code:`;` . The result of a compound expression is its last part or :code:`Null`  if it ends with a :code:`;` .

>>> 1; 2; 3
  = 3
>>> 1; 2; 3;


Inside :code:`For` , :code:`While` , and :code:`Do`  loops, :code:`Break[]`  exits the loop, and :code:`Continue[]`  continues to the next iteration.

>>> For[i = 1, i <= 5, i++, If[i == 4, Break[]]; Print[i]]

