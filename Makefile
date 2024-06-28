VENV := .venv
export PATH := $(VENV)/bin:$(PATH)

$(VENV): scripts/requirements.txt
	python3 -m venv $(VENV) >/dev/null
	. $(VENV)/bin/activate
	pip install -r scripts/requirements.txt >/dev/null

calendar: $(VENV)
	python3 scripts/ical2json.py

build:
	python3 buildsite.py

clean:
	-rm -rd .venv >/dev/null 2>&1 || true
	-rm -rd public >/dev/null 2>&1 || true

serve: build
	python3 -m http.server 8000

github-actions: calendar build

.PHONY: clean venv build serve
