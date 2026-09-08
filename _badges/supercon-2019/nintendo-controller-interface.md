---
title: Nintendo Controller Interface
id: supercon-2019-nintendo-controller-interface
layout: badge
parent: Supercon 2019
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2019
year: 2019
makers:
- name: Ben Hencke
  url: https://twitter.com/im889
summary: 'A cartridge that lets a Nintendo game controller plug into the 2019 Supercon FPGA badge, enabling multiplayer gaming on the badge.'
functions: 'Adapts a Nintendo game controller as an input device for the badge, for multiplayer games.'
look:
  colors: []
  shape: null
  themes:
  - console
  - retro computer
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
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2019/11/29/a-fantastic-frontier-of-fpga-flexibility-found-in-the-2019-supercon-badge
  url: https://hackaday.com/2019/11/29/a-fantastic-frontier-of-fpga-flexibility-found-in-the-2019-supercon-badge/
  kind: article
images:
- file: assets/images/badges/supercon-2019/nintendo-controller-interface/c071df8258.jpg
  source: "https://hackaday.com/2019/11/29/a-fantastic-frontier-of-fpga-flexibility-found-in-the-2019-supercon-badge/"
  credit: "Hackaday"
  caption: "Ben Hencke's Nintendo controller interface cartridge for the 2019 Supercon FPGA badge"
contact: {}
notes:
- A hack enabling a Nintendo game controller to interface with the 2019 Supercon badge for multiplayer gaming. Found by the event-year sweep, task supercon-2019.
status: released
sources:
- kind: url
  url: https://hackaday.com/2019/11/29/a-fantastic-frontier-of-fpga-flexibility-found-in-the-2019-supercon-badge/
  title: Nintendo Controller Interface
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2019); event read as ''supercon-2019''.'
- kind: url
  url: https://hackaday.com/2019/11/29/a-fantastic-frontier-of-fpga-flexibility-found-in-the-2019-supercon-badge/
  title: A Fantastic Frontier Of FPGA Flexibility Found In The 2019 Supercon Badge
  accessed: '2026-09-08'
  note: 'Hackaday''s roundup of Supercon 2019 badge-hacking-village projects; names Ben Hencke as the maker of a Nintendo-controller interface cartridge for multiplayer gaming, and includes a photo of it (Badge-hacking-2019-03-Nintendo-controllers.jpg).'
research:
  status: verified
  confidence: low
  last_checked: '2026-09-08'
  notes: 'Confirmed real (photographed in the Hackaday roundup, credited to Ben Hencke), but this was a one-off badge-hacking-village project built during the con, not a distributed product. No dedicated project page, repo, chip/hardware detail, price, quantity, or design files were found on Hackaday.io (checked Ben Hencke''s profile at hackaday.io/projects/hacker/142050) or GitHub (checked github.com/simap). Set status to released since it existed and worked at the event; get_one and tech fields left empty for lack of sourcing. Fact-check pass (2026-09-08): re-fetched the Hackaday article and confirmed every remaining claim word-for-word: it names Ben Hencke, describes him "interfacing with Nintendo controllers for multiplayer gaming," and its "Custom Cartridges" section explicitly calls these badge add-ons cartridges; the maker Twitter link (twitter.com/im889) is the same link the article itself uses for Hencke; the saved photo matches the article''s own "Badge-hacking-2019-03-Nintendo-controllers.jpg" image, which the article attaches to this exact item. Note the two `sources` entries both cite the same single URL rather than two independent sources, so "low" confidence (one press mention, no maker page) stands. No unsupported field or sentence found; nothing else changed.'
last_modified_date: '2026-09-08'
---

At the 2019 Hackaday Supercon, the conference badge was an FPGA board with a cartridge slot, and attendees spent the weekend building add-on cartridges for it during the badge-hacking village. Ben Hencke's contribution was a cartridge that let a standard Nintendo game controller plug in and act as an input device for the badge, opening the door to multiplayer games running on the FPGA.

The project is documented only in Hackaday's post-event roundup of that year's badge hacks, which names Hencke and includes a photo of the controller wired into the badge; no standalone project page, source repository, or bill of materials has surfaced. As with most of the weekend's cartridges, it appears to have been a one-off built and demoed on site rather than something offered for sale or release afterward.
