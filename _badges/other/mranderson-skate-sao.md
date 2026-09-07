---
title: MrAnderson
id: other-mranderson-skate-sao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2024
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: A work-in-progress proof-of-concept SAO by davedarko that mounts real fingerboard trucks on the PCB, paired with an inspirational quote from skateboarder Andy Anderson.
functions: 'None (passive/decorative proof of concept; no electronics function described)'
look:
  colors: []
  shape: null
  themes:
  - skateboard
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
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/MrAnderson
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  kind: repo
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main/MrAnderson
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/MrAnderson
  kind: repo
images:
  - file: assets/images/badges/other/mranderson-skate-sao/4d9d7dfc93.jpg
    source: "https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/MrAnderson"
    credit: "davedarko"
    caption: "Prototype Skate SAO PCB with fingerboard trucks mounted"
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  title: davedarko/Simple-Add-ons-SAO — Find all of my simple add-ons in this repository
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/MrAnderson
  title: Simple-Add-ons-SAO/MrAnderson at main
  accessed: '2026-09-07'
  note: Folder listing confirms project files (2411_Skate.md, AndyAndersonBoard.jpg, MrAnderson.svg, Eagle/KiCad sources).
- kind: url
  url: https://raw.githubusercontent.com/davedarko/Simple-Add-ons-SAO/main/MrAnderson/2411_Skate.md
  title: 2411_Skate.md (raw)
  accessed: '2026-09-07'
  note: 'Confirms description: proof of concept for using fingerboard trucks on PCBs, with an inspirational quote by Andy Anderson; idea stated as "Fingerboards have trucks, why not use them on a PCB instead."'
- kind: url
  url: https://api.github.com/repos/davedarko/Simple-Add-ons-SAO/contents/MrAnderson/MrAnderson
  title: GitHub API directory listing for MrAnderson/MrAnderson
  accessed: '2026-09-07'
  note: 'Fact-check: confirms the design files are MrAnderson.kicad_sch, MrAnderson.kicad_pcb, MrAnderson.kicad_pro (KiCad only) — no Eagle files present, correcting eda_tool from Eagle to KiCad.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): confirmed via GitHub API directory listing that the MrAnderson subfolder contains only KiCad files (.kicad_sch, .kicad_pcb, .kicad_pro) — no Eagle files were found, so eda_tool was corrected from "Eagle" to "KiCad". (The maker''s 2411_Skate.md does say "Github with Eagle/KiCad files," but that line is a boilerplate link reused verbatim across other project folders in the same repo that do use Eagle, so it is not reliable evidence for this specific item; the actual file extensions are.) Removed "professional" as an unsupported descriptor for Andy Anderson — no cited source states his profession. Verified the saved image (4d9d7dfc93.jpg) matches the repo''s AndyAndersonBoard.jpg (same 1031x1200 dimensions and embedded eBay/ImageMagick processing comment; the maker appears to have sourced/re-saved the photo from an eBay listing). All other confirmed facts (proof-of-concept SAO, fingerboard trucks on PCB, Andy Anderson quote, no electronics, no pricing/quantity/distribution/event) still stand from the maker''s own repo. No pricing, quantity, distribution, or specific event was ever published, so those fields stay empty and status remains "researched" rather than "verified".'
last_modified_date: '2026-09-07'
---

MrAnderson is a proof-of-concept SAO (add-on board) by hardware maker davedarko, part of their ongoing Simple Add-ons repository of small PCB designs. Rather than functioning as an electronic gadget, it explores mounting real fingerboard trucks directly onto the PCB, paired with an inspirational quote from skateboarder Andy Anderson. The maker's own note frames the idea plainly: "Fingerboards have trucks, why not use them on a PCB instead."

The design files, in KiCad format (schematic, PCB, and a fingerboard-truck footprint library), are published in davedarko's Simple-Add-ons-SAO GitHub repository. No pricing, quantity, or distribution details were published, and no specific convention or year is named for the piece; the project folder is dated with a "2411" prefix (suggesting November 2024), but this could not be confirmed against any named event.

## Make your own

KiCad source files (schematic and PCB), along with a fingerboard-truck footprint library, are available in the [MrAnderson folder](https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/MrAnderson) of davedarko's Simple-Add-ons-SAO repository.
