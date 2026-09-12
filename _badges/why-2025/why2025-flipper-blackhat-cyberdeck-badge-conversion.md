---
title: Blackpants (WHY2025 badge / Flipper Blackhat cyberdeck conversion)
id: why-2025-why2025-flipper-blackhat-cyberdeck-badge-conversion
layout: badge
parent: Why 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: why-2025
year: 2025
makers:
- name: Rootkit Labs
  url: https://rootkitlabs.com
summary: A post-event fork of the WHY2025 conference badge (ESP32-P4, SolderParty keyboard) turned into "Blackpants," a replacement carrier board for the Flipper Blackhat that runs full Linux as a handheld cyberdeck.
functions: Runs Linux as a handheld computer; carries a Flipper Blackhat WiFi-pentesting addon board in place of a Flipper Zero; used for pentesting/hacking tasks via the Blackhat addon.
look:
  colors:
  - black
  shape: rectangle
  themes:
  - cyberpunk
  - hardware tool
  - security
  - retro computer
tech:
  mcu: ESP32-P4
  leds: null
  display: 480x480 LCD (Edgar Case 2.0 screen)
  connectivity:
  - wifi
  - usb
  battery: null
  sao_version: null
get_one:
  price: $150 CAD
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: 'Checked shop.rootkitlabs.com/products/blackpants on 2026-09-07: listed at $150 CAD, "Sold out."'
  distribution:
  - purchase
  where: Sold assembled via shop.rootkitlabs.com; requires a separately-sold Flipper Blackhat addon board to complete.
make_your_own:
  open_source: true
  hardware_url: https://github.com/o7-machinehum/Blackpants
  firmware_url: https://github.com/o7-machinehum/Blackpants
  eda_tool: null
  license: MIT
  notes: Repo (MIT licensed) includes docs, EE (electrical) and mech (mechanical) folders and QMK keyboard firmware integration for the backlit QWERTY keyboard. It pairs with the separate Flipper Blackhat repo (github.com/o7-machinehum/flipper-blackhat, flipper-blackhat-os).
links:
- label: hackaday.com/2026/02/02/an-event-badge-re-imagined-as-a-cyberdeck
  url: https://hackaday.com/2026/02/02/an-event-badge-re-imagined-as-a-cyberdeck/
  kind: article
  archived: https://web.archive.org/web/20260717220116/https://hackaday.com/2026/02/02/an-event-badge-re-imagined-as-a-cyberdeck/
- label: 'Blackpants hardware/firmware repo (GitHub: o7-machinehum/Blackpants)'
  url: https://github.com/o7-machinehum/Blackpants
  kind: repo
  archived: https://web.archive.org/web/20260509095628/https://github.com/o7-machinehum/Blackpants
- label: 'Flipper Blackhat repo (GitHub: o7-machinehum/flipper-blackhat)'
  url: https://github.com/o7-machinehum/flipper-blackhat
  kind: repo
  archived: https://web.archive.org/web/20260607122023/https://github.com/o7-machinehum/flipper-blackhat
- label: Blackpants product listing (Rootkit Labs shop)
  url: https://shop.rootkitlabs.com/products/blackpants
  kind: store
  archived: https://web.archive.org/web/20260323045728/https://shop.rootkitlabs.com/products/blackpants
- label: 'Rootkit Labs project video: "I Built a Fully Open Source Handheld Computer (FROM SCRATCH)"'
  url: https://www.youtube.com/watch?v=QxqeU8ZfaYg
  kind: video
  archived: https://web.archive.org/web/20260901112922/https://www.youtube.com/watch?v=QxqeU8ZfaYg
- label: Rootkit Labs
  url: https://rootkitlabs.com
  kind: website
  archived: https://web.archive.org/web/20260812211644/https://rootkitlabs.com/
- label: WHY2025 Badge wiki (original badge this was forked from)
  url: https://wiki.why2025.org/Badge
  kind: doc
  archived: https://web.archive.org/web/20260508205824/https://wiki.why2025.org/Badge
images:
- file: assets/images/badges/why-2025/why2025-flipper-blackhat-cyberdeck-badge-conversion/749fe27634.jpg
  source: https://hackaday.com/2026/02/02/an-event-badge-re-imagined-as-a-cyberdeck/
  credit: Rootkit Labs
  caption: The WHY2025 badge forked into a Blackpants handheld Linux cyberdeck
  archived: https://web.archive.org/web/20260717220116/https://hackaday.com/2026/02/02/an-event-badge-re-imagined-as-a-cyberdeck/
- file: assets/images/badges/why-2025/why2025-flipper-blackhat-cyberdeck-badge-conversion/465e853780.jpg
  source: https://shop.rootkitlabs.com/products/blackpants
  credit: Rootkit Labs
  caption: 'Blackpants product photo: backlit QWERTY keyboard and 480x480 LCD'
  archived: https://web.archive.org/web/20260323045728/https://shop.rootkitlabs.com/products/blackpants
contact: {}
notes:
- Post-event fork of the WHY2025 badge (ESP32-P4 + SolderParty keyboard) into a cyberdeck
- Maker's own name for the project is "Blackpants," not "Flipper Blackhat Cyberdeck" (the latter is Hackaday's article title / this entry's original sheet title).
status: released
sources:
- kind: url
  url: https://hackaday.com/2026/02/02/an-event-badge-re-imagined-as-a-cyberdeck/
  title: An Event Badge Re-Imagined As A Cyberdeck
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-press); event read as ''WHY2025''.'
  archived: https://web.archive.org/web/20260717220116/https://hackaday.com/2026/02/02/an-event-badge-re-imagined-as-a-cyberdeck/
- kind: url
  url: https://www.youtube.com/watch?v=QxqeU8ZfaYg
  title: I Built a Fully Open Source Handheld Computer (FROM SCRATCH)
  accessed: '2026-09-07'
  note: Maker's own video (Rootkit Labs channel); confirmed project name "Blackpants", origin story from Flipper Blackhat, links to hardware repo and shop listing, credited the SolderParty keyboard and the WHY2025 badge wiki as the base.
  archived: https://web.archive.org/web/20260901112922/https://www.youtube.com/watch?v=QxqeU8ZfaYg
- kind: url
  url: https://github.com/o7-machinehum/Blackpants
  title: 'GitHub: o7-machinehum/Blackpants'
  accessed: '2026-09-07'
  note: Confirms MIT license, open hardware/firmware repo structure (docs, ee, mech, QMK keyboard firmware).
  archived: https://web.archive.org/web/20260509095628/https://github.com/o7-machinehum/Blackpants
- kind: url
  url: https://shop.rootkitlabs.com/products/blackpants
  title: Blackpants – Rootkit Labs shop listing
  accessed: '2026-09-07'
  note: Price ($150 CAD), sold-out status, 480x480 LCD ("Edgar Case 2.0" screen), backlit QWERTY keyboard, two extra USB-A ports, sold assembled and pairs with a separately-sold Flipper Blackhat.
  archived: https://web.archive.org/web/20260323045728/https://shop.rootkitlabs.com/products/blackpants
- kind: url
  url: https://rootkitlabs.com
  title: Rootkit Labs
  accessed: '2026-09-07'
  note: Confirms maker identity and links to GitHub org o7-machinehum.
  archived: https://web.archive.org/web/20260812211644/https://rootkitlabs.com/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Core facts confirmed by the maker''s own video, GitHub repo, and shop listing. Not found/left empty: LED info (none mentioned by any source), exact battery spec, quantity made, and price in USD (only $150 CAD is stated). The Hackaday article and community sheet used "Flipper Blackhat Cyberdeck" as a descriptive title; the maker calls the carrier board itself "Blackpants," and titled the entry accordingly while keeping the original phrase in the id/slug.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/why-2025/why2025-flipper-blackhat-cyberdeck-badge-conversion.glb
  method: kicad
  source_file: ee/integrated/blackpants.kicad_pcb
  generated: '2026-09-10'
  bytes: 1915888
---

Blackpants is a handheld Linux computer built by Rootkit Labs by forking the WHY2025 conference badge — which shipped with an ESP32-P4 and a SolderParty mechanical keyboard — into a new carrier board. Instead of hosting the original badge firmware, Blackpants pairs with the maker's earlier project, the Flipper Blackhat (a WiFi-pentesting Linux addon originally built for the Flipper Zero), giving that addon a proper keyboard, a 480x480 LCD (matching the "Edgar Case 2.0" screen), and two extra USB-A ports. The maker built it after repeated comments that the Flipper Zero was "the tail wagging the dog" once a screen was attached to the Blackhat addon — Blackpants is the response, a full standalone Linux handheld with the Flipper Zero relegated to an optional attachment.

The hardware and firmware are published on GitHub under the MIT license (documentation, electrical and mechanical design files, and QMK keyboard firmware), making the whole build — Blackpants carrier plus the separate Flipper Blackhat repo — open source end to end. Rootkit Labs sold an assembled unit through their Shopify storefront for $150 CAD; as of this research the listing shows sold out. A Flipper Blackhat board is sold separately and is required to complete the device, and the maker warns that mismatched assembly of the pair can permanently damage the hardware.

## Make your own

Design files (docs, electrical, and mechanical folders) plus QMK keyboard firmware are in the [Blackpants GitHub repo](https://github.com/o7-machinehum/Blackpants), MIT licensed. Building one also requires a [Flipper Blackhat](https://github.com/o7-machinehum/flipper-blackhat) board to plug into the carrier; the original [WHY2025 badge](https://wiki.why2025.org/Badge) design is the starting point for the carrier's form factor.
