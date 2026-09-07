---
title: DC27_ShittyAddons (Deadpool, Punisher, Pickle Rick, Windows)
id: dc27-shittyaddons-deadpool-punisher-pickle-rick-windows
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: ID64F
  url: https://github.com/ID64F
summary: A set of four independent SAOs — Deadpool, Punisher, Pickle Rick, and a Windows-logo design — sold as kits by the same maker for DEF CON 27.
functions: ''
look:
  colors: []
  shape: null
  themes:
  - pop culture
  - movie
  - tv
tech:
  mcu: ATtiny85
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold as kits on the maker's Tindie store (tindie.com/stores/s3gfault) and in person at conferences.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/ID64F/DC27_ShittyAddons
  firmware_url: null
  eda_tool: null
links:
- label: github.com/ID64F/DC27_ShittyAddons
  url: https://github.com/ID64F/DC27_ShittyAddons
  kind: repo
- label: Tindie store (s3gfault)
  url: https://www.tindie.com/stores/s3gfault/
  kind: store
images: []
contact: {}
notes:
- multiple character SAOs in one repo
status: listed
sources:
- kind: url
  url: https://github.com/ID64F/DC27_ShittyAddons
  title: DC27_ShittyAddons (Deadpool, Punisher, Pickle Rick, Windows)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 27''.'
- kind: url
  url: https://raw.githubusercontent.com/ID64F/DC27_ShittyAddons/master/README.rst
  title: DC27_ShittyAddons README.rst
  accessed: '2026-09-07'
  note: Confirms maker sold assembled kits via Tindie (s3gfault) and at conferences; ATtiny85 MCU programmed via a SOIC Bite clip; notes firmware for Punisher and Deadpool was not yet uploaded at time of writing.
- kind: url
  url: https://api.github.com/repos/ID64F/DC27_ShittyAddons
  title: ID64F/DC27_ShittyAddons repo metadata
  accessed: '2026-09-07'
  note: Repo description ("Deadpool, Punisher, Pickle Rick and Windows project files"), created/pushed August 2019, confirming DC27 (2019) timing; contains four assembly PDFs (deadpool_SAO.pdf, pickle_rick_SAO.pdf, punisher_SAO.pdf, windows_SAO.pdf) and no firmware source in the repo.
- kind: url
  url: https://www.tindie.com/stores/s3gfault/
  title: s3gfault Tindie store
  accessed: '2026-09-07'
  note: 'Attempted to check for current listings, price, and photos; blocked by Cloudflare bot-check (could not confirm price, quantity, or availability, or find product photos).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    The GitHub repo (created and last pushed August 2019, matching DC27) holds only
    PDF component-placement diagrams for four separate character/logo SAOs
    (Deadpool, Punisher, Pickle Rick, Windows) sharing an ATtiny85 MCU programmed
    via a SOIC Bite test-clip connector; the README states firmware for the
    Punisher and Deadpool boards had not been uploaded, so open_source is only
    "partial" (schematics/placement published, no firmware in the repo). The
    maker's Tindie store (s3gfault) is named as the sales channel but was
    unreachable behind Cloudflare, so price, quantity made, current availability,
    and photos of the physical boards could not be confirmed. No LED, display, or
    connectivity details were stated anywhere found. Real name behind ID64F /
    s3gfault not published on any page checked.
last_modified_date: '2026-09-07'
---

ID64F released design files for four separate Shitty Add-Ons ahead of DEF CON 27 (2019): Deadpool, Punisher, Pickle Rick, and a Windows-logo board. Each is built around an ATtiny85, programmed through a SOIC Bite test-clip connector rather than a standard header, and the maker sold assembled kits through their Tindie store (s3gfault) as well as in person at conferences.

The GitHub repo (`ID64F/DC27_ShittyAddons`) is mostly a documentation drop rather than a full open-source release: it contains PDF component-placement diagrams for all four boards, but the README notes that firmware for the Punisher and Deadpool designs had not yet been uploaded, and no firmware source appears in the repo at all. No schematic, PCB, or Gerber files are included either — just the placement PDFs.

Details on look (color, exact shape), LEDs, price, and quantities made could not be confirmed: the Tindie storefront named as the sales channel is blocked by Cloudflare bot protection, and no other page describing the finished boards or showing photos of them was found.
