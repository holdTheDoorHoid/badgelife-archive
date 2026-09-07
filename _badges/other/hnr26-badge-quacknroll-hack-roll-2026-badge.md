---
title: hnr26-badge-quacknroll — Hack&Roll 2026 badge
id: other-hnr26-badge-quacknroll-hack-roll-2026-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2026
makers:
- name: NUS Hackers
summary: 'The "Quack & Roll" badge given to attendees of Hack&Roll 2026, NUS Hackers'' annual student hackathon in Singapore; it was the organization''s first custom PCB conference badge.'
functions: 'Buttons light up onboard LEDs; a demo firmware lights the LEDs (arranged like dice pips) depending on which buttons are pressed. Attendees could reprogram the ESP32-C3 themselves during the event.'
look:
  colors: []
  shape: null
  themes:
  - duck
  - learn to solder
tech:
  mcu: ESP32-C3-WROOM-02-N4
  leds: null
  display: null
  connectivity:
  - nfc
  battery: null
  sao_version: null
get_one:
  price: free
  price_usd: null
  quantity: '1,000+'
  availability: free
  distribution:
  - free_drop
  where: Given to attendees of Hack&Roll 2026 (NUS Hackers'' hackathon) as part of the event badge/goodie package.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/nushackers/hnr26-badge-quacknroll
  eda_tool: null
links:
- label: github.com/nushackers/hnr26-badge-quacknroll
  url: https://github.com/nushackers/hnr26-badge-quacknroll
  kind: repo
- label: github.com/nushackers/hnr26-badge-workshop
  url: https://github.com/nushackers/hnr26-badge-workshop
  kind: repo
- label: HnR'26 badge I/O component library docs
  url: https://nushackers.github.io/hnr26-badge-workshop/hnr26-badge/html/
  kind: doc
- label: 'Hack&Roll 2026 recap (NUS Hackers blog)'
  url: https://www.nushackers.org/2026/02/15/hnr2026/
  kind: article
- label: 'Friday Hacks #287: NUSMods and Hack&Roll Badges talk'
  url: https://www.nushackers.org/2026/01/friday-hacks-287
  kind: article
- label: Hack&Roll 2026 event site
  url: https://hacknroll.nushackers.org/
  kind: website
images:
- file: assets/images/badges/other/hnr26-badge-quacknroll-hack-roll-2026-badge/6616610ddb.jpg
  source: "https://www.nushackers.org/2026/02/15/hnr2026/"
  credit: "NUS Hackers"
  caption: "Colored PCB Quack & Roll badges from Hack&Roll 2026"
contact: {}
notes:
- 'Badge team credited by NUS Hackers: Terence Chan (PCB design), Tan Le Yew (NFC controller firmware), Lim Yik Jin (hardware), Park Youngseo (artwork), and Koh Chan Hong "Ravern" / Tan Rongwen "Daren" as Espressif liaisons. The ESP32-C3-WROOM-02-N4 modules were sponsored by Espressif Systems.'
status: released
sources:
- kind: url
  url: https://github.com/nushackers/hnr26-badge-quacknroll
  title: hnr26-badge-quacknroll — Hack&Roll 2026 badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''Hack&Roll 2026''.'
- kind: url
  url: https://github.com/nushackers/hnr26-badge-workshop
  title: hnr26-badge-workshop — Hack&Roll 2026 firmware workshop repo
  accessed: '2026-09-07'
  note: 'Confirms LEDs, buttons, AW9523 GPIO expander, ESP32-C3-WROOM-02-N4 sponsored by Espressif; demo firmware lights LEDs based on button presses (dice-style).'
- kind: url
  url: https://www.nushackers.org/2026/02/15/hnr2026/
  title: 'Hack&Roll 2026 recap — NUS Hackers'
  accessed: '2026-09-07'
  note: 'Confirms this was NUS Hackers'' first custom PCB badge, given to attendees, who personalized/hacked them during the event; source of the badge photo.'
- kind: url
  url: https://www.nushackers.org/2026/01/friday-hacks-287
  title: 'Friday Hacks #287: NUSMods and Hack&Roll Badges'
  accessed: '2026-09-07'
  note: 'Confirms over 1,000 badges were assembled and programmed; badge team (Terence and Yik Jin) previously built GreyCTF electronic badges; NFC controller mentioned via repo README.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Hack&Roll is an annual NUS Hackers hackathon in Singapore, not a hacker/security con, so there is no matching id in _data/events.yml (no "hackroll" or "hnr" event exists); left as event: other per instructions, year set to 2026 from sources. Could not confirm LED count, exact color scheme/PCB shape, display (none apparent), battery/power source (likely USB from a host device or programmer, not confirmed), or SAO header presence. The repo README mentions an "NFC controller" but no further detail on an NFC chip or antenna was found on the pages reviewed; listed under tech.connectivity as a maker-stated feature only. Price/quantity: badges were free to hackathon attendees; "over 1,000" units stated in the Friday Hacks talk description.'
last_modified_date: '2026-09-07'
---

The "Quack & Roll" badge was made by NUS Hackers for Hack&Roll 2026, their annual 24-hour student hackathon held at the National University of Singapore. It was the organization's first custom PCB conference badge, built around an ESP32-C3-WROOM-02-N4 module donated by Espressif Systems. The badge uses buttons wired through an AW9523 GPIO expander to drive onboard LEDs, and shipped with a simple demo program that lights the LEDs (arranged like dice pips) in response to button presses; the badge's I/O is also documented as a small component library so hackers could extend it during the event. NUS Hackers reported assembling and programming over 1,000 of them for attendees, who were seen personalizing and hacking on the boards throughout the weekend.

The badge was designed and built by a small internal team: Terence Chan handled the PCB design, Tan Le Yew wrote the NFC controller firmware, Lim Yik Jin worked on the hardware, Park Youngseo did the artwork, and Koh Chan Hong ("Ravern") and Tan Rongwen ("Daren") liaised with Espressif for the sponsored chips. Terence and Yik Jin had previously built badges for GreyCTF, an NUS-affiliated CTF competition. Firmware and workshop materials are published on GitHub (`nushackers/hnr26-badge-quacknroll` and `nushackers/hnr26-badge-workshop`), including a rendered component-library reference, but no separate hardware/PCB design repository or Gerber files were found, so open-source status is recorded as partial (firmware only, confirmed).

## Make your own

The `hnr26-badge-workshop` repository contains ESP-IDF firmware source and a companion walkthrough for programming the badge's LEDs and buttons via the AW9523 GPIO expander; the rendered API docs are at the GitHub Pages link above. No hardware design files (schematic/PCB/Gerbers) were located, so replicating the physical board is not currently possible from public sources.
