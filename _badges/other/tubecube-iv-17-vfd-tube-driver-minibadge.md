---
title: TubeCube — IV-17 VFD tube driver minibadge
id: other-tubecube-iv-17-vfd-tube-driver-minibadge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: other
year: 0
makers:
- name: hamster
  url: https://github.com/hamster
summary: A single-digit IV-17 vacuum-fluorescent-display driver built as a stacked minibadge; multiple units chain together over a serial line to scroll a message banner across several tubes.
functions: Displays alphanumeric characters (and two dots) on an IV-17 VFD tube. Units daisy-chain via UART so a message scrolls from tube to tube; each board idles its high-voltage supply when its character is blank to cut power draw from ~90mA to ~40mA.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - hardware tool
tech:
  mcu: ATtiny1616
  leds: null
  display: IV-17 VFD tube (16 alphanumeric elements plus 2 dots)
  connectivity:
  - uart
  - i2c
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
  open_source: true
  hardware_url: https://github.com/hamster/TubeCube
  firmware_url: https://github.com/hamster/TubeCube/tree/master/Software
  eda_tool: null
  license: MIT
  notes: Repo includes the schematic (TubeCube.pdf), the IV-17 datasheet, and firmware source under Software/. Digit patterns adapted from dmadison/Segmented-LED-Display-ASCII; boost-supply design partly derived from the Adafruit Ice Tube Clock.
links:
- label: github.com/hamster/TubeCube
  url: https://github.com/hamster/TubeCube
  kind: repo
  archived: https://web.archive.org/web/20260309115640/https://github.com/hamster/TubeCube
images: []
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://github.com/hamster/TubeCube
  title: TubeCube — IV-17 VFD tube driver minibadge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
  archived: https://web.archive.org/web/20260309115640/https://github.com/hamster/TubeCube
- kind: url
  url: https://raw.githubusercontent.com/hamster/TubeCube/master/README.md
  title: hamster/TubeCube README
  accessed: '2026-09-07'
  note: Primary source for hardware description, chip, tube, chaining behavior, and power figures.
- kind: url
  url: https://api.github.com/repos/hamster/TubeCube
  title: hamster/TubeCube repository metadata
  accessed: '2026-09-07'
  note: Confirmed MIT license, repo created 2019-10-23, single maker (hamster), no listed topics or homepage.
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched all three cited sources (repo homepage, raw README, GitHub API metadata) and confirmed every populated field and body sentence — MCU (ATtiny1616), tube (IV-17, 16 elements + 2 dots), UART/I2C connectivity, chaining behavior, ~90mA/~40mA power figures, MIT license, repo file listing (TubeCube.pdf, IV-17.pdf, Software/), the Adafruit Ice Tube Clock and dmadison/Segmented-LED-Display-ASCII credits, the four-board solder-bridge stackup, and the "few bucks a tube... from Ukraine" eBay sourcing. Removed an unsupported "Soviet-era" characterization of the tube from the body text — no cited source states this. No source states which conference or year this was made for, and no price, quantity, or availability information was found anywhere; event stays other. The repo''s two images (tube.PNG, HVPS.PNG) are schematic/datasheet diagrams, not photos of the assembled physical badge, so images remain empty. Repo created 2019-10-23, last pushed 2019-10-23
    (single burst of work). NOTE: found a separate, more complete existing entry for the apparent same project at _badges/other/tubecube-minibadge.md (id other-tubecube-minibadge, year 2019, maker link to hackaday.io/hacker/277672-hamster) — likely a duplicate; flagged in report, not touched per one-entry-per-task rule.'
last_modified_date: '2026-09-07'
---

TubeCube is a minibadge built around a single IV-17 vacuum-fluorescent display tube — an alphanumeric VFD the maker sources cheaply from eBay sellers in Ukraine — driven by an ATtiny1616 and an HV5812 high-voltage SPI switch. The design stacks four small PCBs joined by solder bridges rather than headers, and includes its own boost converter (adapted in part from the Adafruit Ice Tube Clock) to generate the roughly 24–25V grid voltage the tube needs, while running the filament directly off 5V through a resistor rather than the tube's rated AC drive.

Its notable feature is chaining: each TubeCube listens on UART, and if it doesn't see another unit already talking, it assumes it's the head of the chain and starts generating a scrolling message banner itself; otherwise it displays whatever character it receives and passes the previous character on to the next tube in line. To save power, a unit drops its boost supply to an idle state whenever the character it's showing doesn't need illumination, cutting draw from about 90mA to roughly 40mA per tube.

The hardware and firmware are both published (MIT license) in the maker's GitHub repo, including the schematic, the IV-17 datasheet, and source under a Software/ directory. No conference, year, price, or quantity is documented anywhere in the project, and no photo of an assembled unit was found — only schematic diagrams of the tube pinout and the boost-supply circuit.
