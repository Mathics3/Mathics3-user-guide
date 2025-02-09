Defining, applying and compiling rules.
=======================================

`WMA link <https://reference.wolfram.com/language/guide/Rules.html>`_


Rules are a basic element in the evaluation process. Every Definition in \Mathics consists of a set of rules associated with a symbol. The evaluation process consists of the sequential application of rules associated with the symbols appearing in a given expression. The process iterates until no rules match the final expression.

In \Mathics, rules consist of a Pattern object :math:`pat` and an Expression :math:`repl`. When the Rule is applied to a symbolic Expression :math:`expr`, the interpreter tries to match the pattern with subexpressions of :math:`expr` in a top-to-bottom way. If a match is found, the subexpression is then replaced by :math:`repl`.

If the :math:`pat` includes named subpatterns, symbols in :math:`repl` associated with that name are replaced by the (sub) match in the final expression.

Let us consider, for example, the :code:`Rule` :

>>> rule = F[u_]->g[u]

    =
:math:`F\left[\text{u\_}\right]->g\left[u\right]`



This rule associates the pattern :code:`F[u_]`  with the expression :code:`g[u]` .

Then, using the :code:`Replace`  operator :code:`/.`  we can apply the rule to an expression

>>> a + F[x ^ 2] /. rule

    =
:math:`a+g\left[x^2\right]`



Notice that the rule is applied from top to bottom just once:

>>> a + F[F[x ^ 2]] /. rule

    =
:math:`a+g\left[F\left[x^2\right]\right]`



Here, the subexpression :code:`F[F[x^2]]`  matches with the pattern, and the named subpattern :code:`u_`  matches with :code:`F[x^2]` . The original expression is then replaced by :code:`g[u]` , and :code:`u`  is replaced with the subexpression that matches the subpattern (:code:`F[x ^ 2]` ).

Notice also that the rule is applied just once. We can apply it recursively until no further matches are found by using the :code:`ReplaceRepeated`  operator :code:`//.` :

>>> a + F[F[x ^ 2]] //. rule

    =
:math:`a+g\left[g\left[x^2\right]\right]`



Rules are kept as expressions until a :code:`Replace`  expression is evaluated. At that moment, :code:`Pattern`  objects are :code:`compiled` , taking into account the attributes of the symbols involved. To make the repeated application of the same rule over different expressions faster, it is convenient to use :code:`Dispatch`  tables. These expressions store precompiled versions of a list of rules, avoiding repeating the :code:`compilation`  step each time the rules are applied.

>>> dispatchrule = Dispatch[{rule}]

    =
:math:`\text{Dispatch}\left[\text{<1>}\right]`


>>> a + F[F[x ^ 2]] //. dispatchrule

    =
:math:`a+g\left[g\left[x^2\right]\right]`




.. toctree::
    :maxdepth: 2

    defining-applying-and-compiling-rules/dispatch.rst
    defining-applying-and-compiling-rules/replace.rst
    defining-applying-and-compiling-rules/replaceall.rst
    defining-applying-and-compiling-rules/replacelist.rst
    defining-applying-and-compiling-rules/replacerepeated.rst
    defining-applying-and-compiling-rules/ruledelayed.rst
    defining-applying-and-compiling-rules/rule.rst

