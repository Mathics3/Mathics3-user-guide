HoldAllComplete
===============

`WMA link <https://reference.wolfram.com/language/ref/HoldAllComplete.html>`_


:code:`HoldAllComplete`
    is an attribute that includes the effects of :code:`HoldAll`  and          :code:`SequenceHold` , and also protects the function from being           affected by the upvalues of any arguments.





:code:`HoldAllComplete`  even prevents upvalues from being used, and     includes :code:`SequenceHold` .

>>> SetAttributes[f, HoldAllComplete]

>>> f[a] ^= 3;

>>> f[a]
  = f[a]
>>> f[Sequence[a, b]]
  = f[Sequence[a, b]]
