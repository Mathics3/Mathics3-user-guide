SetFileDate
===========

`WMA link <https://reference.wolfram.com/language/ref/SetFileDate.html>`_


:code:`SetFileDate` [":math:`file`"]
    set the file access and modification dates of :math:`file` to the current date.

:code:`SetFileDate` [":math:`file`", :math:`date`]
    set the file access and modification dates of :math:`file` to the specified date list.

:code:`SetFileDate` [":math:`file`", :math:`date`, ":math:`type`"]
    set the file date of :math:`file` to the specified date list.
    The ":math:`type`" can be one of ":math:`Access`", ":math:`Creation`", ":math:`Modification`", or :code:`All` .





Create a temporary file (for example purposes)

>>> tmpfilename = $TemporaryDirectory <> "/tmp0";


>>> Close[OpenWrite[tmpfilename]];


>>> SetFileDate[tmpfilename, {2002, 1, 1, 0, 0, 0.}, "Access"];


>>> DeleteFile[tmpfilename]
    = `

