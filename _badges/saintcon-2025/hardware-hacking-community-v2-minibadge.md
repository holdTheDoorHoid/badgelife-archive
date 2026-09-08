---
title: Hardware Hacking Community v2 minibadge
id: saintcon-2025-hardware-hacking-community-v2-minibadge
layout: badge
parent: Saintcon 2025
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2025
year: 2025
makers:
- name: jkarras & mav
summary: A reward minibadge given out at the SAINTCON 2025 Hardware Hacking Community (HHC) helpdesk to attendees who finish another minibadge or soldering project.
functions: 'No interactive functions beyond an illuminated mascot logo: a single LED backlights the HHC character graphic once assembled.'
look:
  colors:
  - black
  - orange
  - silver
  shape: rectangle
  themes:
  - mascot
  - learn to solder
tech:
  mcu: none
  leds:
    count: 1
    type: null
    note: One LED backlights the orange/silver Hardware Hacking Community mascot logo, visible lit in the assembly video.
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: 'free (earned, not sold)'
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Handed out at the Hardware Hacking Community helpdesk at SAINTCON 2025 to anyone who had completed another minibadge or soldering project, while supplies lasted.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: saintcon.zip/SAINTCON_2025/index.html@p=1462
  url: https://saintcon.zip/SAINTCON_2025/index.html@p=1462
  kind: website
- label: SAINTCON 2025 HHC MB Assembly Guide (YouTube)
  url: https://www.youtube.com/watch?v=mYhyAsTBl1Q
  kind: video
- label: Hardware Hacking Community - SAINTCON
  url: https://www.saintcon.org/communities/hardware-hacking/
  kind: website
images:
- file: assets/images/badges/saintcon-2025/hardware-hacking-community-v2-minibadge/f36f41d6d7.jpg
  source: "https://www.youtube.com/watch?v=mYhyAsTBl1Q"
  credit: "SAINTCON Hardware Hacking Community"
  caption: "Assembly guide video thumbnail showing the Hardware Hacking Community v2 minibadge components"
contact: {}
notes:
- HHC minibadge awarded at SAINTCON 2025 to attendees completing a soldering project, verified at the Hardware Hacking helpdesk (also shown in a YouTube assembly guide). Found by the event-year sweep, task saintcon-2025.
- The SAINTCON page's own <title> tag reads "Hardware Hacking v2" (dropping "Community"), but the body text and community page both call it the "Hardware Hacking Community minibadge" / "HHC Minibadge" — kept the sweep's fuller title.
status: released
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2025/index.html@p=1462
  title: Hardware Hacking Community v2 minibadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2025); event read as ''saintcon-2025''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2025/index.html@p=1462
  title: COM - Hardware Hacking v2 - SAINTCON
  accessed: '2026-09-08'
  note: Confirmed the minibadge is a free reward for completing a soldering project at the HHC helpdesk, credited to jkarras and mav; no price, quantity, or chip/LED specs are stated on the page itself.
- kind: url
  url: https://www.youtube.com/watch?v=mYhyAsTBl1Q
  title: SAINTCON 2025 HHC MB Assembly Guide - YouTube
  accessed: '2026-09-08'
  note: Assembly walkthrough confirms SMD and through-hole LED soldering steps; video thumbnail shows the finished badge (black square PCB, orange/silver backlit mascot logo, screw-mounted corners), used as the archive image.
- kind: url
  url: https://www.saintcon.org/communities/hardware-hacking/
  title: Hardware Hacking Community - SAINTCON 26
  accessed: '2026-09-08'
  note: Background on the Hardware Hacking Community, which has run since 2014 and issues this minibadge as its yearly reward item.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: The maker's own SAINTCON pages and an official assembly-guide video confirm the badge exists, its makers, event/year, distribution method (free reward, not sold), and appearance (illuminated mascot logo). No source states an MCU, exact LED part number, board dimensions, price, or production quantity, so those fields are left empty rather than guessed. No design files (hardware/firmware/Gerbers) were found published for this specific badge.
last_modified_date: '2026-09-08'
---

The Hardware Hacking Community (HHC) minibadge is not sold; it is a reward. SAINTCON's Hardware Hacking Community, run by jkarras and mav since 2014, hands the badge out at its conference helpdesk to any attendee who finishes assembling another minibadge or brings in a completed soldering project of their own. Stock is limited to "until we run out," making it a first-come, first-served token of having done the work rather than a purchasable item.

Physically it is a small black PCB carrying the orange-and-silver Hardware Hacking Community mascot logo and the year "SAINTCON 2025," mounted with four corner screws. A single LED backlights the logo once soldered in, per the official assembly-guide video, which walks through SMD component placement followed by through-hole LED soldering. No chip, display, or connectivity is used; no design files or Gerbers for this specific badge have been published, distinguishing it from the fully open hardware projects the HHC otherwise showcases.
