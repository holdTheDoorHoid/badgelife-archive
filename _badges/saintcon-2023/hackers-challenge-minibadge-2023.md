---
title: Hackers Challenge Minibadge (2023)
id: saintcon-2023-hackers-challenge-minibadge-2023
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: Santiago
summary: 'A SAINTCON contest minibadge for the Hackers Challenge game, a purple PCB badge depicting a hooded pixel-art character over the "HACKERS CHALLENGE" logotype.'
functions: 'Handed out by Hackers Challenge Game Masters (sometimes after solving a puzzle). A back-side solder jumper picks whether its two LEDs run SOLID or BLINK; no other interactivity.'
look:
  colors: [purple, white, yellow]
  shape: null
  themes: [ctf, security, pixel art, mascot]
tech:
  mcu: none
  leds:
    count: 2
    type: reverse-mount
    note: 'D1/D2 (NCD0805R1); a back-side jumper selects SOLID vs BLINK (clock) mode - never bridge both.'
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: unknown
  distribution: [contest]
  where: 'Obtained by interacting with a Hackers Challenge Game Master at SAINTCON 2023; they may require solving a puzzle first.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  kind: website
- label: Hackers Challenge (saintcon.org)
  url: https://www.saintcon.org/hackers-challenge/
  kind: website
images:
  - file: assets/images/badges/saintcon-2023/hackers-challenge-minibadge-2023/front.jpg
    source: "https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf"
    credit: "Santiago / SAINTCON 2023 Minibadge Guide"
    caption: "Front of the 2023 Hackers Challenge minibadge, hooded-figure pixel art"
  - file: assets/images/badges/saintcon-2023/hackers-challenge-minibadge-2023/back.jpg
    source: "https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf"
    credit: "Santiago / SAINTCON 2023 Minibadge Guide"
    caption: "Back of the badge showing the SOLID/BLINK jumper, two LEDs, and U1 EEPROM"
contact: {}
notes:
- 2023 Contest minibadge for the Hackers Challenge game, designed by Santiago with inspiration from Rigel and Zevlag; distinct from the archive's existing 2022 Zevlag-designed Hackers Challenge badge and the 2017 official minibadge. Found by the event-year sweep, task saintcon-2023.
status: released
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  title: Hackers Challenge Minibadge (2023)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2023); event read as ''saintcon-2023''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  title: 2023 SAINTCON Minibadge Guide, page 53 (Hackers Challenge Contest Minibadge)
  accessed: '2026-09-10'
  note: 'Confirmed the item and its full detail card: maker, description, difficulty/rarity, assembly instructions, parts list (D1/D2 NCD0805R1, R1/R2 0805W8F680JT5E, U1 ZD24C32A-SSGMB), and front/back photos.'
- kind: url
  url: https://www.saintcon.org/hackers-challenge/
  title: Hackers Challenge - SAINTCON
  accessed: '2026-09-10'
  note: "Background on the Hackers Challenge CTF itself (SAINTCON's signature Jeopardy-style contest, run by Santiago and Legoclones); confirms the maker's full name is Santiago Ocano per a related SAINTCON 2025 recap video, though the minibadge guide itself only credits 'Santiago'."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: "The official 2023 SAINTCON Minibadge Guide (page 53) fully confirms this item: a mostly-assembled purple PCB minibadge, front side a pixel-art hooded figure over the 'HACKERS CHALLENGE' wordmark, back side two reverse-mount LEDs (D1/D2) and a ZD24C32A-SSGMB EEPROM (U1), with a solder jumper choosing SOLID or BLINK LED behavior. Rated difficulty 'beginner' and rarity 'common'. Distributed free by Hackers Challenge Game Masters during the con, sometimes gated behind solving a puzzle. No maker storefront, repo, or open-source files were found, so make_your_own and get_one.quantity stay empty. Left tech.sao_version as 'none' since the badge's three 2-position headers are plain minibadge mounting pins, not an SAO connector."
last_modified_date: '2026-09-10'
---

The 2023 Hackers Challenge Minibadge was designed by Santiago as the contest minibadge for SAINTCON's Hackers Challenge, the conference's signature Jeopardy-style capture-the-flag. Santiago credits Rigel and Zevlag's earlier Hackers Challenge badges as inspiration; this minibadge is a distinct, smaller companion piece rather than a replacement for the full badge line SAINTCON has run for the game since at least 2017.

The board is a purple PCB shaped like a hooded, pixel-art character with "HACKERS CHALLENGE" printed beneath it in a blocky retro font. It ships mostly assembled: builders solder a jumper on the back to choose between the two on-board LEDs (D1/D2) running solid or blinking, plus three 2-position headers in the corners for mounting. The back also carries a small EEPROM (U1, marked ZD24C32A-SSGMB) alongside the LEDs and their current-limiting resistors.

SAINTCON rated it "beginner" difficulty and "common" rarity, and it was given away free by Hackers Challenge Game Masters on the show floor, sometimes after a player solved at least one puzzle. No storefront, repository, or open hardware/firmware files were found for it.
