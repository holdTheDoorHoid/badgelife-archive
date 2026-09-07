---
title: RFID/NFC BADGE
id: saintcon-2021-rfid-nfc-badge
layout: badge
parent: Saintcon 2021
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2021
year: 2021
makers:
- name: Jup1t3r
summary: A SAINTCON 2021 minibadge built around an NFC tag sticker, part of a large set of minibadges Jup1t3r designed for that year's conference.
functions: Carries an NFC tag sticker on its face; two LEDs light up as an indicator/decoration.
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: none
  leds:
    count: 2
    type: null
    note: 'D1 and D2; oriented with the green dot toward the top of the board'
  display: null
  connectivity:
  - nfc
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=RFID/NFC%20BADGE&year=2021
  url: https://minibadge.wiki/?search=RFID/NFC%20BADGE&year=2021
  kind: website
- label: minibadge.wiki 2021 data export (JSON)
  url: https://minibadge.wiki/2021.json
  kind: doc
images:
  - file: assets/images/badges/saintcon-2021/rfid-nfc-badge/a3bec66f78.jpg
    source: "https://minibadge.wiki/data/"
    credit: "Jup1t3r"
    caption: "Front of the RFID/NFC minibadge"
  - file: assets/images/badges/saintcon-2021/rfid-nfc-badge/f5eabaac38.jpg
    source: "https://minibadge.wiki/data/"
    credit: "Jup1t3r"
    caption: "Back of the RFID/NFC minibadge"
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://minibadge.wiki/?search=RFID/NFC%20BADGE&year=2021
  title: RFID/NFC BADGE
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2021''.'
- kind: url
  url: https://minibadge.wiki/2021.json
  title: MiniBadge Wiki 2021 data export
  accessed: '2026-09-07'
  note: 'Raw JSON record for this badge: author Jup1t3r, soldering instructions (two LEDs D1/D2, single resistor, headers trimmed flush, NFC sticker centered on top), soldering difficulty Intermediate. quantityMade, category, and howToAcquire fields were present but empty in the export.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The live search page at minibadge.wiki renders client-side and returned no visible data on fetch; the underlying 2021.json data export (linked from minibadge.wiki/data/) carries the actual record and was used instead. It gives build/soldering instructions and front/back images but no maker bio, price, quantity made, or acquisition method, and no separate maker page or repo was found. Jup1t3r designed a large slate of SAINTCON 2021 minibadges (e.g. Private LTE, Red Team, Hacker Challenge) alongside this one.'
last_modified_date: '2026-09-07'
---

The RFID/NFC BADGE is one of a set of SAINTCON 2021 minibadges designed by Jup1t3r, a prolific minibadge author for that year's conference. Rather than an active RFID/NFC reader, the badge is built to carry an NFC tag sticker on its face — the assembly notes call for centering a provided NFC sticker on top of the board, with the header pins trimmed flush so they don't interfere with it.

Assembly is rated intermediate: it uses two LEDs (D1 and D2, oriented with the green dot toward the top) and a single non-polarized resistor, along with the header/sticker step described above. No pricing, quantity made, or distribution details were published in the available records, and no dedicated maker page or repository for the badge was found beyond the minibadge.wiki community database entry.

## Make your own

No hardware files, gerbers, or firmware were found; only the soldering guide from minibadge.wiki (LEDs D1/D2 oriented green-dot-up, single resistor, headers trimmed flush, NFC sticker centered on top) is documented.
