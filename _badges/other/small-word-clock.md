---
title: Small Word Clock
id: other-small-word-clock
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: other
year: 2019
makers:
- name: Shawn Maxwell
  url: https://hackaday.io/sjm4306
summary: A desktop word clock that spells out the time in lit-up words on a 12x10 LED matrix, built as a two-board sandwich with a laser/PCB-cut lettering mask over the LED board.
functions: Tells time as illuminated words; has several idle animation modes (chase, random, twinkle, pong, rain, bouncing ball, ripple) selectable with a button.
look:
  colors: []
  shape: rectangle
  themes:
  - minimalist
  - text
tech:
  mcu: PIC16F887
  leds:
    count: 120
    type: null
    note: 12x10 LED matrix behind a lettering mask, powered from USB 5V
  display: LED matrix 12x10
  connectivity: []
  battery: CR1220 (RTC backup)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: available
  distribution:
  - purchase
  - kit
  where: Sold as a DIY or pre-assembled kit through Makerfabs (partnership announced December 2019); design files are also free to build yourself.
make_your_own:
  open_source: yes
  hardware_url: https://hackaday.io/project/164406-small-word-clock
  firmware_url: https://hackaday.io/project/164406-small-word-clock
  eda_tool: null
links:
- label: hackaday.io/project/164406-small-word-clock
  url: https://hackaday.io/project/164406-small-word-clock
  kind: hackaday
images:
- file: assets/images/badges/other/small-word-clock/3105be0b00.jpg
  source: "https://hackaday.io/project/164406-small-word-clock"
  credit: "Shawn Maxwell (sjm4306)"
  caption: "Assembled Small Word Clock with LED word-display and 3D-printed light box"
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://hackaday.io/project/164406-small-word-clock
  title: Small Word Clock
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://hackaday.io/project/164406-small-word-clock
  title: Small Word Clock (project page, fetched)
  accessed: '2026-09-07'
  note: Maker, chip, LED matrix, RTC/battery, animation modes, and Makerfabs kit partnership confirmed via the project page.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This is not a hacker-conference badge or SAO -- it is Shawn Maxwell's (sjm4306) entry in the 2019 Hackaday Prize "Tell Time" contest, later sold as a DIY/assembled kit by Makerfabs. No matching con/event exists in events.yml, so event is left as "other". Could not confirm a current price or units-made figure; the Makerfabs product page returned a 404 when checked directly, so price/availability could not be independently verified beyond the project page's mention of the partnership.
last_modified_date: '2026-09-07'
---

The Small Word Clock is a desktop clock by Shawn Maxwell (Hackaday.io user sjm4306), built for the 2019 Hackaday Prize's "Tell Time" contest. Instead of digits, it spells out the time in illuminated words behind a laser- or PCB-cut lettering mask, using a 12x10 LED matrix driven by a PIC16F887 microcontroller. A DS1302 real-time clock with a CR1220 backup battery keeps time when the clock is unplugged, while the LEDs themselves run off USB 5V power. Three buttons let the owner set the hour and minute and cycle through seven idle animation modes -- chase, random, twinkle, pong, rain, bouncing ball, and ripple.

The design splits into two PCBs that snap together: a front board that acts as the lettering mask, and a rear board carrying the LEDs and microcontroller, separated by a 3D-printed light box that keeps light from bleeding between letters. Maxwell released the hardware (Gerbers), 3D-printable housing files (Solidworks/STL), and firmware (built with the HI-TECH C compiler for MPLab) as open source from the start. In December 2019 he partnered with Makerfabs, who began offering both DIY and pre-assembled kit versions for sale.

This is not a hacker-conference badge or SAO; it was pulled into the archive from a "SAOs to buy" link list. It has no tie to a specific con, so it is filed under the "other" event bucket rather than corrected to a con id.
