LoadModule
==========


:code:`LoadModule` [:math:`module`]
    'Load Mathics definitions from the python module :math:`module`





>>> LoadModule["nomodule"]

    LoadModule::loaderror Python import errors with: No module named 'nomodule'.

    =
:math:`\text{\$Failed}`


>>> LoadModule["sys"]

    LoadModule::notmathicslib Python module "sys" is not a Mathics3 module.

    =
:math:`\text{\$Failed}`


