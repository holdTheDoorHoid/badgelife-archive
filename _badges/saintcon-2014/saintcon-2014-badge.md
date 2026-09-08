---
title: SAINTCON 2014 Badge
id: saintcon-2014-saintcon-2014-badge
layout: badge
parent: SAINTCON 2014
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: saintcon-2014
year: 2014
makers:
- name: Luke Jenkins and Klint Holmes
summary: An unpopulated Arduino-Uno-clone badge that SAINTCON 2014 attendees soldered together themselves, then hacked through five progressive firmware challenges at the Hardware Hacking Village.
functions: 'Five-stage "hack the badge" challenge run over a serial terminal menu: (1) a serial terminal interface, (2) an IR receiver (Vishay TSOP382), (3) an IR transmitter diode (Vishay TSAL4400) for sending codes, (4) an NTC 10k thermistor analog sensor, and (5) a Microchip 24LC01B I2C EEPROM. An optional $15 daughterboard added tri-color LEDs with PWM drivers for blinky effects.'
look:
  colors: []
  shape: null
  themes:
  - learn to solder
  - hardware tool
  - village badge
  - puzzle
tech:
  mcu: ATmega328 (Arduino Uno clone)
  leds: null
  display: null
  connectivity:
  - ir
  - i2c
  battery: null
  sao_version: null
get_one:
  price: free (badge kit); $15 optional blinky daughterboard
  price_usd: null
  quantity: '400+'
  availability: unknown
  distribution:
  - free_drop
  where: Given to all 400+ SAINTCON 2014 attendees at conference registration in Ogden, Utah.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: 'Design files and firmware were shared via Weber State University''s Box drive (weberstate.app.box.com/badge); the link was live as of the 2014 writeups but was not independently verified as still reachable.'
links:
- label: datko.net/2014/10/24/hacking_saintcon_badge
  url: https://datko.net/2014/10/24/hacking_saintcon_badge/
  kind: website
- label: hackaday.com/2014/10/28/saintcon-badge-badge-hacking-for-mortals
  url: https://hackaday.com/2014/10/28/saintcon-badge-badge-hacking-for-mortals/
  kind: article
- label: badge.gallery/series/saintcon
  url: https://badge.gallery/series/saintcon
  kind: website
images:
  - file: assets/images/badges/saintcon-2014/saintcon-2014-badge/521b801c25.jpg
    source: "https://datko.net/2014/10/24/hacking_saintcon_badge/"
    credit: "Josh Datko / datko.net"
    caption: "The unpopulated badge and kit as it came in the registration bag"
  - file: assets/images/badges/saintcon-2014/saintcon-2014-badge/d4d6c5929e.jpg
    source: "https://datko.net/2014/10/24/hacking_saintcon_badge/"
    credit: "Josh Datko / datko.net"
    caption: "Completed badge assembled with the optional blinky daughterboard"
contact: {}
notes:
- The official SAINTCON 2014 conference badge, an unpopulated Arduino-clone circuit board (inspired by SparkFun's RedBoard) that attendees soldered together at the Hardware Hacking Village with five progressive firmware challenges. Found by the event-year sweep, task saintcon-2014.
- 'Title matches how the sweep and secondary sources refer to it; no maker-given product name was found beyond "the SAINTCON badge."'
- 'Availability today (still findable, sold, etc.) could not be confirmed; this was a free conference giveaway in 2014, not a storefront item, so `availability: unknown` reflects lack of current-day info rather than doubt it existed.'
- 'The Weber State Box link for design files/firmware (weberstate.app.box.com/badge) was reported live in 2014 coverage but was not fetched/verified in this pass, so `hardware_url`/`firmware_url` are left empty rather than guessed.'
status: released
sources:
- kind: url
  url: https://datko.net/2014/10/24/hacking_saintcon_badge/
  title: SAINTCON 2014 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2014); event read as ''saintcon-2014''.'
- kind: url
  url: https://hackaday.com/2014/10/28/saintcon-badge-badge-hacking-for-mortals/
  title: SAINTCON Badge (Badge Hacking For Mortals)
  accessed: '2026-09-08'
  note: Confirmed the unpopulated-board design, challenge structure, and Weber State file-sharing distribution of design files.
- kind: url
  url: https://badge.gallery/series/saintcon
  title: SAINTCON · Hacker Con Badges
  accessed: '2026-09-08'
  note: Corroborating summary confirming Arduino-compatible design, FTDI programming, blinky daughterboard, and hidden challenges.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core facts (maker, event, five-stage challenge, unpopulated Arduino-clone design, free distribution to 400+ attendees, $15 blinky daughterboard) are confirmed by a first-hand attendee writeup (Josh Datko, datko.net) and corroborated by Hackaday and badge.gallery. No maker-run storefront or GitHub repo was found, so tech.mcu is inferred only as "ATmega328 (Arduino Uno clone)" from the Arduino-Uno-clone description, not a datasheet; exact LED count/type on the daughterboard and current-day availability of the Box design-file link were not confirmed, so those fields are left empty/unknown.'
last_modified_date: '2026-09-08'
---

The SAINTCON 2014 badge, designed by Luke Jenkins and Klint Holmes, was an unpopulated Arduino-Uno-clone circuit board handed out to all 400-plus attendees of SAINTCON (Ogden, Utah, October 20-23, 2014) at registration. Rather than a working device out of the box, it was a soldering exercise: attendees assembled the board themselves at the conference's Hardware Hacking Village, run by Matt Lorimer, before it would do anything.

Once built, the badge doubled as a "hack the badge" puzzle with five progressive stages accessed through a serial terminal menu: a terminal interface, an IR receiver, an IR transmitter, an NTC thermistor, and an I2C EEPROM, each unlocking the next piece of hardware and firmware to work with. Roughly 123 attendees completed the first challenge and 59 finished all five; conference-goer and security researcher Josh Datko documented the process and was reportedly the first to finish. A $15 optional daughterboard added tri-color LEDs with PWM drivers for blinky effects. Design files and firmware were shared through a Weber State University Box folder, in keeping with the badge's goal of being an approachable, beginner-friendly alternative to more elaborate hacker-con badges like DEF CON's.

## Make your own

No verified, currently-reachable repository or file mirror was found in this pass; the original distribution point (weberstate.app.box.com/badge) is cited in 2014-era coverage but was not checked for continued availability.
