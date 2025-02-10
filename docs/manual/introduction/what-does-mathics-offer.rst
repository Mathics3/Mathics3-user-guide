What does \Mathics offer?
=========================

Because \Mathics is compatible with the Wolfram-Language kernel within the
confines of the Python ecosystem, it is a powerful functional
programming language, driven by pattern matching and rule application.

Primitive types include rationals, complex numbers, and arbitrary-precision numbers. Other primitive types such as images or graphs, or NLP come from the various Python libraries that \Mathics uses.

Outside of the "core" \Mathics kernel (which has only a primitive command-line interface), in separate GitHub projects, as add-ons, there are:



- a `command-line interface <https://pypi.org/project/mathicsscript/>`_ using either `prompt-toolkit <https://python-prompt-toolkit.readthedocs.io/en/master/>`_, or GNU Readline

- a `Django-based web server <https://pypi.org/project/Mathics-Django/>`_

- a `A browser-based no-install online front-end <https://mathics3.github.io/Mathics3-live/>`_

- a `Mathics3 module for Graphs <https://pypi.org/project/pymathics-graph/>`_ (via `NetworkX <https://networkx.org/>`_),

- a `Mathics3 module for NLP <https://pypi.org/project/pymathics-natlang/>`_ (via `nltk <https://www.nltk.org/>`_, `spacy <https://spacy.io/>`_, and others)

- a `Mathics3 Debugger Module <https://pypi.org/project/Mathics3-trepan/>`_ (experimental)

- a `A docker container <https://hub.docker.com/r/mathicsorg/mathics>`_ which bundles all of the above


