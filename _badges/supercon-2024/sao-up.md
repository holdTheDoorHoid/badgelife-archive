---
title: SAO Up
id: supercon-2024-sao-up
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2024
year: 2024
makers:
- name: astuder
  url: https://github.com/astuder
summary: A small PCB adapter for the Hackaday Supercon 8 Add-On Badge that rotates an SAO slot by 90 degrees so SAOs sit closer to upright, usable on either side of the badge; designed in the ten days between the badge reveal and the event and released under CERN-OHL-P-2.0.
functions: 'Passive pass-through adapter; rotates one SAO slot 90 degrees to a more upright orientation. No active electronics, LEDs, or firmware of its own.'
look:
  colors: [green]
  shape: rectangle
  themes: [hardware tool]
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Not sold; shared as an open-hardware design for anyone to fabricate themselves.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/astuder/supercon8-sao-adapters/tree/main/sao-up
  firmware_url: null
  eda_tool: KiCad
  license: CERN-OHL-P-2.0
  notes: 'Repo also includes a second adapter, "SAO Bridge," which adds a center SAO slot and rotates the left/right slots upright; that is a separate item and not this entry.'
links:
- label: github.com/astuder/supercon8-sao-adapters
  url: https://github.com/astuder/supercon8-sao-adapters
  kind: repo
- label: github.com/astuder/supercon8-sao-adapters/tree/main/sao-up
  url: https://github.com/astuder/supercon8-sao-adapters/tree/main/sao-up
  kind: repo
- label: github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  kind: repo
images:
- file: assets/images/badges/supercon-2024/sao-up/fc029f04c4.jpg
  source: "https://github.com/astuder/supercon8-sao-adapters"
  credit: "astuder"
  caption: "SAO Up adapter, rotates an SAO slot 90 degrees to sit upright"
- file: assets/images/badges/supercon-2024/sao-up/1c22d9689e.jpg
  source: "https://github.com/astuder/supercon8-sao-adapters"
  credit: "astuder"
  caption: "Supercon 8 badge shown without and with the SAO adapters installed"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/astuder/supercon8-sao-adapters
  title: astuder/supercon8-sao-adapters - Adapters for the Hackaday Supercon 8 SAO Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://raw.githubusercontent.com/astuder/supercon8-sao-adapters/main/README.md
  title: 'README: supercon8-sao-adapters'
  accessed: '2026-09-07'
  note: 'Full description of both adapters (SAO Up and SAO Bridge), the design motivation, green PCB color choice/reason, CERN-OHL-P license statement, and source images.'
- kind: url
  url: https://github.com/astuder/supercon8-sao-adapters/tree/main/sao-up
  title: sao-up subfolder
  accessed: '2026-09-07'
  note: 'Confirms KiCad design files (sao-up.kicad_pcb/pro/sch) for this specific adapter.'
- kind: url
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  title: Hack-a-Day/2024-Supercon-8-Add-On-Badge
  accessed: '2026-09-07'
  note: Confirms the host badge is the 2024 Hackaday Supercon 8 Add-On Badge with a six-SAO hub.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Maker''s own repo README fully describes the item. Not sold or given away as a physical product as far as sources indicate; it is a shared open-hardware design (KiCad files) that people fabricate themselves, so get_one fields are mostly left empty/unknown. Exact SAO slot count on the host badge (six) comes from the badge repo, not this adapter''s own docs. tech.sao_version set to v1.69bis (6-pin) based on it being a 2024-era Hackaday SAO badge, though the adapter repo itself does not state the pin count explicitly.'
last_modified_date: '2026-09-07'
---

astuder designed SAO Up as a small companion PCB for the 2024 Hackaday Supercon 8 Add-On Badge, released in the roughly ten days between the badge's public reveal and the start of Supercon. The Supercon 8 badge has six SAO slots, but four of them sit sideways or upside-down, making plugged-in SAOs look awkward. SAO Up is a passive pass-through board that rotates a single SAO slot by 90 degrees so the SAO sits closer to upright; the same board design works on either the left or right side of the badge depending on which side the headers are soldered.

The adapters were made in green PCB rather than the more obvious black because green offered the fastest turnaround at JLCPCB given the tight timeline. The design is released under the CERN-OHL-P-2.0 permissive open hardware license, and the maker explicitly invites others to duplicate, adapt, or reuse it. The same repository also documents a second, related adapter called SAO Bridge, which adds a new center SAO slot to the badge in addition to rotating the side slots — that is a distinct design and not the subject of this entry.

## Make your own

KiCad design files (`sao-up.kicad_pcb`, `sao-up.kicad_pro`, `sao-up.kicad_sch`) are published in the `sao-up` subfolder of the repository under CERN-OHL-P-2.0. Order the board from a PCB fab of your choice (the maker used JLCPCB for fast turnaround), then solder female/male SAO headers to the appropriate sides to rotate a slot on the Supercon 8 badge.
