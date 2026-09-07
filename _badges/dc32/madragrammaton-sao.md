---
title: Madragrammaton SAO
id: dc32-madragrammaton-sao
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
makers:
- name: The Mad Hatters
  url: https://madhatters.lol
summary: "A companion SAO to the Mad Hatter Auto Revelator badge from Utah group The Mad Hatters: 16 LEDs behind a Mad-Hatter-themed medallion, with an onboard potentiometer that dials the flash rate of the badge's own hat LED."
functions: "16 LEDs light up the SAO's face; a potentiometer on the SAO controls the flash rate of the LED in the host badge's 3D-printed top hat. No menu or display of its own."
look:
  colors:
  - black
  - red
  shape: custom
  themes:
  - meme
  - mascot
tech:
  mcu: none
  leds:
    count: 16
    type: null
    note: "Maker's page states '16 LEDs' without a part number."
  display: none
  connectivity: []
  battery: CR2032
  sao_version: v1.69bis
get_one:
  price: $25.00
  price_usd: 25.0
  quantity: '75'
  availability: unknown
  availability_note: "Not found in Hacker Warehouse's online store search on 2026-09-06 (searching 'mad hatter' returns only HackRF One listings). Price and quantity come only from the community sheet; the maker's page states neither."
  distribution:
  - purchase
  where: "Hacker Warehouse at DEF CON 32 (Las Vegas, August 2024), sold alongside the Mad Hatter Auto Revelator badge, per the maker's page."
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: "No schematic, PCB, or firmware files for the SAO itself were found in the maker's defcon2024badge GitHub repository. The repo's stl/ folder does include a print-ready top hat sized for the SAO's connector (tophat_dc32_sao.stl), remixed by The Mad Hatters from a design by Printables user lytta (CC BY 4.0)."
links:
- label: madhatters.lol
  url: https://madhatters.lol
  kind: website
- label: GitHub repo (badge hardware/firmware; includes the SAO's top hat STL)
  url: https://github.com/the-mad-hatters/defcon2024badge
  kind: repo
- label: "SAO top hat STL (stl/tophat_dc32_sao.stl)"
  url: https://github.com/the-mad-hatters/defcon2024badge/tree/main/stl
  kind: fab
images:
- file: assets/images/badges/dc32/madragrammaton-sao/2d6cfcd7a9.png
  source: "https://madhatters.lol/"
  credit: "The Mad Hatters"
  caption: "The Madragrammaton SAO, lit red, in a mirrored macro shot from the maker's page"
contact: {}
notes:
- "Sold as a companion to the Mad Hatter Auto Revelator badge (see dc32-mad-hatter-auto-revelator); same maker, same event."
status: released
sources:
- kind: sheet
  event: dc32
  row: 108
  updated: ''
- kind: url
  url: https://madhatters.lol/
  title: "Mad Hatter Auto Revelator (The Mad Hatters) — Part II: Madragrammaton SAO"
  accessed: '2026-09-06'
  note: "Maker's own page, 'PART II: MADRAGRAMMATON SAO' section: 16 LEDs, potentiometer to control flash rate of the LED in the badge's hat, connects via v1.69bis SAO connector or runs standalone on a CR2032, sold at Hacker Warehouse at DC32. Also the source of the product photo (madragrammaton_sao_image.png)."
- kind: url
  url: https://github.com/the-mad-hatters/defcon2024badge
  title: GitHub - the-mad-hatters/defcon2024badge
  accessed: '2026-09-06'
  note: "Repository tree checked for SAO-specific hardware/firmware files; only a top-hat STL for the SAO (stl/tophat_dc32_sao.stl) was found, no schematic or PCB source."
- kind: url
  url: https://github.com/the-mad-hatters/defcon2024badge/blob/main/stl/README.md
  title: stl/README.md
  accessed: '2026-09-06'
  note: "Describes tophat_dc32_sao.stl as a print-ready hat for the SAO connector, remixed from Printables user lytta's design (CC BY 4.0)."
- kind: url
  url: https://hackerwarehouse.com/?s=mad+hatter&post_type=product
  title: You searched for mad hatter - Hacker Warehouse
  accessed: '2026-09-06'
  note: "Store search for 'mad hatter' returns only HackRF One listings; no Madragrammaton product found, so current availability is unknown."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: "Core description (16 LEDs, potentiometer controlling the badge hat LED's flash rate, v1.69bis connector, CR2032 option, Hacker Warehouse availability) comes from the maker's own page and matches the note already recorded on the sibling badge entry (dc32-mad-hatter-auto-revelator). Not independently confirmed: LED part number/type, any onboard chip (the description reads like a passive potentiometer + LED board with no MCU, but this is inferred, not stated), and the sheet's price ($25) and quantity (75), which the maker's page does not repeat. No PCB/schematic source files were found for the SAO itself, only a 3D-printable hat sized for it. Shape/colors are judged from the one product photo (a mirrored macro shot), which does not show the full board outline clearly. No Hackaday, Reddit, or press coverage of the SAO specifically was found; a live Hacker Warehouse search turned up no listing, so present-day availability is unconfirmed."
last_modified_date: '2026-09-06'
---

The Madragrammaton is the SAO half of The Mad Hatters' DEF CON 32 release, sold alongside their Mad Hatter Auto Revelator badge at Hacker Warehouse in August 2024. Where the badge carries the joke's OLED "seer stones" and menu system, the SAO is simpler: a small board bearing the group's Mad Hatter character and the "MADRAGRAMMATON" lettering, lit by 16 LEDs of its own. A potentiometer on the SAO doesn't control its own lights, but instead dials the flash rate of the LED inside the badge's 3D-printed top hat, letting a wearer plug in the add-on and tune part of the main badge's animation from the SAO itself.

It connects to the badge with a standard v1.69bis SAO header, or can run on its own from a CR2032 coin cell when unplugged. No firmware, chip, or PCB source files for the SAO were found in the maker's public repository; the one file specific to it is a print-ready top hat STL sized for the SAO's connector, a remix of a design by Printables user lytta, released under a CC BY 4.0 license alongside the rest of the project's 3D-printable parts.
