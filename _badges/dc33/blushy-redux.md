---
title: Blushy Redux
id: dc33-blushy-redux
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc33
year: 2025
series: Blushy
makers:
- name: GhostGlitch
  url: https://ghostglitch.net
summary: A no-microcontroller, fully analog SAO shaped like a pixel-art blushing ghost, updated for DC33 with always-on LEDs and an eSAO accessory header for tiny "hats."
functions: An updated take on our previous blushing ghost design, this ghost of many hats now comes with always-on blinkenlights! Boop the capacitive-touch cheeks and Blushy reacts (and gets annoyed if you boop too much); an eSAO 3-pin header on top lets it wear small accessory "hats."
look:
  colors:
  - white
  - pink
  shape: ghost
  themes:
  - mascot
  - halloween
tech:
  mcu: none
  leds:
    count: 6
    type: discrete
    note: Surface-mount LEDs driven by discrete analog circuitry (transistors, a 555-style oscillator, no code); always-on in the Redux revision. Capacitive-touch pads form the ghost's blushing "cheeks."
  display: none
  connectivity: []
  inputs:
  - touch
  - capacitive
  battery: powered by host badge
  sao_version: null
get_one:
  price: 1 Social Interaction
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given away in person at DEF CON by the GhostGlitch team.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: KiCad
links:
- label: ghostglitch.net
  url: https://ghostglitch.net
  kind: website
  archived: https://web.archive.org/web/20251014071724/https://ghostglitch.net/
- label: Blushy SAO page
  url: https://ghostglitch.net/sao/blushy
  kind: website
  archived: https://web.archive.org/web/20251213162553/https://ghostglitch.net/sao/blushy
- label: eSAO Hats page
  url: https://ghostglitch.net/sao/hats
  kind: website
  archived: https://web.archive.org/web/20251213161720/https://ghostglitch.net/sao/hats
- label: 'Blog: Making Friends by Ghosting Strangers'
  url: https://ghostglitch.net/blog/2025/jan/10
  kind: article
images:
- file: assets/images/badges/dc33/blushy-redux/55779c3fa3.jpg
  source: https://ghostglitch.net/sao/blushy
  credit: GhostGlitch
  caption: Blushy SAO, front
  archived: https://web.archive.org/web/20251213162553/https://ghostglitch.net/sao/blushy
- file: assets/images/badges/dc33/blushy-redux/b0f783a348.jpg
  source: https://ghostglitch.net/sao/hats
  credit: GhostGlitch
  caption: Blushy with eSAO hat accessories attached
  archived: https://web.archive.org/web/20251213161720/https://ghostglitch.net/sao/hats
contact:
  emails:
  - contact@ghostglitch.net
notes:
- Come find us at the con!
status: released
sources:
- kind: sheet
  event: dc33
  row: 34
  updated: 7/25/2025 22:21:35
- kind: url
  url: https://ghostglitch.net/sao/blushy
  title: Blushy the Blushing Ghost | GhostGlitch
  accessed: '2026-09-06'
  note: Current description of the Blushy SAO (capacitive-touch boop behavior, analog design); confirms shape and general concept, though the page does not distinguish the "Redux" revision by name.
  archived: https://web.archive.org/web/20251213162553/https://ghostglitch.net/sao/blushy
- kind: url
  url: https://ghostglitch.net/sao/hats
  title: eSAO Hats! | GhostGlitch
  accessed: '2026-09-06'
  note: Describes the eSAO (even Shittier Add-On) 3-pin accessory header referenced in the sheet's "ghost of many hats" description.
  archived: https://web.archive.org/web/20251213161720/https://ghostglitch.net/sao/hats
- kind: url
  url: https://ghostglitch.net/sao
  title: All the SAOs | GhostGlitch
  accessed: '2026-09-06'
  note: Defines the eSAO connector pinout (data, ground, 3.3V) and lists GhostGlitch's SAO lineup.
  archived: https://web.archive.org/web/20251014075544/https://ghostglitch.net/sao
- kind: url
  url: https://ghostglitch.net/blog/2025/jan/10
  title: Making Friends by Ghosting Strangers
  accessed: '2026-09-06'
  note: Origin story of Blushy — fully analog design (no microcontroller, low pin-count capacitive touch IC, transistors), and manufacturing history (an earlier batch of ~150 boards); does not mention the DC33 Redux revision specifically.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: |
    Maker's own site (ghostglitch.net) confirms Blushy is a fully analog SAO (no microcontroller) with capacitive-touch "boop" interaction and an eSAO 3-pin accessory header for "hats," matching the sheet's description of this DC33 entry as an updated ("Redux") version with always-on LEDs. However, the site's current Blushy/hats pages describe the SAO generally and do not call out a distinct "Redux" revision by name, so revision-specific details (exact LED behavior change, quantity made for DC33, SAO header version, open-source status of hardware/firmware files) could not be confirmed and are left empty rather than guessed. LED count (6) and colors (white PCB, pink under lighting) are read directly from the maker's own product photo.
last_modified_date: '2026-09-06'
---

Blushy is GhostGlitch's pixel-art blushing-ghost SAO, notable for having no microcontroller at all: its blush, blinkenlights, and reaction to being "booped" all come from discrete analog circuitry — transistors, a square-wave oscillator, and a low-pin-count capacitive-touch IC — rather than code. The team built it as a follow-up to their earlier "Magic Blue Ball" SAO after attending DEF CON and discovering the SAO add-on spec; the original Blushy run numbered roughly 150 boards, hand-assembled with a pick-and-place and a converted toaster-oven reflow setup.

"Blushy Redux" is GhostGlitch's DC33 (2025) update to the design, described on the community sheet as adding always-on LEDs to the existing blushing-ghost concept. The SAO carries a 3-pin "eSAO" (even Shittier Add-On) header on top — data, ground, and 3.3V — that lets small accessory pieces ("hats": novelty items like Frankenstein neck screws or rubber ducks) plug into the ghost. As with GhostGlitch's other badges, it was given away for free at the con in exchange for conversation ("1 Social Interaction" on the sheet) rather than sold.

## Make your own

No hardware, firmware, or fabrication files for Blushy are published; GhostGlitch's site does describe the eSAO connector pinout for anyone who wants to design a compatible accessory, but the ghost board itself is not open-sourced as far as could be found.
