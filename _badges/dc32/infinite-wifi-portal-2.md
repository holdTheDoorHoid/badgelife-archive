---
title: Infinite WiFi Portal
id: dc32-infinite-wifi-portal-2
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Whiskey Pirate Crew (not badgelife)
  url: https://whiskeypirates.com
  role: hardware (built by "True")
- name: Aask
  url: https://aask.ltd
  role: concept and firmware
summary: A hand-held infinity-mirror medallion made for DEF CON 32 that doubles as a clock and shows the number of nearby WiFi networks on its LED ring.
functions: Outer LED ring ticks like a clock's second hand at a default 60 BPM; the ring's lit length shows the current count of visible WiFi networks; the badge auto-dims and powers off its LED driver when tilted face-down and relights when turned upright; a rear button is present but left open for owners to program themselves; connecting to WiFi and an MQTT broker lets an owner remotely change the tick speed and a scrolling banner message.
look:
  colors:
  - black
  - multicolor
  shape: circle
  themes:
  - jewelry
  - wearable
  form_factor: medallion
tech:
  mcu: ESP32-N1-Mini
  leds:
    count: 80
    type: IS31FL3729-driven matrix (42 white, 1 green, 1 red) plus 36 neopixel-style RGB
    note: The 44-LED matrix forms the infinity-mirror face; the 36 RGB LEDs are separate, data-pin driven.
  display: LED matrix 3x15
  connectivity:
  - wifi
  inputs:
  - buttons
  - accelerometer
  battery: null
  sao_version: none
get_one:
  price: $120.00
  price_usd: 120.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Made for and distributed at DEF CON 32 (Las Vegas, Aug 2024) by the makers directly; no ongoing storefront listing was found.
make_your_own:
  open_source: yes
  hardware_url: https://git.trueserve.org/trueControl/dc32-infinite-wifi-portal
  firmware_url: https://github.com/Aask42/DC32_Infinite_Wifi_Portal
  eda_tool: null
  license: null
  notes: Firmware is MicroPython, flashed with the repo's own auto_flash.sh/auto_flash.ps1 scripts and a custom MicroPython build (needed for non-blocking WiFi scanning); a Thonny-based workflow is documented for editing main.py directly. No license file is published; the maker just calls it "open-source on GitHub."
links:
- label: Infinite WiFi Portal firmware (GitHub)
  url: https://github.com/Aask42/DC32_Infinite_Wifi_Portal
  kind: repo
- label: Infinite WiFi Portal hardware (trueserve Git)
  url: https://git.trueserve.org/trueControl/dc32-infinite-wifi-portal
  kind: repo
- label: aask.ltd/iwp (project page)
  url: https://aask.ltd/iwp
  kind: website
- label: trueControl BASIC - DC32 badge index
  url: https://basic.truecontrol.org/wp-badges/
  kind: doc
- label: Whiskey Pirates (crew site)
  url: https://whiskeypirates.com
  kind: website
images:
  - file: assets/images/badges/dc32/infinite-wifi-portal-2/9ff2a8bf36.jpg
    source: "https://github.com/Aask42/DC32_Infinite_Wifi_Portal"
    credit: "Aask / True"
    caption: "The Infinite WiFi Portal medallion, worn on a retro-reflective lanyard"
  - file: assets/images/badges/dc32/infinite-wifi-portal-2/d433372a37.png
    source: "https://github.com/Aask42/DC32_Infinite_Wifi_Portal"
    credit: "Aask / True"
    caption: "The infinity-mirror LED ring and matrix face of the badge"
contact: {}
notes:
- Sheet listed the maker as "Whiskey Pirate Crew (not badgelife)"; the badge was actually a two-person collaboration between "True" (trueControl, of the Whiskey Pirates) who built the hardware, and Aask (aask.ltd), who wrote the firmware and led the concept.
status: released
sources:
- kind: sheet
  event: dc32
  row: 117
  updated: ''
- kind: url
  url: https://basic.truecontrol.org/
  title: trueControl BASIC
  accessed: '2026-09-07'
  note: Current site index confirms the badge's existence and title, and links to the (now-404) dc32/infinite-wifi page and the crew's site.
- kind: url
  url: http://web.archive.org/web/20240910151951/https://basic.truecontrol.org/database/dc32/infinite-wifi/
  title: "Infinite WiFi Portal - trueControl BASIC (Wayback Machine, Sep 2024)"
  accessed: '2026-09-07'
  note: Archived version of the badge's own page, live during DEF CON 32; links to both the hardware and firmware repos and names the two makers ("true" for hardware, "Aask and crew" for code).
- kind: url
  url: https://github.com/Aask42/DC32_Infinite_Wifi_Portal
  title: "GitHub - Aask42/DC32_Infinite_Wifi_Portal"
  accessed: '2026-09-07'
  note: Primary source for functions, hardware components (MCU, LED driver, sensors), firmware/flashing process, and maker credits. Also the source of both saved images.
- kind: url
  url: https://git.trueserve.org/trueControl/dc32-infinite-wifi-portal
  title: "trueControl/dc32-infinite-wifi-portal - trueserve Git"
  accessed: '2026-09-07'
  note: Confirmed the hardware repo is still live and belongs to trueControl; page itself carries no further written detail beyond the repo file listing.
- kind: url
  url: https://aask.ltd/iwp
  title: "Infinite WiFi Portal - aask.ltd"
  accessed: '2026-09-07'
  note: Confirms Aask (calling the outfit "Aask Labs") as co-maker and describes it as the fifth entry in an ongoing "Infinity Mirror" product series; page is an unfinished writeup with no price/quantity/availability info.
- kind: url
  url: https://hackaday.com/2021/08/06/hands-on-whiskey-pirates-dc29-hardware-badge-blings-with-risc-v/
  title: "Hands-On: Whiskey Pirates DC29 Hardware Badge Blings With RISC-V"
  accessed: '2026-09-07'
  note: Background source confirming "Whiskey Pirates" as a DEF CON badge-making crew that describes itself as "adamantly not 'badgelife'" (matching the sheet's maker note) and led by trueControl ("true"); no DC32-specific content.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    This is the same physical badge as dc32-infinite-wifi-portal (that entry
    credits it only to "Aask Labs"; this one, from a separate sheet row,
    credits "Whiskey Pirate Crew (not badgelife)" - both are correct, it was
    a two-person collaboration). Web search (WebSearch tool) was unavailable
    for this task (session budget exhausted) and live search engines
    (Google, Bing, DuckDuckGo) all blocked or failed automated fetches; the
    Wayback Machine's archived copy of the badge's own now-404 project page
    was the source that unlocked the hardware/firmware repo links and maker
    attribution. Price ($120, from the sheet) could not be independently
    confirmed - no live storefront listing was found for this item, and
    quantity made, exact battery/power source, and open-source license are
    not stated anywhere the makers published. The aask.ltd/iwp page is
    itself an unfinished writeup and did not add facts beyond what the
    GitHub README already gave.
last_modified_date: '2026-09-07'
---

The Infinite WiFi Portal is a hand-held infinity-mirror medallion made for DEF CON 32 (Las Vegas, August 2024), worn on a retro-reflective lanyard. It was a two-person build: "True," of the Whiskey Pirates crew ("adamantly not 'badgelife'"), designed and built the hardware, while Aask (aask.ltd) wrote the firmware and led the concept - the fifth badge in Aask's ongoing "Infinity Mirror" series of projects. An ESP32-N1-Mini drives an IS31FL3729 LED matrix (42 white, 1 green, 1 red LED in a 3x15 grid) behind the mirrored face, plus 36 separate RGB LEDs, alongside an accelerometer and a light sensor.

Functionally, the outer ring of the mirror ticks like a clock's second hand at a default 60 beats per minute, while the number of lit LEDs on that ring reflects how many WiFi networks the badge currently sees nearby. Tilting the badge face-down auto-dims and powers off the LED driver to save power; turning it back upright wakes it. A button on the back is left unprogrammed for owners to customize. The firmware is MicroPython (a custom build is required for its non-blocking WiFi scanning) and can be reconfigured over WiFi and MQTT to change the tick speed or a scrolling banner, or edited directly over USB serial with Thonny.

## Make your own

Both halves of the project are published: hardware documentation lives in True's trueserve Git repo, and the firmware (plus flashing scripts for Windows and Unix) is on Aask's GitHub. To flash a device, the repo's `auto_flash.sh` (or `auto_flash.ps1` on Windows) installs the required custom MicroPython build via esptool; from there, `main.py` can be edited directly in Thonny to change the BPM or banner text, or controlled remotely by configuring WiFi credentials and an MQTT broker (the makers suggest HiveMQ's free tier) in `CONFIG/WIFI_CONFIG.py`.
