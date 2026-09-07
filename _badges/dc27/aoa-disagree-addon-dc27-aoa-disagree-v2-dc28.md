---
title: AOA Disagree Addon (DC27) / AOA Disagree v2 (DC28)
id: dc27-aoa-disagree-addon-dc27-aoa-disagree-v2-dc28
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: trueControl / true
  url: https://shop.truecontrol.org/
  role: circuit, layout, and code
- name: Cprossu
  role: concept
summary: A SAO/GAT-standard addon that pokes fun at the Boeing 737 MAX "AOA DISAGREE"
  indicator, blinking a row of LEDs to warn that its two angle-of-attack sensors disagree.
functions: 'DC27 original: a 555-timer astable circuit blinks 10 orange LEDs per board,
  with period and duty cycle adjustable via rear-mounted trimpots, and boards buildable
  right-side-up or upside-down. DC28 v2: replaces the 555 with trueControl''s own "WP
  CHIP" digital logic, adds an 11th LED per board, and keeps configurable display
  programs/speeds via rear-mounted trimpots.'
look:
  colors:
  - orange
  shape: null
  themes:
  - meme
tech:
  mcu: 'DC27: NE555 timer (analog, not a microcontroller); DC28 v2: trueControl "WP CHIP" custom digital logic'
  leds:
    count: 10
    type: discrete
    note: Through-hole high-visibility orange LEDs, 10 per board on DC27; DC28 v2 uses 11 per board.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: 2-pack solder kit around $15-20; DC28 v2 fully-assembled single unit was $13
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: 'Checked 2026-09-07: the DC27 kit (product_id=90) and the DC28
    v2 fully-assembled listing (product_id=68) both return "Product not found" on
    trueControl''s shop. The DC28 v2 2-pack solder kit (product_id=69) is still listed,
    showing "Availability: 1".'
  distribution:
  - purchase
  - kit
  where: Sold through trueControl's own OpenCart storefront (shop.truecontrol.org),
    both as an intermediate-difficulty solder kit and (for the DC28 v2) fully assembled.
    Proceeds funded Whiskey Pirates projects.
make_your_own:
  open_source: partial
  hardware_url: https://dc28.whiskeypirates.com/img/aoav2-gat-brev3-sch.png
  firmware_url: null
  eda_tool: null
  notes: A build/assembly guide for the DC28 v2 kit is published at dc28.whiskeypirates.com/manual/aoa-disagree-v2-build,
    and a schematic PNG for the v2 board is linked from the same site. No full source
    repo, Gerbers, or BOM file were found for either version.
links:
- label: basic.truecontrol.org/dc27/aoa-disagree
  url: https://basic.truecontrol.org/dc27/aoa-disagree/
  kind: website
- label: basic.truecontrol.org/database/dc27/aoa-disagree (live page)
  url: https://basic.truecontrol.org/database/dc27/aoa-disagree/
  kind: website
- label: basic.truecontrol.org/database/dc28/aoa-disagree-v2 (v2 page)
  url: https://basic.truecontrol.org/database/dc28/aoa-disagree-v2/
  kind: website
- label: AOA Disagree DC27 Addon (2Pk Solder Kit) - shop listing
  url: https://shop.truecontrol.org/index.php?route=product/product&product_id=90
  kind: store
- label: AOA Disagree v2 DC28 Addon Badge - assembled shop listing
  url: https://shop.truecontrol.org/index.php?route=product/product&product_id=68
  kind: store
- label: AOA Disagree v2 DC28 Addon (2Pk Solder Kit) - shop listing
  url: https://shop.truecontrol.org/index.php?route=product/product&product_id=69
  kind: store
- label: dc28.whiskeypirates.com project page
  url: https://dc28.whiskeypirates.com/
  kind: website
- label: AOA v2 build/assembly guide
  url: https://dc28.whiskeypirates.com/manual/aoa-disagree-v2-build
  kind: doc
- label: AOA v2 schematic (PNG)
  url: https://dc28.whiskeypirates.com/img/aoav2-gat-brev3-sch.png
  kind: doc
images:
- file: assets/images/badges/dc27/aoa-disagree-addon-dc27-aoa-disagree-v2-dc28/cc4749584c.jpg
  source: "https://shop.truecontrol.org/index.php?route=product/product&product_id=69"
  credit: "trueControl"
  caption: "Assembled AOA Disagree v2 addon, two-pack finished units"
- file: assets/images/badges/dc27/aoa-disagree-addon-dc27-aoa-disagree-v2-dc28/5464c46923.jpg
  source: "https://shop.truecontrol.org/index.php?route=product/product&product_id=69"
  credit: "trueControl"
  caption: "AOA Disagree v2 addon board during assembly, LEDs and WP CHIP module populated"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
- The community sheet's title bundles two distinct releases into one entry; DC27
  (2019) is the original 555-timer kit, DC28 (2020) is the "v2" digital redesign.
  This entry is filed under dc27 (its original release) per the research guide's
  rule to use the con the item was made for.
status: released
sources:
- kind: url
  url: https://basic.truecontrol.org/dc27/aoa-disagree/
  title: AOA Disagree Addon (DC27) / AOA Disagree v2 (DC28)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc27''.'
- kind: url
  url: https://basic.truecontrol.org/database/dc27/aoa-disagree/
  title: AOA Disagree Addon - trueControl BASIC
  accessed: '2026-09-07'
  note: The linked URL 404s; the live page lives one level deeper under /database/.
    Confirmed maker (trueControl), event placement (DC27 @ Caesars), and the DC28
    v2 sibling page via the site nav, though the page's own content body is empty
    on trueControl's site.
- kind: url
  url: https://shop.truecontrol.org/index.php?route=product/product&product_id=90
  title: AOA Disagree DC27 Addon (2Pk Solder Kit) - trueControl Shop
  accessed: '2026-09-07'
  note: Archived copy (web.archive.org, snapshot 2025-03-27) used since the live
    listing now 404s. Source for DC27 original description, 555-timer/orange-LED
    specs, BOM, and price.
- kind: url
  url: https://shop.truecontrol.org/index.php?route=product/product&product_id=68
  title: AOA Disagree v2 DC28 Addon Badge (2020) - trueControl Shop
  accessed: '2026-09-07'
  note: Archived copy (web.archive.org, snapshot 2022-07-06) used since the live
    listing now 404s. Source for the assembled DC28 v2 description and price, and
    the sibling product IDs.
- kind: url
  url: https://shop.truecontrol.org/index.php?route=product/product&product_id=69
  title: AOA Disagree v2 DC28 Addon (2Pk Solder Kit) - trueControl Shop
  accessed: '2026-09-07'
  note: Live listing. Source for the DC28 v2 kit description, WP CHIP/11-LED detail,
    BOM, price, current stock, and the two saved photos.
- kind: url
  url: https://dc28.whiskeypirates.com/manual/aoa-disagree-v2-build
  title: AOA v2 Build Instructions
  accessed: '2026-09-07'
  note: Confirmed DC28 v2 kit contents (2x REV3 boards, WP CHIP, resistor/cap/LED
    counts) and assembly technique.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Core facts (maker, concept credit, event/year for both releases, circuit
    design, LED counts, kit contents, pricing history) come from trueControl's own
    shop listings and build manual. Total quantity made was not stated anywhere
    found. The DC27 original's exact PCB color/finish and any board photos of it
    specifically were not found; the two saved photos are both of the DC28 v2 (the
    only version with images available). No maker-published contact details were
    found. trueControl's own basic.truecontrol.org documentation page for this item
    has an empty content body (appears to be a site-wide build issue, not specific
    to this entry) so it contributed only navigation/context, not descriptive text.
last_modified_date: '2026-09-07'
---

The AOA Disagree Addon is trueControl's send-up of the Boeing 737 MAX's infamous "AOA DISAGREE" cockpit alert, which warned pilots that the plane's two angle-of-attack sensors were reporting conflicting data — an alert notoriously omitted as a paid option on some 737 MAX aircraft before the type's 2019 grounding. The badge does the same job in miniature: a row of LEDs that blinks to tell you its sensors disagree, "more reliable than Boeing equipment as shipped." Concept by Cprossu, with circuit, layout and firmware/logic by true of trueControl; proceeds funded the Whiskey Pirates group's DEF CON projects.

The original version launched at DEF CON 27 (2019) as an intermediate solder kit built around a 555-timer astable oscillator blinking 10 high-visibility orange LEDs per board, with period and duty cycle set by rear-mounted trimpots. It was sold as a 2-pack kit (enough parts for two working boards plus one spare "unlicensed" PCB) and doubled as a soldering-101 teaching kit at the con, complete with right-side-up and upside-down board variants. For DEF CON 28 (2020) trueControl released the "AOA Disagree v2": the 555 timer was swapped for trueControl's own "WP CHIP" digital logic, the LED count grew to 11 per board, and it kept the same rear-trimpot-configurable blink behavior. The v2 was sold both as a fully-assembled SAO addon and as a 2-pack solder kit, with an optional retention lanyard (required to meet the GAT addon standard) so it could hang off a host badge without getting lost.

As of this check (2026-09-07), the original DC27 kit and the assembled DC28 v2 listing have both been pulled from trueControl's shop (their product pages now 404), while the DC28 v2 solder kit remains listed with a single unit in stock. A build/assembly guide and board schematic for the v2 are published on the Whiskey Pirates' DC28 project site.

## Make your own

No hardware source files (schematics beyond a single PNG, Gerbers, BOM spreadsheets, or firmware) were found published for either version. What is available:

- A step-by-step assembly guide for the DC28 v2 kit at [dc28.whiskeypirates.com/manual/aoa-disagree-v2-build](https://dc28.whiskeypirates.com/manual/aoa-disagree-v2-build), covering component placement order and SMD soldering technique for the resistors, capacitor, trimpots, WP CHIP, and LEDs.
- A schematic image for the v2 board ("REV3"): [aoav2-gat-brev3-sch.png](https://dc28.whiskeypirates.com/img/aoav2-gat-brev3-sch.png).
