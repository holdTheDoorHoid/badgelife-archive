---
title: Anime CTF Badge
id: other-anime-ctf-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2022
makers:
- name: Hackerware.io
  url: https://www.hackster.io/HacksFromPanda
  role: designer/maker (Abhinav SP)
summary: A CTF badge shaped like an anime character (Dragon Ball-style, glowing red eyes and fists) made for Raytheon's CTF at the 2022 Texas Cyber Summit; players plug it into micro-USB and solve a filesystem-themed serial console challenge to light up sets of "superpower" LEDs.
functions: Serial-based capture-the-flag game over a micro-USB/UART connection at 9600 baud (terminal set to Both NL & CR). Sending three asterisks (***) starts CTF mode; the challenge is themed as a filesystem to explore for clues. Correct flags light different LED groups (representing anime "superpowers"); a secret flag unlocks a blinky animation mode. Sending RESET and reconnecting factory-resets the badge. The coin cell must be removed to play the CTF and reinserted afterward to keep the blinky mode.
look:
  colors:
  - red
  - blue
  - yellow
  - black
  - clear
  themes:
  - anime
  - pop culture
  - ctf
  - security
  form_factor: pcb badge
tech:
  mcu: ABOV A96S174
  leds:
    count: 10
    type: reverse-mount SMD
    note: 2 red, 4 yellow, 4 blue LEDs reverse-mounted to glow through the PCB (eyes and "aura" effect) behind a clear epoxy front
  display: none
  connectivity:
  - usb
  - uart
  battery: CR2032 (backup/blinky-mode power; removed during CTF play, which is powered over micro-USB)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Made for Raytheon's CTF at Texas Cyber Summit 2022; distribution to attendees not specified by the source.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.hackster.io/HacksFromPanda/anime-ctf-badge-afcb2c
  url: https://www.hackster.io/HacksFromPanda/anime-ctf-badge-afcb2c
  kind: article
- label: www.facebook.com/Hackerwares/posts/launching-in-texas-cyber-summit-is-the-ctf-badge-from-raytheon-intelligence-spac/470490485103516
  url: https://www.facebook.com/Hackerwares/posts/launching-in-texas-cyber-summit-is-the-ctf-badge-from-raytheon-intelligence-spac/470490485103516/
  kind: website
images:
- file: assets/images/badges/other/anime-ctf-badge/842e367b9d.jpg
  source: https://www.hackster.io/HacksFromPanda/anime-ctf-badge-afcb2c
  credit: Abhinav SP / Hackerware.io
  caption: The Anime CTF Badge, front view, with reverse-mounted LEDs lit behind the character and flame-shaped clear-epoxy background
- file: assets/images/badges/other/anime-ctf-badge/b71b65439b.jpg
  source: https://www.hackster.io/HacksFromPanda/anime-ctf-badge-afcb2c
  credit: Abhinav SP / Hackerware.io
  caption: Rear of the badge, showing the CH340G USB-serial chip, ABOV A96S174 MCU, CR2032 holder, micro-USB port, and 'MADE BY HACKERWARE.IO' handwriting alongside Raytheon's CODEX branding
- file: assets/images/badges/other/anime-ctf-badge/34ccbb0c9d.jpg
  source: https://www.hackster.io/HacksFromPanda/anime-ctf-badge-afcb2c
  credit: Abhinav SP / Hackerware.io
  caption: Front of the Anime CTF Badge, showing the anime character artwork and reverse-mounted SMD LEDs
- file: assets/images/badges/other/anime-ctf-badge/15022b13c7.jpg
  source: https://www.hackster.io/HacksFromPanda/anime-ctf-badge-afcb2c
  credit: Abhinav SP / Hackerware.io
  caption: The badge lit up in the full set of unlocked LED colors after solving the CTF
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- Made for Raytheon Intelligence & Space's "CODEX" CTF at the Texas Cyber Summit (Texas Cyber Summit is not currently a distinct event in this archive's events list, so the event field is left as 'other').
- An anime-styled capture-the-flag badge sponsored by Raytheon Intelligence & Space, launched at Texas Cyber Summit 2022, unlocking abilities as flags are solved. Found by the event-year sweep, task con-blue-team-con.
- Maker Hackster.io post titles it "Anime CTF Badge"; retitled from the sweep's generic "Texas Cyber Summit 2022 CTF Badge" to match.
- 'Possible duplicate: an existing entry other-anime-ctf-badge ("Anime CTF Badge", maker Hackerware.io) filed under event "other" appears to be the same badge; it should likely be merged into this event-specific entry.'
status: released
sources:
- kind: url
  url: https://www.hackster.io/HacksFromPanda/anime-ctf-badge-afcb2c
  title: Anime CTF Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''unclear''.'
- kind: url
  url: http://web.archive.org/web/20231211085509/https://www.hackster.io/HacksFromPanda/anime-ctf-badge-afcb2c
  title: Anime CTF Badge (Wayback Machine snapshot, 2023-12-11)
  accessed: '2026-09-07'
  note: Live hackster.io page returned a Cloudflare block; used this archived snapshot for the write-up, components list, maker credit, event/maker context, and image URLs (published date, MCU, LEDs, CTF mechanics).
- kind: url
  url: https://www.facebook.com/Hackerwares/posts/launching-in-texas-cyber-summit-is-the-ctf-badge-from-raytheon-intelligence-spac/470490485103516/
  title: Texas Cyber Summit 2022 CTF Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-blue-team-con); event read as ''Texas Cyber Summit 2022''.'
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched the Wayback snapshot directly (WebFetch could not reach web.archive.org, so used curl) and confirmed maker (Abhinav SP / Hackerware.io, "College dropout artist, hacker and entrepreneur ... Founder, Hackerware.io"), full CTF mechanics (9600 baud, Both NL & CR, "***" to start, filesystem theme, RESET to factory-reset, secret flag unlocks blinky mode, reinsert coin cell), and the full components list (custom PCB, micro-USB B, 2 red/4 yellow/4 blue SMD LEDs reverse-mounted, CH340G SOIC16, 12.000 MHz crystal, ABOV A96S174, CR2032 holder) verbatim against the "Things used" and "Story" sections. Publish date (September 22, 2022) confirms year 2022. The Raytheon Intelligence & Space "CODEX" branding is not named anywhere in the archived page text (only generic "Raytheon" appears) but is directly visible, legibly, in the rear-PCB photo (silkscreen reading "CODEX" with the Raytheon Intelligence & Space logo) saved as this entry''s second image, so
    that detail is confirmed by the photo rather than the prose. No pricing, quantity-made, or distribution details were given by the source, so those fields are left empty. No SAO header is mentioned; treated as a standalone badge. Design files (hardware/firmware) are not published as far as this source shows. Both saved images were matched against attachments on the same project page. Merged with duplicate entry ''Anime CTF Badge'' (texas-cyber-summit-2022-texas-cyber-summit-2022-ctf-badge).'
last_modified_date: '2026-09-08'
redirect_from:
- /badges/texas-cyber-summit-2022/texas-cyber-summit-2022-ctf-badge/
---

The Anime CTF Badge is a hardware capture-the-flag challenge built by Abhinav SP of Hackerware.io for Raytheon Intelligence & Space's "CODEX" CTF at the 2022 Texas Cyber Summit. Shaped like an anime character (a Dragon Ball-style fighter with glowing eyes and clenched fists, backed by a flame-shaped clear-epoxy panel), the badge reverse-mounts red, yellow, and blue SMD LEDs so light diffuses through the PCB itself for the eyes and "aura" effect, rather than shining from the front.

To play, participants remove the CR2032 coin cell, connect the badge over micro-USB, and open a serial terminal at 9600 baud. Sending three asterisks starts CTF mode, which presents a filesystem-themed set of directories and clues; correct answers light different LED colors tied to the character's "superpowers," while a hidden flag switches the badge into a standalone blinky-animation mode (at which point the coin cell can be reinserted to keep it glowing after disconnecting). A RESET command lets a stuck player factory-reset and start over. The board is built around an ABOV A96S174 microcontroller with a CH340G USB-to-serial chip, a 12 MHz crystal, and ten reverse-mounted LEDs.

No information on production quantity, price, or how the badge was distributed to Texas Cyber Summit attendees was found in the source material, and hardware/firmware design files do not appear to be published.

## Notes merged from the duplicate entry "Anime CTF Badge"

Raytheon Intelligence & Space sponsored this capture-the-flag badge for Texas Cyber Summit 2022, commissioning Abhinav SP of Hackerware.io to build it around an anime theme where solving flags "unlocks superpowers." The badge is built around an ABOV A96S174 microcontroller with a CH340G USB-to-serial chip, and reverse-mounts ten SMD LEDs (two red, four yellow, four blue) behind a clear-epoxy anime-character face so light diffuses through the front artwork and the character's eyes.

To play, a wearer removes the CR2032 coin cell, plugs in a micro-USB cable, and talks to the badge over a serial terminal at 9600 baud. Sending three asterisks starts the CTF, which is framed as a filesystem to explore; correct flags progressively light the red, yellow, and then blue LED groups, a hidden flag unlocks a blinky animation mode, and sending "RESET" factory-resets the badge. Once the blue-LED flag is solved, players are told to reinsert the coin cell before disconnecting so the unlocked state persists.

No pricing, production quantity, or open-source hardware/firmware files were published alongside the write-up.
