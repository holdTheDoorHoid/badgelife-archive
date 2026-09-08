---
title: CTF Shitty Add-On
id: other-ctf-shitty-add-on
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2019
makers:
- name: Uri Shaked
  url: https://urish.org/
summary: A tiny ATtiny85-based Shitty Add-On built as a self-contained hardware CTF, where solvers reverse-engineer an undocumented I2C protocol to extract and rewrite a hidden flag.
functions: 'A four-level hardware capture-the-flag challenge run over I2C (device address 0x23): turn on the onboard LED, extract a hidden flag from flash/EEPROM, write a "blinking rootkit," and finally overwrite the flag in firmware. Winners received a free board plus a Wokwi Uno board.'
look:
  colors: []
  shape: circle
  themes:
  - ctf
  - puzzle
  - security
tech:
  mcu: ATtiny85
  leds:
    count: 1
    type: discrete
    note: single red LED on pin PB1
  display: none
  connectivity:
  - i2c
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '~20'
  availability: unknown
  distribution:
  - purchase
  where: Sold on Tindie; assembled by PCBWay.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/urish/ctf-shittyaddon
  firmware_url: https://github.com/urish/ctf-shittyaddon
  eda_tool: null
links:
- label: blog.wokwi.com/capture-the-flag-shitty-add-on
  url: https://blog.wokwi.com/capture-the-flag-shitty-add-on/
  kind: website
- label: urish/ctf-shittyaddon (GitHub)
  url: https://github.com/urish/ctf-shittyaddon
  kind: repo
- label: 'Hackster: Build Your Own Capture the Flag Shitty Add-On'
  url: https://dev.hackster.io/news/build-your-own-capture-the-flag-shitty-add-on-for-your-supercon-badge-84956914eea6
  kind: article
- label: 'bburky: CTF Shitty Add-On Writeup'
  url: https://bburky.com/ctf-shittyaddon-writeup/
  kind: article
images:
- file: assets/images/badges/other/ctf-shitty-add-on/df3b1d489b.jpg
  source: "https://blog.wokwi.com/capture-the-flag-shitty-add-on/"
  credit: "Uri Shaked"
  caption: "The CTF Shitty Add-On PCB"
- file: assets/images/badges/other/ctf-shitty-add-on/4e447dd086.jpg
  source: "https://blog.wokwi.com/capture-the-flag-shitty-add-on/"
  credit: "Uri Shaked"
  caption: "Assembled CTF Shitty Add-On boards"
contact: {}
notes:
- An ATtiny85-based capture-the-flag Shitty Add-On with I2C reverse-engineering puzzles, sold on Tindie. Found by the event-year sweep, task supercon-2019, but the maker's own account does not tie it to Hackaday Supercon 2019 (see research.notes); event corrected to 'other'.
status: released
sources:
- kind: url
  url: https://blog.wokwi.com/capture-the-flag-shitty-add-on/
  title: CTF Shitty Add-On
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2019); event originally read as ''supercon-2019'', later corrected to ''other'' (see research.notes).'
- kind: url
  url: https://blog.wokwi.com/capture-the-flag-shitty-add-on/
  title: 'CTF Shitty Add-On - An ATtiny85 Hardware Challenge For The Brave!'
  accessed: '2026-09-08'
  note: 'Maker''s own blog post (published 30 Oct 2019); confirmed MCU, LED, I2C protocol/address 0x23, four-level CTF structure, SCL/SDA swap on an early batch, ~20 units assembled by PCBWay, a few sold on Tindie, open-source firmware/hardware on GitHub. States the boards were originally meant to accompany a separate ''smart conference badge'' and were only assembled/tested after that (unnamed in this post) conference; does not name Supercon anywhere.'
- kind: url
  url: https://dev.hackster.io/news/build-your-own-capture-the-flag-shitty-add-on-for-your-supercon-badge-84956914eea6
  title: Build Your Own Capture the Flag Shitty Add-On for Your Supercon Badge
  accessed: '2026-09-08'
  note: 'Page returns HTTP 403 to automated fetch; only a search-index snippet was read (both originally and on recheck). Its own headline is the only source calling this a "Supercon badge" add-on; not corroborated by the maker''s blog or repo.'
- kind: url
  url: https://github.com/urish/ctf-shittyaddon
  title: urish/ctf-shittyaddon
  accessed: '2026-09-08'
  note: Confirms MIT-licensed open-source firmware/hardware repo, ATtiny85 + ShittyAddon V1 connector + reset button + red LED on PB1, I2C slave at 0x23.
- kind: url
  url: https://bburky.com/ctf-shittyaddon-writeup/
  title: CTF Shitty Add-On Writeup (bburky)
  accessed: '2026-09-08'
  note: Independent solver's writeup exists and links back to the maker's blog post; does not mention Supercon or any specific conference.
- kind: url
  url: https://hackaday.com/2019/05/18/heres-how-hard-it-is-to-produce-a-conference-badge/
  title: "Here's How Hard It Is To Produce A Conference Badge"
  accessed: '2026-09-08'
  note: 'Identifies the "smart conference badge" referenced in the CTF blog post as a separate nRF52840 badge Shaked''s team built for Aramcon 2019, a private Israeli tech event (published 18 May 2019) — unrelated to Hackaday Supercon.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Fact-check pass (2026-09-08): re-read the maker''s blog post directly (previously only a search snippet had been used for the Hackster nuance). The blog post never names Supercon anywhere. It says the CTF boards were originally meant to ship alongside a separate "smart conference badge," and were only assembled/tested "after the conference" due to a tight schedule. Tracing that badge (Hackaday, 18 May 2019, "Here''s How Hard It Is To Produce A Conference Badge") shows it was built for Aramcon 2019, a private Israeli tech event with no connection to Hackaday Supercon. The Hackster.io article''s headline ("...for Your Supercon Badge") appears to be the only thing tying this item to Supercon at all, and is not corroborated by the maker''s own blog, the GitHub repo, or the independent (bburky) writeup, none of which mention Supercon. Since the item was not made for Supercon 2019 and there is no evidence it was distributed there, event has been corrected from ''supercon-2019'' to ''other''; this leaves the entry''s folder (_badges/supercon-2019/) mismatched with its event field, which is expected and left to the archive''s general reconciliation process rather than moved as part of this fact-check. Removed the unsupported ''learn to solder'' theme tag: the boards are assembled by PCBWay and sold assembled, and no source describes a self-solder kit. All other non-empty fields were checked against the maker''s blog post and GitHub repo and are supported: ATtiny85, single red LED on PB1, I2C address 0x23, four-level CTF (LED on / extract flag / remote code exec (blinking) / overwrite flag), ~20 units via PCBWay, sold on Tindie, MIT-licensed open hardware+firmware, SCL/SDA swap on an early batch (used in body only, not a discrete field). Both images (PCB photo, assembled-boards photo) are sourced from the same blog post, which does show a bare PCB and multiple assembled boards, consistent with their captions. Still unresolved: get_one.price/price_usd/availability (Tindie listing itself was not reachable, blocked from automated fetch), tech.battery, tech.sao_version (the GitHub README does say "ShittyAddon V1 connector," which would support sao_version: v1, but filling that in is new research beyond this fact-check''s scope and is flagged here rather than added), look.colors, series, and contact. dev.hackster.io continues to return HTTP 403 to automated fetch, so that source is still only confirmed via a search-index snippet.'
last_modified_date: '2026-09-08'
redirect_from:
- /badges/supercon-2019/ctf-shitty-add-on/
---

The CTF Shitty Add-On is a hardware capture-the-flag puzzle built by Uri Shaked (creator of Wokwi) around a single ATtiny85 microcontroller. The tiny round board plugs into a badge's Shitty Add-On (SAO) header and exposes an undocumented I2C interface at address 0x23; solving the challenge means reverse-engineering that interface to control the board's one red LED, extract a flag hidden in the chip's memory, and ultimately rewrite the firmware to plant a new flag of your own. Roughly 20 boards were assembled through PCBWay and sold on Tindie, with winners of the challenge receiving a free board along with a Wokwi Uno board.

Shaked's blog post announcing the project (published on blog.wokwi.com on October 30, 2019) says the CTF boards were originally meant to ship alongside a separate "smart conference badge" his team built, but assembly and testing only began after that conference due to a tight schedule; that badge turns out to have been built for Aramcon 2019, a private Israeli tech event unrelated to Hackaday Supercon. Nothing in the maker's blog, the GitHub repo, or an independent solver's writeup ties the CTF Shitty Add-On to Hackaday Supercon 2019 — the only source connecting it to Supercon at all is a Hackster.io article headlined "for your Supercon badge," which appears to be marketing shorthand for "any SAO-header badge" rather than a claim about where this board was made or sold. Both hardware design files and the ATtiny85 firmware (including the flag-checking logic) are open source on GitHub at urish/ctf-shittyaddon under the MIT license, and at least one independent solver (Blake Burkhart) published a full writeup of solving the puzzle.

A known quirk documented by the maker: an early batch of boards had the I2C SCL and SDA pins swapped, requiring manual rewiring before use.
