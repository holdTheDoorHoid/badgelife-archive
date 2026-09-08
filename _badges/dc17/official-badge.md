---
title: DEF CON 17 Official Badge
id: dc17-official-badge
layout: badge
parent: DC17
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc17
year: 2009
makers:
- name: Joe Grand (Kingpin) / Grand Idea Studio
  url: https://grandideastudio.com/portfolio/other/defcon-17-badge/
summary: 'The official DEF CON 17 (2009) electronic badge: seven interlocking puzzle-piece shapes for each attendee category, with a sound-reactive RGB LED and badge-to-badge communication.'
functions: Sound-reactive RGB LED that responds to ambient volume and frequency in three modes (Party/reactive, Quiet/color-cycling, Sleep); wired multi-badge communication; firmware upgradeable via serial bootloader.
look:
  colors: []
  shape: puzzle piece
  themes:
  - puzzle
  - security
tech:
  mcu: MC56F8006
  leds:
    count: 1
    type: RGB
    note: Kingbright RGB LED, sound-reactive
  display: none
  connectivity:
  - uart
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: 6,694
  availability: unknown
  distribution:
  - free_drop
  where: Given to attendees at DEF CON 17 (2009); badge type (human, goon, press, speaker, vendor, contest organizer, uber) matched registration category.
make_your_own:
  open_source: true
  hardware_url: https://grandideastudio.com/portfolio/other/defcon-17-badge/
  firmware_url: https://grandideastudio.com/portfolio/other/defcon-17-badge/
  eda_tool: null
  notes: Grand Idea Studio publishes schematic, BOM, assembly drawing, test procedure, and source code (CodeWarrior format) for the badge on the portfolio page.
  bom_url: https://grandideastudio.com/media/dc17_bdg_bom.pdf
links:
- label: grandideastudio.com/portfolio/other/defcon-17-badge
  url: https://grandideastudio.com/portfolio/other/defcon-17-badge/
  kind: website
- label: defcon.org/images/defcon-17/dc-17-presentations/defcon-17-joe-grand-making_the_dc17_badge.pdf
  url: https://defcon.org/images/defcon-17/dc-17-presentations/defcon-17-joe-grand-making_the_dc17_badge.pdf
  kind: doc
- label: forum.defcon.org/forum/defcon/defcon-badge-hacking-for-all-defcon-badges/11710-defcon-17-dc17-badge-pre-release-information
  url: https://forum.defcon.org/forum/defcon/defcon-badge-hacking-for-all-defcon-badges/11710-defcon-17-dc17-badge-pre-release-information
  kind: social
- label: badge.gallery/badges/def-con-17-badge
  url: https://badge.gallery/badges/def-con-17-badge
  kind: website
- label: dc17_bdg_slides.pdf (Making and Hacking the DEFCON 17 Badge)
  url: https://grandideastudio.com/wp-content/uploads/dc17_bdg_slides.pdf
  kind: doc
images:
- file: assets/images/badges/dc17/official-badge/26a346acb2.jpg
  source: https://grandideastudio.com/portfolio/other/defcon-17-badge/
  credit: Grand Idea Studio
  caption: DEF CON 17 badge set, seven interlocking puzzle-piece shapes
- file: assets/images/badges/dc17/official-badge/8b64578d93.jpg
  source: https://grandideastudio.com/portfolio/other/defcon-17-badge/
  credit: Grand Idea Studio
  caption: DEF CON 17 badge, front detail
- file: assets/images/badges/dc17/official-badge/26a346acb2.jpg
  source: https://grandideastudio.com/portfolio/other/defcon-17-badge/
  credit: Grand Idea Studio
  caption: DEF CON 17 badge, front
- file: assets/images/badges/dc17/official-badge/8b64578d93.jpg
  source: https://grandideastudio.com/portfolio/other/defcon-17-badge/
  credit: Grand Idea Studio
  caption: DEF CON 17 badge, back / components
contact: {}
notes:
- Seven interlocking puzzle-piece badge shapes (human, goon, press, speaker, vendor, contest organizer, uber) built around a Freescale MC56F8006 DSC, MEMS mic and RGB LED that reacts to ambient sound and links badge-to-badge; 6,694 units made. Found by the event-year sweep, task dc17-all.
- Likely a duplicate of existing entry dc17-badge (same maker, same event, same badge); flagged for review, not merged per research guide.
- Sound-reactive badge (Freescale MC56F8006 + MEMS mic + RGB LED) issued in seven puzzle-piece role shapes; ~6,694 units made. Found by the event-year sweep, task general-2006.
- This entry duplicates dc17-official-badge, another stub sourced from the same sweep and the same maker page (grandideastudio.com/portfolio/other/defcon-17-badge). Both describe the identical badge.
status: listed
sources:
- kind: url
  url: https://grandideastudio.com/portfolio/other/defcon-17-badge/
  title: DEF CON 17 Official Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc17-all); event read as ''dc17''.'
- kind: url
  url: https://grandideastudio.com/portfolio/other/defcon-17-badge/
  title: DEF CON 17 Badge - Grand Idea Studio portfolio
  accessed: '2026-09-08'
  note: Confirmed shapes, MCU (MC56F8006), RGB LED, MEMS mic, CR2032 power, 6,694 units made, and that design files/source are published.
- kind: url
  url: https://defcon.org/images/defcon-17/dc-17-presentations/defcon-17-joe-grand-making_the_dc17_badge.pdf
  title: Making the DEFCON 17 Badge (Joe Grand presentation, DEF CON 17)
  accessed: '2026-09-08'
  note: PDF is largely image-based; could not extract further confirming text beyond title/author metadata.
- kind: url
  url: https://badge.gallery/badges/def-con-17-badge
  title: DEF CON 17 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2006); event read as ''dc17''.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Maker's own portfolio page confirms all core facts already recorded by the sweep. Price was not stated anywhere found; badges were given free to registered attendees by category, so price/price_usd left empty. This entry appears to duplicate dc17-badge (same maker, same event, same description) -- reported as duplicate_of rather than merged, per research guide (one entry per task). Merged with duplicate entry 'DEF CON 17 Badge' (dc17-badge).
last_modified_date: '2026-09-08'
redirect_from:
- /badges/dc17/badge/
---

The DEF CON 17 (2009) official badge, designed by Joe Grand (Kingpin) of Grand Idea Studio, took the form of seven interlocking puzzle-piece shapes -- one for each attendee category (human, goon, press, speaker, vendor, contest organizer, and uber) -- that fit together into a single large puzzle when assembled as a set. Each badge was built around a Freescale MC56F8006 16-bit digital signal controller, a Knowles Acoustics MEMS microphone, and a Kingbright RGB LED that reacted to ambient sound volume and frequency, cycling through a reactive "Party" mode, an idle color-cycling "Quiet" mode, and a low-power "Sleep" mode. Badges could also communicate with each other over a wired connection, and firmware was upgradeable via a serial bootloader. Power came from a single CR2032 coin cell.

Grand Idea Studio manufactured 6,694 units for distribution to registered attendees at DEF CON 17, with badge shape indicating the holder's registration category. The design was released as an open project: schematic, bill of materials, assembly drawing, test procedure, and CodeWarrior-format source code are published on Grand Idea Studio's portfolio page, encouraging attendees to modify or hack the hardware.

## Make your own

Grand Idea Studio's portfolio page for the badge hosts the full schematic, BOM, assembly drawing, test procedure, and source code (CodeWarrior format) needed to reproduce or modify the badge.

## Notes merged from the duplicate entry "DEF CON 17 Badge"

The DEF CON 17 badge (2009) was designed by Joe Grand (Kingpin) of Grand Idea Studio, continuing his run of DEF CON badges from 2006 through 2010. Built around a Freescale MC56F8006 16-bit digital signal controller and a Knowles MEMS microphone, the badge listens to the room and drives a Kingbright RGB LED through three states: a "party mode" that reacts live to ambient volume and frequency, a slower idle color cycle, and a sleep state to save the CR2032 coin cell. Badges could also talk to each other over a wired connection, and a serial bootloader let owners reflash the firmware.

Rather than a single design, the badge was cut into seven interlocking puzzle-piece shapes corresponding to attendee roles — Human, Goon, Press, Speaker, Vendor, Contest Organizer, and Uber — with 6,694 units produced in total as conference credentials, not sold at retail.

## Make your own

Grand Idea Studio has published the full schematic, bill of materials, assembly drawings, a test procedure, and the CodeWarrior-format firmware source for the badge on its portfolio page, alongside Joe Grand's "Making (and Hacking) the DEFCON 17 Badge" presentation slides.
