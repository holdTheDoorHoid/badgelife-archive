---
title: Grateful Dead Mini Badge (2022)
id: saintcon-2022-grateful-dead-mini-badge-2022
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: CompuDocUt
- name: SHIFTY
summary: A SAINTCON 2022 minibadge with the Grateful Dead "Steal Your Face" lightning-bolt skull etched into the PCB, lit by two blue LEDs.
functions: ''
look:
  colors:
  - gold
  - white
  - green
  shape: rectangle
  themes:
  - music
  - skull
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: Two blue LEDs (D1 "RED", D2 "BLUE" silkscreen labels) driven through a single shared 2200-ohm resistor.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: 'Maker published detailed illustrated assembly (soldering) instructions as a PDF; no schematic, board files, or Gerbers were published alongside it.'
links:
- label: github.com/CompuDocUt/SaintConMinibadges/blob/main/Grateful%20Dead%20Mini%20Badge%202022%20assembly%20instructions%20.pdf
  url: https://github.com/CompuDocUt/SaintConMinibadges/blob/main/Grateful%20Dead%20Mini%20Badge%202022%20assembly%20instructions%20.pdf
  kind: doc
- label: github.com/CompuDocUt/SaintConMinibadges
  url: https://github.com/CompuDocUt/SaintConMinibadges
  kind: repo
images:
  - file: assets/images/badges/saintcon-2022/grateful-dead-mini-badge-2022/b7646b3a91.jpg
    source: "https://github.com/CompuDocUt/SaintConMinibadges/blob/main/Grateful%20Dead%20Mini%20Badge%202022%20assembly%20instructions%20.pdf"
    credit: "CompuDocUt"
    caption: "Bare PCB with Grateful Dead Steal Your Face artwork and 2022 COMPUDOC/SHIFTY silkscreen"
  - file: assets/images/badges/saintcon-2022/grateful-dead-mini-badge-2022/59fb44e474.jpg
    source: "https://github.com/CompuDocUt/SaintConMinibadges/blob/main/Grateful%20Dead%20Mini%20Badge%202022%20assembly%20instructions%20.pdf"
    credit: "CompuDocUt"
    caption: "Assembled badge with two-pin header, seated in the SaintCon minibadge socket rail"
contact: {}
notes:
- 'The sweep''s sources list linked only the assembly-instructions PDF filename; the title matches it exactly, so no wording correction was needed.'
status: released
sources:
- kind: url
  url: https://github.com/CompuDocUt/SaintConMinibadges/blob/main/Grateful%20Dead%20Mini%20Badge%202022%20assembly%20instructions%20.pdf
  title: Grateful Dead Mini Badge (2022)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://raw.githubusercontent.com/CompuDocUt/SaintConMinibadges/main/Grateful%20Dead%20Mini%20Badge%202022%20assembly%20instructions%20.pdf
  title: Grateful Dead Mini Badge assembly instructions (PDF)
  accessed: '2026-09-10'
  note: Read in full; source for the PCB artwork/silkscreen, parts list (PCB, 2200-ohm resistor, 2x blue LEDs, 2x2-pin headers), assembly steps, and the two saved photos.
- kind: url
  url: https://github.com/CompuDocUt/SaintConMinibadges
  title: CompuDocUt/SaintConMinibadges (GitHub repo)
  accessed: '2026-09-10'
  note: Repo file listing confirms this and three sibling SAINTCON minibadges (BESD Train, CompuDoc, and a 2023 Grateful Dead badge) from the same maker.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed to exist and read the full assembly-instructions PDF, which is the only source found. No storefront, price, quantity, or Hackaday/press coverage located, so pricing, quantity, and general availability are unknown. The board silkscreen credits "COMPUDOC/SHIFTY", so SHIFTY is listed as a second maker/collaborator alongside CompuDocUt; not confirmed which of the two led design vs. board house liaison. The PDF notes both LEDs are blue "so that both will light" despite the silkscreen separately labeling pads RED and BLUE, i.e. there is no functional red LED on this badge - documented as-is rather than corrected. tech.mcu/tech.sao_version set to none since this is a passive two-LED board with a simple 2-pin power header, not a true SAO; it visually plugs into a socket rail alongside SAO-style boards in the maker''s own photo. A same-maker "Grateful Dead Mini Badge 2023" PDF exists in the same repo and is reported separately below rather than folded into this entry.'
last_modified_date: '2026-09-10'
---

CompuDocUt (with SHIFTY credited on the board silkscreen) made this SAINTCON 2022 minibadge featuring the Grateful Dead's "Steal Your Face" lightning-bolt skull, etched in gold and white on the PCB. It is a simple, learn-to-solder-friendly board: one 2200-ohm resistor and two blue LEDs (silkscreened D1/RED and D2/BLUE) share a single current-limiting resistor, so both LEDs glow blue regardless of which pad they're read from - the maker's own instructions note this was a fix for a problem running two different LED colors off one resistor. Power comes in through a pair of 2-pin headers that let the badge plug into the same style of rail/socket system used elsewhere on the wearer's main SAINTCON badge or a minibadge holder.

The maker published a short, photo-heavy PDF walking through assembly step by step, aimed at soldering beginners, down to LED polarity (the green paint dot marks the cathode) and two alternate methods for placing the header pins. No schematic, PCB design files, or firmware were published alongside it - it is documentation for building the kit, not an open-hardware release. No price, production quantity, or storefront listing was found for this badge.

## Make your own

Build steps from the maker's PDF: solder the 2200-ohm resistor at R1; solder one blue LED at the pad marked BLUE and the second blue LED at the pad marked RED, orienting each LED's green-dot (cathode) lead opposite the board's "+" marking; then solder in the two 2-pin headers, long leads on the same side as the resistor/LEDs (the maker suggests seating the header pins in a socket first to keep them straight before soldering).
