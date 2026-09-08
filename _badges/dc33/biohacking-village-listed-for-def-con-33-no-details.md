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
summary: The DEF CON 33 Biohacking Village badge, built around a Raspberry Pi Compute Module 5 running PamirAI's Distiller platform, gives the wearer a pocket-sized, fully offline AI medical chatbot that listens to spoken questions and answers on an e-ink screen.
functions: Runs local LLMs entirely on-device (no internet connection) as a voice-driven medical-question chatbot; listens via a built-in microphone and responds with treatment suggestions on an e-ink screen.
look:
  colors:
  - green
  shape: rectangle
  themes:
  - village badge
  - hardware tool
tech:
  mcu: Raspberry Pi Compute Module 5 (RP2040 as board manager)
  leds:
    count: null
    type: RGB
    note: A power-indicator LED on the back plus a side-firing RGB LED that stays lit after shutdown; LED colors are customizable through the UI or the on-badge AI assistant.
  display: e-ink (non-touch, navigated with physical buttons)
  connectivity:
  - wifi
  battery: USB-C, requires a USB-PD charger rated 9V/3A minimum; auto-shuts down below 1% battery and won't power on below 3%
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Given out at the DEF CON 33 Biohacking Village in Las Vegas, August 2025; exact distribution method (all attendees vs. contest/volunteer only) not stated in sources found.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/Pamir-AI/distiller-cm5-sdk
  eda_tool: null
  notes: PamirAI's Distiller SDK (Python, Apache-2.0) is public; the docs.pamir.ai/bhv user guide points to a "BHV branch" of both distiller-cm5-sdk and distiller-cm5-python, but the repo's default page fetched here did not show that branch. No hardware/Gerber files were found.
links:
- label: Raspberry Pi blog post
  url: https://www.raspberrypi.com/news/creating-the-most-advanced-event-badge-yet-for-the-biohacking-village-at-def-con/
  kind: article
  archived: https://web.archive.org/web/20260531142306/https://www.raspberrypi.com/news/creating-the-most-advanced-event-badge-yet-for-the-biohacking-village-at-def-con/
- label: Distiller BHV Edition user guide
  url: https://docs.pamir.ai/bhv
  kind: doc
  archived: https://web.archive.org/web/20260510140351/https://docs.pamir.ai/bhv
- label: Biohacking Village badges page
  url: https://villageb.io/Badges
  kind: website
  archived: https://web.archive.org/web/20260511223900/https://www.villageb.io/badges
- label: distiller-cm5-sdk (GitHub)
  url: https://github.com/Pamir-AI/distiller-cm5-sdk
  kind: repo
images:
- file: assets/images/badges/dc33/biohacking-village-listed-for-def-con-33-no-details/1c5214ceee.jpg
  source: https://www.raspberrypi.com/news/creating-the-most-advanced-event-badge-yet-for-the-biohacking-village-at-def-con/
  credit: Raspberry Pi (raspberrypi.com)
  caption: 'Front of the Distiller BHV Edition badge: green 3D-printed enclosure and e-ink screen showing the medical chatbot'
  archived: https://web.archive.org/web/20260531142306/https://www.raspberrypi.com/news/creating-the-most-advanced-event-badge-yet-for-the-biohacking-village-at-def-con/
- file: assets/images/badges/dc33/biohacking-village-listed-for-def-con-33-no-details/d46094e0cf.jpg
  source: https://www.raspberrypi.com/news/creating-the-most-advanced-event-badge-yet-for-the-biohacking-village-at-def-con/
  credit: Raspberry Pi (raspberrypi.com)
  caption: Back of the Distiller BHV Edition badge's green 3D-printed enclosure
  archived: https://web.archive.org/web/20260531142306/https://www.raspberrypi.com/news/creating-the-most-advanced-event-badge-yet-for-the-biohacking-village-at-def-con/
contact: {}
notes:
- Sheet listed only "BioHacking Village" with no badge details; the badge was identified as the "Distiller BHV Edition" via PamirAI/SolaSec press coverage and PamirAI's own documentation. The village's own site lists it as "AI Chatbot Badge (2025)" by PamirAI & SolaSec; the Raspberry Pi article does not name it.
status: released
sources:
- kind: sheet
  event: dc33
  row: 14
  tab: 2025 (expected makers)
  updated: ''
- kind: url
  url: https://www.raspberrypi.com/news/creating-the-most-advanced-event-badge-yet-for-the-biohacking-village-at-def-con/
  title: Creating the most advanced event badge yet for the Biohacking Village at DEF CON
  accessed: '2026-09-06'
  note: Maker names (PamirAI, SolaSec), Compute Module 5 basis, offline AI chatbot function, badge photos
  archived: https://web.archive.org/web/20260531142306/https://www.raspberrypi.com/news/creating-the-most-advanced-event-badge-yet-for-the-biohacking-village-at-def-con/
- kind: url
  url: https://docs.pamir.ai/bhv
  title: Distiller BHV Edition User Guide
  accessed: '2026-09-06'
  note: Detailed hardware specs - RP2040 board manager, e-ink display, side-firing RGB LED, USB-C/PD power requirements, SDK links
  archived: https://web.archive.org/web/20260510140351/https://docs.pamir.ai/bhv
- kind: url
  url: https://villageb.io/Badges
  title: Badges — Biohacking Village
  accessed: '2026-09-06'
  note: Lists the 2025 badge as "AI Chatbot Badge (2025)" by PamirAI & SolaSec, a pocket-sized medical chatbot running three AI models on a Raspberry Pi CM5; page content is mostly about the 2026 badge
  archived: https://web.archive.org/web/20260511223900/https://www.villageb.io/badges
- kind: url
  url: https://github.com/Pamir-AI/distiller-cm5-sdk
  title: Pamir-AI/distiller-cm5-sdk
  accessed: '2026-09-06'
  note: Confirms public Apache-2.0 Python SDK for the Distiller platform used by the badge
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-06'
  notes: Fact-checked 2026-09-06 against all four cited pages; unsupported theme tags and image credits were corrected. Retitled from "BioHacking Village (listed for DEF CON 33, no details)" after identifying the actual badge as the Distiller BHV Edition. Maker's own documentation (docs.pamir.ai) confirms hardware details, so core specs are solid, but price, exact quantity made, precise distribution rules, and hardware (as opposed to firmware) open-source files were not found, so confidence is medium rather than high. LED count and SAO header presence are unknown.
last_modified_date: '2026-09-06'
---

The DEF CON 33 (2025) Biohacking Village badge, called the Distiller BHV Edition,
was a collaboration between PamirAI, which builds the Distiller edge-AI hardware
and software platform, and SolaSec, which handled the physical design, 3D-printed
enclosure, and final assembly. Built around a Raspberry Pi Compute Module 5 with
an RP2040 handling board management, it was reportedly the most powerful, and
most power-hungry, badge the Biohacking Village had produced to that point.

Rather than blinky LEDs or a CTF puzzle in the usual badge sense, the badge's
headline feature was a pocket-sized, fully offline medical chatbot: three AI
models ran locally on the Compute Module 5 so wearers could ask medical
questions into the built-in microphone and get treatment suggestions back, all
without an internet connection. Output and navigation went through a non-touch e-ink
screen and physical buttons, with a side-firing RGB LED whose color could be
customized through the UI or the on-badge AI assistant and which stayed lit even after
shutdown. It charged over USB-C and needed a fairly beefy USB-PD charger (9V/3A
minimum) to keep up with the Compute Module's power draw.

PamirAI's own Distiller SDK and Python source are public on GitHub under an
Apache-2.0 license, and the maker's documentation site (docs.pamir.ai/bhv) walks
through setup and use of the BHV edition specifically, though this research did
not turn up a dedicated hardware/Gerber release for the badge itself.
