Working with Lists
==================

Lists can be entered in \Mathics with curly braces :code:`{`  and :code:`}` :

>>> mylist = {a, b, c, d}

    =
:math:`\left\{a,b,c,d\right\}`



There are various functions for constructing lists:

>>> Range[5]

    =
:math:`\left\{1,2,3,4,5\right\}`


>>> Array[f, 4]

    =
:math:`\left\{f\left[1\right],f\left[2\right],f\left[3\right],f\left[4\right]\right\}`


>>> ConstantArray[x, 4]

    =
:math:`\left\{x,x,x,x\right\}`


>>> Table[n ^ 2, {n, 2, 5}]

    =
:math:`\left\{4,9,16,25\right\}`



The number of elements of a list can be determined with :code:`Length` :

>>> Length[mylist]

    =
:math:`4`



Elements can be extracted using double square braces:

>>> mylist[[3]]

    =
:math:`c`



Negative indices count from the end:

>>> mylist[[-3]]

    =
:math:`b`



Lists can be nested:

>>> mymatrix = {{1, 2}, {3, 4}, {5, 6}};



There are alternate forms to display lists:

>>> TableForm[mymatrix]

    =
:math:`\begin{array}{cc} 1 & 2\\ 3 & 4\\ 5 & 6\end{array}`


>>> MatrixForm[mymatrix]

    =
:math:`\left(\begin{array}{cc} 1 & 2\\ 3 & 4\\ 5 & 6\end{array}\right)`



There are various ways of extracting elements from a list:

>>> mymatrix[[2, 1]]

    =
:math:`3`


>>> mymatrix[[;;, 2]]

    =
:math:`\left\{2,4,6\right\}`


>>> Take[mylist, 3]

    =
:math:`\left\{a,b,c\right\}`


>>> Take[mylist, -2]

    =
:math:`\left\{c,d\right\}`


>>> Drop[mylist, 2]

    =
:math:`\left\{c,d\right\}`


>>> First[mymatrix]

    =
:math:`\left\{1,2\right\}`


>>> Last[mylist]

    =
:math:`d`


>>> Most[mylist]

    =
:math:`\left\{a,b,c\right\}`


>>> Rest[mylist]

    =
:math:`\left\{b,c,d\right\}`



Lists can be used to assign values to multiple variables at once:

>>> {a, b} = {1, 2};


>>> a

    =
:math:`1`


>>> b

    =
:math:`2`



Operations like addition and multiplication, "thread" over lists; lists are combined element-wise:

>>> {1, 2, 3} + {4, 5, 6}

    =
:math:`\left\{5,7,9\right\}`


>>> {1, 2, 3} * {4, 5, 6}

    =
:math:`\left\{4,10,18\right\}`



It is an error to combine lists with unequal lengths:

>>> {1, 2} + {4, 5, 6}

    Thread::tdlen Objects of unequal length cannot be combined.

    =
:math:`\left\{1,2\right\}+\left\{4,5,6\right\}`


