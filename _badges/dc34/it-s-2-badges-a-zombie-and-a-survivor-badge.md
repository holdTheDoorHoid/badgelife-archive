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
summary: 'A paired two-badge CTF for DEF CON 34: one player wears "Patient Zero," another a "Survivor," and the outbreak-and-cure puzzle only resolves when the two badges are brought together.'
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
  themes:
  - horror
  - ctf
  - puzzle
  - security
tech:
  mcu: null
  leds:
    count: null
    type: NeoPixel
    note: Patient Zero has animated NeoPixel eyes; Survivor has an 8-LED biohazard underglow ring.
  display: e-ink (Survivor) / OLED (Patient Zero)
  connectivity:
  - nfc
  - ir
  - ble
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
links:
- label: www.h4irl1n3-m0gg3r5.com
  url: https://www.h4irl1n3-m0gg3r5.com/
  kind: website
- label: www.h4irl1n3-m0gg3r5.com/content.js
  url: https://www.h4irl1n3-m0gg3r5.com/content.js
  kind: website
- label: x.com/zeroo_patient
  url: https://x.com/zeroo_patient
  kind: social
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
  status: researched
  confidence: low
  last_checked: '2026-09-06'
  notes: 'No external web presence found for the maker "Hairline Moggers" (also styled H4irl1n3 M0gg3r5) or for this badge: web search, DuckDuckGo, and GitHub searches for the maker name returned nothing relevant, and Hackaday.io has no matching project. No storefront, repo, or press coverage was located. All descriptive detail in this entry (functions, look, tech) comes from the maker''s own text on the community badge sheet, which is the only available source; it could not be independently corroborated. Fields with no supporting detail on the sheet (colors, shape, mcu, quantity, price_usd, open-source status, images) are left empty rather than guessed. DEF CON 34 is an upcoming 2026 event, so this may be a not-yet-built or in-progress project rather than one that has already shipped.'
last_modified_date: '2026-09-06'
---

Hairline Moggers (styled H4irl1n3 M0gg3r5) listed a two-badge paired CTF for DEF CON 34 on the community badge sheet: a "Patient Zero" badge and a "Survivor" badge that only resolve their puzzle when brought together. Patient Zero carries animated NeoPixel eyes, an OLED for facial expressions, a piezo zombie groan, three capacitive touch zones, an NFC "bite" tag, and a 38 kHz IR transmitter that sends HMAC-signed "infection" packets. Survivor carries an e-ink "quarantine dossier," an 8-LED biohazard underglow ring, an NFC defense tag, and an IR receiver only.

Per the maker's description, the two badges interact in stages: Patient Zero arms itself through a touch ritual, the two badges tap NFC antennas to register the infection vector, Patient Zero beams a signed IR payload that any Survivor in range can pick up, and an infected Survivor's underglow shifts from green to red, its e-ink dossier redraws to a "SPECIMEN" card, its NFC tag rewrites to expose the infection to other scanners, and its BLE advertising name flips from SURVIVOR-xxxx to INFECTED-xxxx. Getting infected reveals half of an antidote grid; standing an infected Survivor next to a Patient Zero badge lets the pair reconstruct the cure. A companion SAO called "Brain in a Jar," meant for the official DEF CON badge, uses the same IR protocol to spread the infection independently.

None of this could be verified beyond the sheet listing itself — no storefront, repository, Hackaday.io project, or press mention of the maker or the badge could be found, so distribution, price, quantity, and hardware details (MCU, exact LED counts, colors, open-source status) are left blank rather than guessed.

