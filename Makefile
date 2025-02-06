PIP ?= pip3
RM  ?= rm
PYTHON ?= python

#: Default target - same as "develop"
all: user-docs

.PHONY: developer-docs clean

#: Build developer guide
user-docs: setup
	$(PYTHON) generate/doc2rst.py
	$(MAKE) -C docs html latexpdf


#: Install necessary Python modules
setup:
	pip install -r requirements.txt

#: Rebuild docs from scratch
build rebuild:
	$(MAKE) -C docs $<

#: Wipe derivable files
clean:
	$(MAKE) -C docs $<

