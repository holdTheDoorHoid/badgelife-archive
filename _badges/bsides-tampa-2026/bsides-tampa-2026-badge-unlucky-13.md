---
title: BSides Tampa 2026 Badge (Unlucky 13)
id: bsides-tampa-2026-bsides-tampa-2026-badge-unlucky-13
layout: badge
parent: BSides Tampa 2026
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-tampa-2026
year: 2026
makers:
- name: Joshua Grose
  role: badge design and CTF
- name: c0ldbru
  role: badge build (per maker's LinkedIn post)
summary: The official 2026 BSides Tampa conference badge, an ATtiny1616-based board built around a hidden capture-the-flag puzzle.
functions: Runs a multi-stage crypto/puzzle CTF (Base64, pigpen and Hylian/Zelda-alphabet ciphers) spread across the badge, its lanyard, and a companion website; a Morse-blinking LED activates when two GPIO pins are bridged, and the badge exposes UART pads that leak a firmware dump used as one of the puzzle steps.
look:
  colors: []
  shape: null
  themes:
  - ctf
  - puzzle
  - pirate
  - pop culture
tech:
  mcu: ATtiny1616
  leds:
    count: null
    type: null
    note: At least one LED ("right eye") blinks Morse code when GPIO1 and GPIO2 are bridged.
  display: none
  connectivity:
  - uart
  battery: coin cell
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - contest
  where: Given to registered BSides Tampa 2026 attendees; not sold separately. Conference registration for 2026 is closed as of this check.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: mason-lee-101.github.io/blog/bsides-tampa-2026-badge-ctf
  url: https://mason-lee-101.github.io/blog/bsides-tampa-2026-badge-ctf/
  kind: website
- label: bsidestampa.net/activities/badge-challenge
  url: https://bsidestampa.net/activities/badge-challenge
  kind: website
  archived: https://web.archive.org/web/20260612202631/https://bsidestampa.net/activities/badge-challenge
- label: www.youtube.com/watch?v=q2zXdGrIu3E
  url: https://www.youtube.com/watch?v=q2zXdGrIu3E
  kind: video
images:
- file: assets/images/badges/bsides-tampa-2026/bsides-tampa-2026-badge-unlucky-13/f3a7083ecf.jpg
  source: https://mason-lee-101.github.io/blog/bsides-tampa-2026-badge-ctf/
  credit: Mason Lee (blog writeup)
  caption: Front of the BSides Tampa 2026 badge showing the CTF design
- file: assets/images/badges/bsides-tampa-2026/bsides-tampa-2026-badge-unlucky-13/f972d06ea6.jpg
  source: https://mason-lee-101.github.io/blog/bsides-tampa-2026-badge-ctf/
  credit: Mason Lee (blog writeup)
  caption: Back of the BSides Tampa 2026 badge showing the ATtiny1616 chip and UART pads
- file: assets/images/badges/bsides-tampa-2026/bsides-tampa-2026-badge-unlucky-13/f3a7083ecf.jpg
  source: https://mason-lee-101.github.io/blog/bsides-tampa-2026-badge-ctf/
  credit: Joshua Grose / BSides Tampa
  caption: Front of the 2026 BSides Tampa CTF badge
- file: assets/images/badges/bsides-tampa-2026/bsides-tampa-2026-badge-unlucky-13/c6134d6129.jpg
  source: https://bsidestampa.net/activities/badge-challenge
  credit: BSides Tampa
  caption: 'The Uber Badge award: gold Aztec skull design with embroidered crossbones bag and wax-sealed envelope'
  archived: https://web.archive.org/web/20260612202631/https://bsidestampa.net/activities/badge-challenge
contact: {}
notes:
- ATtiny1616-based electronic badge for BSides Tampa 2026 with a multi-cipher CTF, Morse-blinking LED, and UART firmware-dump challenge. Found by the event-year sweep, task bsides-augusta.
- The sheet titled this "BSides Tampa 2026 Badge (Unlucky 13)"; no source found actually calls the badge "Unlucky 13" by that name, so this may be the write-up author's nickname for it rather than the maker's. Left as-is since no better title surfaced.
- 'The sweep''s title, "BSides Tampa 2026 Badge / Uber Badge Challenge," conflates two things: the conference badge (an ATtiny1616-based hardware/CTF puzzle designed by Joshua Grose, distributed to all attendees) and the "Uber Badge," a separate award given to whoever solves the CTF (free lifetime-style admission, styled as a gold Aztec skull with embroidered crossbones and a wax-sealed envelope).'
status: listed
sources:
- kind: url
  url: https://mason-lee-101.github.io/blog/bsides-tampa-2026-badge-ctf/
  title: BSides Tampa 2026 Badge (Unlucky 13)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-augusta); event read as ''BSides Tampa 2026''.'
- kind: url
  url: https://mason-lee-101.github.io/blog/bsides-tampa-2026-badge-ctf/
  title: BSides Tampa 2026 Badge CTF Write-up | Mason Lee
  accessed: '2026-09-10'
  note: 'Primary source: identifies Joshua Grose as maker, ATtiny1616 MCU, SAO v1.69bis header, UART pads, Morse-blinking LED, Zelda/Hylian-alphabet theming, and CTF mechanics. Also source of the two saved photos.'
- kind: url
  url: https://bsidestampa.net/activities/badge-challenge
  title: Badge Challenge | BSides Tampa 2026
  accessed: '2026-09-10'
  note: Confirms this is the official conference badge challenge; states 2026 registration/sales are closed; no maker, price, or hardware detail given here.
  archived: https://web.archive.org/web/20260612202631/https://bsidestampa.net/activities/badge-challenge
- kind: url
  url: https://www.linkedin.com/posts/joshuagrose_bsidestampa-bsides-infosec-activity-7326444199673765890-n-yk
  title: Joshua Grose LinkedIn post on badge production
  accessed: '2026-09-10'
  note: Joshua Grose posts that "this years BSides Tampa badges have made it - all 22 boxes!" and credits "c0ldbru and I" for the work; used for maker/build-team attribution, not read as a firm quantity figure.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Confirmed as a real badge via the maker's own confirmation on the write-up page and a corroborating LinkedIn post; this appears to be the same physical object as the existing entry bsides-tampa-2026-bsides-tampa-2026-badge-uber-badge-challenge (same event, same CTF, same links), likely created from a different sweep pass. No maker page, storefront, price, exact LED count/type, or open-source files were found, so those fields are left empty. "22 boxes" in the LinkedIn post is ambiguous (boxes of parts vs. finished units) and was not used as a quantity figure. Merged with duplicate entry 'BSides Tampa 2026 Badge Challenge / Uber Badge' (bsides-tampa-2026-bsides-tampa-2026-badge-uber-badge-challenge).
last_modified_date: '2026-09-10'
redirect_from:
- /badges/bsides-tampa-2026/bsides-tampa-2026-badge-uber-badge-challenge/
---

The 2026 BSides Tampa conference badge is an ATtiny1616-based board built by Joshua Grose (with help from a collaborator going by c0ldbru) around a layered capture-the-flag puzzle rather than as a standalone electronics showpiece. Bridging two GPIO pins makes an LED on the badge blink out a Morse-coded clue, and UART pads on the back allow a firmware dump that forms one step of the challenge chain. The badge carries a full SAO v1.69bis connector.

The CTF itself spans more than the PCB: solvers work through Base64 and pigpen-cipher clues, a set of Hylian (Legend of Zelda: Wind Waker) alphabet characters printed on the badge and lanyard, and a companion website, eventually earning an "Uber Badge" for the winner and free 2027 admission for the runner-up. A detailed public write-up and video walkthrough by attendee Mason Lee document the full solve path and include the only known photos of the badge's front and back.

This entry and bsides-tampa-2026-bsides-tampa-2026-badge-uber-badge-challenge both describe what appears to be the same physical badge and challenge, discovered independently by different sweep passes; no separate distinguishing details were found to justify keeping them apart.

## Notes merged from the duplicate entry "BSides Tampa 2026 Badge Challenge / Uber Badge"

The BSides Tampa 2026 conference badge is built around an ATtiny1616 microcontroller with an exposed UART header and a coin-cell battery, and it works as a self-contained puzzle: front and back carry messages encoded in Base64, ROT13, ROT47, and a Zelda-derived "Ancient Hylian" cipher, the lanyard hides a further Base64 clue, and bridging two GPIO pins makes an onboard LED blink out Morse code. Decoding the physical clues points solvers to an online CTF site, `unlucky13.notmalware.fyi`, with thirteen further challenges spanning cryptography, steganography, and reverse engineering. The badge and CTF were designed by Joshua Grose, who also verifies solves in person at the con.

Winning the full challenge does not just earn bragging rights — it wins the "Uber Badge," a separate keepsake award styled as a gold Aztec skull with an embroidered crossbones pouch and a wax-sealed envelope, which BSides Tampa says carries free admission to the following year's conference; a team's runner-up members and second-place solvers get a straight free-admission prize instead. This is an annual BSides Tampa tradition, with past years' badge challenges (2023-2025) featured on the same page as photos of earlier badges and previous Uber Badge winners.
