---
title: 'Audio Spectrum Analyzer: A SuperCon Badge'
id: other-audio-spectrum-analyzer-a-supercon-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2015
makers:
- name: Nathaniel Quillin
  url: https://hackaday.io/nathaniel-quillin
summary: A hand-built badge hack entered in the "Most Over the Top" category of the 2015 Hackaday SuperConference badge contest, built around a Teensy 3.2 and a TFT display.
functions: A waterfall audio spectrum analyzer fed by a microphone and an internal sine-wave source, a peak detector fed by the same signals, a badge mode that displays text, and image-displaying features.
look:
  colors: []
  shape: null
  themes:
  - music
  - hardware tool
tech:
  mcu: Teensy 3.2
  leds: null
  display: TFT display (ILI9341)
  connectivity:
  - audio
  battery: 9V battery
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - contest
  where: Built as a one-off entry for the Hackaday SuperConference 2015 badge hacking contest; not sold.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/8575-audio-spectrum-analyzer-a-supercon-badge
  url: https://hackaday.io/project/8575-audio-spectrum-analyzer-a-supercon-badge
  kind: hackaday
  archived: https://web.archive.org/web/20250910083603/https://hackaday.io/project/8575-audio-spectrum-analyzer-a-supercon-badge
images:
- file: assets/images/badges/other/audio-spectrum-analyzer-a-supercon-badge/e9a204d7e2.jpg
  source: https://hackaday.io/project/8575-audio-spectrum-analyzer-a-supercon-badge
  credit: Nathaniel Quillin
  caption: The Audio Spectrum Analyzer SuperCon badge with TFT display
  archived: https://web.archive.org/web/20250910083603/https://hackaday.io/project/8575-audio-spectrum-analyzer-a-supercon-badge
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/8575-audio-spectrum-analyzer-a-supercon-badge
  title: 'Audio Spectrum Analyzer: A SuperCon Badge'
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''Supercon''.'
  archived: https://web.archive.org/web/20250910083603/https://hackaday.io/project/8575-audio-spectrum-analyzer-a-supercon-badge
- kind: url
  url: https://hackaday.io/project/8575-audio-spectrum-analyzer-a-supercon-badge
  title: 'Audio Spectrum Analyzer: A SuperCon Badge'
  accessed: '2026-09-07'
  note: Confirmed maker (Nathaniel Quillin), event (Hackaday SuperCon 2015, entered Nov 25, 2015 in the "Most Over the Top" contest category), functions, MCU (Teensy 3.2 with Teensy Audio Adapter), display (ILI9341 TFT), power (9V battery), and two 10k potentiometers as controls. A GitHub repo (nqbit/superconbadge) was mentioned as a design source but returned 404 when checked, so make_your_own fields were left empty.
  archived: https://web.archive.org/web/20250910083603/https://hackaday.io/project/8575-audio-spectrum-analyzer-a-supercon-badge
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This is a badge-hacking-contest entry for Hackaday SuperCon 2015 ("Most Over the Top" category), not a con-issued badge. No event id for 2015 exists in _data/events.yml (ids start at supercon-2016), so event is left as 'other'; the con and year are Hackaday SuperConference 2015. No pricing, quantity, or open-source design files could be confirmed - the GitHub repo linked from Hackaday.io (nqbit/superconbadge) 404s.
last_modified_date: '2026-09-07'
---

Nathaniel Quillin built this badge hack for the 2015 Hackaday SuperConference badge contest, entering it in the "Most Over the Top" category. Rather than a con-issued badge, it is a personal project built around a Teensy 3.2 microcontroller paired with a Teensy Audio Adapter, driving an ILI9341 TFT display and running on a 9V battery with two 10k potentiometers for control.

The badge's core feature is a waterfall-style audio spectrum analyzer, fed by both a microphone and an internal sine-wave source, alongside a peak detector reading the same inputs. It also has a text-display badge mode and some additional image-display functionality. The Hackaday.io project page includes a photo gallery and a video of the badge working, but no sales, pricing, or production-quantity information, consistent with this being a one-off contest build rather than a produced/distributed badge.

A GitHub repository (nqbit/superconbadge) was referenced as the project's likely source/design repo but was unreachable (404) at the time of this research, so hardware and firmware links could not be confirmed or added.
