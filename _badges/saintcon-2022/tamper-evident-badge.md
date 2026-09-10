---
title: Tamper Evident Badge
id: saintcon-2022-tamper-evident-badge
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: Jup1t3r
summary: A simple SAINTCON 2022 minibadge handed out for interacting with the Tamper Evident Contest booth.
functions: 'No interactivity beyond soldering: 3 LEDs light from a single resistor, wired straight across the badge''s 4x 2-position headers with no microcontroller.'
look:
  colors: [yellow, brown]
  shape: null
  themes: [security, learn to solder]
tech:
  mcu: none
  leds:
    count: 3
    type: discrete
    note: 3 LEDs (D1-D3) and one resistor (R1), single-pad hand-soldered
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: free
  distribution: [free_drop]
  where: Given out at the Tamper Evident Contest booth at SAINTCON 2022 for attempting to defeat one of the tamper-evident devices on display there.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  kind: doc
- label: 'CONTEST - Tamper Evident - SAINTCON (archived 2022 page)'
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/tamper/
  kind: website
images:
  - file: assets/images/badges/saintcon-2022/tamper-evident-badge/front.jpg
    source: "https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf"
    credit: "Jup1t3r / SAINTCON"
    caption: "Front of the Tamper Evident minibadge, page 30 of the SAINTCON 2022 MiniBadge Assembly Guide"
  - file: assets/images/badges/saintcon-2022/tamper-evident-badge/back.jpg
    source: "https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf"
    credit: "Jup1t3r / SAINTCON"
    caption: "Back of the PCB showing the 3 LEDs, resistor, and 4x 2-position headers"
contact: {}
notes:
- Sweep title read "Tamper Evident BADGE" (all caps BADGE); the guide's own heading capitalizes it "Tamper Evident Badge" on the page banner but "BADGE" in running text - kept the natural-case form as the title.
- Difficulty "beginner", rarity "uncommon" per the assembly guide; these aren't archive fields so noted here instead.
status: released
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: Tamper Evident BADGE
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2022); event read as ''saintcon-2022''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: SAINTCON MiniBadge Assembly Guide 2022 (page 30)
  accessed: '2026-09-10'
  note: 'Confirmed the badge exists (PDF text-extracted with pdftotext, page rendered with pdftoppm since WebFetch could not parse the binary PDF directly): designer Jup1t3r, given for interacting with the Tamper Evident Contest booth, difficulty beginner / rarity uncommon, parts list (3 LEDs, 1 resistor, 4x 2-position headers), and the front/back board images.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/tamper/
  title: 'CONTEST - Tamper Evident - SAINTCON'
  accessed: '2026-09-10'
  note: 'Archived 2022 contest page confirming Tamper Evident is a physical-security seal-bypass contest, and that a minibadge is earned by attempting the booth challenge (no further badge specifics given here).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed real via the 2022 MiniBadge Assembly Guide PDF (page 30) and the archived Tamper Evident contest page. No maker profile, storefront, or social post found for Jup1t3r beyond the SAINTCON guide credits, so quantity made and open-source status are unknown. Price/quantity left empty since the guide gives neither a run size nor a dollar price (it was a free contest-participation give-away, not sold).'
last_modified_date: '2026-09-10'
---

The Tamper Evident Badge is a SAINTCON 2022 minibadge designed by Jup1t3r, distributed at the convention's Tamper Evident Contest booth to anyone who attempted to defeat one of the tamper-evident seals or devices on display there — a taste of the full multi-day physical-security contest that ran the same week. The badge itself is intentionally simple: a yellow PCB shaped like a rumpled, eye-peeking burlap sack with "TAMPER EVIDENT" lettered across the front, and a beginner-difficulty back side carrying three LEDs (D1-D3), one resistor (R1), and four 2-position headers, all single-pad hand-solderable with no microcontroller or programmed behavior.

The SAINTCON 2022 MiniBadge Assembly Guide lists it as "uncommon" rarity among that year's minibadge set. Beyond the guide's own credit line and the contest's archived description, no separate maker page, repository, or storefront for the badge was found, so details like total quantity produced and whether the design files were ever published remain unknown.

