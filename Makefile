SHELL := /bin/bash

.PHONY: run
run:
	@docker run --rm -it -v ${PWD}:/work -w /work -p 5173:5173 node:latest bash
