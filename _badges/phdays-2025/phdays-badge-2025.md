---
title: PHDays Badge 2025
id: phdays-2025-phdays-badge-2025
layout: badge
parent: Phdays Fest 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: phdays-2025
year: 2025
makers:
- name: Positive Labs / Positive Technologies
summary: 'A second-generation electronic conference badge with a 10x10 pixel LED matrix display, built on ESP32, sold as festival merch at PHDays Fest 2025.'
functions: 'Displays preset or custom images and animations on its 10x10 pixel matrix, and plays RTTTL ringtone-format melodies through a built-in speaker (with an on-device RTTTL editor). Content is set over Wi-Fi via a web interface.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: ESP32
  leds:
    count: null
    type: null
    note: '10x10 pixel LED matrix behind light guides/diffusing film, similar to the 2024 badge'
  display: LED matrix 10x10
  connectivity:
  - wifi
  battery: null
  sao_version: null
get_one:
  price: '7331 RUB'
  price_usd: null
  quantity: ''
  availability: available
  availability_note: 'Listed "in stock" on positivemerch.com as of 2026-09-08; sold at the festival May 22-24, 2025 and online from June 1, 2025'
  distribution:
  - purchase
  where: 'Sold at PHDays Fest 2025 (Moscow, Luzhniki) and afterward through the official Positive Merch online store'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/Ushinbuy/PHD_Badge_2025
  firmware_url: https://github.com/nlef/PHDays-Badge
  eda_tool: null
links:
- label: habr.com/ru/companies/pt/articles/890296
  url: https://habr.com/ru/companies/pt/articles/890296/
  kind: website
- label: 'Positive Merch: PHDays Fest 2025 badge product page'
  url: https://positivemerch.com/product/elektronnyj-bejdzh-phdays-fest-2025/
  kind: store
- label: 'GitHub: nlef/PHDays-Badge (firmware)'
  url: https://github.com/nlef/PHDays-Badge
  kind: repo
- label: 'GitHub: Ushinbuy/PHD_Badge_2025 (3D/housing models)'
  url: https://github.com/Ushinbuy/PHD_Badge_2025
  kind: repo
images:
  - file: assets/images/badges/phdays-2025/phdays-badge-2025/27b8a3bb86.jpg
    source: "https://positivemerch.com/product/elektronnyj-bejdzh-phdays-fest-2025/"
    credit: "Positive Merch / Positive Labs"
    caption: "PHDays Fest 2025 badge, front view"
  - file: assets/images/badges/phdays-2025/phdays-badge-2025/0ca8be639c.jpg
    source: "https://positivemerch.com/product/elektronnyj-bejdzh-phdays-fest-2025/"
    credit: "Positive Merch / Positive Labs"
    caption: "PHDays Fest 2025 badge, alternate view"
contact: {}
notes:
- Second-generation PHDays badge with redesigned housing, new features and expanded customization, made for PHDays Fest 2025 (May 22-24). Found by the event-year sweep, task con-phdays.
- 'The habr.com article the sweep cited is actually a retrospective on the first-generation PHDays Badge 2024 (built by Positive Labs / Nikolay for PHDays Fest 2 in May 2024); it only mentions the 2025 badge as a planned sequel. This entry''s facts about the 2025 badge itself come from the Positive Merch store listing and the linked GitHub repos, not from the habr article.'
status: released
sources:
- kind: url
  url: https://habr.com/ru/companies/pt/articles/890296/
  title: PHDays Badge 2025
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''PHDays Fest 3 2025''. On inspection this article covers the 2024 badge, only mentioning a 2025 sequel as planned.'
- kind: url
  url: https://positivemerch.com/product/elektronnyj-bejdzh-phdays-fest-2025/
  title: 'Электронный бейдж PHDAYS FEST 2025 — Positive Merch'
  accessed: '2026-09-08'
  note: 'Official store listing for the 2025 badge; confirms it exists as a distinct product, gives MCU (ESP32), display (10x10), speaker/RTTTL feature, price, and availability. Source of both saved images.'
- kind: url
  url: https://github.com/nlef/PHDays-Badge
  title: 'nlef/PHDays-Badge (GitHub)'
  accessed: '2026-09-08'
  note: 'Firmware repo for the PHDays Badge line (10x10 display, RTTTL playback/editor); links out to a separate repo for the 2025 badge''s 3D/housing models.'
- kind: url
  url: https://github.com/Ushinbuy/PHD_Badge_2025
  title: 'Ushinbuy/PHD_Badge_2025 (GitHub)'
  accessed: '2026-09-08'
  note: '3D model / housing repo specifically for the 2025 badge, linked from the firmware README.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed the 2025 badge is a real, distinct, released product (not just a plan) via the official Positive Merch listing and GitHub repos. Could not confirm LED count/type, battery, or quantity made for the 2025 revision specifically (the 2024 badge used ~100 LEDs and had ~1,000 units made, per the habr article, but that is not stated to carry over unchanged). No confirmation of what changed in the housing redesign beyond the sweep''s own note. eda_tool and gerbers/BOM not found.'
last_modified_date: '2026-09-08'
---

The PHDays Badge 2025 is the second generation of Positive Labs' interactive conference badge for Positive Technologies' PHDays Fest, following a first badge made for PHDays Fest 2 in 2024. Like its predecessor, it is built around an ESP32 and centers on a 10x10 pixel LED matrix that can show preset or custom images and animations; the 2025 revision adds a built-in speaker that plays RTTTL-format melodies, including an on-device RTTTL editor. Content, images, animations, and sounds are set through a Wi-Fi web interface.

The badge was sold as official festival merchandise at PHDays Fest 2025 (Moscow, Luzhniki sports complex, May 22-24, 2025) for 7,331 RUB, and continued to be sold afterward through the Positive Merch online store. Firmware for the PHDays Badge line is open source on GitHub (nlef/PHDays-Badge), and the 2025 badge's 3D-printed housing and structural parts are published in a separate repo (Ushinbuy/PHD_Badge_2025) linked from the firmware README.

Note on sourcing: the page the discovery sweep originally cited for this entry is actually a Habr retrospective about the 2024 badge's development, which only mentions a 2025 sequel as a stated plan. That the 2025 badge was in fact made, sold, and is a distinct product was confirmed separately through Positive Technologies' own merch store and the linked GitHub repositories.
