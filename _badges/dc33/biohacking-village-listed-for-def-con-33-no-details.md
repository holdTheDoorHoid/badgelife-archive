---
title: Distiller BHV Edition
id: dc33-biohacking-village-listed-for-def-con-33-no-details
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
nav_title: Biohacking Village (listed for DEF CON 33, no details)
type: badge
event: dc33
year: 2025
makers:
- name: PamirAI
  url: https://pamir.ai
  role: hardware and software (Distiller platform)
- name: SolaSec
  role: physical design, 3D-printed enclosure, and assembly
- name: Biohacking Village
  url: https://villageb.io
  role: commissioning village
summary: The DEF CON 33 Biohacking Village badge, built around a Raspberry Pi Compute
  Module 5 running PamirAI's Distiller platform, gives the wearer a pocket-sized,
  fully offline AI medical chatbot that listens and talks back.
functions: Runs local LLMs entirely on-device (no internet connection) as a voice-driven
  medical-question chatbot; listens via a built-in microphone and responds with
  treatment-idea style answers on an e-ink screen.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - sci-fi
tech:
  mcu: Raspberry Pi Compute Module 5 (RP2040 as board manager)
  leds:
    count: null
    type: RGB
    note: A back status LED plus a side-firing RGB LED that stays lit after shutdown;
      LED colors are customizable via the on-badge AI assistant.
  display: e-ink (non-touch, navigated with physical buttons)
  connectivity:
  - wifi
  battery: USB-C, requires a USB-PD charger rated 9V/3A minimum; auto-shuts down
    below 1% battery and won't power on below 3%
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Given out at the DEF CON 33 Biohacking Village in Las Vegas, August 2025;
    exact distribution method (all attendees vs. contest/volunteer only) not stated
    in sources found.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/Pamir-AI/distiller-cm5-sdk
  eda_tool: null
  notes: PamirAI's Distiller SDK (Python, Apache-2.0) is public on the main branch;
    a "BHV branch" of both distiller-cm5-sdk and distiller-cm5-python is referenced
    in search results but was not directly confirmed by fetching a branch listing.
    No hardware/Gerber files were found.
links:
- label: Raspberry Pi blog post
  url: https://www.raspberrypi.com/news/creating-the-most-advanced-event-badge-yet-for-the-biohacking-village-at-def-con/
  kind: article
- label: Distiller BHV Edition user guide
  url: https://docs.pamir.ai/bhv
  kind: doc
- label: Biohacking Village badges page
  url: https://villageb.io/Badges
  kind: website
- label: distiller-cm5-sdk (GitHub)
  url: https://github.com/Pamir-AI/distiller-cm5-sdk
  kind: repo
images:
- file: assets/images/badges/dc33/biohacking-village-listed-for-def-con-33-no-details/1c5214ceee.jpg
  source: "https://www.raspberrypi.com/news/creating-the-most-advanced-event-badge-yet-for-the-biohacking-village-at-def-con/"
  credit: "SolaSec / Raspberry Pi"
  caption: "The Distiller BHV Edition badge, showing enclosure and e-ink screen"
- file: assets/images/badges/dc33/biohacking-village-listed-for-def-con-33-no-details/d46094e0cf.jpg
  source: "https://www.raspberrypi.com/news/creating-the-most-advanced-event-badge-yet-for-the-biohacking-village-at-def-con/"
  credit: "SolaSec / Raspberry Pi"
  caption: "Close-up of the Distiller BHV Edition badge hardware"
contact: {}
notes:
- "Sheet listed only \"BioHacking Village\" with no badge details; the badge was\
  \ identified as the \"Distiller BHV Edition\" via PamirAI/SolaSec press coverage\
  \ and PamirAI's own documentation."
status: released
sources:
- kind: sheet
  event: dc33
  row: 14
  tab: 2025 (expected makers)
  updated: ''
- kind: url
  url: https://www.raspberrypi.com/news/creating-the-most-advanced-event-badge-yet-for-the-biohacking-village-at-def-con/
  title: Creating the most advanced event badge yet for the Biohacking Village at
    DEF CON
  accessed: '2026-09-06'
  note: Maker names (PamirAI, SolaSec), Compute Module 5 basis, offline AI chatbot
    function, badge photos
- kind: url
  url: https://docs.pamir.ai/bhv
  title: Distiller BHV Edition User Guide
  accessed: '2026-09-06'
  note: Detailed hardware specs - RP2040 board manager, e-ink display, side-firing
    RGB LED, USB-C/PD power requirements, SDK links
- kind: url
  url: https://villageb.io/Badges
  title: Badges — Biohacking Village
  accessed: '2026-09-06'
  note: Confirmed the badge is referred to on the village's own site as "the most
    computationally powerful badge ever built"; page content served was mostly
    about the 2026 badge
- kind: url
  url: https://github.com/Pamir-AI/distiller-cm5-sdk
  title: Pamir-AI/distiller-cm5-sdk
  accessed: '2026-09-06'
  note: Confirms public Apache-2.0 Python SDK for the Distiller platform used by
    the badge
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Retitled from "BioHacking Village (listed for DEF CON 33, no details)"
    after identifying the actual badge as the Distiller BHV Edition. Maker's own
    documentation (docs.pamir.ai) confirms hardware details, so core specs are
    solid, but price, exact quantity made, precise distribution rules, and hardware
    (as opposed to firmware) open-source files were not found, so confidence is
    medium rather than high. LED count and SAO header presence are unknown.
last_modified_date: '2026-09-06'
---

The DEF CON 33 (2025) Biohacking Village badge, called the Distiller BHV Edition,
was a collaboration between PamirAI, which builds the Distiller edge-AI hardware
and software platform, and SolaSec, which handled the physical design, 3D-printed
enclosure, and final assembly. Built around a Raspberry Pi Compute Module 5 with
an RP2040 handling board management, it was reportedly the most powerful, and
most power-hungry, badge the Biohacking Village had produced to that point.

Rather than blinky LEDs or a CTF puzzle in the usual badge sense, the badge's
headline feature was a pocket-sized, fully offline medical chatbot: three LLMs
ran locally on the Compute Module 5 so wearers could ask medical questions into
the built-in microphone and get spoken-style treatment ideas back, all without
an internet connection. Output and navigation went through a non-touch e-ink
screen and physical buttons, with a side-firing RGB LED whose color could be
customized through the on-badge AI assistant and which stayed lit even after
shutdown. It charged over USB-C and needed a fairly beefy USB-PD charger (9V/3A
minimum) to keep up with the Compute Module's power draw.

PamirAI's own Distiller SDK and Python source are public on GitHub under an
Apache-2.0 license, and the maker's documentation site (docs.pamir.ai/bhv) walks
through setup and use of the BHV edition specifically, though this research did
not turn up a dedicated hardware/Gerber release for the badge itself.
