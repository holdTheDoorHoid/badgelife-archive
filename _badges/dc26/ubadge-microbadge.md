---
title: microbadge (uBadge)
id: dc26-ubadge-microbadge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Joe Fitz (securelyfitz)
  url: https://github.com/securelyfitz
summary: A functional badge built into a single square centimeter, based on a stripped-down Digispark/ATtiny85 with one SAO header, designed to be extended with plug-together "arms," faces, and add-ons.
functions: Runs user-programmable ATtiny85 code, reprogrammable over USB (micronucleus/Digispark bootloader); the SAO header carries power, ground and I2C to whatever arms/faces/add-ons are plugged in, including two proof-of-concept "polyglot" sketches that abuse the I2C bus timing to drive NeoPixels or push out UART on the data line.
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
  - minimalist
  - village badge
tech:
  mcu: ATtiny85
  leds: null
  display: none
  connectivity:
  - i2c
  - usb
  inputs: []
  power: external 3.3V (no onboard regulator)
  battery: CR2032 (edge-mount pad; typically supplied by a plugged-in face/arm instead)
  sao_version: v1
  sao_ports: 1
get_one:
  price: ''
  price_usd: null
  quantity: '1100 (11 panels of a 10x10 panelized grid)'
  availability: unknown
  distribution:
  - free_drop
  where: Given out by Joe Fitz (securelyfitz) at DEF CON 26, 2018.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/securelyfitz/microbadge
  firmware_url: null
  gerbers_url: https://github.com/securelyfitz/microbadge/tree/master/hardware/gerbers
  eda_tool: Eagle
  license: null
links:
- label: github.com/securelyfitz/microbadge
  url: https://github.com/securelyfitz/microbadge
  kind: repo
- label: "Hackaday: All The Badges Of DEF CON 26, Vol 1 (uBadge section)"
  url: https://hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1/
  kind: article
images:
- file: assets/images/badges/dc26/ubadge-microbadge/6faa6f202a.jpg
  source: "https://hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1/"
  credit: "Hackaday"
  caption: "The microbadge shown for scale, roughly 1cm square"
- file: assets/images/badges/dc26/ubadge-microbadge/ba665d009e.jpg
  source: "https://hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1/"
  credit: "Hackaday"
  caption: "Microbadge fitted with a set of plug-together SAO 'arms'"
contact: {}
notes:
- 'Sweep imported this as "uBadge (microbadge)"; the maker''s own README titles the repo just "microbadge" ("functional badge in 1 square centimeter"), and Hackaday''s coverage calls it "uBadge." Kept both names in the title since sources use them interchangeably.'
- 'Likely the same physical item as dc26-ubadge-badge ("uBadge (μBadge)"), a separate stub entry from the same maker/event pulled from the same Hackaday article — see duplicate_of in the research report.'
- No price is stated anywhere found; it was handed out for free at the con rather than sold.
- No explicit software/hardware license found in the repo (no LICENSE file), though the design files (Eagle schematic/board/gerbers) are published in the open GitHub repo.
status: released
sources:
- kind: url
  url: https://github.com/securelyfitz/microbadge
  title: uBadge (microbadge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc26-saos); event read as ''dc26''.'
- kind: url
  url: https://github.com/securelyfitz/microbadge
  title: "microbadge README"
  accessed: '2026-09-08'
  note: Maker's own description of design, chip, assembly (1100 units via 1BitSquared/Piotr), BOM cost, and add-on ecosystem.
- kind: url
  url: https://hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1/
  title: "All The Badges Of DEF CON 26, Vol 1 - uBadge section"
  accessed: '2026-09-08'
  note: Independent confirmation of the item (called "uBadge"), photos, and the 10x10 panel / 11 panel production detail.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Core facts (maker, event/year, chip, SAO design, ~1100 units, free distribution) confirmed by both the maker''s own GitHub README and independent Hackaday coverage. No price, license, or firmware repo found. Likely duplicates dc26-ubadge-badge — see research report.'
last_modified_date: '2026-09-08'
---

The microbadge (also called the uBadge by Hackaday and in DEF CON badge roundups) is a functional electronic badge shrunk down to about one square centimeter, made by Joe Fitz (securelyfitz) for DEF CON 26 in 2018. It strips a Digispark ATtiny85 board down to the essentials — dropping the USB-A connector, voltage regulator, and 3.3V protection diodes in favor of a MicroUSB header and a single SAO (Shitty Add-On) connector carrying power, ground, and I2C. Because it has no onboard regulator, it needs external 3.3V power, typically supplied by whatever "arm," "face," or other add-on is plugged into its SAO header rather than a battery on the badge itself, though there is a pad for an edge-mounted CR2032 holder.

Joe designed the microbadge as the hub of a wider system of interchangeable SAO parts he built for DEF CON 26: several styles of plug-together "arms" (human, robot, tentacle, and bug variants), interchangeable "faces," and adapters for attaching NeoPixel strips, I2C breakout boards, and other add-ons. He also wrote two proof-of-concept firmware sketches that exploit gaps in the I2C protocol's bus-arbitration rules to smuggle out NeoPixel or UART signaling on the same data line. With help from Piotr (esden) and 1BitSquared, about 1100 units were assembled in time for the con, panelized as eleven 10x10 panels, and given away for free rather than sold.

## Make your own

The hardware — Eagle schematic, board file, and gerbers — is published in the [GitHub repo](https://github.com/securelyfitz/microbadge). No firmware repo or license file was found; the README documents the BOM (under $1 per unit excluding add-ons) and walks through assembling a full badge from a microbadge, a face, arms, and a battery holder, plus how to reprogram the ATtiny85 over USB with the Digispark/micronucleus toolchain.
