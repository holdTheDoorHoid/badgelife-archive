---
title: CrikeyCon 8 Badge
id: crikeycon-2022-crikeycon-8-badge
layout: badge
parent: CrikeyCon 2022
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: crikeycon-2022
year: 2022
makers:
- name: CrikeyCon
summary: A simple, learn-to-solder conference badge for CrikeyCon 8 (Brisbane, 2022) built around three LEDs and a 2x3 SAO header.
functions: 'No programmable behavior: it is a passive LED circuit, lit by a coin-cell or by power drawn through its SAO header once an add-on SAO is attached.'
look:
  colors: []
  shape: null
  themes:
  - learn to solder
  - sao
  - kit
tech:
  mcu: none
  leds:
    count: 3
    type: discrete
    note: Three blue 1206 surface-mount LEDs with current-limiting resistors; the build guide offers a choice of normal or reverse-mount LED orientation.
  display: none
  connectivity: []
  battery: CR2025/CR2032 coin cell (holder optional), or powered via a device plugged into the badge's SAO header
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: crikeycon.com/archive/2022-dieiyadhfielsklkjjkj/badge.html
  url: https://crikeycon.com/archive/2022-dieiyadhfielsklkjjkj/badge.html
  kind: website
- label: 'badge.gallery: CrikeyCon 8 Badge'
  url: https://badge.gallery/badges/crikeycon-8-badge
  kind: article
images: []
contact: {}
notes:
- Official CrikeyCon 8 (2022) conference badge with a simple coin-cell LED circuit and a 2x3 SAO header for add-on boards, per CrikeyCon's own archived soldering guide. Found by the event-year sweep, task con-kiwicon.
status: released
sources:
- kind: url
  url: https://crikeycon.com/archive/2022-dieiyadhfielsklkjjkj/badge.html
  title: CrikeyCon 8 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-kiwicon); event read as ''CrikeyCon 8 2022''.'
- kind: url
  url: https://badge.gallery/badges/crikeycon-8-badge
  title: CrikeyCon 8 Badge - Hacker Con Badges
  accessed: '2026-09-10'
  note: Third-party dossier that quotes CrikeyCon's own build guide in detail (power options, LED type/count, coin-cell holder, SAO header, no firmware) and confirms location (Brisbane) and event; it explicitly notes it has no rights-cleared photo of the badge.
- kind: url
  url: https://badge.gallery/addons/crikeycon-8-badge/sao-header-and-led-soldering-kit
  title: SAO header and LED soldering kit - Hacker Con Badges
  accessed: '2026-09-10'
  note: Corroborates the same build-guide details (coin-cell power, 2x3 SAO-header power, three LEDs, resistors, optional LED mounting orientation).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: >-
    The maker's own page (crikeycon.com/archive/2022-dieiyadhfielsklkjjkj/badge.html) returns a
    Cloudflare interactive challenge to automated fetches, so it could not be read directly; a
    Wayback Machine lookup also failed to return a matching snapshot. Confirmation instead comes
    from a search-engine snippet of that page plus a third-party badge dossier (badge.gallery) that
    quotes the same build guide at length, so confidence is medium rather than high. No MCU/firmware
    is implied anywhere; the badge is a passive LED circuit, consistent with "none" for tech.mcu.
    Price, quantity made, and distribution/availability are not stated in any source found, so those
    fields are left empty. No usable photo of the badge itself was found; badge.gallery notes it
    deliberately omits an image for the same reason (no rights-cleared photo located). Left status
    as "released" rather than "listed" since the build guide is written for attendees who already
    have the badge in hand, implying it was actually distributed at CrikeyCon 8.
last_modified_date: '2026-09-10'
---

CrikeyCon 8's 2022 conference badge is a deliberately simple, learn-to-solder board rather than a
programmable device: three blue 1206 surface-mount LEDs and their current-limiting resistors, wired
to run either off an optional CR2025/CR2032 coin cell or off power drawn through the badge's 2x3
(SAO v2) header when a Simple Add-On is plugged in. CrikeyCon's own archived build guide walks
attendees through component selection and soldering, including a choice between normal and
reverse-mount LED orientation, and frames the part choices around avoiding through-hole components
that could snag on clothing.

No firmware or microcontroller is described anywhere in the sources found — this is a passive
analog circuit whose only "feature" is lighting up, with the SAO header serving as the badge's
extensibility point for other CrikeyCon-compatible add-ons rather than as a data interface.

The maker's own build-guide page could not be fetched directly (it sits behind a Cloudflare
challenge), so the details above are drawn from a search-engine snippet of that page together with
a third-party badge dossier (badge.gallery) that quotes the guide's content in detail. No photo of
the badge could be located; price, production quantity, and how (or whether) it was distributed
beyond CrikeyCon 8 attendees are not stated in any source found.
