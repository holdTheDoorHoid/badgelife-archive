---
title: NixieSAO
id: supercon-2024-nixiesao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Kevin Santo Cappuccio
  url: https://hackaday.io/architeuthisFlux
summary: A hand-built Simple Add-On for the 2024 Hackaday Supercon badge that mounts a genuine vintage Burroughs Nixie tube on a spinning slip ring so it can display any digit 0-9.
functions: Displays a single digit (0-9) on a real Nixie tube; the tube itself is mounted on a rotating DIY slip ring and connected to an 18-position selector switch (salvaged from a resistance substitution box) to pick the digit.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - hardware tool
tech:
  mcu: none
  leds: null
  display: Burroughs 122P244 Nixie tube
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/197822-nixiesao
  url: https://hackaday.io/project/197822-nixiesao
  kind: hackaday
- label: "Hackaday.io profile: architeuthisFlux (Kevin Santo Cappuccio)"
  url: https://hackaday.io/architeuthisFlux
  kind: hackaday
- label: "Hackaday.com: There's Already A Nixie Addon For The 2024 Supercon Badge"
  url: https://hackaday.com/2024/09/12/theres-already-a-nixie-addon-for-the-2024-supercon-badge/
  kind: article
images:
- file: assets/images/badges/supercon-2024/nixiesao/2782d22f95.jpg
  source: "https://hackaday.io/project/197822-nixiesao"
  credit: "Kevin Santo Cappuccio"
  caption: "The NixieSAO with its Burroughs Nixie tube lit and displaying a digit"
contact: {}
notes:
- "Sheet listed the maker as 'astuder (Adrian Studer)'; sources instead credit Kevin Santo Cappuccio (Hackaday.io user architeuthisFlux, maker of the Jumperless smart breadboard) as the sole builder. Corrected."
status: released
sources:
- kind: url
  url: https://hackaday.io/project/197822-nixiesao
  title: NixieSAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''Supercon''.'
- kind: url
  url: https://hackaday.io/project/197822-nixiesao
  title: NixieSAO
  accessed: '2026-09-07'
  note: "Project page: built for Supercon 8 (2024) SAO Contest, submitted 09/06/2024; uses a Burroughs 122P244 Nixie tube, an HV8200 180V nixie power supply, an 18-position selector switch, and a hand-etched copper slip ring; no PCB, no firmware; build took about 6 hours."
- kind: url
  url: https://hackaday.com/2024/09/12/theres-already-a-nixie-addon-for-the-2024-supercon-badge/
  title: "There's Already A Nixie Addon For The 2024 Supercon Badge"
  accessed: '2026-09-07'
  note: Confirms maker (Kevin Santo Cappuccio), the 2024 Supercon badge context, and component details (Burroughs Nixie tube, HV8200 supply, salvaged selector switch, DIY slip ring).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: "No price, quantity, or distribution info found - this reads as a one-off contest entry rather than something sold or given away, so get_one fields are left empty/unknown and availability is set to not_released. No design files (hardware/firmware) were published; make_your_own fields left null. LED info left null since the tube itself is the display, not an LED array."
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/nixiesao/
---

The NixieSAO is a Simple Add-On built by Kevin Santo Cappuccio (Hackaday.io user architeuthisFlux, also known for the Jumperless smart breadboard) for the SAO contest at Hackaday Supercon 8 in 2024. Rather than a conventional PCB with surface-mount LEDs, it centers on a genuine vintage Burroughs 122P244 Nixie tube - a real piece of 1960s-era hardware that contains a small amount of radioactive Krypton-85, as is typical of Nixie tubes of that era.

To drive the tube from a badge's low-voltage SAO header, Cappuccio used an HV8200 nixie power supply module that steps 3V up to the roughly 180V a Nixie tube needs to glow. The digit shown (0 through 9) is selected using an 18-position rotary switch salvaged from a resistance substitution box, and because the whole tube assembly needed to rotate, he built a makeshift slip-ring contact system out of pogo pins riding on hand-etched concentric copper rings on a scrap of copper-clad board. The entire build - deliberately avoiding both custom PCB design and any firmware - reportedly came together in about six hours, in keeping with a "no code, no PCB" ethos that made it a contender for the contest's Least Manufacturable award.

No evidence was found that the NixieSAO was ever sold, kitted, or given away beyond the single contest unit; it appears to be a one-off demonstration piece rather than a released product, and no hardware or firmware files have been published for it.
