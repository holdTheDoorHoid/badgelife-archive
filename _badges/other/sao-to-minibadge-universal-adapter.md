---
title: SAO-to-Minibadge Universal Adapter
id: other-sao-to-minibadge-universal-adapter
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: other
year: 0
makers:
- name: Herushan
  url: https://github.com/Herushan
summary: A passive PCB adapter that lets a Minibadge plug into an SAO header, or an SAO plug into a Minibadge display/badge, solderable either direction.
functions: No active function; it is a connector adapter. Depending on which parts are soldered on, it converts SAO-format connectors to Minibadge format or Minibadge format to SAO, so a badge with one connector type can accept accessories built for the other.
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Not sold; the maker asks that people build their own from the published Gerbers rather than buy/sell it.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/Herushan/SAO-to-Minibadge-universal-adapter
  firmware_url: null
  eda_tool: KiCad
  gerbers_url: https://github.com/Herushan/SAO-to-Minibadge-universal-adapter/blob/main/UniSAOMBgerber.zip
  license: Unclear; maker says "still figuring out the best license... for personal use and please do not sell this item."
links:
- label: github.com/Herushan/SAO-to-Minibadge-universal-adapter
  url: https://github.com/Herushan/SAO-to-Minibadge-universal-adapter
  kind: repo
- label: Build/solder video (YouTube)
  url: https://youtu.be/1QgKpa0yQGg
  kind: video
images:
- file: assets/images/badges/other/sao-to-minibadge-universal-adapter/6c31ad64d8.jpg
  source: https://github.com/Herushan/SAO-to-Minibadge-universal-adapter
  credit: Herushan
  caption: Assembled SAO-to-Minibadge adapter board
- file: assets/images/badges/other/sao-to-minibadge-universal-adapter/36af4bfab4.jpg
  source: https://github.com/Herushan/SAO-to-Minibadge-universal-adapter
  credit: Herushan
  caption: SAO-to-Minibadge adapter board, front
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/Herushan/SAO-to-Minibadge-universal-adapter
  title: SAO-to-Minibadge-universal-adapter
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/Herushan/SAO-to-Minibadge-universal-adapter
  title: GitHub repo README and file listing
  accessed: '2026-09-07'
  note: Confirmed purpose (bidirectional SAO<->Minibadge connector adapter), parts list (16 male header pins or two 8-hole female single-row headers plus a male or female SAO header), KiCad + Gerber files, license caveat, and photos.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This is a general-purpose connector adapter, not made for a specific convention or year, so it is left under "other" with no year. The maker does not state a chip, LEDs, price, or quantity made because the board is a passive connector adapter with no active components. No storefront was found; the maker explicitly discourages selling it and points people to the Gerbers instead. Fact-check (2026-09-07): re-fetched the GitHub repo README and confirmed the summary, parts list, KiCad/Gerber links, license caveat, and video link verbatim; confirmed both saved images show boards labeled "Universal SAO to MB converter" matching the repo. Removed one unsupported body sentence that had specifically named "SAINTCON" as the venue for the Minibadge format -- the README never names SAINTCON or any event, so that detail was invented and has been deleted.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/sao-to-minibadge-universal-adapter.glb
  method: kicad
  source_file: SAO_MB_adapter.kicad_pcb
  generated: '2026-09-10'
  bytes: 101892
---

Herushan's SAO-to-Minibadge Universal Adapter is a small, purely passive PCB that bridges two badge-accessory connector standards: the SAO (Shitty Add-On) header found on many DEF CON-style badges, and the Minibadge format. Built and soldered one way, it lets a Minibadge plug into a badge's SAO header; built the other way, it lets an SAO plug into a Minibadge-compatible display or badge. There are no active components — just header pins (16 male pins, or two 8-hole female single-row headers) plus a male or female SAO connector, so assembly is a straightforward soldering job.

The maker published the full KiCad project (schematic, PCB layout, and project files) along with a ready-to-order Gerber zip, and posted a video walking through how to solder the adapter together. Licensing is left unsettled — the README says the maker is "still figuring out the best license for this" and asks that people not sell the board, treating it instead as a build-it-yourself accessory shared for personal use.

Because it is a generic connector adapter rather than something made for a particular badge or year, it is catalogued here without a specific convention or release date attached.
