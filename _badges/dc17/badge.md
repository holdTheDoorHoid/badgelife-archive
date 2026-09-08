---
title: DEF CON 17 Badge
id: dc17-badge
layout: badge
parent: DC17
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc17
year: 2009
makers:
- name: Joe Grand / Grand Idea Studio
  url: https://grandideastudio.com/portfolio/other/defcon-17-badge/
summary: 'The official DEF CON 17 (2009) conference badge: an active electronic badge whose RGB LED reacts to ambient sound, issued in seven interlocking puzzle-piece role shapes.'
functions: 'Three operating states: Party mode (RGB LED responds to audio volume and frequency picked up by an onboard MEMS microphone), Quiet/Idle (LED cycles through colors), and Sleep. Supports wired badge-to-badge communication and a serial bootloader for firmware updates.'
look:
  colors: []
  shape: null
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
  quantity: '6,694 units'
  availability: unknown
  distribution:
  - free_drop
  where: Issued as conference credentials to attendees, goons, press, speakers, vendors, contest organizers, and staff at DEF CON 17; not sold commercially.
make_your_own:
  open_source: yes
  hardware_url: https://grandideastudio.com/media/dc17_bdg_schematic.pdf
  firmware_url: https://grandideastudio.com/media/dc17_bdg_source.zip
  bom_url: https://grandideastudio.com/media/dc17_bdg_bom.pdf
  eda_tool: null
  notes: 'Grand Idea Studio also published assembly drawings, a test procedure, presentation slides, and a "haiku" writeup for this badge.'
links:
- label: badge.gallery/badges/def-con-17-badge
  url: https://badge.gallery/badges/def-con-17-badge
  kind: website
- label: grandideastudio.com/portfolio/other/defcon-17-badge
  url: https://grandideastudio.com/portfolio/other/defcon-17-badge/
  kind: website
- label: dc17_bdg_slides.pdf (Making and Hacking the DEFCON 17 Badge)
  url: https://grandideastudio.com/wp-content/uploads/dc17_bdg_slides.pdf
  kind: doc
images:
- file: assets/images/badges/dc17/badge/26a346acb2.jpg
  source: "https://grandideastudio.com/portfolio/other/defcon-17-badge/"
  credit: "Grand Idea Studio"
  caption: "DEF CON 17 badge, front"
- file: assets/images/badges/dc17/badge/8b64578d93.jpg
  source: "https://grandideastudio.com/portfolio/other/defcon-17-badge/"
  credit: "Grand Idea Studio"
  caption: "DEF CON 17 badge, back / components"
contact: {}
notes:
- Sound-reactive badge (Freescale MC56F8006 + MEMS mic + RGB LED) issued in seven puzzle-piece role shapes; ~6,694 units made. Found by the event-year sweep, task general-2006.
- 'This entry duplicates dc17-official-badge, another stub sourced from the same sweep and the same maker page (grandideastudio.com/portfolio/other/defcon-17-badge). Both describe the identical badge.'
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/def-con-17-badge
  title: DEF CON 17 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2006); event read as ''dc17''.'
- kind: url
  url: https://grandideastudio.com/portfolio/other/defcon-17-badge/
  title: 'Grand Idea Studio: DEFCON 17 Badge'
  accessed: '2026-09-08'
  note: Maker's own portfolio page; confirmed chip, mic, LED, battery, quantity, seven role shapes, and published design/firmware files.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Core facts (chip, mic, LED, quantity, seven role shapes, distribution as a free conference credential) confirmed on the maker''s own portfolio page. No price is documented since it was not sold. Duplicate of dc17-official-badge, which was created from the same maker page under a different sweep task; the two entries should likely be merged.'
last_modified_date: '2026-09-08'
---

The DEF CON 17 badge (2009) was designed by Joe Grand (Kingpin) of Grand Idea Studio, continuing his run of DEF CON badges from 2006 through 2010. Built around a Freescale MC56F8006 16-bit digital signal controller and a Knowles MEMS microphone, the badge listens to the room and drives a Kingbright RGB LED through three states: a "party mode" that reacts live to ambient volume and frequency, a slower idle color cycle, and a sleep state to save the CR2032 coin cell. Badges could also talk to each other over a wired connection, and a serial bootloader let owners reflash the firmware.

Rather than a single design, the badge was cut into seven interlocking puzzle-piece shapes corresponding to attendee roles — Human, Goon, Press, Speaker, Vendor, Contest Organizer, and Uber — with 6,694 units produced in total as conference credentials, not sold at retail.

## Make your own

Grand Idea Studio has published the full schematic, bill of materials, assembly drawings, a test procedure, and the CodeWarrior-format firmware source for the badge on its portfolio page, alongside Joe Grand's "Making (and Hacking) the DEFCON 17 Badge" presentation slides.
