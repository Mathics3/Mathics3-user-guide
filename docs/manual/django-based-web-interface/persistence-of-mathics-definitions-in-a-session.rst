Persistence of Mathics Definitions in a Session
===============================================

When you use the Django-based Web interface of \Mathics, a browser session is created. Cookies have to be enabled to allow this. Your session holds a key that is used to access your definitions that are stored in a database on the server. As long as you don't clear the cookies in your browser, your definitions will remain even when you close and re-open the browser.

This implies that you should not store sensitive, private information in \Mathics variables when using the online Web interface. In addition to their values being stored in a database on the server, your queries might be saved for debugging purposes. However, the fact that they are transmitted over plain HTTP should make you aware that you should not transmit any sensitive information. When you want to do calculations with that kind of stuff, simply install \Mathics locally!

If you are using a public terminal, to erase all your definitions and close the browser window. When you use \Mathics in a browser, use the command :code:`Quit[]`  or its alias, :code:`Exit[]` .

When you reload the current page in a browser using the default URL, e.g.,  :code:`http:localhost:8000` , all of the previous input and output disappears.

On the other hand, Definitions as described above do not, unless :code:`Quit[]`  or :code:`Exit[]`  is entered as described above.

If you want a URL that records the input entered, the `<Generate Input Hash>`_ button does this. The button looks like this:

.. image:: generate-hash-button.png


For example, assuming you have a \Mathics server running at port 8000 on  :code:`localhost` , and you enter the URL  :code:`http://localhost:8000/#cXVlcmllcz14` , you should see a single line of input containing :code:`x`  entered.

Of course, what the value of this is when evaluated depends on whether :code:`x`  has been previously defined.