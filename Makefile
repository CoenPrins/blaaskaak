GCAL_URL := "https://calendar.google.com/calendar/ical/3d4cae9300502ef446e65cc6d4434f3e39e818a3b34bd9d42c9c3b567b779a3f%40group.calendar.google.com/public/basic.ics"

static/events.ics:
	curl $(GCAL_URL) > $@

prerequisite: static/events.ics

build: | prerequisite
	hugo

dev:
	hugo serve -D
