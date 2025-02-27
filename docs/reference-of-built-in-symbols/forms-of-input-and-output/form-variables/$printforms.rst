$PrintForms
===========


:code:`$PrintForms`
    contains the list of basic print forms. It is updated automatically when new :code:`PrintForms`  are defined by setting format values.





>>> $PrintForms

    =
:math:`\left\{\text{InputForm},\text{PythonForm},\text{SympyForm},\text{TraditionalForm},\text{MathMLForm},\text{TeXForm},\text{StandardForm},\text{FullForm},\text{OutputForm},\text{MyForm}\right\}`



Suppose now that we want to add a new format :code:`MyForm` . Initially, it does not belong to :code:`$PrintForms` :

>>> MemberQ[$PrintForms, MyForm]

    =
:math:`\text{True}`



Now, let's define a format rule:

>>> Format[F[x_], MyForm] := "F<<" <> ToString[x] <> ">>"



Now, the new format belongs to the :code:`$PrintForms`  list

>>> MemberQ[$PrintForms, MyForm]

    =
:math:`\text{True}`


