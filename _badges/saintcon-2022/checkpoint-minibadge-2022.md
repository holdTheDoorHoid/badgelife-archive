---
title: CHECKPOINT MINIBADGE (2022)
id: saintcon-2022-checkpoint-minibadge-2022
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: Jup1t3r
summary: A sponsor minibadge SAINTCON 2022 designed for Check Point to show off the company's new logo, built around a single LED that can be jumpered to run solid or blinking.
functions: 'No interactivity beyond the LED: a 3-pin jumper on the back selects solid-on or blinking mode for the single LED.'
look:
  colors:
  - black
  - gold
  shape: circle
  themes:
  - logo
  - security
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: Single through-hole LED with a series resistor; a 3-position jumper header selects solid vs. blink.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given out at the Check Point sponsor booth at SAINTCON 2022 for visiting and interacting with staff.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  kind: website
images:
  - file: assets/images/badges/saintcon-2022/checkpoint-minibadge-2022/8d089995fd.jpg
    source: "https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf"
    credit: "SAINTCON / Jup1t3r"
    caption: "Checkpoint minibadge front, with LED, resistor, and solid/blink jumper pads on the back"
contact: {}
notes:
- Sponsor minibadge for Checkpoint at SAINTCON 2022. Found by the event-year sweep, task saintcon-2022.
- 'Sheet/sweep used the sponsor''s informal one-word spelling "Checkpoint"; the assembly guide page itself also
  titles it "CHECKPOINT MINIBADGE" but the on-badge silkscreen and sponsor name are "Check Point" (checkpoint.com).
  Kept the guide''s title as-is since that is the maker/event''s own heading.'
status: released
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: CHECKPOINT MINIBADGE (2022)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2022); event read as ''saintcon-2022''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: SAINTCON Minibadge Assembly Guide 2022, page 37 (Checkpoint Minibadge)
  accessed: '2026-09-10'
  note: 'Full assembly-guide page confirms designer (Jup1t3r), that Check Point is a 2022 sponsor who commissioned
    the badge to showcase their new logo, distribution (free at the Check Point sponsor booth), difficulty
    (beginner), rarity (common), and the single-LED/resistor/3-pin solid-blink jumper build. Also used to extract
    the front-image PNG embedded on that page for the images field.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: The assembly guide (the entry's only source, a 98-page PDF) is the maker/event's own document and fully
    confirms the badge, its designer, and its build/distribution details. No separate maker storefront, repo, or
    press coverage was found for this specific minibadge (expected for a one-off sponsor giveaway); hardware/firmware
    files, exact quantity made, and a price (it was a free sponsor-booth item, not sold) are not stated anywhere
    found. tech.mcu is 'none' because the badge is a passive LED board with no microcontroller.
last_modified_date: '2026-09-10'
---

Checkpoint Minibadge is a sponsor minibadge from SAINTCON 2022, commissioned by security company Check Point and designed by SAINTCON regular Jup1t3r to show off the sponsor's then-new logo. The circular black PCB carries the Check Point mark in gold/copper, one through-hole LED, a series resistor, and a 3-pin jumper header on the back that lets the builder choose between the LED running solid or blinking.

Unlike most personal minibadges sold or traded among attendees, this one was a sponsor giveaway: attendees obtained it for free by visiting the Check Point booth on the SAINTCON expo floor and interacting with staff there, rather than through the community swap/sale market. The SAINTCON assembly guide rates it beginner difficulty and common rarity, consistent with its simple single-LED build intended for quick soldering practice at the booth.

No independent hardware/firmware release, storefront, or press coverage beyond the official SAINTCON 2022 Minibadge Assembly Guide was found; that guide (a maker/event first-party source) is the basis for all details above.
