---
title: ror3-sao — Reali7y Over Run
id: dc33-ror3-sao-reali7y-over-run
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc33
year: 2025
makers:
- name: Reali7y Over Run
  url: https://reali7y-over.run/
summary: 'An SAO given out to participants of the REALI7Y OVERRUN contest at DEF CON 33, with open firmware that players could hack to earn contest points.'
functions: 'Runs contest-supplied firmware driving LED patterns via two onboard buttons; part of the REALI7Y OVERRUN storyline contest, participants could rewrite the firmware to "impress" contest runner cmdc0de for challenge points.'
look:
  colors: []
  shape: null
  themes:
  - ctf
  - puzzle
tech:
  mcu: CH32V003
  leds:
    count: 6
    type: WS2812B
    note: "Repo BOM lists 'WS2112B', almost certainly a typo for WS2812B."
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Given to participants of the REALI7Y OVERRUN contest at DEF CON 33 (2025); the repo README addresses the reader as an SAO holder, but no source states whether it was free, included with registration, or distributed some other way.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/reali7y-over-run/ror3-sao/tree/main/ror3-sao-firmware
  eda_tool: null
links:
- label: github.com/reali7y-over-run/ror3-sao
  url: https://github.com/reali7y-over-run/ror3-sao
  kind: repo
- label: REALI7Y OVERRUN contest site
  url: https://reali7y-over.run/
  kind: website
- label: DEF CON 33 contest listing — REALI7Y OVERRUN
  url: https://defcon.org/html/defcon-33/dc-33-contests.html
  kind: article
- label: DEF CON Forums — REALI7Y OVERRUN
  url: https://forum.defcon.org/node/249299
  kind: social
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/reali7y-over-run/ror3-sao
  title: ror3-sao — Reali7y Over Run
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://raw.githubusercontent.com/reali7y-over-run/ror3-sao/main/README.md
  title: ror3-sao README
  accessed: '2026-09-07'
  note: 'BOM (6x WS2112B/WS2812B LEDs, CH32V003, SAO connector, 2 buttons, WCH Link V2 programming header) and description of the impress-cmdc0de firmware challenge.'
- kind: url
  url: https://defcon.org/html/defcon-33/dc-33-contests.html
  title: 'DEF CON 33 Contests page'
  accessed: '2026-09-07'
  note: 'Confirms REALI7Y OVERRUN is a DEF CON 33 (2025) contest; no SAO mention on this page itself.'
- kind: url
  url: https://forum.defcon.org/node/249299
  title: 'REALI7Y OVERRUN - DEF CON Forums'
  accessed: '2026-09-07'
  note: "Confirms REALI7Y OVERRUN is a hybrid contest with a deepfake/forgery storyline (per the page's own description meta tag); the guest-visible page does not contain the word \"SAO\" anywhere, so it does not itself confirm the SAO give-away — that comes from the GitHub repo."
- kind: url
  url: https://reali7y-over.run/
  title: 'REALI7Y OVERRUN'
  accessed: '2026-09-07'
  note: 'Contest microsite; fetched content gave no further badge specifics beyond the title.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Verification pass (2026-09-07): re-fetched all 5 cited sources. GitHub repo and its raw README confirm the BOM (CH32V003, 6x WS2112B/WS2812B-family LEDs, 2 buttons, SAO connector, WCH Link V2 programming header) and the "impress cmdc0de" firmware-hacking mechanic; the defcon.org contests page confirms REALI7Y OVERRUN is a listed DEF CON 33 (2025) contest, supporting the dc33/2025 correction. The DEF CON forum thread page, however, does not actually contain the word "SAO" anywhere in its guest-visible content (the full post body is not rendered for logged-out visitors) -- it only corroborates the deepfake/forgery storyline description, not an SAO give-away. Its source note was corrected accordingly, and get_one.distribution (previously "free_drop") was blanked since no source states whether the SAO was free, bundled with registration, or distributed some other way; get_one.where was reworded to reflect that. Event corrected from "other" to dc33 remains supported by the GitHub repo (contest tie-in) plus the defcon.org contests page. No PCB/hardware design files, price, quantity made, or photos of the actual board were found anywhere; the GitHub repo contains only firmware, no gerbers/schematic. "cmdc0de" (GitHub: cmdc0de) appears to be the contest runner/SAO designer but no maker bio or separate storefront was located. LED part number in the repo README is written "WS2112B", which does not match any known LED part and is treated here as a likely typo for WS2812B. With the distribution field blanked and the forum source note corrected, every remaining non-empty field is supported by a source that was actually re-read.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/ror3-sao-reali7y-over-run/
---

The ror3-sao is a Shitty Add-On distributed to participants of REALI7Y OVERRUN, a hybrid interactive storyline contest run at DEF CON 33 (2025) about deepfakes, forgery, and figuring out who can be trusted. The SAO itself is built around a CH32V003 RISC-V microcontroller driving six WS2812B-family addressable LEDs and two push buttons, connects to a host badge over a standard SAO header, and is reprogrammed through a WCH Link V2 programmer in RISC-V mode.

What makes the badge notable is that its firmware is the contest mechanic: the project's README invites players to rewrite the SAO's code and show it to contest runner cmdc0de to earn challenge points, rather than shipping a fixed light show. The GitHub repository (reali7y-over-run/ror3-sao) publishes the firmware and a short bill of materials, but no schematic, PCB layout, or Gerbers were found, so the hardware side is not confirmed open source. No price, production quantity, or photos of an assembled unit turned up in the sources checked, and no source states exactly how it reached participants' hands.

