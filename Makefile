VENV := .venv
BUILD := public

PY := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip

$(VENV): requirements.txt
	python3 -m venv $(VENV)
	. $(VENV)/bin/activate
	$(PIP) install --quiet --disable-pip-version-check --require-virtualenv -r requirements.txt
	touch $(VENV)

calendar: $(VENV)
	$(PY) ical2json.py

$(BUILD): $(VENV) pages static buildsite.py base.html
	$(PY) buildsite.py

clean:
	find . -path "./$(VENV)" -exec rm -rd {} +
	find . -path "./$(BUILD)" -exec rm -rd {} +

serve: $(BUILD)
	$(PY) liveserver.py

# for easy CLI targets
virtual-env: $(VENV)
site: $(BUILD)
all: calendar site

.PHONY: calendar site clean serve virtual-env all
.DEFAULT_GOAL := site
