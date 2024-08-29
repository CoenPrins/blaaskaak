# blaaskaak.nl

This is the repository for the [blaaskaak.nl](https://blaaskaak.nl) website.
There are a couple points of interest, each described in their own sections in
this document.


## Structure

```
.
├── Makefile                       # File used to build the site
├── README.md                      # This file
├── base.html                      # Base template for each page
├── calendar-url.txt               # The ICS url to the Google Calendar
├── pages/                         # HTML main content for each page
├── public/                        # Build location, ignored by Git
├── scripts                        #
│   ├── ical2json.py               # Convert the ics file to JS-readable
│   ├── liveserver.py              # Run a local live server
│   └── requirements.txt           # Python packages
└── static                         #
    ├── CNAME                      # The site name. Required!
    ├── css                        #
    │   ├── event-list.css         # Just the event list styles
    │   └── style.css              # Main styles (common to each page)
    ├── media/                     # Images and other media content
    └── js                         #
        ├── calendar.js            # Construct the event list
        └── nav-current-page.js    # Arrows in nav point to current page
```

## Building website

Generally you can run everything for this site via the command `make`. These
are the subcommands (called 'targets' in Make):

- `all`: Same as `make calendar site`.
- `static`: Copy static files to `public/`.
- `pages`: Build pages with base to `public/`.
- `site`: Same as `make pages static`.
- `calendar`: Download and convert Google Calendar.
- `clean-venv`: Remove `.venv/` folder.
- `clean-build`: Remove `public/` folder.
- `clean`: Same as `make clean-venv clean-build`
- `format`: Format files (currently only Python files)


## Static Folder

This includes javascript (`js/`), css (`css/`) and media (`media/`) files.
Files are directly copied to the build folder (`public/`), without changing.

Couple of ideas to keep it clean:

- Shared css goes in `style.css`. Larger css for specific elements that only
  appear on one page can go in separate css files.
- Try not to write html in js files, but use html [`<template>`
  elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template).
- Use _tools_ in your _editor_ that make life easier:
  - Beautifiers / formatters to format your code (e.g.
    [prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode))
  - Linters for pointing to obvious errors


## Pages Folder

Pages define the main HTML content for each page. Want another page? Add a file
and write content. No need for `<html>` and `<body>` tags (basically everything
that can be seen in [`base.html`](./base.html). It is recommended to wrap
everything in a `<main>` tag, but not necessary. If you want the page to be
different from others, you _can_ just write a complete html file in the
`pages/` folder. It is important that this file starts with the line:
`<!DOCTYPE html>`.

## Base Template

This HTML will appear on every page. `$content` is replaced with the file
content of the page file. `$subtitle` replaced with the humanized filename of
the page file.


## Google Calendar Data

The information about gigs is pulled from Google Calendar, based on a schedule
(currently once a day). This is done using Github Actions, which runs `make
all` once a day and then deploys the `public/` folder to GitHub Pages (hosting).

It runs on:
- Schedule: every day at 15:35
- Push: every push to the `main` branch
- Manual: can be activated manually

This means that _everything_ that appears in the `public/` folder, _will_ be
available online. Remember that.
