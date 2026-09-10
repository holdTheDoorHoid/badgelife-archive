---
title: Red Team MiniBadge
id: saintcon-2022-red-team-minibadge-2022
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: Jup1t3r
summary: A community minibadge for SAINTCON 2022's Red Team Community, earned by visiting the community and interacting with them at the con.
functions: 'Two LEDs plus a status LED, controlled by a hand-solderable JP1 jumper that picks between blink and solid-on modes.'
look:
  colors:
  - red
  - black
  shape: rectangle
  themes:
  - security
  - village badge
tech:
  mcu: none
  leds:
    count: 3
    type: reverse-mount
    note: Two edge LEDs plus one center LED; mode set by soldering the BLINK or SOLID pads of jumper JP1 (or leaving it open/bridging both, which the guide marks BAD).
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: none
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Handed out by visiting the Red Team Community at SAINTCON 2022 and interacting with them.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  kind: website
images:
  - file: assets/images/badges/saintcon-2022/red-team-minibadge-2022/db7a782b02.jpg
    source: "https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf"
    credit: "SAINTCON / Jup1t3r"
    caption: "Front of the 2022 Red Team Community minibadge"
  - file: assets/images/badges/saintcon-2022/red-team-minibadge-2022/71bacc7c60.jpg
    source: "https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf"
    credit: "SAINTCON / Jup1t3r"
    caption: "Back of the PCB showing LEDs, resistor, and BLINK/SOLID jumper"
contact: {}
notes:
- The sweep's sheet listed the title as "RED TEAM MINIBADGE (2022)"; the assembly guide itself just says "RED TEAM MINIBADGE" (the "(2022)" was added by the sheet to disambiguate from the 2021 edition). Title here follows the guide's own styling (title case, no year suffix), matching how "RED TEAM" in 2021 is recorded.
- This is a distinct minibadge from the 2021 "RED TEAM" minibadge by the same maker (id saintcon-2021-red-team); SAINTCON's Red Team Community minibadge appears to be redesigned each year.
status: released
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: RED TEAM MINIBADGE (2022)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2022); event read as ''saintcon-2022''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: SAINTCON MiniBadge Assembly Guide 2022, p.24 (Red Team MiniBadge)
  accessed: '2026-09-10'
  note: Primary source for maker, description, difficulty/rarity, distribution method, LED/jumper assembly details, and both badge photos.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Confirmed directly in the maker-credited 2022 SAINTCON MiniBadge Assembly Guide (p.24), not just a search snippet. No storefront, repo, or design-file listing was found — this looks like an in-person con giveaway with no public digital trail beyond the assembly guide, consistent with other SAINTCON community minibadges. Quantity made is not stated. Rarity is listed as "Common" and difficulty as "Beginner" in the guide, but the archive has no controlled field for rarity/difficulty so that is only noted here.
last_modified_date: '2026-09-10'
---

The Red Team MiniBadge is a 2022 SAINTCON community minibadge designed by Jup1t3r for the con's Red Team Community, a track focused on penetration-testing tools and tactics. Like other SAINTCON community minibadges, it wasn't sold — attendees earned it for free by visiting the Red Team Community's area and interacting with them during the con.

The board is a simple, unpowered add-on (it draws power from the host badge) with three LEDs: two edge LEDs and one center LED. Assemblers solder the LEDs and a resistor using the single-pad hand-soldering method, then choose between a "blink" or "solid on" behavior by bridging one of two pads on jumper JP1 (leaving both pads bridged at once is called out in the guide as a bad configuration). It mounts via a set of four 2-position headers, and its red-and-black graphic reuses the same three-hooded-figures "Red Team Community" artwork also seen on the 2021 edition of this minibadge by the same designer.

No public repository, storefront listing, or design files for this minibadge were found; its only known documentation is the official SAINTCON 2022 MiniBadge Assembly Guide.
