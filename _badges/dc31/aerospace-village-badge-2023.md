---
title: The Wright Stuff
id: dc31-aerospace-village-badge-2023
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: Aerospace Village
  url: https://www.aerospacevillage.org/
  role: organizer/publisher
- name: flysurreal.com
  role: artwork
summary: The main Aerospace Village badge for DEF CON 31, depicting the Wright brothers in spacesuits riding a satellite to mark 120 years of powered flight. It runs on an ESP32 with hidden Easter eggs and one SAO expansion slot.
functions: 'Hides "numerous" Easter eggs for attendees to find; built around an ESP32 for "modern technology and interactivity" per the maker''s page. Firmware and PCB source live in the Badge/WrightSpace folder of the linked repo (Arduino sketch plus a KiCad PCB).'
look:
  colors:
  - black
  - silver
  themes:
  - space
  - pop culture
  - village badge
  form_factor: pcb badge
tech:
  mcu: ESP32
  leds:
    count: null
    type: RGB
    note: RGB LEDs light the satellite's antenna dish in the maker's photo; exact count not stated in sources.
  display: none
  connectivity: []
  battery: null
  sao_version: null
  sao_ports: 1
get_one:
  price: minimum $80 donation
  price_usd: 80
  quantity: ''
  availability: unknown
  availability_note: 'Checked 2026-09-07: no working storefront found; it was sold in person only.'
  distribution:
  - village
  where: Available in person at DEF CON 31 (2023) at the Aerospace Village for a minimum $80 donation to the Village.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/AerospaceVillage/avBadge_2023/tree/main/Badge/WrightSpace
  firmware_url: https://github.com/AerospaceVillage/avBadge_2023/tree/main/Badge/WrightSpace/Arduino
  eda_tool: KiCad
links:
- label: github.com/AerospaceVillage/avBadge_2023
  url: https://github.com/AerospaceVillage/avBadge_2023
  kind: repo
- label: DC31 Badge | Aerospace Village
  url: https://www.aerospacevillage.org/dc31-badge
  kind: website
images:
- file: assets/images/badges/dc31/aerospace-village-badge-2023/05c9cc0598.jpg
  source: "https://www.aerospacevillage.org/dc31-badge"
  credit: "Aerospace Village / art by flysurreal.com"
  caption: "The Wright Stuff: the Wright brothers in spacesuits riding a satellite, with RGB LEDs lit at the satellite's antenna dish"
contact:
  email: village@aerospacevillage.org
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- 'The linked repo (avBadge_2023) actually covers two distinct DC31 badges plus SAOs: "The Wright Stuff" (this entry, the general $80-donation village badge, ESP32, one SAO slot) and "The Wright Flyer" (a separate 50-unit limited-edition 5th-anniversary badge, ESP32-S2, two counter-rotating propellers, two SAO slots, sold on Tindie for $250) — see research.notes and other_items_found.'
status: released
sources:
- kind: url
  url: https://github.com/AerospaceVillage/avBadge_2023
  title: Aerospace Village Badge 2023
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc31''. README confirms the repo covers two badges (Wright Flyer, Wright Stuff) and several SAOs; WrightSpace subfolder has a KiCad PCB and an Arduino sketch.'
- kind: url
  url: https://www.aerospacevillage.org/dc31-badge
  title: DC31 Badge | Aerospace Village
  accessed: '2026-09-07'
  note: Maker's own page describing both DC31 badges in detail; source for summary, functions, MCU, price/donation amount, distribution, artwork credit, and the photo saved to images.
- kind: url
  url: https://www.hackster.io/news/aerospace-village-celebrates-120-years-of-flight-with-this-limited-edition-commemorative-badge-9b48c147144c
  title: 'Aerospace Village Celebrates 120 Years of Flight with This Limited Edition Commemorative Badge'
  accessed: '2026-09-07'
  note: Press coverage; confirmed the Wright Flyer is the separate 50-unit limited edition (used for other_items_found, not this entry).
- kind: url
  url: https://www.tindie.com/products/aero_village/aerospace-village-5th-anniversary-badge-for-dc-31/
  title: Aerospace Village 5th Anniversary Badge for DC 31 (Tindie)
  accessed: '2026-09-07'
  note: Storefront for the separate Wright Flyer badge ($250, ESP32-S2, two SAO slots); confirms this is a different item from the one documented in this entry.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched aerospacevillage.org/dc31-badge and the avBadge_2023 repo/WrightSpace folder and confirmed title, maker/artist credit, summary, MCU (ESP32), one SAO slot, $80 minimum donation, distribution, functions quotes ("numerous intriguing Easter eggs", "modern technology and interactivity"), 120-years/5th-anniversary framing, KiCad+Arduino file structure, open-source status, and the saved photo (which does show pink/RGB LEDs lit in the satellite dish, matching the caption). Removed "retro computer" and "security" from look.themes: neither term appears on the maker''s page or in any source and neither is visually supported by the artwork; replaced with "village badge", which the source explicitly supports (general-admission badge for the Village). The repo README and the maker''s own dc31-badge page make clear this GitHub repo covers two separate badges plus SAOs. This entry was written for "The Wright Stuff," the general-admission $80-donation village badge (ESP32, one SAO slot), since it best matches a single generic "Aerospace Village Badge 2023" title. "The Wright Flyer" is a distinct 50-unit limited-edition badge (ESP32-S2, two SAO slots, propellers, sold via Tindie for $250) and is reported separately as a candidate for its own entry. LED count, exact PCB colors beyond black/silver, and battery/power details were not stated in any source found and are left empty rather than guessed. No secondary storefront or attendee report of the Wright Stuff badge was found beyond the maker''s own page.'
last_modified_date: '2026-09-07'
---

"The Wright Stuff" is the Aerospace Village's general-admission badge for DEF CON 31 (2023), marking the 120th anniversary of the Wright brothers' first powered flight. The artwork, credited to flysurreal.com, shows the Wright brothers in spacesuits riding a satellite through space, with RGB LEDs lighting the satellite's antenna dish. It runs on an ESP32 and, per the maker, hides "numerous" Easter eggs for attendees to find, alongside one SAO expansion header. It was distributed in person at the Village for a minimum $80 donation rather than sold through a storefront.

Hardware and firmware for the badge are open source, published in the `Badge/WrightSpace` folder of the Aerospace Village's `avBadge_2023` GitHub repository (a KiCad PCB and an Arduino sketch). That same repository also contains a second, separate DC31 badge — "The Wright Flyer," a 50-unit limited edition released for the Village's 5th anniversary, built around an ESP32-S2 with two counter-rotating propellers and two SAO slots, sold through Tindie for $250 — plus a number of standalone SAOs. Because the repo bundles multiple distinct items under one name, this entry covers only the Wright Stuff badge; the Wright Flyer is flagged separately as it likely warrants its own archive entry.
