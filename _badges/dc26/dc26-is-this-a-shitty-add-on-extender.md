---
title: Is This a Shitty Add-on Extender
id: dc26-dc26-is-this-a-shitty-add-on-extender
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: awkward intelligence
  url: https://hackaday.io/Awkwardai
summary: An SAO extender board that passes a badge's SAO header through to another add-on, part of awkward intelligence's collection of "shitty add-on" designs made for DEF CON 26; the maker's own file listing labels it simply '"Is this a shitty add-on" extender'.
functions: Passes the SAO header pins through so a second add-on can be stacked on top; no active circuitry described in the source material.
look:
  colors: []
  shape: null
  themes:
  - meme
tech:
  mcu: null
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
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://cdn.hackaday.io/files/1599526843386368/Isthisshitty.zip
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  url: https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  kind: hackaday
  archived: https://web.archive.org/web/20260505144653/https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
- label: hackaday.io/project/159952/files
  url: https://hackaday.io/project/159952/files
  kind: hackaday
  archived: https://web.archive.org/web/20260907115748/https://hackaday.io/project/159952/files
- label: Isthisshitty.zip (design files)
  url: https://cdn.hackaday.io/files/1599526843386368/Isthisshitty.zip
  kind: fab
- label: awkward intelligence on Hackaday.io
  url: https://hackaday.io/Awkwardai
  kind: hackaday
  archived: https://web.archive.org/web/20260307194059/https://hackaday.io/Awkwardai
images: []
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  title: The Harbinger Shitty Add-on Badges
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260505144653/https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
- kind: url
  url: https://hackaday.io/project/159952/files
  title: Files - The Harbinger Shitty Add-on Badges
  accessed: '2026-09-07'
  note: 'File listing shows Isthisshitty.zip (302.76 kB, uploaded 2019-03-04) with the maker''s own description: "Is this a shitty add-on" extender. No further specs, price, or images given.'
  archived: https://web.archive.org/web/20260907115748/https://hackaday.io/project/159952/files
- kind: url
  url: https://hackaday.io/Awkwardai
  title: awkward intelligence - Hackaday.io profile
  accessed: '2026-09-07'
  note: Confirms maker identity and Twitter handle (@awkwardai); no additional detail on this specific extender.
  archived: https://web.archive.org/web/20260307194059/https://hackaday.io/Awkwardai
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched all three cited sources and confirmed the file listing (Isthisshitty.zip, 302.76 kB, uploaded 03/04/2019, captioned "Is this a shitty add-on" extender), the parent project page (maker awkward intelligence, DEF CON 26, no other mention of this specific item, header images show other badges in the batch not this one), and the maker''s Hackaday.io profile (identity and @awkwardai handle). No images are claimed for this entry, so there was nothing to check against the folder or source pages there. One field was corrected: make_your_own.open_source was "yes" but only the hardware zip is published and no firmware exists or is mentioned — since tech.mcu is unknown rather than confirmed "none", firmware status cannot be ruled either way, so this is more accurately "partial" per the guide''s definition (both hardware and firmware published = yes). Everything else in the entry is supported by the cited sources or is correctly left null/empty. Only source is the maker''s own DEF CON 26 project page on Hackaday.io, which is an overview of a whole batch of "shitty add-on" boards; the page''s log/description text never singles out this extender, so everything here comes from the file listing''s own caption on Isthisshitty.zip. No chip, LED, price, quantity, or availability information was found anywhere, and no photo of the assembled board turned up. The title''s echo of the "Is this a pigeon?" meme format is a naming-convention observation, not something a source states outright. Treat mcu/leds/tech fields as genuinely unknown rather than presumed-passive, since the schematic inside the zip was not opened.'
last_modified_date: '2026-09-07'
---

Awkward intelligence built a large batch of "shitty add-on" (SAO) boards for DEF CON 26 in 2018 and later archived the design files under a single Hackaday.io project, "The Harbinger Shitty Add-on Badges." This extender is one of that batch: a simple board that takes a badge's SAO header and breaks it back out, letting a second add-on stack on top of it, in the tongue-in-cheek naming style ("Is this a shitty add-on?") the maker used across the series.

The only description that exists for it is the caption the maker put on the file itself, `Isthisshitty.zip`, uploaded to the project's files section on March 4, 2019. That zip is presumed to hold the fabrication files (the maker's other entries in the same listing are Gerber sets), but its contents were not opened during this pass, so no chip, LED, or connector details can be confirmed. No price, quantity, or photo of the physical board was found; the project page's own images are of other badges in the same collection (the Harbinger LED flasher, Shitty Calvin), not this extender.

## Make your own

The maker's zip archive (`Isthisshitty.zip`, linked above) is described as containing this board's design files, but its contents were not inspected — someone wanting to build it would need to download and open the archive to confirm what's inside (schematic, Gerbers, BOM) before fabricating.
