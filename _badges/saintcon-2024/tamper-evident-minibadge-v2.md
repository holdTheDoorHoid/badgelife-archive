---
title: Tamper Evident minibadge (v2)
id: saintcon-2024-tamper-evident-minibadge-v2
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
series: Tamper Evident
makers:
- name: SHIFTY
summary: A SAINTCON minibadge whose PCB art recreates a "WARRANTY VOID IF REMOVED" tamper-evident sticker, peeled back to reveal a shredded foil pattern underneath.
functions: 'Passive: two LEDs light when the badge is powered through its host-badge connection. No other electronic function.'
look:
  colors:
  - red
  - black
  - white
  - silver
  shape: rectangle
  themes:
  - security
  - puzzle
  - village badge
tech:
  mcu: none
  leds:
    count: 2
    type: 1206 SMD
    note: Two 1206 LEDs (D1, D2), each with its own 1206 resistor, per the KiCad schematic and the SAINTCON 2024 Minibadge Guide's assembly instructions; no microcontroller, so they simply light when powered.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Visit the Tamper Evident community table at SAINTCON 2024 and assemble it there from the parts provided; no price or quantity is stated in the official guide.
make_your_own:
  open_source: true
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Tamper%20Evident%20v2%20-%20SHIFTY
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/Tamper%20Evident%20v2%20-%20SHIFTY
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Tamper%20Evident%20v2%20-%20SHIFTY
  kind: repo
images:
- file: assets/images/badges/saintcon-2024/tamper-evident-minibadge-v2/e3f1019de7.png
  source: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Tamper%20Evident%20v2%20-%20SHIFTY
  credit: SHIFTY
  caption: Tamper Evident minibadge v2 PCB artwork
contact: {}
notes:
- Tamper-evident themed minibadge v2 for SAINTCON 2024, credited to SHIFTY. Found by the event-year sweep, task saintcon-2024.
- The repo folder is titled "Tamper Evident v2 - SHIFTY"; the entry title keeps the sweep's parenthetical wording ("(v2)"). The SAINTCON 2024 Minibadge Guide itself calls it the "Tamper Evident Community Minibadge" with no version number visible to attendees; the "(v2)" title is kept here (as it already was) to match the cross-reference to it in the 2023 sibling entry's body text.
- SHIFTY has made several "Tamper Evident" themed badges across years (a SAINTCON 2022 Tamper Evident BADGE and a 2023 Tamper Evident Community Badge are separate, already-cataloged entries); this v2 minibadge appears to be the 2024 entry in that recurring line, so it is tagged with series "Tamper Evident".
- The KiCad schematic (D1, D2 = LED, R1, R2 = resistor, plus a MiniBadge_Simple connector wired to a "+VBATT" net) confirms two 1206 LEDs with current-limiting resistors and no MCU or onboard battery. The official SAINTCON 2024 Minibadge Guide (p.32) independently shows the same board (red PCB, "TAMPER"/"EVIDENT" text, the WARRANTY-VOID sticker art, "SAINTCON 2024" and "SHIFTY" silkscreen) with matching parts (1206 LED, 1206 resistor, FR4 PCB, 2-pin headers), rated beginner difficulty / uncommon rarity, obtained by visiting the Tamper Evident community table.
status: listed
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Tamper%20Evident%20v2%20-%20SHIFTY
  title: Tamper Evident minibadge (v2)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Tamper%20Evident%20v2%20-%20SHIFTY
  title: MiniBadges2024/Tamper Evident v2 - SHIFTY at main
  accessed: '2026-09-10'
  note: Confirmed the repo folder is real and contains KiCad hardware source (schematic, PCB, footprint) plus SVG/PSD/PNG artwork for a "warranty void if removed" sticker design; no README or maker write-up in this folder describing chip, LEDs, price, or quantity.
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/Tamper%20Evident%20v2%20-%20SHIFTY/Tamper%20evident.png
  title: Tamper evident.png
  accessed: '2026-09-10'
  note: Source image saved to the entry; shows the tamper-evident-sticker artwork used on the badge.
- kind: url
  url: https://github.com/utahsaint-org/saintcon.zip.files/blob/main/2024/2024-SAINTCON-MiniBadge-Guide-v3.0-10.20.2024-1.pdf
  title: 2024 SAINTCON MiniBadge Guide v3.0 (p.32, Tamper Evident Community Minibadge)
  accessed: '2026-09-10'
  note: Official SAINTCON build guide, found via a web search this pass turned up after the researcher reported not finding it. Page 32 confirms designer (SHIFTY), the same artwork on a red PCB, front/back photos, difficulty (beginner), rarity (uncommon), "how do I get one" (visit the community), and a parts list of 1206 LED, 1206 resistor, FR4 PCB, and 2-pin headers, matching the KiCad schematic.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-10'
  notes: Fact-check pass located the official SAINTCON 2024 Minibadge Guide (p.32), which the original research missed; it independently confirms the maker, artwork, and hardware, and supplied LED count, MCU, battery, and how-to-get-one facts that were previously left blank, matching the same pattern as the 2023 sibling "Tamper Evident Community Badge" entry. Price, exact quantity, and current availability are still not stated anywhere found and remain blank. No independent press or social coverage of this specific badge was found.
last_modified_date: '2026-09-10'
model:
  file: assets/models/saintcon-2024/tamper-evident-minibadge-v2.glb
  method: kicad
  source_file: Tamper Evident v2 - SHIFTY/Tamper Evident v2 - SHIFty.kicad_pcb
  generated: '2026-09-10'
  bytes: 58148
---

The Tamper Evident minibadge (v2) is a SAINTCON 2024 minibadge by SHIFTY, part of a recurring "Tamper Evident" themed line that also includes a SAINTCON 2022 badge and a 2023 community badge. Its PCB artwork recreates a classic "WARRANTY VOID IF REMOVED" tamper-evident sticker on a red board, drawn peeling back to reveal a shredded destructive-vinyl pattern underneath — a visual joke on the tamper-evidence theme rather than a functional tamper sensor. SAINTCON's official 2024 Minibadge Guide lists it as the "Tamper Evident Community Minibadge," rates it "beginner" difficulty and "uncommon" rarity, and says it's obtained by visiting the Tamper Evident community table and assembling it there.

Electronically it is simple: two 1206 SMD LEDs (D1 and D2), each with its own current-limiting resistor, wired through the minibadge's edge connector so it lights up when powered from a host badge. There is no microcontroller or onboard battery. The project's GitHub repository includes KiCad schematic, PCB, and footprint files alongside the source SVG and Photoshop artwork, so the hardware design is openly published; no price, production quantity, or ongoing availability is stated in either the repository or the official guide, so those fields are left blank.
