Symbols and Assignments
=======================

Symbols need not be declared in \Mathics, they can just be entered and remain variable:

>>> x
    =

:math:`x`



Basic simplifications are performed:

>>> x + 2 x
    =

:math:`3 x`



Symbols can have any name that consists of characters and digits:

>>> iAm1Symbol ^ 2
    =

:math:`\text{iAm1Symbol}^2`



You can assign values to symbols:

>>> a = 2
    =

:math:`2`


>>> a ^ 3
    =

:math:`8`


>>> a = 4
    =

:math:`4`


>>> a ^ 3
    =

:math:`64`



Assigning a value returns that value. If you want to suppress the output of any result, add a :code:`;`  to the end of your query:

>>> a = 4;



Values can be copied from one variable to another:

>>> b = a;



Now changing :code:`a`  does not affect :code:`b` :

>>> a = 3;


>>> b
    =

:math:`4`



Such a dependency can be achieved by using "delayed assignment" with the :code:`:=`  operator (which does not return anything, as the right side is not even evaluated):

>>> b := a ^ 2


>>> b
    =

:math:`9`


>>> a = 5;


>>> b
    =

:math:`25`


