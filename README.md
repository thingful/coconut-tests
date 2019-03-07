# coconut-tests

Repository that attempts to test the Zenroom coconut scripts via the python wrapper.

## Getting started

On first ensure you include `--recursive` flag to get submodules:

```bash
$ git clone --recursive https://github.com/thingful/coconut-tests.git
```

Alternatively if you need to update you can run:

```bash
$ git submodule update --init --recursive
```

(added to remind myself about submodules).

This little script requires zenroom.py to be installed. Simplest approach is
just to create a virtualenv and then within that virtualenv run:

```bash
$ pip install -r requirements.txt
```

## Running the script

To run all operations for Coconut try running the following from within your
virtualenv:

```bash
$ python coconut-workflow.py
```
