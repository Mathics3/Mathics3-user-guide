$PrintForms
===========


:code:`$PrintForms`
    contains the list of basic print forms. It is updated automatically when new :code:`PrintForms`  are defined by setting format values.





>>> $PrintForms
  = ...

Suppose now that we want to add a new format :code:`MyForm` . Initially, it does not belong to :code:`$PrintForms` :

>>> MemberQ[$PrintForms, MyForm]
  = False

Now, let's define a format rule:

>>> Format[F[x_], MyForm] := "F<<" <> ToString[x] <> ">>"


Now, the new format belongs to the :code:`$PrintForms`  list

>>> MemberQ[$PrintForms, MyForm]
  = True
