---
title: WS2812 RGB LED Array badge hack
id: supercon-2019-ws2812-rgb-led-array-badge-hack
layout: badge
parent: Supercon 2019
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2019
year: 2019
makers:
- name: Thomas Sarlandie
  url: https://hackaday.io/sarfata
summary: 'A one-off colorful LED array Thomas Sarlandie added to his Supercon 2019 badge during badge-hacking, mentioned in passing in Hackaday''s roundup of that year''s badge mods.'
functions: ''
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
  leds:
    count: null
    type: null
    note: null
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
- label: hackaday.io/sarfata (Thomas Sarlandie)
  url: https://hackaday.io/sarfata
  kind: hackaday
images: []
contact: {}
notes:
- An addressable RGB LED array driven from the 2019 Supercon badge, by the maker of the shIRtty addon. Found by the event-year sweep, task supercon-2019.
status: listed
sources:
- kind: url
  url: https://hackaday.com/2019/11/29/a-fantastic-frontier-of-fpga-flexibility-found-in-the-2019-supercon-badge/
  title: WS2812 RGB LED Array badge hack
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2019); event read as ''supercon-2019''.'
- kind: url
  url: https://hackaday.com/2019/11/29/a-fantastic-frontier-of-fpga-flexibility-found-in-the-2019-supercon-badge/
  title: A Fantastic Frontier Of FPGA Flexibility Found In The 2019 Supercon Badge
  accessed: '2026-09-08'
  note: 'Confirmed the sole mention: "From a colorful array by Thomas Sarlandie to a retina-destroying setup from Garrett Mace" in the article''s roundup of badge-hacking LED mods. No dedicated project page found.'
- kind: url
  url: https://hackaday.io/sarfata
  title: Thomas Sarlandie - Hackaday.io profile
  accessed: '2026-09-08'
  note: 'Checked his Hackaday.io profile for a dedicated project page on this LED array. He has a documented project for the same badge (shIRtty addon, an IR SAO), but no project page for the WS2812 array itself.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-08'
  notes: 'The only source is a single sentence in Hackaday''s Nov 2019 roundup of Supercon badge hacks: "From a colorful array by Thomas Sarlandie to a retina-destroying setup from Garrett Mace..." That confirms the hack existed and was shown at Supercon 2019, but there is no dedicated project page, repo, photo, or further description of it anywhere found (checked Sarlandie''s Hackaday.io profile, which documents his shIRtty IR addon for the same badge but not this LED array). LED count, chip, mounting, and distribution are unknown and were left empty rather than guessed. Fact-check pass (2026-09-08): re-verified both cited sources word-for-word. The Hackaday sentence says only "a colorful array" and never names a chip; tech.leds.type had been set to WS2812 (matching the title/slug) with no source actually specifying that chip, so it was blanked back to null rather than left as an unsupported guess. Note the title and slug still carry the same "WS2812" assumption; left as-is since renaming/re-slugging is outside this pass, but it is equally unconfirmed by any source. A body sentence claiming the LEDs were wired onto the badge''s "perf/prototyping area" was also unsupported by any source and was trimmed. Everything else in the entry checked out against the two cited sources. This looks like an impromptu one-off hack shown at the con, not a distributed product, so most get_one/tech fields cannot be filled.'
last_modified_date: '2026-09-08'
---

A one-off badge hack shown at Hackaday Supercon 2019: Thomas Sarlandie — better known at that con for his shIRtty addon, an infrared-transceiver Shitty Add-On for the same badge — wired up a colorful array of addressable RGB LEDs to his badge. It's known only from a single mention in Hackaday's November 2019 roundup of Supercon badge-hacking projects, which singles it out as "a colorful array" alongside other attendees' LED mods.

No dedicated writeup, repository, or photo of this specific project has been found. It was likely a quick con-floor hack rather than a planned or distributed product, which fits the near-total absence of further documentation.
