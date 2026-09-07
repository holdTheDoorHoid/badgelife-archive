---
title: The FALKEN Wombat Badge 2
id: bsides-adelaide-2025-the-falken-wombat-badge-2
layout: badge
parent: BSides Adelaide 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-adelaide-2025
year: 2025
makers:
- name: Hackerware.io (Abhinav SP)
  url: https://hackerware.io/
summary: 'The second Wombat Badge for BSides Adelaide: a cable-free CTF badge where players solve crypto puzzles and enter the answers as 10-bit binary flags on two buttons.'
functions: 'Onboard CTF: press the CTF button, then enter a 10-bit binary flag using the "1" and "0" buttons to solve each of 7 challenges (A-G, plus a hidden 8th unlocked with "1010101010"). Correct flags light the matching challenge LED. Holding "1" and "0" together resets the challenges. A slide switch gives a 3-second preview of the display. Challenges reportedly include Morse code, the Bacon cipher, Brainfuck, and a Vigenere cipher.'
look:
  colors: []
  shape: null
  themes:
  - animal
  - robot
  - cyberpunk
  - ctf
  - puzzle
tech:
  mcu: null
  leds:
    count: 8
    type: discrete
    note: 7 small solder-it-yourself challenge LEDs plus 1 two-pin RGB LED that shows a random pattern
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to BSides Adelaide 2025 attendees; assembled/soldered in a hardware village at the con.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.hackster.io/HacksFromPanda/the-falken-wombat-badge-2-bsides-adelaide-e15fbd
  url: https://www.hackster.io/HacksFromPanda/the-falken-wombat-badge-2-bsides-adelaide-e15fbd
  kind: article
- label: hackerware.io/wombat2
  url: https://hackerware.io/wombat2
  kind: website
  archived: false
- label: 'semaja2.net: BSides Adelaide 2025 Hardware Badge Writeup'
  url: https://semaja2.net/2025/05/14/bsides-adelaide-2025-badge-writeup/
  kind: article
  archived: false
images:
- file: assets/images/badges/bsides-adelaide-2025/the-falken-wombat-badge-2/5937669d7d.jpg
  source: "https://hackerware.io/wombat2"
  credit: "Hackerware.io"
  caption: "The FALKEN Wombat Badge 2, BSides Adelaide 2025"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://www.hackster.io/HacksFromPanda/the-falken-wombat-badge-2-bsides-adelaide-e15fbd
  title: The FALKEN Wombat Badge 2
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''BSides Adelaide 2025 (no matching event id in events.yml)''.'
- kind: url
  url: https://hackerware.io/wombat2
  title: The BSides Adelaide Wombat-2 CTF Badge
  accessed: '2026-09-07'
  note: "Maker's own page; confirms maker, CTF mechanic, LED layout (7 solder-your-own challenge LEDs + 1 two-pin RGB LED), buttons, reset gesture, hidden challenge, and image."
- kind: url
  url: https://semaja2.net/2025/05/14/bsides-adelaide-2025-badge-writeup/
  title: BSides Adelaide 2025 Hardware Badge Writeup
  accessed: '2026-09-07'
  note: "Third-party attendee writeup; confirms 7 challenges (A-G) plus secret 8th, cipher types used (Morse, Bacon, Brainfuck, Vigenere), and that badges were distributed at the con."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The hackster.io story page (original source) returned a Cloudflare block and could not be read directly; content was instead confirmed via the maker''s own hackerware.io/wombat2 page and a third-party attendee writeup. MCU/chip, display, connectivity, power/battery, SAO support, price, quantity made, and open-source status are not stated on either accessible source and are left empty. The event id bsides-adelaide-2025 already exists in events.yml and matches, so no correction was needed. This is the second badge in the Wombat series; the original 2024 Wombat Badge (also by Hackerware.io) is a separate item — see other_items_found.'
last_modified_date: '2026-09-07'
---

The FALKEN Wombat Badge 2 is the second entry in Hackerware.io's Wombat Badge series, made by Abhinav SP for BSides Adelaide 2025. It follows the original 2024 Wombat Badge, and its artwork reworks the wombat mascot into a mechanical, steampunk-tinged robot set against a background of cascading Matrix-style binary code, in a nod to the film *WarGames* ("FALKEN").

Unlike the first Wombat Badge, this version drops the USB tether entirely: the badge runs its CTF game standalone. Players press a dedicated CTF button and then enter a 10-bit binary flag using two buttons labeled "1" and "0" to solve each of seven crypto challenges (labeled A through G), plus a hidden eighth challenge unlocked by entering "1010101010". Reported puzzle types include Morse code, the Bacon cipher, Brainfuck, and a Vigenere cipher. A correct flag instantly lights the matching challenge LED; holding both buttons down resets progress. The badge carries seven small LEDs that attendees solder on themselves as part of a hardware village at the conference, plus a single two-pin RGB LED that runs a random idle pattern. It was given out to BSides Adelaide 2025 attendees rather than sold.

Chip/MCU, display, connectivity, power source, SAO support, price, and total quantity made are not stated on the pages that could be read for this entry and are left blank pending better sources.
