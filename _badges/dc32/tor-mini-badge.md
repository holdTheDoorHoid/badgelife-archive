---
title: TOR Mini Badge
id: dc32-tor-mini-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: dc32
year: 2024
makers:
- name: Seeess
summary: A five-LED minibadge/SAO by Seeess sold at DEF CON 32, deliberately pitched as being either "a very shitty badge, or an amazing SAO."
functions: Its either a very shitty badge, or an amazing SAO. It can be powered independently or off a host badge (via SAO port) and has a MCU but only 5 LEDs. It can be used to blink back different sequences, and has two simple games that you can plan to unlock two additional modes.
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
  leds:
    count: 5
    type: null
    note: Blinks back different sequences; exact LED part not stated by any source found.
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $50.00
  price_usd: 50.0
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links: []
images: []
contact: {}
notes: []
status: listed
sources:
- kind: sheet
  event: dc32
  row: 94
  updated: '2024-06-12'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-06'
  notes: 'Extensive search turned up nothing independent for this specific item. Tried:
    Google/Bing/DuckDuckGo (all blocked JS challenges or returned no usable results),
    Hackaday.io (the "seeess" profile exists, joined 2017, but has zero projects
    created and does not list this badge), GitHub search (no repo matches "seeess
    mini" or a TOR mini badge), Tindie (seeess store returned 403), Reddit (fetch
    blocked), and X/Twitter (fetch blocked, paywalled). The one substantive hit was
    a GitHub mirror (stevemats/lie_detector_badge) archiving Seeess''s separate DC29
    "TOR Lie Detector Badge" -- a different, larger item (SAMD21/Seeeduino XIAO,
    dual OLEDs, GSR + heart-rate sensors) whose profits went to the Tor Project.
    That confirms Seeess has a history of Tor-themed badges/SAOs and lends some
    plausibility to this mini badge''s name referencing Tor, but nothing found
    confirms that link, a chip, LED type, quantity, or availability for the Mini
    Badge itself, so those fields are left empty rather than guessed. Left the
    community-sheet description (title, price, functions) as the sole basis for
    this entry.'
last_modified_date: '2026-09-06'
---

The TOR Mini Badge is a compact minibadge/SAO by the maker Seeess, sold at DEF CON 32 for $50. The maker's own pitch -- "either a very shitty badge, or an amazing SAO" -- frames it as a deliberately minimal companion piece: it runs its own MCU but drives only five LEDs, and can be worn standalone with its own power or plugged into a host badge's SAO port to draw power from it.

Functionally it's built around blinking back LED sequences, with two simple games built in that can unlock two further modes -- suggesting a small puzzle layer on top of what is otherwise a bare-bones blinky add-on.

Seeess also made the larger "TOR Lie Detector Badge" (first appearing at DEF CON 29, with a version also listed for DC32), a GSR-and-heart-rate SAO whose sale proceeds went to the Tor Project. That history makes it likely this Mini Badge's name is a nod to the same theme, though no source found confirms that link for this specific item, and no chip, LED part number, quantity made, or current availability could be verified independently of the community sheet this entry was imported from.
