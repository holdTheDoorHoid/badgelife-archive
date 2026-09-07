---
title: Persistence of Vision POV Display SAO
id: supercon-2024-persistence-of-vision-pov-display-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Michael Yim
  url: https://hackaday.io/cowtheory
summary: A hand-waved SAO that uses an accelerometer to trigger a persistence-of-vision text display from 10 white LEDs, made as a Hackaday Supercon 8 SAO contest entry.
functions: Detects the wave motion of your hand with an ADXL345 accelerometer and blinks 5 front and 5 back white LEDs in time with the motion to draw a virtual 5-pixel by 12-character line of text (default message "SUPERCON8"). The message is customizable over I2C and supports A-Z, 0-9, space, and a few punctuation characters.
look:
  colors: []
  shape: rectangle
  themes:
  - text
  - hardware tool
tech:
  mcu: Padauk PFC232
  leds:
    count: 10
    type: discrete
    note: 5 white 0603 SMT LEDs on the front and 5 on the back, used for persistence-of-vision text
  display: none
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: null
get_one:
  price: free
  price_usd: null
  quantity: '128'
  availability: sold_out
  availability_note: 'Distributed free at Supercon 2024 (Nov 2024); no storefront listing found as of 2026-09-07.'
  distribution:
  - free_drop
  where: Given away to attendees at Hackaday Supercon 8 (2024) as a SAO contest entry.
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/198272-persistence-of-vision-pov-display-sao
  firmware_url: https://hackaday.io/project/198272-persistence-of-vision-pov-display-sao
  eda_tool: Eagle
links:
- label: hackaday.io/project/198272-persistence-of-vision-pov-display-sao
  url: https://hackaday.io/project/198272-persistence-of-vision-pov-display-sao
  kind: hackaday
images:
  - file: assets/images/badges/supercon-2024/persistence-of-vision-pov-display-sao/50eaf47118.jpg
    source: "https://hackaday.io/project/198272-persistence-of-vision-pov-display-sao"
    credit: "Michael Yim"
    caption: "The Persistence of Vision POV Display SAO, a hand-waved accelerometer-triggered LED text display"
  - file: assets/images/badges/supercon-2024/persistence-of-vision-pov-display-sao/0b020ccc69.jpg
    source: "https://hackaday.io/project/198272-persistence-of-vision-pov-display-sao"
    credit: "Michael Yim"
    caption: "Assembled batch of POV Display SAO boards from the production run"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198272-persistence-of-vision-pov-display-sao
  title: Persistence of Vision POV Display SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: supercon-addons); event read as ''Supercon 8 Add-On Contest — honorable mention''.'
- kind: url
  url: https://hackaday.io/project/198272-persistence-of-vision-pov-display-sao
  title: Persistence of Vision POV Display SAO - Hackaday.io project page
  accessed: '2026-09-07'
  note: 'Confirmed maker (Michael Yim / cowtheory), event (Supercon 8 SAO contest, 2024), specs (ADXL345 accelerometer, PFC232 MCU, 10x white 0603 LEDs), production run of 128 units given away free, and Eagle design files hosted on the project page.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Event corrected from supercon-2025 to supercon-2024: the project page states it was made for the Hackaday Supercon 8 SAO contest, which was Supercon 2024. No SAO header pin-count was stated on the page, so tech.sao_version is left null. No modern storefront or price beyond "free giveaway" was found, so get_one.price_usd is left null and availability is inferred as sold_out (one-off event giveaway, not a standing listing).'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/supercon-2025/persistence-of-vision-pov-display-sao/
---

The Persistence of Vision POV Display SAO is a shake-to-read add-on built by Michael Yim (Hackaday.io handle cowtheory) for the Supercon 8 SAO contest in 2024. Instead of a fixed display, it uses an ADXL345 accelerometer to sense when the wearer waves the board through the air, and fires 10 white 0603 LEDs (5 facing front, 5 facing back) in a timed sequence so the motion blur draws out a line of text — a classic persistence-of-vision trick shrunk down to badge-add-on size. A Padauk PFC232 microcontroller runs the show, and the default message reads "SUPERCON8"; the text is changeable over I2C and covers A-Z, 0-9, space, and a handful of punctuation marks.

Yim produced a run of 128 fully assembled units for the contest, with only 3 non-functional boards out of the whole batch, and gave them away free to attendees at Supercon 2024. The project page frames the SAO connection as purely a power source — the display itself doesn't communicate over the SAO's I2C bus with the host badge, it's driven independently by the onboard PFC232.

## Make your own

The Hackaday.io project page hosts the Eagle schematic (`POV Display SAO.sch`) and board layout (`POV Display SAO.brd`) along with datasheets for the PFC232 and ADXL345, so the hardware side is reproducible; no separate firmware repository or license was found, so `make_your_own.open_source` is recorded as partial rather than yes.
