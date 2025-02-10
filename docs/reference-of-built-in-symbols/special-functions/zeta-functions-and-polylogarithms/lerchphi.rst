LerchPhi
========

`Lerch transcendent <https://en.wikipedia.org/wiki/Lerch_transcendent>`_ (`WMA <https://reference.wolfram.com/language/ref/LerchPhi.html>`_)


:code:`LerchPhi[z,s,a]`
    gives the Lerch transcendent :math:`\Phi(z,s,a)`.





>>> LerchPhi[2, 3, -1.5]

    =
:math:`19.3893-2.1346 I`


>>> LerchPhi[1, 2, 1/4] == 8 Catalan + Pi^2

    =
:math:`17.1973`



Plot between between -1 and 1:

>>> Plot[LerchPhi[x, 1, 2], {x, -1, 1}]
    = -Graphics-`

