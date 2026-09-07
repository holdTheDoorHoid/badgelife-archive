---
title: Shitty Calvin
id: dc26-dc26-shitty-calvin-sao
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: awkward intelligence
  url: https://hackaday.io/Awkwardai
summary: Calvin (of Calvin and Hobbes peeing-sticker fame) SAO with a four-stage LED sequencer driven by a 4017B decade counter and a 555 timer, given away with "Shitty Add-On" sets at DEF CON 26; final gerbers posted as shittycalvin.zip.
functions: Four-stage LED sequencer, blinky only (no interactivity beyond power-on).
look:
  colors: []
  shape: null
  themes:
  - meme
  - pop culture
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Bundled with awkward intelligence's other "Shitty Add-On" SAOs at DEF CON 26 (2018); the maker stated it would not be sold individually.
make_your_own:
  open_source: partial
  hardware_url: https://cdn.hackaday.io/files/1599526843386368/shittycalvin.zip
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  url: https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  kind: hackaday
  archived: https://web.archive.org/web/20260505144653/https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
- label: hackaday.io/project/159952/files
  url: https://hackaday.io/project/159952/files
  kind: hackaday
  archived: https://web.archive.org/web/20260907115748/https://hackaday.io/project/159952/files
- label: shittycalvin.zip (design files)
  url: https://cdn.hackaday.io/files/1599526843386368/shittycalvin.zip
  kind: fab
  archived: https://web.archive.org/web/20260907120350/https://cdn.hackaday.io/files/1599526843386368/shittycalvin.zip
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  title: The Harbinger Shitty Add-on Badges
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260505144653/https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
- kind: url
  url: https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  title: The Harbinger Shitty Add-on Badges
  accessed: '2026-09-07'
  note: 'Project description text confirms: "Shitty Calvin is a four-stage LED sequencer driven by a 4017b and 555 timer," maker is awkward intelligence, and the maker states "I won''t be selling these individually, only with my Shitty Add-On sets."'
  archived: https://web.archive.org/web/20260505144653/https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
- kind: url
  url: https://hackaday.io/project/159952/files
  title: The Harbinger Shitty Add-on Badges - Files
  accessed: '2026-09-07'
  note: Lists shittycalvin.zip, "Final version of Shitty Calvin," uploaded 2019-03-04, 319.37 kB.
  archived: https://web.archive.org/web/20260907115748/https://hackaday.io/project/159952/files
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The Hackaday.io project page ("The Harbinger Shitty Add-on Badges," part of a larger multi-SAO project by awkward intelligence for DEF CON 26) confirms the summary and design-file link. Could not confirm PCB color, LED count/type, exact quantity made, or find a photo confidently identified as this specific SAO (the project's gallery images are not individually captioned, so none were saved to avoid misattributing another SAO in the same series). No independent press coverage found.
last_modified_date: '2026-09-07'
---

Shitty Calvin is a shitty add-on (SAO) made by awkward intelligence as part of "The Harbinger," a larger collection of add-ons and hardware built for DEF CON 26 in 2018. It riffs on the Calvin and Hobbes comic strip's famous "peeing Calvin" bumper-sticker image, driving a simple four-stage LED sequencer with a 4017B decade counter and a 555 timer astable oscillator — a fully analog, MCU-free blinky circuit typical of the "shitty add-on" genre that prizes irreverence and minimal parts count over sophistication.

The maker did not sell Shitty Calvin as a standalone item; it was distributed as a freebie bundled with awkward intelligence's other Shitty Add-On SAOs at DEF CON 26. Final design files were posted to the Hackaday.io project as shittycalvin.zip in March 2019.

## Make your own

The final gerbers/design archive is posted at the Hackaday.io project's files page as `shittycalvin.zip`. No separate firmware is applicable since the board is a discrete-logic (4017B + 555) circuit with no microcontroller.
