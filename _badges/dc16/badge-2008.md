---
title: DEF CON 16 Badge (2008)
id: dc16-badge-2008
layout: badge
parent: DC16
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc16
year: 2008
makers:
- name: Joe Grand (Grand Idea Studio)
  url: https://grandideastudio.com/portfolio/other/defcon-16-badge/
summary: 'The official DEF CON 16 (2008) electronic badge: an open, hackable PCB built around a Freescale MC9S08JM60 microcontroller with IR badge-to-badge communication, an SD card slot, and a USB bootloader.'
functions: 'Three push-button modes: Receive (IR), Transmit/TV-B-Gone (IR remote-control emulation for shutting off TVs when no SD card is inserted), and Sleep. Reads/writes a FAT16-formatted SD card for data storage. Hosted an official Badge Hacking Contest with 20 entries, including a webcam-tracked "Human Password Generator" (winner), Apple Front Row/HP remote emulation, a cellular-automaton simulator, and a badge-hosted web server.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - radio
tech:
  mcu: MC9S08JM60
  leds: null
  display: none
  connectivity:
  - ir
  - usb
  battery: CR123A 3V lithium
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: '8500'
  availability: free
  distribution:
  - free_drop
  where: Distributed to DEF CON 16 attendees, staff, and other roles as their conference badge; not sold separately.
make_your_own:
  open_source: yes
  hardware_url: https://grandideastudio.com/media/dc16_bdg_schematic.pdf
  firmware_url: https://grandideastudio.com/media/dc16_bdg_source.zip
  eda_tool: null
links:
- label: grandideastudio.com/portfolio/other/defcon-16-badge
  url: https://grandideastudio.com/portfolio/other/defcon-16-badge/
  kind: website
- label: 'Making the DEFCON 16 Badge (Nuts & Volts, March 2009)'
  url: https://www.nutsvolts.com/index.php?/magazine/article/making_the_defcon_16_badge
  kind: article
- label: Badge Hacking Contest entries (Front Row Badge, GitHub)
  url: https://github.com/bkerley/dc16_badge/
  kind: repo
- label: DEF CON 16 Contest Results (official)
  url: https://www.defcon.org/html/defcon-16/dc-16-contest-results.html
  kind: doc
images:
- file: assets/images/badges/dc16/badge-2008/ef9410ce00.jpg
  source: "https://grandideastudio.com/portfolio/other/defcon-16-badge/"
  credit: "Grand Idea Studio"
  caption: "DEF CON 16 badge, main product photo"
- file: assets/images/badges/dc16/badge-2008/19633e5a62.jpg
  source: "https://grandideastudio.com/portfolio/other/defcon-16-badge/"
  credit: "Grand Idea Studio"
  caption: "DEF CON 16 badge, secondary photo"
contact: {}
notes:
- Official DEF CON 16 electronic badge built around a Freescale MC9S08JM60 microcontroller with IR transceiver (badge-to-badge data passing), SD card slot and USB bootloader; 8,500 units made in 8 role-denoting variants (Human, Goon, Staff, Press, Speaker, Vendor, Contest Organizer, Uber). Found by the event-year sweep, task dc16-all.
- Title and core facts confirmed directly by the maker's own portfolio page; wording of the sweep's one-line note matched the maker's description closely, so no title correction was needed.
status: released
sources:
- kind: url
  url: https://grandideastudio.com/portfolio/other/defcon-16-badge/
  title: DEF CON 16 Badge (2008)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc16-all); event read as ''dc16''.'
- kind: url
  url: https://grandideastudio.com/portfolio/other/defcon-16-badge/
  title: 'Grand Idea Studio: DEFCON 16 Badge'
  accessed: '2026-09-08'
  note: 'Full page fetch confirming MCU, IR/SD/USB-bootloader features, CR123A battery, 8,500-unit run across 8 role variants, distribution as free attendee badge, documentation links, and product photos.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: LED count/type not stated by the maker beyond referencing LEDs used in a contest entry's motion-tracking hack, so tech.leds is left empty. Price is not applicable/not published since the badge was distributed free to attendees rather than sold. No disagreement found between sources.
last_modified_date: '2026-09-08'
---

The DEF CON 16 badge was designed by Joe Grand of Grand Idea Studio for the 2008 edition of DEF CON, continuing his run of annual official badge designs for the conference. It is built around a Freescale Flexis MC9S08JM60 8-bit microcontroller and was deliberately built with "open" circuitry so attendees could study and modify it. The badge supports infrared transmission and reception for badge-to-badge interaction, reads and writes a FAT16-formatted SD card, and can be reflashed in the field through a USB bootloader. A single CR123A 3V lithium battery powers the board, and a single push-button cycles through three states: Receive, Transmit (which doubles as a TV-B-Gone-style universal TV-off remote when no SD card is present), and Sleep.

Grand Idea Studio manufactured 8,500 badges for the event, produced in eight soldermask/silkscreen and text-cutout variants that denoted different attendee roles: Human, Goon, Staff, Press, Speaker, Vendor, Contest Organizer, and Uber (the last awarded to winners of official DEF CON contests). The badges were given to attendees as their conference credential rather than sold.

As with other years, Grand Idea Studio ran an official Badge Hacking Contest over the weekend; 20 entries were submitted. The winning entry, by the Greek Geeks, was a "Human Password Generator" that used a webcam to track the motion of the badge's LEDs, hashed the resulting motion profile on a laptop, and sent it back to the badge over USB to compute a password. Other notable entries emulated Apple Front Row and HP laptop remote controls over IR, simulated Wolfram-style cellular automata with results stored on the SD card, and turned the badge into a small web server serving static content from its SD card.

## Make your own

Grand Idea Studio has published full documentation for the badge on its portfolio page: schematic, bill of materials, assembly drawing, test procedure (with video), Freescale CodeWarrior source code, a USB virtual serial port driver, and a "Care & Feeding Guide." A related infrared test unit (schematic, Gerbers, and BASIC Stamp 2sx source) used during development is documented as well. Several contest entries' project files are also linked from the same page, including the GitHub-hosted "Front Row Badge" firmware.
