---
title: '"BIC PICK" Badge - 2025'
id: dc33-pcb-blinky-badges
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: Blacks in Cyber (BiC)
  url: https://www.blacksincyberconf.com/badge
summary: A wearable, Afro-pick-shaped PCB badge made by Blacks In Cybersecurity (BiC) for DEF CON 33, custom designed and built by Eli McRae. It lights up and can power up to six other add-ons.
functions: Lights up and is built to power up to six other SAO-style add-ons; can itself connect to a previous-year DEF CON badge or be powered independently over USB-C.
look:
  colors:
  - black
  - red
  shape: afro pick
  themes:
  - village badge
  form_factor: pcb badge
tech:
  mcu: null
  leds:
    count: null
    type: null
    note: 'The product description says the badge "lights up" but does not state an LED count or part number.'
  display: null
  connectivity:
  - usb
  battery: 'USB-C, or powered by a connected DEF CON badge from the previous year'
  sao_version: null
  sao_ports: 6
get_one:
  price: $35
  price_usd: 35
  quantity: ''
  availability: sold_out
  availability_note: 'Checked 2026-09-07: listed at $35 on Blacks In Cyber''s Square store, marked "Out of stock."'
  distribution:
  - purchase
  - village
  where: Sold through Blacks In Cyber's own Square Online store (blacksincyber.square.site), tied to the B.I.C. Village at DEF CON 33.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: blacksincyber.square.site/shop/badges/3
  url: https://blacksincyber.square.site/shop/badges/3
  kind: store
- label: '"BIC PICK" Badge - 2025 (product page)'
  url: https://blacksincyber.square.site/product/-bic-pick-badge-2025/SSS2MZXAPY4VDMA6FDHEOA7I
  kind: store
- label: BADGE | BlacksInCyber
  url: https://www.blacksincyberconf.com/badge
  kind: website
- label: DEF CON 33 - BiC Village - B I C Pick DEF CON 33 Badge Walkthrough - Eli McRae
  url: https://www.youtube.com/watch?v=BczXjBh6bsM
  kind: video
images:
- file: assets/images/badges/dc33/pcb-blinky-badges/25b62bb733.jpg
  source: https://www.blacksincyberconf.com/badge
  credit: Blacks In Cyber
  caption: BIC Pick badge, an Afro-pick-shaped PCB badge made for the BIC Village's fifth anniversary at DEF CON 33
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: released
sources:
- kind: url
  url: https://blacksincyber.square.site/shop/badges/3
  title: PCB "Blinky" Badges
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc33 (ongoing merch, not year-specific)''.'
- kind: url
  url: https://blacksincyber.square.site/product/-bic-pick-badge-2025/SSS2MZXAPY4VDMA6FDHEOA7I
  title: '"BIC PICK" Badge - 2025 | BLACKS IN CYBER'
  accessed: '2026-09-07'
  note: 'The store''s "Badges" category (reached via the sheet''s /shop/badges/3 link, which now redirects to the category listing) currently shows two items; this one, "BIC PICK" Badge - 2025 ($35, out of stock), matches the DC33 shield logo and Afro-pick pick shape. Full product description read via a JS-rendered browser session: maker''s own words on what it is, who made it (Eli McRae), that it powers up to 6 add-ons, and that it connects via USB-C or a prior-year DEF CON badge. The other item in the category, "BIC Soul Glo Badge," carries a "34" mark and appears to be a different (DC34) item, not this one.'
- kind: url
  url: https://www.blacksincyberconf.com/badge
  title: BADGE | BlacksInCyber
  accessed: '2026-09-07'
  note: 'Maker''s own page confirms the "BIC Pick" is an Afro-pick-shaped badge made for the B.I.C. Village''s five-year anniversary at DEF CON 33, sold/traded on-site; supplied the product image used here.'
- kind: url
  url: https://www.youtube.com/watch?v=BczXjBh6bsM
  title: DEF CON 33 - BiC Village - B I C Pick DEF CON 33 Badge Walkthrough - Eli McRae
  accessed: '2026-09-07'
  note: Confirmed via search as a walkthrough of this badge by its developer, Eli McRae; video content itself was not transcribed for this pass.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This entry (from the community sheet''s generic "PCB ''Blinky'' Badges" storefront link) is the same physical item as the already-researched dc33-blacks-in-cyber-village-badge entry, which itself already merged two other duplicates (dc33-bic-pick and dc33-bic-pick-sao): the "BIC Pick," an Afro-pick-shaped badge by Blacks in Cyber (BiC) for DEF CON 33, designed by Eli McRae. duplicate_of: dc33-blacks-in-cyber-village-badge. This pass adds detail the others lacked: the maker''s own storefront description (functions, that it powers up to 6 add-ons, USB-C/host-badge power) and a confirmed current price ($35, out of stock) and maker name (Eli McRae). Note a price discrepancy: the community sheet used by the sibling entry recorded $45; the maker''s live Square listing checked here shows $35. No MCU, exact LED count/part, or SAO header version is published anywhere found. The Square store page is a JavaScript single-page app; no direct image URL could be extracted from it despite trying DOM/shadow-DOM inspection and network-request capture, so the image saved here comes from the maker''s separate /badge page instead.'
last_modified_date: '2026-09-07'
---

The "BIC PICK" Badge - 2025 is a wearable PCB badge made by Blacks In Cybersecurity (BiC) for the B.I.C. Village's fifth anniversary at DEF CON 33 (2025), custom designed and built by Eli McRae. It is shaped like an Afro pick, which the maker describes as a nod to "the cultural symbol of the Afro pick, an everyday tool that became a statement of pride, identity, and resistance during the Black Power era," carrying that same meaning into hacker culture.

Beyond being a wearable keepsake, the badge lights up and was built to power up to six other add-ons (SAOs), so it can act as a small hub for other people's badge accessories. It can draw power from a connected DEF CON badge from the previous year, or run independently from a USB-C portable charger. The maker's product page jokingly notes the badge is sometimes called an SAO ("Shitty Add On") itself, since it can also plug into another badge that way.

It was sold through Blacks In Cyber's own Square Online store at $35 and tied to the B.I.C. Village; as of this check it is listed as out of stock, with the maker noting boards were "designed and built specifically for 2025," so once sold out they are gone "unless there is major demand." This item is the same physical badge already documented in more general terms under the archive's `dc33-blacks-in-cyber-village-badge` entry.
