---
title: Cornbadge
id: other-cornbadge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2019
makers:
- name: jamesdietle
  url: https://github.com/jamesdietle
summary: A minimal ATtiny85-based SAO with five fading LEDs, built to be a super cheap, beginner-friendly badgelife add-on.
functions: 'Powers on into one of five randomly-chosen LED animation routines each boot: normal fade, all-start-full, fast fade, quick delay, or slow delay, cycling brightness on five independently-controlled LEDs.'
look:
  colors: []
  shape: null
  themes:
  - food
tech:
  mcu: ATtiny85
  leds:
    count: 5
    type: discrete
    note: Individually PWM-faded via analogWrite; brightness/fade pattern chosen at random on each power-up.
  display: null
  connectivity: []
  battery: null
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/jamesdietle/Cornbadge/blob/master/Cornbadge.ino
  eda_tool: null
links:
- label: github.com/jamesdietle/Cornbadge
  url: https://github.com/jamesdietle/Cornbadge
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://github.com/jamesdietle/Cornbadge
  title: Cornbadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''unknown (not stated in repo)''.'
- kind: url
  url: https://raw.githubusercontent.com/jamesdietle/Cornbadge/master/README.md
  title: Cornbadge README
  accessed: '2026-09-07'
  note: 'States it uses the ATtiny85 and the "Shitty Addon protocol from #Badgelife" (linking to the Shitty Add-Ons Hackaday.io project); no event/con named.'
- kind: url
  url: https://raw.githubusercontent.com/jamesdietle/Cornbadge/master/Cornbadge.ino
  title: Cornbadge.ino
  accessed: '2026-09-07'
  note: Firmware source showing 5 independently-faded LEDs on pins 0-4 and a random startup routine selecting one of five fade patterns.
- kind: url
  url: https://api.github.com/repos/jamesdietle/Cornbadge/commits
  title: Cornbadge commit history
  accessed: '2026-09-07'
  note: All commits dated 2019-04-02, used to estimate the badge's year.
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    No event or con is named anywhere in the repo or README; the badge is only tied to the maker's
    "#cornbadge" Twitter tag and the general badgelife/Shitty-Add-Ons SAO ecosystem, not a specific
    conference. Year (2019) is inferred from the repo's commit history, not stated by the maker.
    Firmware (an Arduino .ino sketch) is published, but no hardware files (schematic, PCB, gerbers)
    were found in the repo, so open_source is marked "partial" rather than "yes". No price,
    quantity, or availability information was found anywhere. The two images in the README (an
    animated Giphy GIF and a JPG pinout/programming diagram) do not show a photo of the physical
    badge itself, so no images were saved per the archive's image rules. A web search for
    additional coverage (Hackaday, Twitter/X, forums) could not be run this session (search
    budget exhausted); only the GitHub repo and its raw files were checked.
last_modified_date: '2026-09-07'
---

Cornbadge is a bare-bones SAO (Shitty Add-On) built by James Dietle (@jamesdietle) around an ATtiny85, published to GitHub in April 2019. The maker describes the goal as putting "a super cheap arduino into people's hands so they can start messing around and showing off," making it explicitly a beginner/hobbyist project rather than a conference giveaway with a stated distribution plan.

The board drives five LEDs, each independently PWM-faded in software. On every power-up the firmware picks one of five preset routines at random — a normal fade, all-LEDs-starting-lit, a faster fade, a quick delay, or a slow delay — so the same board behaves a little differently each time it's plugged in. The firmware (an Arduino .ino sketch) is published in the repo, but no schematic, PCB layout, or gerbers were found there, so the hardware side does not appear to be openly published alongside it.

No specific convention or year is named in the source material; the "2019" year here is inferred only from the repository's commit timestamps, and the badge's only stated context is the general badgelife/Shitty-Add-Ons SAO ecosystem via a link to that Hackaday.io project.
