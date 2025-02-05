NValues
=======


:code:`NValues` [:math:`symbol`]
    gives the list of numerical values associated with :math:`symbol`.
    
    *Note: this function is in Mathematica 5 but has been removed from           current Mathematica.*





>>> NValues[a]
  = {}
>>> N[a] = 3;

>>> NValues[a]
  = {HoldPattern[N[a, MachinePrecision]] :> 3}

You can assign values to :code:`NValues` :

>>> NValues[b] := {N[b, MachinePrecision] :> 2}

>>> N[b]
  = 2.

Be sure to use :code:`SetDelayed` , otherwise the left-hand side of the     transformation rule will be evaluated immediately,     causing the head of :code:`N`  to get lost. Furthermore, you have to     include the precision in the rules; :code:`MachinePrecision`      will not be inserted automatically:

>>> NValues[c] := {N[c] :> 3}

>>> N[c]
  = c

Mathics will assign any list of rules to :code:`NValues` ; however,     inappropriate rules will never be used:

>>> NValues[d] = {foo -> bar};

>>> NValues[d]
  = {HoldPattern[foo] :> bar}
>>> N[d]
  = d
