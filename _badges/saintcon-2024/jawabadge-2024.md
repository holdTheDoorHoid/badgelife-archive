---
title: STAR WARS Jawa Minibadge
id: saintcon-2024-jawabadge-2024
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: Jup1t3r
summary: A Jawa-shaped SAINTCON minibadge with two white "eye" LEDs and a third red LED, part of the designer's ongoing Star Wars minibadge series.
functions: 'No interactivity beyond the three through-hole LEDs, which light continuously when plugged into a powered minibadge chain; purely passive (LEDs and resistors, no logic), so no blinking or other effect is possible.'
look:
  colors:
  - black
  - yellow
  - white
  - red
  shape: character
  themes:
  - sci-fi
  - movie
  - pop culture
tech:
  mcu: none
  leds:
    count: 3
    type: THT
    note: Two LEDs for the Jawa's eyes (the front artwork shows them as white circles) and a third LED (silkscreened "RED LED") elsewhere on the board -- its position doesn't line up with the blaster held in the front artwork, so it isn't confirmed as a "muzzle" light; hand-soldered single-pad style per the build guide.
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: limited
  distribution:
  - swap
  where: Traded in person with the designer, Jup1t3r, at the SAINTCON 2024 Minibadge Trading space; not sold.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/JawaBadge-2024
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/JawaBadge-2024
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/JawaBadge-2024
  kind: repo
- label: 2024 SAINTCON MiniBadge Build Guide (PDF)
  url: https://github.com/utahsaint-org/saintcon.zip.files/blob/main/2024/2024-SAINTCON-MiniBadge-Guide-v3.0-10.20.2024-1.pdf
  kind: doc
images: []
contact: {}
notes:
- Star Wars Jawa-themed minibadge submitted for SAINTCON 2024. Found by the event-year sweep, task saintcon-2024.
- 'The sweep''s sheet title was the repo folder name, "JawaBadge-2024"; the maker''s own build-guide entry calls it "STAR WARS Jawa Minibadge" and says it is "a continuation of the Star Wars series of badges."'
status: released
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/JawaBadge-2024
  title: JawaBadge-2024
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/JawaBadge-2024
  title: JawaBadge-2024 design files
  accessed: '2026-09-10'
  note: KiCad schematic/PCB and Gerbers confirm the part list -- 3x Device:LED, 3x Device:R_US, one Minibadge:MiniBadge_Simple connector footprint (2-pin minibadge power header, no MCU). No LED-color or blink/logic info in the source files.
- kind: url
  url: https://github.com/utahsaint-org/saintcon.zip.files/blob/main/2024/2024-SAINTCON-MiniBadge-Guide-v3.0-10.20.2024-1.pdf
  title: 2024 SAINTCON MiniBadge Build Guide v3.0
  accessed: '2026-09-10'
  note: 'Official build guide, page 117: names the badge "STAR WARS Jawa Minibadge", credits designer Jup1t3r, gives assembly steps (THT LEDs single-pad soldered, resistors, pin headers), rates it difficulty "Intermediate" and rarity "Uncommon", and says to find Jup1t3r at the Minibadge Trading space to get one. The page''s front-side artwork shows two white circular "eyes" at the same hood position as the two eye LEDs on the back diagram, supporting "white" for those two; the third LED is only silkscreened "RED LED", with no text calling it a blaster/muzzle light, and its board position (lower-left, near the keychain loop) does not line up with the blaster''s muzzle in the front artwork (upper-right) -- fact-check pass removed that unsupported "blaster muzzle" characterization and a separate unsupported claim that the LEDs could blink.'
research:
  status: verified
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Verified against the maker''s GitHub repo (KiCad source confirms 3x LED, 3x resistor, one MiniBadge connector, no MCU) and page 117 of the official 2024 SAINTCON MiniBadge Build Guide PDF (title, designer, difficulty/rarity, how-to-get-one text, and front/back reference art, fetched and rendered directly from the PDF). Fact-check pass (2026-09-10) corrected two unsupported claims from the prior research pass: (1) the LEDs cannot "blink" -- the board is passive (LEDs + resistors, no logic/MCU) and no source describes any blink or power-rail-pulse behavior, so `functions` was corrected to state it is purely passive; (2) the red LED was described as lighting the blaster''s "muzzle", but its position in the build-guide diagram (lower-left, by the keychain loop) does not match the muzzle location in the front artwork (upper-right) and no source calls it a muzzle light, so that framing was removed from `summary`, `tech.leds.note`, and the body, and `look.colors` gained `red` for the LED''s actual color. No price or production quantity is published anywhere found; SAINTCON minibadges are generally traded/given rather than sold, consistent with the build guide''s "go find the designer to trade" instructions. No maker photo of the assembled/soldered badge found -- only vector artwork and the build guide''s front/back reference renders, which are embedded in the PDF rather than hosted at a stable image URL, so none were saved via fetch_image.py. No hackaday/social presence found for "Jup1t3r" tied to this badge beyond the SAINTCON minibadge scene.'
last_modified_date: '2026-09-10'
---

The STAR WARS Jawa Minibadge is a SAINTCON 2024 minibadge shaped like a hooded Jawa from Star Wars, designed by Jup1t3r as part of an ongoing Star Wars-themed minibadge series for the con. The black PCB carries three through-hole LEDs -- two sitting in the hood as the Jawa's glowing eyes (shown white in the front artwork) and a third, silkscreened "RED LED," elsewhere on the board -- wired through three resistors off the shared minibadge power header, with no microcontroller or other logic on board.

Like most SAINTCON minibadges it wasn't sold; the official 2024 build guide rates it "Intermediate" difficulty and "Uncommon" rarity, and tells attendees to track down Jup1t3r in person at the con's Minibadge Trading space to get one. The KiCad source and Gerbers are published on the community's shared MiniBadges2024 GitHub repo, so anyone can fabricate their own copy, though no separate firmware exists since the board is purely LED-and-resistor.

## Make your own

The `JawaBadge-2024` folder in the [MiniBadges2024 repo](https://github.com/utahsaint-org/MiniBadges2024/tree/main/JawaBadge-2024) has the complete KiCad project (schematic, PCB, and fab-ready Gerbers/drill files) plus the original vector artwork. Order the Gerbers from any PCB house, then hand-solder the two white LEDs and one red LED using the single-pad method described in the official build guide, followed by the three resistors and the 2-pin minibadge header.

