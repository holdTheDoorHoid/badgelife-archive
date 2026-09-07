---
title: The Future will Prevail
id: dc31-the-future-will-prevail
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: Richard Gowen
  role: creator / campaign owner
- name: Alt_Bier
  url: https://www.youtube.com/@alt_bier_hacker
  role: team member
- name: Brian Culver
  role: team member
summary: A Back to the Future / DeLorean themed wearable badge crowdfunded on Indiegogo for DEF CON 31, with a laser-engraved time-machine scene and RGB LEDs that light up flame and lightning-bolt accents.
functions: RGB LED lighting effects (flame trail and lightning-bolt patterns around the engraved DeLorean); worn clipped on with carabiner-style hooks like a badge/pin.
look:
  colors:
  - blue
  - gold
  - multicolor
  shape: rectangle
  themes:
  - movie
  - sci-fi
  - retro computer
  form_factor: pcb badge
tech:
  mcu: ESP32
  leds:
    count: null
    type: RGB
    note: Edge-lit RGB LEDs produce flame and lightning-bolt lighting effects around the DeLorean artwork, visible in the campaign's own photos; exact LED count and driver chip are not stated in any source found.
  display: null
  connectivity:
  - wifi
  battery: 9V (two included per kit; ~7-8 hours runtime)
  sao_version: null
get_one:
  price: $60 kit / $100 assembled
  price_usd: null
  quantity: 120 DIY kits offered (65 claimed) and 35 fully-assembled badges offered (35 claimed, sold out)
  availability: sold_out
  availability_note: Indiegogo campaign ran 2023-06-05 to 2023-07-05 and ended funded ($7,400 raised of a $5,000 goal, 148%, 100 backers). The $100 assembled-badge tier sold out (35/35 claimed); the $60 DIY-kit tier did not sell out (65/120 claimed) but the campaign is closed. Checked via a Wayback Machine snapshot from 2023-09-27; the live Indiegogo page could not be loaded (2026-09-07).
  distribution:
  - crowdfunding
  - kit
  where: Indiegogo crowdfunding campaign; rewards (kit or assembled badge) were picked up in person at DEF CON 31.
make_your_own:
  open_source: true
  hardware_url: https://github.com/gowenrw/future_badge
  firmware_url: https://github.com/gowenrw/future_badge
  eda_tool: KiCad
  notes: GitHub repo (gowenrw/future_badge) contains art, code, KiCad (6.x) EDA files, and docs; licensed MIT. The maker's own project site (futurebadge.altbier.us) hosts assembly instructions, schematics and build videos. The compiled CTF challenge library itself is not open source; everything else is.
links:
- label: www.indiegogo.com/projects/future-badge-wearable-art-defcon-badgelife#
  url: https://www.indiegogo.com/projects/future-badge-wearable-art-defcon-badgelife#/
  kind: store
- label: Alt_Bier's YouTube channel
  url: https://www.youtube.com/@alt_bier_hacker
  kind: social
- label: futurebadge.altbier.us
  url: https://futurebadge.altbier.us/
  kind: website
- label: gowenrw/future_badge (GitHub)
  url: https://github.com/gowenrw/future_badge
  kind: repo
- label: 'Badge Review: Future Badge by @alt_bier (t.fish)'
  url: https://tdot.fish/2024/02/25/futurebadge
  kind: article
- label: 'Walkthru: Future Badge by @alt_bier (t.fish)'
  url: https://tdot.fish/2024/02/25/futurebadge-walkthru
  kind: article
images:
- file: assets/images/badges/dc31/the-future-will-prevail/97d4bb34aa.jpg
  source: https://www.indiegogo.com/projects/future-badge-wearable-art-defcon-badgelife
  credit: Richard Gowen / Future Badge team
  caption: Future Badge campaign cover image on Indiegogo
- file: assets/images/badges/dc31/the-future-will-prevail/46f873c7cc.jpg
  source: https://www.indiegogo.com/projects/future-badge-wearable-art-defcon-badgelife
  credit: Richard Gowen / Future Badge team
  caption: Assembled Future Badge worn at DEF CON 31, showing the DeLorean / Back to the Future artwork and edge LEDs
- file: assets/images/badges/dc31/the-future-will-prevail/3ca8dc5546.jpg
  source: https://futurebadge.altbier.us/
  credit: Alt_Bier
  caption: Future Badge hero shot, Back to the Future themed DEF CON 31 badge
- file: assets/images/badges/dc31/the-future-will-prevail/f8b0f4b690.jpg
  source: https://tdot.fish/2024/02/25/futurebadge
  credit: t.fish
  caption: PCB detail showing assembly silkscreen and stacked-board design
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- This appears to be a duplicate of the existing entry dc31-the-future-will-prevail (same maker Alt_Bier, same badge, same DEF CON 31 Indiegogo campaign). That entry additionally credits Richard Gowen (campaign owner) and Brian Culver as team members, and records pricing/quantity ($60 kit / $100 assembled; 120 kits offered, 65 claimed; 35 assembled, sold out) from an archived Indiegogo snapshot.
status: released
sources:
- kind: sheet
  event: dc31
  row: 3
  updated: '2023-02-14'
- kind: url
  url: http://web.archive.org/web/20230927213642/https://www.indiegogo.com/projects/future-badge-wearable-art-defcon-badgelife
  title: 'Future Badge: Wearable Art DEFCON #Badgelife (Indiegogo, Wayback Machine snapshot)'
  accessed: '2026-09-07'
  note: Maker's own campaign page (live site returns a Cloudflare challenge). Confirmed title, creator (Richard Gowen) and team (Alt_Bier, Brian Culver), tagline, perk pricing/quantities/claims, funding total and dates, and campaign photos.
- kind: url
  url: https://futurebadge.altbier.us/
  title: Future Badge (The Future will Prevail)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc31''. Maker''s own project page: theme, DeLorean/capacitive touch concept, ESP32, WiFi, 9V battery, open-source GitHub repo link, hero image.'
- kind: url
  url: https://github.com/gowenrw/future_badge
  title: gowenrw/future_badge
  accessed: '2026-09-07'
  note: Confirms repo contains art/code/eda(KiCad 6.x)/docs for the DC31 badge; license set to MIT.
- kind: url
  url: https://tdot.fish/2024/02/25/futurebadge
  title: 'Badge Review: Future Badge by @alt_bier'
  accessed: '2026-09-07'
  note: 'Third-party hands-on review: detailed LED breakdown (4 WS2812 + 4 red/yellow + 4 blue + 2 white), 9V battery runtime, two-PCB sandwich construction, WiFi AP CTF mode details ("FUTURE-BADGE" SSID), lanyard, eBay availability as of 2024-02-25, image URLs.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The live Indiegogo page is behind a Cloudflare challenge that blocked automated fetches; a 2023-09-27 Wayback Machine snapshot of the maker's own campaign page supplied the structured campaign data (perks, funding, team, photos) used here. No project write-up/story text, GitHub repo, or Hackaday.io page was found describing the electronics, so MCU, LED count/driver, power source, and open-source status are left blank rather than guessed. A live web search could not be run this session (search budget exhausted for the session), so this could not be cross-checked against press coverage or forum posts. Alt_Bier, the name on the community sheet, appears in the archived page as a team member (YouTube handle alt_bier_hacker) alongside campaign owner Richard Gowen and team member Brian Culver. Merged with duplicate entry 'Future Badge (The Future will Prevail)' (dc31-future-badge-the-future-will-prevail).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc31/future-badge-the-future-will-prevail/
model:
  file: assets/models/dc31/the-future-will-prevail.glb
  method: kicad
  source_file: eda/future_badge/future_badge.kicad_pcb
  generated: '2026-09-07'
  bytes: 607020
---

The Future will Prevail was funded through a June–July 2023 Indiegogo campaign ("Future Badge: Wearable Art DEFCON #Badgelife") run by Richard Gowen with team members Alt_Bier and Brian Culver, aimed at DEF CON 31. The badge carries a laser-engraved Back to the Future scene — a DeLorean over a flame trail with a lightning bolt, plus a time-circuit-style trio of date readouts — on a navy PCB with gold traces, and RGB LEDs light up the flame and lightning accents. It clips on with carabiner-style hooks rather than a lanyard.

The campaign offered a $60 DIY kit (solder-it-yourself, 120 available, 65 claimed) and a $100 fully-assembled badge (35 available, all claimed). It closed having raised $7,400 against a $5,000 goal from 100 backers, and rewards were handed out in person at DEF CON 31. No hardware or firmware files, MCU, or detailed electronics specs were found in the sources checked, so those fields are left blank pending further research.

## Notes merged from the duplicate entry "Future Badge (The Future will Prevail)"

The Future Badge is a Back to the Future themed electronic badge Alt_Bier made for DEF CON 31, whose conference theme, "The Future Will Prevail," suggested the time-traveling DeLorean. The badge is cut to an oblong, movie-ticket-like shape and its front artwork — the Hill Valley courthouse clock tower, a sports almanac, Doc Brown, a time-machine dashboard readout, and a silver DeLorean hitting 88 MPH — is built from two stacked PCBs with backlit solder-mask voids, hiding the electronics between the boards while highlighting the art.

An ESP32 drives the badge's lighting (WS2812 RGB LEDs plus discrete red/yellow, blue, and white LEDs) and a capacitive-touch pad on the silver DeLorean toggles effects such as a color-changing logo, flickering tire tracks, and strobing lightning. Holding that touch pad for about thirty seconds switches the badge into a WiFi access-point mode, broadcasting an SSID of "FUTURE-BADGE" that hosts a hidden, Back to the Future themed CTF puzzle. The badge runs on a 9V battery (two included) for roughly seven to eight hours and ships as a mostly through-hole DIY solder kit, with silkscreened assembly guidance directly on the PCB, alongside fully-assembled units.

It was distributed through an Indiegogo crowdfunding campaign, with rewards picked up at DEF CON 31; a hands-on review from February 2024 noted a few units still available afterward through the maker's eBay store. All hardware and firmware (save the compiled CTF challenge library) are published on GitHub under the MIT license, with build videos and documentation on the maker's own project site.

This entry closely tracks another archive entry, `dc31-the-future-will-prevail`, for what appears to be the same badge and campaign; see that entry for pricing and quantity details pulled from an archived Indiegogo snapshot.
