---
title: Cyber City Circuits Red Team Village badges (DEF CON 33)
id: dc33-cyber-city-circuits-listed-for-def-con-33-no-details
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: Cyber City Circuits
  url: https://cybercitycircuits.com
summary: A custom PCB fabrication and assembly shop that designed and built three badges for the Red Team Village at DEF CON 33; the badge designs themselves are not documented anywhere the maker has published.
functions: ''
look:
  colors: []
  shape: null
  themes:
  - security
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 3
  availability: unknown
  distribution:
  - village
  where: Red Team Village at DEF CON 33
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- kind: website
  label: Cyber City Circuits
  url: https://cybercitycircuits.com
- kind: store
  label: Cyber City Circuits event badge storefront (BadgesBadgesBadges.com)
  url: https://badgesbadgesbadges.com
images: []
contact: {}
notes:
- "Sheet listed only the maker name with no badge details; this was DEF CON 33's version of the same open item as the dc32 entry for this maker."
status: released
sources:
- kind: sheet
  event: dc33
  row: 29
  tab: 2025 (expected makers)
  updated: ''
- kind: url
  url: https://cybercitycircuits.com
  title: Cyber City Circuits — home page
  accessed: '2026-09-06'
  note: "Confirms CCC is a PCB design/assembly/rapid-prototyping shop (North Augusta, SC, veteran-owned, est. 2018) that offers 'Custom PCB Event Badges'; a customer review states CCC 'produced three amazing badges for RTV at DEF CON 33'."
- kind: url
  url: https://badgesbadgesbadges.com
  title: BadgesBadgesBadges.com — Cyber City Circuits' event-badge storefront
  accessed: '2026-09-06'
  note: "Repeats the same DEF CON 33 / RTV review; lists CCC's general customizable badge spec (up to 4 RGB LEDs, 12 patterns, onboard microprocessor, USB-C, single battery) but has no page specific to the DEF CON 33 / RTV badges themselves."
research:
  status: researched
  confidence: low
  last_checked: '2026-09-06'
  notes: >-
    "Cyber City Circuits" (CCC) is a contract PCB design/assembly business, not a
    hobbyist badge line, which is why the sheet only had a maker name and no
    other details: they were commissioned to fabricate badges for someone else's
    village rather than releasing a badge under their own name. The only
    corroborating source found is a customer (Brian Sak) review on CCC's own
    website stating CCC "produced three amazing badges for RTV [Red Team
    Village] at DEF CON 33." No page from CCC, Red Team Village, or press
    describes those three badges' design, chips, LEDs, or appearance, and no
    photo of them was located, so most technical and look fields are left
    empty rather than guessed. `type` is set to `badge` and `get_one.quantity`
    to 3 on the strength of that one review; `availability`/`status` reflect
    that the badges were handed out at the village rather than sold. General
    specs shown on CCC's badge storefront (BadgesBadgesBadges.com) are listed
    only in the links/notes, not copied into `tech`, since they describe CCC's
    generic badge product line, not confirmed to be what RTV actually got.
    Web search tooling was largely blocked (search-engine CAPTCHAs, exhausted
    session search budget) after the initial useful hits, so further
    corroboration was not attempted this pass.
last_modified_date: '2026-09-06'
---

Cyber City Circuits (CCC) is a PCB design, assembly, and rapid-prototyping company based in North Augusta, South Carolina, founded in 2018 and run as a service-disabled-veteran-owned small business. It normally does contract PCB work — assembly, reverse engineering, and unsupported-hardware recreation — and separately runs a custom-event-badge product line under the storefront BadgesBadgesBadges.com. The community badge sheet listed the company as an expected DEF CON 33 (2025) maker with no further detail.

The only confirmation found of what they actually brought to DEF CON 33 is a customer review on CCC's own site from Brian Sak, who wrote that "David and CCC were phenomenal to work with and produced three amazing badges for RTV [Red Team Village] at DEF CON 33." That places CCC as the fabricator/designer of a set of three badges made for the Red Team Village at that con, rather than a badge CCC released under its own brand. No page describing those specific badges — their look, chip, LEDs, or how they were distributed to village attendees — could be located from CCC, Red Team Village, or press coverage, so this entry records the confirmed fact of the commission without guessing at the hardware.

CCC's general badge-storefront page advertises a standard customizable badge spec (up to four RGB LEDs with a dozen selectable patterns, an onboard microcontroller, USB-C charging, single-battery operation, gold or silver ENIG finish) starting around $25/unit at 100-piece quantities, but there is no indication that this generic spec is what the Red Team Village badges actually used, so it is not recorded in the `tech` fields above.
