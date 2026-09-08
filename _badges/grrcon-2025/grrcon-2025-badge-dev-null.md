---
title: GrrCon 2025 Badge (/dev/null)
id: grrcon-2025-grrcon-2025-badge-dev-null
layout: badge
parent: GrrCON 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: grrcon-2025
year: 2025
makers:
- name: Dan Lacher
summary: An unofficial community badge built around a Raspberry Pi Zero 2W and an e-ink display that shows attendee-submitted messages.
functions: Attendees scan a QR code to reach a web form (index.php) and submit a short text message; a script on the badge (badge.php) pulls the latest submissions and renders them on the e-ink display, filtering profanity against a maintained word list.
look:
  colors: []
  shape: null
  themes:
  - text
tech:
  mcu: Raspberry Pi Zero 2W
  leds: null
  display: e-paper
  connectivity:
  - wifi
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/danlacher/GrrConBadge
  eda_tool: null
links:
- label: github.com/danlacher/GrrConBadge
  url: https://github.com/danlacher/GrrConBadge
  kind: repo
images: []
contact: {}
notes:
- Unofficial Raspberry Pi Zero 2W + e-ink badge for GrrCon 2025 that displays QR-submitted attendee messages. Found by the event-year sweep, task con-derbycon.
- 'Sweep title matches the maker''s own repo README title ("/dev/null''s GrrCon 2025 Badge"); no change needed.'
status: released
sources:
- kind: url
  url: https://github.com/danlacher/GrrConBadge
  title: GrrCon 2025 Badge (/dev/null)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-derbycon); event read as ''GrrCON 2025''.'
- kind: url
  url: https://github.com/danlacher/GrrConBadge
  title: danlacher/GrrConBadge
  accessed: '2026-09-08'
  note: 'Confirmed the badge is a real, built project: repo README describes a Raspberry Pi Zero 2W badge with e-ink display, a PHP web form (index.php) for attendee text submissions, a bad-words filter, and badge.php to render the latest submission on the display. Repo contents also include a QR code image (GrrCon2025-devnull-qr.jpg) and an archive of collected submissions from the event, confirming it was actually deployed at GrrCon 2025.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: "Confirmed as a real, deployed badge via the maker's own GitHub repo (code, QR asset, and archived attendee submissions from the event). No maker's-own photo of the physical badge/display was found in the repo (only the QR code graphic), so images is left empty. Price, quantity made, and distribution/availability were never stated anywhere in the repo; left unknown. No LED, color, or shape information was given. Open-source status is set to partial: firmware/software (PHP + Python) is public, but no separate hardware design files (enclosure, wiring, BOM) were found in the repo, so hardware_url is left empty."
last_modified_date: '2026-09-08'
---

Dan Lacher (posting as "/dev/null") built an unofficial companion badge for GrrCon 2025 around a Raspberry Pi Zero 2W and an e-ink display. Rather than running fixed art or a game, the badge served as a live community message board: attendees scanned a printed QR code to reach a small PHP web form, typed a short message, and a script running on the Pi polled the latest submissions and rendered them on the display, with a maintained bad-words list filtering out profanity before anything reached the screen.

The project's GitHub repository holds the full software stack — the PHP input page, the Python/PHP display script, the word filter, and a submissions log — plus an archived folder of the actual messages collected while the badge was running at the con, which confirms it was built and used on-site rather than only planned. No photos of the finished physical badge were included in the repo, and the maker did not publish pricing, quantity, or distribution details, so those fields remain unknown; this looks to have been a one-off personal build rather than a con-sold item.

## Make your own

The software is open on GitHub (github.com/danlacher/GrrConBadge): `index.php` serves the submission form, `badge.php` runs on the badge to fetch and display the newest message, and `bad-words.txt` supplies the content filter. No separate hardware files (schematic, enclosure, BOM) were published — building a copy would mean supplying your own Raspberry Pi Zero 2W, e-ink display, and wiring to match the scripts.
