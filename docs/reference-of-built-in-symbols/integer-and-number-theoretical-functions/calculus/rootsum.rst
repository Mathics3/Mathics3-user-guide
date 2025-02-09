RootSum
=======

`WMA link <https://reference.wolfram.com/language/ref/RootSum.html>`_


:code:`RootSum` [:math:`f`, :math:`form`]
    sums :math:`form`[:math:`x`] for all roots of the polynomial :math:`f`[:math:`x`].





Integrating a rational function of any order:

>>> Integrate[1/(x^5 + 11 x + 1), {x, 1, 3}]

    =
:math:`\text{RootSum}\left[-1-212960 \text{\#1}^3-9680 \text{\#1}^2-165 \text{\#1}+41232181 \text{\#1}^5\&,\left(\text{Log}\left[3749971-3512322106304 \text{\#1}^4+453522741 \text{\#1}+16326568676 \text{\#1}^2+79825502416 \text{\#1}^3\right]-4 \text{Log}\left[5\right]\right) \text{\#1}\&\right]-\text{RootSum}\left[-1-212960 \text{\#1}^3-9680 \text{\#1}^2-165 \text{\#1}+41232181 \text{\#1}^5\&,\left(\text{Log}\left[3748721-3512322106304 \text{\#1}^4+453522741 \text{\#1}+16326568676 \text{\#1}^2+79825502416 \text{\#1}^3\right]-4 \text{Log}\left[5\right]\right) \text{\#1}\&\right]`


>>> N[%, 50]

    =
:math:`0.051278805184286949884270940103072421286139857550894`



Simplification of :code:`RootSum`  expression

>>> RootSum[#^5 - 11 # + 1 &, (#^2 - 1)/(#^3 - 2 # + c) &]

    =
:math:`\frac{538-88 c+396 c^2+5 c^3-5 c^4}{97-529 c-53 c^2+88 c^3+c^5}`


>>> RootSum[#^5 - 3 # - 7 &, Sin] //N//Chop

    =
:math:`0.292188`



Use :code:`Normal`  to expand :code:`RootSum` :

>>> RootSum[1+#+#^2+#^3+#^4 &, Log[x + #] &]

    =
:math:`\text{RootSum}\left[1+\text{\#1}^2+\text{\#1}^3+\text{\#1}^4+\text{\#1}\&,\text{Log}\left[x+\text{\#1}\right]\&\right]`


>>> %//Normal

    =
:math:`\text{Log}\left[-\frac{1}{4}-\frac{\sqrt{5}}{4}-I \sqrt{\frac{5}{8}-\frac{\sqrt{5}}{8}}+x\right]+\text{Log}\left[-\frac{1}{4}-\frac{\sqrt{5}}{4}+I \sqrt{\frac{5}{8}-\frac{\sqrt{5}}{8}}+x\right]+\text{Log}\left[-\frac{1}{4}-I \sqrt{\frac{5}{8}+\frac{\sqrt{5}}{8}}+\frac{\sqrt{5}}{4}+x\right]+\text{Log}\left[-\frac{1}{4}+I \sqrt{\frac{5}{8}+\frac{\sqrt{5}}{8}}+\frac{\sqrt{5}}{4}+x\right]`


