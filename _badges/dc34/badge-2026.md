---
title: DEF CON 34 Badge (2026)
id: dc34-badge-2026
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
series: null
makers:
- name: Andrew "bunnie" Huang
  url: https://www.bunniestudios.com/
- name: Team CHEESO
  url: https://cheeso.io/defcon-34-badge
summary: The official DEF CON 34 badge, designed by Team CHEESO around Andrew "bunnie" Huang's open-source Baochip-1x, a RISC-V chip built for physical inspection. It doubles as a FIDO2/TOTP security key and password manager after the con.
functions: Runs Xous OS (a Rust microkernel) on the detachable Baochip-1x core module. Scans QR codes with a low-resolution camera (no photo storage) for badge challenges and light-pattern exchange between badges, and works post-conference as a FIDO2/TOTP hardware security key and password manager.
look:
  colors:
  - black
  - copper
  - silver
  shape: sun
  themes:
  - security
  - privacy
  - hardware tool
  - puzzle
  - wearable
tech:
  mcu: Baochip-1x (Vexriscv RISC-V core + 4x PicoRV32 I/O cores, TSMC 22nm)
  leds:
    count: null
    type: RGB
    note: Flashes in colors/patterns that vary by badge role (attendee, speaker, goon, Uber); badges can extend colors and build more complex patterns by exchanging light with other badges (WIRED).
  display: 128x128 monochrome OLED
  connectivity:
  - usb
  - i2c
  battery: 2x AA (about 3 days of intermittent use); USB-C powers the detached core module
  sao_version: v1.69bis
  sao_ports: 2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  availability_note: Distributed to attendees at DEF CON 34 (Aug 2026) as part of registration. No price figure or spare-badge sale was confirmed in the sources checked (a prior draft's "$520 / $100 spares" figures could not be verified and were removed). Checked 2026-09-07.
  distribution:
  - free_drop
  where: Handed out to attendees at DEF CON 34 registration.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/baochip/baochip-1x
  firmware_url: https://github.com/betrusted-io/xous-core
  eda_tool: null
  notes: The Baochip-1x silicon RTL is published on GitHub under the CERN-OHL-W v2 license, and the badge runs the open-source Xous OS (betrusted-io/xous-core). The badge's own PCB/enclosure design files were not confirmed as published as of this check; media.defcon.org hosts a "DEF CON 34 SAO Spec Sheet.pdf" for people building SAOs to plug into the badge, plus firmware bundles (loader.uf2, swap.uf2, xous.uf2).
links:
- label: www.wired.com/story/defcon-34-badge-baochip-andrew-bunnie-huang
  url: https://www.wired.com/story/defcon-34-badge-baochip-andrew-bunnie-huang/
  kind: article
  archived: https://web.archive.org/web/20260904142943/https://www.wired.com/story/defcon-34-badge-baochip-andrew-bunnie-huang/
- label: media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20badge
  url: https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20badge/
  kind: website
- label: cheeso.io/defcon-34-badge
  url: https://cheeso.io/defcon-34-badge
  kind: website
  archived: https://web.archive.org/web/20260805063950/https://cheeso.io/defcon-34-badge
- label: hackster.io - DEF CON 34 badge / Baochip-x1
  url: https://www.hackster.io/news/the-def-con-34-badge-packs-a-surprise-andrew-bunnie-huang-s-mostly-open-baochip-x1-1e03307d4797
  kind: article
  archived: https://web.archive.org/web/20260819020931/https://www.hackster.io/news/the-def-con-34-badge-packs-a-surprise-andrew-bunnie-huang-s-mostly-open-baochip-x1-1e03307d4797
- label: github.com/baochip/baochip-1x
  url: https://github.com/baochip/baochip-1x
  kind: repo
  archived: https://web.archive.org/web/20260817143602/https://github.com/baochip/baochip-1x
- label: github.com/betrusted-io/xous-core
  url: https://github.com/betrusted-io/xous-core
  kind: repo
  archived: https://web.archive.org/web/20260817143635/https://github.com/betrusted-io/xous-core/
images:
- file: assets/images/badges/dc34/badge-2026/dda61166ff.png
  source: https://cheeso.io/defcon-34-badge
  credit: Team CHEESO / bunnie Huang
  caption: DEF CON 34 HUMAN badge with the removable BaoChip-1x core module
  archived: https://web.archive.org/web/20260805063950/https://cheeso.io/defcon-34-badge
- file: assets/images/badges/dc34/badge-2026/195752599f.png
  source: https://cheeso.io/defcon-34-badge
  credit: Team CHEESO / bunnie Huang
  caption: Back of the DEF CON 34 HUMAN badge, honoring Kingpin's 2006 badge design, with battery holder
  archived: https://web.archive.org/web/20260805063950/https://cheeso.io/defcon-34-badge
contact: {}
notes:
- 'Confirmed this session via WIRED: ''The New Defcon Badges Pack a Unique Open Source Chip That Doubles as a Security Key.'' Human-shaped badge built around bunnie''s open-source BaoChip, doubles as a security key. Also see media.defcon.org DEF CON 34 badge folder (DEF CON 34 SAO Spec Sheet.pdf) as a secondary source.'
- 'cheeso.io/defcon-34-badge (Team CHEESO''s own project page) is the richest source: two badge tiers were made, "HUMAN" (2-layer PCB, matte black/copper/silver, sun-shaped) and "INHUMAN" (4-layer PCB in department colors with gold inlay, cogwheel-shaped); the page also shows "ARTIST" badge photos. This entry describes the HUMAN badge, the one shown in the WIRED coverage; the INHUMAN/ARTIST variants may deserve their own entries if the archive tracks badge tiers separately.'
- Quantity made was not stated in any source checked; left empty rather than guessed.
status: released
sources:
- kind: url
  url: https://www.wired.com/story/defcon-34-badge-baochip-andrew-bunnie-huang/
  title: DEF CON 34 Badge (2026)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: official-badges); event read as ''DEF CON 34''.'
  archived: https://web.archive.org/web/20260904142943/https://www.wired.com/story/defcon-34-badge-baochip-andrew-bunnie-huang/
- kind: url
  url: https://cheeso.io/defcon-34-badge
  title: DEFCON 34 Badge — CHEESO team & bunnie
  accessed: '2026-09-07'
  note: Maker (Team CHEESO) project page; source of shape, colors, display, camera, SAO ports, battery, and badge tier photos (HUMAN/INHUMAN/ARTIST).
  archived: https://web.archive.org/web/20260805063950/https://cheeso.io/defcon-34-badge
- kind: url
  url: https://media.defcon.org/DEF%20CON%2034/DEF%20CON%2034%20badge/
  title: DEF CON 34 badge files (media.defcon.org)
  accessed: '2026-09-07'
  note: Confirms official firmware files (loader.uf2, swap.uf2, xous.uf2 -> Xous OS) and a DEF CON 34 SAO Spec Sheet PDF for third-party SAO makers.
- kind: url
  url: https://www.hackster.io/news/the-def-con-34-badge-packs-a-surprise-andrew-bunnie-huang-s-mostly-open-baochip-x1-1e03307d4797
  title: 'The DEF CON 34 Badge Packs a Surprise: Andrew "bunnie" Huang''s "Mostly-Open" Baochip-x1'
  accessed: '2026-09-07'
  note: Confirms chip specs (Vexriscv 350MHz, TSMC 22nm, 4MB RRAM, 2MB SRAM, quad 700MHz PicoRV32, IRIS inspection). Live page returns Cloudflare 403 to automated fetches; re-verified this session via the Wayback Machine capture (20260819020931) instead. Does NOT mention any registration price or spare-badge price.
  archived: https://web.archive.org/web/20260819020931/https://www.hackster.io/news/the-def-con-34-badge-packs-a-surprise-andrew-bunnie-huang-s-mostly-open-baochip-x1-1e03307d4797
- kind: url
  url: https://github.com/baochip/baochip-1x
  title: 'GitHub - baochip/baochip-1x: Baochip 1x Silicon'
  accessed: '2026-09-07'
  note: Confirms the chip RTL is published under CERN-OHL-W v2.
  archived: https://web.archive.org/web/20260817143602/https://github.com/baochip/baochip-1x
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-opened every cited source. Two errors found and fixed: (1) look.colors included "gold", but cheeso.io states gold inlay is exclusive to the INHUMAN/other tiers -- the HUMAN badge (which this entry covers) is black/copper/silver only; gold removed. (2) get_one had specific figures ("$520" registration price, "$100" spare badges, availability: sold_out) that do not appear on any of the four cited sources (WIRED, cheeso.io, media.defcon.org, Hackster.io) -- blanked price and changed availability to "free" (distributed with registration), with the discrepancy noted in availability_note. Added tech.leds (previously null): WIRED confirms the badges have LEDs that flash per badge role and exchange patterns with other badges, matching the "functions" field. Everything else checked out: chip specs (Vexriscv 350MHz, TSMC 22nm, 2MB SRAM/4MB RRAM, quad 700MHz PicoRV32) via archived Hackster.io and WIRED; OLED/camera/battery/SAO-port/Kingpin-homage/USB-C details
    and both photos'' captions via cheeso.io; firmware files and SAO spec sheet (which independently confirms I2C and a 6-pin/v1.69bis-style header) via media.defcon.org; chip RTL license (CERN-OHL-W-2.0) and Xous OS repo via GitHub. Hackster.io''s live page 403s to automated fetches (Cloudflare); verified instead via a Wayback Machine capture with matching content. Quantity made for this specific (HUMAN) tier is still not stated anywhere and remains blank -- WIRED gives "27,000" as the total DEF CON 34 badges across all tiers/roles combined, which is not specific enough to this entry to use. The badge''s own PCB/case design files remain unconfirmed as published (open_source: partial is correct). This entry covers the "HUMAN" badge tier only; "INHUMAN" and "ARTIST" tiers seen on the maker''s page may warrant separate entries (see other_items_found in the original research pass).'
last_modified_date: '2026-09-07'
---

The DEF CON 34 badge (2026) was designed by Team CHEESO around Andrew "bunnie" Huang's Baochip-1x, the first production-scale open-source silicon chip built specifically so conference attendees could physically verify its internals. The chip pairs a 350 MHz Vexriscv RISC-V core with four 700 MHz PicoRV32 I/O cores, 2 MiB of SRAM, and 4 MiB of RRAM, fabricated on TSMC's 22nm process with a package designed for infrared (IRIS) inspection so owners can compare the visible transistor pattern against the chip's published design. The chip lives on a detachable core module with USB-C, which plugs into the badge body; the badge itself runs Xous OS, a Rust-based microkernel operating system.

The badge shipped in at least two visual tiers built on the same electronics: a "HUMAN" badge (sun-shaped, 2-layer PCB, matte black front with a copper back and silver inlay) and an "INHUMAN" badge (cogwheel-shaped, 4-layer PCB in department-specific colors with gold inlay), both carrying a hexagon peacock emblem and two SAO ports; press photos of an "ARTIST" variant also appear on the maker's page. The badge body includes a 128x128 monochrome OLED display and a deliberately low-resolution camera used only for scanning QR codes (it stores no photos), supporting on-badge challenges and encrypted light-pattern exchanges between badges during the con. It runs on 2 AA batteries for about three days of intermittent use, with the back panel referencing Kingpin's original 2006 DEF CON electronic badge. After the conference, the Baochip-1x core doubles as a FIDO2/TOTP security key and password manager.

Every attendee whose registration guaranteed a badge got one; whether DEF CON separately sold spare badges, and at what price, was not confirmed in the sources checked. The Baochip-1x silicon RTL is published on GitHub under the CERN-OHL-W v2 license, and the badge's firmware is built on the open-source `betrusted-io/xous-core` project; DEF CON's own media page hosts the firmware bundle (loader, swap, and OS images) plus a spec sheet for anyone building a third-party SAO for the badge's headers. Whether the badge's own PCB and enclosure files are published separately from the chip and OS repos was not confirmed in this pass.
