---
title: NYC Badge
id: dc34-nyc-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: buck
summary: A beginner-friendly electronic badge with pre-soldered neo-pixels and three SAO connectors, made for DEF CON 34 badge pickup.
functions: 'Lights up via onboard and SAO-connected neo-pixels; two tactile switches and a power switch for basic interaction.'
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: ATMEGA328
  leds: null
  display: none
  connectivity: []
  battery: 3x AAA
  sao_version: null
get_one:
  price: $60
  price_usd: 60
  quantity: '20'
  availability: sold_out
  distribution:
  - purchase
  where: Sold through Uberflux (uberflux.com), an independent badge/SAO marketplace.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: uberflux.com/product/BUCK-NYC
  url: https://uberflux.com/product/BUCK-NYC
  kind: store
images:
  - file: assets/images/badges/dc34/nyc-badge/48ab8c53ae.jpg
    source: "https://uberflux.com/product/BUCK-NYC"
    credit: "buck / Uberflux"
    caption: "The NYC Badge, an ATMEGA328-based DEF CON 34 badge with 3 SAO connectors"
contact: {}
notes:
- 'Uberflux. $60, status: sold out.'
- 'Uberflux lists the badge under DEF CON 34 Badge Pickup; the maker''s Uberflux profile page (uberflux.com/maker/buck) gives no further biographical or social info.'
status: released
sources:
- kind: url
  url: https://uberflux.com/product/BUCK-NYC
  title: NYC Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: uberflux-shops); event read as ''unknown''.'
- kind: url
  url: https://uberflux.com/product/BUCK-NYC
  title: NYC Badge
  accessed: '2026-09-07'
  note: 'Confirmed maker, MCU (ATMEGA328, 16MHz), 3 SAO connectors, 6 unsoldered neo-pixels, 2 tactile switches, power switch, AAA battery holder, $60 price, 20 units made and sold out, and that it was made for DEF CON 34 badge pickup.'
- kind: url
  url: https://uberflux.com/maker/buck
  title: 'buck - Uberflux maker profile'
  accessed: '2026-09-07'
  note: 'Maker profile page; lists only the NYC Badge, no bio or external links found.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-checked 2026-09-07: re-fetched the Uberflux product page (BUCK-NYC) and maker profile (buck) directly (including the page''s embedded JSON) and confirmed maker, ATMEGA328 (pre-flashed, 16MHz crystal), 3 SAO connectors, 6 unsoldered neo-pixels enough for one bottom SAO, 2 tactile switches + power switch, 3x AAA battery holder (not included), $60 price, 20/20 sold, "Def Con 34 Badge Pickup" as the drop, and event dc34 = DEF CON 34 = 2026 per _data/events.yml. Maker profile page confirmed no bio/social links beyond this one listing. Verified the saved product photo (48ab8c53ae.jpg) matches the page''s own cover image. No contradictions found; all remaining empty fields (look.colors, look.shape, look.themes, tech.leds, tech.connectivity, tech.sao_version, make_your_own.*) were correctly left blank because the source never states them. Every fact remaining in the entry is directly supported by the cited sources.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/nyc-badge/
---

The NYC Badge is an entry-level electronic badge made by a maker going by "buck" and sold through the Uberflux badge marketplace, intended as a pickup item at DEF CON 34. It runs on a pre-flashed ATMEGA328 microcontroller with a 16 MHz crystal and is built around beginner-friendly assembly: the bridge and back-layer neo-pixels come pre-soldered, so builders only need to add header pins and other through-hole parts. It is powered by three AAA batteries (not included) and includes a power switch and two tactile switches for interaction.

The badge carries three SAO (Shitty Add-On) connectors and ships with six unsoldered neo-pixel LEDs, enough to light one bottom SAO of the buyer's choosing, letting owners customize which add-on gets illuminated. It sold for $60 in a run of 20 units, all of which sold out on Uberflux.

No hardware or firmware files were found to be published for this badge, and the maker's Uberflux profile page offers no additional biography or outside links.
