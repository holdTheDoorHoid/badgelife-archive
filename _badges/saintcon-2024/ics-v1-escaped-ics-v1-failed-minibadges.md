---
title: ICS V1 Escaped / ICS V1 Failed minibadges
id: saintcon-2024-ics-v1-escaped-ics-v1-failed-minibadges
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: unconfirmed
summary: A pair of simple SAINTCON 2024 minibadges marking the two possible outcomes of an ICS (industrial control systems) themed challenge — "Escaped" and "Failed" — as two separate PCB designs sharing the same layout.
functions: ''
look:
  colors: []
  shape: null
  themes:
  - security
  - puzzle
  - ctf
tech:
  mcu: none
  leds:
    count: 2
    type: SMD
    note: 1206 SMD LEDs, driven through a series resistor; no microcontroller on either board.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/ICS%20V1%20Escaped
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/ICS%20V1%20Escaped
  kind: repo
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/ICS%20V1%20Failed
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/ICS%20V1%20Failed
  kind: repo
images: []
contact: {}
notes:
- 2024 versions of the ICS Escape Room outcome minibadges (2023 versions by SHIFTY already in archive; these are separate 2024 repo folders without confirmed maker). Found by the event-year sweep, task saintcon-2024.
- 'Sweep''s title wording kept as-is: the two 2024 folders ("ICS V1 Escaped" and "ICS V1 Failed") are each a distinct KiCad PCB design, not one badge with two names. Reported "ICS V1 Failed" separately in case it warrants its own entry.'
status: listed
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/ICS%20V1%20Escaped
  title: ICS V1 Escaped / ICS V1 Failed minibadges
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024
  title: 'utahsaint-org/MiniBadges2024: Minibadges for SAINTCON 2024'
  accessed: '2026-09-10'
  note: Repo README confirms "Minibadges for SAINTCON 2024" and lists both "ICS V1 Escaped" and "ICS V1 Failed" as sibling folders alongside dozens of other 2024 minibadge designs; no per-badge maker credit given (other folders in the same repo carry a "- SHIFTY" suffix, these two do not).
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/ICS%20V1%20Failed
  title: ICS V1 Failed (repo folder)
  accessed: '2026-09-10'
  note: Sibling design to "ICS V1 Escaped"; same KiCad footprints (MiniBadge_Simple connector, 2x 1206 LED, resistor), different silkscreen ("ICS Failed" vs "ICS Escaped").
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed via the maker org''s own GitHub repo (utahsaint-org/MiniBadges2024) that both designs exist as real KiCad/Gerber PCB projects made for SAINTCON 2024 — not just a sweep snippet. No README, image, or commit credits a specific individual maker (unlike several sibling folders in the same repo tagged "- SHIFTY"), so makers stays unconfirmed. No storefront, price, quantity, or distribution info found; likely a giveaway/trade minibadge typical of the SAINTCON minibadge community rather than a sold item. No rendered photos are in the repo (only Gerbers/KiCad source), so no images could be saved. Each board is a simple passive design: a MiniBadge_Simple edge connector (powered by the host badge), 2x 1206 SMD LEDs, and a series resistor — no MCU, no independent power source. Could not determine LED color, PCB color, or shape from the source files alone.'
last_modified_date: '2026-09-10'
---

"ICS V1 Escaped" and "ICS V1 Failed" are a pair of SAINTCON 2024 minibadges tied to an ICS (industrial control systems) themed challenge, most likely an escape-room-style puzzle where finishing successfully earns one badge and running out of time or failing earns the other. They live as two separate folders in the `utahsaint-org/MiniBadges2024` GitHub repository, which collects the community's minibadge designs for SAINTCON 2024 — the same organization and format used by dozens of other 2024 minibadges in that repo, several of which are individually credited to the maker "SHIFTY" (who is already credited for the 2023 versions of these same ICS outcome badges elsewhere in the archive). Neither "ICS V1 Escaped" nor "ICS V1 Failed" carries that credit in this repo, so the maker for the 2024 versions is left unconfirmed here.

Both boards are simple, uncomplicated minibadges: each uses the standard "MiniBadge_Simple" edge connector to draw power from a host badge, and each lights two 1206 SMD LEDs through a series resistor — there is no microcontroller, display, or independent battery on either design. The only difference between the two KiCad projects is the silkscreen text ("ICS Escaped" vs. "ICS Failed") that marks which outcome the wearer received.

Full KiCad source and Gerber fabrication files are published for both designs in the repo, so they qualify as open hardware, but no price, quantity made, or distribution channel could be confirmed — these read as giveaway or trade minibadges typical of the SAINTCON minibadge community rather than a priced product.
