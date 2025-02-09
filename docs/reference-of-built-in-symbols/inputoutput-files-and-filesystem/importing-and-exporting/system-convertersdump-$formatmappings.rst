System`ConvertersDump`$FormatMappings
=====================================


:code:`System`ConverterDump$FormatMappings`
    Returns a list of associations between file extensions and file types.





The list of MIME types associated to the extension JPEG:

>>> Select[System`ConvertersDump`$FormatMappings,(#1[[2]]=="JPEG")&][[All, 1]]

    =
:math:`\left\{\text{APPLICATION/JPG},\text{APPLICATION/X-JPG},\text{IMAGE/JPEG},\text{IMAGE/JPG},\text{IMAGE/PJPEG},\text{JPEG},\text{JPG}\right\}`


