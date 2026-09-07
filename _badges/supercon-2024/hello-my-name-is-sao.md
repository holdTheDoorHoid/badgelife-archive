---
title: Hello My Name Is SAO
id: supercon-2024-hello-my-name-is-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: A deliberately minimal write-your-name-with-a-pen name-tag SAO with an optional set of four RGB LED faders, davedarko's first entry to the Supercon 2024 SAO contest, made in red, green and blue board variants.
functions: 'A blank name-tag surface to hand-write on; the LED version adds four onboard RGB LED faders (auto color-cycling) for a bit of blink without any programming, though only one is reliably wired per board without manual rework.'
look:
  colors: [red, green, blue, white]
  shape: rectangle
  themes: [minimalist, text]
tech:
  mcu: none
  leds:
    count: 4
    type: RGB
    note: 'LED version only ("blinkyparts style"); the plain version has no LEDs. Board carries four discrete legged RGB LED faders (D1-D4, per the KiCad schematic); the maker''s errata says only one of the four is correctly connected on shipped boards, the other three needing manual rework.'
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '~90 kits'
  availability: unknown
  distribution: [free_drop, contest]
  where: 'Bagged and tagged for distribution to attendees at Supercon 2024 as a Supercon 8 SAO contest entry.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/HelloMyNameIs
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  kind: repo
- label: hackaday.io/project/197693-hello-my-name-is-sao
  url: https://hackaday.io/project/197693-hello-my-name-is-sao
  kind: hackaday
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main/HelloMyNameIs
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/HelloMyNameIs
  kind: repo
images:
  - file: assets/images/badges/supercon-2024/hello-my-name-is-sao/a051b6437a.jpg
    source: "https://hackaday.io/project/197693-hello-my-name-is-sao"
    credit: "davedarko"
    caption: "Hello My Name Is SAO project cover photo, Supercon 2024"
  - file: assets/images/badges/supercon-2024/hello-my-name-is-sao/edce5635ad.jpg
    source: "https://hackaday.io/project/197693-hello-my-name-is-sao"
    credit: "davedarko"
    caption: "Assembled Hello My Name Is SAO boards"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  title: davedarko/Simple-Add-ons-SAO — Find all of my simple add-ons in this repository
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/197693-hello-my-name-is-sao
  title: "Hello My Name Is SAO — Hackaday.io"
  accessed: '2026-09-07'
  note: Maker's project log; confirms event (Supercon 8 SAO contest, 2024), ~90 kits made in red/green/blue, RGB LED with faders, cover photo.
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/HelloMyNameIs
  title: "Simple-Add-ons-SAO/HelloMyNameIs at main"
  accessed: '2026-09-07'
  note: Confirms two variants (plain and LED/"blinkyparts style") and KiCad design files. The folder's ReadMe.md errata says boards have four LEDs and only one is correctly connected per board (not per panel); the KiCad schematic confirms four discrete LED parts (D1-D4).
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check correction (2026-09-07): the researcher''s draft described a single onboard RGB LED. The KiCad schematic in the HelloMyNameIs/henlo_blinkyparts_style folder shows four discrete "Device:LED" parts (D1-D4), and the maker calls them "legged RGB LED faders" and says only one of the four is correctly wired per board ("All of them only have one of the LEDs correctly connected, for the other three you have to botch a bit") - not "one of four per panel" as previously written. tech.leds, functions, summary, and body text corrected accordingly. The maker quote in the body was also tightened to match the source''s wording more closely. Price and exact per-kit cost were not stated on either source. sao_version assumed v1 (4-pin) as no SAO version is specified by the maker; treat as unconfirmed. Firmware URL left null since the board is passive (no MCU in the schematic) and no firmware repo is referenced. sao_version blanked to null (previously guessed as v1) since neither source states the connector version. All other fields (quantity ~90 kits, red/green/blue variants, KiCad, event, hardware_url, images) were confirmed directly against the cited Hackaday.io page and GitHub folder/readme.'
last_modified_date: '2026-09-07'
---

Hello My Name Is SAO is davedarko's first entry into the Supercon 8 SAO add-on contest at Supercon 2024. It leans hard into simplicity: the base idea is just a blank name-tag surface meant to be written on by hand, built as a deliberate rejection of the increasingly complex badges seen at the con. As the maker put it on the project's Hackaday.io page, "I think that blinking an LED is already too much, and programming a badge is too much work while listening to amazing talks anyways."

A "blinkyparts style" variant adds four onboard RGB LED faders for a bit of visual interest without requiring any code — no microcontroller is involved. Around 90 kits were produced across red, green and blue PCB variants, bagged and tagged for handout to attendees at the event. The maker's own errata notes a wiring slip: on shipped boards, only one of the four LEDs was correctly connected, with the other three needing manual rework ("1 LED seems plenty strong already anyways," the readme adds).

## Make your own

KiCad hardware files for both the plain and LED versions are published in davedarko's Simple-Add-ons-SAO repository under the `HelloMyNameIs` folder. No firmware is needed since the board carries no microcontroller.
