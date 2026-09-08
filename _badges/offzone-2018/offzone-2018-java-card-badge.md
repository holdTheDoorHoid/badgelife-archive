---
title: OFFZONE 2018 Java Card Badge
id: offzone-2018-offzone-2018-java-card-badge
layout: badge
parent: OFFZONE 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: offzone-2018
year: 2018
makers:
- name: BI.ZONE
summary: A bank-card-shaped conference badge with an embedded Java Card chip, used as the interactive centerpiece of OFFZONE 2018 before BI.ZONE moved to PCB badges the following year.
functions: Runs Java Card applets accessed through a USB smart-card reader; attendees played a Battle City ("Tanks") clone against the card and a Sokoban-style puzzle, plus other small challenges.
look:
  colors: []
  shape: card
  themes:
  - security
  - crypto
tech:
  mcu: Java Card chip
  leds: null
  display: none
  connectivity:
  - usb
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to OFFZONE 2018 attendees.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: habr.com/ru/articles/707392
  url: https://habr.com/ru/articles/707392/
  kind: article
images:
- file: assets/images/badges/offzone-2018/offzone-2018-java-card-badge/3d8122f4aa.jpg
  source: "https://habr.com/ru/articles/707392/"
  credit: "BI.ZONE"
  caption: "The 2018 Java Card badge, bank-card sized with embossed text"
- file: assets/images/badges/offzone-2018/offzone-2018-java-card-badge/fa35192279.jpg
  source: "https://habr.com/ru/articles/707392/"
  credit: "BI.ZONE"
  caption: "Testing the embossed card in an old card-imprinter machine"
contact: {}
notes:
- Sweep found this via a search snippet; the article it points to fully confirms the item (BI.ZONE retrospective on OFFZONE badge history, published 2022). Sweep's one-line summary was accurate.
status: released
sources:
- kind: url
  url: https://habr.com/ru/articles/707392/
  title: "Как в BI.ZONE разрабатывают PCB-бейджи для конференции OFFZONE"
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''OFFZONE 2018''.'
- kind: url
  url: https://habr.com/ru/articles/707392/
  title: "Как в BI.ZONE разрабатывают PCB-бейджи для конференции OFFZONE"
  accessed: '2026-09-08'
  note: BI.ZONE retrospective article (Habr, Dec 2022) with a dedicated 2018 section confirming the Java Card badge, its Tanks/Sokoban applets, USB reader use, and embossed bank-card design; also the source of both saved images.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Only source found is this one BI.ZONE-authored retrospective article (third-party outlet Habr, but written from BI.ZONE's own account and quotes their team) — no independent maker page, storefront, or press coverage exists for a badge this old. No price, quantity, MCU/chip model, or design-file details were given; distribution is inferred as a free conference giveaway since no sale is mentioned anywhere.
last_modified_date: '2026-09-08'
---

In 2018, before BI.ZONE started making PCB badges for its OFFZONE security conference in Moscow, attendees received a bank-card-shaped badge built around a Java Card chip. It looked and felt like a real debit or credit card, right down to embossed, raised-print lettering and a card number that validated against the standard bank-card checksum algorithm — a deliberate wink at how much conference fraud involves stolen payment cards.

The card's interactive element lived in its Java Card applets. Attendees found a USB smart-card reader at the venue and used it to run small programs stored on the chip, including a Battle City-style "Tanks" game played against the card itself and a Sokoban-like puzzle, along with other minor challenges. It predates OFFZONE's later switch to custom PCB badges (starting with the 2019 floppy-disk badge), making it the earliest known OFFZONE attendee badge.

No pricing, production-quantity, or open hardware/firmware details have surfaced; the only source found is a 2022 BI.ZONE retrospective published on Habr that briefly profiles each year's OFFZONE badge.
