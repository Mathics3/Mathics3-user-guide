Django-based Web Interface
==========================

In the future, we plan on providing an interface to Jupyter as a separate package.

However currently as part \Mathics, we distribute a browser-based interface using long-term-release (LTS) Django 4.

Since a Jupyter-based interface seems preferable to the home-grown interface described here, it is doubtful whether there will be future improvements to the this interface.

When you enter Mathics in the top after the Mathics logo and the word "Mathics" you'll see a *menubar*.

It looks like this:

.. image:: menubar.png


These save and load worksheets, share sessions, run a gallery of examples, go to the GitHub organization page, and provide information about the particular Mathics3 installation.

These are explained in the sections below.

.. toctree::
    :maxdepth: 2

    django-based-web-interface/gallery-examples.rst
    django-based-web-interface/keyboard-commands.rst
    django-based-web-interface/persistence-of-mathics-definitions-in-a-session.rst
    django-based-web-interface/saving-loading-and-deleting-worksheets.rst
    django-based-web-interface/uris.rst

