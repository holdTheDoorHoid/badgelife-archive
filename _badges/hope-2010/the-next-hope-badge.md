---
title: The Next HOPE Badge
id: hope-2010-the-next-hope-badge
layout: badge
parent: The Next HOPE
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hope-2010
year: 2010
makers:
- name: HOPE / OpenAMD badge committee
  role: hardware/firmware (design led by Travis Goodspeed and the badge committee)
summary: An active RFID attendee badge for The Next HOPE (2010) that beacons each wearer's position several times a second, letting an on-site tracking system show where attendees are around the venue.
functions: Broadcasts a 2.4GHz beacon packet a few times a second so an aggregation server can estimate each badge's location from signal strength/packet loss across the venue; color-coded LEDs distinguish attendees, speakers, and security; badges could be reprogrammed over USB or JTAG/BSL for on-badge hacking.
look:
  colors: []
  shape: null
  themes:
  - radio
  - security
tech:
  mcu: MSP430F2618 / MSP430F2418
  leds:
    count: 3
    type: discrete
    note: 'Color-coded RGB indicator LEDs: blue for attendees, green for speakers, red for security.'
  display: none
  connectivity:
  - rfid
  - usb
  battery: separate (badge and battery given out separately; not inserting the battery opted a wearer out of tracking)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to attendees of The Next HOPE (Hotel Pennsylvania, Manhattan, July 16-18, 2010); optional USB reprogramming upgrade kits were also offered at the conference and were expected to sell out quickly.
make_your_own:
  open_source: yes
  hardware_url: null
  firmware_url: https://github.com/openamd/badge_firmware
  eda_tool: null
links:
- label: hackaday.com/2010/06/22/next-hope-badge-hacking-primer
  url: https://hackaday.com/2010/06/22/next-hope-badge-hacking-primer/
  kind: article
- label: github.com/openamd/badge_firmware
  url: https://github.com/openamd/badge_firmware
  kind: repo
- label: travisgoodspeed.blogspot.com/2010/06/hacking-next-hope-badge.html
  url: https://travisgoodspeed.blogspot.com/2010/06/hacking-next-hope-badge.html
  kind: website
- label: ieee-dataport.org/open-access/crawdad-hopenhamd
  url: https://ieee-dataport.org/open-access/crawdad-hopenhamd
  kind: doc
images:
- file: assets/images/badges/hope-2010/the-next-hope-badge/2c2b9934c2.jpg
  source: "https://hackaday.com/2010/06/22/next-hope-badge-hacking-primer/"
  credit: "Hackaday"
  caption: "The Next HOPE badges, 2010"
- file: assets/images/badges/hope-2010/the-next-hope-badge/e53465a9a2.jpg
  source: "https://travisgoodspeed.blogspot.com/2010/06/hacking-next-hope-badge.html"
  credit: "Travis Goodspeed"
  caption: "The Next HOPE badge (NHBadge)"
contact: {}
notes:
- The community sheet listed this as "The Next Hope Badge"; kept as title. Original sweep note called the maker "HOPE / OpenAMD badge committee" — sources credit Travis Goodspeed as lead designer alongside the badge committee, building on the OpenBeacon/Sputnik and Last HOPE badge lineage.
- Price and quantity made were not stated in any source checked; left empty.
- Hardware (schematic/PCB) files were not found at a public URL, only discussed/pictured in Goodspeed's writeup; only the firmware repo URL is confirmed, so open_source is recorded as "yes" based on the firmware being public, but hardware_url is left empty since no direct hardware repo/Gerbers link was found.
status: released
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Confirmed by Hackaday's hacking-primer writeup, Travis Goodspeed's own blog post (detailed technical breakdown), the openamd/badge_firmware GitHub repo, and an IEEE DataPort dataset description of the RFID tracking captures from the event. All sources agree on the core facts (MSP430 + NRF24L01+ active RFID beacon badge for The Next HOPE, July 2010). No price or production quantity found anywhere.
last_modified_date: '2026-09-10'
---

The Next HOPE badge was an active RFID tracking badge given to attendees of The Next HOPE, held at the Hotel Pennsylvania in Manhattan in July 2010. Built around an MSP430F2618 or MSP430F2418 microcontroller paired with an NRF24L01+ 2.4GHz radio, the badge broadcast short beacon packets several times a second; an aggregation server used packet loss and signal data from OpenBeacon receivers around the venue to estimate each wearer's approximate location in real time, continuing the OpenAMD (Attendee Meta Data) concept from earlier HOPE badges. Onboard RGB LEDs were color-coded to identify attendees, speakers, and security staff at a glance.

Badges shipped separately from their batteries, so attendees who didn't want to be tracked could simply leave the battery out. The design was covered in detail in a Hackaday "hacking primer" and in a technical writeup by Travis Goodspeed, who was closely involved with the badge committee; the badge exposed JTAG, BSL, NRF/SPI, and MSP430 Port 3 GPIO headers for hardware hacking, and optional USB reprogramming upgrade kits were sold at the conference. The three days of RFID beacon traffic captured from the badges were later published as a research dataset (CRAWDAD hope/nh_amd) covering roughly 200 million packets.

## Make your own

The firmware is public at github.com/openamd/badge_firmware, targeting the MSP430F2618/F2418 in 80LQFP or 64LQFP packages. Custom firmware can be loaded over the built-in hardware bootloader using tools such as goodfet.bsl. No public hardware (schematic/PCB/Gerber) repository was located during this research pass, though annotated schematics appear in Travis Goodspeed's blog writeup.
