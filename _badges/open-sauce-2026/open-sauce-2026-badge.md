---
title: Open Sauce 2026 Badge
id: open-sauce-2026-open-sauce-2026-badge
layout: badge
parent: Open Sauce 2026
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: open-sauce-2026
year: 2026
makers:
- name: Caleb Marting (with Gerard Hudson)
summary: The official Open Sauce 2026 festival badge, an Arduino MKR Zero-compatible board shaped like the "SauceBot" mascot with a built-in "Bop It"-style reaction game.
functions: 'A five-action reaction game (yell into the mic, shake the accelerometer, press the button, swipe left/right across the LEDs, and a sleep/wake mode). Two SAO headers let attendees plug in add-ons; a 3D-printable adapter converts a standard SAO into the badge''s 2x3 header. Attendees rewrote the firmware into new minigames (Simon, a lung-tester, a theremin, a drum machine) during a Saturday-night hacking session.'
look:
  colors:
  - black
  shape: robot
  themes:
  - robot
  - mascot
  - game
  - hardware tool
tech:
  mcu: SAMD21 (Arduino MKR Zero-compatible)
  leds:
    count: 3
    type: discrete
    note: 3x 5mm red LEDs, swiped left/right as part of the reaction game
  display: none
  connectivity:
  - usb
  - i2c
  battery: coin cell (BS-02-A1AJ010 holder), USB-chargeable via the MKR Zero
  sao_version: v2
  inputs:
  - buttons
  - microphone
  - accelerometer
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to attendees of Open Sauce 2026 (San Mateo County Event Center, July 17-19, 2026) as the event badge.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/calebmarting/os2026-badge
  firmware_url: https://github.com/calebmarting/os2026-badge
  gerbers_url: null
  bom_url: null
  eda_tool: KiCad
  license: MIT
  fab_url: null
  notes: 'Repo includes full schematics, KiCad PCB files, firmware, a soldering-assembly guide, and a 3D-printable SAO-header adapter (printables.com). A separate community firmware fork with new minigames is at github.com/putnam/opensauce2026-badge.'
links:
- label: github.com/calebmarting/os2026-badge
  url: https://github.com/calebmarting/os2026-badge
  kind: repo
- label: badge.gallery/addons/open-sauce-2026-badge/open-sauce-2026-source-and-event-trail
  url: https://badge.gallery/addons/open-sauce-2026-badge/open-sauce-2026-source-and-event-trail
  kind: website
- label: github.com/putnam/opensauce2026-badge
  url: https://github.com/putnam/opensauce2026-badge
  kind: repo
images:
  - file: assets/images/badges/open-sauce-2026/open-sauce-2026-badge/ae5656b6c8.jpg
    source: "https://github.com/calebmarting/os2026-badge"
    credit: "Caleb Marting"
    caption: "Assembled Open Sauce 2026 badge (SauceBot mascot design)"
  - file: assets/images/badges/open-sauce-2026/open-sauce-2026-badge/d5cb0fa94d.jpg
    source: "https://github.com/calebmarting/os2026-badge"
    credit: "Caleb Marting"
    caption: "Badge back showing battery holder and SAO headers"
contact: {}
notes:
- Official Open Sauce 2026 festival badge, an Arduino MKR Zero-compatible board running 'Bop It' style firmware with optional SAO and battery headers; alternate community firmware was released separately by GitHub user putnam. Found by the event-year sweep, task con-open-sauce.
- 'The sweep''s notes described "reverse-mount" style LEDs and possible RGB LEDs; the maker''s own repo confirms these are 3 plain 5mm red THT LEDs, not RGB. A community fork README (putnam) separately describes "five RGB LEDs," which appears to be a description of an attached SAO or a misreading rather than the base badge — treated the maker''s own repo as authoritative.'
status: listed
sources:
- kind: url
  url: https://github.com/calebmarting/os2026-badge
  title: Open Sauce 2026 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-open-sauce); event read as ''Open Sauce 2026''.'
- kind: url
  url: https://github.com/calebmarting/os2026-badge
  title: calebmarting/os2026-badge README
  accessed: '2026-09-08'
  note: 'Maker''s own repo: hardware BOM, assembly instructions, LED count/type, MIT license, SAO header adapter link.'
- kind: url
  url: https://badge.gallery/addons/open-sauce-2026-badge/open-sauce-2026-source-and-event-trail
  title: Open Sauce 2026 source-and-event trail
  accessed: '2026-09-08'
  note: 'Confirmed event dates/venue, Gerard Hudson collaboration, KiCad files, and that no official Open Sauce organizer repo was found separate from the maker''s.'
- kind: url
  url: https://github.com/putnam/opensauce2026-badge
  title: putnam/opensauce2026-badge README
  accessed: '2026-09-08'
  note: 'Community firmware fork made during the event; describes accelerometer (LIS3DH), mic, SAO support, and new minigames; used with caution due to LED-count discrepancy with the maker''s repo.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Core facts (maker, event, hardware, open-source status) confirmed on the maker''s own GitHub repo. Price, quantity made, and current availability are not stated anywhere found, so those fields are left empty/unknown. Exact MCU part number not given (repo says "Arduino MKR Zero-compatible" / uses an Arduino MKR Zero "T-Piece"/"Sopracciglio" module rather than a bare chip on the badge itself) -- listed the MKR Zero''s SAMD21 family as tech.mcu since that is the effective compute on the assembled badge. See notes above on the LED-count/type discrepancy between the two repos.'
last_modified_date: '2026-09-08'
---

The Open Sauce 2026 badge is the official festival badge for Open Sauce (San Mateo County Event Center, July 17-19, 2026), designed by Caleb Marting with Gerard Hudson. It's built as a castellated add-on board that an attendee solders an Arduino MKR Zero module ("T-Piece") onto, giving the badge SAMD21-class compute inside a shape the maker calls "SauceBot": a robot face with a microphone over one eye, a tactile button over the other, and three red LEDs across the mouth. Out of the box it runs a "Bop It"-style reaction game using the mic, button, accelerometer-based shake, and LED swipe gestures, plus a sleep/wake mode.

The badge exposes two 6-pin SAO headers and a 2-pin battery-only header, and the maker published a 3D-printable adapter (on Printables) that turns a standard SAO into the badge's connector. Everything needed to build or modify one — KiCad schematics/PCB, firmware, and a photographed soldering guide — is published on GitHub under the MIT license, explicitly framed by the maker as "an Arduino MKR Zero in a Trench Coat" meant to be hacked further.

That invitation was taken up on-site: at least two attendees reverse-engineered the stock firmware overnight and returned Sunday with four new games. One of those forks, published separately by GitHub user "putnam," replaces the Bop It game with Simon, a lung-tester, a theremin, and a drum machine, and adds an "attract mode" that can drive SAO LED add-ons.

## Make your own

1. Fabricate the PCB from the KiCad files in the `os2026-badge` repo (or order the shared Gerbers if the maker publishes them).
2. Gather parts: an Arduino MKR Zero-compatible "T-Piece," a CMA-4544PF-W electret microphone, a 6x6mm tactile button, three 5mm red LEDs, and a BS-02-A1AJ010 coin-cell holder (2x 6-pin SAO headers and a 2-pin battery header are optional).
3. Follow the repo's photographed soldering guide: solder the castellated T-piece first, then the mic, button, LEDs (long leg into the square pad), and finally the battery holder on the back.
4. Flash the stock firmware from the repo, or try the community "putnamhack" firmware/examples included for alternate games.
