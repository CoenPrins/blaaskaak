.venv:
	python3 -m venv .venv >/dev/null

venv: .venv
	. .venv/bin/activate

requirements: venv
	pip install -r scripts/requirements.txt

calendar: requirements
	python3 scripts/ical2json.py

build:
	python3 buildsite.py

clean:
	-rm -rd .venv >/dev/null 2>&1 || true
	-rm -rd public >/dev/null 2>&1 || true

serve: build
	python3 -m http.server 8000

github: calendar build

.PHONY: clean venv build serve
