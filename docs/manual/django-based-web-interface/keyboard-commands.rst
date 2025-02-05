Keyboard Commands
=================

There are some keyboard commands you can use in the Django-based Web interface of \Mathics.


:code:`Shift+Return`
    This evaluates the current cell (the most important one, for sure). On the right-hand side, you may also see an "=" button which can be clicked to do the same thing.

:code:`Ctrl+D`
    This moves the cursor over to the documentation pane on the right-hand side. From here you can perform a search for a pre-defined \Mathics function, or symbol. Clicking on the "?" symbol on the right-hand side does the same thing.

:code:`Ctrl+C`
    This moves the cursor back to the document code pane area where you type \Mathics expressions

:code:`Ctrl+S`
    Save worksheet

:code:`Ctrl+O`
    Open worksheet

:code:`Right Click`  on MathML output
    Opens MathJax Menu





Of special note is the last item on the list: right-click to open the MathJax menu. Under "Math Setting"/"Zoom Trigger",  if the zoom trigger is set to a value other than "No Zoom", then when that trigger is applied to MathML-formatted output, the MathML formula pops up a window for the formula. The window can show the formula larger. Also, this is a way to see output that is too large to fit on the display since the window allows for scrolling.

Keyboard command behavior depends on the browser used, the operating system, desktop settings, and customization. We hook into the desktop "Open the current document" and "Save the current document" functions that many desktops provide. For example see: `Finding keyboard shortcuts <https://help.ubuntu.com/community/KeyboardShortcuts#Finding_keyboard_shortcuts>`_

Often, these shortcut keyboard commands are only recognized when a text field has focus; otherwise, the browser might do some browser-specific actions, like setting a bookmark etc.