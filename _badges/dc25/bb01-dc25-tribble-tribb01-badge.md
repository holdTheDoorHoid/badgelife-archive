---
title: BB01 - DC25 Tribble/TriBB01 Badge
id: dc25-bb01-dc25-tribble-tribb01-badge
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: anotheremily
  url: https://hackaday.io/anotheremily
summary: A hand-made, glowing plush "tribble" badge built by Beyond Binaries, a group for trans/non-binary/non-cis hackers at DEF CON and Queercon, for DEF CON 25.
functions: Two buttons cycle through 9 color patterns and 4 transition modes on the internal NeoPixels; clips on to be worn as a lanyard badge or purse charm.
look:
  colors:
  - white
  - purple
  - multicolor
  shape: null
  themes:
  - animal
  - sci-fi
  - wearable
  - jewelry
tech:
  mcu: Adafruit Trinket 5V
  leds:
    count: 7
    type: NeoPixel Jewel (5050 RGBW, cool white)
    note: driven through a 470 ohm current-limiting resistor
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Hand-soldered and hand-sewn in a limited run for Beyond Binaries members/attendees at DEF CON 25; not sold commercially.
make_your_own:
  open_source: true
  hardware_url: https://hackaday.io/project/25878-bb01-dc25-tribbletribb01-badge
  firmware_url: https://hackaday.io/project/25878-bb01-dc25-tribbletribb01-badge
links:
- label: hackaday.io/project/25878-bb01-dc25-tribbletribb01-badge
  url: https://hackaday.io/project/25878-bb01-dc25-tribbletribb01-badge
  kind: hackaday
  archived: https://web.archive.org/web/20251212042715/https://hackaday.io/project/25878-bb01-dc25-tribbletribb01-badge
images:
- file: assets/images/badges/dc25/bb01-dc25-tribble-tribb01-badge/6769007680.jpg
  source: https://hackaday.io/project/25878-bb01-dc25-tribbletribb01-badge
  credit: anotheremily
  caption: Five BB01 Tribble badges lit in different colors, showing the NeoPixel Jewel eyes through the fur
  archived: https://web.archive.org/web/20251212042715/https://hackaday.io/project/25878-bb01-dc25-tribbletribb01-badge
contact: {}
notes:
- Sheet title styles it "BB01 - DC25 Tribble/TriBB01 Badge"; the Hackaday.io project itself is titled "BB01 - DC25 Tribble/TriBB01 Badge" as well, so kept as-is.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/25878-bb01-dc25-tribbletribb01-badge
  title: BB01 - DC25 Tribble/TriBB01 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''DEF CON 25''.'
  archived: https://web.archive.org/web/20251212042715/https://hackaday.io/project/25878-bb01-dc25-tribbletribb01-badge
- kind: url
  url: https://hackaday.io/project/25878-bb01-dc25-tribbletribb01-badge
  title: BB01 - DC25 Tribble/TriBB01 Badge (project page)
  accessed: '2026-09-07'
  note: Confirmed maker (anotheremily), event/year (DEF CON 25, 2017), hardware (Adafruit Trinket 5V + 2x NeoPixel Jewel), functions (9 color patterns, 4 transition modes, two buttons), and that source code and Gerbers (v1.0/v1.1) are published on the project page. Also identified the group as Beyond Binaries.
  archived: https://web.archive.org/web/20251212042715/https://hackaday.io/project/25878-bb01-dc25-tribbletribb01-badge
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Price and total quantity made are not stated on the Hackaday.io project page; left empty. No separate maker storefront, repo, or social post was found beyond the Hackaday.io project itself, which hosts both the write-up and the linked source/Gerber downloads, so no additional links were added. Distribution set to free_drop since this reads as a hand-made badge given to Beyond Binaries members/attendees rather than sold, though the page does not explicitly confirm this framing.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc25/bb01-dc25-tribble-tribb01-badge.glb
  method: gerber
  source_file: gerber_v1.0_production.zip/gerber
  generated: '2026-09-07'
  bytes: 117352
  size_mm:
  - 49.8
  - 34.8
---

BB01, also called the "TriBB01" badge, is a hand-built, furry, glowing tribble badge made for DEF CON 25 (2017) by a Hackaday.io user going by anotheremily, for Beyond Binaries, a group for trans, non-binary, and non-cisgender hackers at DEF CON and Queercon. Rather than a bare PCB, the badge hides its electronics inside a small ball of white or purple faux fur, styled after the tribbles from Star Trek, and clips onto a lanyard or bag so it can be worn or carried as a charm.

Inside each tribble is an Adafruit Trinket 5V driving two 7-LED NeoPixel Jewel modules (5050 RGBW, cool white) through a current-limiting resistor, with two tactile buttons (pulled up with 10k resistors) letting the wearer cycle through 9 color patterns and 4 transition modes. The firmware source and both a v1.0 and a corrected v1.1 Gerber set are published on the project's Hackaday.io page for anyone who wants to build their own.

No price or total production count is listed on the project page; from the description and photos, the badges appear to have been a small, hand-soldered and hand-sewn batch made for Beyond Binaries' own community rather than a commercial product.
