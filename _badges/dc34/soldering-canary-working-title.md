---
title: Volatile Organic Canary SAO
id: dc34-soldering-canary-working-title
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: Xenu (team name is Lepi Labs)
  url: https://lepi-labs.com
summary: A novelty air-quality SAO that uses a Sensirion SGP40 VOC sensor to react, playfully and inexactly, to soldering fumes and other airborne compounds.
functions: 'Cycles through five modes via a Mode button: a VOC-index emote display (eyes go from ^^ to XX and the RGB LED shifts blue-to-red as air quality worsens), a numeric VOC-index readout, and three idle animations (pinwheel, looping eyes, cartoon blinking eyes). Explicitly for novelty use only, not a reliable measurement.'
look:
  colors:
  - yellow
  - orange
  - white
  shape: bird
  themes:
  - bird
  - animal
  - measurement
tech:
  mcu: ATtiny1616
  leds:
    count: 1
    type: RGB
    note: Single RGB LED, interrupt-driven, transitions blue to green to yellow to red with worsening VOC index.
  display: 2-character 14-segment display (dual 74595 shift registers)
  connectivity:
  - i2c
  battery: CR2032 (also runs on SAO connector power)
  sao_version: null
get_one:
  price: $45
  price_usd: 45.0
  quantity: null
  availability: sold_out
  availability_note: Uberflux storefront showed 0 remaining, 11 sold, as of 2026-09-06 (re-checked 2026-09-07). Total made is not stated; the repo says it was also sold in person at DEF CON 34.
  distribution:
  - purchase
  where: Sold at DEF CON 34 and through the Uberflux marketplace.
make_your_own:
  open_source: true
  hardware_url: https://github.com/lepi-labs/5-dc34-canary-badge
  firmware_url: https://github.com/lepi-labs/5-dc34-canary-badge
  eda_tool: KiCad
links:
- label: lepi-labs.com/shop
  url: https://lepi-labs.com/shop
  kind: store
- label: lepi-labs.com
  url: https://lepi-labs.com
  kind: website
- label: github.com/lepi-labs/5-dc34-canary-badge
  url: https://github.com/lepi-labs/5-dc34-canary-badge
  kind: repo
- label: uberflux.com/product/LEPI-dc34-canary
  url: https://uberflux.com/product/LEPI-dc34-canary
  kind: store
images:
- file: assets/images/badges/dc34/soldering-canary-working-title/05825e7aeb.jpg
  source: https://github.com/lepi-labs/5-dc34-canary-badge
  credit: Lepi Labs
  caption: Volatile Organic Canary SAO
- file: assets/images/badges/dc34/soldering-canary-working-title/aa0646ce7d.jpg
  source: https://uberflux.com/product/LEPI-dc34-canary
  credit: Lepi Labs
  caption: Volatile Organic Canary SAO product photo
contact:
  discord: xenu
  emails:
  - xenu@lepi-labs.com
  raw:
  - 'Bluesky:'
notes:
- Sheet title was "Soldering Canary (working title)"; the maker's own repo and storefront name it "Volatile Organic Canary SAO".
status: released
sources:
- kind: sheet
  event: dc34
  row: 9
  updated: 5/26/2026 20:37:04
  listing: New
- kind: url
  url: https://github.com/lepi-labs/5-dc34-canary-badge
  title: 5-dc34-canary-badge (README) - lepi-labs
  accessed: '2026-09-06'
  note: Maker's own repo README and hardware overview; confirmed real title, MCU, sensors, pinout, modes, and that hardware/firmware/KiCad files are published.
- kind: url
  url: https://uberflux.com/product/LEPI-dc34-canary
  title: Volatile Organic Canary SAO - Uberflux
  accessed: '2026-09-06'
  note: Storefront listing; confirmed price ($45), sold-out status (0 remaining, 11 sold), battery (CR2032), and description; source of the product photo.
- kind: url
  url: https://lepi-labs.com/shop
  title: Lepi Labs shop
  accessed: '2026-09-06'
  note: Current shop page no longer lists this item (only other Lepi Labs badges); confirms it is not currently sold there.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-06'
  notes: Verified 2026-09-07 against the maker's GitHub README, the repo file listing (KiCad files under board/, firmware under code/, no LICENSE) and the Uberflux listing. The community sheet's working title and link (lepi-labs.com/shop) did not resolve to this item directly; found via the maker's GitHub org (lepi-labs), whose "5-dc34-canary-badge" repo names the real product "Volatile Organic Canary SAO" and links to the Uberflux storefront where it was actually sold. Quantity (11 sold) and sold-out status are as observed on Uberflux at last check, not necessarily final. No LICENSE file was found in the repo, so hardware/firmware are published but license terms are unstated.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc34/soldering-canary-working-title.glb
  method: kicad
  source_file: board/5-dc34-canary-badge.kicad_pcb
  generated: '2026-09-07'
  bytes: 231764
---

The Volatile Organic Canary is a SAO made by Xenu of Lepi Labs for DEF CON 34, built around a Sensirion SGP40 volatile-organic-compound sensor paired with an SHT4x for temperature/humidity compensation. An ATtiny1616 drives a two-character 14-segment display and a single RGB LED, cycling through a VOC-index "emote" mode (a canary face that changes from ^^ to XX as air quality worsens, with the LED sliding from blue toward red), a numeric VOC-index readout, and three idle animations. The maker is explicit that the SGP40's VOC index measures relative changes in air quality rather than an absolute, calibrated reading, so the badge is meant as a playful indicator of things like soldering fumes rather than a real safety instrument.

It was sold at DEF CON 34 and through the Uberflux marketplace for $45; the Uberflux listing showed 11 sold and none remaining as of this check. Hardware (KiCad schematics and PCB) and firmware source are published on GitHub under Lepi Labs' account, though no license file accompanies them. The badge can run either from SAO connector power or a CR2032 battery, and exposes an unsoldered UPDI header for reprogramming the ATtiny (3.3V only, with the battery removed first, since the header's VCC line is not diode-protected).

The community badge sheet listed this entry under a working title, "Soldering Canary," which did not match the maker's own naming; the actual product name, confirmed from the maker's GitHub README and storefront listing, is "Volatile Organic Canary SAO."
