---
title: Cyberdeck SAO
id: supercon-2023-cyberdeck-sao
layout: badge
parent: Supercon 2023
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2023
year: 2023
makers:
- name: Tom Nardi
  url: https://hackaday.io/hacker/1022-tom-nardi
summary: A Simple Add-On built for Hackaday Supercon 2023 that celebrates real-life cyberdecks, pairing an ATtiny3224 with a 0.91-inch 128x32 SSD1306 OLED that scrolls cyberpunk text including passages from Neuromancer.
functions: Scrolls text on the OLED, including passages from William Gibson's Neuromancer broken into strings by a Python script; a side-mounted tactile button drives interaction; four reverse-mounted LEDs (red, white, blue, green) light the underside of the board.
look:
  colors: []
  shape: cyberdeck (miniature keyboard-and-screen deck)
  themes:
  - cyberpunk
  - retro computer
tech:
  mcu: ATtiny3224
  leds:
    count: 4
    type: reverse-mount
    note: 1206 LEDs in red, white, blue, and green mounted on the back of the PCB
  display: 0.91" 128x32 SSD1306 OLED
  connectivity: []
  battery: powered by host badge
  sao_version: v1
get_one:
  price: free
  price_usd: null
  quantity: '30'
  availability: free
  distribution:
  - free_drop
  where: Handed out at Hackaday Supercon 2023 in Pasadena; 30 units built and flashed.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/192676-cyberdeck-sao
  url: https://hackaday.io/project/192676-cyberdeck-sao
  kind: hackaday
  archived: https://web.archive.org/web/20260417123924/https://hackaday.io/project/192676-cyberdeck-sao
images:
- file: assets/images/badges/supercon-2023/cyberdeck-sao/15790e79a0.jpg
  source: https://hackaday.io/project/192676-cyberdeck-sao
  credit: Tom Nardi
  caption: The Cyberdeck SAO, a miniature cyberdeck-styled Simple Add-On with OLED display
  archived: https://web.archive.org/web/20260417123924/https://hackaday.io/project/192676-cyberdeck-sao
- file: assets/images/badges/supercon-2023/cyberdeck-sao/e2b6c31967.jpg
  source: https://hackaday.io/project/192676-cyberdeck-sao
  credit: Tom Nardi
  caption: A batch of 30 assembled Cyberdeck SAOs laid out before Supercon 2023
  archived: https://web.archive.org/web/20260417123924/https://hackaday.io/project/192676-cyberdeck-sao
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/192676-cyberdeck-sao
  title: Cyberdeck SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260417123924/https://hackaday.io/project/192676-cyberdeck-sao
- kind: url
  url: https://hackaday.io/project/192676-cyberdeck-sao
  title: Cyberdeck SAO
  accessed: '2026-09-07'
  note: Confirmed maker (Tom Nardi), event/year (Supercon 2023, Pasadena), MCU (ATtiny3224), display (0.91" 128x32 SSD1306 OLED), 4 reverse-mount LEDs, side tact button, 4-pin SAO header, Neuromancer text scroller written in a Python-generated string format, 30 units built and given away free, no open-source files or repo published on the project page.
  archived: https://web.archive.org/web/20260417123924/https://hackaday.io/project/192676-cyberdeck-sao
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: No GitHub/repo, Gerber, or BOM links found on the project page, so make_your_own fields are left empty. PCB solder-mask color and exact SAO pin count (4 vs 6) not stated on the page, so look.colors and a firm sao_ports figure are left empty; sao_version set to v1 (4-pin) based on the "4-pin SAO header" wording in the page summary. No press coverage or storefront found beyond the Hackaday.io project page itself.
last_modified_date: '2026-09-07'
---

The Cyberdeck SAO is a Simple Add-On that Tom Nardi built for Hackaday Supercon 2023 in Pasadena, shaped like a tiny cyberdeck: a keyboard-textured PCB with a fold-out carrying handle and a 0.91-inch 128x32 SSD1306 OLED standing in for the deck's screen. An ATtiny3224 drives the display, scrolling cyberpunk-flavored text — including passages from William Gibson's Neuromancer, chopped into short strings by a Python script Nardi wrote for the job. A side-mounted tactile button lets the wearer step through the display, and four reverse-mounted LEDs (red, white, blue, and green) light up the underside of the board. It draws power through the standard SAO header from whatever main badge it plugs into.

Nardi built and flashed 30 of them for Supercon 2023, and handed them out at the event rather than selling them. The Hackaday.io project page is the only public source found for it; no GitHub repository, Gerbers, or BOM appear to be linked from that page, and no separate press coverage or storefront listing turned up.
