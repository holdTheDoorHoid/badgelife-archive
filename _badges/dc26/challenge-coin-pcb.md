---
title: DC26 Monero Badge Challenge coin PCB
id: dc26-challenge-coin-pcb
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: other
event: dc26
year: 2018
makers:
- name: dodgymike
  url: https://github.com/dodgymike
  role: PCB design/fabrication
- name: elasticninja
  role: Monero Badge Challenge creator
- name: tonym128
  role: Monero Badge Challenge creator
- name: fluffypony
  role: Monero Badge Challenge creator
summary: A free PCB "challenge coin" handed out at DEF CON 26's BCOS/Monero village as the entry token for the Monero Badge Challenge, a cipher puzzle that unlocked the real Monero Badge.
functions: 'Carries an encoded (ciphertext) message printed/etched on both the front and back. Solvers decoded the message, used the same key to encode their own reply string, and tweeted it at the badge creators to get directions to redeem a full DEF CON 26 Monero Badge.'
look:
  colors: []
  shape: circle
  themes:
  - crypto
  - privacy
  - puzzle
  - coin
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Handed out at the BCOS/Monero village (Pompeii room, Caesars Palace) and at DEF CON info booths during DEF CON 26; also available directly from the Monero Badge creators.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/dodgymike/dc26-monero-badge-pcb/tree/master/dc26-challenge
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/dodgymike/dc26-monero-badge-pcb/tree/master/dc26-challenge
  url: https://github.com/dodgymike/dc26-monero-badge-pcb/tree/master/dc26-challenge
  kind: repo
- label: dc26-monero-badge-pcb (parent repo)
  url: https://github.com/dodgymike/dc26-monero-badge-pcb
  kind: repo
- label: monerobadge.org (DEF CON 26 Monero Badge Challenge)
  url: https://web.archive.org/web/20220122002926/http://monerobadge.org/
  kind: website
images:
- file: assets/images/badges/dc26/challenge-coin-pcb/46146857f1.jpg
  source: "https://monerobadge.org"
  credit: "Monero Badge Challenge / dodgymike"
  caption: "Front of the DC26 Monero Badge Challenge coin PCB, showing the encoded message"
- file: assets/images/badges/dc26/challenge-coin-pcb/5a6d89c813.jpg
  source: "https://monerobadge.org"
  credit: "Monero Badge Challenge / dodgymike"
  caption: "Back of the DC26 Monero Badge Challenge coin PCB, showing the encoded message"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://github.com/dodgymike/dc26-monero-badge-pcb/tree/master/dc26-challenge
  title: dc26-challenge coin PCB
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''dc26''.'
- kind: url
  url: https://github.com/dodgymike/dc26-monero-badge-pcb
  title: dodgymike/dc26-monero-badge-pcb - Defcon 26 Monero badge PCB
  accessed: '2026-09-07'
  note: Parent repo README confirms the dc26-challenge folder holds the "DC26 challenge coin PCB project"; links to the separate firmware repo for the full Monero badge (not this coin).
- kind: url
  url: https://web.archive.org/web/20220122002926/http://monerobadge.org/
  title: The Monero Badge Challenge || DEF CON 26 (Wayback Machine capture)
  accessed: '2026-09-07'
  note: Live site returned a server error; used the archived copy. Describes the challenge coin/token, the cipher puzzle, how tokens were distributed, and names the creators (elasticninja, tonym128, fluffypony). Supplied the two token photos used here.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    The KiCad files for this coin (dc26-challenge.kicad_pcb) show 192 modules but zero nets
    and zero tracks, confirming it is a passive/decorative PCB with no MCU, LEDs, or active
    circuitry - the copper/silkscreen forms the coin's face art and the encoded message, not
    a functional circuit. This is distinct from the main DC26 Monero Badge (an actual
    electronic badge with its own firmware repo, USB, battery, and RGB LED schematics) that
    lives in the same parent repository; this entry covers only the free challenge-coin
    token, not the electronic badge it unlocks. Exact quantity made is not stated in any
    source found. dodgymike is credited via the repo as the PCB designer/fabricator; the
    Monero Badge Challenge itself (the puzzle and distribution) was run by elasticninja,
    tonym128, and fluffypony per monerobadge.org.
last_modified_date: '2026-09-07'
---

The DC26 Monero Badge Challenge coin is a free PCB token given out at DEF CON 26 (2018) as the entry point to the unofficial Monero Badge Challenge. Unlike the electronic Monero Badge it led to, the coin itself is a passive PCB: its KiCad source shows a couple hundred silkscreen/copper-art elements but no components, nets, or traces, so there is no chip or LEDs to speak of, just a coin-shaped board bearing an encoded message on both faces.

To claim a real Monero Badge, DEF CON 26 attendees first had to pick up one of these tokens from the badge creators (@elasticninja, @tonym128, @fluffypony), the BCOS/Monero village at Caesars Palace, or a DEF CON info booth. The token carried the same ciphertext on every copy; solvers decoded the message, re-encoded a message of their own with the same key, and tweeted it at the creators to receive a rendezvous location where they could trade the coin for the finished badge.

The KiCad project for the coin lives in the `dc26-challenge` subfolder of dodgymike's `dc26-monero-badge-pcb` repository, alongside the separate schematics for the full electronic Monero Badge (USB, battery, RGB LEDs, an accelerometer) - that badge is a different, more complex artifact from the same project and is not what this entry describes.

## Make your own

KiCad source (schematic and PCB layout) and Gerbers for the coin are in the `dc26-challenge` folder of the linked repository. No firmware is involved since the coin has no active electronics.
