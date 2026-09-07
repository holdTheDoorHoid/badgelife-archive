---
title: Dragon Badge
id: other-dragon-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2025
makers:
- name: Abhinav Pandagale / Hackerware.io
  url: https://hackerware.io
summary: A dragon-shaped conference badge made by Hackerware.io for SINCON Singapore 2025, built around an onboard CTF that attendees solve over a USB serial connection to light up their own hand-soldered LEDs.
functions: 'An 8-stage CTF played over a USB-C serial connection (Arduino IDE serial monitor at 9600 baud): each solved challenge unlocks one of 8 LEDs until the badge lights up fully. Challenges mix classic ciphers (Bacon cipher, a runic substitution cipher, ROT13, base64, a letter-position cipher, a T9/phone-keypad cipher, rail-fence cipher), a semaphore-flag image, hidden text in the badge''s own Gerber files, and audio steganography (steghide) on a hidden "dragon roar" WAV file. The CTF''s puzzle trail and a hidden flag reference the Dragon Playground at Toa Payoh, Singapore. Before the CTF starts, attendees hand-solder their own 1206 SMD LEDs onto the board at a soldering table.'
look:
  colors:
  - orange
  - white
  - purple
  - blue
  shape: dragon
  themes:
  - fantasy
  - ctf
  - puzzle
  - security
  form_factor: pcb badge
tech:
  mcu: null
  leds:
    count: 8
    type: 1206 SMD LED
    note: Attendee-soldered at a con soldering table; each LED is unlocked by solving one CTF stage over serial.
  display: none
  connectivity:
  - usb
  battery: CR2032 coin cell
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Handed out to attendees at the SINCON Singapore 2025 registration/main counter.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: astikrawat.medium.com/sincon-sg-2025-ctf-walkthrough-of-dragon-badge-by-hackerware-io-1efb31322f10
  url: https://astikrawat.medium.com/sincon-sg-2025-ctf-walkthrough-of-dragon-badge-by-hackerware-io-1efb31322f10
  kind: website
- label: hackerware.io/sincon2025
  url: https://hackerware.io/sincon2025
  kind: website
- label: 'Hackerware.io: SINCON Dragon Badge soldering tutorial (PDF)'
  url: https://www.hackerware.io/sincon-dragon-solder.pdf
  kind: doc
- label: 'Hackerware.io: SINCON Dragon Badge CTF setup guide (PDF)'
  url: https://www.hackerware.io/sincon-dragon-ctf.pdf
  kind: doc
images:
  - file: assets/images/badges/other/dragon-badge/d11acba280.jpg
    source: "https://hackerware.io/sincon2025"
    credit: "Hackerware.io"
    caption: "The SINCON 2025 Dragon Badge, front"
  - file: assets/images/badges/other/dragon-badge/babd10469b.png
    source: "https://astikrawat.medium.com/sincon-sg-2025-ctf-walkthrough-of-dragon-badge-by-hackerware-io-1efb31322f10"
    credit: "Astik Rawat"
    caption: "Dragon Badge with all 8 LEDs lit after completing the CTF"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- 'Made for SINCON Singapore 2025 (May 2025); no matching event id exists yet in _data/events.yml, so this stays filed under "other". Silkscreen on the board reads "SINCON 2025 Badge By Hackerware.io".'
- Exact MCU/USB-serial chip part numbers are not legible/stated in any source found; left blank rather than guessed.
status: released
sources:
- kind: url
  url: https://astikrawat.medium.com/sincon-sg-2025-ctf-walkthrough-of-dragon-badge-by-hackerware-io-1efb31322f10
  title: 'SINCON SG 2025: CTF Walkthrough of Dragon Badge by hackerware.io'
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''SINCON SG 2025''. Full walkthrough of the 8 CTF stages, soldering step, and badge photos.'
- kind: url
  url: https://hackerware.io/sincon2025
  title: Welcome To Hackerware - The SINCON Dragon CTF Badge
  accessed: '2026-09-07'
  note: Maker's own project page confirming it is SINCON's third conference badge, with an onboard interactive CTF; links to the soldering and CTF-setup PDFs and a front-view photo.
- kind: url
  url: https://www.hackerware.io/sincon-dragon-solder.pdf
  title: The SINCON Dragon Badge - Soldering Tutorial
  accessed: '2026-09-07'
  note: Confirms the badge ships pre-soldered except for the 1206 SMD LEDs attendees solder themselves; shows silkscreen text "SINCON 2025 Badge By Hackerware.io", CR2032 coin cell, USB-C port, and on/off switch.
- kind: url
  url: https://www.hackerware.io/sincon-dragon-ctf.pdf
  title: The SINCON Dragon Badge - CTF Interfacing
  accessed: '2026-09-07'
  note: Confirms 8 challenges/8 LEDs, USB-C + Arduino IDE serial monitor at 9600 baud, and the RESET command.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Core facts (maker, event, year, CTF mechanics, LED count, battery, connector) confirmed from the maker's own project page and PDFs plus a detailed third-party walkthrough. No storefront, price, quantity made, MCU part number, or open-source design files were found, so those fields are left empty. No matching SINCON event id exists in _data/events.yml.
last_modified_date: '2026-09-07'
---

The Dragon Badge is the third conference badge made by Hackerware.io (Abhinav Pandagale) for SINCON Singapore, issued at the 2025 event. Shaped like a stylized dragon in orange and white silkscreen, it runs on a CR2032 coin cell behind an on/off switch and connects to a computer over USB-C. Rather than shipping fully assembled, attendees solder their own row of eight 1206 SMD LEDs onto the underside at a conference soldering table before the badge does anything.

Once soldered, the badge only flashes its LEDs for a three-second preview until the attached CTF is solved. Plugging it into a computer (with the badge switched off first) and opening a serial terminal at 9600 baud unlocks an 8-stage puzzle trail mixing classic ciphers (Bacon, ROT13, a runic alphabet, rail-fence, a T9-style phone cipher), a semaphore-flag image, hidden text buried in the badge's own published Gerber files, and steganography hidden in an audio file of a dragon roar. Each correct answer lights one more LED, and the puzzle trail traces a tribute to Toa Payoh's real-world Dragon Playground in Singapore.

No storefront, price, or production quantity was found for this badge — it appears to have been distributed free to attendees at SINCON 2025's registration desk rather than sold, and no hardware or firmware files have been published as open source.
