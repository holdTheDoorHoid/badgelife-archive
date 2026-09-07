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
- name: Hairline Moggers (H4irl1n3 M0gg3r5)
  url: https://www.h4irl1n3-m0gg3r5.com/
summary: 'A paired two-badge CTF for DEF CON 34 that cannot be bought: one player wears a skull-shaped "Zombie" (Patient Zero) badge that broadcasts infection over IR, another wears a "Survivor" badge that can only be bitten, and the outbreak-and-cure puzzle only resolves when the two badges are brought together.'
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
  colors:
  - white
  - black
  shape: skull (Zombie) / rectangle (Survivor)
  themes:
  - horror
  - skull
  - ctf
  - puzzle
  form_factor: pcb badge
tech:
  mcu: ESP32-S3
  leds:
    count: null
    type: NeoPixel
    note: Zombie badge has two NeoPixel eyes; Survivor has a NeoPixel ring (sheet says 8-LED biohazard underglow ring).
  display: OLED
  connectivity:
  - nfc
  - ir
  - ble
  - usb
  inputs:
  - buttons
  - capacitive
  power: USB-C
  battery: null
  sao_version: null
get_one:
  price: free
  price_usd: 0.0
  quantity: ''
  availability: free
  availability_note: 'Maker site checked 2026-09-07: "You can''t buy these. Badges drop throughout the conference."'
  distribution:
  - free_drop
  where: Not sold. Per the maker, badges are dropped throughout DEF CON 34 by the H4irl1n3 M0gg3r5 crew roaming the floor; the sheet says you have to perform actions or find certain people to get one.
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
images:
- file: assets/images/badges/dc34/it-s-2-badges-a-zombie-and-a-survivor-badge/9843798c74.jpg
  source: https://www.h4irl1n3-m0gg3r5.com/
  credit: H4irl1n3 M0gg3r5
  caption: Zombie (Patient Zero) badge, from the maker's site
- file: assets/images/badges/dc34/it-s-2-badges-a-zombie-and-a-survivor-badge/6a1bba6f0b.jpg
  source: https://www.h4irl1n3-m0gg3r5.com/
  credit: H4irl1n3 M0gg3r5
  caption: Survivor badge, from the maker's site
contact:
  discord: batman_14j
  emails:
  - tshipway@gmail.com
notes: []
status: announced
sources:
- kind: sheet
  event: dc34
  row: 11
  updated: 5/27/2026 17:26:33
  listing: New
- kind: url
  url: https://www.h4irl1n3-m0gg3r5.com/
  title: H4IRL1N3 M0GG3R5 // DC34 BADGE DROP
  accessed: '2026-09-07'
  note: Maker's site; confirms the DC34 two-badge drop, Brain in a Jar SAO, and the badge photos used here.
- kind: url
  url: https://www.h4irl1n3-m0gg3r5.com/content.js
  title: Site copy for h4irl1n3-m0gg3r5.com
  accessed: '2026-09-07'
  note: 'Spec strings: Zombie badge MCU ESP32-S3, skull-shaped PCB, IR/NFC/BLE; Survivor NeoPixel ring, IR receiver, NFC, buzzer; "You can''t buy these. Badges drop throughout the conference."; CTF backend not live yet.'
- kind: url
  url: https://x.com/zeroo_patient
  title: Zero Patient (@Zeroo_patient) / X
  accessed: '2026-09-07'
  note: Account exists and is linked from the maker's site as the drop channel; posts could not be read (login wall).
research:
  status: researched
  confidence: low
  last_checked: '2026-09-06'
  notes: 'Fact-check 2026-09-07: the earlier claim of "no web presence" was wrong; the maker''s site linked in the entry is live and confirms the project. Site specs (ESP32-S3, skull PCB, IR/NFC/BLE, NeoPixel ring, buzzer) and the maker''s photos were used for tech/look fields. Discrepancies between the sheet description and the maker''s site/photos: the sheet says the Survivor has an e-ink "quarantine dossier", but the site lists its display as a NeoPixel ring and the photo shows a small OLED module on both badges, so display is recorded as OLED; the sheet calls the badges Patient Zero/Survivor, the site calls them Zombie/Survivor. The functions field is left as the maker''s sheet text. Not found: LED counts, quantity, open-source status, whether badges actually dropped at DC34 (site vault still said CTF backend not live when checked); X posts unreadable without login. The Brain in a Jar SAO has its own entry (dc34-h4irl1n3-m0gg3r5-brain-in-a-jar-sao).'
last_modified_date: '2026-09-06'
---

Hairline Moggers (styled H4irl1n3 M0gg3r5) built a two-badge paired CTF for DEF CON 34, which the maker's site says grew out of an idea hatched in the Circus Circus food court during DC33. The skull-shaped Zombie badge (called "Patient Zero" on the community sheet) runs an ESP32-S3 and carries NeoPixel eyes, a small OLED, a piezo buzzer, an IR transmitter and NFC/BLE radios; per the sheet it has capacitive touch zones that arm it and it fires HMAC-signed "infection" packets over 38 kHz IR. The rectangular "Zombie Removal Unit" Survivor badge has a NeoPixel ring, an IR receiver only, an NFC tag whose destination shifts as you progress, and a buzzer that warns when a zombie is close.

Per the maker, the two badges interact in stages: the Zombie arms itself, the badges tap NFC antennas to register the infection, the Zombie beams a signed IR payload that any Survivor in line of sight can pick up, and an infected Survivor changes its LEDs, its NFC tag and its BLE advertising name from SURVIVOR-xxxx to INFECTED-xxxx. Getting infected reveals half of an antidote grid; only two badges side by side can reconstruct the cure. The site describes the whole con floor as the game board, with the crew roaming as live infection zones, unmapped cure stations, 3D-printed medkit props and identical-looking trap medkits. A companion "Brain in a Jar" SAO, meant for the official DEF CON badge, uses the same IR protocol and has its own entry in this archive.

The badges are not for sale: the maker says they drop throughout the conference and to watch r/Defcon and the @Zeroo_patient X account. Quantity, LED counts and open-source status were not published, and when checked the site's CTF vault page still said the backend was not live.
