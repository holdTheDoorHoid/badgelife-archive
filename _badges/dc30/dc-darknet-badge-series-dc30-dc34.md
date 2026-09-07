---
title: DC Darknet badge series (DC30-DC34)
id: dc30-dc-darknet-badge-series-dc30-dc34
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
series: DC Darknet / Darknet-NG
makers:
- name: Darknet (Gulo)
  url: https://darknet-ng.network
summary: A multi-year line of DIY educational badges made by the Darknet crew (led by "Gulo") for DEF CON, running at least from Darknet 11 at DC30 (2022) through Darknet-NG 14 at DC33/DC34. Early entries were "Printed Circuit Cardboard" kits teaching basic electronics; later entries became LoRa/Meshtastic mesh-networking badges.
functions: 'Varies by year. DC30''s "Darknet 11" is a three-level learn-to-solder-style kit (no soldering iron needed): Level 1 is a static LED circuit, Level 2 a transistor-based blinking (bistable multivibrator) circuit, and Level 3 a 555-timer 3D wire sculpture. Completing all three levels could earn a "Darknet 11 Black Badge" while supplies lasted. Later Darknet-NG badges (DC31 onward) are off-grid LoRa mesh-network nodes built around Meshtastic-compatible ESP32 boards.'
look:
  colors: []
  shape: null
  themes:
  - learn to solder
  - kit
  - radio
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: <=$100
  price_usd: 100.0
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Distributed at DEF CON to attendees who built/assembled the kit; later years' mainboards (e.g. LILYGO/Heltec LoRa32 ESP32 boards) were sourced by attendees themselves from third-party retailers ahead of the con.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/darknet-ng/Darknet-NG-13-Badge
  firmware_url: null
  eda_tool: null
links:
- label: github.com/thedarknet
  url: https://github.com/thedarknet
  kind: repo
- label: darknet-ng.network
  url: https://darknet-ng.network
  kind: website
- label: DCDarknet Badge Instructions for DEFCON 30 (Gulo Gulo Desu blog)
  url: https://gulogulodesu.com/blog/darknet/darknet11_badge.html
  kind: article
- label: github.com/darknet-ng
  url: https://github.com/darknet-ng
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
- 'This entry covers an entire multi-year series rather than one badge; the archive already has separate per-year stub entries for the same maker: dc30-they-still-have-not-said-anything, dc31-badge-information-is-up-and-available-on-their-site, dc32-another-badge-similar-to-past-years, dc32-secret-badge-no-info-at-all, dc33-darknet-ng-14-badge-levels-1-2-3, and dc34-darknet-ng-smao.'
- From what I have heard, it is supposed to cost <=$100
status: released
sources:
- kind: url
  url: https://github.com/thedarknet
  title: DC Darknet badge series (DC30-DC34)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''dc30''.'
- kind: url
  url: https://gulogulodesu.com/blog/darknet/darknet11_badge.html
  title: DCDarknet Badge Instructions for DEFCON 30 ('Darknet 11')
  accessed: '2026-09-07'
  note: 'Maker''s own writeup of the DC30 badge: three-level PCCB electronics-teaching kit, components, and the black-badge reward for completing all levels.'
- kind: url
  url: https://darknet-ng.network/darknet-ng-12-badge-for-def-con-31/
  title: Darknet-NG 12 Badge for DEF CON 31
  accessed: '2026-09-07'
  note: DC31 successor badge switched to a LILYGO LoRa32 ESP32 Meshtastic mesh-network design; confirms the series continues year to year under a new numbering (Darknet-NG 12, 13, 14...).
- kind: url
  url: https://github.com/darknet-ng
  title: darknet-ng GitHub organization
  accessed: '2026-09-07'
  note: Lists Darknet11-Badge (DC30), Darknet-NG-12-Badge (DC31) and Darknet-NG-13-Badge (DC32/33) repositories, confirming the yearly cadence and open-source hardware files.
- kind: sheet
  event: dc30
  row: 19
  updated: '2022-07-28'
- kind: url
  url: https://darknet-ng.network/
  title: Darknet-NG
  accessed: '2026-09-07'
  note: Darknet-NG's current site has no archive of a DEF CON 30 (2022) badge; earliest badge posts on their sitemap start at DEF CON 31 (2023).
  archived: https://web.archive.org/web/20260821062758/https://darknet-ng.network/
- kind: url
  url: https://darknet-ng.network/wp-sitemap-posts-post-1.xml
  title: Darknet-NG post sitemap
  accessed: '2026-09-07'
  note: Full list of the group's blog posts contains no DEF CON 30 / 2022 badge post.
- kind: url
  url: http://web.archive.org/web/20220522080429/https://darknet-ng.network/
  title: darknet-ng.network (Wayback Machine, May 2022)
  accessed: '2026-09-07'
  note: Only Wayback snapshot near DEF CON 30 shows the site 'under maintenance' with no badge content; no other 2022 snapshots exist in the CDX index.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This entry is a series overview, not a single badge, so per-badge fields (tech.mcu, leds, price, quantity) are left empty because they differ every year: DC30''s "Darknet 11" is a passive paper/cardboard electronics kit (LEDs, resistors, a 555 timer, no MCU); DC31''s "Darknet-NG 12" and later years are ESP32-based LoRa/Meshtastic mesh badges (e.g. LILYGO LoRa32, Heltec WiFi LoRa 32 V3, Seeed Xiao ESP32-S3). The archive already has separate stub entries per year for this same maker (see notes above) that duplicate this one; the closest single match is dc30-they-still-have-not-said-anything, filed under the same event. Merged with duplicate entry ''They still have not said anything...'' (dc30-they-still-have-not-said-anything).'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc30/they-still-have-not-said-anything/
---

The "Darknet" badge line is a long-running DEF CON tradition run by a crew fronted by someone using the handle Gulo (of gulogulodesu.com), with roots going back to at least Darknet 8 for DC26/DC27. For DEF CON 30 (2022) the team released "Darknet 11," a deliberately low-cost "Printed Circuit Cardboard" (PCCB) kit built to teach basic electronics rather than to be soldered: builders assembled their own circuit on a paper/cardstock badge using supplied LEDs, resistors, capacitors, 2N2222A transistors, and a 555 timer IC, progressing through three levels from a simple lit LED to a blinking bistable-multivibrator circuit to a 555-timer 3D wire sculpture, all powered by three AAA batteries. Finishing all three levels could earn a limited "Darknet 11 Black Badge."

Starting with DEF CON 31, the project rebranded as "Darknet-NG" and pivoted hardware entirely: the "Darknet-NG 12" badge and its successors ("13" for DC32/33, "14" for DC33/34, described as "Signal in the Noise") are built around commodity ESP32 LoRa boards (LILYGO LoRa32, Heltec WiFi LoRa 32 V3, Seeed Xiao ESP32-S3) running Meshtastic, letting attendees build an off-grid mesh network out of their badges rather than a soldering-practice circuit. Designs and firmware for these later badges are open-sourced on GitHub under the darknet-ng organization, with 3D-printable cases shared on Thingiverse and Printables.

Because this archive entry was created from a sheet listing as one umbrella item spanning DC30 through DC34, and the archive already carries separate per-year stub entries for the same maker (DC30, DC31, two for DC32, DC33, and DC34), the material here is best read as background context for those; no further per-year detail was pulled into this entry to avoid guessing at facts specific to a single year.

## Notes merged from the duplicate entry "They still have not said anything..."

The community badge sheet for DEF CON 30 (2022) carries this row as commentary rather than a confirmed listing: someone had "heard word" that Darknet — the long-running DEF CON contest group now known as Darknet-NG — was working on a badge, guessed at a price of $100 or less, and noted that as of the sheet's last update the group still had not said anything official.

No corroborating source could be found. Darknet-NG's own website only documents badges going back to DEF CON 31 (2023), and no archived snapshot, press coverage, or social post from mid-2022 mentions a badge from the group. It is not known whether this badge was ever finished, released quietly without documentation, or dropped entirely; this entry stands as a record of the rumor rather than a confirmed item.
