---
title: CactusCon 2018 Badge (CactusCoin)
id: cactuscon-2018-cactuscon-2018-paid-badge
layout: badge
parent: CactusCon 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cactuscon-2018
year: 2018
makers:
- name: Erik Wilson
  url: https://github.com/erikwilson
summary: 'The electronic badge given to paid CactusCon 2018 (CactusCon 7) attendees, built around a TTGO LoRa OLED ESP32 module and nicknamed "CactusCoin" by its designer.'
functions: 'Six capacitive touch "buttons" driven from four sensor pads, a Wi-Fi access point with captive portal and websockets, LoRa (433MHz) radio, and firmware-hidden secrets/puzzles. An optional "bot" upgrade adds a motor driver, wheels, and motors for a driveable add-on, with joystick control from a companion badge.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - puzzle
  - radio
tech:
  mcu: ESP32
  leds: null
  display: 0.96" OLED
  connectivity:
  - wifi
  - bluetooth
  - lora
  battery: 18650 Li-ion
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: 'Given to attendees who paid for registration at CactusCon 2018 (September 28-29, 2018, Mesa Convention Center); paid registrations reportedly sold out before the event.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/erikwilson/CactusCon7
  firmware_url: https://github.com/erikwilson/CactusCon7
  eda_tool: null
links:
- label: badge.gallery/badges/cactuscon-2018-paid-badge
  url: https://badge.gallery/badges/cactuscon-2018-paid-badge
  kind: website
- label: erikwilson/CactusCon7 (GitHub)
  url: https://github.com/erikwilson/CactusCon7
  kind: repo
  archived: false
- label: 'CactusCon 2018 badge thread (HeatSync Labs Google Group)'
  url: https://groups.google.com/g/heatsynclabs/c/rIPB8tivkY0
  kind: social
  archived: false
images:
  - file: assets/images/badges/cactuscon-2018/cactuscon-2018-paid-badge/168b50ba52.jpg
    source: "https://github.com/erikwilson/CactusCon7"
    credit: "Erik Wilson"
    caption: "CactusCoin badge board, TTGO LoRa OLED ESP32"
  - file: assets/images/badges/cactuscon-2018/cactuscon-2018-paid-badge/dc9030a347.png
    source: "https://github.com/erikwilson/CactusCon7"
    credit: "Erik Wilson"
    caption: "CactusCoin badge with spare parts"
contact: {}
notes:
- 'Sweep-imported title was "CactusCon 2018 Paid Badge," describing only a paid-registration entitlement with no confirmed hardware; research confirmed it was in fact an electronic badge, designer-nicknamed "CactusCoin", documented in the designer''s own GitHub repo (CactusCon7). Title updated to reflect this; CactusCon''s numbering has this event as "CactusCon 7."'
- 'License for the hardware/firmware is not stated in the repo; treated as open_source: partial (source published, no explicit license).'
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/cactuscon-2018-paid-badge
  title: CactusCon 2018 Paid Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-layerone); event read as ''CactusCon 2018''.'
- kind: url
  url: https://github.com/erikwilson/CactusCon7
  title: 'erikwilson/CactusCon7: CactusCoin badge for CactusCon 2018'
  accessed: '2026-09-10'
  note: "Maker's own repo; confirms hardware (TTGO LoRa OLED ESP32, capacitive buttons, LoRa/WiFi/BLE, 0.96\" OLED, 18650 battery), firmware, parts list, and README image explicitly captioned \"CactusCon 2018\"."
- kind: url
  url: https://groups.google.com/g/heatsynclabs/c/rIPB8tivkY0
  title: 'CactusCon 2018 badge thread - HeatSync Labs Google Group'
  accessed: '2026-09-10'
  note: 'Confirms Erik Wilson designed the badge, that it was solder-it-yourself and tied to an on-badge game, and that it was built/flashed at HeatSync Labs before the event.'
- kind: url
  url: https://kiltedhacker.com/cactuscon-2018/
  title: 'CactusCon 2018 - Kilted Hacker (search snippet)'
  accessed: '2026-09-10'
  note: 'Page itself was unreachable (site refuses connections), but a search snippet quotes it describing a hardware hacking village where attendees could "assemble and mod your electronic badge" and that paid registrations "ran out" — corroborates limited/sold-out availability.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Core facts (maker, hardware, event) confirmed via the designer''s own GitHub repo and a contemporaneous HeatSync Labs community thread. Price and exact quantity produced are not stated anywhere found and are left empty. The kiltedhacker.com blog post could not be directly fetched (connection refused) so only its search-snippet text was used, for the sold-out/limited-availability detail only.'
last_modified_date: '2026-09-10'
---

CactusCon 2018 — the seventh CactusCon, held September 28-29, 2018 at the Mesa Convention Center — issued an electronic badge to attendees who paid for registration, rather than to everyone who attended for free. Designer Erik Wilson built the badge around a TTGO LoRa OLED ESP32 module, giving it a 0.96" OLED display, Wi-Fi, Bluetooth, and a 433 MHz LoRa radio on top of the ESP32's dual-core processor. Six capacitive touch "buttons" are driven from just four sensor pads, and the badge runs on a single 18650 lithium-ion cell. Wilson nicknamed the design "CactusCoin."

Beyond basic blinky/radio functions, the badge shipped with an access point, a captive portal, websocket support, and firmware-hidden secrets, tying into a badge-based game for attendees who built their own units. HeatSync Labs, the Mesa hackerspace behind much of CactusCon's hardware village, hosted build-and-flash sessions in the two nights before the con, and an optional "bot" upgrade let owners bolt on a motor driver, wheels, and motors for a small driveable add-on, steerable from a joystick on a companion badge.

Paid badges were limited: contemporaneous accounts describe registrations selling out before the event, and community members were still asking for the schematics and firmware after the fact. The firmware and a parts list are published in Wilson's `CactusCon7` GitHub repository, though no explicit open-source license is stated.

## Make your own

Erik Wilson's [CactusCon7 repository](https://github.com/erikwilson/CactusCon7) has the Arduino-based firmware and a full parts list (TTGO LoRa OLED ESP32 module, female headers, an 18650 battery holder and switch, plus the optional motor/wheel/joystick kit for the "bot" upgrade). No PCB design files (Gerbers/schematics) were found in the repo or linked from it — the build instructions center on the off-the-shelf TTGO module rather than a custom board.
