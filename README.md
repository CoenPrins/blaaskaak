# blaaskaak.nl

This is the repository for the blaaskaak.nl website. There are a couple points
of interest, each described in their own sections in this document.

## Static website

This includes all `/*.html` files in the root folder and the javascript (`/js/`)
and css (`/css/`) files. Used to markup and design the static webpage.

Couple of ideas to keep it clean:

- Shared css goes in `style.css`. Larger css for specific elements that only
  appear on one page can go in separate css files.
- Try not to write html in js files, but use html [`<template>`
  elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template).
- Validate your html online, e.g. with https://validator.w3.org/
- Or even better, use TOOLS in your EDITOR:
  - Beautifiers / formatters to format your code
  - Linters for pointing to obvious errors

## Pulling Google Calendar data

The information about gigs is pulled from Google Calendar, based on a schedule
(currently once a day). This is done using Github Actions, and the action is
defined in
[`./.github/workflows/refresh-events.yml`](./.github/workflows/refresh-events.yml).
It also includes comments to explain the steps.

It runs on:
- Schedule: every day at 15:35
- Push: every push to the `main` branch
- Manual: can be activated manually

Its function is basically to run a single python script
([scripts/ical2json.py](./scripts/ical2json.py)) that pulls the data
from GCal en puts it in an events.json file. For a more in-depth description
about the Python script, see [scripts/README.md](./scripts/README.md).

The resulting json file is then committed to the `build` branch, on which the
site is also served by Github Pages. This branch should not be committed
directly to. Every change to `main`, will also go automatically to `build`.
