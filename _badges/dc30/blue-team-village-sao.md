---
title: Blue Team Village SAO
id: dc30-blue-team-village-sao
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: Blue Team Village
summary: A companion SAO shaped like the Blue Team Village shield-and-sword mark, made to plug into BTV's DEF CON 30 5th Anniversary badge.
functions: ''
look:
  colors:
  - blue
  shape: logo
  themes:
  - logo
  - security
  - mascot
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Picked up in person at Blue Team Village during DEF CON 30 (Flamingo Las Vegas, August 12-13, 2022) after reserving a free "pickup only" slot on Eventbrite.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.eventbrite.com/e/blue-team-village-sao-def-con-vegas-pickup-only-tickets-397239031637
  url: https://www.eventbrite.com/e/blue-team-village-sao-def-con-vegas-pickup-only-tickets-397239031637
  kind: website
images:
- file: assets/images/badges/dc30/blue-team-village-sao/c6337c21c1.jpg
  source: "https://www.eventbrite.com/e/blue-team-village-sao-def-con-vegas-pickup-only-tickets-397239031637"
  credit: "Blue Team Village"
  caption: "The BTV SAO, a blue PCB cut to the Blue Team Village shield-and-sword mark with SMD components and edge-castellated pins, shown resting on an oscilloscope's front panel"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: released
sources:
- kind: url
  url: https://www.eventbrite.com/e/blue-team-village-sao-def-con-vegas-pickup-only-tickets-397239031637
  title: Blue Team Village SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc30''.'
- kind: url
  url: https://www.eventbrite.com/e/blue-team-village-sao-def-con-vegas-pickup-only-tickets-397239031637
  title: "Blue Team Village SAO - DEF CON VEGAS PICKUP ONLY (Eventbrite listing)"
  accessed: '2026-09-07'
  note: "Confirmed event date (Aug 12-13, 2022, Flamingo Las Vegas), tagline ('Get a BTV SAO to stick on your Blue Team Village 5th Anniversary Badge -- it's BTV all the way down!'), and the listing's hero photo of the physical SAO."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    The Eventbrite listing confirms this is a real, physical SAO made to accompany BTV's DEF
    CON 30 5th Anniversary badge, and its hero photo (saved to images) shows the actual part:
    a blue PCB cut to the BTV shield-and-sword mark with a handful of small SMD components
    and gold edge-castellated pads along the bottom, consistent with an SAO edge connector.
    No maker page, repo, or press coverage turned up any chip, LED, or firmware details, and
    the Eventbrite page's ticket price was not recoverable from the fetched markup (the event
    has since ended, so the storefront no longer shows a purchasable price). Distribution was
    a free-reservation "pickup only" ticket rather than a paid store listing, hence
    get_one.distribution is set to village rather than purchase. This is a companion piece to
    the separate main-badge entry dc30-blue-team-village-btv-badge; it is not a duplicate of
    that entry.
last_modified_date: '2026-09-07'
---

Blue Team Village handed out this SAO at DEF CON 30 (Flamingo Las Vegas, August 12-13, 2022) as a companion add-on for its 5th Anniversary main badge that year. The board is cut to BTV's shield-and-sword mark rather than a rectangle, done in blue soldermask with white silkscreen artwork, and carries a small cluster of SMD components along with gold edge-castellated pads at the bottom consistent with an SAO edge connector.

Rather than being sold through a storefront, the SAO was distributed through an Eventbrite listing requiring a free "pickup only" reservation, redeemed in person at the village during the con. No maker write-up, repository, or press coverage was found describing its electronics (chip, LED count/type, or firmware), so those fields are left blank rather than guessed.
