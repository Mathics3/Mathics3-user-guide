SetEnvironment
==============

`WMA link <https://reference.wolfram.com/language/ref/SetEnvironment.html>`_


:code:`SetEnvironment` [":math:`var`" -> ":math:`value`"]
    sets the value of an operating system environment variable.

:code:`SetEnvironment` [{":math:`var`" -> ":math:`value`", ...}]
    sets more than one environment variable.





Set a single environment variable:

>>> SetEnvironment["FOO" -> "bar"]


See that the environment variable has changed:

>>> GetEnvironment["FOO"]
  = FOO -> bar

Set two environment variables:

>>> SetEnvironment[{"FOO" -> "baz", "A" -> "B"}]
  = SetEnvironment[{FOO -> baz, A -> B}]

See that the environment variable has changed:

>>> GetEnvironment["FOO"]
  = FOO -> baz

Environment values must be strings:

>>> SetEnvironment["FOO" -> 5]
  = $Failed
>>> GetEnvironment["FOO"]
  = FOO -> baz

If the environment name is not a string, the evaluation fails without a message.

>>> SetEnvironment[1 -> "bar"]


See also `:code:`Environment`  </doc/reference-of-built-in-symbols/global-system-information/environment/>`_ and `:code:`GeEnvironment`  </doc/reference-of-built-in-symbols/global-system-information/getenvironment/>`_.