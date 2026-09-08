---
title: Brainy - The Brain badge
id: other-brainy-the-brain-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2020
makers:
- name: Danny Fernandez Raygoza
  url: https://github.com/Danny24
summary: A brain-shaped PCB pin badge with a smiling face and band-aid, driven by a PIC12LF1822 with 8 charlieplexed white LEDs (6 front, 2 back) that mimic neuron activity, powered by a CR2032 and made in 2020 to commemorate the maker's recovery from brain surgery.
functions: Button-controlled LED animation patterns simulating neuron activity, plus a low-power mode; an ICSP connector allows uploading custom animations/firmware.
look:
  colors: []
  shape: brain
  themes:
  - anime
  - pin
tech:
  mcu: PIC12LF1822
  leds:
    count: 8
    type: charlieplexed
    note: White SMD (0603) LEDs, 6 mounted on the front and 2 on the back, arranged to simulate neuron activity.
  display: none
  connectivity: []
  battery: CR2032
  sao_version: none
get_one:
  price: $24.45
  price_usd: 24.45
  quantity: ''
  availability: sold_out
  availability_note: Tindie listing showed out of stock as of Sep 27, 2023 (checked 2026-09-07).
  distribution:
  - purchase
  where: Sold directly by the maker (2BRobots, Mexico) via Tindie, to help cover ongoing medical expenses.
make_your_own:
  open_source: true
  hardware_url: https://github.com/Danny24/brainyBadge
  firmware_url: https://github.com/Danny24/brainyBadge
  gerbers_url: null
  bom_url: null
  eda_tool: Eagle
  license: null
  fab_url: https://www.pcbway.com/project/shareproject/Brainy___The_Brain_badge.html
  notes: Board outline traced from a vector graphic using Inkscape and svgtoeagle; Gerbers also shared as brain_badge_v1.zip on the PCBWay project page.
links:
- label: www.pcbway.com/project/shareproject/Brainy___The_Brain_badge.html
  url: https://www.pcbway.com/project/shareproject/Brainy___The_Brain_badge.html
  kind: fab
- label: github.com/Danny24/brainyBadge
  url: https://github.com/Danny24/brainyBadge
  kind: repo
  archived: https://web.archive.org/web/20260509103823/https://github.com/Danny24/brainyBadge
- label: hackaday.io/project/170993-brainy-the-pcb-badge
  url: https://hackaday.io/project/170993-brainy-the-pcb-badge
  kind: hackaday
- label: www.tindie.com/products/danny024/brainy-the-brain-badge
  url: https://www.tindie.com/products/danny024/brainy-the-brain-badge/
  kind: store
  archived: https://web.archive.org/web/20260503131451/https://www.tindie.com/products/danny024/brainy-the-brain-badge/
images:
- file: assets/images/badges/other/brainy-the-brain-badge/8c0660ad08.jpg
  source: https://www.tindie.com/products/danny024/brainy-the-brain-badge/
  credit: Danny Fernandez Raygoza / 2BRobots
  caption: Brainy the brain-shaped PCB badge
  archived: https://web.archive.org/web/20260503131451/https://www.tindie.com/products/danny024/brainy-the-brain-badge/
- file: assets/images/badges/other/brainy-the-brain-badge/0c91cee592.jpg
  source: https://hackaday.io/project/170993-brainy-the-pcb-badge
  credit: Danny Fernandez Raygoza
  caption: Brainy PCB layout / assembled badge on Hackaday project page
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://www.pcbway.com/project/shareproject/Brainy___The_Brain_badge.html
  title: Brainy - The Brain badge - Share Project - PCBWay
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/170993-brainy-the-pcb-badge
  title: Brainy - The PCB Badge - Hackaday.io
  accessed: '2026-09-07'
  note: Backstory (2020 brain surgery for a tectal plate tumor / hydrocephalus, VP shunt), design process (Eagle, Inkscape, svgtoeagle), assembly details, and gallery images.
- kind: url
  url: https://github.com/Danny24/brainyBadge
  title: Danny24/brainyBadge - GitHub
  accessed: '2026-09-07'
  note: Confirmed open-source Firmware/Hardware/Pictures repo structure and a LICENSE file; maker dedication to those who helped during recovery.
  archived: https://web.archive.org/web/20260509103823/https://github.com/Danny24/brainyBadge
- kind: url
  url: https://www.tindie.com/products/danny024/brainy-the-brain-badge/
  title: Brainy - The Brain Badge by danny024 on Tindie
  accessed: '2026-09-07'
  note: Price ($24.45), out-of-stock status (since Sep 27, 2023), seller location (2BRobots, Mexico), and a product photo.
  archived: https://web.archive.org/web/20260503131451/https://www.tindie.com/products/danny024/brainy-the-brain-badge/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: This is a personal/community project rather than a badge made for a specific convention, so it has no matching id in events.yml and stays under "other" (its maker made and sold it independently via Tindie/PCBWay/Hackaday, not tied to one con). Exact quantity made and a Gerbers direct link were not stated on any source checked; left empty. PCBWay page mentions an 11-vote community rating (9.27/10), not otherwise recorded in the schema.
last_modified_date: '2026-09-07'
---

Brainy is a brain-shaped PCB pin badge designed by Danny Fernandez Raygoza (2BRobots) in April 2020, shortly after surgery to treat hydrocephalus caused by a tumor on his tectal plate. Rather than risk removing the tumor, doctors implanted a ventriculoperitoneal shunt; Danny designed the badge as a thank-you to the people who helped him through recovery, and later began selling it to help cover ongoing medical costs. The board is shaped like a brain with a cartoon face and a band-aid, and its outline was traced from a vector drawing using Inkscape and the svgtoeagle tool before being laid out in Eagle CAD.

Electrically, the badge is built around a PIC12LF1822 microcontroller driving 8 charlieplexed white 0603 SMD LEDs (6 on the front, 2 on the back) in patterns meant to look like firing neurons. A push button cycles through animation modes and can put the badge into a low-power mode, and it runs off a single CR2032 coin cell. An onboard ICSP header lets owners reflash it with their own custom animations.

Danny published the hardware and firmware on GitHub and shared Gerbers through a PCBWay community project page, and sold assembled units through Tindie for $24.45; the Tindie listing has shown sold out since September 2023. The project also has a detailed write-up on Hackaday.io covering the medical backstory and build process.
