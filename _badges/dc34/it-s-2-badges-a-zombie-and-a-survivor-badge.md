---
title: It's 2 badges.   A Zombie and a Survivor badge
id: dc34-it-s-2-badges-a-zombie-and-a-survivor-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Hairline Moggers  (H4irl1n3 M0gg3r5)
summary: ''
functions: |-
  Two badges, one outbreak. The system is a paired CTF: one player wears Patient Zero, another wears a Survivor, and the challenge only resolves when they're in the same room.

  Patient Zero — animated NeoPixel eyes, OLED facial expressions and zombie-groan piezo, three capacitive touch zones (TEMPLE / SPINE / CORTEX) that wake the infection with a neural-activation sequence, NFC bite-tag, and a 38kHz IR transmitter that fires HMAC-signed "infection" packets.

  Survivor — e-ink quarantine dossier, 8-LED biohazard underglow ring, NFC defense tag, and IR receive-only (it can be bitten, never bite back).

  How the badges interact:
  1. Neural Activation — Patient Zero arms itself locally via the touch ritual.
  2. Bite Pairing — Patient Zero and Survivor must physically tap NFC antennas for 2 seconds (≤5cm) to register the infection vector.
  3. Infection Broadcast — Patient Zero beams a signed IR payload; any Survivor in line-of-sight picks it up, validates the HMAC, and turns.
  4. The Infection Moment — when the Survivor accepts a valid packet:
      * the underglow ring shifts from green biohazard pulse to a slow red arterial throb,
      * the e-ink dossier redraws — the survivor's name is overstruck, the photo is replaced with a "SPECIMEN" header, and the badge's NFC tag rewrites to expose the infection signature so other survivors who scan it learn they've been exposed,
      * BLE advertising changes from SURVIVOR-xxxx to INFECTED-xxxx, so anyone with a phone scanner sees the outbreak spread across the conference floor in real time,
      * and — critically — the badge now reveals its half of the antidote grid. Infection is the prerequisite for solving the puzzle, not the failure state.
  5. The Antidote — the encrypted flag is split across the two badges'. Neither badge can read the cure alone — you have to physically stand the two badges side-by-side to reconstruct the flag to cure yourself.

  Companion SAO (for the official badge) — Brain in a Jar — a glowing brain that screams "BRAINS!" over IR on capacitive touch, using the same 38kHz protocol as Patient Zero so it can infect nearby Survivors without their host badge's permission.

  No portal guns this year, but the Plumbus mount-point is reserved on Rev C.
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $0 - will have to perform actions or find certain people to get a badge
  price_usd: 0.0
  quantity: ''
  availability: unknown
  distribution: []
  where: $0 - will have to perform actions or find certain people to get a badge
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links: []
images: []
contact:
  discord: batman_14j
  emails:
  - tshipway@gmail.com
notes: []
status: listed
sources:
- kind: sheet
  event: dc34
  row: 11
  updated: 5/27/2026 17:26:33
  listing: New
research:
  status: stub
  confidence: low
  last_checked: '2026-09-06'
  notes: Imported from the community badge sheet; not yet researched.
last_modified_date: '2026-09-06'
---

