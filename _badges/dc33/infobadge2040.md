---
title: InfoBadge2040
id: dc33-infobadge2040
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: TheBadgES
  url: https://thebadg.es
summary: A reprogrammable e-ink event badge built around a Raspberry Pi Pico (RP2040), sold to DEF CON 33 attendees for on-site pickup.
functions: |-
  InfoBadge2040 is a customizable electronic ID badge powered by the Raspberry Pi Pico (RP2040). It’s designed to reflect your personality or event branding.
  We built InfoBadge2040 to solve a common problem at tech events: boring, disposable name tags that don’t reflect the creativity of the people wearing them. We wanted a reprogrammable badge that looked good, could be personalized easily, and made a statement — without being bulky or overcomplicated. The RP2040 gave us the flexibility and performance to make that vision real.

  PURCHASE ONLY IF YOU ARE ATTENDING DEFCON33. THE DELIVERY WILL BE AT THE CONFERENCE.
look:
  colors:
  - black
  shape: rectangle
  themes:
  - text
  - minimalist
tech:
  mcu: RP2040
  leds: null
  display: 2.9" 4-color e-paper (black/white/red/yellow, ~11s refresh)
  connectivity:
  - uart
  battery: battery-less design (low-power e-ink)
  sao_version: none
get_one:
  price: 50$
  price_usd: 50
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold on Tindie (thebadges shop); pickup was at DEF CON 33 itself, not shipped
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/thebadges/infobadge2040
  url: https://www.tindie.com/products/thebadges/infobadge2040/
  kind: store
- label: thebadg.es
  url: https://thebadg.es
  kind: website
  archived: https://web.archive.org/web/20260515222208/https://www.thebadg.es/
images:
- file: assets/images/badges/dc33/infobadge2040/bf54a34667.jpg
  source: https://www.tindie.com/products/thebadges/infobadge2040/
  credit: TheBadgES
  caption: InfoBadge2040 e-ink badge, front view (displaying a QR code and text)
- file: assets/images/badges/dc33/infobadge2040/7b33cd97b6.jpg
  source: https://www.tindie.com/products/thebadges/infobadge2040/
  credit: TheBadgES
  caption: InfoBadge2040 PCB, back view
contact:
  emails:
  - info@thebadg.es
notes: []
status: released
sources:
- kind: sheet
  event: dc33
  row: 33
  updated: 7/24/2025 12:33:40
- kind: url
  url: https://www.tindie.com/products/thebadges/infobadge2040/
  title: InfoBadge2040 - Tindie
  accessed: '2026-09-06'
  note: Confirmed price ($50), 2.9-inch 4-color e-ink display with ~11s refresh, SPI interface, sold out since Aug 4 2025, product photos.
- kind: url
  url: https://thebadg.es
  title: thebadg.es - Event Tech Badge Company
  accessed: '2026-09-06'
  note: 'Maker''s own site: confirms RP2040, battery-less/low-power e-ink design, UART programming, user-programmable via Arduino IDE or Raspberry Pi SDK, QR code generation, contact email.'
  archived: https://web.archive.org/web/20260515222208/https://www.thebadg.es/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Core specs (RP2040, 2.9" 4-color e-ink, UART programming, $50) confirmed by both the Tindie storefront and the maker's own site (thebadg.es). No GitHub repo, Hackerday.io project, or published hardware/firmware files were found, so make_your_own fields are left empty rather than guessed. Battery/power detail is the maker's own phrasing ("battery-less design with low-power e-ink display") and is a little ambiguous about how the badge is actually powered day-to-day; left as-is rather than interpreted. No LED info found. Status set to released since this was sold and delivered at DEF CON 33 (not merely announced), and get_one.availability set to sold_out per the Tindie listing (out of stock since 2025-08-04). Quantity made was not stated anywhere found.
last_modified_date: '2026-09-06'
---

InfoBadge2040 is a reprogrammable electronic ID badge made by TheBadgES (a Valencia, Spain-based event-badge company) for DEF CON 33 attendees. It's built around a Raspberry Pi Pico (RP2040) driving a 2.9-inch four-color e-paper display (black, white, red, yellow) with an around-11-second refresh, and is described by the maker as a "battery-less design" using the display's low power draw. The badge can be personalized with a wearer's name, role, company, and social handles, and can generate its own QR code; the maker says it's fully hackable and can be reprogrammed over UART using either the Arduino IDE or the Raspberry Pi Pico SDK.

The badge was sold through Tindie for $50, explicitly restricted to attendees of DEF CON 33 with delivery only at the conference (no shipping). The listing has been marked out of stock since August 4, 2025. TheBadgES also sold a companion item that year, "The Big Badge Game" (a separate archive entry), and offers custom badge runs and soldering workshops for other events. No public GitHub repository, Hackaday.io project, or Gerber/BOM files were located, so this appears to be a closed-design product rather than an open-hardware release.
