---
title: Veilid SAO
id: dc32-veillid-sao
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
makers:
- name: C0ldbru (Rot13 labs)
summary: A single-key USB-C macropad SAO from rot13labs that opens a terminal and launches the Veilid privacy network's website, with a random keycap and switch and neopixel backlighting.
functions: 'Designed to help us take back control. Even has a nice, resounding click to it. By default the single key triggers a macro that opens a terminal and uses it to open the user''s default browser to Veilid''s website; fully QMK compatible, so the macro/key can be reprogrammed with the QMK Toolbox.'
look:
  colors: []
  shape: null
  themes:
  - privacy
  - security
  - hardware tool
tech:
  mcu: null
  leds:
    count: 1
    type: neopixel
    note: single neopixel for backlighting
  display: null
  connectivity:
  - usb
  battery: null
  sao_version: null
  inputs:
  - buttons
get_one:
  price: $35.00
  price_usd: 35.0
  quantity: ''
  availability: unknown
  availability_note: 'Sold via the maker''s goimagine.com storefront; that listing (and the goimagine.com platform itself) is gone as of 2026-09-06, so current availability could not be checked. Last confirmed live via Wayback Machine capture dated 2024-06-20.'
  distribution:
  - purchase
  where: 'Sold on goimagine.com (a handmade-goods marketplace) direct from the maker''s shop, "rot13labs," based in Gainesville, FL. Listed with free shipping; SAOs shipped every other day via USPS ground.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: Described as "fully QMK compatible" (implying QMK firmware), but no repo, Gerbers, or BOM were found.
links:
- label: t.co/QBz8afPb4W
  url: https://t.co/QBz8afPb4W
  kind: website
- label: x.com/c0ldbru
  url: https://x.com/c0ldbru
  kind: social
- label: goimagine.com/veilid-sao (archived)
  url: http://web.archive.org/web/20240620131205/https://goimagine.com/veilid-sao/
  kind: store
images:
  - file: assets/images/badges/dc32/veillid-sao/827d1b0d8f.jpg
    source: "https://goimagine.com/veilid-sao/"
    credit: "rot13labs"
    caption: "Veilid SAO product photo"
contact: {}
notes:
- 'Sheet spelled the title "Veillid SAO" (double-L); the maker''s own listing spells it "Veilid SAO," matching the Veilid project''s actual name. Kept the entry id/filename as dc32-veillid-sao but corrected the title.'
status: released
sources:
- kind: sheet
  event: dc32
  row: 32
  updated: '2024-06-06'
- kind: url
  url: http://web.archive.org/web/20240620131205/https://goimagine.com/veilid-sao/
  title: 'Veilid SAO - goimagine.com (Wayback Machine capture, 2024-06-20)'
  accessed: '2026-09-06'
  note: 'Primary source: maker''s own product listing. Confirmed maker name "rot13labs" (matches C0ldbru), price $35, single-key QMK-compatible USB-C macropad with neopixel backlighting, random keycap/switch, free shipping, and that a portion of profits go to the Veilid project. The live goimagine.com URL now 404s and t.co/QBz8afPb4W redirects to it, so this Wayback capture was used instead.'
- kind: url
  url: https://t.co/QBz8afPb4W
  title: t.co redirect target (goimagine.com/veilid-sao, now 404)
  accessed: '2026-09-06'
  note: Confirmed the shortlink still resolves to the (now-dead) goimagine.com product page; could not reach live content.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'Core facts (maker, description, price, mechanism) come from the maker''s own archived storefront listing, but the live listing and the whole goimagine.com marketplace are gone, so current availability, quantity made, MCU, and open-source status could not be confirmed. The x.com/c0ldbru profile returned HTTP 402 (paywalled) and could not be checked; no Hackaday.io, GitHub, or press coverage was found for this specific item. Left mcu, quantity, and make_your_own fields empty/null rather than guess.'
last_modified_date: '2026-09-06'
---

The Veilid SAO is a single-key USB-C macropad add-on sold by rot13labs (maker C0ldbru) around DEF CON 32, built to promote the Veilid decentralized privacy network. Out of the box, pressing its one key runs a macro that opens a terminal and uses it to launch the user's default browser to Veilid's website — a small, self-aware joke about "resounding clicks" and "taking back control." Because it's fully QMK compatible, the key (or macro) can be freely reprogrammed with the QMK Toolbox to do anything else.

Each unit shipped with a single neopixel for backlighting and a random keycap color and mechanical switch type, drawn from whatever stock the maker had on hand; buyers could request (not guarantee) a preference. It sold for $35 with free shipping direct from rot13labs' shop on the handmade-goods marketplace goimagine.com, with a portion of the proceeds donated to the Veilid project. rot13labs, based in Gainesville, FL, has made badges since 2020 and is also known for the Hackbutt and BSides Tampa badges.

The original goimagine.com listing and the marketplace itself are no longer live; details here come from a Wayback Machine capture from June 2024. The maker's chip choice, total quantity made, and whether hardware/firmware files were ever published could not be confirmed from available sources.
