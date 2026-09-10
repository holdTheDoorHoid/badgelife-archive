---
title: BSides Canberra 2016 badge
id: bsides-canberra-2016-bsidescbrbadge2016-arduino-running-order-badge
layout: badge
parent: BSides Canberra 2016
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-canberra-2016
year: 2016
makers:
- name: Ingmar M. ("Iggy")
  url: https://github.com/BSidesCbr
summary: The delegate badge for BSides Canberra 2016, a red PCB badge built around a NodeMCU ESP8266 board and a 1.8" SPI TFT that joins the venue Wi-Fi to pull down tweets tagged #BSidesCbr.
functions: Connects to the "BSidesCTF" SSID and fetches tweets tagged #BSidesCbr from a small companion server, showing them alongside animated demo effects (sine/cosine-table graphics) on its color TFT.
look:
  colors:
  - red
  shape: rectangle
  themes:
  - security
  - hardware tool
tech:
  mcu: ESP8266 (NodeMCU, ESP-12E module)
  leds: null
  display: 1.8" SPI TFT (ST7735, 128x160)
  connectivity:
  - wifi
  battery: null
  sao_version: null
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Handed out to BSides Canberra 2016 delegates.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/BSidesCbr/BsidesCbrBadge2016
  firmware_url: https://github.com/BSidesCbr/BsidesCbrBadge2016
  eda_tool: KiCad
links:
- label: github.com/BSidesCbr/BsidesCbrBadge2016
  url: https://github.com/BSidesCbr/BsidesCbrBadge2016
  kind: repo
images:
  - file: assets/images/badges/bsides-canberra-2016/bsidescbrbadge2016-arduino-running-order-badge/c29843d9f6.jpg
    source: "https://github.com/BSidesCbr/BsidesCbrBadge2016/blob/master/badgepresso.pdf"
    credit: "Ingmar M. (\"Iggy\")"
    caption: "The finished red PCB badge, silkscreened \"BSIDES Canberra 2016\" with a Telstra sponsor logo and a 1.8\" TFT cutout."
  - file: assets/images/badges/bsides-canberra-2016/bsidescbrbadge2016-arduino-running-order-badge/bc639cc2a0.jpg
    source: "https://github.com/BSidesCbr/BsidesCbrBadge2016/blob/master/badgepresso.pdf"
    credit: "Ingmar M. (\"Iggy\")"
    caption: "Badge PCB with a NodeMCU ESP8266 board and 1.8\" SPI TFT module wired up during assembly."
contact: {}
notes:
- 'The discovery sweep titled this entry "BsidesCbrBadge2016 (Arduino running-order badge)" after the repo name; the maker''s own presentation calls it simply the BSides Canberra 2016 badge.'
status: released
sources:
- kind: url
  url: https://github.com/BSidesCbr/BsidesCbrBadge2016
  title: BsidesCbrBadge2016 (Arduino running-order badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-canberra); event read as ''BSides Canberra 2016''.'
- kind: url
  url: https://github.com/BSidesCbr/BsidesCbrBadge2016/blob/master/README.md
  title: BsidesCbrBadge2016 README
  accessed: '2026-09-10'
  note: Confirms the badge connects to the BSidesCTF SSID and pulls #BSidesCbr tweets from a companion server; repo has three parts (code generator, server, badge firmware).
- kind: url
  url: https://github.com/BSidesCbr/BsidesCbrBadge2016/blob/master/badgepresso.pdf
  title: "\"That #&@^! Badge!\" - BSides Canberra 2016 badge design presentation"
  accessed: '2026-09-10'
  note: Maker's own conference-talk slide deck. Confirms designer (Ingmar M., "Iggy"), hardware choice (NodeMCU ESP8266 + ST7735 1.8" SPI TFT, MCP23S17 GPIO expander, MCP3208 ADC, all optional), KiCad schematic (rev 1.20, dated 2016-02-09), that it was given away free, and shows photos of the finished red PCB with a Telstra sponsor logo.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Quantity made and any storefront/price beyond "free" were not stated anywhere found. No separate LICENSE file in the repo, so open_source is marked partial (code is public on GitHub but no explicit license or Gerber/BOM files were found) rather than a confirmed "yes". LEDs and battery are not mentioned in the schematic or slides, so left empty. Buttons (5x tactile) exist but are not modeled in the schema's tech fields.
last_modified_date: '2026-09-10'
---

The BSides Canberra 2016 delegate badge is a red PCB badge designed by an organizer known as "Iggy" (Ingmar M.), built around a NodeMCU ESP8266 board wired to a 1.8" SPI TFT (ST7735 driver, 128x160). Per the maker's own conference talk ("That #&@^! Badge!"), the brief from a fellow organizer, Kylie, was simply "I want WiFi," and the design grew from there into a badge that joins the venue's "BSidesCTF" Wi-Fi network and pulls down tweets tagged #BSidesCbr from a small companion server, alongside animated demo effects driven by sine/cosine lookup tables. Five tactile buttons (up/down/left/right/select) are on the board, and the schematic includes optional, jumper-selectable expansion via an MCP23S17 GPIO expander and an MCP3208 analog-to-digital converter for hobbyists who want to hack on the extra I/O.

The badge was given away free to delegates. Its firmware was written in the Arduino IDE against the ESP8266 core, and the hardware was laid out in KiCad; both the firmware and a KiCad-generated schematic PDF are published in the project's GitHub repository, though no explicit open-source license or Gerber/BOM files accompany them. The board carries a Telstra logo, indicating conference sponsorship. The event-year discovery sweep filed this entry under the repository's name, "BsidesCbrBadge2016 (Arduino running-order badge)," but the badge itself is not named that anywhere in the maker's own materials.

## Make your own

The GitHub repository (github.com/BSidesCbr/BsidesCbrBadge2016) holds three parts: a "BadgeCodeGenerator" that produces the sine/cosine lookup tables and a compressed background image as a C header, a small server component that scrapes Twitter for the #BSidesCbr hashtag and serves it as text, and the Arduino sketch flashed to the badge itself (which needs the SSID "BSidesCTF" present to get any network functionality). The repo also bundles the Adafruit GFX and ST7735 libraries and the MCP23S17 library it depends on, along with a KiCad schematic PDF (`badgev1.pdf`) and the maker's own design-and-build slide deck (`badgepresso.pdf`), which documents the full bring-up process including IDE setup for the ESP8266 Arduino core.
