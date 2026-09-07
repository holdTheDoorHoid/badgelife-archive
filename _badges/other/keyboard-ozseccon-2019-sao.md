---
title: keyboard (OzSecCon 2019 SAO)
id: other-keyboard-ozseccon-2019-sao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2019
makers:
- name: digitalrane (ec0)
  url: https://github.com/digitalrane
summary: 'A tiny 16-key mechanical keyboard SAO, built with real Cherry MX switches read through an MCP23017 I/O expander.'
functions: 'Sixteen individually-wired Cherry MX switch positions, scanned via an MCP23017 16-bit I/O expander over the SAO connector; one onboard LED.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds:
    count: 1
    type: null
    note: Single LED (D1), driver/purpose not documented.
  display: null
  connectivity:
  - i2c
  battery: null
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/digitalrane/badgelife/tree/master/OzSecCon2019/keyboard
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/digitalrane/badgelife/tree/master/OzSecCon2019/keyboard
  url: https://github.com/digitalrane/badgelife/tree/master/OzSecCon2019/keyboard
  kind: repo
- label: github.com/digitalrane/badgelife
  url: https://github.com/digitalrane/badgelife
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: listed
sources:
- kind: url
  url: https://github.com/digitalrane/badgelife/tree/master/OzSecCon2019/keyboard
  title: keyboard (OzSecCon 2019 SAO)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''other''.'
- kind: url
  url: https://raw.githubusercontent.com/digitalrane/badgelife/master/OzSecCon2019/keyboard/keyboard-BOM.csv
  title: keyboard-BOM.csv
  accessed: '2026-09-07'
  note: 'BOM: MCP23017 I/O expander IC, 16x Cherry MX switches, 1x LED (D1), 3 resistors, 2x5-pin SAO socket.'
- kind: url
  url: https://github.com/digitalrane/badgelife
  title: digitalrane/badgelife
  accessed: '2026-09-07'
  note: 'Repo root README: "hardware CAD files for ec0''s various badge mods," organized by con/year folders; no pricing or distribution info given.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'No matching event id exists in events.yml for "OzSecCon" (a small Australian security conference) — left event as "other" and named the con here as instructed. The repo folder is dated 2019 (OzSecCon2019), taken as the year made-for. KiCad schematic/PCB/BOM files are published, but no firmware repo or README beyond the one-line description was found, so open_source is "partial" rather than "yes". No photos of the assembled board were found anywhere in the repo (no images folder, no README image) or via the maker''s GitHub profile, so images/get_one/contact remain empty. Web search budget was exhausted before broader searches (Hackaday, Twitter/Bluesky, OzSecCon program) could be run to corroborate price, quantity, or distribution — those remain unconfirmed.'
last_modified_date: '2026-09-07'
---

digitalrane (handle ec0) designed this SAO as a miniature mechanical keyboard: sixteen individual Cherry MX switch footprints wired into an MCP23017 16-bit I/O expander, which reports key states back to the host badge over the SAO's I2C connection. It uses the larger "LSAO" (SAO v1.69bis) footprint, matching the connector library included in the repository, and carries a single onboard LED whose exact function is not documented.

The design lives in digitalrane's `badgelife` GitHub repository, in a folder named for OzSecCon 2019, suggesting it was built for or around that Australian security conference that year. The repo publishes the KiCad schematic, PCB layout, and BOM for the board, but there is no accompanying firmware repository, assembly photo, or write-up describing how (or whether) it was distributed, so its production run, price, and availability are unknown.
