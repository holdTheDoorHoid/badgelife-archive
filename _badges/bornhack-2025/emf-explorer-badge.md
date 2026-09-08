---
title: EMF Explorer Badge
id: bornhack-2025-emf-explorer-badge
layout: badge
parent: BornHack 2025
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: bornhack-2025
year: 2025
makers:
- name: Darcy Neal (SporkLogic)
  url: https://sporklogic.com/
summary: 'A through-hole soldering kit that senses ambient electromagnetic frequencies (20Hz-20kHz) and amplifies them roughly 1000x into headphones, letting the wearer "hear" Bluetooth devices, cellphones, laptop touchpads, and other electronics.'
functions: 'Detects and audibly amplifies hidden EM signals from nearby electronics via an induction coil and amplifier IC; output plays through a stereo headphone jack. Also lights up as a wearable badge (one LED).'
look:
  colors: []
  shape: null
  themes:
  - radio
  - measurement
  - hardware tool
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 1
    type: null
    note: Single LED for wearable illumination; not addressable/RGB per sources checked.
  display: none
  connectivity:
  - audio
  battery: 2x AAA
  sao_version: none
get_one:
  price: "£23 (Pimoroni); price not listed on SporkLogic's own page"
  price_usd: null
  quantity: ''
  availability: available
  availability_note: 'As of 2026-09-08, listed out of stock on Pimoroni''s shop (restock signup offered); listing still live on SporkLogic and Maker Shed.'
  distribution:
  - purchase
  - kit
  where: 'Sold as a soldering kit via SporkLogic''s own site, Maker Shed, Pimoroni, and local pickup via Ko-fi; a bare PCB is also available via OSH Park.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/drc3p0/emf-explorer-badge
  firmware_url: null
  eda_tool: KiCad
links:
- label: sporklogic.com/emf-explorer-badge
  url: https://sporklogic.com/emf-explorer-badge/
  kind: website
- label: EMF Explorer Badge soldering kit (SporkLogic store)
  url: https://sporklogic.com/product/emf-explorer-soldering-kit/
  kind: store
- label: emfexplorer.space
  url: https://emfexplorer.space/
  kind: website
- label: EMF Explorer Badge (GitHub, KiCad files)
  url: https://github.com/drc3p0/emf-explorer-badge
  kind: repo
- label: EMF Explorer Badge Soldering Kit (Pimoroni)
  url: https://shop.pimoroni.com/products/emf-explorer-badge
  kind: store
- label: EMF Explorer Kit (Maker Shed)
  url: https://www.makershed.com/products/emf
  kind: store
images:
  - file: assets/images/badges/bornhack-2025/emf-explorer-badge/5121f12ffa.jpg
    source: "https://sporklogic.com/emf-explorer-badge/"
    credit: "SporkLogic"
    caption: "EMF Explorer Badge illuminated, worn"
  - file: assets/images/badges/bornhack-2025/emf-explorer-badge/1a722758c1.jpg
    source: "https://sporklogic.com/emf-explorer-badge/"
    credit: "SporkLogic"
    caption: "EMF Explorer Badge kit with packaging"
contact: {}
notes:
- 'The sweep imported this as a BornHack 2025 badge; it is actually a general SporkLogic product, not made specifically for BornHack. It was taught as a soldering workshop at BornHack 2025 (program listing: bornhack.dk/bornhack-2025/program/sensing-the-world-around-you-with-emf/) and was also run as a workshop at Toorcamp 2024 (per photo dates on the maker''s own product page) and covered as a third-party badge in Hackaday''s BornHack roundup. Kept filed under bornhack-2025 since that is the event the sweep and this archive entry are tied to; the kit itself predates and outlives any single con. Found by the event-year sweep, task bornhack-2025.'
status: released
sources:
- kind: url
  url: https://sporklogic.com/emf-explorer-badge/
  title: EMF Explorer Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bornhack-2025); event read as ''bornhack-2025''.'
- kind: url
  url: https://sporklogic.com/emf-explorer-badge/
  title: EMF Explorer Badge - SporkLogic
  accessed: '2026-09-08'
  note: 'Core description, function, battery, LED, packaging photos.'
- kind: url
  url: https://emfexplorer.space/
  title: EMF Explorer - Tune in to the electromagnetic frequencies around you
  accessed: '2026-09-08'
  note: 'Confirms maker (SporkLogic / Darcy Neal), frequency range and gain spec, distribution channels, GitHub repo.'
- kind: url
  url: https://shop.pimoroni.com/products/emf-explorer-badge
  title: EMF Explorer Badge Soldering Kit - Pimoroni
  accessed: '2026-09-08'
  note: 'Price (GBP), open-source KiCad repo link, IC chip and component list, out-of-stock status, Make: Vol. 90 feature.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Confirmed as a real, still-sold product (not just a search snippet). Could not find a stated total quantity made or a single USD price (SporkLogic''s own page has no listed price; Pimoroni lists £23). No MCU is used (amplifier IC only, marked "2115D" on the Pimoroni parts list) and no display. Left get_one.price_usd empty since no USD figure was found on the maker''s own page.'
last_modified_date: '2026-09-08'
---

The EMF Explorer Badge is a through-hole soldering kit from SporkLogic (Darcy Neal) that turns invisible electromagnetic activity into sound. An induction coil picks up EMF in roughly the 20Hz-20kHz range, an amplifier circuit boosts it about a thousand-fold, and the result plays through a headphone jack — letting the builder "hear" Bluetooth radios, phones, laptop touchpads, and other nearby electronics. It also doubles as a wearable badge, running off two AAA batteries with a single LED for illumination.

It is not a con-specific badge: SporkLogic sells it year-round through its own site, Maker Shed, and Pimoroni (with a bare PCB also available via OSH Park), and it has been featured in Make: Volume 90. This archive entry exists because BornHack 2025 ran it as a soldering workshop ("Sensing the world around you with EMF"); the same kit was also taught at Toorcamp 2024 and picked up by Hackaday's BornHack badge coverage.

## Make your own

The hardware is fully open: KiCad design files are published on GitHub at [drc3p0/emf-explorer-badge](https://github.com/drc3p0/emf-explorer-badge), and Pimoroni's listing links an assembly guide plus an "interactive frequency monitor" and a companion zine explaining how the board works.
