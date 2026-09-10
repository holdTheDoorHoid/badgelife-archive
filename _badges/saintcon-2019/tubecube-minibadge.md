---
title: TubeCube Minibadge
id: saintcon-2019-tubecube-minibadge
layout: badge
parent: SAINTCON 2019
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2019
year: 2019
makers:
- name: hamster (cavehamster)
  url: https://hackaday.io/hacker/277672-hamster
summary: A stacked-PCB SAINTCON minibadge that drives a Soviet-surplus IV-17 vacuum fluorescent display tube, boosting a few volts up to the ~24V the tube's grid needs.
functions: Displays alphanumeric characters (16 elements plus two dots) on the IV-17 tube; multiple units daisy-chain over UART so a message scrolls across a line of tubes, with each tube dropping its boost supply to an idle state on blank characters to save power (about 90mA active, ~40mA idle).
look:
  colors: []
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
  open_source: yes
  hardware_url: https://github.com/hamster/TubeCube
  firmware_url: https://github.com/hamster/TubeCube/tree/master/Software
  eda_tool: null
links:
- label: hackaday.io/project/168249-tubecube-minibadge/details
  url: https://hackaday.io/project/168249-tubecube-minibadge/details
  kind: hackaday
- label: github.com/hamster/TubeCube
  url: https://github.com/hamster/TubeCube
  kind: repo
images:
  - file: assets/images/badges/saintcon-2019/tubecube-minibadge/205832fa18.jpg
    source: "https://hackaday.io/project/168249-tubecube-minibadge/details"
    credit: "hamster"
    caption: "TubeCube minibadge mounted on a SAINTCON badge"
contact: {}
notes:
- A SAINTCON minibadge-standard add-on hosting an IV-17 VFD tube with onboard boost power supply and UART daisy-chaining, built by hamster for SAINTCON 2019 (also covered on Hackaday and with source at github.com/hamster/TubeCube). Found by the event-year sweep, task saintcon-2019.
- Duplicates an existing, more thoroughly researched entry at other-tubecube-minibadge (and a second partial duplicate at other-tubecube-iv-17-vfd-tube-driver-minibadge); both were previously logged with event "other" because their sources at the time (Hackaday and GitHub README/API pages, not the full Hackaday.io project log) did not state a convention. This pass read the full Hackaday.io project log, which explicitly ties the badge to SAINTCON and states a quantity of 8.
status: released
sources:
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
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: >-
    Maker's own Hackaday.io project log confirms this was built for SAINTCON 2019 (it plugs into
    a "Saintcon minibadge socket" and references a SAINTCON talk by the maker on PCB art), resolving
    the event ambiguity that an earlier duplicate entry (other-tubecube-minibadge) left as "other."
    Quantity (8 made, 4 worn by the maker, remainder gifted) and price (never set — maker floated a
    possible future Tindie release contingent on a redesign, which never happened per the repo's
    single 2019-10-23 commit burst) come directly from the same project log. Hardware/firmware
    details (ATtiny1616, HV5812, boost to ~24V, UART chaining, 90mA/40mA power figures) match what
    the duplicate entries already verified against the GitHub repo. This is a duplicate of
    other-tubecube-minibadge (more complete, MIT license and repo file details) and
    other-tubecube-iv-17-vfd-tube-driver-minibadge (also flags the first as a likely duplicate);
    flagged per the one-entry-per-task rule rather than merged. tech.leds, look.colors/shape,
    get_one.price, and make_your_own.eda_tool remain empty/null as no source states them for this
    unit (the sibling entry's "green" PCB color is from its own saved photo of a different-looking
    unit and was not independently confirmed here).
last_modified_date: '2026-09-10'
---

The TubeCube is a stacked-PCB minibadge built around a Soviet-surplus IV-17 vacuum fluorescent display tube, made by Hackaday.io user "hamster" (cavehamster) for SAINTCON 2019. It plugs into SAINTCON's 0.8-inch-square minibadge socket standard, though the maker describes bending that standard somewhat to fit the design. An ATtiny1616 drives a boost converter that steps a few volts up to roughly 24V for the tube's grid, paired with an HV5812 high-voltage driver chip for the individual segments; the four small PCBs that make up the cube are joined by solder-filleted pads at the inside corners rather than a single flat board or connectors.

Its signature feature is daisy-chaining: each tube listens on UART at boot for a "magic" sync byte, and any unit that doesn't hear one after about a second assumes it is the head of the chain and starts clocking out a scrolling string; other tubes fall in line as slaves, each passing its previously displayed character down to the next tube as a new one arrives, producing a scrolling banner across the whole chain. Idle tubes drop their boost supply to cut power draw from about 90mA down to roughly 40mA.

The maker built 8 units for SAINTCON 2019, wore 4 on their own badge, and gave the rest away; the badge was never sold, though the maker's Hackaday log mentions weighing a future redesign for a possible Tindie listing that does not appear to have happened. Hardware and firmware are both published on GitHub under the MIT license.

## Make your own

Board schematics and the IV-17 datasheet are included as PDFs in the [GitHub repo](https://github.com/hamster/TubeCube), and the firmware (built from an Atmel START base project) lives in the repo's `Software` folder. The README covers sourcing an IV-17 tube (the maker notes they were still cheaply available from Ukrainian eBay sellers as of writing), the HV5812/boost-converter circuit, and the UART chaining protocol used to drive multiple cubes together.
