---
title: TOR Lie Detector Badge
id: dc32-tor-lie-detector-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
series: Tor Lie Detector Badge
makers:
- name: Seeess
  url: https://github.com/seeess
summary: A wearable "mini lie detector" for the Tor Project's DEF CON vendor booth, using a galvanic skin response (GSR) sensor and a heart-rate sensor to graph your body's stress response on two OLED screens.
functions: The GSR sensors helps you practice for your next fed interview, or out your fed friends
look:
  colors: []
  shape: null
  themes:
  - privacy
  - security
  - measurement
  - hardware tool
tech:
  mcu: SAMD21 (Seeeduino XIAO)
  leds: null
  display: 2x 1.3" I2C OLED
  connectivity:
  - usb
  - i2c
  inputs:
  - buttons
  battery: 2x AA (boosted to 3.3V), or USB-C
  sao_version: v1.69bis
get_one:
  price: $150.00
  price_usd: 150.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Tor Project vendor booth at DEF CON 32
make_your_own:
  open_source: yes
  hardware_url: https://github.com/seeess/Defcon-Tor-31-Badge
  firmware_url: https://github.com/seeess/Defcon-Tor-31-Badge
  eda_tool: null
  license: WTFPL
  notes: No DEF CON 32-specific repository was found; the linked repo is the DC31 "re-run" of this same design, which is the most recent documented version.
links:
- label: github.com/seeess
  url: https://github.com/seeess
  kind: repo
- label: twitter.com/see_ess
  url: https://twitter.com/see_ess
  kind: social
- label: "Defcon-Tor-31-Badge (most recent documented version of this design)"
  url: https://github.com/seeess/Defcon-Tor-31-Badge
  kind: repo
  note: "DC31 README: 're-run from dc29 since we keep selling out.' Describes the GSR + heart-rate sensor, dual OLED, SAMD21 XIAO hardware."
- label: "Defcon-Tor-29-Badge (original release)"
  url: https://github.com/seeess/Defcon-Tor-29-Badge
  kind: repo
  note: Original Tor lie-detector badge, sold at the Hacker Warehouse vendor booth at DC29.
images:
- file: assets/images/badges/dc32/tor-lie-detector-badge/242da92ae2.jpg
  source: "https://github.com/seeess/Defcon-Tor-31-Badge"
  credit: "Seeess"
  caption: "The Tor Lie Detector Badge, showing the dual 1.3-inch OLED screens, GSR finger-cuff cable, and heart-rate sensor pad (photo from the DC31 re-release, same design)"
contact: {}
notes:
- These will be available at the TOR Booth in the vendor area
- 'This is the same "Lie Detector Badge" series Seeess/Tor Project has sold since DC29 (see dc31-lie-detector-badge-re-release-of-dc29), not the separate, simpler "TOR Mini Badge" also listed for DC32 (dc32-tor-mini-badge, GitHub repo Defcon-Tor-32) which has no sensors.'
status: listed
sources:
- kind: sheet
  event: dc32
  row: 93
  updated: '2024-06-11'
- kind: url
  url: https://github.com/seeess
  title: seeess (GitHub profile)
  accessed: '2026-09-06'
  note: Confirms maker's repos, including a distinct Defcon-Tor-32 ("mini-badge") repo separate from this lie-detector line.
- kind: url
  url: https://github.com/seeess/Defcon-Tor-31-Badge
  title: "Defcon-Tor-31-Badge README"
  accessed: '2026-09-06'
  note: "Most recent documented version of the Tor lie-detector badge design: GSR + heart-rate sensors, dual 1.3\" OLED, SAMD21 Seeeduino XIAO, 2x AA or USB-C power, 1.69bis SAO header, WTFPL license, function text matching the DC32 sheet entry's wording."
- kind: url
  url: https://github.com/seeess/Defcon-Tor-29-Badge
  title: "Defcon-Tor-29-Badge README"
  accessed: '2026-09-06'
  note: Confirms this is the original release of the lie-detector design (DC29), sold at the Hacker Warehouse vendor booth, with identical GSR/heart-rate description.
- kind: url
  url: https://github.com/seeess/Defcon-Tor-32
  title: "Defcon-Tor-32 README (Tor mini-badge)"
  accessed: '2026-09-06'
  note: Confirms this is a DIFFERENT DC32 product by the same maker (5-LED ATtiny402 SAO, no sensors) - ruled out as the source of this entry's GSR/lie-detector functions text.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: >-
    No DC32-specific repository or storefront page for the lie-detector badge was found, so the
    exact 2024 hardware revision, price, and quantity are unconfirmed. Tech/hardware fields above
    are drawn from the DC31 "re-run" repo (the most recent documented iteration of this same
    design, explicitly a re-release of DC29), which shares this entry's maker, event series
    (Tor Project vendor booth), and near-identical functions text ("practice ... fed interview").
    The community sheet's $150 price and quantity could not be independently verified against any
    maker-published page; kept as originally entered. Twitter/X profile (twitter.com/see_ess ->
    x.com/see_ess) returned an access-restricted response and could not be checked. This session's
    web search budget was exhausted before a broader search for a DC32-specific listing could be
    run, so a dedicated 2024 storefront page, if one exists, was not found.
last_modified_date: '2026-09-06'
---

The Tor Lie Detector Badge is a running joke-turned-tradition at the Tor Project's DEF CON vendor booth: a wearable "mini lie detector" combining a galvanic skin response (GSR) sensor and a heart-rate sensor, with live readings graphed on two 1.3" OLED screens. Finger cuffs clip onto two fingers to read skin conductance while a reverse-mounted LED/photodiode pair on the board reads pulse from a fingertip. The badge is built around a Seeeduino XIAO (SAMD21 Cortex-M0+), runs off two AA batteries (boosted to 3.3V) or USB-C, and connects to a host badge through a keyed 1.69bis SAO header. Proceeds from sales go to the Tor Project; the maker, who goes by Seeess, has stated they do not charge for their own time.

The design debuted at DEF CON 29 sold at the Hacker Warehouse booth, and proved popular enough that it was "re-run" essentially unchanged (aside from an OLED driver swap) at DEF CON 31. The DEF CON 32 community sheet lists a "TOR Lie Detector Badge" from the same maker at the Tor booth for $150, with functions text ("helps you practice for your next fed interview, or out your fed friends") that closely echoes the DC29/DC31 README's own description. No DC32-specific repository, storefront listing, or price confirmation was found, so it is documented here using the DC31 repo as the best available source for its technical design, while price and quantity are left as reported on the sheet. This is a distinct product from the simpler "TOR Mini Badge" (a 5-LED ATtiny402 SAO with two button games) that the same maker also brought to DC32.

## Make your own

Firmware and hardware documentation for the most recent version of this design are published on GitHub under the WTFPL license (see `Defcon-Tor-31-Badge`). It's built around a Seeeduino XIAO (Arduino IDE, SAMD21 board package), with GSR and heart-rate sensing handled in the badge's own firmware and three third-party Arduino libraries (`ss_oled`, `Adafruit_SleepyDog`, `FlashStorage_SAMD`) driving the dual OLEDs and low-power sleep. Raw sensor data is also streamed over USB serial for viewing in the Arduino Serial Plotter.

## History

Part of Seeess's recurring "Tor badge" line for the Tor Project's DEF CON vendor booth, which has included several distinct designs across years: a simple onion-shaped SAO (DC27, DC30), this GSR/heart-rate "lie detector" (DC29, re-released DC31, and evidently offered again at DC32 per the sheet), and a separate minimalist LED-blinky SAO ("TOR Mini Badge," DC32).
