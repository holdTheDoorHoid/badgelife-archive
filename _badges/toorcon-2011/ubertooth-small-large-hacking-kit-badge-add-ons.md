---
title: Ubertooth small/large hacking kits (ToorCon 13 badge add-ons)
id: toorcon-2011-ubertooth-small-large-hacking-kit-badge-add-ons
layout: badge
parent: ToorCon 13
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: toorcon-2011
year: 2011
makers:
- name: Great Scott Gadgets
  url: https://greatscottgadgets.com/tc13badge/
summary: Two optional add-on kits for the ToorCon 13 badge; the small kit lets the badge run on USB power, and the large kit adds the parts and a second microcontroller needed to turn the badge into a passive Ubertooth-style Bluetooth monitor.
functions: 'Small kit: USB power delivery for the base badge. Large kit: everything in the small kit, plus components and an LPC1756 microcontroller that add Ubertooth-capable passive Bluetooth sniffing to the badge, alongside its stock 2.4 GHz spectrum-analyzer function (Wi-Fi, Bluetooth, ZigBee, and microwave-oven signal detection via 13 channel LEDs).'
look:
  colors: []
  shape: null
  themes:
  - radio
  - hardware tool
  - security
tech:
  mcu: LPC1756 (added by large kit; base badge uses a Renesas R5F212L4/R8C)
  leds: null
  display: null
  connectivity:
  - bluetooth
  battery: CR2032 (on base badge)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Sold/distributed alongside the ToorCon 13 badge at ToorCon San Diego 13 (Oct 7-9, 2011); build guides still hosted by Great Scott Gadgets.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/greatscottgadgets/ubertooth/tree/master/hardware/tc13badge
  firmware_url: https://github.com/greatscottgadgets/ubertooth
  eda_tool: null
links:
- label: badge.gallery/addons/toorcon-13-spectrum-analyzer-badge/ubertooth-large-hacking-kit
  url: https://badge.gallery/addons/toorcon-13-spectrum-analyzer-badge/ubertooth-large-hacking-kit
  kind: website
- label: 'Great Scott Gadgets: ToorCon 13 Badge'
  url: https://greatscottgadgets.com/tc13badge/
  kind: website
- label: 'GitHub: ubertooth/hardware/tc13badge'
  url: https://github.com/greatscottgadgets/ubertooth/blob/master/hardware/tc13badge/README
  kind: repo
images: []
contact: {}
notes:
- Sweep's title read "Ubertooth small/large hacking kit (badge add-ons)"; retitled to
  "kits" (plural) since these are two distinct kits (small and large) per the maker's
  own page.
status: released
sources:
- kind: url
  url: https://badge.gallery/addons/toorcon-13-spectrum-analyzer-badge/ubertooth-large-hacking-kit
  title: Ubertooth small/large hacking kit (badge add-ons)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://greatscottgadgets.com/tc13badge/
  title: 'ToorCon 13 Badge - Great Scott Gadgets'
  accessed: '2026-09-10'
  note: Maker's own page describing the badge, the small kit (USB power), and the large kit (adds Ubertooth capability via an LPC1756).
- kind: url
  url: https://github.com/greatscottgadgets/ubertooth/blob/master/hardware/tc13badge/README
  title: 'ubertooth/hardware/tc13badge README - GitHub'
  accessed: '2026-09-10'
  note: Confirms open hardware/firmware for the tc13badge kits under the Ubertooth project.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Confirmed as a real, released pair of add-on kits (not just a search snippet) via the maker's own site and GitHub. Could not find price, quantity made, or a photo of the kit hardware itself (only a PCB diagram of the base badge was found, which was not used since it does not show the kit components). Availability today is unclear ("historical" per badge.gallery); build/parts-list PDFs are still linked from the maker's page but were not fetched for further detail.
last_modified_date: '2026-09-10'
---

Great Scott Gadgets sold two optional hardware add-on kits alongside the ToorCon 13 badge at ToorCon San Diego 13 in October 2011. The base badge is a 2.4 GHz RF spectrum analyzer, using 13 LEDs to show activity across the Wi-Fi band and flagging Bluetooth, ZigBee, and microwave-oven interference. The small kit simply added the parts needed to run the badge from USB power instead of its CR2032 coin cell.

The large kit went further: it supplied everything in the small kit plus the additional components and a second microcontroller (an NXP LPC1756) required to turn the badge into a passive Ubertooth-capable Bluetooth monitor, tying the badge into Great Scott Gadgets' broader Project Ubertooth line. Building the large kit meant installing the added parts and flashing firmware to both the badge's original Renesas microcontroller and the new LPC1756.

Hardware designs and firmware for both kits are published as open source under the Ubertooth project on GitHub, and Great Scott Gadgets' own ToorCon 13 badge page still links assembly diagrams and parts lists. Pricing, production quantities, and current stock status were not stated on any source found.
