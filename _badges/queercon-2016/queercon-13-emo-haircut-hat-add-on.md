---
title: Queercon 13 emo-haircut hat add-on
id: queercon-2016-queercon-13-emo-haircut-hat-add-on
layout: badge
parent: Queercon 13 (2016)
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: queercon-2016
year: 2016
makers:
- name: Queercon badge team
  url: https://github.com/duplico/qc13
  role: unconfirmed which team member designed this specific hat
summary: A plug-in "hat" for the 2016 Queercon 13 cuttlefish/squid badge shaped like an emo haircut, one of three hat styles (with a unicorn horn and an LED top hat) made to fit the badge's expansion ports.
functions: Plugs into either of the two 1x4 expansion headers on top of the Queercon 13 badge's head, which carry power, ground, and an I2C bus; whether this specific hat carries its own LEDs driven over that bus (as the top hat reportedly did) is unconfirmed.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - meme
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed with or alongside the Queercon 13 badge at DEF CON 24 (2016).
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/52950-shitty-add-ons/log/151626-an-oral-history-of-the-shitty-add-on-standard
  url: https://hackaday.io/project/52950-shitty-add-ons/log/151626-an-oral-history-of-the-shitty-add-on-standard
  kind: website
- label: "Hackaday: What We Learned from the 2016 Queercon Badge"
  url: https://hackaday.com/2016/08/10/what-we-learned-from-the-2016-queercon-badge/
  kind: article
- label: duplico/qc13 (Queercon 13 badge firmware repo)
  url: https://github.com/duplico/qc13
  kind: repo
images:
  - file: assets/images/badges/queercon-2016/queercon-13-emo-haircut-hat-add-on/9033fac38e.jpg
    source: "https://hackaday.com/2016/08/10/what-we-learned-from-the-2016-queercon-badge/"
    credit: "Hackaday"
    caption: "Queercon 13 cuttlefish badge shown with its plug-in hat add-ons"
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/52950-shitty-add-ons/log/151626-an-oral-history-of-the-shitty-add-on-standard
  title: Queercon 13 emo-haircut hat add-on
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://hackaday.io/project/52950-shitty-add-ons/log/151626-an-oral-history-of-the-shitty-add-on-standard
  title: An oral history of the shitty add-on standard
  accessed: '2026-09-10'
  note: "Confirms the emo haircut existed as one of three hat options (unicorn horn, emo haircut, top hat with LEDs) for the 2016 Queercon cuttlefish badge, connected via a 1x4 power/ground/I2C header."
- kind: url
  url: https://hackaday.com/2016/08/10/what-we-learned-from-the-2016-queercon-badge/
  title: What We Learned from the 2016 Queercon Badge
  accessed: '2026-09-10'
  note: "Describes the Queercon 13 badge (squid/cuttlefish shape, 60 cyan eye LEDs, RGB tentacle LEDs, MSP430, phototransistor, 2x AA) and its two head-mounted hat expansion ports; names the unicorn horn as the article's favorite hat but does not describe the emo haircut hat specifically. Source of the saved photo."
- kind: url
  url: https://github.com/duplico/qc13
  title: "duplico/qc13: Queercon 13 electronic badge"
  accessed: '2026-09-10'
  note: "Badge firmware repo ('The Blooper!'), credits George Louthan; confirms MSP430FR5949 MCU and hat support, but repo's imaging/ directory holds only flashing scripts, no hat-specific files or photos."
research:
  status: verified
  confidence: low
  last_checked: '2026-09-10'
  notes: >-
    Fact-check pass (2026-09-10): re-fetched all three cited sources and confirmed the core claims --
    the Hackaday.io oral history quotes the 1x4 power/ground/I2C header and the three hat styles
    (unicorn horn, emo haircut, LED top hat); the Hackaday.com article confirms the badge shape, LED
    counts, MCU-era details, the four-person maker team (Evan Mackay, George Louthan, Jonathan Nelson,
    Jason Painter), and carries the saved photo; the duplico/qc13 repo's imaging/ directory was checked
    directly via the GitHub API and holds only flashing scripts (base_flash.bat, flash.bat, flash.py,
    qc13.txt), confirming no hat-specific files or photos exist there. Two claims were softened for
    lack of direct support: `summary` no longer says the hats were "sold" (distribution channel is
    unconfirmed) and `functions` no longer implies this specific hat drives lighting effects, since no
    source confirms the emo-haircut hat carries its own LEDs (unlike the top hat). Existence and the
    general plug-in mechanism are confirmed; no source describes the emo-haircut hat individually
    (materials, LEDs if any, who specifically designed it, or quantity made), so those fields correctly
    remain empty. The badge team is credited for the badge overall, not for this hat specifically --
    role is marked unconfirmed. No dedicated storefront, repo, or photo of the emo-haircut hat alone was
    found; the saved image shows the badge wearing its hats as a set.
last_modified_date: '2026-09-10'
---

The emo-haircut hat was one of three interchangeable "hats" made for the 2016 Queercon 13 badge, a squid/cuttlefish-shaped board designed by Evan Mackay, George Louthan, Jonathan Nelson, and Jason Painter for DEF CON 24. The badge had two small expansion ports on top of its head that broke out power, ground, and an I2C bus on a 1x4 connector -- a design that predates and helped inspire the later Shitty Add-On (SAO) standard. Wearers could plug in a hat shaped like an emo haircut, a unicorn horn with a rainbow LED inside, or a top hat studded with LEDs.

Beyond its existence and general mechanism, no source found describes the emo-haircut hat on its own: no maker credit specific to this hat, no photo isolating it from the badge's other hats, and no details on its construction or whether it carried its own LEDs (as the top hat apparently did). The one image on file shows the Queercon 13 badge wearing its hats as a set rather than the emo haircut individually.
