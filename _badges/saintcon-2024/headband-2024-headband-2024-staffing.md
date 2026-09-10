---
title: Headband-2024 / Headband-2024-Staffing
id: saintcon-2024-headband-2024-headband-2024-staffing
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: unconfirmed
summary: 'A pair of headband-style SAINTCON 2024 minibadges (an attendee version and a staffing version) designed to clip onto the conference''s minibadge expansion board.'
functions: ''
look:
  colors: []
  shape: null
  themes:
  - minibadge
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
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
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Headband-2024
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/Headband-2024
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Headband-2024
  kind: repo
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/Headband-2024-Staffing
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Headband-2024-Staffing
  kind: repo
- label: 'SAINTCON MiniBadge Community'
  url: https://www.saintcon.org/communities/minibadge/
  kind: website
images: []
contact: {}
notes:
- Headband-style wearable minibadge (attendee and staffing variants) for SAINTCON 2024. Found by the event-year sweep, task saintcon-2024.
- 'Sweep''s wording "Headband-2024 / Headband-2024-Staffing" kept as title (matches the two repo folder names); no maker-published display name was found.'
status: listed
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Headband-2024
  title: Headband-2024 / Headband-2024-Staffing
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024
  title: 'utahsaint-org/MiniBadges2024: Minibadges for SAINTCON 2024'
  accessed: '2026-09-10'
  note: 'Confirms the repo root README ("Minibadges for SAINTCON 2024") and that Headband-2024 and Headband-2024-Staffing are two separate top-level folders in the collection alongside ~30 other 2024 minibadge designs.'
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Headband-2024-Staffing
  title: Headband-2024-Staffing
  accessed: '2026-09-10'
  note: 'Confirms the staffing variant folder exists with its own KiCad project, Gerbers, and SVG art assets, mirroring the attendee folder.'
- kind: url
  url: https://www.saintcon.org/communities/minibadge/
  title: Minibadge Community - SAINTCON
  accessed: '2026-09-10'
  note: 'Background on SAINTCON''s long-running minibadge trading tradition (community-designed add-on boards that clip onto an expansion board); no Headband-specific mention found here.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-10'
  notes: >-
    Confirmed real: the GitHub repo utahsaint-org/MiniBadges2024 contains two top-level folders,
    Headband-2024 and Headband-2024-Staffing, each with a complete KiCad project (schematic, PCB,
    Gerbers) and a small set of SVG art assets, so hardware design files are open (no firmware or
    BOM found, hence open_source: partial rather than yes). No maker/designer name is attributed to
    this specific design anywhere found (the repo is credited only to the utahsaint-org GitHub
    organization); no photo of the finished, populated board was located, only vector artwork files
    (SVG) that could not be confirmed as an accurate depiction of the final badge, so no images were
    saved. No price, quantity made, or availability info was found — SAINTCON minibadges are
    community-submitted designs typically brought/traded in person rather than sold, per the
    saintcon.org minibadge community page, but nothing ties that general pattern to this specific
    badge with a source. Could not determine colors, LEDs, MCU, or other tech specs from the
    KiCad/Gerber files without opening them in EDA software, which was out of scope for a text
    fetch/search pass.
last_modified_date: '2026-09-10'
---

Headband-2024 and Headband-2024-Staffing are a pair of SAINTCON 2024 minibadges published in the `utahsaint-org/MiniBadges2024` GitHub repository, which collects roughly three dozen community-designed minibadges made for that year's conference. SAINTCON's minibadges are small add-on boards that clip onto a shared expansion board worn by attendees, and are traded in person at the con's dedicated minibadge community and museum; this pair follows that pattern with a normal attendee version and a separate version apparently intended for event staffing volunteers.

Both folders in the repo contain a full KiCad project (schematic and PCB files) plus generated Gerbers and a handful of SVG artwork assets, so the hardware design is openly available, but no README, BOM, or firmware accompanies either folder. No maker name, price, quantity, or photo of an assembled board could be found in the repo or in general searches about SAINTCON 2024 minibadges, so those fields are left blank rather than guessed.
