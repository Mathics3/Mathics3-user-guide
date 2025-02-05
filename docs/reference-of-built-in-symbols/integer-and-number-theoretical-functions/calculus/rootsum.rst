RootSum
=======

`WMA link <https://reference.wolfram.com/language/ref/RootSum.html>`_


:code:`RootSum` [:math:`f`, :math:`form`]
    sums :math:`form`[:math:`x`] for all roots of the polynomial :math:`f`[:math:`x`].





Integrating a rational function of any order:

>>> Integrate[1/(x^5 + 11 x + 1), {x, 1, 3}]
  = RootSum[-1 - 212960 #1 ^ 3 - 9680 #1 ^ 2 - 165 #1 + 41232181 #1 ^ 5&, (Log[3749971 - 3512322106304 #1 ^ 4 + 453522741 #1 + 16326568676 #1 ^ 2 + 79825502416 #1 ^ 3] - 4 Log[5]) #1&] - RootSum[-1 - 212960 #1 ^ 3 - 9680 #1 ^ 2 - 165 #1 + 41232181 #1 ^ 5&, (Log[3748721 - 3512322106304 #1 ^ 4 + 453522741 #1 + 16326568676 #1 ^ 2 + 79825502416 #1 ^ 3] - 4 Log[5]) #1&]
>>> N[%, 50]
  = 0.051278805184286949884270940103072421286139857550894

Simplification of :code:`RootSum`  expression

>>> RootSum[#^5 - 11 # + 1 &, (#^2 - 1)/(#^3 - 2 # + c) &]
  = (538 - 88 c + 396 c ^ 2 + 5 c ^ 3 - 5 c ^ 4) / (97 - 529 c - 53 c ^ 2 + 88 c ^ 3 + c ^ 5)
>>> RootSum[#^5 - 3 # - 7 &, Sin] //N//Chop
  = 0.292188

Use :code:`Normal`  to expand :code:`RootSum` :

>>> RootSum[1+#+#^2+#^3+#^4 &, Log[x + #] &]
  = RootSum[1 + #1 ^ 2 + #1 ^ 3 + #1 ^ 4 + #1&, Log[x + #1]&]
>>> %//Normal
  = Log[-1 / 4 - Sqrt[5] / 4 - I Sqrt[5 / 8 - Sqrt[5] / 8] + x] + Log[-1 / 4 - Sqrt[5] / 4 + I Sqrt[5 / 8 - Sqrt[5] / 8] + x] + Log[-1 / 4 - I Sqrt[5 / 8 + Sqrt[5] / 8] + Sqrt[5] / 4 + x] + Log[-1 / 4 + I Sqrt[5 / 8 + Sqrt[5] / 8] + Sqrt[5] / 4 + x]
