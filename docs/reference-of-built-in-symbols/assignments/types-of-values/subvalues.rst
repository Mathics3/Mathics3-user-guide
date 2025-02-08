SubValues
=========

`WMA link <https://reference.wolfram.com/language/ref/SubValues.html>`_


:code:`SubValues` [:math:`symbol`]
    gives the list of subvalues associated with :math:`symbol`.
    
    *Note: this function is not in current Mathematica.*





>>> f[1][x_] := x


>>> f[2][x_] := x ^ 2


>>> SubValues[f]
    =

:math:`\left\{\text{HoldPattern}\left[f\left[2\right]\left[\text{x\_}\right]\right]\text{:>}x^2,\text{HoldPattern}\left[f\left[1\right]\left[\text{x\_}\right]\right]\text{:>}x\right\}`


>>> Definition[f]
    =

:math:`\begin{array}{l} f\left[2\right]\left[\text{x\_}\right]=x^2\\ f\left[1\right]\left[\text{x\_}\right]=x\end{array}`


