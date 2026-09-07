---
title: "First to Rescue"
id: dc32-https-www-villageb-io-2024badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Biohacking Village
  url: https://www.villageb.io/
- name: SolaSec
  role: hardware/firmware design
summary: A hackable electronic breathalyzer badge shaped like an ambulance, made for DEF CON 32's Biohacking Village under the theme "First to Rescue."
functions: Measures blood-alcohol content with an onboard MQ-3 sensor, hosts a Wi-Fi access point with a password-protected web UI at 192.168.4.1, and carries CTF flags to capture.
look:
  colors:
  - red
  - white
  - black
  shape: ambulance
  themes:
  - ctf
  - security
  - village badge
  form_factor: pcb badge
tech:
  mcu: RP2040 (Raspberry Pi Pico W)
  leds: null
  display: unspecified (README references an onboard status light/screen; exact part not published)
  connectivity:
  - wifi
  - usb
  battery: rechargeable, charged via micro-USB; chemistry not stated
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Distributed at the Biohacking Village at DEF CON 32 (2024); exact distribution method (free vs. badge-holder only) not stated on the sources found.
make_your_own:
  open_source: 'yes'
  hardware_url: https://365.altium.com/files/9CA5ACBF-76BB-4CD4-BA4E-9E25169BB9EB?openedFrom=files&variant=[No+Variations]
  firmware_url: https://github.com/Biohacking-Village-CTF/BHV_Badge_2024
  eda_tool: Altium
  license: CC BY-NC-ND 4.0
  notes: Schematics, 3D models and Gerbers are on Altium 365; firmware (MicroPython) and setup instructions are in the GitHub repo. License is non-commercial, no-derivatives.
links:
- kind: website
  label: Biohacking Village badge page (2024 snapshot, current site no longer serves this route)
  url: https://web.archive.org/web/20240813021244/https://www.villageb.io/2024badge
- kind: repo
  label: BHV_Badge_2024 (GitHub)
  url: https://github.com/Biohacking-Village-CTF/BHV_Badge_2024
- kind: fab
  label: Hardware files on Altium 365
  url: https://365.altium.com/files/9CA5ACBF-76BB-4CD4-BA4E-9E25169BB9EB?openedFrom=files&variant=[No+Variations]
images:
- file: assets/images/badges/dc32/https-www-villageb-io-2024badge/b70ff92bff.jpg
  source: "https://github.com/Biohacking-Village-CTF/BHV_Badge_2024"
  credit: "SolaSec / Biohacking Village"
  caption: "Front PCB art of the 2024 Biohacking Village badge, styled as an ambulance"
- file: assets/images/badges/dc32/https-www-villageb-io-2024badge/3a81e74a8c.jpg
  source: "https://www.villageb.io/2024badge"
  credit: "Biohacking Village"
  caption: "Exploded render of the badge enclosure, breathalyzer sensor tube, and PCB"
contact: {}
notes:
- The sheet listed only the URL "https://www.villageb.io/2024badge" as the title; that route no longer resolves on the current (2026) villageb.io site, which has since been rebuilt on a different platform. Content was recovered from Wayback Machine snapshots taken August-December 2024.
- The current villageb.io "Badge Legacy" list (as of 2026) includes an undated "Ambulance Badge... integrated breathalyser, created as a tribute to FDNY paramedics by SolaSec," which matches this badge.
status: released
sources:
- kind: sheet
  event: dc32
  row: 18
  updated: ''
- kind: url
  url: https://web.archive.org/web/20240813021244/https://www.villageb.io/2024badge
  title: "2024 Badge | Villageb.io (Wayback Machine snapshot, Aug 13 2024)"
  accessed: '2026-09-06'
  note: Confirmed badge name "First to Rescue," theme, one-line description ("hackable breathalyzer with an embedded access point and flags to capture"), conceptualization credited to Nina Alli, and link to the GitHub repo.
- kind: url
  url: https://github.com/Biohacking-Village-CTF/BHV_Badge_2024
  title: "Biohacking-Village-CTF/BHV_Badge_2024"
  accessed: '2026-09-06'
  note: README confirms MQ-3 BAC sensor, Raspberry Pi Pico W, Wi-Fi AP with per-badge password and QR pairing, micro-USB charging, Altium 365 hardware files, and the CC BY-NC-ND 4.0 license. Badge art in images/image.png shows "'24," "BIOHACKING VILLAGE," "SOLASEC," and maker handles @So1lDeoGloria, @Nate_Sm1th, @headinthebooth, @Kshockles.
- kind: url
  url: https://www.villageb.io/Badges
  title: "Biohacking Village - Badges (current site, 2026)"
  accessed: '2026-09-06'
  note: Current site's "Badge Legacy" section lists an undated "Ambulance Badge" by SolaSec with a matching description, but no 2024-specific page remains live.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Maker's current website no longer hosts the original 2024 badge page (site was rebuilt on a different platform by 2026); all technical detail comes from Wayback Machine snapshots and the maker's own GitHub repo, which is strong primary-source material even though it's not live on villageb.io today. Exact quantity made, price/free status, and LED/display part numbers were not found in any source checked. The four Twitter/X handles credited in the badge art (So1lDeoGloria, Nate_Sm1th, headinthebooth, Kshockles) were not individually researched beyond being named as contributors.
last_modified_date: '2026-09-06'
---

The 2024 Biohacking Village badge, themed "First to Rescue," is a working electronic breathalyzer shaped like a toy ambulance, designed by SolaSec for DEF CON 32. A Raspberry Pi Pico W drives an MQ-3 alcohol sensor: press the single button, wait for the sensor to warm up, and blow into a disposable mouthpiece to get a blood-alcohol reading (the README is careful to note it's for fun, not anything medical or legal). Conceptualization is credited to Nina Alli, founder of the Biohacking Village.

Each badge advertises its own Wi-Fi access point (SSID `AMB-xxxxxx`) with a password-protected web UI at 192.168.4.1, and a QR code for quick pairing — the badge also carried CTF flags to find, tying it into the village's usual capture-the-flag track. It charges over micro-USB, which also doubles as a way to recalibrate the sensor by burning off residual alcohol.

Hardware (schematics, 3D models, Gerbers) is published on Altium 365 and firmware (MicroPython, with build tooling to compile to frozen bytecode) is on GitHub, under a CC BY-NC-ND 4.0 license. The original villageb.io page for this badge is gone from the maker's current (2026) site, which has been rebuilt from scratch; the 2024 content survives only in Wayback Machine snapshots and the GitHub repo.
