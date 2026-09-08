---
title: BruCON 2021 badge
id: brucon-2021-brucon-2021-badge
layout: badge
parent: BruCON 2021
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: brucon-2021
year: 2021
makers:
- name: Jegeva
  role: design/firmware
- name: Ray Harvey
  role: artwork
summary: 'ESP32-based electronic badge for BruCON 0x0D (2021), styled around a backlit gasmask graphic, with a Nokia-style LCD, a D-pad/button menu, RGB LEDs, and an onboard alcohol sensor.'
functions: 'A menu-driven badge (D-pad + A/B buttons) showing a conference schedule and venue map on a Nokia 6100-style LCD; connects to a badge backend over WiFi/MQTT using per-attendee TLS client certificates; drives RGB LEDs behind the gasmask artwork; includes a heated gas sensor used as an onboard breathalyzer/"ALC" reading, a nod to the con''s Westvleteren beer tradition; runs on battery with charge sensing.'
look:
  colors: []
  shape: null
  themes:
  - security
  - horror
  - beer
tech:
  mcu: ESP32
  leds:
    count: null
    type: RGB
    note: Single addressable/analog RGB LED driven behind the gasmask artwork (see leds.c); exact count not stated.
  display: Nokia 6100-style LCD (SPI, 132x132 controller)
  connectivity:
  - wifi
  inputs:
  - buttons
  battery: LiPo, with onboard charge-current sensing
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/Jegeva/BruCON_2021
  firmware_url: https://github.com/Jegeva/BruCON_2021
  eda_tool: KiCad
  license: CERN-OHL-P (firmware and PCB); gasmask artwork is CC/NA by Ray Harvey
  notes: 'Repo includes final Gerbers, KiCad source, ESP-IDF firmware, and the conference backend (PHP enrollment + MQTT). Maker''s README notes two known fab mistakes in the as-built boards: a VBAT trace missing to the sensor/backlight/LED section, and a keyed connector footprint that does not match the part referenced in the KiCad docs (needs a bodge wire).'
links:
- label: github.com/Jegeva/BruCON_2021
  url: https://github.com/Jegeva/BruCON_2021
  kind: repo
images: []
contact: {}
notes:
- ESP32-based BruCON 2021 electronic conference badge with LEDs, backlight and sensor integration, decorated with gasmask artwork. Found by the event-year sweep, task con-brucon.
- 'Sweep title matched the maker''s own; no rewording needed.'
status: released
sources:
- kind: url
  url: https://github.com/Jegeva/BruCON_2021
  title: BruCON 2021 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-brucon); event read as ''BruCON 2021''.'
- kind: url
  url: https://raw.githubusercontent.com/Jegeva/BruCON_2021/main/README.md
  title: 'Jegeva/BruCON_2021 README'
  accessed: '2026-09-08'
  note: 'Confirms maker, event, ESP32 firmware/PCB under CERN-OHL-P, gasmask art credited to Ray Harvey (CC/NA), and two documented fab mistakes.'
- kind: url
  url: https://raw.githubusercontent.com/Jegeva/BruCON_2021/main/firmware/main/nokialcd.h
  title: 'firmware/main/nokialcd.h'
  accessed: '2026-09-08'
  note: 'Confirms a Nokia 6100-family SPI LCD driver plus D-pad (up/down/left/right) and A/B button pin definitions, backlight enable pin, and a charging-detect pin.'
- kind: url
  url: https://raw.githubusercontent.com/Jegeva/BruCON_2021/main/firmware/main/sensor.h
  title: 'firmware/main/sensor.h'
  accessed: '2026-09-08'
  note: 'Confirms an onboard ADC-read, heated gas sensor with an "ALC" calibration task, i.e. an alcohol/breathalyzer-style sensor.'
- kind: url
  url: https://api.github.com/repos/Jegeva/BruCON_2021/git/trees/main?recursive=1
  title: 'Repo file tree (Jegeva/BruCON_2021, main branch)'
  accessed: '2026-09-08'
  note: 'Confirms wifi.c, mqtt.c, leds.c, menu.c/menu.json (schedule), touch.c, battery.c, and a PHP+MQTT conference backend with per-client TLS certs; no photos of the assembled badge were found in the repo, only PCB/silkscreen design files (pcb/gasmask*.svg).'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Core facts (maker, event, MCU, display, LEDs, sensor, connectivity, open-source status) confirmed directly from the maker''s own repo (README + firmware source). Not found anywhere: price, quantity made, how/whether it was distributed to all attendees or sold, and PCB colors/shape. No assembled-badge photos exist in the repo to save (only PCB design SVGs and cropped silkscreen-layer PNGs, which are design files, not photos of the item) — images left empty rather than guessed.'
last_modified_date: '2026-09-08'
---

The BruCON 2021 badge (BruCON 0x0D) was designed by Jegeva, with gasmask artwork by Ray Harvey, for the October 2021 edition of the Belgian security conference. It is built around an ESP32 driving a Nokia 6100-style SPI LCD, a D-pad and two buttons for menu navigation, and RGB LEDs lit behind the gasmask graphic on the PCB.

Beyond the schedule/map menu, the badge talks to a conference backend over WiFi and MQTT, authenticating with a per-attendee TLS client certificate issued by the organizers' own backend (visible in the repo's `backend/` folder, including the PHP enrollment script and certificate-authority files). It also carries a heated gas sensor whose firmware task is explicitly named for alcohol calibration, functioning as an onboard breathalyzer — a wink at BruCON's long-running Westvleteren beer tradition, referenced directly in the firmware's embedded map image assets.

The hardware and firmware are open source under CERN-OHL-P, with the artwork separately licensed CC/NA by Ray Harvey. The maker's README documents two fabrication mistakes present in the boards as actually handed out: a missing VBAT trace to the sensor/backlight/LED section, and a keyed-connector footprint mismatch versus the part referenced in the KiCad documentation, both requiring a bodge wire to fix. No information was found on price, quantity produced, or exact distribution method (sold vs. included with registration), and no photographs of the assembled badge were located — only PCB design files and cropped silkscreen-layer renders.
