---
title: Whose Slide Is It Anyway? 10 Year Anniversary Badge
id: dc34-whose-slide-is-it-anyway-10-year-anniversary-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Whose Slide Is It Anyway?
  url: https://wsiiax.myshopify.com/
summary: A commemorative electronic badge marking ten years of the "Whose Slide Is It Anyway?" DEF CON improv-comedy contest, with a silk-screened replica of the event's iconic gong artwork.
functions: For such a tiny speaker, it's pretty goddamn loud when you hit the GONG! button. 24 LED's doing a light show every time a sound effect plays ensures nobody will miss you in a crowd. Includes three pre-programmed sound effects, each with its own synchronized LED light show, including the signature gong.
look:
  colors: []
  shape: null
  themes:
  - meme
  - pop culture
  - charity
tech:
  mcu: ESP32-C3
  leds:
    count: 24
    type: RGB
    note: ''
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $75 pre-con, stupid human tricks during con.
  price_usd: 75.0
  quantity: '~100'
  availability: sold_out
  availability_note: Checked 2026-09-06; Shopify listing shows sold out.
  distribution:
  - purchase
  - charity
  where: Sold via the WSIIAX Shopify store ($75); pickup at DEF CON or by international arrangement (UK buyers could collect in Glasgow the weekend after DEF CON).
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: wsiiax.myshopify.com
  url: https://wsiiax.myshopify.com/
  kind: store
- label: www.youtube.com/watch?v=GrN6yD06NBM
  url: https://www.youtube.com/watch?v=GrN6yD06NBM
  kind: video
- label: Product page (10 Year Anniversary Badge)
  url: https://wsiiax.myshopify.com/products/whose-slide-is-it-anyway-10-year-anniverary-badge
  kind: store
images:
- file: assets/images/badges/dc34/whose-slide-is-it-anyway-10-year-anniversary-badge/a3d3f9336e.jpg
  source: "https://wsiiax.myshopify.com/products/whose-slide-is-it-anyway-10-year-anniverary-badge"
  credit: "WSIIAX"
  caption: "Front of the badge with silk-screened replica of the WSIIA gong artwork"
- file: assets/images/badges/dc34/whose-slide-is-it-anyway-10-year-anniversary-badge/ebaf603be3.jpg
  source: "https://wsiiax.myshopify.com/products/whose-slide-is-it-anyway-10-year-anniverary-badge"
  credit: "WSIIAX"
  caption: "Back of the PCB badge"
contact:
  discord: rand0h
  emails:
  - Danny.Akacki@gmail.com
  - rand0h@defcon.social
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 28
  updated: 7/3/2026 9:34:53
  listing: New
- kind: url
  url: https://wsiiax.myshopify.com/products/whose-slide-is-it-anyway-10-year-anniverary-badge
  title: "Whose Slide Is It Anyway? 10 Year Anniversary Badge – WSIIAX"
  accessed: '2026-09-06'
  note: Primary source for price, quantity (~100), availability (sold out), MCU (ESP32-C3), LED count, sound effects, artist credits (Blenster, 1DarkOne), and the charity purpose (proceeds to Aaron "Bind" Kremin's family).
- kind: url
  url: https://wsiiax.myshopify.com/
  title: Whose Slide 10 Year Anniversary Badge – WSIIAX
  accessed: '2026-09-06'
  note: Confirms store, price, and product images.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: >-
    Maker's own Shopify product page confirms the core technical facts (ESP32-C3, 24 RGB LEDs,
    3 sound effects with light shows, ~100 units made, $75, sold out). No hardware/firmware
    repo or Gerbers were found, so make_your_own fields are left empty rather than guessed.
    The linked YouTube video (GrN6yD06NBM) could not be fetched for content (only footer/nav
    text returned) so it was kept as a link but not used as a source. The badge honors Aaron
    "Bind" Kremin, creator of the original WSIIA gong, who has passed away; proceeds beyond
    manufacturing cost go to his family's medical costs. The event itself began at DEF CON 25
    (2017 per most WSIIA history, though the store page says "began at DEF CON 25 in 2016" -
    noting the discrepancy here rather than resolving it).
last_modified_date: '2026-09-06'
---

The Whose Slide Is It Anyway? 10 Year Anniversary Badge is a limited-run electronic badge celebrating a decade of the DEF CON stage contest of the same name, where contestants improvise lightning talks over random, unseen slide decks. Roughly 100 were made and sold through the group's Shopify store for $75, with buyers picking up their badge at DEF CON (or arranging pickup in Glasgow, for UK backers). It runs on an ESP32-C3 driving 24 RGB LEDs and a small but surprisingly loud speaker, playing three pre-programmed sound effects — including the contest's signature gong — each paired with its own LED light show.

The front of the board carries a silk-screened replica of the artwork from the actual WSIIA gong, designed by Blenster with rear artwork by 1DarkOne. The badge doubles as a tribute: it commemorates Aaron "Bind" Kremin, who built the original gong for the event and has since passed away, and proceeds beyond manufacturing cost were directed to supporting his family with ongoing medical costs.

No hardware or firmware files were found to be published for this badge, so it is documented here as closed/unreleased design rather than open source.
