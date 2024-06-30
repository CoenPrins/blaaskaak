VENV := .venv
BUILD := public

export PATH := $(VENV)/bin:$(PATH)
SHELL := env PATH=$(PATH) /bin/bash

$(VENV): requirements.txt
	python3 -m venv $(VENV)
	. $(VENV)/bin/activate
	pip install --quiet --disable-pip-version-check --require-virtualenv -r requirements.txt
	touch $(VENV)

calendar: $(VENV)
	python3 ical2json.py

$(BUILD): pages static buildsite.py base.html
	python3 buildsite.py

clean:
	find . -path "./$(VENV)" -exec rm -rd {} +
	find . -path "./$(BUILD)" -exec rm -rd {} +

serve: $(BUILD)
	python3 liveserver.py

site: $(BUILD)
all: calendar site

.PHONY: calendar site clean serve all
.DEFAULT_GOAL := site
