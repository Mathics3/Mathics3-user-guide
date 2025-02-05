Compile
=======

`WMA link <https://reference.wolfram.com/language/ref/Compile.html>`_


:code:`Compile` [{:math:`x_1`, :math:`x_2`, ...}, :math:`expr`]
    Compiles :math:`expr` assuming each :math:`xi` is a :math:`Real` number.

:code:`Compile` [{{:math:`x_1`, :math:`t_1`} {:math:`x_2`, :math:`t_1`} ...}, :math:`expr`]
    Compiles assuming each :math:`x_i` matches type :math:`t_i`.





Compilation is performed using llvmlite , or Python's builtin
"compile" function.

>>> cf = Compile[{x, y}, x + 2 y]
  = CompiledFunction[{x, y}, x + 2 y, ...]
>>> cf[2.5, 4.3]
  = 11.1
>>> cf = Compile[{{x, _Real}}, Sin[x]]
  = CompiledFunction[{x}, Sin[x], ...]
>>> cf[1.4]
  = 0.98545

Compile supports basic flow control:

>>> cf = Compile[{{x, _Real}, {y, _Integer}}, If[x == 0.0 && y <= 0, 0.0, Sin[x ^ y] + 1 / Min[x, 0.5]] + 0.5]
  = CompiledFunction[{x, y}, ...]
>>> cf[3.5, 2]
  = 2.18888

Loops and variable assignments are supported usinv Python builtin "compile" function:

>>> Compile[{{a, _Integer}, {b, _Integer}}, While[b != 0, {a, b} = {b, Mod[a, b]}]; a]       (* GCD of a, b *)
  = CompiledFunction[{a, b}, a, -PythonizedCode-]
