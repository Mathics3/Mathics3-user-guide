PIP ?= pip3
RM  ?= rm
PYTHON ?= python

# Variable indicating Mathics3 Modules you have available on your system, in latex2doc option format
MATHICS3_MODULE_OPTION ?=--load-module pymathics.trepan,pymathics.graph,pymathics.natlang

#: Default target - same as "develop"
all: doctest-data rst-documentation user-docs

.PHONY: developer-docs clean


doctest-data: setup
	MATHICS_CHARACTER_ENCODING="UTF-8" $(PYTHON) -m mathics.docpipeline --output $(MATHICS3_MODULE_OPTION)
	$(PYTHON) generate/testdata.py

rst-documentation:
	$(PYTHON) generate/doc2rst.py $(MATHICS3_MODULE_OPTION)

#: Build developer guide
user-docs:
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

