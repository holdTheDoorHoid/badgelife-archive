---
title: 'The ides of DEFCON: An Unofficial Electronic Badge'
id: dc25-the-ides-of-defcon-an-unofficial-electronic-badge
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: John Adams
  url: https://hackaday.io/netik
  role: lead / team "Ides"
summary: An independently produced, crowdfunded wearable badge for DEF CON 25 (2017), built as a game platform around a color TFT screen, RGB LEDs, and a sub-1GHz radio for badge-to-badge play.
functions: A wearable game badge and development platform featuring a Roman ("SPQR")-themed battle game played over badge-to-badge wireless links, blinky RGB lighting, sound, and hidden unlock codes that reveal extra features.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - wearable
  - ctf
tech:
  mcu: NXP/Freescale MKW01Z128 (ARM Cortex-M0+ with integrated sub-1GHz radio)
  leds:
    count: 12
    type: WS2812B
    note: RGB status/blinky lighting
  display: 320x240 color TFT, with SD card reader
  connectivity:
  - sub-ghz
  battery: rechargeable battery with USB charging
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 'approximately 225-300 units (Kickstarter-backed production run)'
  availability: sold_out
  distribution:
  - crowdfunding
  - purchase
  where: 'Sold via a Kickstarter presale ("Indie DEFCON Badge: The Ides of DEFCON"); presales sold out, with remaining units offered for sale on-site at DEF CON 25.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/netik/dc25_spqr_badge
  firmware_url: https://github.com/netik/chibios-orchard
  eda_tool: null
links:
- label: hackaday.io/project/14756-the-ides-of-defcon-an-unofficial-electronic-badge
  url: https://hackaday.io/project/14756-the-ides-of-defcon-an-unofficial-electronic-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260708173713/https://hackaday.io/project/14756-the-ides-of-defcon-an-unofficial-electronic-badge
- label: 'GitHub: dc25_spqr_badge (hardware)'
  url: https://github.com/netik/dc25_spqr_badge
  kind: repo
- label: 'GitHub: chibios-orchard (firmware platform)'
  url: https://github.com/netik/chibios-orchard
  kind: repo
- label: 'Kickstarter: Indie DEFCON Badge - The Ides of DEFCON'
  url: https://www.kickstarter.com/projects/1887776662/indie-defcon-badge-the-ides-of-defcon
  kind: store
images:
- file: assets/images/badges/dc25/the-ides-of-defcon-an-unofficial-electronic-badge/01c6d1aad3.jpg
  source: "https://hackaday.io/project/14756-the-ides-of-defcon-an-unofficial-electronic-badge"
  credit: "John Adams / Team Ides"
  caption: "The Ides of DEFCON badge, DC25 (2017)"
- file: assets/images/badges/dc25/the-ides-of-defcon-an-unofficial-electronic-badge/99a32247b6.jpg
  source: "https://hackaday.io/project/14756-the-ides-of-defcon-an-unofficial-electronic-badge"
  credit: "John Adams / Team Ides"
  caption: "The Ides of DEFCON badge close-up"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/14756-the-ides-of-defcon-an-unofficial-electronic-badge
  title: 'The ides of DEFCON: An Unofficial Electronic Badge'
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''DEF CON 25''.'
  archived: https://web.archive.org/web/20260708173713/https://hackaday.io/project/14756-the-ides-of-defcon-an-unofficial-electronic-badge
- kind: url
  url: https://hackaday.io/project/14756-the-ides-of-defcon-an-unofficial-electronic-badge
  title: 'The ides of DEFCON: An Unofficial Electronic Badge (project log)'
  accessed: '2026-09-07'
  note: 'Full project log: confirms maker (John Adams / "netik"), MCU (Freescale MKW01Z128 / ChibiOS-Orchard platform), 320x240 TFT + SD card, 12x WS2812 LEDs, sub-1GHz radio, Kickstarter presale sold out with production run around 225-300 units, GitHub links for hardware and firmware, and a follow-up DC27 (2019) badge project.'
- kind: url
  url: https://github.com/netik/dc25_spqr_badge
  title: netik/dc25_spqr_badge
  accessed: '2026-09-07'
  note: Hardware repo linked from the Hackaday project page.
- kind: url
  url: https://github.com/netik/chibios-orchard
  title: netik/chibios-orchard
  accessed: '2026-09-07'
  note: Firmware/platform repo (ChibiOS + Orchard framework) linked from the Hackaday project page.
- kind: url
  url: https://www.kickstarter.com/projects/1887776662/indie-defcon-badge-the-ides-of-defcon
  title: 'Kickstarter: Indie DEFCON Badge - The Ides of DEFCON'
  accessed: '2026-09-07'
  note: 'Referenced from the Hackaday page as the presale channel; page itself returned HTTP 403 to direct fetch (Kickstarter blocks automated access), so no pledge-tier pricing was confirmed directly.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Retail/pledge price could not be confirmed - the Hackaday log gives per-board manufacturing cost estimates ($140 prototype, $30-60/board bulk before screen and battery) but not what backers/attendees actually paid, and the Kickstarter page itself blocked automated fetching (HTTP 403). Exact LED count/type and quantity are drawn from the Hackaday project log and a third-party summary rather than a spec sheet, so treated as medium confidence. The team produced a sequel badge for DEF CON 27 (2019); see hackaday.io/project/161163-team-ides-dc27-badge, reported separately as a candidate entry.'
last_modified_date: '2026-09-07'
---

The Ides of DEFCON was an independently produced, crowdfunded electronic badge built for DEF CON 25 in 2017 by John Adams ("netik") and a small team of Bay Area engineers and makers, run as a self-funded project outside the official DEF CON badge process. It shipped as a wearable game platform: a 320x240 color TFT screen with an SD card slot, 12 WS2812 RGB LEDs, a speaker, and an NXP/Freescale MKW01Z128 (Cortex-M0+ with an integrated sub-1GHz radio), running a ChibiOS-based firmware stack the team called "Orchard." The badge's centerpiece was a Roman/"SPQR"-themed battle game played badge-to-badge over the built-in radio, alongside blinky lighting effects and hidden unlock codes that revealed extra features.

The badge was funded and sold through a Kickstarter campaign ("Indie DEFCON Badge: The Ides of DEFCON"), which the team's project log describes as selling out its presale allotment, with a production run on the order of 225-300 units; a further batch was made available for on-site sale at DEF CON 25 itself. The team published both the hardware and firmware as open source after the con, with the PCB design in the `dc25_spqr_badge` GitHub repository and the ChibiOS/Orchard firmware platform in `chibios-orchard`. The same team went on to build a follow-up badge for DEF CON 27 in 2019, documented as a separate Hackaday.io project.
