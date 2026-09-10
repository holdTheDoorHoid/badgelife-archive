---
title: Kiwicon Intro to Badge Hacking (training badge/kit)
id: kiwicon-2018-kiwicon-intro-to-badge-hacking-training-badge-kit
layout: badge
parent: Kiwicon 2018
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: kiwicon-2018
year: 2018
makers:
- name: kiwicon-badge (GitHub org; course instructor writes in first person, not named in the README)
  url: https://github.com/kiwicon-badge
summary: 'A learn-to-solder training kit built for the "Intro to Badge Hacking" course at Kiwicon 2038AD (2018): a round green PCB with a 5x4 charlieplexed LED matrix, built up through six hands-on labs.'
functions: 'Alternately/individually flashes 20 green LEDs in a charlieplexed 5x4 matrix, driven by a hand-written ATtiny13A program the student loads themselves via USBAsp/ISP; the course also has students breadboard a simple 2-LED microcontroller circuit before soldering the final badge.'
look:
  colors:
  - green
  shape: circle
  themes:
  - learn to solder
  - kit
tech:
  mcu: ATtiny13A
  leds:
    count: 20
    type: charlieplexed
    note: Green 5mm through-hole LEDs arranged in a 5x4 matrix, driven from only 5 microcontroller pins via charlieplexing.
  display: none
  connectivity:
  - none
  battery: CR2025 or CR2032 coin cell
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Handed out to attendees of the "Intro to Badge Hacking" training session at Kiwicon 2038AD (Nov 16-17, 2018); not sold separately.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/kiwicon-badge/badge
  firmware_url: https://github.com/kiwicon-badge/badge/tree/master/lab-06
  eda_tool: null
links:
- label: github.com/kiwicon-badge/badge
  url: https://github.com/kiwicon-badge/badge
  kind: repo
- label: Kiwicon - Intro to Badge Hacking (training page)
  url: https://www.kiwicon.org/the-con/training/intro-to-badge-hacking/
  kind: website
images:
- file: assets/images/badges/kiwicon-2018/kiwicon-intro-to-badge-hacking-training-badge-kit/ecb57523a7.jpg
  source: "https://github.com/kiwicon-badge/badge"
  credit: "kiwicon-badge (course instructor)"
  caption: "Badge PCB design with 20-LED charlieplexed matrix"
- file: assets/images/badges/kiwicon-2018/kiwicon-intro-to-badge-hacking-training-badge-kit/a1a1084600.png
  source: "https://github.com/kiwicon-badge/badge"
  credit: "kiwicon-badge (course instructor)"
  caption: "Assembled training badge, final step"
contact: {}
notes:
- Sweep's title used the sheet's generic wording; the repo/README does not give the kit a distinct product name beyond describing it as the badge for the "Intro to Badge Hacking" course, so the existing title is kept.
- The repo's own text calls the event "Kiwicon 2038" (Kiwicon's stylized name for 2018), which matches _data/events.yml's kiwicon-2018 (dates: Nov 16-17, 2018, "Kiwicon 2038AD"); no event correction needed.
- The instructor is not named in the README (writes in first person); the GitHub repo's sole non-org contributor is "JeromeVanRooijen", but this is not confirmed as the instructor/designer by any maker statement, so makers.name records the org handle rather than guessing an identity.
status: released
sources:
- kind: url
  url: https://github.com/kiwicon-badge/badge
  title: Kiwicon Intro to Badge Hacking (training badge/kit)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://github.com/kiwicon-badge/badge
  title: 'kiwicon-badge/badge: README, labs, schematics, port mapping'
  accessed: '2026-09-10'
  note: 'Primary source: confirms event (Kiwicon 2038AD / 2018), ATtiny13A MCU, 20 green charlieplexed LEDs, CR2025/32 coin cell, USBAsp programming, six-lab course structure, open hardware/firmware.'
- kind: url
  url: https://www.kiwicon.org/the-con/training/intro-to-badge-hacking/
  title: Kiwicon - Intro to Badge Hacking
  accessed: '2026-09-10'
  note: Linked from the README as the course's official training page.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Core technical facts (MCU, LEDs, battery, programming method, course structure) are confirmed straight from the maker''s own repo, so those are solid. Left unresolved: the instructor/designer''s name (not stated in the README), whether the training badge was ever sold or given beyond the workshop, quantity made, and whether the design files are licensed for reuse (no LICENSE file found in a quick repo skim). Kiwicon''s own training page (kiwicon.org) was linked but not independently confirmed to still describe this exact course; treated as supporting, not primary.'
last_modified_date: '2026-09-10'
---

The "Intro to Badge Hacking" badge is the take-home kit for Kiwicon's hands-on soldering and electronics course, run at Kiwicon 2038AD (the con's playful name for its 2018 edition, held Nov 16-17 in Wellington). Students work through six labs — circuits, microcontrollers, programming, soldering, badge assembly, and finally reprogramming their own badge — ending with a round green PCB carrying 20 green LEDs. The LEDs are wired in a 5x4 charlieplexed matrix so that an ATtiny13A, using only 5 of its I/O pins, can address each one individually; power comes from a CR2025/CR2032 coin cell on the back.

The course README and code are published on GitHub under the `kiwicon-badge` organization, with the schematic, PCB layout, per-lab instructions, and the ATtiny13A firmware (loaded via USBAsp/ISP) all included, making the whole kit reproducible by anyone. The instructor who wrote and ran the course is not named in the README itself; the repository's only outside contributor is credited as JeromeVanRooijen, though that has not been confirmed as the designer's identity by any maker statement.

As a workshop kit rather than a commercial product, it was distributed to attendees of that specific training session rather than sold, and no information on production quantity or continued availability was found.
