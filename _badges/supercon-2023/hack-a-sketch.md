---
title: Hack-a-Sketch
id: supercon-2023-hack-a-sketch
layout: badge
parent: Supercon 2023
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2023
year: 2023
makers:
- name: Jeremy Geppert
  url: https://hackaday.io/jeremygeppert
- name: Andy Geppert
  url: https://hackaday.io/andy-geppert
- name: pandiarajan2122
  url: https://hackaday.io/pandiarajan2122
summary: 'A 3D-printed frame and two potentiometer knobs that turn the official Hackaday Supercon 2023 "Vectorscope" badge into an Etch A Sketch-style drawing toy.'
functions: 'Repurposes the Vectorscope badge''s built-in Lissajous mode: two potentiometers wired to the badge''s analog inputs act as X/Y knobs, drawing a line on the vector display. A later firmware tweak added a dedicated menu mode with a gray background and black line to mimic an actual Etch A Sketch screen.'
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - kit
tech:
  mcu: null
  leds: null
  display: 'Vectorscope badge''s built-in oscilloscope-style vector display (host badge)'
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Built at Hackaday Supercon 2023 by attendees on their own Vectorscope conference badges; design files were later posted for others to print and build.'
make_your_own:
  open_source: 'yes'
  hardware_url: https://hackaday.io/project/193538-hack-a-sketch
  firmware_url: https://hackaday.io/project/193538-hack-a-sketch
  eda_tool: null
links:
- label: hackaday.io/project/193538-hack-a-sketch
  url: https://hackaday.io/project/193538-hack-a-sketch
  kind: hackaday
- label: 'Hack-a-Day/Vectorscope (base badge firmware/hardware on GitHub)'
  url: https://github.com/Hack-a-Day/Vectorscope
  kind: repo
- label: 'Hackaday: 2023 Hackaday Supercon Badge: Welcome To The Vectorscope'
  url: https://hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope/
  kind: article
images:
  - file: assets/images/badges/supercon-2023/hack-a-sketch/bbb652e85d.jpg
    source: "https://hackaday.io/project/193538-hack-a-sketch"
    credit: "Jeremy Geppert / Andy Geppert"
    caption: "Hack-a-Sketch: a 3D-printed frame and dual potentiometer knobs added to a Supercon 2023 Vectorscope badge"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/193538-hack-a-sketch
  title: Hack-a-Sketch
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/193538-hack-a-sketch
  title: Hack A Sketch project page
  accessed: '2026-09-07'
  note: 'Primary source: maker names, event/year, mechanism (potentiometers wired into Lissajous mode), downloadable STL/gcode/firmware files, image gallery.'
- kind: url
  url: https://github.com/Hack-a-Day/Vectorscope
  title: 'GitHub - Hack-a-Day/Vectorscope'
  accessed: '2026-09-07'
  note: 'Confirms the Vectorscope is the official 2023 Hackaday Supercon badge that Hack-a-Sketch modifies.'
- kind: url
  url: https://hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope/
  title: '2023 Hackaday Supercon Badge: Welcome To The Vectorscope'
  accessed: '2026-09-07'
  note: 'Background on the host badge (RP2040-based Vectorscope) that Hack-a-Sketch was built on top of.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched all three cited sources (Hackaday.io project page, Hack-a-Day/Vectorscope GitHub repo, hackaday.com article). Confirmed makers, event/year, mechanism (two potentiometers wired into the Vectorscope''s Lissajous/X-Y scope mode), the Friday-night firmware tweak and Saturday addition of a dedicated gray-background/black-line menu mode, the downloadable STL/gcode/firmware files, and that the Vectorscope is the official RP2040-based 2023 Supercon badge. The body''s "brother"/"nephew" wording matches the maker''s own project description ("collaboration project between my brother, nephew, myself and others"), though the page does not say by name which of Andy Geppert or pandiarajan2122 is the brother vs. the nephew -- the body''s pairing (Andy = brother, sharing the Geppert surname) is a reasonable but not explicitly confirmed inference. Removed a second saved image (8a5f5c0875.jpg) that turned out, on inspection, to show an unrelated white "Artemis Says" device, not Hack-a-Sketch or the Vectorscope -- likely mis-grabbed during image fetch; only one image (bbb652e85d.jpg, verified as the actual Hack-a-Sketch build) remains. This is a badge hack/mod built on top of the official Hackaday Supercon 2023 "Vectorscope" badge, not a standalone badge or SAO -- classified as type: accessory since it requires the host badge and is a physical add-on (3D-printed frame + potentiometer knobs) plus a small firmware patch. Event corrected from "other" to "supercon-2023" per _data/events.yml. No price, quantity, or sales info exists -- it was a personal/collaborative con build, not sold. No dedicated GitHub repo for the Hack-a-Sketch mod itself exists; firmware and STL files are hosted as direct downloads on the Hackaday.io project page.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/hack-a-sketch/
---

Hack-a-Sketch is a hardware hack built at Hackaday Supercon 2023 by Jeremy Geppert, his brother Andy Geppert, his nephew, and other attendees (including help from a contributor called Simen), turning the event's official "Vectorscope" conference badge into an Etch A Sketch-style toy. The Vectorscope badge already drew Lissajous curves on its built-in vector display; the team wired two potentiometers into the badge's analog input and power lines to act as X/Y knobs, then 3D-printed a frame and knob caps sized to the badge so it could be held and turned like a real Etch A Sketch.

The first working version came together Friday night of the con with only a small firmware tweak to the stock Lissajous mode. On Saturday, with help from Simen, the team added a dedicated menu entry that rendered a black line on a gray background to better mimic the look of an actual Etch A Sketch screen. The 3D print files (frame and knob, as STL and pre-sliced Prusa MK3 gcode) and the modified Python firmware file were later posted to the project's Hackaday.io page for other attendees to replicate.

Because it modifies the host Vectorscope badge rather than being a separate product, there is no price, unit count, or storefront associated with Hack-a-Sketch -- it exists as a documented con build and a small set of downloadable files rather than something that was sold or distributed as its own item.
