---
title: Custom case with LED "nOOds" for the Supercon 2025 badge
id: supercon-2025-custom-case-with-led-noods-for-the-supercon-2025-badge
layout: badge
parent: Supercon 2025
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2025
year: 2025
makers:
- name: thzinc
  url: https://thzinc.com/
summary: A 3D-printed replacement faceplate/case for the 2025 Supercon badge with glowing LED strand "noodles" run through curved channels, made by thzinc (Daniel James) for the con's opening badge-hacking day.
functions: 'Purely cosmetic: illuminates in a single color (blue, tested also in pink and green) via an LED strip routed through 3D-printed channels; no interactive functions of its own. Wired into an extra power/IO breakout on the host Supercon badge, exposed through the back of the case with no on/off switch (the LED runs whenever the badge is powered).'
look:
  colors:
  - blue
  - clear
  shape: rectangle
  themes:
  - synthwave
tech:
  mcu: none
  leds:
    count: null
    type: LED strip
    note: 'Described by the maker as LED "nOOds" (noodle-style strip lighting); several attendees mistook the strands for EL wire, which the maker notes it is not.'
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '1 (personal one-off build, not distributed)'
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: thzinc.com/2025/10/31/hackaday-superconference-2025-days-7-through-1-design-by-contract.html
  url: https://thzinc.com/2025/10/31/hackaday-superconference-2025-days-7-through-1-design-by-contract.html
  kind: website
images:
- file: assets/images/badges/supercon-2025/custom-case-with-led-noods-for-the-supercon-2025-badge/80ce358658.jpg
  source: "https://thzinc.com/2025/10/31/hackaday-superconference-2025-days-7-through-1-design-by-contract.html"
  credit: "thzinc (Daniel James)"
  caption: "Faceplate illuminated with electric blue LED strand, test-fit before final assembly"
- file: assets/images/badges/supercon-2025/custom-case-with-led-noods-for-the-supercon-2025-badge/258548c5f5.jpg
  source: "https://thzinc.com/2025/10/31/hackaday-superconference-2025-days-7-through-1-design-by-contract.html"
  credit: "thzinc (Daniel James)"
  caption: "Badge reassembled in the finished custom case, LED strand lit blue"
contact: {}
notes:
- Sweep initially saw this only in a search snippet (page appeared to return 403); a direct curl fetch with a browser User-Agent succeeded and confirmed the item and its details in full. Title and event id match the maker's own description.
status: released
sources:
- kind: url
  url: https://thzinc.com/2025/10/31/hackaday-superconference-2025-days-7-through-1-design-by-contract.html
  title: Custom case with LED "nOOds" for the Supercon 2025 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2025); event read as ''supercon-2025''.'
- kind: url
  url: https://thzinc.com/2025/10/31/hackaday-superconference-2025-days-7-through-1-design-by-contract.html
  title: Hackaday Superconference 2025 – Days -7 through 1 - Design by contract – thzinc
  accessed: '2026-09-10'
  note: Maker's blog post confirming the item exists; supplied maker name, design process, LED color testing, wiring to the badge's extra breakout, and reactions at the con.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Fact-check re-fetched the maker''s blog post directly (curl with a browser User-Agent; WebFetch still gets a 403 from this host) and confirmed every remaining factual sentence against it word-for-word: maker identity (Daniel James / thzinc, from the page byline and avatar alt text), the blue/pink/green color testing, the "transparent rectangle" case shape, the extra power/IO breakout wiring with no on/off switch, the EL-wire mix-up with attendees, and the personal one-off status. Removed the "retro computer" look theme, which was not supported by any source (only "synthwave" is backed by the maker''s own "80s neon" description). A follow-up web search turned up no independent press coverage or storefront/file listing for this item, and the maker''s Thingiverse profile could not be checked for a published model (client-rendered page, not fetchable by curl) — this does not contradict anything in the entry, since make_your_own fields are already left empty. Confidence stays medium because everything rests on a single primary source, even though that source was read in full.'
last_modified_date: '2026-09-10'
---

For Supercon 2025, hacker and blogger thzinc (Daniel James) 3D-printed a replacement faceplate and case for the official Supercon badge, threading LED strip lighting through curved channels for an "80s neon" look he calls LED "nOOds." He iterated through a few design ideas — including working his own handle into the case and echoing the badge's "Jazz woosh" branding — before settling on the curved design, and test-printed the faceplate in a few colors (pink, green, and blue) before choosing blue as the final look.

To power the LEDs, he tapped an extra power/IO breakout on the badge itself, soldering on headers and routing a short wire out through the back of the new case; there is no on/off switch, so the light runs whenever the badge is powered. He built and wore the case in time for the con's opening badge-hacking day, where several attendees mistook the glowing strands for EL wire (which requires much higher voltage than the low-voltage LED strip he actually used). The project was a personal build for himself rather than something sold, kitted, or open-sourced.
