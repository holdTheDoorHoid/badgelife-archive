---
title: SAINTCON 2023 Attendee Minibadge
id: saintcon-2023-saintcon-2023-attendee-game-minibadge
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: MK Factor
summary: The official 2023 SAINTCON attendee minibadge, given to every attendee as part of the badge game; a "CG ID Badge" themed PCB with an onboard EEPROM the main badge reads to identify it.
functions: Identifies itself to the main SAINTCON badge via an onboard EEPROM, read through the badge's minibadge slot; the badge's own RGB LED lights up to confirm a valid read. Part of the wider SAINTCON badge game alongside many other collectible game minibadges.
look:
  colors:
  - green
  - gold
  shape: rectangle
  themes:
  - security
  - puzzle
  - ctf
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - i2c
  battery: null
  sao_version: null
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Included automatically with every 2023 SAINTCON attendee badge; other game-related minibadges in the same series had to be earned by playing the badge game.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  kind: doc
images:
  - file: assets/images/badges/saintcon-2023/saintcon-2023-attendee-game-minibadge/159cab9075.jpg
    source: "https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf"
    credit: "MK Factor / SAINTCON"
    caption: "Front of the Attendee Minibadge (CG ID Badge design)"
  - file: assets/images/badges/saintcon-2023/saintcon-2023-attendee-game-minibadge/fe0596074f.jpg
    source: "https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf"
    credit: "MK Factor / SAINTCON"
    caption: "Back of the Attendee Minibadge showing EEPROM and MK Factor logo"
contact: {}
notes:
- Official 2023 badge-game minibadge with an onboard EEPROM the main SAINTCON badge reads via its RGB LED slot; separate from the main compukidmike badge PCB already catalogued. Found by the event-year sweep, task saintcon-2023.
- The 2023 SAINTCON Minibadge Guide (p.13) titles this piece "Official Game Minibadge — Attendee Minibadge (and other badge game minibadges)"; the sweep's shorter "Attendee Game Minibadge" wording is kept in the entry id/slug, but the title here is trimmed to match the guide's own name for the card ("Attendee Minibadge").
status: released
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  title: SAINTCON 2023 Attendee Game Minibadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2023); event read as ''saintcon-2023''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  title: 2023 SAINTCON Minibadge Guide (10.31.2023), p.13 "Official Game Minibadge"
  accessed: '2026-09-10'
  note: Confirms designer (MK Factor), that it is the official 2023 attendee minibadge included free with every badge, has a pre-soldered/pre-programmed EEPROM the main badge reads via RGB LED, difficulty beginner, rarity common, and no separate LED of its own.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Only source found is the official SAINTCON 2023 Minibadge Guide itself, but it is the maker/event's own primary document and fully confirms the sweep's summary line. No maker page, storefront, or third-party coverage exists for this specific minibadge (it was never sold - it was bundled free with every attendee badge). MCU/EEPROM chip model, LED count/type, and PCB dimensions are not stated in the guide and are left empty rather than guessed.
last_modified_date: '2026-09-10'
---

The SAINTCON 2023 Attendee Minibadge is the official, free minibadge every attendee received as part of that year's badge game, designed by MK Factor. It carries a "CG ID Badge" motif on the front and a small pre-soldered, pre-programmed EEPROM on the back; when plugged into the main SAINTCON badge's minibadge slot, the host badge's own RGB LED lights up to confirm it can read the chip and identify the piece. Unlike most of the other badge-game minibadges, this one has no LED of its own, since the host badge supplies the illumination.

Assembly only required soldering the header pins to the back of the board — the guide rates it "beginner" difficulty and "common" rarity, since every attendee got one automatically rather than having to earn it through gameplay. It sits alongside a large family of other official and community game minibadges from the same event that were only obtainable by playing the SAINTCON badge game.

No separate maker page, storefront listing, or third-party writeup for this specific minibadge could be found; the only known documentation is SAINTCON's own 2023 Minibadge Guide PDF, which is treated here as the primary/maker source.
