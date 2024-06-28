VENV := .venv
BUILD := public
export PATH := .:$(VENV)/bin:$(PATH)
SHELL := env PATH=$(PATH) /bin/bash

$(VENV): requirements.txt
	python3 -m venv $(VENV)
	. $(VENV)/bin/activate
	pip install --quiet --disable-pip-version-check --require-virtualenv -r requirements.txt
	touch .venv

calendar:
	python3 scripts/ical2json.py

build:
	python3 buildsite.py

clean:
	-rm -rd $(VENV) >/dev/null 2>&1 || true
	-rm -rd $(BUILD) >/dev/null 2>&1 || true

serve: build
	python3 -m http.server 8000 --directory $(BUILD)

all: calendar build

.PHONY: calendar build clean serve all
