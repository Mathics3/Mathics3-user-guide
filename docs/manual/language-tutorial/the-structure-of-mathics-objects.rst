The Structure of \Mathics Objects
=================================

Every expression in \Mathics is built upon the same principle: it consists of a `<head>`_ and an arbitrary number of `<children>`_, unless it is an `<atom>`_, i.e. it can not be subdivided any further. To put it another way: everything is a function call. This can be best seen when displaying expressions in their "full form":

>>> FullForm[a + b + c]

    =
:math:`\text{Plus}\left[a, b, c\right]`



Nested calculations are nested function calls:

>>> FullForm[a + b * (c + d)]

    =
:math:`\text{Plus}\left[a, \text{Times}\left[b, \text{Plus}\left[c, d\right]\right]\right]`



Even lists are function calls of the function :code:`List` :

>>> Head[{1, 2, 3}]

    =
:math:`\text{List}`



However, its full form is presented with :code:`{...}` 

>>> FullForm[{1, 2, 3}]

    =
:math:`\left\{1,2,3\right\}`



The head of an expression can be determined with :code:`Head` :

>>> Head[a + b + c]

    =
:math:`\text{Plus}`



The children of an expression can be accessed like list elements:

>>> (a + b + c)[[2]]

    =
:math:`b`



The head is the 0th element:

>>> (a + b + c)[[0]]

    =
:math:`\text{Plus}`



The head of an expression can be exchanged using the function :code:`Apply` :

>>> Apply[g, f[x, y]]

    =
:math:`g\left[x,y\right]`


>>> Apply[Plus, a * b * c]

    =
:math:`a+b+c`



:code:`Apply`  can be written using the operator :code:`@@` :

>>> Times @@ {1, 2, 3, 4}

    =
:math:`24`



(This exchanges the head :code:`List`  of :code:`{1, 2, 3, 4}`  with :code:`Times` , and then the expression :code:`Times[1, 2, 3, 4]`  is evaluated, yielding 24.)
:code:`Apply`  can also be applied on a certain `<level>`_ of an expression:

>>> Apply[f, {{1, 2}, {3, 4}}, {1}]

    =
:math:`\left\{f\left[1,2\right],f\left[3,4\right]\right\}`



Or even on a range of levels:

>>> Apply[f, {{1, 2}, {3, 4}}, {0, 2}]

    =
:math:`f\left[f\left[1,2\right],f\left[3,4\right]\right]`



:code:`Apply`  is similar to :code:`Map`  (:code:`/@` ):

>>> Map[f, {1, 2, 3, 4}]

    =
:math:`\left\{f\left[1\right],f\left[2\right],f\left[3\right],f\left[4\right]\right\}`


>>> f /@ {{1, 2}, {3, 4}}

    =
:math:`\left\{f\left[\left\{1,2\right\}\right],f\left[\left\{3,4\right\}\right]\right\}`



The atoms of \Mathics are numbers, symbols, and strings. :code:`AtomQ`  tests whether an expression is an atom:

>>> AtomQ[5]

    =
:math:`\text{True}`


>>> AtomQ[a + b]

    =
:math:`\text{False}`



The full form of rational and complex numbers looks like they were compound expressions:

>>> FullForm[3 / 5]

    =
:math:`\text{Rational}\left[3, 5\right]`


>>> FullForm[3 + 4 I]

    =
:math:`\text{Complex}\left[3, 4\right]`



However, they are still atoms, thus unaffected by applying functions, for instance:

>>> f @@ Complex[3, 4]

    =
:math:`3+4 I`



Nevertheless, every atom has a head:

>>> Head /@ {1, 1/2, 2.0, I, "a string", x}

    =
:math:`\left\{\text{Integer},\text{Rational},\text{Real},\text{Complex},\text{String},\text{Symbol}\right\}`



The operator :code:`===`  tests whether two expressions are the same on a structural level:

>>> 3 === 3

    =
:math:`\text{True}`


>>> 3 == 3.0

    =
:math:`\text{True}`



But:

>>> 3 === 3.0

    =
:math:`\text{False}`



because :code:`3`  (an :code:`Integer` ) and :code:`3.0`  (a :code:`Real` ) are structurally different.