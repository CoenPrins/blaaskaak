VENV := .venv
BUILD := public

PY := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip

$(VENV): requirements.txt
	python3 -m venv --clear $(VENV)
	$(PIP) install --quiet --disable-pip-version-check -r requirements.txt
	touch $(VENV)

calendar: $(VENV)
	$(PY) ical2json.py "$(BUILD)/events.json"

site: $(VENV)
	$(PY) buildsite.py

serve: $(BUILD)
	$(PY) liveserver.py "$(BUILD)"

clean:
	find . -path "./$(VENV)" -exec rm -rd {} +
	find . -path "./$(BUILD)" -exec rm -rd {} +

# TODO: add html/css/js
format: $(VENV)
	$(VENV)/bin/black *.py

# for easy CLI targets
virtual-env: $(VENV)
all: site calendar

.PHONY: calendar site clean serve virtual-env all
.DEFAULT_GOAL := site
