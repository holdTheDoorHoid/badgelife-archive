---
title: DC801 Minibadge
id: saintcon-2017-dc801-minibadge
layout: badge
parent: Saintcon 2017
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2017
year: 2017
makers:
- name: snurkle engineering / hamster
  url: https://www.tindie.com/stores/hamster/
summary: A minibadge shaped like Helga, the DC801 mascot, with a pair of RGB LEDs for eyes that slow-cycle through colors at random.
functions: 'No interactive functions; two RGB LEDs automatically cycle through colors slowly and at random. Can be worn via header pins or as a shirt pin.'
look:
  colors: []
  shape: null
  themes:
  - mascot
  - security
tech:
  mcu: none
  leds:
    count: 2
    type: RGB
    note: Automatic slow color-cycling; brightness set via user-selected resistor (0ohm, 470ohm, or 1kohm).
  display: null
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: 'Tindie listing marked "Product Retired" / no longer available for sale as of 2026-09-07.'
  distribution:
  - purchase
  where: Sold via the maker's Tindie store (snurkle engineering); now retired.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/cavehamster/DC801-SAINTCON2017-Minibadge
  firmware_url: null
  eda_tool: KiCad
  license: MIT
  notes: Repo is named for the 2017 SAINTCON badge; includes KiCad design files and a .pretty footprint library.
links:
- label: www.tindie.com/products/hamster/dc801-minibadge-badgelife-addon
  url: https://www.tindie.com/products/hamster/dc801-minibadge-badgelife-addon/
  kind: store
- label: github.com/cavehamster/DC801-SAINTCON2017-Minibadge
  url: https://github.com/cavehamster/DC801-SAINTCON2017-Minibadge
  kind: repo
images:
- file: assets/images/badges/saintcon-2017/dc801-minibadge/8534397253.jpg
  source: "https://www.tindie.com/products/hamster/dc801-minibadge-badgelife-addon/"
  credit: "snurkle engineering"
  caption: "DC801 Minibadge featuring Helga with RGB LED eyes"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
- 'The Tindie listing and its linked GitHub repo (cavehamster/DC801-SAINTCON2017-Minibadge) both tie this minibadge to the 2017 SAINTCON badge, but the same listing also says it plugs into the DC25 and DC26 DC801 DEF CON badges. No matching id for SAINTCON 2017 was found for a DC801/DEF CON-specific event in events.yml at the "other" level, and there is a saintcon-2017 id; recommend event: saintcon-2017 (see event_corrected_to) with the DC25/DC26 compatibility called out here rather than treated as the primary event.'
status: listed
sources:
- kind: url
  url: https://www.tindie.com/products/hamster/dc801-minibadge-badgelife-addon/
  title: DC801 Minibadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''unknown''.'
- kind: url
  url: https://github.com/cavehamster/DC801-SAINTCON2017-Minibadge
  title: DC801 SAINTCON2017 Minibadge (GitHub)
  accessed: '2026-09-07'
  note: Confirms 2017 SAINTCON origin, KiCad design files, MIT license, LED brightness resistor options.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s Tindie listing and GitHub repo agree on the core facts (Helga mascot, two auto-cycling RGB LED eyes, 3.3V, resistor-selectable brightness). Price and quantity made were not stated anywhere found. The Tindie page frames this as a "badgelife addon" usable on DC25/DC26 DC801 badges as well as the 2017 SAINTCON badge; treated 2017 SAINTCON as the primary/originating event per the repo name. A related, separate product ("DC801 SAO") exists from the same maker and is reported separately below rather than folded into this entry.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/dc801-minibadge/
---

The DC801 Minibadge is a small badgelife addon by snurkle engineering (maker handle "hamster," also known as cavehamster on GitHub), made for DC801, the Salt Lake City DEF CON group. It depicts Helga, the DC801 mascot, with a pair of RGB LEDs standing in for her eyes; the LEDs run automatically, slow-cycling through colors at random with no user interaction. Brightness is set at assembly time by choosing one of three resistor values (0ohm, 470ohm, or 1kOhm).

The design originated for the 2017 SAINTCON badge, per the maker's GitHub repository name and contents, but the Tindie storefront also lists it as compatible with the DC25 and DC26 DC801 DEF CON badges, so it saw use across more than one event. It runs at 3.3V and is meant to be either plugged into a compatible host badge or worn on its own via header pins or a shirt pin tack.

The hardware is fully open source: the maker's GitHub repository (cavehamster/DC801-SAINTCON2017-Minibadge) publishes the KiCad design files and footprint library under an MIT license. The Tindie listing for this minibadge is now marked "Product Retired" and no longer available for purchase; price and production quantity were not stated in any source found.
