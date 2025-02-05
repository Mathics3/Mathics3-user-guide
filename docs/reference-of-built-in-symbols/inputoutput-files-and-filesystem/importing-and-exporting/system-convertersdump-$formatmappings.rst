System`ConvertersDump`$FormatMappings
=====================================


:code:`System`ConverterDump$FormatMappings`
    Returns a list of associations between file extensions and file types.





The list of MIME types associated to the extension JPEG:

>>> Select[System`ConvertersDump`$FormatMappings,(#1[[2]]=="JPEG")&][[All, 1]]
  = ...
