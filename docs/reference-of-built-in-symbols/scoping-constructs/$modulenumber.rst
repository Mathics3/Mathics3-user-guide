$ModuleNumber
=============

`WMA link <https://reference.wolfram.com/language/ref/$ModuleNumber.html>`_

:code:`$ModuleNumber`
    is the current "serial number" to be used for local module variables.






<ul>
<li>:code:`$ModuleNumber`  is incremented every time :code:`Module`  or :code:`Unique`  is called.
<li> a Mathics session starts with :code:`$ModuleNumber`  set to 1.
<li> You can reset :code:`$ModuleNumber`  to a positive machine integer, but if you do so, naming conflicts may lead to inefficiencies.
</li>