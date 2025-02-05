$SystemCharacterEncoding
========================

`WMA link <https://reference.wolfram.com/language/ref/$SystemCharacterEncoding.html>`_

$SystemCharacterEncoding
    gives the default character encoding of the system.
    
    On startup, the value of environment variable :code:`MATHICS_CHARACTER_ENCODING`        sets this value. However if that environment variable is not set, set the value       is set in Python using :code:`sys.getdefaultencoding()` .





>>> $SystemCharacterEncoding
  = ...
