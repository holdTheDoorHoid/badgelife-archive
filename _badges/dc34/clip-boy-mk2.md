---
title: Clip-Boy Mk2
id: dc34-clip-boy-mk2
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Coruscant Productions, LLC (niko)
  url: https://tropicsquirrel.github.io/shop/
summary: A wrist-mounted, Fallout-parody DEF CON 34 badge built around an ESP32-S3 with a touchscreen and Wi-Fi/Bluetooth recon tools. "Mk2" appears to be alternate naming for the same badge already catalogued as Clip-Boy (dc34-clip-boy), not a distinct second hardware revision.
functions: Wi-Fi and Bluetooth analysis tools, a theremin with customizable LEDs, 90+ unlockable collectibles; ships in a passive listen-only mode with optional research builds available for user installation.
look:
  colors:
  - grey
  shape: null
  themes:
  - retro computer
  - sci-fi
  - puzzle
  - security
  - radio
tech:
  mcu: ESP32-S3
  leds:
    count: null
    type: RGB
    note: Addressable RGB, customizable, feeds a built-in theremin light show.
  display: 2.8" LVGL touchscreen
  connectivity:
  - wifi
  - bluetooth
  battery: null
  sao_version: v1.69bis
get_one:
  price: $120 (first run; sold out)
  price_usd: 120.0
  quantity: '152 units (first run)'
  availability: sold_out
  distribution:
  - purchase
  - preorder
  where: Sold directly by the maker via the Coruscant Productions shop page; a second run was being demand-gauged as of the last check.
make_your_own:
  open_source: true
  hardware_url: https://github.com/SafeHazard/Clip-Boy
  firmware_url: https://github.com/SafeHazard/Clip-Boy
  eda_tool: EasyEDA
links:
- label: tropicsquirrel.github.io/shop
  url: https://tropicsquirrel.github.io/shop/
  kind: website
- label: SafeHazard/Clip-Boy on GitHub
  url: https://github.com/SafeHazard/Clip-Boy
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- 'Sweep wording was "Clip-Boy Mk2"; the maker''s shop and GitHub repo both refer to the badge simply as "Clip-Boy" with no separate Mk2 hardware revision found. This entry duplicates dc34-clip-boy (and dc34-dc34-clip-boy) — same maker, same repo, same specs.'
status: sold_out
sources:
- kind: url
  url: https://tropicsquirrel.github.io/shop/
  title: Clip-Boy Mk2
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://github.com/SafeHazard/Clip-Boy
  title: Clip-Boy Conference Badge
  accessed: '2026-09-10'
  note: Confirms maker, license, hardware/firmware details; identical to dc34-clip-boy entry.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: This entry duplicates the already fully-researched dc34-clip-boy entry (and dc34-dc34-clip-boy). No distinct "Mk2" hardware revision was found on the maker's shop page or GitHub repo; "Mk2" seems to be alternate/informal naming for the same badge. Did not save images or re-fetch details already captured in dc34-clip-boy to avoid duplicating that work.
last_modified_date: '2026-09-10'
---

Clip-Boy is a wrist-mounted, Fallout-parody electronic badge unofficially made for DEF CON 34 by Bryce, a teenage maker operating as Coruscant Productions, LLC (GitHub handle SafeHazard/tropicsquirrel). It runs on an ESP32-S3 with a 2.8" LVGL touchscreen, addressable RGB LEDs driving a built-in theremin light show, and Wi-Fi/Bluetooth analysis tools including code contributed from the ESP32 Marauder project. The badge ships in a passive listen-only mode, with optional research firmware builds available for users to install themselves.

This entry, sourced from the shop page's own "Clip-Boy Mk2" label, appears to describe the same badge already catalogued in more detail as `dc34-clip-boy`: same maker, same GitHub repository (SafeHazard/Clip-Boy), same $120 first-run price, 152-unit quantity, and sold-out status. No second hardware revision was found; the maker's GitHub repo and shop page both refer to the project simply as "Clip-Boy."
