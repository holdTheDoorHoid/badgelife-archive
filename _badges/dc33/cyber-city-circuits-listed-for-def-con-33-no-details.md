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
summary: A custom PCB fabrication and assembly shop that produced three badges for "RTV" (the Red Team Village) at DEF CON 33, according to a customer review on its own site; the badges themselves are not documented anywhere the maker has published.
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
  quantity: null
  availability: unknown
  distribution: []
  where: Made for RTV (Red Team Village) at DEF CON 33 per a customer review; how attendees received them is not documented.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- kind: website
  label: Cyber City Circuits
  url: https://cybercitycircuits.com
  archived: https://web.archive.org/web/20260606142506/https://cybercitycircuits.com/
- kind: store
  label: Cyber City Circuits event badge storefront (BadgesBadgesBadges.com)
  url: https://badgesbadgesbadges.com
  archived: https://web.archive.org/web/20260614134519/https://badgesbadgesbadges.com/
images: []
contact: {}
notes:
- Sheet listed only the maker name with no badge details; this was DEF CON 33's version of the same open item as the dc32 entry for this maker.
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
  note: Confirms CCC is a PCB design/assembly/rapid-prototyping shop ('Est. 2018 in Augusta, Ga', address in N Augusta, SC, 'Service Connected Disabled Veteran Owned Small Business') that offers 'Custom PCB Event Badges' via BadgesBadgesBadges.com; a customer review by Brian Sak states CCC 'produced three amazing badges for RTV at DEF CON 33'. Verified 2026-09-07.
  archived: https://web.archive.org/web/20260606142506/https://cybercitycircuits.com/
- kind: url
  url: https://badgesbadgesbadges.com
  title: BadgesBadgesBadges.com — Cyber City Circuits' event-badge storefront
  accessed: '2026-09-06'
  note: Repeats the same DEF CON 33 / RTV review; lists CCC's general customizable badge spec (up to 4 RGB LEDs, up to 12 patterns, onboard microprocessor, USB-C, single battery, gold or silver lead-free finish, $24.99 each at 100 pieces) but has no page specific to the DEF CON 33 / RTV badges themselves. Verified 2026-09-07.
  archived: https://web.archive.org/web/20260614134519/https://badgesbadgesbadges.com/
research:
  status: researched
  confidence: low
  last_checked: '2026-09-06'
  notes: '"Cyber City Circuits" (CCC) is a contract PCB design/assembly business, not a hobbyist badge line, which is why the sheet only had a maker name and no other details. The only corroborating source is a customer review by Brian Sak, shown on both cybercitycircuits.com and badgesbadgesbadges.com, saying CCC "produced three amazing badges for RTV at DEF CON 33." Fact-check 2026-09-07 re-read both pages and confirmed that quote and the company background. The expansion of "RTV" to Red Team Village is the archive''s reading (RTV is the usual abbreviation for that DEF CON village), not stated in the review, and no Red Team Village or press page confirming the badges was found, so the entry stays at `researched` / low confidence. "Three badges" most likely means three designs, not three units, so `get_one.quantity` is left null; nothing states how or whether the badges were handed out, so `distribution` is empty. No design, chip, LED, look or photo information exists for the actual RTV
    badges; the generic spec on BadgesBadgesBadges.com is not copied into `tech` because it is CCC''s standard product line, not confirmed to be what RTV received.'
last_modified_date: '2026-09-07'
---

Cyber City Circuits (CCC) is a PCB design, assembly, and rapid-prototyping company established in 2018 in Augusta, Georgia and now addressed in North Augusta, South Carolina, run as a service-connected disabled-veteran-owned small business. It does contract PCB work (assembly, reverse engineering, and recreating unsupported or obsolete hardware) and separately sells custom event badges through the storefront BadgesBadgesBadges.com. The community badge sheet listed the company as an expected DEF CON 33 (2025) maker with no further detail.

The only confirmation found of what they brought to DEF CON 33 is a customer review on CCC's own sites from Brian Sak, who wrote that CCC "produced three amazing badges for RTV at DEF CON 33." Read as the Red Team Village, that makes CCC the fabricator of three badges made for that village rather than a badge released under its own brand. No page describing those badges, their look, chip, LEDs, or how they reached village attendees was located from CCC, Red Team Village, or press coverage, so this entry records the commission without guessing at the hardware.

CCC's badge storefront advertises a standard customizable badge (up to four RGB LEDs with up to twelve selectable patterns, an onboard microprocessor, a USB-C connector, single included battery, gold or silver lead-free finish) at $24.99 per unit for 100 pieces, falling to $15.99 at 1,000. There is no indication that this generic spec is what the Red Team Village badges used, so it is not recorded in the `tech` fields above.
