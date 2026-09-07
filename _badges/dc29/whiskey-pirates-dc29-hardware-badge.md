---
title: Whiskey Pirates DC29 Hardware Badge
id: dc29-whiskey-pirates-dc29-hardware-badge
layout: badge
parent: DC29
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc29
year: 2021
makers:
- name: Whiskey Pirates (TrueControl)
  url: http://whiskeypirates.com/
summary: A hand-assembled RISC-V nametag badge from the Whiskey Pirates crew, sandwiching a PCB between an etched acrylic faceplate and a clear, edge-lit backplate.
functions: Shows a customizable name on its OLED display, with firmware that tilts the displayed letters to match the physical angle of the badge as it hangs. RGB "eye" LEDs flicker through selectable color programs, and edge-lit RGB LEDs shine through the clear acrylic backplate. A red LED doubles as an ambient-light sensor and low-battery indicator. Four acrylic button caps on the badge's cross-bone arms provide input.
look:
  colors: [black, clear]
  shape: skull
  themes: [pirate, skull, radio, hardware tool]
tech:
  mcu: GD32VF103 (RISC-V)
  leds:
    count: null
    type: RGB
    note: RGB "eye" LEDs plus edge-lit RGB LEDs firing into the clear acrylic backplate; a separate red LED serves as light sensor and low-battery indicator.
  display: OLED
  connectivity: [usb]
  battery: 1x AAA
  sao_version: null
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: free
  distribution: [free_drop]
  where: 'Given out by the Whiskey Pirates crew to people found in person at DEF CON 29; the maker''s site states "we don''t sell it" and getting one requires "just be cool. no guarantees."'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://git.trueserve.org/WhiskeyPirates/dc29-whiskey-pirates-badge
  eda_tool: null
links:
- label: whiskeypirates.com
  url: http://whiskeypirates.com/
  kind: website
- label: hackaday.com/2021/08/06/hands-on-whiskey-pirates-dc29-hardware-badge-blings-with-risc-v
  url: https://hackaday.com/2021/08/06/hands-on-whiskey-pirates-dc29-hardware-badge-blings-with-risc-v/
  kind: article
- label: dc29.whiskeypirates.com
  url: https://dc29.whiskeypirates.com/
  kind: website
- label: 'git.trueserve.org: WhiskeyPirates/dc29-whiskey-pirates-badge'
  url: https://git.trueserve.org/WhiskeyPirates/dc29-whiskey-pirates-badge
  kind: repo
images:
- file: assets/images/badges/dc29/whiskey-pirates-dc29-hardware-badge/5bf24e8a34.jpg
  source: "https://hackaday.com/2021/08/06/hands-on-whiskey-pirates-dc29-hardware-badge-blings-with-risc-v/"
  credit: "Hackaday / TrueControl"
  caption: "Front of the badge showing the OLED nametag through the etched acrylic faceplate"
- file: assets/images/badges/dc29/whiskey-pirates-dc29-hardware-badge/ac3372ce80.jpg
  source: "https://hackaday.com/2021/08/06/hands-on-whiskey-pirates-dc29-hardware-badge-blings-with-risc-v/"
  credit: "Hackaday / TrueControl"
  caption: "Edge-lit RGB LEDs shining through the clear acrylic backplate"
contact: {}
notes:
- RISC-V (GD32VF103) badge with edge-lit acrylic sandwich, OLED display showing tilt-corrected name text, serialized hand-assembled units.
status: released
sources:
- kind: url
  url: http://whiskeypirates.com/
  title: Whiskey Pirates DC29 Hardware Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc28-dc29); event read as ''DEF CON 29 (unofficial)''.'
- kind: url
  url: https://hackaday.com/2021/08/06/hands-on-whiskey-pirates-dc29-hardware-badge-blings-with-risc-v/
  title: 'Hands-On: Whiskey Pirates DC29 Hardware Badge Blings With RISC-V'
  accessed: '2026-09-07'
  note: 'Primary source for chip (GD32VF103 RISC-V, plus a PDK13 Padauk chip and a CH552T USB debug chip), OLED tilt-text feature, RGB eye and edge LEDs, red light-sensor/low-battery LED, acrylic-PCB-acrylic construction, button caps, USB ports, AAA battery, hard power switch, serialization, and hand-assembly (~4 hours/badge). Also source of both saved images.'
- kind: url
  url: https://dc29.whiskeypirates.com/
  title: WP DC29 - firmware and FAQ page
  accessed: '2026-09-07'
  note: 'Maker''s own DC29 badge page: confirms firmware/source download links, that the badge is not sold ("we don''t sell it"), and distribution by chance/social proximity at the con ("just be cool. no guarantees").'
- kind: url
  url: https://git.trueserve.org/WhiskeyPirates/dc29-whiskey-pirates-badge
  title: WhiskeyPirates/dc29-whiskey-pirates-badge - trueserve Git
  accessed: '2026-09-07'
  note: 'Confirms a public firmware/resources repo exists for the badge (description: "Firmware and resources for the Whiskey Pirates DC29 minibadge - a nametag badge with a 3 layer acrylic-PCB-acrylic stackup"); repo requires sign-in to browse file contents, so hardware/Gerber availability inside it could not be confirmed.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s own pages and Hackaday agree on construction and distribution. LED count, exact quantity made, and whether hardware design files (KiCad/Gerbers) are included in the linked repo could not be confirmed (the repo requires login to browse past the top-level page). No price - the maker states explicitly it is not sold, only given to people met in person at the con.'
last_modified_date: '2026-09-07'
---

The Whiskey Pirates DC29 Hardware Badge is a hand-built nametag badge made by TrueControl for the Whiskey Pirates crew at DEF CON 29 (2021). It sandwiches a PCB between an etched acrylic faceplate and a clear acrylic backplate, with an OLED display showing the wearer's name through the faceplate. A notable firmware touch tilts the displayed name text to match the physical angle at which the badge is hanging. The board is built around a GD32VF103, a RISC-V microcontroller, which the maker believed at the time might be the first unofficial con badge to use a hardware RISC-V core; it also carries a small Padauk PDK13 and a CH552T USB chip used for debugging.

RGB "eye" LEDs flicker through selectable color programs, and additional RGB LEDs fire into the edges of the clear acrylic backplate for a lit-edge effect, while a red LED does double duty as an ambient light sensor and low-battery indicator. The badge is powered by a single AAA battery with a hard power switch, and has two USB ports (one for the main MCU, one for the debug chip). Four acrylic button caps mounted on the badge's cross-bone-shaped arms serve as the input controls. Each unit was serialized with its own number, visible in an on-badge "About" menu, and the crew reported roughly four hours of hand-assembly labor per badge, done at the designer's home except for the ICs and bare PCB fabrication.

The badge was never sold; the Whiskey Pirates' own DC29 page is blunt about this ("we don't sell it") and says getting one requires being found and liked in person at the con ("just be cool. no guarantees."). Firmware and other resources are hosted in a public git repository at git.trueserve.org, and the same page links firmware binaries and source archives directly, though the repository itself requires a login to browse past its landing page, so it was not possible to confirm whether hardware design files (schematics/Gerbers) are included alongside the firmware.
