---
title: BSides Perth 2018 NodeMCU badge
id: bsides-perth-2018-bsides-perth-2018-nodemcu-badge
layout: badge
parent: BSides Perth 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-perth-2018
year: 2018
makers:
- name: BSides Perth
summary: A handmade conference badge built around a NodeMCU ESP8266 module driving a small TFT display, given to delegates of BSides Perth 2018.
functions: Renders JPEG images and status text on a TFT screen over SPI, connects to Wi-Fi, and fades a status LED; firmware hides a CTF-style flag (flag{fladge_on_the_badge}) for a badge-hacking challenge.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - ctf
tech:
  mcu: ESP8266 (NodeMCU)
  leds:
    count: 1
    type: null
    note: single status LED on GPIO D8, PWM-faded
  display: TFT LCD (ILI9163C driver)
  connectivity:
  - wifi
  battery: null
  sao_version: none
get_one:
  price: free
  price_usd: 0
  quantity: '300+ (given to delegates)'
  availability: free
  distribution:
  - free_drop
  where: Given to BSides Perth 2018 delegates as part of the standard con swag (with a t-shirt, beanie, and tool kit).
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/BsidesPerth/Badge-2018
  eda_tool: null
links:
- label: github.com/BsidesPerth/Badge-2018
  url: https://github.com/BsidesPerth/Badge-2018
  kind: repo
- label: Australian Cyber Security Magazine - BSidesPerth 2018 podcast series
  url: https://australiancybersecuritymagazine.com.au/bsidesper-2018-podcast-series-bsidesperth/
  kind: article
- label: 'sudosammy/BSides-Badge-CO2-Monitor (badge reused as a CO2 monitor)'
  url: https://github.com/sudosammy/BSides-Badge-CO2-Monitor
  kind: repo
images: []
contact: {}
notes:
- Handmade NodeMCU ESP8266 Wi-Fi badge given to BSides Perth 2018 delegates with an associated badge-hack competition; source published on GitHub. Found by the event-year sweep, task bsides-canberra.
- 'Sweep entry title matched the maker''s own naming; no title correction needed.'
status: released
sources:
- kind: url
  url: https://github.com/BsidesPerth/Badge-2018
  title: BSides Perth 2018 NodeMCU badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-canberra); event read as ''BSides Perth 2018''.'
- kind: url
  url: https://github.com/BsidesPerth/Badge-2018
  title: BsidesPerth/Badge-2018 (firmware source, BSides_Perth_2018v0.9.ino)
  accessed: '2026-09-10'
  note: 'Confirmed MCU (NodeMCU ESP8266), TFT display via TFT_ILI9163C library over SPI, single PWM LED on D8, WiFi libraries, JPEG rendering from SPIFFS, and an embedded CTF flag string; no README content or hardware/PCB design files present, only the Arduino sketch and bundled libraries.'
- kind: url
  url: https://australiancybersecuritymagazine.com.au/bsidesper-2018-podcast-series-bsidesperth/
  title: BSidesPer 2018 Podcast series #BSidesPerth - Australian Cyber Security Magazine
  accessed: '2026-09-10'
  note: 'Confirms over 300 delegates received the handmade NodeMCU ESP8266 badge as part of standard con swag alongside t-shirts, beanies, and tool kits (i.e. given away free, not sold).'
- kind: url
  url: https://github.com/sudosammy/BSides-Badge-CO2-Monitor
  title: sudosammy/BSides-Badge-CO2-Monitor
  accessed: '2026-09-10'
  note: 'Third-party project repurposing a BSides Perth 2018 badge into a CO2/temp/humidity monitor; corroborates the badge is a real ESP8266 + TFT board people actually hold, but is not itself a source for the original badge''s specs.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: No original photo of the badge itself was found (the con's own site and press coverage did not carry one, and the GitHub repo has no images); look.colors/shape and tech.battery are left empty because no source states them. Quantity is approximate, inferred from delegate count reported in press coverage, not a stated production number. A competing catalog site (badge.gallery) turned up in search results describing the same badge with very similar wording to this entry; not used as a source since it appears to be a mirror/aggregator rather than a primary account.
last_modified_date: '2026-09-10'
---

The BSides Perth 2018 badge was a handmade conference badge built around a NodeMCU ESP8266 development board driving a small SPI TFT display (via the TFT_ILI9163C library). It was given free to delegates as part of the standard con swag — alongside a t-shirt, beanie, and tool kit — to the more than 300 people who attended BSides Perth that year.

On the hardware side the badge is close to a bare NodeMCU: a single status LED on GPIO D8 is PWM-faded, and the TFT is wired directly to the module's SPI pins (documented as a comment block in the firmware source). The firmware renders JPEG images from the board's SPIFFS filesystem, connects to Wi-Fi, and buries a CTF-style flag string (`flag{fladge_on_the_badge}`) in the code, tying the badge to BSides Perth's badge-hacking competition that year.

Firmware for the badge is published on GitHub (BsidesPerth/Badge-2018) as a single Arduino sketch with its bundled libraries, but no PCB design files or a bill of materials were published alongside it — the "hardware" is essentially a wiring recipe for stock modules rather than a custom board. At least one delegate later repurposed a badge into a portable CO2/temperature/humidity monitor, which is corroborating (but not authoritative) evidence that real units exist in the wild.
