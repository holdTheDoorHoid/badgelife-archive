---
title: Mr. Robot shitty addon
id: supercon-2019-mr-robot-shitty-addon
layout: badge
parent: Supercon 2019
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2019
year: 2019
makers:
- name: davedarko
  url: https://hackaday.io/davedarko
summary: An ATtiny85-based I2C sound-card Shitty Add-On shaped like the Mr. Robot (fsociety) mask, designed by davedarko in October 2019 to test OSH Park After Dark PCBs and given working I2C tone firmware at Hackaday Supercon 2019 using the Penghicorn badge as host.
functions: Receives I2C commands from a host badge and plays tones through a small onboard speaker/amplifier.
look:
  colors:
  - black
  shape: null
  themes:
  - robot
  - tv
tech:
  mcu: ATtiny85
  leds: null
  display: none
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: null
get_one:
  price: $12.30 (OSH Park PCB cost)
  price_usd: 12.3
  quantity: ''
  availability: unknown
  distribution: []
  where: Given out / built with fellow badge makers at Hackaday Supercon 2019; not a general storefront listing.
make_your_own:
  open_source: partial
  hardware_url: https://oshpark.com/shared_projects/XmKK8P7r
  firmware_url: null
  eda_tool: Eagle
links:
- label: hackaday.io/project/168037-mr-robot-shitty-addon
  url: https://hackaday.io/project/168037-mr-robot-shitty-addon
  kind: hackaday
  archived: https://web.archive.org/web/20260511233618/https://hackaday.io/project/168037-mr-robot-shitty-addon
- label: hackaday.io/project/168037-mr-robot-shitty-addon/logs
  url: https://hackaday.io/project/168037-mr-robot-shitty-addon/logs
  kind: hackaday
- label: oshpark.com/shared_projects/XmKK8P7r
  url: https://oshpark.com/shared_projects/XmKK8P7r
  kind: fab
  archived: https://web.archive.org/web/20260509231854/https://oshpark.com/shared_projects/XmKK8P7r
images:
- file: assets/images/badges/supercon-2019/mr-robot-shitty-addon/fbb58473d9.jpg
  source: https://hackaday.io/project/168037-mr-robot-shitty-addon
  credit: davedarko
  caption: Mr. Robot shitty addon SAO board
  archived: https://web.archive.org/web/20260511233618/https://hackaday.io/project/168037-mr-robot-shitty-addon
- file: assets/images/badges/supercon-2019/mr-robot-shitty-addon/6df3b79535.jpg
  source: https://hackaday.io/project/168037-mr-robot-shitty-addon
  credit: davedarko
  caption: Mr. Robot shitty addon board, project photo
  archived: https://web.archive.org/web/20260511233618/https://hackaday.io/project/168037-mr-robot-shitty-addon
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/168037-mr-robot-shitty-addon
  title: Mr. Robot shitty addon | Hackaday.io
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260511233618/https://hackaday.io/project/168037-mr-robot-shitty-addon
- kind: url
  url: https://hackaday.io/project/168037-mr-robot-shitty-addon
  title: Mr. Robot shitty addon | Hackaday.io
  accessed: '2026-09-07'
  note: Project summary, description, timeline, and og:image used for confirming details and grabbing a photo.
  archived: https://web.archive.org/web/20260511233618/https://hackaday.io/project/168037-mr-robot-shitty-addon
- kind: url
  url: https://hackaday.io/project/168037-mr-robot-shitty-addon/logs
  title: Mr. Robot shitty addon - Logs | Hackaday.io
  accessed: '2026-09-07'
  note: Build logs confirming ATtiny85, I2C tone firmware written at Supercon (11/17-18/2019), Penghicorn badge used as host, and speaker volume limitations.
- kind: url
  url: https://oshpark.com/shared_projects/XmKK8P7r
  title: OSH Park shared project - Mr. Robot Badge Shitty Addon
  accessed: '2026-09-07'
  note: PCB specs (1.58 x 1.57 in, 2-layer, black "After Dark" finish, $12.30), component list (ATtiny85, BC847, KMTG-1102 speaker).
  archived: https://web.archive.org/web/20260509231854/https://oshpark.com/shared_projects/XmKK8P7r
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's own Hackaday.io project page and logs, plus the OSH Park shared-project page, confirm the core facts. No firmware repo link or standalone image gallery was found beyond the project page photos; quantity made and formal availability/distribution are not stated anywhere found, so those fields are left empty. LED info not mentioned in any source (likely none - it's an audio-only SAO), left as null rather than guessed.
last_modified_date: '2026-09-07'
---

The Mr. Robot shitty addon is an I2C sound-card SAO shaped like the fsociety/Mr. Robot mask, designed by Hackaday.io user davedarko in October 2019. It was built specifically to test OSH Park's then-new "After Dark" black PCB process, and doubles as a working badge accessory: an ATtiny85 drives a small speaker through a BC847 transistor amplifier, letting a host badge send it I2C commands to play tones.

The board started out without firmware ("no firmware yet" in the original write-up), but davedarko finished working I2C tone-generation code during Hackaday Supercon 2019 in November, using the Penghicorn badge as the I2C host to trigger it. Build logs from the show note that the speaker output was quieter than hoped, with the maker considering alternative surface-mount speakers (citing a beeping R2D2 SAO as reference) for a possible future revision.

Hardware files (Eagle schematic/board plus a PDF) are shared publicly via an OSH Park shared-project link, making the board itself open for anyone to order a copy; no firmware repository link was found. Quantity built and how widely it was distributed beyond the Supercon crowd are not documented in the sources found.
