---
title: Application Security Challenge Badge
id: saintcon-2023-application-security-challenge-badge
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: SHIFTY
summary: A SAINTCON 2023 contest minibadge earned by finding and fixing vulnerabilities in a sample Flask web app.
functions: 'Awarded for completing the AppSec Challenge: clone a vulnerable Flask app, find and fix its vulnerabilities, and submit the fixed code for a score.'
look:
  colors:
  - yellow
  - black
  shape: rectangle
  themes:
  - security
  - ctf
  - insect
  form_factor: pcb badge
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: single 1206 LED (D1), lights via the badge's chain header rather than an MCU
  display: none
  connectivity: []
  battery: powered by host badge/chain
  sao_version: none
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - contest
  where: 'Earned at the SAINTCON 2023 AppSec community booth by completing the "biggest challenge" — fixing all vulnerabilities in a sample Flask application.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  kind: doc
images:
  - file: assets/images/badges/saintcon-2023/application-security-challenge-badge/front.jpg
    source: "https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf"
    credit: "SHIFTY / SAINTCON"
    caption: "Front of the badge, AppSec Challenge artwork"
  - file: assets/images/badges/saintcon-2023/application-security-challenge-badge/back.jpg
    source: "https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf"
    credit: "SHIFTY / SAINTCON"
    caption: "Back of the badge showing LED, resistor, and SAINTCON 2023 SHIFTY silkscreen"
contact: {}
notes:
- 2023 Contest minibadge for the AppSec vulnerability-fixing challenge against a sample Flask app. Found by the event-year sweep, task saintcon-2023.
- 'The official SAINTCON 2023 Minibadge Guide lists this as a "CONTEST MINIBADGE" titled "APPLICATION SECURITY CHALLENGE BADGE" — matches the sweep''s title exactly.'
status: released
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  title: Application Security Challenge Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2023); event read as ''saintcon-2023''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  title: 2023 Minibadge Guide (10.31.2023), p.51 — Application Security Challenge Badge
  accessed: '2026-09-10'
  note: 'Confirmed the badge exists as a distinct minibadge (companion to the separate "Application Security Community Badge"): designer SHIFTY, contest distribution (free, earned by completing the Flask vulnerability challenge), difficulty beginner, rarity uncommon, parts 1206 LED + 1206 resistor + FR4 PCB + 2-pin pin headers, front/back artwork captured as images.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'No price/quantity/open-source info given — it was a free contest reward, not sold, and the guide does not state a print run. No maker URL found for SHIFTY (SAINTCON''s minibadge design team/brand, credited across dozens of 2023-2025 SAINTCON minibadges) beyond this PDF. No separate storefront, repo, or photo outside the official guide was found.'
last_modified_date: '2026-09-10'
---

The Application Security Challenge Badge is a SAINTCON 2023 contest minibadge designed by SHIFTY, given to attendees who completed the AppSec community's "biggest challenge": cloning a sample Python Flask web application, finding its vulnerabilities, fixing them, and submitting the corrected code for a score. It was rated beginner difficulty and uncommon rarity in the official Minibadge Guide, and attendees who wanted help were pointed to the separate AppSec community booth to learn scanning tools.

Electrically it is a simple, unpowered minibadge: a single 1206 LED and 1206 resistor on an FR4 PCB, wired through 2-pin pin headers so it lights when chained to a powered badge (no onboard MCU, battery, or display). The board art is a stylized dark-winged insect over "APPSEC CHALLENGE" text on a yellow background; the back carries the LED, resistor, and a "SAINTCON 2023 / SHIFTY" silkscreen.

It was distributed for free as a contest reward rather than sold, and no separate storefront, repository, or design-file release was found for it.
