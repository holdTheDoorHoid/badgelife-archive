---
title: Fuccs Shitty Addon
id: other-fuccs-shitty-addon-hw
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2019
makers:
- name: jeffmakes
  url: https://github.com/jeffmakes
  role: PCB layout and hardware design
- name: Jann Foehringer
  role: co-designer
summary: 'A low-poly fox-head shitty add-on (SAO) with two LEDs for eyes, driven by an ATtiny85, designed by jeffmakes and Jann Foehringer for the TROOPERS 19 security conference badge.'
functions: 'Two individually-controlled LEDs (the fox''s eyes) driven by an onboard ATtiny85 microcontroller. The SAO''s I2C pins double as an ISP header (SCK/MISO/MOSI/RESET) for programming the ATtiny85 in-circuit.'
look:
  colors:
  - blue
  - white
  shape: fox head
  themes:
  - animal
  - fox
tech:
  mcu: ATtiny85
  leds:
    count: 2
    type: discrete
    note: Reverse-mount/TOPLED-style SMD LEDs used as the fox's eyes, each driven through a 100 ohm resistor from the ATtiny85.
  display: null
  connectivity: []
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/jeffmakes/fuccs-shitty-addon-hw
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/jeffmakes/fuccs-shitty-addon-hw
  url: https://github.com/jeffmakes/fuccs-shitty-addon-hw
  kind: repo
- label: 'Insinuator.net: Troopers 19 – Badge Hardware'
  url: https://insinuator.net/2019/07/troopers-19-badge-hardware/
  kind: article
images:
  - file: assets/images/badges/other/fuccs-shitty-addon-hw/8d45026d0e.jpg
    source: "https://github.com/jeffmakes/fuccs-shitty-addon-hw"
    credit: "jeffmakes"
    caption: "KiCad 3D render of the Fuccs Shitty Addon PCB, a low-poly fox head with LED eyes"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/jeffmakes/fuccs-shitty-addon-hw
  title: fuccs-shitty-addon-hw
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://insinuator.net/2019/07/troopers-19-badge-hardware/
  title: 'Troopers 19 – Badge Hardware'
  accessed: '2026-09-07'
  note: 'ERNW/Insinuator writeup of the TROOPERS 19 badge by jeffmakes; describes the Fuccs Addon as a Shitty Addon designed with Jann Foehringer using the svg2shenzhen Inkscape workflow.'
- kind: url
  url: https://github.com/jeffmakes/fuccs-shitty-addon-hw/blob/master/fuccs-shitty-addon.kicad/fuccs-shitty-addon.sch
  title: fuccs-shitty-addon.sch
  accessed: '2026-09-07'
  note: 'Schematic confirms ATtiny85-20SU MCU, two LEDs (D1 "LED L", D2 "LED R") each with a 100 ohm series resistor, a 10K resistor, a 100nF decoupling cap, and a 2x3 SAO connector labeled "Shitty Addon + ISP" reusing SDA/SCL as MOSI/SCK for ISP programming.'
- kind: url
  url: https://raw.githubusercontent.com/jeffmakes/fuccs-shitty-addon-hw/master/gerber/README.txt
  title: gerber/README.txt
  accessed: '2026-09-07'
  note: 'Fabrication notes: 0.8mm FR4 substrate, 2-layer copper, blue soldermask both sides, white legend both sides.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Made for the TROOPERS 19 conference (Heidelberg, Germany, March 2019) badge, per the commit history (gerbers released March 2019) and the Insinuator.net article by the main badge''s co-designer. No "troopers" event exists yet in _data/events.yml, so event is left as "other" per the research guide; a maintainer could add a troopers-2019 event id. Could not confirm price, quantity made, or how/whether it was distributed to attendees separately from the main badge (the article''s "~600 happy badges" figure is for the main TROOPERS19 badge, not confirmed for this SAO). No firmware repository was found. The SVG artwork file (graphics/FUCSS_PCB_redrawn-correct-layers.svg) could not be saved as an archive image (fetch_image.py could not decode the SVG); the KiCad 3D-render PNG was saved instead. Fact-checked 2026-09-07: re-fetched the GitHub repo, schematic, gerber README, and Insinuator article, and confirmed the ATtiny85 MCU, 2 LEDs each with a 100-ohm resistor, ISP-over-SAO wiring, blue/white 2-layer 0.8mm FR4 fab spec, both makers, the svg2shenzhen workflow, and the March 2019 gerber-release commits. The saved image was pixel-matched against the repo''s graphics/fuccs-kicad-view.png and is an exact match. One nuance: the Insinuator article''s byline is Malte Heinzelmann, not jeffmakes; the post itself says it is written "by Jeff (@jeffmakes)" and only posted under Heinzelmann''s name, so "co-authored by the badge''s co-designer" is a reasonable paraphrase, not a citation error.'
last_modified_date: '2026-09-07'
---

The Fuccs Shitty Addon is a "shitty add-on" (SAO) shaped like a low-poly fox head, designed by jeffmakes and Jann Foehringer for the TROOPERS 19 security conference in Heidelberg, Germany (March 2019). It plugs into the TROOPERS 19 badge's SAO header, which supplies 3.3V power, and carries an ATtiny85 microcontroller that independently drives two SMD LEDs mounted as the fox's eyes, each through its own 100-ohm current-limiting resistor.

The board's artwork was created by tracing an SVG fox-head graphic into KiCad footprints using the svg2shenzhen Inkscape extension, a workflow the designers wrote up favorably in the companion article about the main TROOPERS 19 badge. The same 2x3 header used for the SAO interface doubles as an in-circuit ISP header, reusing the SAO's I2C data/clock lines as SPI MOSI/SCK so the ATtiny85 can be reprogrammed after assembly. Hardware design files (KiCad schematic/PCB, gerbers, and two production revisions) are published on GitHub, but no accompanying firmware repository has been found, and details on how many were made or how they reached attendees are not documented in the available sources.
