PIP ?= pip3
RM  ?= rm
PYTHON ?= python

# Variable indicating Mathics3 Modules you have available on your system, in latex2doc option format
MATHICS3_MODULE_OPTION ?=--load-module pymathics.trepan,pymathics.graph,pymathics.natlang

#: Default target - same as "develop"
all: user-docs

.PHONY: developer-docs clean

#: Build developer guide
user-docs: setup
	$(PYTHON) -m mathics.docpipeline --output --keep-going $(MATHICS3_MODULE_OPTION)
	$(PYTHON) generate/testdata.py
	$(PYTHON) generate/doc2rst.py $(MATHICS3_MODULE_OPTION)
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

