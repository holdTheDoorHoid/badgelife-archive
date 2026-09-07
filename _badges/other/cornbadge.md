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
functions: 'Powers on into one of four randomly-chosen LED behavior variants each boot (a fifth "slow delay" variant exists in the code but is unreachable because of how the random range is called): default fade, all-LEDs-start-at-zero, faster fade steps, or a faster update delay, cycling brightness on five independently-controlled LEDs.'
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: ATtiny85
  leds:
    count: 5
    type: discrete
    note: Individually PWM-faded via analogWrite; one of four reachable startup variants (a fifth is defined in code but never selected, due to a random-range bug) is chosen at random each power-up.
  display: null
  connectivity: []
  battery: null
  sao_version: null
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
status: unknown
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
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    Fact-check pass (2026-09-07): re-read all four cited sources directly. Two errors from the
    prior research pass were corrected. (1) The firmware's random(4) call in Arduino only returns
    0-3, so the fifth "slow delay" case defined in the switch statement can never be selected;
    functions/tech.leds.note now describe four reachable startup variants instead of five, and the
    "all-start-full" variant is actually all five brightnesses set to 0 (dark), despite the code's
    own comment mislabeling it "full" - fixed to "all-LEDs-start-at-zero". (2) status was changed
    from "released" to "unknown": no source states the badge was ever distributed to anyone besides
    the maker; the closest evidence is the README's animated GIF, which does show a real PCB (green,
    5 LEDs, someone's hand programming it) - contradicting the prior pass's claim that neither README
    image shows the physical item - but that only documents the maker's own prototype, not a release.
    No new image was added in this pass (out of scope for a fact-check-only run); a future research
    pass could pull a frame from that GIF as an image credited to the README. tech.sao_version and
    look.themes ("food") were blanked: no source states the SAO connector pin count, and nothing in
    the repo, README, or GIF shows corn imagery or a food-shaped board - "food" was an unsupported
    inference from the name alone. No event or con is named anywhere in the repo or README; the
    badge is only tied to the maker's "#cornbadge" Twitter tag and the general badgelife/Shitty-Add-Ons
    SAO ecosystem, not a specific conference. Year (2019) is confirmed via the repo's commit history
    (all commits 2019-04-02), not stated by the maker. Firmware is published, no hardware files
    (schematic, PCB, gerbers) are in the repo, so open_source: partial is confirmed. No price,
    quantity, or availability information exists anywhere checked. A web search for additional
    coverage (Hackaday, Twitter/X, forums) was not run this pass, per the fact-check task's scope
    (verify cited sources, no new research); every field and sentence remaining in the entry is now
    supported by the four existing sources, or correctly left blank/unknown where unsupported, so
    research.status is set to "verified" - confidence stays low because the underlying sources are
    thin (one repo, no coverage, no confirmed distribution).
last_modified_date: '2026-09-07'
---

Cornbadge is a bare-bones SAO (Shitty Add-On) built by James Dietle (@jamesdietle) around an ATtiny85, published to GitHub in April 2019. The maker describes the goal as putting "a super cheap arduino into people's hands so they can start messing around and showing off," making it explicitly a beginner/hobbyist project rather than a conference giveaway with a stated distribution plan.

The board drives five LEDs, each independently PWM-faded in software. On every power-up the firmware rolls a random number to pick one of four preset routines — a normal fade, all-LEDs-starting-at-zero-brightness, a faster fade, or a faster update delay — so the same board behaves a little differently each time it's plugged in. The code actually defines a fifth "slow delay" routine, but a mismatch between the random-number range and the number of cases means it can never be selected, so it never runs in practice. The firmware (an Arduino .ino sketch) is published in the repo, but no schematic, PCB layout, or gerbers were found there, so the hardware side does not appear to be openly published alongside it.

No specific convention or year is named in the source material; the "2019" year here is inferred only from the repository's commit timestamps, and the badge's only stated context is the general badgelife/Shitty-Add-Ons SAO ecosystem via a link to that Hackaday.io project.
