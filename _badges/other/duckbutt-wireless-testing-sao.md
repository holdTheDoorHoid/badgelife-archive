---
title: Duckbutt Wireless Testing SAO
id: other-duckbutt-wireless-testing-sao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 0
makers:
- name: rot13labs
  url: https://rot13labs.com/
summary: A rubber-duck-shaped SAO from rot13labs that spins up its own "duckbutt" WiFi network and web UI for wireless scanning, deauth, and probe attacks.
functions: Creates a WiFi access point named "duckbutt"; connecting to it exposes a management web UI for wireless scanning, deauthentication attacks, and probe attacks. Has a removable antenna connector for swapping in a larger or directional antenna.
look:
  colors:
  - red
  - black
  shape: duck
  themes:
  - duck
  - radio
  - security
tech:
  mcu: ESP8266
  leds: null
  display: null
  connectivity:
  - wifi
  battery: null
  sao_version: null
get_one:
  price: "$45"
  price_usd: 45
  quantity: "micro batch of 5"
  availability: sold_out
  availability_note: "Tindie listing showed 'oos' (out of stock) / retired as of 2026-09-07"
  distribution:
  - purchase
  where: Sold on Tindie by rot13labs in a micro batch of five units.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/spacehuhn/esp8266_deauther
  eda_tool: null
links:
- label: www.tindie.com/products/rot13labs/limited-duckbutt-wireless-testing-sao
  url: https://www.tindie.com/products/rot13labs/limited-duckbutt-wireless-testing-sao/
  kind: store
- label: rot13labs.com
  url: https://rot13labs.com/
  kind: website
- label: "rot13labs - setup - Duckbutt"
  url: https://rot13labs.com/setup/duckbutt
  kind: doc
images:
- file: assets/images/badges/other/duckbutt-wireless-testing-sao/d7364e1081.png
  source: "https://www.tindie.com/products/rot13labs/limited-duckbutt-wireless-testing-sao/"
  credit: "rot13labs"
  caption: "Duckbutt Wireless Testing SAO, red variant"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/rot13labs/limited-duckbutt-wireless-testing-sao/
  title: Duckbutt Wireless Testing SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''unclear''.'
- kind: url
  url: https://rot13labs.com/setup/duckbutt
  title: "rot13labs - setup - Duckbutt"
  accessed: '2026-09-07'
  note: "Maker's setup page for the Duckbutt; gave Arduino/board-package setup instructions (no MCU or event details confirmed here that agreed with the Tindie listing)."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    The Tindie listing (accessed 2026-09-07, using the Wayback-cached description text) says this is
    a "duckbutt wireless testing SAO" running the "esp8266 deauther" firmware from spacehuhn on an
    ESP8266, with a removable antenna and a serial header for custom firmware. It requires at least
    3.3V and will not run on badges powered only by a CR2032. The listing states "The duckbutts listed
    here are the last two remaining SAOs from the micro batch of five of these that I made. I might
    make another small batch of them for DEFCON 31" -- this line is dated before DEF CON 31 (2023) and
    implies the original batch of five predates DC31 rather than being made for it, so the event was
    left as "other" rather than set to dc31; a maker tweet from May 2023 (c0ldbru/rot13labs) does show
    a "sneak peek" of DEF CON 31 badgelife, but it is not confirmed that image was this SAO rather than
    other rot13labs badges shown alongside it. Price ($45) and out-of-stock status came from page
    metadata. LED count/type and display were not mentioned anywhere and were left empty. A separate,
    similarly named rot13labs product, the "Hackbutt" (ESP8266 badUSB / wifi testing badge), turned up
    in search results and is a different item -- flagged separately, not merged into this entry.
last_modified_date: '2026-09-07'
---

The Duckbutt Wireless Testing SAO is a rubber-duck-shaped add-on made by rot13labs, a small Florida-based hardware shop known for hacker-tool SAOs and badges. Plugging it in and connecting to the WiFi network it broadcasts (named "duckbutt") opens a management web UI that can run wireless scans, deauthentication attacks, and probe attacks -- built around an ESP8266 running spacehuhn's open-source "esp8266 deauther" firmware. A removable antenna connector lets an owner swap in a larger or directional antenna, and exposed reset/flash buttons plus a serial header make it easy to reflash with custom firmware.

Only five of these were made in the original micro batch, sold through rot13labs' Tindie store for $45 each; the listing was already down to its last two units when checked and the product is now retired/out of stock. The maker noted they might make a further small batch for DEF CON 31, but it isn't confirmed whether this batch was itself made for that specific event or an earlier one, so no specific con could be pinned down with confidence.

## Make your own

Firmware is spacehuhn's open-source esp8266_deauther project (https://github.com/spacehuhn/esp8266_deauther); no hardware files (schematic/Gerbers) were published or found for the SAO board itself.
