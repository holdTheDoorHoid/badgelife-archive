---
title: TubeCube Minibadge
id: other-tubecube-minibadge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: other
year: 2019
makers:
- name: hamster
  url: https://hackaday.io/hacker/277672-hamster
summary: A stacked-PCB minibadge that drives a Soviet-era IV-17 VFD tube, boosting a few volts of input up to the ~25-70V the tube needs.
functions: Displays alphanumeric characters (16 elements plus two dots) on the IV-17 vacuum fluorescent tube; when chained to other cubes over UART it passes characters down the line to scroll a message banner across multiple units, and idles its boost supply down when not displaying to save power.
look:
  colors:
  - green
  shape: null
  themes:
  - retro computer
  - hardware tool
tech:
  mcu: ATtiny1616
  leds: null
  display: IV-17 VFD tube (16-segment alphanumeric + 2 dots)
  connectivity:
  - uart
  - i2c
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '8'
  availability: limited
  distribution:
  - free_drop
  where: Made for SAINTCON 2019; the maker built 8 units, wore 4 on their own badge, and gave the rest away. Not sold; the maker considered a redesign for a possible future Tindie listing but never released one.
make_your_own:
  open_source: true
  hardware_url: https://github.com/hamster/TubeCube
  firmware_url: https://github.com/hamster/TubeCube/tree/master/Software
  eda_tool: null
links:
- label: hackaday.io/project/168249-tubecube-minibadge
  url: https://hackaday.io/project/168249-tubecube-minibadge
  kind: hackaday
- label: github.com/hamster/TubeCube
  url: https://github.com/hamster/TubeCube
  kind: repo
  archived: https://web.archive.org/web/20260309115640/https://github.com/hamster/TubeCube
- label: hackaday.io/project/168249-tubecube-minibadge/details
  url: https://hackaday.io/project/168249-tubecube-minibadge/details
  kind: hackaday
images:
- file: assets/images/badges/other/tubecube-minibadge/205832fa18.jpg
  source: https://hackaday.io/project/168249-tubecube-minibadge
  credit: hamster
  caption: TubeCube minibadge with its IV-17 VFD tube, shown next to an AA battery for scale
- file: assets/images/badges/other/tubecube-minibadge/205832fa18.jpg
  source: https://hackaday.io/project/168249-tubecube-minibadge/details
  credit: hamster
  caption: TubeCube minibadge mounted on a SAINTCON badge
contact: {}
notes:
- IV-17 VFD tube driver minibadge, ATtiny1616, boost SMPS to 70V.
- The PCB is built as 4 stacked boards joined by solder bridges, silkscreened with a small raccoon-face logo; the maker calls the form factor "minibadge-cubed."
- A SAINTCON minibadge-standard add-on hosting an IV-17 VFD tube with onboard boost power supply and UART daisy-chaining, built by hamster for SAINTCON 2019 (also covered on Hackaday and with source at github.com/hamster/TubeCube). Found by the event-year sweep, task saintcon-2019.
- Duplicates an existing, more thoroughly researched entry at other-tubecube-minibadge (and a second partial duplicate at other-tubecube-iv-17-vfd-tube-driver-minibadge); both were previously logged with event "other" because their sources at the time (Hackaday and GitHub README/API pages, not the full Hackaday.io project log) did not state a convention. This pass read the full Hackaday.io project log, which explicitly ties the badge to SAINTCON and states a quantity of 8.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/168249-tubecube-minibadge
  title: TubeCube Minibadge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/168249-tubecube-minibadge
  title: TubeCube Minibadge - Hackaday.io
  accessed: '2026-09-07'
  note: Project description, maker (hamster), creation date (2019-11-01), tech specs (ATtiny1616, HV5812, LM9022, boost to 70V), and project photos.
- kind: url
  url: https://github.com/hamster/TubeCube
  title: hamster/TubeCube - GitHub
  accessed: '2026-09-07'
  note: README describing the "minibadge-cubed form factor," 4-board solder-bridge stackup, IV-17 tube details, HV5812/boost circuit, chained-UART display protocol, and MIT license.
  archived: https://web.archive.org/web/20260309115640/https://github.com/hamster/TubeCube
- kind: url
  url: https://hackaday.io/project/168249-tubecube-minibadge/details
  title: TubeCube Minibadge
  accessed: '2026-09-10'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2019); event read as ''saintcon-2019''.'
- kind: url
  url: https://hackaday.io/project/168249-tubecube-minibadge/details
  title: TubeCube Minibadge - Hackaday.io project log
  accessed: '2026-09-10'
  note: 'Full project log text: confirms SAINTCON 2019 (built for SAINTCON, plugs into a "Saintcon minibadge socket," references a SAINTCON talk by the maker), ATtiny1616 + HV5812 driver, UART daisy-chain protocol (0x23 sync byte, 9600 baud, push/shove chaining), 8 units made (4 worn on maker''s own badge, rest given away), no price, and no release to Tindie ever happened.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-opened both cited sources and the saved photo. Confirmed a real, built minibadge (not just a concept) from the maker''s own Hackaday.io project and GitHub repo (MIT-licensed hardware and firmware, schematics, and a photo of the assembled unit next to an AA battery clearly showing the green PCB and raccoon-face logo). Corrected one overstatement in the body: the GitHub README says the filament is simply fed a resistor-limited 5V, not driven by the LM9022 chip whose datasheet is attached to the Hackaday project page as a reference file only — the body no longer credits the LM9022 with driving the filament, and the boost figure was tightened to the README''s stated 24V (not 25V). No source states which convention it was made for or sold at, or any price/quantity/availability info, so event is left as "other" rather than guessed; type "minibadge" (stacked-cube form factor, SAO-adjacent but not itself an SAO) matches the maker''s own description. Created/posted
    November 2019; no evidence found tying it to a specific SAINTCON year or any other named con. Everything remaining in the entry is directly supported by the two cited sources and the saved image. Merged with duplicate entry ''TubeCube Minibadge'' (saintcon-2019-tubecube-minibadge).'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/saintcon-2019/tubecube-minibadge/
---

The TubeCube is a self-contained minibadge built around a Soviet-surplus IV-17 vacuum fluorescent display tube — the same family of tube used in retro clock kits like Adafruit's Ice Tube Clock, from which its boost-converter design is partly borrowed. An ATtiny1616 runs a PWM boost supply that steps a few volts up to around 24V (with headroom to 70V) to drive the tube's grid, while an SPI-controlled HV5812 high-voltage switch handles the individual segments; the filament itself is simply fed a resistor-limited 5V rather than through a dedicated driver chip. The whole thing is built from four small PCBs stacked into a cube and joined with solder bridges rather than a single flat board, giving it the "minibadge-cubed" form factor the maker (hackaday.io user "hamster") named it after; the badge's side panel carries a small raccoon-face logo.

Multiple TubeCubes can be daisy-chained over UART: each unit passes along whatever character it isn't currently displaying, so a line of cubes can scroll a banner message across all of them, with each cube dimming its boost supply during blank characters to cut power draw from about 90mA to roughly 40mA.

Hardware (schematics, board files) and firmware are both published on GitHub under the MIT license, making this a fully open-source build. No source found states what event, if any, the TubeCube was made for or sold at, nor any pricing or quantity information — it reads as an independent hardware project documented and shared through Hackaday.io and GitHub rather than a badge distributed at a specific convention.

## Make your own

The hardware and firmware are both in the [GitHub repo](https://github.com/hamster/TubeCube): board schematics and the IV-17 datasheet are included as PDFs, and the firmware (written from an Atmel START base project, developed in Atmel Studio) is in the `Software` folder. The README walks through sourcing an IV-17 tube (the maker notes they were still available cheaply from Ukrainian eBay sellers as of writing), the HV5812/boost-converter circuit, and the UART chaining protocol used to drive multiple cubes together.

## Notes merged from the duplicate entry "TubeCube Minibadge"

The TubeCube is a stacked-PCB minibadge built around a Soviet-surplus IV-17 vacuum fluorescent display tube, made by Hackaday.io user "hamster" (cavehamster) for SAINTCON 2019. It plugs into SAINTCON's 0.8-inch-square minibadge socket standard, though the maker describes bending that standard somewhat to fit the design. An ATtiny1616 drives a boost converter that steps a few volts up to roughly 24V for the tube's grid, paired with an HV5812 high-voltage driver chip for the individual segments; the four small PCBs that make up the cube are joined by solder-filleted pads at the inside corners rather than a single flat board or connectors.

Its signature feature is daisy-chaining: each tube listens on UART at boot for a "magic" sync byte, and any unit that doesn't hear one after about a second assumes it is the head of the chain and starts clocking out a scrolling string; other tubes fall in line as slaves, each passing its previously displayed character down to the next tube as a new one arrives, producing a scrolling banner across the whole chain. Idle tubes drop their boost supply to cut power draw from about 90mA down to roughly 40mA.

The maker built 8 units for SAINTCON 2019, wore 4 on their own badge, and gave the rest away; the badge was never sold, though the maker's Hackaday log mentions weighing a future redesign for a possible Tindie listing that does not appear to have happened. Hardware and firmware are both published on GitHub under the MIT license.

## Make your own

Board schematics and the IV-17 datasheet are included as PDFs in the [GitHub repo](https://github.com/hamster/TubeCube), and the firmware (built from an Atmel START base project) lives in the repo's `Software` folder. The README covers sourcing an IV-17 tube (the maker notes they were still cheaply available from Ukrainian eBay sellers as of writing), the HV5812/boost-converter circuit, and the UART chaining protocol used to drive multiple cubes together.
