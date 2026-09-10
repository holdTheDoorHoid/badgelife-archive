---
title: SAO faces (terminator, badgewife, smiley)
id: dc26-sao-faces-terminator-badgewife-smiley
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: Joe Fitz (securelyfitz)
  url: https://github.com/securelyfitz
summary: 'A set of interchangeable SAO "face" PCBs for securelyfitz''s microbadge system at DEF CON 26, each carrying its own SAO port and battery holder so it can be topped with a chosen expression and skewered with a set of "arms".'
functions: 'Each face plugs into the microbadge core (an ATtiny85 "digispark clone") over the SAO''s I2C pins and supplies the badge''s battery holder. The terminator face doubles as a joke: it "terminates" the I2C bus with pullup resistors. Faces carry no logic of their own; they are decorative/structural PCBs combined with separately-sourced arms and the microbadge board to make a complete wearable.'
look:
  colors:
  - black
  - white
  shape: null
  themes:
  - robot
  - sci-fi
  - movie
  - meme
  - pop culture
tech:
  mcu: none
  leds: null
  display: none
  connectivity:
  - i2c
  battery: CR2032
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/securelyfitz/sao-faces
  firmware_url: null
  eda_tool: EasyEDA
  fab_url: null
  license: null
  notes: Repo includes Eagle-style .sch/.brd files, Gerber/CAM sets, and zip archives per design (badgewife, bendor, hackers, roboto, terminator, wife variants); no BOM or assembly instructions beyond the parent microbadge README.
links:
- label: github.com/securelyfitz/sao-faces
  url: https://github.com/securelyfitz/sao-faces
  kind: repo
- label: github.com/securelyfitz/microbadge (parent system README)
  url: https://github.com/securelyfitz/microbadge
  kind: repo
images:
  - file: assets/images/badges/dc26/sao-faces-terminator-badgewife-smiley/981abd45f3.jpg
    source: "https://github.com/securelyfitz/sao-faces"
    credit: "securelyfitz"
    caption: "Terminator face SAO artwork (dc2018_terminator1.bmp)"
  - file: assets/images/badges/dc26/sao-faces-terminator-badgewife-smiley/9a161ac0de.jpg
    source: "https://github.com/securelyfitz/sao-faces"
    credit: "securelyfitz"
    caption: "Smiley face SAO artwork, filed in the repo as hackers.bmp"
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- 'Sweep title matches the maker''s own naming exactly: the microbadge README lists the three faces as "terminator to terminate your I2C signals with pullups", "badgewife for badgelife diehards", and "smiley for dade murphy fans."'
status: released
sources:
- kind: url
  url: https://github.com/securelyfitz/sao-faces
  title: SAO faces (terminator, badgewife, smiley)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://raw.githubusercontent.com/securelyfitz/microbadge/master/README.md
  title: microbadge README (parent system)
  accessed: '2026-09-10'
  note: Confirms DEF CON 26 (2018) context, ATtiny85/digispark core, CR2032 battery, I2C SAO connector, ~1100 microbadges assembled, and the three named faces (terminator, badgewife, smiley).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'The sao-faces repo itself has only a one-line README and no images beyond the design bitmaps; event/year, function, and the "smiley" identification come from the parent microbadge repo''s README rather than from sao-faces directly. The repo holds six design folders/zips (badgewife, bendor, hackers, roboto, terminator, wife) but the maker''s prose only names three faces (terminator, badgewife, smiley) — "hackers.bmp" appears to be the smiley design (an eyepatched smiley face, a nod to the 1995 film Hackers, whose protagonist is Dade Murphy) and "wife"/"bendor"/"roboto" are unlabeled extras not mentioned in prose; not confirmed which files pair to "bride" (dc2018_bride1.bmp) vs "badgewife" vs "wife". No price, quantity-per-face, or standalone availability info found; the ~1100 unit figure in sources is for the microbadge core board as a whole, not this faces set specifically. No storefront or press coverage located.'
last_modified_date: '2026-09-10'
---

Part of Joe Fitz's (securelyfitz) "microbadge" project for DEF CON 26 (2018), sao-faces is a small library of interchangeable face PCBs that snap onto the microbadge's SAO header along with a set of separately-designed "arms," letting attendees mix and match a body for the tiny ATtiny85-based badge. The maker's README names three faces by intent: a **terminator** face (whose name doubles as a joke — it terminates the I2C bus with pullup resistors), a **badgewife** face for "badgelife diehards," and a **smiley** face for fans of the 1995 film *Hackers* (whose lead character is Dade Murphy). Each face carries its own SAO port and a battery holder, since the trimmed-down microbadge core board has no on-board regulator or holder of its own.

The microbadge system as a whole — core board, arms, faces, and several adapter boards (sao-iic, sao-stripper, sao-flipper, sao-rotate, sao-45) — was designed to be "the smallest possible functional badge with a single SAO connector," built from a stripped-down Digispark (ATtiny85, micronucleus USB bootloader) for well under $1 in parts. Around 1,100 microbadge core boards were assembled in time for DEF CON 26 with help from Piotr Esden-Tempski and 1BitSquared; that figure covers the whole microbadge line rather than the faces specifically, and no separate price, per-face production count, or storefront listing for sao-faces was found.

## Make your own

The `sao-faces` GitHub repo is open source, with Eagle-style schematic/board files, Gerbers, and per-design zip archives for six face variants (badgewife, bendor, hackers, roboto, terminator, wife — more than the three named in the maker's prose). There is no BOM or step-by-step build guide in this repo; assembly instructions live in the parent `microbadge` repo's README, which describes soldering a long 4-pin header to the back of a face, adding a battery holder, skewering on a set of arms, and plugging the assembly into a microbadge core board.
