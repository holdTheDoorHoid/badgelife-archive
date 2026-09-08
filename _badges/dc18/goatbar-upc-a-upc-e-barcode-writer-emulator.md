---
title: GoatBar UPC-A/UPC-E Barcode Writer/Emulator
id: dc18-goatbar-upc-a-upc-e-barcode-writer-emulator
layout: badge
parent: DC18
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: dc18
year: 2010
makers:
- name: Brad Threatt
summary: 'A 1st-place DEF CON 18 Badge Hacking Contest entry: a firmware modification for the official DC18 badge that lets the wearer write a UPC-A/UPC-E barcode of a cheaper item and display it on the badge''s LCD to fool retail self-checkout scanners.'
functions: 'Uses the DC18 badge''s two buttons and a menu GUI to enter/select a UPC-A or UPC-E barcode, generates the corresponding barcode pattern, and displays it on the badge''s LCD so a self-checkout laser scanner reads it as if it were printed on an item.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: Freescale MC56F8006
  leds: null
  display: 128x32 reflective LCD (Kent Displays, host DC18 badge)
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution:
  - contest
  where: 'Not sold; a firmware hack for the official DEF CON 18 attendee badge, shared as source code/binary via a personal link (ehq.com/GoatBar.zip) rather than distributed as a product.'
make_your_own:
  open_source: 'yes'
  hardware_url: null
  firmware_url: https://ehq.com/GoatBar.zip
  eda_tool: null
links:
- label: ehq.com/GoatBar.zip
  url: https://ehq.com/GoatBar.zip
  kind: repo
- label: 'DEF CON 18 Contest Results'
  url: https://defcon.org/html/defcon-18/dc-18-contest-results.html
  kind: article
- label: 'Nuts and Volts: DEFCON Badge Hacking Contest writeup'
  url: https://www.nutsvolts.com/uploads/magazine_downloads/Badge_Hacking_Contest.pdf
  kind: article
- label: 'DEF CON forum: DC18 Badge Hacking Contest Results'
  url: https://forum.defcon.org/node/12829
  kind: doc
- label: 'DEF CON 18 badge hack video (media.defcon.org)'
  url: https://media.defcon.org/DEF%20CON%2018/DEF%20CON%2018%20hackaday%20bage%20hacks/DC18%20Badge%20Hack%20GoatBar%20UPC%20Barcode%20Writer%20Emulator.mp4
  kind: video
- label: 'Grand Idea Studio: DEFCON 18 Badge (badge hardware background)'
  url: https://grandideastudio.com/portfolio/other/defcon-18-badge/
  kind: article
images: []
contact: {}
notes:
- 'Winning entry in the DEF CON 18 Badge Hacking Contest: a UPC barcode writer/emulator add-on built around the official DC18 badge, designed to interact with retail self-checkout scanners. Found by the event-year sweep, task dc18-all.'
- 'The sweep''s only source (ehq.com/GoatBar.zip) is a raw firmware/CodeWarrior project archive for a Freescale 56F8006 bootloader, with no README or author info inside; confirmed as the real GoatBar project via DEF CON''s own contest results page, a Nuts & Volts writeup, the DEF CON forums thread, and a media.defcon.org video/transcript of the entry being demoed.'
status: released
sources:
- kind: url
  url: https://ehq.com/GoatBar.zip
  title: GoatBar UPC-A/UPC-E Barcode Writer/Emulator
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc18-all); event read as ''dc18''.'
- kind: url
  url: https://defcon.org/html/defcon-18/dc-18-contest-results.html
  title: 'DEF CON 18 Hacking Conference - Contest Results'
  accessed: '2026-09-08'
  note: 'Confirms 1st place in the DC18 Badge Hacking Contest, maker, and the self-checkout barcode-substitution description.'
- kind: url
  url: https://www.nutsvolts.com/uploads/magazine_downloads/Badge_Hacking_Contest.pdf
  title: 'PDF DEFCON Badge Hacking Contest - Nuts and Volts Magazine'
  accessed: '2026-09-08'
  note: '1st place writeup naming Brad Threatt and describing the two-button GUI barcode entry method.'
- kind: url
  url: https://forum.defcon.org/node/12829
  title: '[Defcon 18] DC18 Badge Hacking Contest Results'
  accessed: '2026-09-08'
  note: 'Community forum record of the contest results with the same description.'
- kind: url
  url: https://grandideastudio.com/portfolio/other/defcon-18-badge/
  title: 'DEFCON 18 Badge - Grand Idea Studio'
  accessed: '2026-09-08'
  note: 'Background on the host DC18 badge hardware: Freescale MC56F8006 MCU, 128x32 reflective LCD, CR2032 battery, 7,780 units made; names GoatBar as the contest winner.'
- kind: url
  url: https://media.defcon.org/DEF%20CON%2018/DEF%20CON%2018%20hackaday%20bage%20hacks/DC18%20Badge%20Hack%20GoatBar%20UPC%20Barcode%20Writer%20Emulator.eng.srt
  title: 'DC18 Badge Hack GoatBar transcript'
  accessed: '2026-09-08'
  note: 'Video transcript of the maker demoing the barcode writer on camera, confirming it is a real, working entry.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed as the real 1st-place DC18 Badge Hacking Contest entry via multiple independent sources (DEF CON, Nuts & Volts, DEF CON forums, media.defcon.org). It is a firmware modification of the official DEF CON 18 badge (Freescale MC56F8006, 128x32 LCD), not a standalone PCB/kit, so hardware fields (leds, connectivity, battery, form factor) reflect the host badge or are left empty since GoatBar itself adds no new hardware. No photo of the badge running GoatBar was found (the only visual record located is a video, not a still image), so images could not be saved. Quantity made, price, and exact contest date/placement year beyond "2010/DC18" are not stated anywhere found.'
last_modified_date: '2026-09-08'
---

Brad Threatt's GoatBar took 1st place in the DEF CON 18 (2010) Badge Hacking Contest, a competition open to any modification of that year's official attendee badge. The DC18 badge itself was built around a Freescale MC56F8006 16-bit digital signal controller with a 128x32 reflective LCD and ran off a CR2032 cell; GoatBar is a firmware hack for that badge rather than a separate board.

The hack lets the wearer use the badge's existing two buttons and a simple on-screen GUI to enter or select a UPC-A or UPC-E barcode for a cheaper item, then displays that barcode on the badge's LCD. Held up to a self-checkout lane's laser scanner, the badge is read as though it were the printed barcode on genuine retail packaging — letting someone ring up a lower-priced item in place of what they actually intend to buy. DEF CON's own contest results page and a contemporary Nuts & Volts writeup both credit the idea to Brad Threatt and describe the same two-button entry method; a media.defcon.org video captures the entry being demonstrated live.

The only link carried by the discovery sweep, ehq.com/GoatBar.zip, turned out to be a raw CodeWarrior/Freescale 56F8006 firmware project archive with no README, but its target chip matches the DC18 badge's MCU and its filename matches the contest entry, so it is almost certainly the GoatBar source itself.

