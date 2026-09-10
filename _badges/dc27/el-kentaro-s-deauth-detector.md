---
title: El Kentaro's Deauth Detector
id: dc27-el-kentaro-s-deauth-detector
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: other
event: dc27
year: 2019
makers:
- name: El Kentaro
  url: https://twitter.com/elkentaro
summary: A handheld ESP-based Wi-Fi deauthentication monitor by El Kentaro, showing live status on an OLED, a running deauth-frame count on a 7-segment display, and a NeoPixel matrix, demoed on Hak5 at DEF CON 27.
functions: 'Watches for 802.11 deauthentication frames in the air, shows a "looking for DEAUTH attacks" status on its OLED, tallies detected deauth frames on a 4-digit 7-segment counter, and lights a NeoPixel LED matrix as an indicator.'
look:
  colors:
  - black
  shape: null
  themes:
  - security
  - radio
  - hardware tool
  - measurement
tech:
  mcu: null
  leds:
    count: null
    type: NeoPixel
    note: 'A NeoPixel LED matrix is visible on the board; video tags also list "arduino" and "neopixel", but no specific MCU or LED count is confirmed by any source.'
  display: OLED + 7-segment
  connectivity:
  - wifi
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.youtube.com/watch?v=daLhn8lIbGo
  url: https://www.youtube.com/watch?v=daLhn8lIbGo
  kind: video
- label: hackaday.com/2019/08/08/this-wifi-spoofing-syringe-is-for-external-use-only
  url: https://hackaday.com/2019/08/08/this-wifi-spoofing-syringe-is-for-external-use-only/
  kind: article
images:
- file: assets/images/badges/dc27/el-kentaro-s-deauth-detector/62e55256b7.jpg
  source: "https://www.youtube.com/watch?v=daLhn8lIbGo"
  credit: "Hak5"
  caption: "El Kentaro's deauth detector: an ESP-based board with an OLED status display, a 7-segment deauth-frame counter, and a NeoPixel matrix"
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- 'Sweep''s source line labeled the entry only with the video URL; the video itself is a Hak5 segment ("DEF CON 27: El Kentaro''s Deauth Detector - Hak5 2601") in which El Kentaro shows the device rather than a maker-authored project page.'
status: released
sources:
- kind: url
  url: https://www.youtube.com/watch?v=daLhn8lIbGo
  title: El Kentaro's Deauth Detector
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://www.youtube.com/watch?v=daLhn8lIbGo
  title: 'DEF CON 27: El Kentaro''s Deauth Detector - Hak5 2601'
  accessed: '2026-09-10'
  note: 'Confirmed the device is real and shown at DEF CON 27 (2019); video keywords tag "arduino" and "neopixel", and description says only that El Kentaro "joins us at DEF CON 27 to share his new hardware hacks" (no further build details in the description). The video thumbnail itself is a photo of the device: an ESP-family board, an OLED reading a "looking for DEAUTH attacks"-style status, a 4-digit 7-segment counter, and a lit NeoPixel matrix.'
- kind: url
  url: https://hackaday.com/2019/08/08/this-wifi-spoofing-syringe-is-for-external-use-only/
  title: This WiFi Spoofing Syringe Is For External Use Only
  accessed: '2026-09-10'
  note: 'Passing mention only: describes a separate El Kentaro project (a syringe-housed WiFi packet injector) and references "his DEAUTH ''bling'' necklace we saw at DEF CON 26" as an example of his prior con gadgets -- that necklace is a different, non-electronic item already catalogued as dc26-deauth-badge, and its own research notes independently flag this DC27 device as a distinct, later, electronic project. No further technical detail on this entry''s device was found here.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-10'
  notes: >-
    Confirmed real via a Hak5 video segment filmed at DEF CON 27, whose thumbnail
    is an actual photo of the device (ESP-family board, OLED, 7-segment counter,
    NeoPixel matrix). No maker-authored project page, GitHub repo, Hackaday.io page,
    Medium post, or storefront listing for this specific device could be reached --
    a plausible maker Medium post ("The WiFi Doctor Will See You Now") returned an
    HTTP 403 from Cloudflare and could not be read. As a result mcu, LED count,
    price, quantity, and availability are unconfirmed and left empty. This is a
    different item from the jewel-encrusted, non-electronic dc26-deauth-badge (also
    by El Kentaro); do not merge the two.
last_modified_date: '2026-09-10'
---

El Kentaro's Deauth Detector is a handheld electronic gadget the maker showed off at DEF CON 27 (2019), featured in a Hak5 video segment recorded at the con. It watches for 802.11 deauthentication frames in the air and reports on them in real time: an OLED screen reads a status message along the lines of "looking for DEAUTH attacks," a 4-digit 7-segment display keeps a running count of frames seen, and a NeoPixel LED matrix lights up as an additional visual indicator. The visible hardware is an ESP-family module board paired with a second board carrying the display and LED matrix, built into a small 3D-printed enclosure.

Beyond the video itself, coverage is thin: the Hak5 video's own description gives no build details, and a Hackaday article about a different El Kentaro project (a WiFi packet injector built into a syringe) only namechecks his earlier "DEAUTH bling necklace" from DEF CON 26 -- a distinct, non-electronic piece already catalogued separately in this archive. No maker-authored write-up, repository, or storefront for this specific detector could be located; a likely maker's-own account of the build on Medium returned a Cloudflare block rather than content. Absent that, chip, LED count, price, quantity, and availability are unknown.
