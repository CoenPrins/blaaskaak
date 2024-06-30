import datetime
import html
import json
import os
import sys
from urllib.request import urlopen

from pathlib import Path

import ics


def request_ics_calendar() -> ics.icalendar.Calendar:
    try:
        ics_url = os.environ["ICS_URL"]
    except KeyError:
        print("ical2json: environment variable ICS_URL not set", file=sys.stderr)
        print('ical2json: set using `export ICS_URL="<google_url>"`', file=sys.stderr)
        sys.exit(1)

    with urlopen(ics_url) as response:
        calendar = ics.icalendar.Calendar(response.read().decode("utf-8"))

    return calendar


def convert_ics(ical: ics.icalendar.Calendar) -> list[dict[str, str | None]]:
    events = []
    for event in sorted(ical.events, key=lambda t: t.begin):
        # ignore private events
        if event.name == "Busy":
            continue
        events.append(
            {
                "name": event.name,
                "begin": event.begin.isoformat(),
                "end": event.end.isoformat(),
                "description": html.unescape(event.description or ""),
                "location": event.location or "",
                "url": event.url,
            }
        )

    return events


def write_json(events: list[dict[str, str | None]], filename: str) -> None:
    fn = Path(filename)
    fn.parent.mkdir(exist_ok=True)

    with open(fn, "w") as f:
        f.write(
            json.dumps(
                {
                    "metadata": {
                        "generated": datetime.datetime.now().isoformat(),
                        # NOTE: you can add more metadata if you want here
                    },
                    "events": events,
                }
            )
        )


if __name__ == "__main__":
    ical = request_ics_calendar()
    events = convert_ics(ical)

    # if path is provided on command line
    output_filename = "static/events.json"
    if len(sys.argv) > 1:
        output_filename = sys.argv[1]

    write_json(events, filename=output_filename)
