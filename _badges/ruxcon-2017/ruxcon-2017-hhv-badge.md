---
title: RuxBadge 2017
id: ruxcon-2017-ruxcon-2017-hhv-badge
layout: badge
parent: Ruxcon 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: ruxcon-2017
year: 2017
makers:
- name: Forgan Reed (darkglade)
  url: https://darkglade.com
  role: electronic design and firmware
- name: Richard Owen (moheart7)
  url: https://moheart7.deviantart.com
  role: badge artwork
summary: 'The soldering-kit badge for Ruxcon 2017''s Hardware Hacking Village: an ESP8266-based board with five WS2812B RGB LEDs and a UART-delivered CTF flag encrypted to each badge''s MAC address.'
functions: 'Runs NodeMCU (Lua) firmware that drives the WS2812B LEDs and prints boot messages over UART, including an AES-encrypted flag (AES-CBC-128, key derived from the badge''s MAC address) that attendees worked out how to decrypt as a CTF.'
look:
  colors:
  - red
  shape: null
  themes:
  - ctf
  - village badge
  - learn to solder
tech:
  mcu: ESP8266 (ESP-12E module)
  leds:
    count: 5
    type: WS2812B
    note: ''
  display: none
  connectivity:
  - uart
  battery: 2xAAA
  sao_version: null
get_one:
  price: free
  price_usd: null
  quantity: '40 boards (panelized two-up for the cost of 20); at least 30 kits handed out in the first three hours of the village'
  availability: sold_out
  distribution:
  - free_drop
  - village
  where: 'Handed out as a soldering kit at the Ruxcon 2017 Hardware Hacking Village; the maker also offered a small number of spare bare boards by email (gratis within Australia) after the con.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/darkglade/ruxconhhv2017
  eda_tool: null
links:
- label: github.com/darkglade/ruxconhhv2017
  url: https://github.com/darkglade/ruxconhhv2017
  kind: repo
- label: ruxconhhv.darkglade.com/2017/RuxBadge2017.pdf
  url: https://ruxconhhv.darkglade.com/2017/RuxBadge2017.pdf
  kind: doc
- label: darkglade.com/2017/10/28/ruxcon-2017-hhv-badge-flag-part-1-the-easy-way
  url: https://darkglade.com/2017/10/28/ruxcon-2017-hhv-badge-flag-part-1-the-easy-way/
  kind: article
- label: ruxconhhv.darkglade.com/2017 (HHV resource page)
  url: https://ruxconhhv.darkglade.com/2017/
  kind: website
- label: 'darkglade.com: Ruxcon 2017 Hardware Hacking Village Wrap'
  url: https://darkglade.com/2017/10/23/ruxcon-2017-hardware-hacking-village-wrap/
  kind: article
images: []
contact: {}
notes:
- 'Sweep imported the title as "Ruxcon 2017 HHV Badge"; the maker''s own build doc and site call it "RuxBadge 2017" (also to distinguish it from the village''s separate, simpler "Simple Solder" learn-to-solder kit that year). Follow-up electronic badge for Ruxcon''s 2017 Hardware Hacking Village with cleartext firmware/flag source and a matching assembly PDF, plus a two-part flag-retrieval writeup on darkglade.com. Found by the event-year sweep, task con-kiwicon.'
status: released
sources:
- kind: url
  url: https://github.com/darkglade/ruxconhhv2017
  title: Ruxcon 2017 HHV Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-kiwicon); event read as ''Ruxcon 2017''.'
- kind: url
  url: https://ruxconhhv.darkglade.com/2017/RuxBadge2017.pdf
  title: RuxBadge2017 instruction sheet (bill of materials and assembly photos)
  accessed: '2026-09-08'
  note: 'Confirmed BOM (ESP-12E, 5x WS2812B, 6 SMD tactile switches, 2xAAA holder) and showed photos of the assembled board: red PCB, teardrop/leaf-shaped outline, "RUXCON 2017" silkscreen and illustrative artwork on both sides.'
- kind: url
  url: https://darkglade.com/2017/10/28/ruxcon-2017-hhv-badge-flag-part-1-the-easy-way/
  title: 'Ruxcon 2017 HHV Badge Flag – Part 1 – The "Easy" Way'
  accessed: '2026-09-08'
  note: 'Confirmed ESP8266/NodeMCU firmware, UART boot messages, and the AES-CBC-128 MAC-derived CTF flag.'
- kind: url
  url: https://ruxconhhv.darkglade.com/2017/
  title: Ruxcon 2017 Hardware Hacking Village resource page
  accessed: '2026-09-08'
  note: 'Lists firmware source/binaries and the build doc; states gerbers for RuxBadge (unlike the separate Simple Solder kit) were not published because the commissioned artwork could not be redistributed, and that spare bare boards were available by email.'
- kind: url
  url: https://darkglade.com/2017/10/23/ruxcon-2017-hardware-hacking-village-wrap/
  title: Ruxcon 2017 Hardware Hacking Village Wrap
  accessed: '2026-09-08'
  note: 'Source for quantity/distribution: 40 boards produced (panelized two-up), 30+ kits given out in the first three hours, gerbers withheld due to commissioned artwork, spare boards offered gratis in Australia.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Maker''s own build doc, wrap post, and CTF writeup confirm this is a real, distributed badge. Could not find price (it was a free village giveaway kit, so get_one.price is set to "free" rather than left blank), exact LED arrangement/purpose beyond "5x WS2812B", or a standalone (non-PDF-embedded) photo URL of the assembled badge to save under images: -- the only photos found are embedded inside RuxBadge2017.pdf. Hardware/gerbers were explicitly not published (commissioned artwork restriction); only firmware source is open, hence open_source: partial. No SAO header found in the BOM/photos, so tech.sao_version left null rather than guessed.'
last_modified_date: '2026-09-08'
---

The RuxBadge 2017 was the solder-your-own electronic badge handed out at Ruxcon 2017's Hardware Hacking Village, designed by Forgan Reed (darkglade) with artwork by Richard Owen (moheart7). It's a red, teardrop-shaped PCB built around an ESP-12E (ESP8266) module, five WS2812B RGB LEDs, six SMD tactile switches, and a 2xAAA battery holder, with headers for UART and for linking boards together. The village produced 40 boards (panelized two-up to double their budget) and went through 30 of them in the first three hours the village opened, handing the rest out over the rest of the weekend.

The badge's NodeMCU (Lua) firmware prints boot messages over UART and hides a capture-the-flag challenge: a flag string encrypted with AES-CBC-128 using a key derived from each badge's own MAC address, so every badge's flag ciphertext (and the work needed to recover it) was unique to that unit. Darkglade wrote up the process of extracting and decrypting the flag in a multi-part blog series starting with "the easy way."

Because the badge artwork was commissioned specifically for this limited run, the maker did not publish gerbers or hardware design files, though the NodeMCU firmware source and compiled binaries are on GitHub. A handful of spare bare boards were offered for free (postage-paid within Australia) to stragglers after the con.

## Make your own

Only the firmware is open. The build doc (RuxBadge2017.pdf) documents the through-hole/SMD assembly for the ESP-12E module, 1000uF SMD electrolytic capacitor, 5x WS2812B LEDs, 8x 10k 0805 resistors, 6x SMD tactile switches, and battery holder, but the schematic/PCB source (Gerbers) was withheld by request of the artist and never published.
