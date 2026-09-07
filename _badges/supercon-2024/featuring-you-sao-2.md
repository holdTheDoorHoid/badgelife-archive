---
title: Featuring You!
id: supercon-2024-featuring-you-sao-2
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Nanik Adnani
  url: https://hackaday.io/nanik
summary: A fully analog SAO shaped like a giant flashing red arrow that points up at the wearer and leaves space to write your name, built with an astable multivibrator and BJT LED drivers so it could be assembled by JLCPCB economic assembly for Supercon 8's SAO contest.
functions: 'Flashes a red arrow LED to draw attention to a hand-written name written on the board; no other interactive functions.'
look:
  colors: [red]
  shape: arrow
  themes: [text]
tech:
  mcu: none
  leds:
    count: null
    type: discrete
    note: Driven by BJT buffers off an astable multivibrator, not addressable.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: free
  distribution: [free_drop]
  where: The maker offered to hand out copies in person to interested attendees at Supercon 8.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/nanikgeorge/FeaturingYouSAO
  firmware_url: null
  eda_tool: KiCad
  notes: Repo also includes an LTspice simulation of the astable multivibrator circuit and a graphics folder for the artwork.
links:
- label: hackaday.io/project/198924-featuring-you
  url: https://hackaday.io/project/198924-featuring-you
  kind: hackaday
- label: github.com/nanikgeorge/FeaturingYouSAO
  url: https://github.com/nanikgeorge/FeaturingYouSAO
  kind: repo
images:
  - file: assets/images/badges/supercon-2024/featuring-you-sao-2/f7eab93eb7.jpg
    source: "https://hackaday.io/project/198924-featuring-you"
    credit: "Nanik Adnani"
    caption: "The Featuring You! SAO, a red flashing arrow with space to write your name"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198924-featuring-you
  title: Featuring You!
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/198924-featuring-you
  title: Featuring You! - Hackaday.io project page
  accessed: '2026-09-07'
  note: Confirmed maker, event (Supercon 8 SAO contest), circuit description (astable multivibrator with BJT LED drivers), JLCPCB economic assembly, free giveaway plan, and pulled the project photo.
- kind: url
  url: https://github.com/nanikgeorge/FeaturingYouSAO
  title: nanikgeorge/FeaturingYouSAO
  accessed: '2026-09-07'
  note: Confirmed repo contents (KiCad PCB files, LTspice sim, graphics folder) and the maker's stated motivation (Supercon badges lack a place to write your name).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'LED count is not stated by the maker; described only as "giant flashing red arrow" LEDs. Quantity made is not stated. No firmware exists since the board is purely analog (no MCU).'
last_modified_date: '2026-09-07'
---

Featuring You! is a Simple Add-On built by Nanik Adnani for the SAO contest at Supercon 8 (2024). The maker noticed that Supercon's badges never leave a spot for attendees to write their own name, so this SAO fills that gap: a giant red arrow, built entirely from analog components, flashes to point down at a blank space where the wearer can write their name by hand.

The board has no microcontroller. A simple astable multivibrator circuit generates the flashing signal, and BJT transistors buffer that oscillator output to drive the arrow's LEDs, with resistors setting the current. The design was built specifically so it could go through JLCPCB's economic assembly service, keeping the SAO cheap to produce; the maker noted afterward that the LEDs came out brighter than intended and that a resistor value would be increased in a future revision, though the units handed out at Supercon work as built.

All hardware design files are open source, published on GitHub as KiCad PCB files, alongside an LTspice simulation of the multivibrator circuit and the graphics used on the board. The maker offered free copies to interested attendees at Supercon; no price, run size, or ongoing availability is stated.
