---
title: DEF CON 27 Electronic Shoot Badge
id: dc27-electronic-shoot-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Gigs
  url: https://gigsbadge.com/
summary: 'An unofficial personal electronics badge for the DEF CON shoot range, a modest reissue of SeeEss''s DC23 shoot badge with a microphone-based shot counter/timer, reverse-engineered by Gigs and rotated into a diamond shape.'
functions: 'Shot timing and counting with random-delay start, reaction-time/dodge/morse-code minigames, sound-level visualization, adjustable shot-detection threshold, battery voltage readout, "clapper" sound-activated mode; a mechanical tilt sensor and 4-digit seven-segment display show status and results.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - measurement
  - puzzle
  form_factor: pcb badge
tech:
  mcu: PIC16F1709
  leds: null
  display: 4-digit seven-segment display with decimal point
  connectivity:
  - audio
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '250'
  availability: sold_out
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://gigsatdc.com/dc27/shootbadge_manual.php
  eda_tool: null
links:
- label: gigsatdc.com/dc27/shootbadge_manual.php
  url: https://gigsatdc.com/dc27/shootbadge_manual.php
  kind: website
- label: gigsatdc.com/dc27/shootbadge_walkthrough.php
  url: https://gigsatdc.com/dc27/shootbadge_walkthrough.php
  kind: doc
- label: gigsbadge.com (maker portfolio)
  url: https://gigsbadge.com/
  kind: website
- label: 'Hackaday: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27'
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
images:
- file: assets/images/badges/dc27/electronic-shoot-badge/f2aa60b17f.jpg
  source: "https://gigsbadge.com/"
  credit: "Gigs"
  caption: "Shoot Badge Reissue, diamond-shaped PCB layout"
contact: {}
notes:
- Unofficial personal electronics badge for the DEF CON shoot range, a reissue of the DC23 shoot badge with a mic-based shot counter/timer; 250 made. Found by the event-year sweep, task dc27-saos.
- 'Duplicate of dc27-dc-shoot-badge (same maker, same DC27 reissue of the DC23 shoot badge, same 250-unit production figure per Hackaday); the two entries appear to describe the same physical item under different sweep-assigned titles.'
status: sold_out
sources:
- kind: url
  url: https://gigsatdc.com/dc27/shootbadge_manual.php
  title: DEF CON 27 Electronic Shoot Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc27-saos); event read as ''dc27''.'
- kind: url
  url: https://gigsbadge.com/
  title: Gigs Badge Portfolio - Shoot Badge Reissue (DEF CON 27)
  accessed: '2026-09-08'
  note: 'Maker''s own portfolio: confirms reissue of SeeEss''s design, reverse-engineered PCB, diamond board rotation, and image of the badge.'
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27
  accessed: '2026-09-08'
  note: 'Confirms maker (Gigs), 250-unit production run, reissue of DC23 shoot badge, microphone-based shot counting and mechanical tilt sensor.'
- kind: url
  url: https://gigsatdc.com/dc27/shootbadge_walkthrough.php
  title: DEF CON 27 Electronic Shoot Badge Challenge Walkthrough
  accessed: '2026-09-08'
  note: 'Confirms a crypto/puzzle challenge was built into the badge, entry point on the lanyard.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Price and exact distribution method (free vs. sold, and to whom) not stated by any source found; left empty. LED info not specified in the manual. Firmware source is described as available on "SeeEss'' GitHub Project" per the manual, but no working repo URL was found, so hardware_url/firmware_url for the maker''s own reissue are left null; open_source set to partial on that basis. This entry substantially duplicates dc27-dc-shoot-badge (same maker, same 250-unit DC23 reissue) — see notes and duplicate_of.'
last_modified_date: '2026-09-08'
---

The DEF CON 27 Electronic Shoot Badge is an unofficial personal-electronics badge made for DEF CON's shoot range, built by Gigs (@gigstaggart) as a reissue of a shot-timer badge SeeEss originally created for DC23. Because the original design files had been lost, Gigs reverse-engineered the PCB from the existing hardware, rotated the board 45 degrees into a diamond shape to allow alternative lanyard mounting, and lightly modified the firmware. Around 250 units were produced, with final assembly reportedly involving roughly 5,000 hand-soldered joints completed the week of the con.

The badge is built around a PIC16F1709 microcontroller and a 4-digit seven-segment display, and uses a microphone to detect and count gunshots for shot-timing games with a random-delay start. It also includes several built-in minigames (reaction time, dodge, and a morse-code challenge), a sound-level visualizer, an adjustable shot-detection threshold, a battery-voltage readout, a "clapper" sound-activated mode, and a mechanical tilt sensor. A separate walkthrough page documents a crypto/puzzle challenge Gigs built into the badge, with the entry point printed on the lanyard.

This entry appears to duplicate `dc27-dc-shoot-badge`, another sweep-discovered entry describing the same badge (same maker, same DC23 reissue, same 250-unit figure) under a different title drawn from the Hackaday roundup.
