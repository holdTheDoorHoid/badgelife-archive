---
title: Anime CTF Badge
id: texas-cyber-summit-2022-texas-cyber-summit-2022-ctf-badge
layout: badge
parent: Texas Cyber Summit 2022
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: texas-cyber-summit-2022
year: 2022
makers:
- name: Abhinav SP / Hackerware.io
  url: https://www.hackster.io/HacksFromPanda
summary: A CTF badge in anime-character design, sponsored by Raytheon Intelligence & Space for Texas Cyber Summit 2022, that lights up reverse-mounted SMD LEDs as "superpowers" as each flag is solved over a serial console.
functions: 'Plays a filesystem-themed CTF over a serial terminal (USB, 9600 baud, both NL & CR): sending three asterisks starts the challenge, correct answers progressively light red, yellow, and blue LED groups, a hidden flag triggers a blinky animation mode, and "RESET" factory-resets the badge.'
look:
  colors:
  - clear
  - multicolor
  shape: null
  themes:
  - anime
  - ctf
  - security
tech:
  mcu: ABOV A96S174
  leds:
    count: 10
    type: reverse-mount
    note: 2 red, 4 yellow, and 4 blue SMD LEDs, reverse-mounted to shine through the PCB and clear epoxy front.
  display: none
  connectivity:
  - usb
  battery: CR2032 (removed while playing the CTF over USB)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given out at Texas Cyber Summit 2022, sponsored by Raytheon Intelligence & Space.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.facebook.com/Hackerwares/posts/launching-in-texas-cyber-summit-is-the-ctf-badge-from-raytheon-intelligence-spac/470490485103516
  url: https://www.facebook.com/Hackerwares/posts/launching-in-texas-cyber-summit-is-the-ctf-badge-from-raytheon-intelligence-spac/470490485103516/
  kind: website
- label: 'Hackster.io: Anime CTF Badge'
  url: https://www.hackster.io/HacksFromPanda/anime-ctf-badge-afcb2c
  kind: hackaday
images:
- file: assets/images/badges/texas-cyber-summit-2022/texas-cyber-summit-2022-ctf-badge/34ccbb0c9d.jpg
  source: https://www.hackster.io/HacksFromPanda/anime-ctf-badge-afcb2c
  credit: Abhinav SP / Hackerware.io
  caption: Front of the Anime CTF Badge, showing the anime character artwork and reverse-mounted SMD LEDs
- file: assets/images/badges/texas-cyber-summit-2022/texas-cyber-summit-2022-ctf-badge/15022b13c7.jpg
  source: https://www.hackster.io/HacksFromPanda/anime-ctf-badge-afcb2c
  credit: Abhinav SP / Hackerware.io
  caption: The badge lit up in the full set of unlocked LED colors after solving the CTF
contact: {}
notes:
- An anime-styled capture-the-flag badge sponsored by Raytheon Intelligence & Space, launched at Texas Cyber Summit 2022, unlocking abilities as flags are solved. Found by the event-year sweep, task con-blue-team-con.
- 'Maker Hackster.io post titles it "Anime CTF Badge"; retitled from the sweep''s generic "Texas Cyber Summit 2022 CTF Badge" to match.'
- 'Possible duplicate: an existing entry other-anime-ctf-badge ("Anime CTF Badge", maker Hackerware.io) filed under event "other" appears to be the same badge; it should likely be merged into this event-specific entry.'
status: released
sources:
- kind: url
  url: https://www.facebook.com/Hackerwares/posts/launching-in-texas-cyber-summit-is-the-ctf-badge-from-raytheon-intelligence-spac/470490485103516/
  title: Texas Cyber Summit 2022 CTF Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-blue-team-con); event read as ''Texas Cyber Summit 2022''.'
- kind: url
  url: https://www.hackster.io/HacksFromPanda/anime-ctf-badge-afcb2c
  title: Anime CTF Badge - Hackster.io
  accessed: '2026-09-08'
  note: Maker's project write-up; confirmed maker, event/sponsor, MCU, LEDs, battery, USB CTF mechanic, and images.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: No price, quantity produced, or open-source hardware/firmware files were found; the maker's write-up does not link a repo or Gerbers. Likely duplicates existing entry other-anime-ctf-badge, filed under event "other" — see duplicate_of in the report.
last_modified_date: '2026-09-08'
---

Raytheon Intelligence & Space sponsored this capture-the-flag badge for Texas Cyber Summit 2022, commissioning Abhinav SP of Hackerware.io to build it around an anime theme where solving flags "unlocks superpowers." The badge is built around an ABOV A96S174 microcontroller with a CH340G USB-to-serial chip, and reverse-mounts ten SMD LEDs (two red, four yellow, four blue) behind a clear-epoxy anime-character face so light diffuses through the front artwork and the character's eyes.

To play, a wearer removes the CR2032 coin cell, plugs in a micro-USB cable, and talks to the badge over a serial terminal at 9600 baud. Sending three asterisks starts the CTF, which is framed as a filesystem to explore; correct flags progressively light the red, yellow, and then blue LED groups, a hidden flag unlocks a blinky animation mode, and sending "RESET" factory-resets the badge. Once the blue-LED flag is solved, players are told to reinsert the coin cell before disconnecting so the unlocked state persists.

No pricing, production quantity, or open-source hardware/firmware files were published alongside the write-up.
