This script is used in the Github Actions workflow
[`refresh-events.yml`](../.github/workflows/refresh-events.yml). It converts a
public Google Calendar to JSON format, ready to be read by the static website.
It grabs the following fields from the ICS data format:

- Title (string)
- Start datetime (ISO 8601 format string)
- End datetime (ISO 8601 format string)
- Location (string)
- Notes (string)
- URL (string) [not tested yet]

The standard filename of the resulting json file is `"../events.json"`. This
means that if you run `ical2json.py` in its folder (`/scripts`), the event.json
file will be placed in the root of the repository.

## Requirements

Requires Python3.11 and the ics package.

```
python3 -m pip install requirements.txt
```

After that, find the [public url to your Google
Calendar](https://support.google.com/calendar/answer/37083) and set the
environment variable `ICS_URL` like so:

```
export ICS_URL=https://calendar.google.com/your_ics_url
```

## Run

```
python3 ical2json.py
```

## Output format

The output is in json format, with the following structure:

```json5
{
    "metadata": {
        "generated": "2024-04-18T10:48:41.711660"
        // can include more if wanted
    },
    "events": [
        {
            "name": "",
            "begin": "",
            "end":"",
            "description": "",
            "location": "",
            "url": ""
        }
    ]
}
```
