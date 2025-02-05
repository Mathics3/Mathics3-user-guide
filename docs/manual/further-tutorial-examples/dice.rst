Dice
====

Let's play with dice in this example. A :code:`Dice`  object shall represent the outcome of a series of rolling a dice with six faces, e.g.:

>>> Dice[1, 6, 4, 4]
  = Dice[1, 6, 4, 4]

Like in most games, the ordering of the individual throws does not matter. We can express this by making :code:`Dice`  :code:`Orderless` :

>>> SetAttributes[Dice, Orderless]

>>> Dice[1, 6, 4, 4]
  = Dice[1, 4, 4, 6]

A dice object shall be displayed as a rectangle with the given number of points in it, positioned like on a traditional dice:

>>> Format[Dice[n_Integer?(1 <= # <= 6 &)]] := Block[{p = 0.2, r = 0.05}, Graphics[{EdgeForm[Black], White, Rectangle[], Black, EdgeForm[], If[OddQ[n], Disk[{0.5, 0.5}, r]], If[MemberQ[{2, 3, 4, 5, 6}, n], Disk[{p, p}, r]], If[MemberQ[{2, 3, 4, 5, 6}, n], Disk[{1 - p, 1 - p}, r]], If[MemberQ[{4, 5, 6}, n], Disk[{p, 1 - p}, r]], If[MemberQ[{4, 5, 6}, n], Disk[{1 - p, p}, r]], If[n === 6, {Disk[{p, 0.5}, r], Disk[{1 - p, 0.5}, r]}]}, ImageSize -> Tiny]]

>>> Dice[1]
  = -Graphics-
>>> Definition[Dice]
  = Attributes[Dice] = {Orderless}
    
    Format[Dice[n_Integer ? (1 <= #1 <= 6&)], MathMLForm] = Block[{p = 0.2, r = 0.05}, Graphics[{EdgeForm[Black], White, Rectangle[], Black, EdgeForm[], If[OddQ[n], Disk[{0.5, 0.5}, r]], If[MemberQ[{2, 3, 4, 5, 6}, n], Disk[{p, p}, r]], If[MemberQ[{2, 3, 4, 5, 6}, n], Disk[{Plus[1, Times[-1, p]], Plus[1, Times[-1, p]]}, r]], If[MemberQ[{4, 5, 6}, n], Disk[{p, Plus[1, Times[-1, p]]}, r]], If[MemberQ[{4, 5, 6}, n], Disk[{Plus[1, Times[-1, p]], p}, r]], If[n === 6, {Disk[{p, 0.5}, r], Disk[{Plus[1, Times[-1, p]], 0.5}, r]}]}, ImageSize -> Tiny]]
    
    Format[Dice[n_Integer ? (1 <= #1 <= 6&)], OutputForm] = Block[{p = 0.2, r = 0.05}, Graphics[{EdgeForm[Black], White, Rectangle[], Black, EdgeForm[], If[OddQ[n], Disk[{0.5, 0.5}, r]], If[MemberQ[{2, 3, 4, 5, 6}, n], Disk[{p, p}, r]], If[MemberQ[{2, 3, 4, 5, 6}, n], Disk[{Plus[1, Times[-1, p]], Plus[1, Times[-1, p]]}, r]], If[MemberQ[{4, 5, 6}, n], Disk[{p, Plus[1, Times[-1, p]]}, r]], If[MemberQ[{4, 5, 6}, n], Disk[{Plus[1, Times[-1, p]], p}, r]], If[n === 6, {Disk[{p, 0.5}, r], Disk[{Plus[1, Times[-1, p]], 0.5}, r]}]}, ImageSize -> Tiny]]
    
    Format[Dice[n_Integer ? (1 <= #1 <= 6&)], StandardForm] = Block[{p = 0.2, r = 0.05}, Graphics[{EdgeForm[Black], White, Rectangle[], Black, EdgeForm[], If[OddQ[n], Disk[{0.5, 0.5}, r]], If[MemberQ[{2, 3, 4, 5, 6}, n], Disk[{p, p}, r]], If[MemberQ[{2, 3, 4, 5, 6}, n], Disk[{Plus[1, Times[-1, p]], Plus[1, Times[-1, p]]}, r]], If[MemberQ[{4, 5, 6}, n], Disk[{p, Plus[1, Times[-1, p]]}, r]], If[MemberQ[{4, 5, 6}, n], Disk[{Plus[1, Times[-1, p]], p}, r]], If[n === 6, {Disk[{p, 0.5}, r], Disk[{Plus[1, Times[-1, p]], 0.5}, r]}]}, ImageSize -> Tiny]]
    
    Format[Dice[n_Integer ? (1 <= #1 <= 6&)], TeXForm] = Block[{p = 0.2, r = 0.05}, Graphics[{EdgeForm[Black], White, Rectangle[], Black, EdgeForm[], If[OddQ[n], Disk[{0.5, 0.5}, r]], If[MemberQ[{2, 3, 4, 5, 6}, n], Disk[{p, p}, r]], If[MemberQ[{2, 3, 4, 5, 6}, n], Disk[{Plus[1, Times[-1, p]], Plus[1, Times[-1, p]]}, r]], If[MemberQ[{4, 5, 6}, n], Disk[{p, Plus[1, Times[-1, p]]}, r]], If[MemberQ[{4, 5, 6}, n], Disk[{Plus[1, Times[-1, p]], p}, r]], If[n === 6, {Disk[{p, 0.5}, r], Disk[{Plus[1, Times[-1, p]], 0.5}, r]}]}, ImageSize -> Tiny]]
    
    Format[Dice[n_Integer ? (1 <= #1 <= 6&)], TraditionalForm] = Block[{p = 0.2, r = 0.05}, Graphics[{EdgeForm[Black], White, Rectangle[], Black, EdgeForm[], If[OddQ[n], Disk[{0.5, 0.5}, r]], If[MemberQ[{2, 3, 4, 5, 6}, n], Disk[{p, p}, r]], If[MemberQ[{2, 3, 4, 5, 6}, n], Disk[{Plus[1, Times[-1, p]], Plus[1, Times[-1, p]]}, r]], If[MemberQ[{4, 5, 6}, n], Disk[{p, Plus[1, Times[-1, p]]}, r]], If[MemberQ[{4, 5, 6}, n], Disk[{Plus[1, Times[-1, p]], p}, r]], If[n === 6, {Disk[{p, 0.5}, r], Disk[{Plus[1, Times[-1, p]], 0.5}, r]}]}, ImageSize -> Tiny]]

The empty series of dice shall be displayed as an empty dice:

>>> Format[Dice[]] := Graphics[{EdgeForm[Black], White, Rectangle[]}, ImageSize -> Tiny]

>>> Dice[]
  = -Graphics-

Any non-empty series of dice shall be displayed as a row of individual dice:

>>> Format[Dice[d___Integer?(1 <= # <= 6 &)]] := Row[Dice /@ {d}]

>>> Dice[1, 6, 4, 4]
  = -Graphics--Graphics--Graphics--Graphics-

Note that \Mathics will automatically sort the given format rules according to their "generality", so the rule for the empty dice does not get overridden by the rule for a series of dice.
We can still see the original form by using :code:`InputForm` :

>>> Dice[1, 6, 4, 4] // InputForm
  = Dice[1, 4, 4, 6]

We want to combine :code:`Dice`  objects using the :code:`+`  operator:

>>> Dice[a___] + Dice[b___] ^:= Dice[Sequence @@ {a, b}]


The :code:`^:=`  (:code:`UpSetDelayed` ) tells \Mathics to associate this rule with :code:`Dice`  instead of :code:`Plus` .

:code:`Plus`  is protected---we would have to unprotect it first:

>>> Dice[a___] + Dice[b___] := Dice[Sequence @@ {a, b}]
  = $Failed

We can now combine dice:

>>> Dice[1, 5] + Dice[3, 2] + Dice[4]
  = -Graphics--Graphics--Graphics--Graphics--Graphics-
>>> Dice[1, 5] + Dice[3, 2] + Dice[4] // InputForm
  = Dice[1, 2, 3, 4, 5]

Let's write a function that returns the sum of the rolled dice:

>>> DiceSum[Dice[d___]] := Plus @@ {d}

>>> DiceSum @ Dice[1, 2, 5]
  = 8

And now let's put some dice into a table:

>>> Table[{Dice[Sequence @@ d], DiceSum @ Dice[Sequence @@ d]}, {d, {{1, 2}, {2, 2}, {2, 6}}}] // TableForm
  = -Graphics--Graphics-   3
    
    -Graphics--Graphics-   4
    
    -Graphics--Graphics-   8

It is not very sophisticated from a mathematical point of view, but it's beautiful.