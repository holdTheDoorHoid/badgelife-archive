---
title: RSA Sandbox Badge
id: other-rsa-sandbox-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 0
makers:
- name: Hackerware.io
  url: https://www.hackerwares.in/
summary: A full-color electronic CTF badge made for the RSA Conference USA Sandbox program, representing the Sandbox community's eight villages.
functions: 'A serial-based CTF: connect via a CP2102 USB-to-TTL adapter, open a serial monitor at 9600 baud, send "***" to start, and solve two puzzle levels for lowercase flags (hints published online). Sending "+++" resets the badge. A separate "Glow All LEDs" hex file is offered for flashing the badge to a static full-color LED display mode.'
look:
  colors: []
  shape: null
  themes:
  - security
  - ctf
  - village badge
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - uart
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://www.hackerwares.in/StrongerTogether_SE2.hex.zip
  eda_tool: null
links:
- label: www.hackerwares.in/rsa
  url: https://www.hackerwares.in/rsa
  kind: website
- label: 'Hackster.io: The RSA Sandbox Badge'
  url: https://www.hackster.io/HacksFromPanda/the-rsa-sandbox-badge-e23c62
  kind: article
- label: Glow All LEDs hex file
  url: https://www.hackerwares.in/StrongerTogether_SE2.hex.zip
  kind: doc
images:
- file: assets/images/badges/other/rsa-sandbox-badge/8c6d1eec10.jpg
  source: https://www.hackerwares.in/rsa
  credit: Hackerwares
  caption: The RSA Sandbox Badge
contact: {}
notes:
- First RSA Conference badge, represents eight villages
- Maker describes it as "our most innovative full colour badge design to represent the vibrant community and 8 villages at the RSA Sandbox" (linking to rsaconference.com/usa/programs/sandbox).
status: listed
sources:
- kind: url
  url: https://www.hackerwares.in/rsa
  title: RSA Sandbox Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''RSA Conference''.'
- kind: url
  url: https://www.hackerwares.in/rsa
  title: The RSA Sandbox Badge
  accessed: '2026-09-07'
  note: Primary maker page; confirms CTF gameplay instructions, firmware hex file link, and the "8 villages" framing.
- kind: url
  url: https://www.hackerwares.in/
  title: Hackerwares
  accessed: '2026-09-07'
  note: Maker's portfolio page confirms this is billed as "First-ever RSA Conference Badge" for the Sandbox community; no chip/LED specs or pricing listed.
  archived: https://web.archive.org/web/20260611200959/https://www.hackerwares.in/
- kind: url
  url: https://www.hackster.io/HacksFromPanda/the-rsa-sandbox-badge-e23c62
  title: The RSA Sandbox Badge - Hackster.io
  accessed: '2026-09-07'
  note: Linked from the maker's page as the "Badge Story" write-up; blocked by Cloudflare bot protection on fetch, could not be read. Kept as a link for future research.
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Re-verified 2026-09-07 against the live maker pages. No matching RSA Conference event id exists in _data/events.yml, so event is left as "other"; the con is RSA Conference USA, Sandbox program. No source states the year directly (the maker page''s copyright footer reads 2023, but that is a site-wide copyright, not a stated badge year, so year is left empty rather than guessed). Could not confirm MCU, LED count/type, display, battery, price, quantity made, or open-source hardware files (only a firmware hex file is published). get_one.where was blanked: no source states how the badge was actually distributed to attendees (only that it was made for the Sandbox program), so the prior "distributed to attendees" text was an unsupported inference and has been removed. The body previously named the maker "Abhinav SP / Abhinav Panda"; the site only confirms the first name "Abhinav" (via its contact email) and the "Panda" handle (HacksFromPanda / TweetsFromPanda) as branding, not a surname
    "SP" — the body has been corrected to drop that unsupported surname. The Hackster.io "Badge Story" article and the maker''s Hackster.io profile are linked from the site but return HTTP 403 on every fetch attempt and could not be read for further detail; kept as links only.'
last_modified_date: '2026-09-07'
---

The RSA Sandbox Badge is a full-color electronic CTF badge made by Hackerware.io, run by a maker named Abhinav who goes by "HacksFromPanda" online, for the RSA Conference USA Sandbox program. The maker bills it as the first badge made for RSA Conference, designed to represent the Sandbox community and its eight villages.

The badge runs a serial-based capture-the-flag: attendees connect a CP2102 USB-to-TTL adapter (Tx/Rx crossed, GND and +5V matched), open a serial monitor at 9600 baud with both NL and CR enabled, and send `***` to begin. Two puzzle levels are hinted at via pages linked from the maker's site, with all flags submitted in lowercase and no brackets; sending `+++` resets the badge. The maker also published a standalone "Glow All LEDs" firmware hex file that puts the badge into a static full-color lighting display mode instead of the CTF.

No microcontroller, LED count/type, display, price, or production quantity is stated on the maker's page or portfolio site. A "Badge Story" write-up on Hackster.io is linked as further reading but could not be retrieved for this entry (blocked by Cloudflare). Hardware design files were not found; only the firmware hex file is published, so the badge is best described as partially open.
