---
title: Hackaday 2016 Paper Plate Badge Hack
id: supercon-2016-hackaday-2016-paper-plate-badge-hack
layout: badge
parent: Hackaday Supercon 2016
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2016
year: 2016
makers:
- name: Jessie Tank (ThunderSqueak)
summary: A hack that turns a paper plate and enameled wire into a working speaker for the PIC-based 2016 Supercon badge, driven from a spare output pin.
functions: Plays simple monophonic music/tones on the badge through the paper-plate speaker; firmware toggles pin B0 through defined note frequencies to beep out a tune.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - diy
tech:
  mcu: PIC (2016 Supercon badge's onboard PIC microcontroller)
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution: []
  where: 'Not sold; a DIY project posted with downloadable source/hex files for anyone to build on their own 2016 Supercon badge.'
make_your_own:
  open_source: yes
  hardware_url: null
  firmware_url: https://hackaday.io/project/18303-hackaday-2016-paper-plate-badge-hack
  eda_tool: null
links:
- label: hackaday.io/project/18303-hackaday-2016-paper-plate-badge-hack
  url: https://hackaday.io/project/18303-hackaday-2016-paper-plate-badge-hack
  kind: hackaday
images:
- file: assets/images/badges/supercon-2016/hackaday-2016-paper-plate-badge-hack/91969f61e3.jpg
  source: "https://hackaday.io/project/18303-hackaday-2016-paper-plate-badge-hack"
  credit: "ThunderSqueak"
  caption: "The paper-plate speaker hack attached to the 2016 Supercon badge"
contact: {}
notes:
- Sweep's snippet described it as "a functional speaker for the 2016 Supercon badge" built from a paper plate and enameled wire; the maker's own Hackaday.io page confirms this and adds firmware detail.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/18303-hackaday-2016-paper-plate-badge-hack
  title: Hackaday 2016 Paper Plate Badge Hack
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2016); event read as ''supercon-2016''.'
- kind: url
  url: https://hackaday.io/project/18303-hackaday-2016-paper-plate-badge-hack
  title: Hackaday 2016 Paper Plate Badge Hack (project page)
  accessed: '2026-09-10'
  note: 'Confirmed project details: creator ThunderSqueak, PIC-based badge, paper-plate speaker driven from pin B0, downloadable code/hex archive uploaded 2016-11-17.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed as a real, maker-documented project on the creator''s own Hackaday.io page (not just a search snippet). Could not find the maker''s real name (Jessie Tank) independently verified beyond the archive''s existing record, nor any additional photos, price, or quantity info — this was a free DIY hack, not a sold item, so those fields are intentionally left empty. No separate hardware repo was found; only the firmware/code zip is linked from the project page.'
last_modified_date: '2026-09-10'
---

Built by hardware hacker ThunderSqueak (Jessie Tank) for Hackaday Supercon 2016, this project turns an ordinary paper plate and a coil of enameled wire into a working speaker driven off a spare pin on the PIC-based 2016 Supercon badge. The paper plate acts as the speaker cone; a magnet-and-coil arrangement wired to the badge's pin B0 lets simple firmware toggle the pin at audio frequencies to produce tones.

The accompanying code defines the frequencies for a set of musical notes and includes a basic beep routine to play them in sequence, effectively letting the badge pick out a simple tune through its improvised speaker. The maker describes the code as "sloppy, but functional," and notes that beep frequencies and timings will likely need tuning to suit a different speaker. Source and a precompiled `.hex` (built with Microchip's XC8 Pro compiler) are posted as a downloadable archive on the project page for anyone who wants to replicate the hack on their own badge.

This was a one-off DIY build shared for free rather than a sold or distributed product, so there is no price, production quantity, or purchase information to record.
