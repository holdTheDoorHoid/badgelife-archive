---
title: LAN PARTY EVENT BADGE
id: saintcon-2023-lan-party-event-badge
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: SHIFTY
summary: A SAINTCON 2023 event minibadge for the con's LAN Party event, handed out to attendees who came to play.
functions: Two onboard LEDs (D1, D2), powered through the host badge's pin header, alternate in time with the host badge's clock once soldered; otherwise decorative, marking the wearer as a LAN Party attendee.
look:
  colors:
  - black
  - white
  shape: rectangle
  themes:
  - arcade
  - text
tech:
  mcu: none
  leds:
    count: 2
    type: null
    note: Two LEDs (D1, D2) and a single resistor (R1); no microcontroller; alternate in time with the host badge's clock once soldered.
  display: none
  connectivity: []
  battery: null
  sao_version: null
  power: powered by host badge
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given out at the LAN Party event at SAINTCON 2023; not sold.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=LAN%20PARTY%20EVENT%20BADGE&year=2023
  url: https://minibadge.wiki/?search=LAN%20PARTY%20EVENT%20BADGE&year=2023
  kind: website
images:
- file: assets/images/badges/saintcon-2023/lan-party-event-badge/3565a94c76.png
  source: https://minibadge.wiki/?search=LAN%20PARTY%20EVENT%20BADGE&year=2023
  credit: SHIFTY
  caption: LAN Party Event Badge, front
- file: assets/images/badges/saintcon-2023/lan-party-event-badge/8d1855ab87.png
  source: https://minibadge.wiki/?search=LAN%20PARTY%20EVENT%20BADGE&year=2023
  credit: SHIFTY
  caption: LAN Party Event Badge, back
contact: {}
notes:
- 'category: Event; rarity: Rare'
- 'Soldering difficulty listed as Beginner: solder the two LEDs and the resistor using the single-pad method, then the pin headers.'
status: released
sources:
- kind: url
  url: https://minibadge.wiki/?search=LAN%20PARTY%20EVENT%20BADGE&year=2023
  title: LAN PARTY EVENT BADGE
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2023''.'
- kind: url
  url: https://minibadge.wiki/2023.json
  title: MiniBadge Wiki 2023 data feed (LAN PARTY EVENT BADGE entry)
  accessed: '2026-09-07'
  note: 'Underlying JSON record for the badge: maker SHIFTY, description, soldering instructions/difficulty, category Event, rarity Rare, front/back image paths, "how to acquire" text. The page itself is a JS single-page app that renders from this feed.'
  archived: https://web.archive.org/web/20260611102022/http://minibadge.wiki/2023.json
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass: pulled the raw minibadge.wiki/2023.json feed directly (rather than the WebFetch summary of it) and confirmed maker, description, soldering instructions, category, rarity, and how-to-acquire text verbatim. Corrected functions/body: the source''s soldering notes state the two LEDs "alternate with the clock once built" (i.e. blink in time with the host badge''s clock), which the prior draft had flattened to a generic "light up when powered ... otherwise decorative" — fixed to reflect the alternating behavior. Softened "LAN Party room" (summary, get_one.where, body) to "LAN Party event" since no source uses "room"; the description only calls it "this classic event." Blanked tech.leds.type (was "reverse-mount"): the source text never names a mount style and the back-of-board photo does not clearly establish it, so it was invented rather than sourced. Corrected look.themes from [retro computer, text] to [arcade, text]: the front artwork shows a hooded figure with game
    controllers and a pixel font, which supports "arcade," but nothing in the art depicts a computer. Verified both saved images (3565a94c76.png, 8d1855ab87.png) against the source''s frontImageUrl/backImageUrl content: front matches the "LAN PARTY" pixel-art graphic, back matches "SAINTCON 2023 / SHIFTY" with D1, D2, R1 labeled, consistent with the entry. Only source remains the minibadge.wiki community database (a fan-run archive, not the maker''s own page); no maker storefront, repo, or social post was found for SHIFTY or this badge, so hardware/PCB files and open-source status stay unknown. quantityMade in the source feed is 0, minibadge.wiki''s default/unset value rather than a stated print run, so get_one.quantity is correctly left blank. The game lineup (StarCraft, Cursed Halo, Battlefield 1942, Minecraft, Overwatch 2, League of Legends, Rocket League, Payday 2) is event flavor text from the description, not badge features, and is presented as such. Everything remaining in the entry
    is now supported by the cited sources.'
last_modified_date: '2026-09-07'
---

The LAN Party Event Badge is a SAINTCON 2023 minibadge made by SHIFTY for the convention's LAN Party event, where attendees played games together — StarCraft, Cursed Halo, Battlefield 1942, Minecraft, Overwatch 2, League of Legends, Rocket League, and Payday 2, among others. It was not sold; attendees got one simply by showing up to the LAN Party.

The badge is a black PCB with white silkscreen art of a hooded gamer flanked by controllers, framed by an arc and the words "LAN PARTY" in a blocky pixel font. Electrically it is simple: two LEDs (D1, D2) and a single current-limiting resistor (R1), with no microcontroller, drawing power through the host badge's pin header. Per the maker's soldering notes, the two LEDs alternate in time with the host badge's clock once built, rather than simply staying lit — standard for a SAINTCON minibadge that plugs onto a larger master badge rather than carrying its own battery. The back is marked "SAINTCON 2023 / SHIFTY." Soldering is rated Beginner: the LEDs and resistor go on first using the single-pad hand-soldering method, followed by the pin headers.

The only source located for this badge is the minibadge.wiki community database, a fan-maintained catalog of SAINTCON minibadges; no storefront, repository, or social post from SHIFTY was found, so it isn't known whether design files were ever published.
