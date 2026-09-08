---
title: LineCon Badge
id: dc26-linecon-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Team MissingNo.
summary: An unofficial DEF CON 26 badge with half-tone artwork rendered directly in the PCB silkscreen, whose main interaction is poking a finger into a hole to trip an IR sensor.
functions: 'Poking a finger into a hole in the board triggers an IR sensor, a playful nod to "linecon" (waiting in line for the official badge). Also offers USB connectivity for serial-based puzzles and unlocks.'
look:
  colors: []
  shape: null
  themes:
  - halftone
tech:
  mcu: STM32
  leds:
    count: 30
    type: APA102
    note: RGB LEDs arranged around the edge of the board
  display: 64x128 OLED
  connectivity:
  - usb
  battery: 3x battery (unspecified cell), mounted on the back for weight balance
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
- label: hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1
  url: https://hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1/
  kind: article
images:
- file: assets/images/badges/dc26/linecon-badge/83c1d2339b.jpg
  source: "https://hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1/"
  credit: "Hackaday"
  caption: "Front of the LineCon badge, showing the half-tone PCB artwork"
- file: assets/images/badges/dc26/linecon-badge/89680772fa.jpg
  source: "https://hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1/"
  credit: "Hackaday"
  caption: "Rear of the LineCon badge, showing the three-battery layout"
contact: {}
notes:
- DC26 indie badge noted for half-tone art rendered directly on the PCB silkscreen. Found by the event-year sweep, task dc26-indie.
- 'The sweep''s notes described the item generically; the maker calls it "LineCon" and the team behind it is Team MissingNo. (also seen written team_missing_no).'
status: listed
sources:
- kind: url
  url: https://hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1/
  title: LineCon Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc26-indie); event read as ''dc26''.'
- kind: url
  url: https://hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1/
  title: All The Badges Of DEF CON 26 (vol 1)
  accessed: '2026-09-08'
  note: Confirms maker (Team MissingNo.), the half-tone silkscreen art, the finger-hole IR interaction, USB puzzle/unlock feature, STM32 MCU, 64x128 OLED display, 30 APA102 LEDs, and the three-battery rear layout. Source of both saved photos.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed as a real DEF CON 26 (2018) badge via Hackaday coverage, which is the strongest source found; no maker-owned page, GitHub repo, or storefront could be located to confirm price, quantity, availability, or open-source status, so those fields are left empty. A web search surfaced a Team MissingNo. tweet referencing a "LineCon 2017" badge (tagged #defcon25) alongside a kit/assembled pricing post ($60 kit / $80 assembled), but that post could not be confirmed as describing this specific DC26 (2018) unit rather than an earlier or later year in the same LineCon series, so it was not used to fill get_one fields.'
last_modified_date: '2026-09-08'
---

The LineCon badge is an unofficial hardware badge Team MissingNo. brought to DEF CON 26 in 2018. Its most distinctive feature is artwork rendered as a half-tone image directly in the PCB silkscreen, a technique Hackaday singled out as unusually accomplished given the medium's limitations. The badge is built around an STM32 microcontroller with a 64x128 OLED display and a ring of 30 APA102 RGB LEDs around its edge, and it connects over USB to support serial-based puzzles and unlocks.

The badge's namesake feature is a hole in the board that houses an IR sensor: poking a finger into it registers an interaction, a wink at "linecon," the long wait for the official DEF CON badge that this project's name plays on. On the back, three batteries are positioned to balance the badge's weight, a deliberate departure from the single-battery-holder layout common on other badges of the era.

No maker-owned page, repository, or storefront was found during this research pass, so price, quantity, and availability are left blank rather than guessed. A social media post referencing a "LineCon 2017" badge and kit/assembled pricing surfaced in search, but it could not be confirmed as describing this same 2018 DC26 edition of the badge, so it was not used to populate those fields.
