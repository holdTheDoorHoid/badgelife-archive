---
title: HOPE XV Electronic Badge
id: hope-2024-hope-xv-electronic-badge-hope-16
layout: badge
parent: HOPE XV
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hope-2024
year: 2024
makers:
- name: HOPE Badge Team (HBT) with Novel Circuits
summary: 'The official electronic badge given to in-person attendees of HOPE XV, built around an ESP32-C3 with WS2812B LEDs and IR badge-to-badge interaction; open hardware and firmware.'
functions: 'Four buttons cycle LED light patterns, adjust brightness, and send an IR "blast" that makes other badges in range flash their lights and buzz their vibration motor. Runs stock firmware or can be reflashed with MicroPython or ESPHome (via the community ESPHomeBadge project).'
look:
  colors:
  - purple
  - black
  - green
  - pink
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: ESP32-C3
  leds:
    count: 16
    type: WS2812B
    note: "Described on the wiki as \"16 WS2812 or similar\""
  display: none
  connectivity:
  - wifi
  - ir
  - nfc
  - usb
  battery: LiPo, charged via MCP73871 controller
  sao_version: null
get_one:
  price: 'Attendee badge included with registration; pro version $100 (extra components) or $150 (extra components and accessories)'
  price_usd: 150
  quantity: ''
  availability: sold_out
  distribution:
  - free_drop
  - purchase
  where: 'Given to in-person HOPE XV attendees at registration; "pro" versions sold at the on-site Badge Clinic.'
make_your_own:
  open_source: yes
  hardware_url: https://gitlab.com/tidklaas/hip-badge
  firmware_url: https://gitlab.com/tidklaas/hip-badge
  eda_tool: KiCad
links:
- label: wiki.hope.net/index.php?title=HOPE_XV_Electronic_Badge
  url: https://wiki.hope.net/index.php?title=HOPE_XV_Electronic_Badge
  kind: website
- label: gitlab.com/tidklaas/hip-badge
  url: https://gitlab.com/tidklaas/hip-badge
  kind: repo
- label: github.com/fortuna/ESPHomeBadge
  url: https://github.com/fortuna/ESPHomeBadge
  kind: repo
images:
  - file: assets/images/badges/hope-2024/hope-xv-electronic-badge-hope-16/843b0c3413.jpg
    source: "https://wiki.hope.net/index.php?title=HOPE_XV_Electronic_Badge"
    credit: "HOPE wiki"
    caption: "Front of the HOPE XV electronic badge"
  - file: assets/images/badges/hope-2024/hope-xv-electronic-badge-hope-16/924e926a31.jpg
    source: "https://wiki.hope.net/index.php?title=HOPE_XV_Electronic_Badge"
    credit: "HOPE wiki"
    caption: "Back of the HOPE XV electronic badge"
contact: {}
notes:
- Official electronic badge given to in-person attendees of the 2024 HOPE conference, built around an ESP32-C3 with 16 WS2812 LEDs and IR badge-to-badge interaction, open-hardware KiCAD design on GitLab. Found by the event-year sweep, task general-2023.
- 'The sweep titled this entry "HOPE XV Electronic Badge (HOPE_16)" ("HOPE_16" is the wiki page''s internal MediaWiki title slug, not a separate model name); retitled to match the maker''s plain name.'
status: released
sources:
- kind: url
  url: https://wiki.hope.net/index.php?title=HOPE_XV_Electronic_Badge
  title: HOPE XV Electronic Badge (HOPE_16)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2023); event read as ''HOPE 2024''.'
- kind: url
  url: https://wiki.hope.net/index.php?title=HOPE_XV_Electronic_Badge
  title: HOPE XV Electronic Badge
  accessed: '2026-09-08'
  note: 'Confirmed badge, maker, chip, LEDs, IR feature, NFC/air-quality sensor pro-version add-ons, and Badge Clinic pricing.'
- kind: url
  url: https://gitlab.com/tidklaas/hip-badge
  title: tidklaas/hip-badge on GitLab
  accessed: '2026-09-08'
  note: 'Open hardware/firmware repo linked by the wiki as the badge design source (page itself is for a separate Dec 2022 Berlin event, "Hacking in Parallel", reused/adapted for HOPE XV per the wiki).'
- kind: url
  url: https://github.com/fortuna/ESPHomeBadge
  title: fortuna/ESPHomeBadge on GitHub
  accessed: '2026-09-08'
  note: 'Confirms this targets the HOPE XV badge specifically; documents ESPHome-based alternate firmware with buttons, LED strip, vibration motor, NFC, air-quality sensor, and IR control.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'This entry duplicates hope-2024-hope-xv-electronic-badge (same badge, same sources); see duplicate_of in the research report. The linked hip-badge GitLab repo is nominally for a different, earlier event ("Hacking in Parallel", Berlin, Dec 2022) reused as the hardware base for the HOPE XV badge; the wiki itself flags that the repo does not explicitly mention HOPE by name. quantity made and exact firmware version not found.'
last_modified_date: '2026-09-08'
---

The HOPE XV Electronic Badge was the official electronic badge given to in-person attendees of HOPE XV (2024), built by the HOPE Badge Team with Novel Circuits around an ESP32-C3 microcontroller and 16 WS2812B-class addressable LEDs. Four buttons let the wearer cycle light patterns and adjust brightness, and an IR emitter/receiver lets nearby badges "blast" each other, triggering flashing lights and a vibration-motor buzz on the receiving badge.

Beyond the standard badge included with registration, a "pro" version with additional components (NFC tags, an air-quality sensor, and other accessories) was sold on-site at the Badge Clinic for $100 or $150 depending on configuration. The hardware and firmware are open source, published as KiCad design files and firmware on GitLab, and the community-built ESPHomeBadge project lets owners reflash the badge with ESPHome for easier customization, including support for WiFi, a badge-info display page, and Home Assistant integration.

The underlying hardware design traces back to a GitLab repository ("hip-badge") originally associated with a separate, earlier event in Berlin ("Hacking in Parallel," December 2022); the HOPE wiki notes the repo doesn't explicitly reference HOPE by name, so the badge team appears to have adapted an existing open-hardware design rather than starting from scratch.
