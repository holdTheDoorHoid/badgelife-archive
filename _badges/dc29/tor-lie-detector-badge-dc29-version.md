---
title: TOR Lie Detector Badge (DC29 version)
id: dc29-tor-lie-detector-badge-dc29-version
layout: badge
parent: DC29
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc29
year: 2021
makers:
- name: Seeess
  url: https://github.com/seeess
- name: gigs
summary: A wearable mini polygraph sold to raise donations for the Tor Project at DEF CON 29, using a GSR finger-cuff sensor and a heart-rate sensor to graph stress responses on dual OLED screens.
functions: Lie Detector mode graphs live GSR (galvanic skin response) and heart-rate/BPM data on two OLED screens; includes Cheat Modes (e.g. Fake Pulse) to simulate or hide a reading, a Calibration mode, a "Bad Defcon Advice" mode with 46 sarcastic tips, and a Name Scroll mode that scrolls a user-entered nickname or the Tor logo.
look:
  colors: []
  shape: null
  themes:
  - privacy
  - security
  - measurement
  - hardware tool
tech:
  mcu: SAMD21 Cortex M0+ (Seeeduino XIAO)
  leds:
    count: null
    type: reverse-mount
    note: Onboard XIAO LEDs plus a reverse-mounted green LED for the heart-rate sensor.
  display: Two 1.3" I2C blue OLEDs
  connectivity:
  - usb
  - i2c
  inputs:
  - potentiometer
  battery: 2x AA (boosted to 3.3V), or USB-C
  sao_version: v1.69bis
  sao_ports: 1
get_one:
  price: $500 donation to the Tor Project
  price_usd: 500
  quantity: ~200
  availability: sold_out
  distribution:
  - crowdfunding
  where: Offered via a donation of $500 to the Tor Project (through donate.torproject.org) from around November 2021 through December 13, 2021; also sold at the Hacker Warehouse vendor booth at DEF CON 29 itself. Limited to roughly 200 units, all profits went to the Tor Project.
make_your_own:
  open_source: true
  hardware_url: https://github.com/seeess/Defcon-Tor-29-Badge
  firmware_url: https://github.com/seeess/Defcon-Tor-29-Badge/blob/main/Defcon-Tor-29-Badge.ino
  eda_tool: null
links:
- label: github.com/stevemats/lie_detector_badge
  url: https://github.com/stevemats/lie_detector_badge
  kind: repo
- label: github.com/seeess/Defcon-Tor-29-Badge
  url: https://github.com/seeess/Defcon-Tor-29-Badge
  kind: repo
- label: Tor Project forum - DEF CON 29 badges available
  url: https://forum.torproject.org/t/tor-project-tor-def-con-29-badges-available-limited-time/1032
  kind: article
- label: DEF CON Forums - 2021 Defcon Tor Badge
  url: https://forum.defcon.org/node/237393
  kind: article
- label: 'Video: Hooked to a Lie Detector [Tor Badge] | DEF CON 29 #badgelife'
  url: https://www.youtube.com/watch?v=etposyGihNA
  kind: video
- label: 'Video: Defcon Tor Project Lie Detector Badge Overview'
  url: https://www.youtube.com/watch?v=aaRbma9SlGY
  kind: video
- label: gigsatdc.com/dc29/torbadge_walkthrough.php
  url: https://gigsatdc.com/dc29/torbadge_walkthrough.php
  kind: website
- label: Gigs Badge and PCB Design portfolio
  url: https://gigsbadge.com/
  kind: website
images:
- file: assets/images/badges/dc29/tor-lie-detector-badge-dc29-version/242da92ae2.jpg
  source: https://github.com/seeess/Defcon-Tor-29-Badge
  credit: Seeess
  caption: The DC29 Tor Lie Detector badge, worn on a lanyard with finger-cuff sensor cable
- file: assets/images/badges/dc29/tor-lie-detector-badge-dc29-version/9ae84b93d8.jpg
  source: https://gigsbadge.com/
  credit: Gigs
  caption: Tor Polygraph Badge (DEF CON 29)
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- The github.com/stevemats/lie_detector_badge link in the original sources appears to be a mirror/fork; the maker's canonical repo is github.com/seeess/Defcon-Tor-29-Badge, added here.
- Re-released for later DEF CONs as separate archive entries (dc31-lie-detector-badge-re-release-of-dc29, dc32-tor-lie-detector-badge) — not duplicates of this DC29 original.
- Sweep sourced this from Gigs's own DC29 challenge-walkthrough page and titled the entry "DC 29 Tor Badge"; the maker's own name for the badge is "Tor Polygraph (Lie Detector) Badge".
- This is the same badge as the existing entry dc29-tor-lie-detector-badge-dc29-version (Seeess, gigs); left as a separate file per task instructions, flagged as duplicate.
- Price and production quantity were not stated on the sources checked (maker portfolio, GitHub README, walkthrough page).
status: released
sources:
- kind: url
  url: https://github.com/stevemats/lie_detector_badge
  title: TOR Lie Detector Badge (DC29 version)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc29''.'
- kind: url
  url: https://github.com/seeess/Defcon-Tor-29-Badge
  title: 'GitHub - seeess/Defcon-Tor-29-Badge: code and manual for the defcon 29 electronic Tor badge'
  accessed: '2026-09-07'
  note: Maker's own repo and README; source for MCU, display, LEDs, battery, features, badge photo.
- kind: url
  url: https://forum.torproject.org/t/tor-project-tor-def-con-29-badges-available-limited-time/1032
  title: Tor DEF CON 29 badges available, limited time
  accessed: '2026-09-07'
  note: Source for price ($500 donation), quantity (~200), deadline, and second maker name (gigs).
- kind: url
  url: https://forum.defcon.org/node/237393
  title: 2021 Defcon Tor Badge
  accessed: '2026-09-07'
  note: Corroborates DEF CON 29 vendor-booth sale.
- kind: url
  url: https://gigsatdc.com/dc29/torbadge_walkthrough.php
  title: DC 29 Tor Badge Challenge Walkthrough
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass; confirms the puzzle/challenge side of the badge and that Gigs made the challenge.
- kind: url
  url: https://gigsbadge.com/
  title: Gigs Badge and PCB Design
  accessed: '2026-09-10'
  note: Maker's own summary of the Tor Polygraph Badge, attribution (Gigs = PCB/hardware, SeeEss = software/marketing), and the item photo.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Core facts (maker, MCU, sensors, price, quantity, distribution window) confirmed via the maker's own GitHub README and the Tor Project's own forum post. LED count not stated precisely by the source ("4 onboard xiao LEDs plus a green heart-rate LED" - left count null since it mixes onboard MCU LEDs with a dedicated sensor LED). Series/EDA tool/gerbers not found. Merged with duplicate entry 'Tor Polygraph (Lie Detector) Badge' (dc29-dc-29-tor-badge).
last_modified_date: '2026-09-10'
redirect_from:
- /badges/dc29/dc-29-tor-badge/
---

The Tor Lie Detector Badge was an electronic wearable mini polygraph created by Seeess (with gigs) and sold to benefit the Tor Project around DEF CON 29 in 2021. Built on a Seeeduino XIAO (SAMD21 Cortex M0+), it pairs a galvanic skin response (GSR) finger-cuff sensor with a heart-rate/pulse sensor, graphing both signals live across two 1.3" I2C OLED screens. Beyond straight lie-detection, the badge includes cheat modes (like faking a calm pulse), a calibration mode, a joke "Bad Defcon Advice" mode with dozens of sarcastic tips, and a name-scroll mode.

Rather than being sold directly, badges were offered to anyone who donated $500 to the Tor Project through its official donation page, with a limited run of roughly 200 units available from around November 2021 through a December 13, 2021 cutoff; some were also sold in person at the Hacker Warehouse vendor booth at DEF CON 29. All proceeds went to the Tor Project, and the maker developed the badge without compensation. Hardware documentation and Arduino firmware are published on GitHub, and the badge proved popular enough to be re-released for later DEF CONs (tracked as separate archive entries for DC31 and DC32).

## Make your own

The firmware (`Defcon-Tor-29-Badge.ino`) and a full build/usage manual are published at github.com/seeess/Defcon-Tor-29-Badge, including wiring notes for the SAMD21 XIAO, the dual OLEDs (I2C addresses 0x78/0x7A), the GSR potentiometer calibration, and the Arduino libraries required (ss_oled, Adafruit_SleepyDog, FlashStorage_SAMD) to compile and flash the badge yourself.

## Notes merged from the duplicate entry "Tor Polygraph (Lie Detector) Badge"

The Tor Polygraph (Lie Detector) Badge was sold at the Hacker Warehouse vendor booth at DEF CON 29 (2021), with all profits donated to the Tor Project. It works as a miniature lie detector: an optical heart-rate sensor (a reverse-mounted green LED read through a fingertip) and a galvanic skin response sensor feed two 1.3" I2C OLED displays that graph the wearer's readings live. Hardware and PCB design were handled by Gigs (@gigstaggart); SeeEss (@see_ess) wrote most of the software and led marketing. It runs on a SAMD21-based Seeeduino XIAO, is powered by two AA batteries boosted to 3.3V (with a USB-C option), and carries a single SAO 1.69bis header.

Beyond the sensor gimmick, the badge doubled as the entry point to a seven-layer crypto/puzzle challenge that Gigs designed and later documented in a public walkthrough: a Konami-code-triggered help menu, morse code printed along the lanyard, Game Genie codes, a Vigenère cipher, What3Words geolocation encoding, and a custom "onion layer" cipher, ending at a web-based challenge page. Firmware and schematics are open-sourced in SeeEss's GitHub repository.

This entry was created from the challenge-walkthrough page alone and is the same physical badge already catalogued as `dc29-tor-lie-detector-badge-dc29-version`; see that entry's notes for any differences in how the two records describe it.
