---
title: Hackbutt v3 wifi testing badge
id: dc31-hackbutt-v3-wifi-testing-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: rot13labs / C0ldbru
  url: https://rot13labs.com
summary: A wifi deauthentication testing badge from rot13labs (C0ldbru) built around an ESP8266 running a custom fork of the ESP8266 Deauther firmware, with an OLED screen, RGB lighting, and a swappable antenna.
functions: Wifi deauth, beacon, and probe-request attacks via a custom ESP8266 Deauther fork, controllable from the onboard OLED/buttons or a web-based interface; usable standalone or as a networked controller; serial headers and flash/reset buttons for firmware updates.
look:
  colors: []
  shape: null
  themes:
  - security
  - radio
  form_factor: pcb badge
tech:
  mcu: ESP8266
  leds:
    count: null
    type: RGB
    note: RGB lighting options mentioned in the Tindie listing; count not specified.
  display: small OLED
  connectivity:
  - wifi
  battery: LiPo 500 mAh
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: 'Tindie listing checked 2026-09-07: marked "Product Retired - No longer available for sale."'
  distribution:
  - purchase
  where: Sold by rot13labs (C0ldbru) on Tindie; listing is now retired.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/c0ldbru/esp8266_deauther_hackbutt
  eda_tool: null
  notes: The Tindie listing says open source code/documentation is available on GitHub, matching the esp8266_deauther_hackbutt firmware fork found for the sibling entry. No schematic, Gerbers, or BOM were found.
links:
- label: www.tindie.com/products/rot13labs/hackbutt-v3-wifi-testing-badge
  url: https://www.tindie.com/products/rot13labs/hackbutt-v3-wifi-testing-badge/
  kind: store
- kind: repo
  label: esp8266_deauther_hackbutt firmware (GitHub)
  url: https://github.com/c0ldbru/esp8266_deauther_hackbutt
images:
- file: assets/images/badges/dc31/hackbutt-v3-wifi-testing-badge/df2292b5ba.png
  source: "https://www.tindie.com/products/rot13labs/hackbutt-v3-wifi-testing-badge/"
  credit: "rot13labs"
  caption: "Hackbutt v3 wifi testing badge, as listed on Tindie"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
- 'This appears to be the same badge as the existing entry dc31-hackbutt-v-3-wifi-testing-badge (same maker, same "Hackbutt v3", ESP8266, OLED, deauther-fork firmware). Treated as a likely duplicate; see research.notes.'
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/rot13labs/hackbutt-v3-wifi-testing-badge/
  title: Hackbutt v3 wifi testing badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc31 (already has an entry: dc31-hackbutt-v-3-wifi-testing-badge)''.'
- kind: url
  url: https://www.tindie.com/products/rot13labs/hackbutt-v3-wifi-testing-badge/
  title: Hackbutt v3 WiFi Testing Badge (Tindie, rot13labs)
  accessed: '2026-09-07'
  note: Listing confirms maker (rot13labs / Dennis, Gainesville FL), ESP8266 chip, OLED screen, RGB lighting, swappable antenna, LiPo 1000mAh + USB-C charging, custom ESP8266 Deauther fork with web UI, and that the product is retired/no longer for sale. Price and quantity not shown since retired.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Likely a duplicate of dc31-hackbutt-v-3-wifi-testing-badge: same title ("Hackbutt v3"), same maker (C0ldbru / rot13labs), same DEF CON 31 / 2023 timeframe, same ESP8266 + OLED + deauther-firmware description. The Tindie listing here adds details (RGB lighting, swappable antenna, LiPo 1000mAh + USB-C, retired status) not present on the other entry, which is why this entry was filled in rather than left blank, but the two should probably be merged by a human editor. Price and unit quantity were not found on the retired listing.'
last_modified_date: '2026-09-07'
---

The Hackbutt v3 is a wifi-testing badge sold by C0ldbru of rot13labs (Gainesville, FL) on Tindie, built around an ESP8266 running a custom fork of the popular ESP8266 Deauther firmware. It adds deauthentication, beacon, and probe-request attacks to a wearable badge, controllable either from an onboard OLED screen and buttons or through a web-based interface, and can run standalone or as a networked controller. The board includes serial headers and flash/reset buttons for updating firmware, RGB lighting, and a swappable antenna, and is powered by a 3.7V 1000 mAh LiPo battery charged over USB-C.

This listing appears to describe the same badge as the archive's existing entry for "Hackbutt v.3 wifi testing badge" (same maker, same DEF CON 31 / 2023 timeframe, same ESP8266 deauther-fork firmware), so the two entries likely belong to a single badge and should be reviewed for a merge. The Tindie page notes the product has since been retired and is no longer available for purchase; no price or production quantity was published.

## Make your own

The firmware is open source: the Tindie listing points to the same GitHub-hosted fork of the ESP8266 Deauther project used by the related entry ([esp8266_deauther_hackbutt](https://github.com/c0ldbru/esp8266_deauther_hackbutt)). No hardware design files (schematic, Gerbers, or BOM) were found published for the board itself.
