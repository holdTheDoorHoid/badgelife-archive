---
title: Aerospace Village Badge 2021
id: dc29-aerospace-village-badge-2021
layout: badge
parent: DC29
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc29
year: 2021
makers:
- name: Aerospace Village
  url: https://www.aerospacevillage.org
- name: Dan Allen
  role: designer
summary: A DEF CON 29 village badge shaped around a pilot's-eye view of an airfield, with lighting that responds according to real FAA airport signal standards and a set of hidden aerospace-security puzzles.
functions: 'LEDs react to input the way real airport traffic-control light signals and pilot signaling standards do (referencing FAA AIM sections 2-1-9, 4-3-13 and 7-7-4); the badge holds hardware-hacking challenges and puzzles whose solution and source code were kept secret until after the con.'
look:
  colors: []
  shape: rectangle
  themes:
  - space
  - security
  - puzzle
  - village badge
tech:
  mcu: ATmega8-16AU
  leds:
    count: 9
    type: discrete
    note: 'Two RGB LEDs plus two each of blue, white and green, three yellow, and one red, per Hackster.io coverage.'
  display: none
  connectivity: []
  battery: 3x AAA
  sao_version: none
get_one:
  price: $35 kit / $40 assembled
  price_usd: 35
  quantity: ''
  availability: sold_out
  availability_note: 'Tindie listings for both the DIY kit and fully-assembled versions show the seller "taking a break" as of 2026-09-07; treated as sold out/unavailable.'
  distribution:
  - purchase
  - kit
  where: Sold by The Aerospace Village on Tindie as a DIY kit ($35, surface-mount soldering required) or fully assembled ($40).
make_your_own:
  open_source: yes
  hardware_url: https://github.com/AerospaceVillage/avBadge_2021
  firmware_url: https://github.com/AerospaceVillage/avBadge_2021
  eda_tool: KiCad
links:
- label: github.com/AerospaceVillage/avBadge_2021
  url: https://github.com/AerospaceVillage/avBadge_2021
  kind: repo
- label: DC29 Badge | Aerospace Village
  url: https://www.aerospacevillage.org/dc29-badge
  kind: website
- label: 2021 Aerospace Village Badge (DIY Kit) — Tindie
  url: https://www.tindie.com/products/aero_village/2021-aerospace-village-badge-diy-kit/
  kind: store
- label: 2021 Aerospace Village Badge (Fully Assembled) — Tindie
  url: https://www.tindie.com/products/aero_village/2021-aerospace-village-badge-fully-assembled/
  kind: store
images:
  - file: assets/images/badges/dc29/aerospace-village-badge-2021/ecf4908a25.jpg
    source: "https://www.aerospacevillage.org/dc29-badge"
    credit: "Aerospace Village"
    caption: "DC29 Aerospace Village badge featuring pilot cockpit and runway artwork"
  - file: assets/images/badges/dc29/aerospace-village-badge-2021/4b309d25d1.jpg
    source: "https://www.aerospacevillage.org/dc29-badge"
    credit: "Aerospace Village"
    caption: "DC29 badge circuit board with batteries and Aerospace Village lanyard"
contact:
  email: village@aerospacevillage.org
notes: []
status: released
sources:
- kind: url
  url: https://github.com/AerospaceVillage/avBadge_2021
  title: Aerospace Village Badge 2021
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: villages-early: DEF CON village and DC-group badges, DEF CON 24-29 (2016-2021)); event read as ''DEF CON 29 (2021)''.'
- kind: url
  url: https://github.com/AerospaceVillage/avBadge_2021/blob/master/README.md
  title: 'avBadge_2021 README'
  accessed: '2026-09-07'
  note: 'Confirms ATmega88 programming path, KiCad hardware, Arduino firmware, assembly instructions, and the badge.gif image.'
- kind: url
  url: https://www.aerospacevillage.org/dc29-badge
  title: 'DC29 Badge | Aerospace Village'
  accessed: '2026-09-07'
  note: 'Maker''s own page: describes the pilot-cockpit/airfield artwork, FAA AIM 2-1-9/4-3-13/7-7-4 based light-signal interactions, art by flysurreal.com, contact email, and source images used for this entry.'
- kind: url
  url: https://www.hackster.io/news/the-aerospace-village-unveils-its-def-con-29-badge-but-keeps-the-source-code-a-secret-770e5a0b5132
  title: 'The Aerospace Village Unveils Its DEF CON 29 Badge — But Keeps the Source Code a Secret'
  accessed: '2026-09-07'
  note: 'Press coverage confirming ATmega8-16AU MCU, LED breakdown (2 RGB, 2 blue, 2 white, 2 green, 3 yellow, 1 red), 3x AAA battery power, designer Dan Allen (US Navy test pilot/software engineer), and $35 kit / $40 assembled pricing via Tindie.'
- kind: url
  url: https://www.tindie.com/products/aero_village/2021-aerospace-village-badge-diy-kit/
  title: '2021 Aerospace Village Badge (DIY kit) — Tindie'
  accessed: '2026-09-07'
  note: 'Confirms $35 kit price and that the listing is currently unavailable ("this seller is taking a break"); describes it as a soldering-learning kit with hidden interactive secrets, source released post-con.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Quantity made was not stated by any source and is left empty. LED type is listed as discrete per Hackster''s component breakdown; the maker''s own page did not itemize LEDs. Event was already correctly set to dc29 (DEF CON 29, 2021) in the stub.'
last_modified_date: '2026-09-07'
---

The 2021 Aerospace Village badge for DEF CON 29 was designed by Dan Allen, a US Navy test pilot and software engineer, with artwork by flysurreal.com giving the badge a pilot's-eye view of an airfield. Rather than being purely decorative, its lighting responds according to real FAA aeronautical standards: sections of the Aeronautical Information Manual covering airport traffic control light signals (AIM 4-3-13) and pilot light-gun responses (AIM 2-1-9) drive how the badge reacts, alongside a nod to AIM 7-7-4. Built around an ATmega8-16AU microcontroller with a mix of RGB, blue, white, green, yellow and red LEDs, and powered by three AAA batteries, the badge hid hardware-hacking challenges and puzzles whose details and source code the Village deliberately kept secret until after the conference.

The Aerospace Village sold the badge on Tindie in two forms: a $35 DIY kit requiring surface-mount soldering experience, marketed in part as a way for newcomers to learn soldering, and a $40 fully-assembled version. Both listings show the seller currently "taking a break," so the badge is not presently available for purchase. Hardware design files (KiCad) and Arduino-based firmware are published in the `AerospaceVillage/avBadge_2021` GitHub repository, along with PDF assembly instructions and a 3D-printable mounting attachment.

## Make your own

The hardware is designed in KiCad and the firmware is an Arduino sketch targeting the ATmega88/ATmega8 via the MiniCore boards package (board: ATmega8, no bootloader — the chip lacks the memory for one). Programming is done over ISP, e.g. with a SparkFun Tiny AVR Programmer and ISP Pogo Adapter, or a USBtinyISP/USBasp. The repository's `Documents` folder has PDF kit-assembly instructions, and the GitHub README includes a short animated GIF of the badge in action.
