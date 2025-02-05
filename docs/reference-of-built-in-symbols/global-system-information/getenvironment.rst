GetEnvironment
==============

`WMA link <https://reference.wolfram.com/language/ref/GetEnvironment.html>`_


:code:`GetEnvironment` [":math:`var`"]
    gives the setting corresponding to the variable "var" in the operating       system environment.

:code:`GetEnvironment` [{":math:`var_1`", ":math:`var_2`", ...}]
    gives a list rules for each of the environment variables listed.

:code:`GetEnvironment[]`
    gives a list rules for all environment variables.





On POSIX systems, the following gets the users HOME directory:

>>> GetEnvironment["HOME"]
  = ...

We can get both the HOME directory and the user name in one go:

>>> GetEnvironment[{"HOME", "USER"}]
  = ...

Arguments however must be strings:

>>> GetEnvironment[HOME]
  = GetEnvironment[HOME]

See also `:code:`Environment`  </doc/reference-of-built-in-symbols/global-system-information/environment/>`_ and `:code:`SetEnvironment`  </doc/reference-of-built-in-symbols/global-system-information/setenvironment/>`_.