---
title: Limited Edition BBV Blinky Badge – Green
id: dc33-bug-bounty-village-dc33-badge
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: Bug Bounty Village
  url: https://shop.bugbountydefcon.com/
- name: Abhinav Panda
  role: hardware designer
summary: A green, Matrix-inspired electronic badge for DEF CON 33's Bug Bounty Village, with a cascading LED "code rain" effect and onboard CTF challenges unlocked by entering flags on tactile buttons.
functions: The badge has blinky LEDs raining down to simulate a Matrix "code rain" effect, plus four tactile buttons to enter binary flags. Flags are tied to different CTF challenges; solving one and entering its code unlocks more LEDs. A secret code reportedly reverses the matrix effect and sends the lights into an "anti-gravity" mode.
look:
  colors:
  - green
  - black
  shape: rectangle
  themes:
  - cyberpunk
  - security
  - ctf
  - village badge
tech:
  mcu: ATmega16A
  leds:
    count: 41
    type: SMD
    note: Arranged as a matrix background for the "code rain" effect.
  display: none
  connectivity: []
  battery: 3xAAA (included)
  sao_version: null
get_one:
  price: $99.99
  price_usd: 99.99
  quantity: limited
  availability: sold_out
  availability_note: 'Storefront listing showed "Sold out" and available: false when checked 2026-09-06.'
  distribution:
  - purchase
  - village
  where: Pre-ordered online at shop.bugbountydefcon.com; pickup only at the Bug Bounty Village at DEF CON 33 with order confirmation and a DEF CON badge shown. No shipping, no on-site sales.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: shop.bugbountydefcon.com
  url: https://shop.bugbountydefcon.com/
  kind: store
- label: Limited Edition BBV Blinky Badge – Green (product page)
  url: https://shop.bugbountydefcon.com/products/limited-edition-bbv-blinky-badge-green-pickup-only-def-con
  kind: store
- label: DEF CON Forums - Limited Edition Bug Bounty Village Badge
  url: https://forum.defcon.org/node/253153
  kind: article
- label: Hackster.io - Bug Bounty Village 2025 Badge
  url: https://www.hackster.io/HacksFromPanda/bug-bounty-village-2025-badge-e1fe09
  kind: doc
images:
- file: assets/images/badges/dc33/bug-bounty-village-dc33-badge/ee58f19685.jpg
  source: https://shop.bugbountydefcon.com/products/limited-edition-bbv-blinky-badge-green-pickup-only-def-con
  credit: Bug Bounty Village
  caption: The green BBV Blinky Badge with matrix-style code rain LED artwork, LEDs off
- file: assets/images/badges/dc33/bug-bounty-village-dc33-badge/ea4e31eb71.jpg
  source: https://shop.bugbountydefcon.com/products/limited-edition-bbv-blinky-badge-green-pickup-only-def-con
  credit: Bug Bounty Village
  caption: The badge lit up, showing the cascading LED code-rain effect
- file: assets/images/badges/dc33/bug-bounty-village-dc33-badge/d122e621cf.jpg
  source: https://shop.bugbountydefcon.com/
  credit: Bug Bounty Village
  caption: Bug Bounty Village DC33 badge, powered on, showing green LED matrix code-rain effect
- file: assets/images/badges/dc33/bug-bounty-village-dc33-badge/79c2bc0409.jpg
  source: https://shop.bugbountydefcon.com/
  credit: Bug Bounty Village
  caption: Back side of the Bug Bounty Village DC33 badge showing battery compartment
contact:
  emails:
  - contact@bugbountydefcon.com
notes:
- Badges are only going to be sold online, and ready to be picked up in person at defcon. No shipping, no selling at DEFCON.
- Product page listed only 4 CTF challenges/buttons at time of research, though the community sheet description mentioned 8 challenges tied to the flag mechanism; kept the sheet's phrasing in functions since it may describe a broader badge line.
- 'Sheet originally listed only the maker name with no badge details ("listed for DEF CON 33, no details"). Research found the badge: the DC33 Bug Bounty Village badge, designed by Abhinav Panda of Hackerware.io.'
- Sold pre-order only, pickup at DEF CON, no shipping.
status: released
sources:
- kind: sheet
  event: dc33
  row: 29
  updated: 7/17/2025 16:11:12
- kind: url
  url: https://shop.bugbountydefcon.com/products/limited-edition-bbv-blinky-badge-green-pickup-only-def-con
  title: Limited Edition BBV Blinky Badge – GREEN (Pickup Only @ DEF CON)
  accessed: '2026-09-06'
  note: Confirmed maker (Bug Bounty Village + Abhinav Panda), specs (ATmega16A, 41 SMD LEDs, 4 buttons, 3xAAA batteries), price, distribution terms, and sold-out status; source of product photos.
- kind: sheet
  event: dc33
  row: 3
  tab: 2025 (expected makers)
  updated: ''
- kind: url
  url: https://shop.bugbountydefcon.com/
  title: Bug Bounty Village Shop
  accessed: '2026-09-06'
  note: Price, chip, LED count, battery, buttons, CTF challenge count, sold-out status, and product photos.
- kind: url
  url: https://forum.defcon.org/node/253153
  title: Limited Edition Bug Bounty Village Badge - Available for Pre-Order
  accessed: '2026-09-06'
  note: Confirms limited green DC33 variant, pre-order-only distribution via forum post from Bug Bounty Village organizer.
- kind: url
  url: https://www.hackster.io/HacksFromPanda/bug-bounty-village-2025-badge-e1fe09
  title: Bug Bounty Village 2025 Badge - Hackster.io
  accessed: '2026-09-06'
  note: Confirms Abhinav Panda (HacksFromPanda) as designer of the 2025 badge; acrylic/LED-matrix design description.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: The maker's own Shopify storefront confirmed the core specs and that the badge sold out and shipped a green variant. No GitHub repo, Hackaday project, or hardware/firmware files were found for this specific badge; checked Abhinav Panda's Hackerware.io site, which references a different-year Bug Bounty Village badge (OLED + RGB) but not this one. Quantity made is not published anywhere found. The product description mentions 4 CTF challenges, while the original sheet description mentioned entering binary flags for multiple challenges and a secret "anti-gravity" mode not corroborated by the product page; kept both since the sheet may reflect additional detail from the maker not published in the store listing. Merged with duplicate entry 'Bug Bounty Village DC33 Badge (design by Abhinav Panda)' (dc33-abhinav-panda-listed-for-def-con-33-no-details).
last_modified_date: '2026-09-06'
redirect_from:
- /badges/dc33/abhinav-panda-listed-for-def-con-33-no-details/
---

The Bug Bounty Village at DEF CON 33 offered a limited-edition green "BBV Blinky Badge," designed by the Bug Bounty Village team with hardware hacker Abhinav Panda. The badge centers on a matrix-inspired acrylic panel over an assembled PCB, with 41 SMD LEDs behind it producing a cascading "code rain" effect reminiscent of *The Matrix*, and full-color, multi-layer printed artwork depicting a masked bug hunter.

Built around an ATmega16A microcontroller and powered by three AAA batteries, the badge runs onboard CTF challenges: wearers enter flags using four tactile push buttons, unlocking additional LED sequences as they solve each one. The community badge sheet also described a secret code that reverses the matrix effect and sends the LEDs into an "anti-gravity" mode, though that detail was not confirmed on the storefront listing.

The badge was sold exclusively online in advance through the Bug Bounty Village's Shopify store at $99.99, for pickup only at the village during DEF CON 33 — buyers had to show their order confirmation and a DEF CON badge to collect it, with no shipping and no on-site sales. By the time this entry was researched, the listing showed the badge as sold out. This is a separate, one-off design from the badge Abhinav Panda/Hackerware.io made for the Bug Bounty Village at DC32 and DC34.

## Notes merged from the duplicate entry "Bug Bounty Village DC33 Badge (design by Abhinav Panda)"

The community sheet listed Abhinav Panda as an expected DEF CON 33 maker with no further detail. Panda, who designs hardware under Hackerware.io and has built several badges for DEF CON's Bug Bounty Village in prior years, was the designer behind the Village's DC33 badge: a limited green-PCB badge with acrylic artwork floated above a full matrix of 41 SMD LEDs driven by an ATmega16A. The LEDs animate a Matrix-style "falling code" effect behind the acrylic logo, with the hacker half of the logo lit from below.

Four tactile buttons let wearers enter binary flags tied to eight onboard CTF challenges; solving them unlocks additional LED sequences, including a secret code that reverses the falling-code animation into an "anti-gravity" mode. The badge ran on 3 AAA batteries (included) and sold for $99.99, pre-order only through the Bug Bounty Village's Shopify store, with pickup at DEF CON 33 and no shipping; it sold out.

This same badge is already tracked in the archive under `dc33-bug-bounty-village-dc33-badge` (maker credited there as "Bug Bounty Village"). This entry exists because the community sheet separately listed Panda by name; no evidence was found of a second, distinct item by him at DEF CON 33.
