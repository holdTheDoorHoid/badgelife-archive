---
title: Education Security Community Minibadge (ESC)
id: saintcon-2024-edu-esc-badge-education-security-v1-v2
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: Jup1t3r
  url: https://github.com/utahsaint-org
summary: A SAINTCON 2024 community minibadge for the Education Security community, shaped like a keyboard "ESC" key as a pun on the community's initials.
functions: Commemorates participation in the Education Security community's activities (presentations and hands-on workshops on K-12, higher-ed, and library cybersecurity); lights a single LED when powered from the host badge.
look:
  colors:
  - red
  - black
  shape: keycap
  themes:
  - security
  - text
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: 1206 SMD LED with a 1206 resistor, hand-soldered single-pad style
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Earned by participating in the Education Security community's presentations and workshops at SAINTCON 2024, per the official MiniBadge Build Guide.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/EDU-ESC-Badge
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/EDU-ESC-Badge
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/EDU-ESC-Badge
  kind: repo
- label: 2024 SAINTCON MiniBadge Build Guide (PDF)
  url: https://github.com/utahsaint-org/saintcon.zip.files/blob/main/2024/2024-SAINTCON-MiniBadge-Guide-v3.0-10.20.2024-1.pdf
  kind: doc
images:
- file: assets/images/badges/saintcon-2024/edu-esc-badge-education-security-v1-v2/25dc585762.png
  source: https://github.com/utahsaint-org/MiniBadges2024/tree/main/EDU-ESC-Badge
  credit: Jup1t3r / utahsaint-org
  caption: 'Artwork proof (EDC-ART.ai) showing the badge outline: a keyboard ESC key, red keycap with black ESC legend'
contact: {}
notes:
- The discovery sweep titled this entry "EDU-ESC-Badge (Education Security, v1/v2)" and credited maker SHIFTY. Research found the repo folder this entry links to (EDU-ESC-Badge, files named ESC-Badge.*) was committed entirely by GitHub user Jup1t3r, who the 2024 SAINTCON MiniBadge Build Guide also credits by name as designer of the "Education Security Community Minibadge (ESC)" — so the title and maker have been corrected to match. The "v1/v2" and "SHIFTY" attribution in the sweep's title actually belong to a different, unrelated pair of folders in the same repo ("Education Security (ESC) - SHIFTY" and "Education Security (ESC) v2 SHIFTY"), which use a different shield-like artwork and a different maker credit; the sweep appears to have conflated the two. That SHIFTY-made pair is reported separately as another item worth its own entry.
status: released
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/EDU-ESC-Badge
  title: EDU-ESC-Badge (Education Security, v1/v2)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024
  title: utahsaint-org/MiniBadges2024 (repo root)
  accessed: '2026-09-10'
  note: Confirmed repo purpose (SAINTCON 2024 minibadges) and listed the EDU-ESC-Badge and Education Security (ESC) - SHIFTY / v2 folders as separate designs.
- kind: url
  url: https://github.com/utahsaint-org/saintcon.zip.files/blob/main/2024/2024-SAINTCON-MiniBadge-Guide-v3.0-10.20.2024-1.pdf
  title: 2024 SAINTCON MiniBadge Build Guide v3.0
  accessed: '2026-09-10'
  note: 'Official guide page for "Education Security Community Minibadge (ESC)": designer credit (Jup1t3r), summary text, difficulty, rarity, parts list (1206 LED, 1206 resistor, FR4 PCB, 4x 2-position headers), and assembly steps.'
- kind: url
  url: https://api.github.com/repos/utahsaint-org/MiniBadges2024/commits?path=EDU-ESC-Badge
  title: Commit history for EDU-ESC-Badge folder
  accessed: '2026-09-10'
  note: Both commits to this folder are authored by Jup1t3r, confirming maker.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: No storefront or quantity-made figure found; this was a free community minibadge, not sold. No photo of the assembled, populated board was found (only the vector artwork proof and PCB design files), so colors/shape are inferred from that artwork rather than a photo of the finished badge — noted as medium rather than high confidence. Quantity made is not stated anywhere found.
last_modified_date: '2026-09-10'
model:
  file: assets/models/saintcon-2024/edu-esc-badge-education-security-v1-v2.glb
  method: kicad
  source_file: EDU-ESC-Badge/ESC-Badge.kicad_pcb
  generated: '2026-09-10'
  bytes: 28568
---

Education Security is one of SAINTCON's recurring community tracks, focused on cybersecurity for K-12, higher-education, and library environments. For SAINTCON 2024 the community's minibadge — credited in the official MiniBadge Build Guide to designer Jup1t3r — takes the shape of a computer keyboard's "ESC" key, playing on the community's own initials (Education Security Community). The badge is a small red keycap-shaped PCB with a black silkscreened "ESC" legend on the face.

Electrically it is a simple, passive minibadge: a single 1206 SMD LED and a matching 1206 resistor, hand-soldered using the single-pad method, wired through four 2-position pin headers that plug it into a host badge for power — it carries no microcontroller of its own. The official guide rates it Beginner difficulty and Uncommon rarity, and says it was earned by attendees who took part in the Education Security community's presentations and hands-on workshops on defending and educating against "student hackers" and other education-sector cybersecurity topics, rather than sold or handed out unconditionally.

KiCad source, Gerbers, and the original Illustrator artwork are published in the utahsaint-org/MiniBadges2024 GitHub repository under the EDU-ESC-Badge folder, so the design can be reproduced, though no firmware is applicable since the board has no MCU.
