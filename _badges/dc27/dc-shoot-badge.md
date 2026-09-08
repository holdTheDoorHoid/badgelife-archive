---
title: DC Shoot Badge
id: dc27-dc-shoot-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Gigs (@gigstaggart)
  url: https://gigsatdc.com/
summary: An independent DEF CON 27 badge built as a personal shot timer and shot counter for the shooting range, reissuing (with permission) the DEF CON 23 shoot badge designed by SeeEss.
functions: Shot timer with random-delay start, impulse/shot counter, audio level display with adjustable detection threshold, a reaction-time game, a dodging game, morse code display, and sound visualization on its 4-digit 7-segment display.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - measurement
  form_factor: pcb badge
tech:
  mcu: PIC16F1709
  leds: null
  display: 4-digit 7-segment LED display
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
- label: hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
- label: gigsatdc.com/dc27/shootbadge_manual.php
  url: https://gigsatdc.com/dc27/shootbadge_manual.php
  kind: doc
- label: gigsatdc.com/dc27/shootbadge_walkthrough.php
  url: https://gigsatdc.com/dc27/shootbadge_walkthrough.php
  kind: doc
- label: gigsatdc.com
  url: https://gigsatdc.com/
  kind: website
- label: gigsbadge.com (maker portfolio)
  url: https://gigsbadge.com/
  kind: website
images:
- file: assets/images/badges/dc27/dc-shoot-badge/ab8a665c79.jpg
  source: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  credit: Hackaday / Gigs (gigstaggart)
  caption: Front of the DC Shoot Badge, DEF CON 27
- file: assets/images/badges/dc27/dc-shoot-badge/b71225aa01.jpg
  source: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  credit: Hackaday / Gigs (gigstaggart)
  caption: Rear of the DC Shoot Badge, DEF CON 27
- file: assets/images/badges/dc27/dc-shoot-badge/f2aa60b17f.jpg
  source: https://gigsbadge.com/
  credit: Gigs
  caption: Shoot Badge Reissue, diamond-shaped PCB layout
contact: {}
notes:
- Independent DC27 badge, 250 units produced, a reissue of a DC23 design, per Hackaday's DC27 unofficial-badge roundup. Found by the event-year sweep, task dc27-indie.
- Sweep imported the title as written; the maker's own manual uses the same name ("DEF CON 27 Electronic Shoot Badge"), so no title correction was needed.
- Unofficial personal electronics badge for the DEF CON shoot range, a reissue of the DC23 shoot badge with a mic-based shot counter/timer; 250 made. Found by the event-year sweep, task dc27-saos.
- Duplicate of dc27-dc-shoot-badge (same maker, same DC27 reissue of the DC23 shoot badge, same 250-unit production figure per Hackaday); the two entries appear to describe the same physical item under different sweep-assigned titles.
status: released
sources:
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: DC Shoot Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc27-indie); event read as ''dc27''.'
- kind: url
  url: https://gigsatdc.com/dc27/shootbadge_manual.php
  title: DEF CON 27 Electronic Shoot Badge User/Hacker Manual
  accessed: '2026-09-08'
  note: 'Maker''s own manual: MCU (PIC16F1709), display (4-digit 7-segment), controls, modes/functions, and explicit credit to SeeEss''s DC23 shoot badge as the basis for the hardware and (largely compatible) firmware.'
- kind: url
  url: https://gigsatdc.com/dc27/shootbadge_walkthrough.php
  title: DEF CON 27 Electronic Shoot Badge Challenge Walkthrough
  accessed: '2026-09-08'
  note: Confirms the badge carried a crypto/puzzle challenge starting from the lanyard.
- kind: url
  url: https://gigsatdc.com/
  title: Gigs at DEF CON (or other cons)
  accessed: '2026-09-08'
  note: Maker's index page confirming the DC27 shoot badge alongside their other badge projects (DC29 Tor Badge, DC31 Sneaky Badge).
- kind: url
  url: https://gigsbadge.com/
  title: Gigs Badge Portfolio - Shoot Badge Reissue (DEF CON 27)
  accessed: '2026-09-08'
  note: 'Maker''s own portfolio: confirms reissue of SeeEss''s design, reverse-engineered PCB, diamond board rotation, and image of the badge.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core facts (MCU, display, functions, 250-unit run, DC23 lineage) confirmed by both Hackaday''s roundup and the maker''s own manual/site, so this is more than a single source but the maker never published price, exact distribution method, or a firmware/hardware repo link for this specific badge (the manual only points to SeeEss''s DC23 repo, which was not located). LED count/type not stated anywhere found. tech.battery left null: the manual mentions configurable voltage regulation (3.3V or unregulated) but not a specific battery type/cell. make_your_own.open_source set to partial because the firmware is described as "largely compatible" with SeeEss''s published DC23 firmware, not a from-scratch open release of this badge''s own files. Merged with duplicate entry ''DEF CON 27 Electronic Shoot Badge'' (dc27-electronic-shoot-badge).'
last_modified_date: '2026-09-08'
redirect_from:
- /badges/dc27/electronic-shoot-badge/
---

The DC Shoot Badge is an independent DEF CON 27 badge made by Gigs (@gigstaggart) as a personal electronic shot timer and counter for use at a shooting range. It is an explicit reissue of the DEF CON 23 shoot badge designed by SeeEss, reusing much of that badge's hardware layout and firmware, which Gigs credits directly in the badge's manual. Roughly 250 units were produced, with final assembly reportedly involving about 5,000 hand-soldered joints completed the week of the con.

Built around a PIC16F1709 microcontroller, the badge uses a 4-digit 7-segment LED display alongside a microphone (for shot detection) and a mechanical tilt sensor (for screen orientation), with two buttons for control. Beyond its shooting-range functions — a shot timer with randomized start delay, an impulse/shot counter, and an adjustable audio detection threshold — it also runs a handful of recreational modes: a reaction-time game, a dodging game, a morse code display, and a sound-level visualizer. The badge additionally carried a crypto/puzzle challenge, with a public walkthrough later posted by the maker.

No price, exact production/distribution method, or hardware/firmware repository specific to the DC27 build were found; the maker's manual instead points back to SeeEss's original DC23 project as the firmware's basis.

## Notes merged from the duplicate entry "DEF CON 27 Electronic Shoot Badge"

The DEF CON 27 Electronic Shoot Badge is an unofficial personal-electronics badge made for DEF CON's shoot range, built by Gigs (@gigstaggart) as a reissue of a shot-timer badge SeeEss originally created for DC23. Because the original design files had been lost, Gigs reverse-engineered the PCB from the existing hardware, rotated the board 45 degrees into a diamond shape to allow alternative lanyard mounting, and lightly modified the firmware. Around 250 units were produced, with final assembly reportedly involving roughly 5,000 hand-soldered joints completed the week of the con.

The badge is built around a PIC16F1709 microcontroller and a 4-digit seven-segment display, and uses a microphone to detect and count gunshots for shot-timing games with a random-delay start. It also includes several built-in minigames (reaction time, dodge, and a morse-code challenge), a sound-level visualizer, an adjustable shot-detection threshold, a battery-voltage readout, a "clapper" sound-activated mode, and a mechanical tilt sensor. A separate walkthrough page documents a crypto/puzzle challenge Gigs built into the badge, with the entry point printed on the lanyard.

This entry appears to duplicate `dc27-dc-shoot-badge`, another sweep-discovered entry describing the same badge (same maker, same DC23 reissue, same 250-unit figure) under a different title drawn from the Hackaday roundup.
