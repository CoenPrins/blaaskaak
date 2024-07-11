VENV := .venv
BUILD_DIR := public

all: calendar site

$(BUILD_DIR):
	mkdir -p $@

$(BUILD_DIR)/%: static/% $(BUILD_DIR)
	cp -R $< $@; touch $@

static: $(subst static,$(BUILD_DIR),$(wildcard static/*))

$(BUILD_DIR)/%: pages/% $(BUILD_DIR)
	sed '/MAIN/r $<' base.html > $@

pages: $(subst pages,$(BUILD_DIR),$(wildcard pages/*))

site: static pages

$(VENV): scripts/requirements.txt
	python3 -m venv --clear $@
	$(VENV)/bin/pip install --quiet --disable-pip-version-check -r $^
	touch $@

calendar: $(VENV) $(BUILD_DIR)
	$(VENV)/bin/python3 scripts/ical2json.py "$(BUILD_DIR)/events.json"

clean-venv:
	find . -path "./$(VENV)" -exec rm -rd {} +

clean-build:
	find . -path "./$(BUILD_DIR)" -exec rm -rd {} +

clean: clean-venv clean-build

# TODO: add html/css/js
format: $(VENV)
	$(VENV)/bin/black scripts/*.py

.PHONY: static pages site calendar clean-*
