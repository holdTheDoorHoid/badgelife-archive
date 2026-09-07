---
title: name-badge-sao — Hello My Name Is tag SAO
id: supercon-2024-name-badge-sao-hello-my-name-is-tag-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Surreality Labs
  url: https://github.com/SurrealityLabs
summary: A DIY SAO that spells out the wearer's name on a 16x8 LED dot-matrix display, built around an STM32F030 microcontroller. Surreality Labs designed it as a giveaway for Hackaday Supercon.
functions: Drives a 128-LED (16x8) matrix, presumably to show or scroll the wearer's name; the board also carries two tactile buttons, likely for setting or cycling the display.
look:
  colors: []
  shape: rectangle
  themes:
  - text
  - name badge
tech:
  mcu: STM32F030C8Tx
  leds:
    count: 128
    type: null
    note: 16x8 LED matrix arranged as a dot-matrix display, row-driven through 16 NPN transistors (MMBT3904); LED color/part not specified in the schematic.
  display: LED matrix 16x8
  connectivity: []
  battery: null
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/SurrealityLabs/name-badge-sao
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/SurrealityLabs/name-badge-sao
  url: https://github.com/SurrealityLabs/name-badge-sao
  kind: repo
- label: 'Surreality Labs: Getting back into the swing of things'
  url: http://surrealitylabs.com/2023/12/getting-back-into-the-swing-of-things/
  title: Getting back into the swing of things - Surreality Labs
  kind: article
- label: Surreality Labs (surrealitylabs.com)
  url: https://surrealitylabs.com
  kind: website
images: []
contact: {}
notes:
- 'Not to be confused with a different, similarly-titled "hello my name is SAO" by maker davedarko for the Supercon 8 (2024) official add-on contest (hackaday.io/project/197693) — that is a separate, non-electronic silkscreen name tag, unrelated to this Surreality Labs board.'
status: announced
sources:
- kind: url
  url: https://github.com/SurrealityLabs/name-badge-sao
  title: name-badge-sao — Hello My Name Is tag SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/SurrealityLabs/name-badge-sao
  title: SurrealityLabs/name-badge-sao GitHub repo
  accessed: '2026-09-07'
  note: 'Repo description ("A shitty add-on that''s also a lovely Hello My Name Is tag"), commit history (3 commits, Nov 12-17 2023, moving from charlieplexed to a normal LED matrix on a new MCU), and pcb/ directory contents (KiCad project, no README, no firmware).'
- kind: url
  url: https://raw.githubusercontent.com/SurrealityLabs/name-badge-sao/main/pcb/name-badge-sao/name-badge-sao.kicad_sch
  title: name-badge-sao.kicad_sch (schematic source)
  accessed: '2026-09-07'
  note: 'Schematic parts list: STM32F030C8Tx MCU, 128 LED symbols (16x8), 16x MMBT3904 transistors, a 6-pin (2x3) SAO connector, 2 tactile switches, SWD programming pads. Confirms SAO v2 header and dot-matrix LED display.'
- kind: url
  url: http://surrealitylabs.com/2023/12/getting-back-into-the-swing-of-things/
  title: Getting back into the swing of things - Surreality Labs
  accessed: '2026-09-07'
  note: 'Maker''s own blog post (Dec 2023) says he plans "a couple of SAO designs" and wants "a bunch of them to give away at Supercon next year" — i.e. Supercon 8 / Nov 2024. This is the basis for setting event to supercon-2024; it states intent, not confirmed completion or distribution.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Event (supercon-2024) is based on the maker''s stated intent in a Dec 2023 blog post ("give away at Supercon next year"), not on a confirmed sighting at the con. The GitHub repo shows only 3 commits, all from Nov 12-17 2023, ending mid-design ("I think that''s an SAO") with no README, no firmware, and no later activity or release — there is no evidence the board was ever finished, fabricated in quantity, or actually distributed. No photos of an assembled unit were found anywhere (repo, blog, or web search), so images could not be filled in. Price, quantity, and availability are all genuinely unknown. LED color/part and battery are not stated in the schematic beyond generic "LED" symbols. Set status to announced rather than listed/released given the above. A different maker (davedarko) made an unrelated, non-electronic silkscreen "hello my name is" SAO for the same Supercon 8 (2024) contest — noted in `notes` so future research does not conflate the two.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/name-badge-sao-hello-my-name-is-tag-sao/
---

Surreality Labs designed this SAO as a wearable name badge built around an STM32F030C8 microcontroller driving a 16x8 grid of 128 LEDs — enough to render a name across a small dot-matrix display rather than relying on printed text. The schematic shows the LEDs row-driven through 16 NPN transistors, a 6-pin SAO connector, two tactile buttons (likely for setting or advancing the displayed name), and an SWD header for programming, but no onboard battery, so it appears to draw power from the host badge.

The project's only public trace is a three-commit GitHub repository from November 2023, ending mid-design, and a December 2023 blog post from the maker saying he hoped to have "a bunch of them to give away at Supercon next year" — pointing at Hackaday Supercon 8 in November 2024. No firmware, photos, or later updates turned up, so it is unclear whether the board was ever finished, fabricated, or actually handed out at that con.
