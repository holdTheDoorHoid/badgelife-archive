---
title: DEF CON 22 Badge
id: dc22-badge
layout: badge
parent: DC22
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc22
year: 2014
makers:
- name: Parallax
  url: https://www.parallax.com/defcon-22-conference-badge/
  role: manufacturer / PCB assembly
- name: Ryan Clarke / LosT
  role: contest lead, concept
- name: Jon McPhalen / J0nnyMac
  role: Propeller firmware
- name: Jeff Moss / The Dark Tangent
  role: badge direction (DEF CON founder)
summary: The official electronic badge for DEF CON 22 (2014), a Propeller 1-based board with infrared transmit/receive, capacitive touch-pad buttons, LEDs, and a full USB programming circuit, produced in thirteen attendee-role styles for a "They Live"-themed puzzle contest.
functions: Infrared communication between badges, capacitive-touch input, LED indicators/animations, and a hacking contest involving cryptology, social engineering, and programming built around the badge's hardware and hidden functions.
look:
  colors: []
  shape: null
  themes:
  - puzzle
  - ctf
  - security
tech:
  mcu: Propeller 1 (P8X32A)
  leds: null
  display: none
  connectivity:
  - ir
  - usb
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: approximately 14,000 units (reported variously as ~13,600-17,000 across sources)
  availability: not_released
  distribution:
  - free_drop
  where: Issued as the conference entry credential to DEF CON 22 attendees, staff, speakers, press, vendors, and contest participants in one of thirteen role-specific styles; not sold separately.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://forums.parallax.com/discussion/156782/defcon-22-badge-code-schematics-and-information-here/
  eda_tool: null
links:
- label: badge.gallery/badges/def-con-22-badge
  url: https://badge.gallery/badges/def-con-22-badge
  kind: website
- label: www.parallax.com/defcon-22-conference-badge
  url: https://www.parallax.com/defcon-22-conference-badge/
  kind: store
- label: Parallax forums - DEFCON 22 Badge Code, Schematics and Information
  url: https://forums.parallax.com/discussion/156782/defcon-22-badge-code-schematics-and-information-here/
  kind: repo
- label: Parallax - DEFCON 22 Badges Have Been Communicating for Almost Ten Years
  url: https://www.parallax.com/defcon-22-badges-have-been-communicating-for-almost-ten-years/
  kind: article
- label: Hackaday - Hands-On DEFCON 22 Badge
  url: https://hackaday.com/2014/08/07/hands-on-defcon-22-badge/
  kind: article
images:
- file: assets/images/badges/dc22/badge/18514f01d1.jpg
  source: https://www.parallax.com/defcon-22-conference-badge/
  credit: Parallax
  caption: DEF CON 22 badge, front view
- file: assets/images/badges/dc22/badge/b743afd769.jpg
  source: https://www.parallax.com/defcon-22-conference-badge/
  credit: Parallax
  caption: DEF CON 22 badge, alternate style variant
- file: assets/images/badges/dc22/badge/18514f01d1.jpg
  source: https://www.parallax.com/defcon-22-conference-badge/
  credit: Parallax Inc.
  caption: DEF CON 22 badge, front view
- file: assets/images/badges/dc22/badge/2d3135c74d.jpg
  source: https://www.parallax.com/defcon-22-conference-badge/
  credit: Parallax Inc.
  caption: DEF CON 22 badge, additional view
contact: {}
notes:
- Sweep-imported wording was "Propeller 1-based badge with IR, touch buttons and USB programming in 13 role styles, ~14,000 units, tied to a 'They Live' puzzle theme." Confirmed against badge.gallery, Parallax's own product page, the Parallax forums thread, and Hackaday coverage.
- This entry duplicates dc22-official-badge-human (same maker team, same badge, same event) — that entry covers the "Human" attendee-role variant specifically; this one is the general/unspecified-role listing.
- Official electronic conference badge for DEF CON 22 (2014), Propeller P8X32A-based with capacitive-touch letters, IR, and 13 attendee-type variants (Human, Uber, Press, Vendor, Goon, Speaker, Artist, Contest); designed around the con's 'They Live' theme. Found by the event-year sweep, task dc22-all.
- The sweep's title used "Official Badge"; Parallax's own page calls it the "DEFCON 22 Conference Badge," so the title was updated to match the maker's wording.
- A sibling entry, dc22-badge (DEF CON 22 Badge), covers the same overall Parallax design; this entry is specifically the Human (general-attendee) variant. Not merged, since the archive tracks per-variant entries for this badge family.
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/def-con-22-badge
  title: DEF CON 22 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2006); event read as ''dc22''.'
- kind: url
  url: https://www.parallax.com/defcon-22-conference-badge/
  title: DEFCON 22 Conference Badge - Parallax
  accessed: '2026-09-08'
  note: Maker's own product page; confirmed MCU, IR, touch buttons, USB programming, and provided badge images.
- kind: url
  url: https://forums.parallax.com/discussion/156782/defcon-22-badge-code-schematics-and-information-here/
  title: 'DEFCON 22 Badge: Code, Schematics and Information'
  accessed: '2026-09-08'
  note: Maker's forum thread with code, schematics, and background; confirms 60-day turnaround and ~14,000 units made in Rocklin, CA.
- kind: url
  url: https://www.parallax.com/defcon-22-badges-have-been-communicating-for-almost-ten-years/
  title: DEFCON 22 Badges Have Been Communicating for Almost Ten Years - Parallax
  accessed: '2026-09-08'
  note: Retrospective Parallax post; cites 17,000 units built (differs from the 14,000 figure elsewhere).
- kind: url
  url: https://hackaday.com/2014/08/07/hands-on-defcon-22-badge/
  title: Hands-On DEFCON 22 Badge - Hackaday
  accessed: '2026-09-08'
  note: Independent press coverage confirming the Propeller-based hardware and contest tie-in.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Core facts (maker, chip, features, event/year, ~14,000 units) confirmed on Parallax''s own pages and corroborated by Hackaday. Sources disagree on exact unit count: Parallax''s product page and forum say ~14,000, a Parallax retrospective post says 17,000, and a YouTube video says 13,600 - recorded as a range rather than guessed at a single number. No price is available since the badge was issued as the conference credential, not sold. LED count/type and exact PCB colors were not stated by any source found and are left empty. This entry substantially duplicates dc22-official-badge-human; both describe the same Parallax/LosT/J0nnyMac DEF CON 22 badge family. Merged with duplicate entry ''DEF CON 22 Conference Badge (Human)'' (dc22-official-badge-human).'
last_modified_date: '2026-09-08'
redirect_from:
- /badges/dc22/official-badge-human/
---

Parallax built the official DEF CON 22 badge for the 2014 conference at the Rio in Las Vegas, working from a Propeller 1 (P8X32A) microcontroller. The badge carried an infrared transmitter and receiver for badge-to-badge communication, capacitive touch-pad buttons, LEDs, and a full USB programming circuit with exposed I/O, ground, and power pins so attendees could reprogram or hack the hardware directly. Design direction came from DEF CON founder Jeff Moss, the badge/contest concept from Ryan Clarke ("LosT"), and the Propeller firmware from Jon McPhalen ("J0nnyMac"). The badge was built around that year's "They Live" theme and drove a hacking contest mixing cryptology, social engineering, and programming puzzles.

Parallax had only about 60 days from being invited onto the project to delivering finished hardware, and manufactured roughly 14,000 assembled boards at its Rocklin, California facility (a later Parallax retrospective cites 17,000, and other secondary sources cite 13,600 - the exact final count is inconsistently reported). The badges were produced in thirteen attendee-role styles (including Human, Uber, Press, Vendor, Goon, Speaker, Artist, and Contest variants) and served as attendees' conference credential rather than being sold separately.

## Make your own

Parallax published code, schematics, and background information for the badge on its community forums, including Propeller Spin/C examples and third-party "BadgeHacker" customization tooling built by the community. No dedicated hardware/Gerber repository was found in this pass; the forum thread is the best entry point for anyone wanting to reproduce or reprogram the badge's firmware.

## Notes merged from the duplicate entry "DEF CON 22 Conference Badge (Human)"

The DEF CON 22 Human badge was the general-attendee version of Parallax's official conference badge for DEF CON 22, held in August 2014. Parallax built roughly 14,000 assembled circuit boards across 13 attendee-type variants (Human, Uber, Press, Vendor, Goon, Speaker, Artist, Contest, and others), each running the same Propeller P8X32A-based hardware designed under DEF CON founder Jeff Moss with contest lead Ryan Clarke (LosT) and Parallax's Jon McPhalen (J0nnyMac).

Beyond serving as the physical ticket into the conference, the badge was the platform for that year's "They Live"-themed hacking contest: capacitive-touch letter pads and an infrared transmitter/receiver let badges communicate with each other and with contest stations, and solving the layered puzzle (spanning cryptology, social engineering, and programming) could earn a holder of the Uber badge lifetime admission to DEF CON. The board also broke out USB programming access and general I/O, power, and ground pins so attendees could keep hacking on it after the con.

Parallax's own product page does not state a retail price (badges were distributed with registration, not sold separately) or say whether the hardware and firmware were ever published; those details were left blank pending better sources.
