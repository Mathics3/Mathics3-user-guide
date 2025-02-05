Do
==

`WMA link <https://reference.wolfram.com/language/ref/Do.html>`_


:code:`Do` [:math:`expr`, {:math:`max`}]
    evaluates :math:`expr` :math:`max` times.

:code:`Do` [:math:`expr`, {:math:`i`, :math:`max`}]
    evaluates :math:`expr` :math:`max` times, substituting :math:`i` in :math:`expr` with values from 1 to
    :math:`max`.

:code:`Do` [:math:`expr`, {:math:`i`, :math:`min`, :math:`max`}]
    starts with :code:`:math:`i` = :math:`max`` .

:code:`Do` [:math:`expr`, {:math:`i`, :math:`min`, :math:`max`, :math:`step`}]
    uses a step size of :math:`step`.

:code:`Do` [:math:`expr`, {:math:`i`, {:math:`i_1`, :math:`i_2`, ...}}]
    uses values :math:`i_1`, :math:`i_2`, ... for :math:`i`.

:code:`Do` [:math:`expr`, {:math:`i`, :math:`i_{min}`, :math:`i_{max}`}, {:math:`j`, :math:`j_{min}`, :math:`j_{max}`}, ...]
    evaluates :math:`expr` for each :math:`j` from :math:`j_{min}` to :math:`j_{max}`, for each :math:`i` from :math:`i_{min}`
    to :math:`i_{max}`, etc.





>>> Do[Print[i], {i, 2, 4}]

>>> Do[Print[{i, j}], {i,1,2}, {j,3,5}]


You can use :code:`Break[]`  and :code:`Continue[]`  inside :code:`Do` :

>>> Do[If[i > 10, Break[], If[Mod[i, 2] == 0, Continue[]]; Print[i]], {i, 5, 20}]

