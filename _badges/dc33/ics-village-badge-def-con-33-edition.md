---
title: ICS Village Badge (DEF CON 33 edition)
id: dc33-ics-village-badge-def-con-33-edition
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: FreeWili / DEF CON ICS Village
summary: A standalone hardware badge built by FreeWili for the ICS Village at DEF CON 33, aimed at hands-on industrial control system (ICS) security exploration and sponsored by Intrepid Control Systems.
functions: Runs an onboard gas/"smell" sensor and other environmental sensing as ICS-style challenges, supports WASM scripting, and pairs with a Rust/Iced desktop app ("Build-A-Badge") for uploading custom images, names, and LED lighting patterns.
look:
  colors:
  - multicolor
  shape: null
  themes:
  - village badge
  - security
  - hardware tool
tech:
  mcu: RP2350A
  leds:
    count: null
    type: RGB
    note: Patterns are configured through the companion "Build-A-Badge" customization app rather than fixed in firmware.
  display: full-color screen
  connectivity:
  - wifi
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  - purchase
  where: Distributed at the ICS Village at DEF CON 33; also listed for sale through the Intrepid Control Systems online store (a dedicated "ICS Village Badge for DEFCON 33" product page), which no longer resolves.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: github.com/freewili/FreeWili_WebDocs/blob/main/docs/defcon-badges/icsvillage-badge-defcon33.md
  url: https://github.com/freewili/FreeWili_WebDocs/blob/main/docs/defcon-badges/icsvillage-badge-defcon33.md
  kind: repo
- label: 'store.intrepidcs.com: ICS Village Badge for DEFCON 33'
  url: https://store.intrepidcs.com/product/ics-badge-33
  kind: store
- label: github.com/freewili/build_a_badge (DefCon33 Build a Badge customization app)
  url: https://github.com/freewili/build_a_badge
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: listed
sources:
- kind: url
  url: https://github.com/freewili/FreeWili_WebDocs/blob/main/docs/defcon-badges/icsvillage-badge-defcon33.md
  title: ICS Village Badge (DEF CON 33 edition)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''dc33''. This page now returns 404 (repo appears renamed/removed) and could not be re-fetched directly.'
- kind: url
  url: https://store.intrepidcs.com/product/ics-badge-33
  title: ICS Village Badge for DEFCON 33 - Intrepid Control Systems Store
  accessed: '2026-09-07'
  note: Search results show this as a real Intrepid Control Systems store listing titled "ICS Village Badge for DEFCON 33"; the live page now 404s (client-rendered Next.js shell with no product data), suggesting the listing was delisted after the event.
- kind: url
  url: https://github.com/freewili/build_a_badge
  title: 'GitHub - freewili/build_a_badge: DefCon33 Build a Badge'
  accessed: '2026-09-07'
  note: Companion Rust/Iced GUI desktop app for personalizing FreeWili DEF CON 33 badges (custom images, 14 LED pattern modes, custom name, USB upload); MIT-licensed. Does not itself confirm which specific badge(s) it targets beyond "DefCon33".
- kind: url
  url: https://www.raspberrypi.com/news/creating-the-most-advanced-event-badge-yet-for-the-biohacking-village-at-def-con/
  title: Creating the most advanced event badge yet for the Biohacking Village at DEF CON - Raspberry Pi
  accessed: '2026-09-07'
  note: 'Article is about a different (Biohacking Village) badge, but a reader comment independently corroborates two facts about this badge: "the DEFCON badge from ICS village was also great, featuring an AI smell sensor. They used the Raspberry Pi RP2350A."'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The maker''s own documentation page (both the GitHub Pages source and its mirror at docs.freewili.com/defcon-badges/icsvillage-badge-defcon33/) is no longer reachable (404) as of 2026-09-07, and the Intrepid Control Systems store listing for this badge has likewise gone dead. Facts here (RP2350A MCU, AI/gas "smell" sensor, full-color screen, WASM scripting, Kyle Irving PCB art, sponsorship by Intrepid Control Systems) come from consistent search-engine snippets of that now-unreachable maker page plus one independent third-party corroboration (a Raspberry Pi blog comment confirming the RP2350A and smell sensor). Could not verify price, quantity made, exact LED count, battery, or SAO header presence, and found no reachable photo of the badge itself, so no images were saved. Distinct from the FreeWili "ICS Village DEF CON 34 Badge" (RP2350B-A4, RS485/CAN/10BASE-T1S), which is a separate, later product. Not the same item as dc32-ics-village-unnamed-badge-sao (a different event and unrelated badge/SAO).'
last_modified_date: '2026-09-07'
---

The ICS Village Badge (DEF CON 33 edition) is a standalone hardware badge that FreeWili built for the ICS Village at DEF CON 33, in partnership with Intrepid Control Systems, as a hands-on tool for exploring industrial control system (ICS) security. It follows on from FreeWili's earlier "Whale Tail" badge line and, according to the maker's own now-offline documentation and corroborating search-engine indexing, is built around a Raspberry Pi RP2350A microcontroller with a full-color screen and an onboard AI-assisted gas/"smell" sensor used for on-site challenges, alongside Wi-Fi connectivity and support for WASM scripting.

Owners could personalize their badge with a companion desktop app, "Build-A-Badge" (Rust, Iced GUI, MIT-licensed, published on GitHub as `freewili/build_a_badge`), which uploads custom images, a custom name, and a choice of roughly 14 LED lighting patterns over USB. The badge appears to have also been sold directly through an Intrepid Control Systems online store listing ("ICS Village Badge for DEFCON 33"), separate from whatever was handed out in the ICS Village itself.

Both of the maker's primary reference pages for this badge — the GitHub-hosted documentation file and its mirror on docs.freewili.com — return 404 as of this research pass, as does the Intrepid Control Systems store listing, so several details (exact price, quantity produced, battery, and precise LED count) could not be confirmed. This is a different, earlier product from the "ICS Village DEF CON 34 Badge" that FreeWili later sold for DEF CON 34 (built around an RP2350B-A4 with industrial bus interfaces), and is unrelated to the separate dc32-ics-village-unnamed-badge-sao entry from DEF CON 32.
