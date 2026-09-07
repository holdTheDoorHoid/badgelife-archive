---
title: DCZia Laser Theremin Synth Badge
id: dc27-dc801-def-con-27-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: DCZia
  url: https://dczia.net
summary: A DEF CON 27 badge built around two laser time-of-flight sensors that turn hand movement in front of the badge into a "laser theremin" synthesizer.
functions: Play a synthesizer theremin-style by moving your hands over two laser time-of-flight sensors, changing pitch/volume; a rotary encoder selects the waveform. Five keys (D C Z I A) switch onboard LED light patterns and colors. Includes onboard speaker/amp, headphone jack, and SD card storage.
look:
  colors: []
  shape: null
  themes:
  - music
  - hardware tool
tech:
  mcu: NRF52 (Rigado BMD-340)
  leds:
    count: null
    type: RGB
    note: Neopixel RGB LEDs; behavior changes with hand proximity on left/right sides.
  display: 0.96" OLED (SSD1306)
  connectivity:
  - ble
  inputs:
  - buttons
  - rotary encoder
  power: null
  battery: null
  sao_version: null
  sao_ports: 2
get_one:
  price: $120
  price_usd: 120
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  - kit
  where: Sold as a complete kit by snurkle engineering on Tindie; listed as out of stock when checked (2026-09-07).
make_your_own:
  open_source: true
  hardware_url: https://github.com/dczia/Defcon27-Badge
  firmware_url: https://github.com/dczia/Defcon27-Badge
  eda_tool: KiCad
links:
- label: github.com/hamster/Defcon27-Badge
  url: https://github.com/hamster/Defcon27-Badge
  kind: repo
- label: github.com/dczia/Defcon27-Badge
  url: https://github.com/dczia/Defcon27-Badge
  kind: repo
- label: DCZia Laser Theremin complete badge kit (Tindie)
  url: https://www.tindie.com/products/hamster/dczia-laser-theremin-complete-badge-kit/
  kind: store
- label: 'Hackaday: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27'
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
images:
- file: assets/images/badges/dc27/dc801-def-con-27-badge/03771e00ed.jpg
  source: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/dczia-laser-theremin-badge-front/
  credit: DCZia / Hackaday
  caption: DCZia laser theremin DEF CON 27 badge, front
- file: assets/images/badges/dc27/dc801-def-con-27-badge/06dfc7d04d.jpg
  source: https://www.tindie.com/products/hamster/dczia-laser-theremin-complete-badge-kit/
  credit: snurkle engineering / Tindie
  caption: DCZia laser theremin badge kit, assembled
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- The sheet listed the maker as "DC801," but the linked repository (a fork of dczia/Defcon27-Badge) is the DCZia group's DEF CON 27 laser theremin badge, not a DC801 badge. Title and maker corrected to DCZia based on the repo, its README, and the Tindie/Hackaday coverage. DC801's own DEF CON 27 badge is a separate project (DC801/DC27PartyBadge, "HCRN") reported separately below.
status: released
sources:
- kind: url
  url: https://github.com/hamster/Defcon27-Badge
  title: DC801 DEF CON 27 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc27''.'
- kind: url
  url: https://github.com/dczia/Defcon27-Badge
  title: 'GitHub - dczia/Defcon27-Badge: DCZia Defcon27 Laser Theremin Synthesizer Badge - 2019'
  accessed: '2026-09-07'
  note: Upstream repo of the linked fork; README gives full hardware/software spec, maker (DCZia), and confirms the badge is unrelated to DC801.
- kind: url
  url: https://www.tindie.com/products/hamster/dczia-laser-theremin-complete-badge-kit/
  title: DCZia Laser Theremin complete badge kit from snurkle engineering on Tindie
  accessed: '2026-09-07'
  note: Price ($120), sold-out availability, and product photos.
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27
  accessed: '2026-09-07'
  note: Confirms badge identity and event; source of the front photo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker corrected from "DC801" (sheet/sweep label) to DCZia; see notes field above for reasoning. Quantity made is unconfirmed: a Seeed Studio blog post ("In the #Badgelife: DEFCON 2019 Badges from concept to production - DCZia") likely covers production numbers but was inaccessible (Cloudflare challenge blocked fetching), so quantity is left blank rather than guessed. LED count and battery/power details were not stated in the sources read.'
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc27/dc801-def-con-27-badge.glb
  method: kicad
  source_file: Hardware/laser-theremin.kicad_pcb
  generated: '2026-09-07'
  bytes: 690116
---

This badge was built by DCZia for DEF CON 27 (2019) around a pair of laser time-of-flight sensors: instead of the antennas of a classic theremin, you wave your hands over the two sensors to control pitch and volume of an onboard synthesizer, with a rotary encoder to pick the waveform. Five clicky keyswitches (spelling out D-C-Z-I-A) switch the RGB LED light patterns, and hand proximity on each side further shifts LED brightness and color. It runs on a Rigado BMD-340 module (Nordic nRF52, 64 MHz Cortex-M4F, Bluetooth 5) and adds an OLED display, onboard speaker and amplifier, a headphone jack, SD card storage, and two SAO connectors for further add-ons.

The hardware (KiCad) and firmware (GNU ARM GCC / Nordic SoftDevice) are open source on GitHub, with a build guide and environment setup docs. A complete assembled/kit version was also sold by snurkle engineering on Tindie for $120, and was sold out as of this check.

The community sheet this entry was seeded from attributed the badge to "DC801," but that appears to be a mix-up: the linked repository is a fork of DCZia's own Defcon27-Badge project, and its README explicitly points to DC801's *own*, separate DEF CON 26/27 party badges as unrelated prior art. DC801's actual DEF CON 27 badge (an Expanse-themed piece called "HCRN," at github.com/DC801/DC27PartyBadge) is a different item and is reported separately rather than merged into this entry.
