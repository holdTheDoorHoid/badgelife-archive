---
title: DEF CON 22 Conference Badge (Human)
id: dc22-official-badge-human
layout: badge
parent: DC22
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc22
year: 2014
makers:
- name: Parallax Inc.
  url: https://www.parallax.com/
  role: manufacturer
- name: Ryan Clarke (LosT)
  role: contest design
- name: Jon McPhalen (J0nnyMac)
  role: firmware/hardware design
summary: The Human-attendee variant of the DEF CON 22 official electronic badge, a Propeller-based board with capacitive touch, IR, and LEDs that doubled as the con's admission ticket and puzzle-contest platform.
functions: 'Functioned as both a conference entry ticket and the "They Live"-themed hacking contest tool: capacitive-touch letter pads and an IR transmitter/receiver let badges interact with each other and with contest infrastructure, working through layers of cryptology, social engineering, and programming challenges. Uber-badge winners received lifetime DEF CON admission.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - puzzle
  - ctf
tech:
  mcu: Propeller P8X32A
  leds: null
  display: null
  connectivity:
  - ir
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '14,000 assembled boards across 13 attendee-type variants'
  availability: unknown
  distribution:
  - free_drop
  where: Handed out at DEF CON 22 registration as the attendee's conference badge; the Human badge was the standard general-attendee variant (others included Uber, Press, Vendor, Goon, Speaker, Artist, and Contest).
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.parallax.com/defcon-22-conference-badge
  url: https://www.parallax.com/defcon-22-conference-badge/
  kind: website
images:
- file: assets/images/badges/dc22/official-badge-human/18514f01d1.jpg
  source: "https://www.parallax.com/defcon-22-conference-badge/"
  credit: "Parallax Inc."
  caption: "DEF CON 22 badge, front view"
- file: assets/images/badges/dc22/official-badge-human/2d3135c74d.jpg
  source: "https://www.parallax.com/defcon-22-conference-badge/"
  credit: "Parallax Inc."
  caption: "DEF CON 22 badge, additional view"
contact: {}
notes:
- Official electronic conference badge for DEF CON 22 (2014), Propeller P8X32A-based with capacitive-touch letters, IR, and 13 attendee-type variants (Human, Uber, Press, Vendor, Goon, Speaker, Artist, Contest); designed around the con's 'They Live' theme. Found by the event-year sweep, task dc22-all.
- The sweep's title used "Official Badge"; Parallax's own page calls it the "DEFCON 22 Conference Badge," so the title was updated to match the maker's wording.
- A sibling entry, dc22-badge (DEF CON 22 Badge), covers the same overall Parallax design; this entry is specifically the Human (general-attendee) variant. Not merged, since the archive tracks per-variant entries for this badge family.
status: listed
sources:
- kind: url
  url: https://www.parallax.com/defcon-22-conference-badge/
  title: DEFCON 22 Conference Badge | Parallax Inc.
  accessed: '2026-09-08'
  note: 'Maker page confirming badge design, MCU, IR/touch features, manufacture quantity (14,000 boards, 13 variants), and event/year; source of the two saved images.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Parallax's own page confirms the badge, its Propeller MCU, IR/touch features, and total production run, but does not break out per-variant details (colors, exact quantity of Human badges specifically, price/cost, or whether hardware/firmware files were released), so those fields are left empty rather than guessed. No LED count or display info was stated.
last_modified_date: '2026-09-08'
---

The DEF CON 22 Human badge was the general-attendee version of Parallax's official conference badge for DEF CON 22, held in August 2014. Parallax built roughly 14,000 assembled circuit boards across 13 attendee-type variants (Human, Uber, Press, Vendor, Goon, Speaker, Artist, Contest, and others), each running the same Propeller P8X32A-based hardware designed under DEF CON founder Jeff Moss with contest lead Ryan Clarke (LosT) and Parallax's Jon McPhalen (J0nnyMac).

Beyond serving as the physical ticket into the conference, the badge was the platform for that year's "They Live"-themed hacking contest: capacitive-touch letter pads and an infrared transmitter/receiver let badges communicate with each other and with contest stations, and solving the layered puzzle (spanning cryptology, social engineering, and programming) could earn a holder of the Uber badge lifetime admission to DEF CON. The board also broke out USB programming access and general I/O, power, and ground pins so attendees could keep hacking on it after the con.

Parallax's own product page does not state a retail price (badges were distributed with registration, not sold separately) or say whether the hardware and firmware were ever published; those details were left blank pending better sources.
