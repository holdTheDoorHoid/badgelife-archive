---
title: Car Hacking Village Badge (DC27)
id: dc27-car-hacking-village-badge-dc27
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Car Hacking Village
  url: https://www.carhackingvillage.com/
summary: 'A DEF CON 27 badge shaped like a small SUV: a laser-cut acrylic body over a rolling, drivable chassis rather than a wearable board.'
functions: 'Drives around under Bluetooth remote control: a DC motor turns the rear wheels through a worm gear, a hobby servo steers the front wheels via an acrylic lever, an OLED "windshield" acts as a display, and the spare tire on the back doubles as a rotary-encoder-plus-button input.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - security
tech:
  mcu: NXP
  leds:
    count: null
    type: RGB
    note: RGB LEDs mounted on PCB strips standing perpendicular to the main board.
  display: 0.96" OLED
  connectivity:
  - bluetooth
  battery: null
  sao_version: null
get_one:
  price: $95 (Car Badge)
  price_usd: 95
  quantity: '350'
  availability: sold_out
  distribution:
  - purchase
  - village
  where: Sold at the DEF CON 27 Car Hacking Village for $95 (a separate $30 "Traffic Light Badge" was also sold); hand-assembled in an approximately 4-hour build per unit to hit the con deadline.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/lanrat/CHVBadge_19
  eda_tool: null
links:
- label: hackaday.com/wp-content/uploads/2019/08/Car-Hacking-Village-Badge-DC27.jpg
  url: https://hackaday.com/wp-content/uploads/2019/08/Car-Hacking-Village-Badge-DC27.jpg
  kind: article
- label: 'Hackaday: The Badgies — Clever, Crazy, And Creative Ideas In Electronic Design'
  url: https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
  kind: article
  archived: https://web.archive.org/web/20260210064529/https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
- label: 'GitHub: lanrat/CHVBadge_19 (Gauge, SUV, and Stoplight SDKs)'
  url: https://github.com/lanrat/CHVBadge_19
  kind: repo
- label: Car Hacking Village — DEF CON 27 event page
  url: https://www.carhackingvillage.com/events/2019/8/2/def-con
  kind: website
images:
- file: assets/images/badges/dc27/car-hacking-village-badge-dc27/8d85cc688f.jpg
  source: https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
  credit: Car Hacking Village / Hackaday
  caption: The SUV-shaped Car Hacking Village badge, full view
  archived: https://web.archive.org/web/20260210064529/https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
- file: assets/images/badges/dc27/car-hacking-village-badge-dc27/d8c3ed9944.jpg
  source: https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/car-hacking-village-badge-dc27-processor/
  credit: Car Hacking Village / Hackaday
  caption: Close-up of the badge's main PCB with the NXP processor
contact: {}
notes:
- image URL only; 350-unit production run
status: released
sources:
- kind: url
  url: https://hackaday.com/wp-content/uploads/2019/08/Car-Hacking-Village-Badge-DC27.jpg
  title: Car Hacking Village Badge (DC27)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 27''.'
- kind: url
  url: https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
  title: 'The Badgies: Clever, Crazy, And Creative Ideas In Electronic Design'
  accessed: '2026-09-07'
  note: 'Main source for construction details: acrylic laser-cut body, DC motor + worm gear rear drive, servo steering, NXP processor, OLED windshield, spare-tire rotary encoder, Bluetooth control, 350-unit run, ~4 hours hand-assembly per badge.'
  archived: https://web.archive.org/web/20260210064529/https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
- kind: url
  url: https://github.com/lanrat/CHVBadge_19
  title: 'GitHub: lanrat/CHVBadge_19 - Stuff for the DEFCON 27 Car Hacking Village Badge'
  accessed: '2026-09-07'
  note: Archived repo with Gauge SDK, SUV SDK (Rev 1), and Stoplight SDK (Rev 1) folders; confirms multiple badge variants but page did not expose file-level chip/firmware detail.
- kind: url
  url: https://www.carhackingvillage.com/events/2019/8/2/def-con
  title: DEF CON — Car Hacking Village
  accessed: '2026-09-07'
  note: 'Confirms pricing: $95 for the Car Badge, $30 for a separate Traffic Light Badge, sold at the village.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This entry covers the SUV-shaped "Car Badge" ($95); a separate $30 "Traffic Light Badge" was sold alongside it at the same village and is not the same item. The GitHub org ttepatti/Car-Hacking-Village-Badges lists lanrat/CHVBadge_19 as the SDK source for this year, with three sub-projects (Gauge, SUV, Stoplight SDKs), suggesting the badge may have shipped in more than one form factor/role; could not confirm from primary sources whether firmware for the SUV variant specifically is included versus just the SDK scaffolding, so open_source is marked partial. Exact NXP part number, LED count, and battery type were not stated in any source read and are left empty rather than guessed.
last_modified_date: '2026-09-07'
---

The DEF CON 27 Car Hacking Village badge, sometimes called the "Car Badge," departed from the usual wearable PCB format: it's a small SUV-shaped vehicle you could drive around by Bluetooth. A laser-cut and laser-etched acrylic shell — chosen over injection molding because only 350 were made — houses a DC motor turning the rear wheels through a worm gear, and a small hobby servo steering the front wheels via an acrylic lever. An NXP processor on the main PCB handles control, paired with a separate battery-management board, RGB LEDs mounted on PCB strips standing perpendicular to the body, a 0.96" OLED "windshield," and a spare tire on the back that doubles as a rotary-encoder input with a button.

The Car Hacking Village sold it at DEF CON 27 for $95, alongside a separate, cheaper $30 "Traffic Light Badge." Each Car Badge reportedly took about four hours to hand-assemble, a real crunch to have 350 of them ready for the con. Hackaday's "Badgies" roundup singled it out as the craziest badge of the year.

Firmware/hardware scaffolding for that year's badges is archived on GitHub under `lanrat/CHVBadge_19`, split into Gauge, SUV, and Stoplight SDK folders — suggesting the village fielded more than one badge form that year, of which the SUV is the one this entry documents.
