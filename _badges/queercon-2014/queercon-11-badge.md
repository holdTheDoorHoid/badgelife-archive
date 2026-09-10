---
title: Queercon 11 Badge
id: queercon-2014-queercon-11-badge
layout: badge
parent: Queercon 11 (2014)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: queercon-2014
year: 2014
makers:
- name: Queercon
  url: https://queercon.org
summary: A floppy-disk-shaped MSP430 social badge for Queercon 11 (co-located with DEF CON 22) that uses IR peer exchange and an ISM-band radio to track proximity between attendees and award points at base stations.
functions: Exchanges identifiers with nearby badges over IR; when two badges pair, both light up and display the other wearer's name. A HopeRF RF69 radio counts nearby QC11 badges for a running proximity score. Base stations placed around the event read badges over IR/radio and award attendance points; the badge won 1st place in the DEF CON 22 badge contest.
look:
  colors: []
  shape: floppy disk
  themes:
  - retro computer
tech:
  mcu: MSP430F5308
  leds:
    count: null
    type: WS2812
    note: WS2812 addressable LED grid used for the on-badge display
  display: LED matrix
  connectivity:
  - ir
  - sub-ghz
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Distributed to Queercon 11 attendees at DEF CON 22 (2014).
make_your_own:
  open_source: true
  hardware_url: https://github.com/duplico/qc11
  firmware_url: https://github.com/duplico/qc11
  eda_tool: null
links:
- label: hackaday.com/2014/09/15/the-queercon-11-badge
  url: https://hackaday.com/2014/09/15/the-queercon-11-badge/
  kind: article
- label: github.com/duplico/qc11
  url: https://github.com/duplico/qc11
  kind: repo
- label: github.com/Queercon/QC11-Badge
  url: https://github.com/Queercon/QC11-Badge
  kind: repo
- label: blinkylights.ninja/blinky-lights/queercon-12-2015
  url: https://blinkylights.ninja/blinky-lights/queercon-12-2015/
  kind: website
- label: forum.defcon.org/node/14911
  url: https://forum.defcon.org/node/14911
  kind: doc
images:
- file: assets/images/badges/queercon-2014/queercon-11-badge/f8ddf57b05.jpg
  source: https://hackaday.com/2014/09/15/the-queercon-11-badge/
  credit: Hackaday
  caption: The Queercon 11 floppy-disk-shaped badge
- file: assets/images/badges/queercon-2014/queercon-11-badge/9996d36cb1.jpg
  source: https://hackaday.com/2014/09/15/the-queercon-11-badge/
  credit: Hackaday
  caption: The Queercon 11 base station reader used to award points
- file: assets/images/badges/queercon-2014/queercon-11-badge/f8ddf57b05.jpg
  source: https://hackaday.com/2014/09/15/the-queercon-11-badge/
  credit: Queercon / Hackaday
  caption: Queercon 11 badge, front
- file: assets/images/badges/queercon-2014/queercon-11-badge/9996d36cb1.jpg
  source: https://hackaday.com/2014/09/15/the-queercon-11-badge/
  credit: Queercon / Hackaday
  caption: Queercon 11 badge reader/base station
contact: {}
notes:
- 'Sweep task dc22-all originally logged this as: "Floppy-disk-shaped MSP430 social badge for Queercon 11, co-located with DEF CON 22, using IR peer exchange and a HopeRF RF69 radio to track proximity and award points at base stations; won 1st place in the DC22 badge contest." Confirmed by Hackaday coverage and the maker''s own GitHub repos (duplico/qc11, Queercon/QC11-Badge).'
- MSP430-based badge-to-badge "Tamagotchi-style" party badge with IR link and HopeRF RF69 radio for Queercon 11 at DEF CON 23, sold for entry to the Queercon party. Found by the event-year sweep, task dc23-all.
- 'Correction: sources (Hackaday, the GitHub repo, and the DEF CON forums) place this badge at Queercon 11, which ran alongside DEF CON 22 in 2014, not DEF CON 23 (2015). The sweep''s original wording "Queercon 11 Badge" was correct, but the event/year it filed under was not; event corrected from queercon-2015 to queercon-2014. This appears to duplicate the existing entry queercon-2014-queercon-11-badge for the same badge.'
status: released
sources:
- kind: url
  url: https://hackaday.com/2014/09/15/the-queercon-11-badge/
  title: Queercon 11 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc22-all); event read as ''queercon-2014''.'
- kind: url
  url: https://github.com/duplico/qc11
  title: 'duplico/qc11: Queercon 11 electronic badge'
  accessed: '2026-09-08'
  note: Maker's own repo; confirms MSP430F5308, WS2812 LED grid, IR pairing, ISM radio neighbor tracking, and CC BY-SA 4.0 / BSD 3-clause open-source licensing.
- kind: url
  url: https://github.com/Queercon/QC11-Badge
  title: Queercon/QC11-Badge
  accessed: '2026-09-08'
  note: Queercon org's own copy of the hardware/firmware repo referenced by the Hackaday article as the source of the released design files.
- kind: url
  url: https://blinkylights.ninja/blinky-lights/queercon-12-2015/
  title: Queercon 11 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc23-all); event read as ''queercon-2015''.'
- kind: url
  url: https://forum.defcon.org/node/14911
  title: Queercon Badges - DEF CON Forums
  accessed: '2026-09-08'
  note: Queercon's own forum post describing the Queercon 11 badge as a follow-up to the prior year's "GayDar" badge.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Price, quantity made, and exact LED count were not stated in any source found and are left empty. Note: a separate entry, queercon-2015-queercon-11-badge, exists with the identical title "Queercon 11 Badge" but filed under the queercon-2015 event folder — Queercon 11 was the 2014 event (co-located with DEF CON 22), so that other entry appears to be a duplicate misfiled by year; not touched here per task scope. Merged with duplicate entry ''Queercon 11 Badge'' (queercon-2014-queercon-11-badge-2).'
last_modified_date: '2026-09-08'
redirect_from:
- /badges/queercon-2014/queercon-11-badge-2/
---

The Queercon 11 badge, worn by attendees of the 2014 Queercon party co-located with DEF CON 22, took the form of a 3.5" floppy disk and ran on an MSP430F5308 microcontroller. It used an infrared link to exchange identifiers with nearby badges — when two badges paired, each lit up its WS2812 LED grid and displayed the other wearer's name — while a HopeRF RF69 ISM-band radio kept a running count of other QC11 badges nearby. Base stations set up around the venue collected this pairing and proximity data to award attendees points, and the badge went on to win first place in the DEF CON 22 badge contest.

Queercon released the hardware design and firmware source for the badge on GitHub (as `Queercon/QC11-Badge` and, from designer George Louthan's own account, `duplico/qc11`), with the hardware under CC BY-SA 4.0 and the software largely under a BSD 3-clause license.

## Make your own

The full KiCad-era hardware files and MSP430 firmware source are published at [github.com/duplico/qc11](https://github.com/duplico/qc11) and [github.com/Queercon/QC11-Badge](https://github.com/Queercon/QC11-Badge); see each repo's README for the build and flashing steps.

## Notes merged from the duplicate entry "Queercon 11 Badge"

The Queercon 11 badge was the party badge for Queercon, the LGBTQ event held alongside DEF CON 22 in Las Vegas in 2014. Built around an MSP430F5308 microcontroller, it followed up the prior year's "GayDar" badge with a similar social-networking gimmick: holding two badges close together exchanged each wearer's identifier over an IR link, logging the pairing (jokingly called "badginal intercourse" by the community). A HopeRF RF69 radio let badges sense other badges nearby over the air, and rainbow LEDs beside the badge's LED display lit up as a wearer racked up points for socializing. Base-station reader terminals at the party could show a badge's pairing history and attendance record.

Queercon released the badge's hardware and firmware as open source on GitHub (`Queercon/QC11-Badge`): the hardware design is licensed CC BY-SA 4.0, with LED animations credited to Jonathan Nelson and George Louthan, and the firmware under a BSD 3-clause license.

This entry was filed under Queercon 12 (2015) by an automated sweep, but the maker's own repository, Hackaday's coverage, and the DEF CON forums all place the badge at Queercon 11 / DEF CON 22 in 2014. It very likely duplicates the archive's existing `queercon-2014-queercon-11-badge` entry for the same badge.

## Make your own

Full hardware and firmware sources are published at [github.com/Queercon/QC11-Badge](https://github.com/Queercon/QC11-Badge), including the MSP430 firmware, a WS2812 LED driver, IR and radio (`radio.c`/`radio.h`) modules, and font/animation assets, along with build documentation in the repo's `/doc` folder.
