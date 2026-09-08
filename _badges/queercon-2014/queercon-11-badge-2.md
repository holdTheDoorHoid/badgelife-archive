---
title: Queercon 11 Badge
id: queercon-2014-queercon-11-badge-2
layout: badge
parent: Queercon 11 (2014)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: queercon-2014
year: 2014
makers:
- name: Queercon
summary: 'A social-networking party badge for Queercon 11 (DEF CON 22, 2014): an MSP430-based badge that swaps identities with other badges over IR and tracks proximity over an RF69 radio link.'
functions: 'Badge-to-badge "badginal intercourse": holding two badges near each other exchanges each holder''s identifier over IR and logs the pairing. An onboard HopeRF RF69 radio senses nearby badges over the air, and rainbow LEDs beside the LED display light up as a wearer accumulates points. Base-station readers at the party could show a badge''s pairing history and attendance.'
look:
  colors: []
  shape: null
  themes:
  - lgbtq
  - party
  - wearable
tech:
  mcu: MSP430F5308
  leds:
    count: null
    type: WS2812
    note: Rainbow LEDs flanking the display, driven by a WS2812 library in the released firmware.
  display: LED display
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
  where: Sold/distributed at Queercon 11, the LGBTQ party held alongside DEF CON 22 in 2014, as entry to the Queercon party.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Queercon/QC11-Badge
  firmware_url: https://github.com/Queercon/QC11-Badge
  eda_tool: null
links:
- label: blinkylights.ninja/blinky-lights/queercon-12-2015
  url: https://blinkylights.ninja/blinky-lights/queercon-12-2015/
  kind: website
- label: github.com/Queercon/QC11-Badge
  url: https://github.com/Queercon/QC11-Badge
  kind: repo
- label: hackaday.com/2014/09/15/the-queercon-11-badge
  url: https://hackaday.com/2014/09/15/the-queercon-11-badge/
  kind: article
- label: forum.defcon.org/node/14911
  url: https://forum.defcon.org/node/14911
  kind: doc
images:
  - file: assets/images/badges/queercon-2014/queercon-11-badge-2/f8ddf57b05.jpg
    source: "https://hackaday.com/2014/09/15/the-queercon-11-badge/"
    credit: "Queercon / Hackaday"
    caption: "Queercon 11 badge, front"
  - file: assets/images/badges/queercon-2014/queercon-11-badge-2/9996d36cb1.jpg
    source: "https://hackaday.com/2014/09/15/the-queercon-11-badge/"
    credit: "Queercon / Hackaday"
    caption: "Queercon 11 badge reader/base station"
contact: {}
notes:
- MSP430-based badge-to-badge "Tamagotchi-style" party badge with IR link and HopeRF RF69 radio for Queercon 11 at DEF CON 23, sold for entry to the Queercon party. Found by the event-year sweep, task dc23-all.
- 'Correction: sources (Hackaday, the GitHub repo, and the DEF CON forums) place this badge at Queercon 11, which ran alongside DEF CON 22 in 2014, not DEF CON 23 (2015). The sweep''s original wording "Queercon 11 Badge" was correct, but the event/year it filed under was not; event corrected from queercon-2015 to queercon-2014. This appears to duplicate the existing entry queercon-2014-queercon-11-badge for the same badge.'
status: listed
sources:
- kind: url
  url: https://blinkylights.ninja/blinky-lights/queercon-12-2015/
  title: Queercon 11 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc23-all); event read as ''queercon-2015''.'
- kind: url
  url: https://github.com/Queercon/QC11-Badge
  title: 'GitHub - Queercon/QC11-Badge'
  accessed: '2026-09-08'
  note: 'Maker''s own repo: confirms MSP430F5308 MCU, WS2812 LEDs, IR and radio modules, open-source hardware (CC BY-SA 4.0) and firmware (BSD 3-clause).'
- kind: url
  url: https://hackaday.com/2014/09/15/the-queercon-11-badge/
  title: 'The Queercon 11 Badge - Hackaday'
  accessed: '2026-09-08'
  note: 'Confirms this badge was for Queercon 11 / DEF CON 22 (2014), not 2015; describes IR pairing, RF69 proximity radio, rainbow LEDs, and base-station readers. Source of both saved images.'
- kind: url
  url: https://forum.defcon.org/node/14911
  title: 'Queercon Badges - DEF CON Forums'
  accessed: '2026-09-08'
  note: 'Queercon''s own forum post describing the Queercon 11 badge as a follow-up to the prior year''s "GayDar" badge.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Event corrected from queercon-2015 to queercon-2014 (see notes above); this badge is Queercon 11, made for DEF CON 22 in 2014, confirmed by the maker''s GitHub repo, Hackaday, and the DEF CON forums. Likely a duplicate of queercon-2014-queercon-11-badge. Price, quantity made, LED count, and colors/shape were not stated in any source found and are left empty.'
last_modified_date: '2026-09-08'
redirect_from:
- /badges/queercon-2015/queercon-11-badge/
---

The Queercon 11 badge was the party badge for Queercon, the LGBTQ event held alongside DEF CON 22 in Las Vegas in 2014. Built around an MSP430F5308 microcontroller, it followed up the prior year's "GayDar" badge with a similar social-networking gimmick: holding two badges close together exchanged each wearer's identifier over an IR link, logging the pairing (jokingly called "badginal intercourse" by the community). A HopeRF RF69 radio let badges sense other badges nearby over the air, and rainbow LEDs beside the badge's LED display lit up as a wearer racked up points for socializing. Base-station reader terminals at the party could show a badge's pairing history and attendance record.

Queercon released the badge's hardware and firmware as open source on GitHub (`Queercon/QC11-Badge`): the hardware design is licensed CC BY-SA 4.0, with LED animations credited to Jonathan Nelson and George Louthan, and the firmware under a BSD 3-clause license.

This entry was filed under Queercon 12 (2015) by an automated sweep, but the maker's own repository, Hackaday's coverage, and the DEF CON forums all place the badge at Queercon 11 / DEF CON 22 in 2014. It very likely duplicates the archive's existing `queercon-2014-queercon-11-badge` entry for the same badge.

## Make your own

Full hardware and firmware sources are published at [github.com/Queercon/QC11-Badge](https://github.com/Queercon/QC11-Badge), including the MSP430 firmware, a WS2812 LED driver, IR and radio (`radio.c`/`radio.h`) modules, and font/animation assets, along with build documentation in the repo's `/doc` folder.
