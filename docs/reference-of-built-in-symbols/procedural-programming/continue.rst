Continue
========

`WMA link <https://reference.wolfram.com/language/ref/Continue.html>`_


:code:`Continue[]`
    continues with the next iteration in a :code:`For` , :code:`While` , or :code:`Do`  loop.





>>> For[i=1, i<=8, i=i+1, If[Mod[i,2] == 0, Continue[]]; Print[i]]

