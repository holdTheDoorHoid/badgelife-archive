---
title: HITBSecConf2024 Bangkok SaikoCTF Badge
id: hitb-2024-hitbsecconf2024-bangkok-saikoctf-badge
layout: badge
parent: Hitbsecconf 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hitb-2024
year: 2024
makers:
- name: Hack In The Box
- name: SRI International
  url: https://www.sri.com/ascend/
  role: research study / SaikoCTF program
- name: IHMC
  role: research study
- name: HackRocks
  role: CTF organizer
- name: Flagyard
  role: CTF organizer / prize sponsor
summary: A hardware token awarded to every participant who completed SaikoCTF, a roughly one-hour research CTF run inside HITBSecConf2024 Bangkok's exhibition area. It doubled as a study artifact for an IARPA-funded (ReSCIND program) cyber-psychology experiment run by SRI International's ASCEND project and IHMC, not a general con badge.
functions: 'Given to CTF finishers as a completion token; described by the organizers as exposing "physio, cyber challenge, and programmable hardware component interfaces." Participants separately wore VR goggles and physiological sensors and worked through a Kali Linux VM during the timed challenge; no public source describes what the badge itself does electronically.'
look:
  colors: []
  shape: null
  themes:
  - ctf
  - security
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution:
  - contest
  where: Awarded on-site to every participant who completed the SaikoCTF challenge at HITBSecConf2024 Bangkok (Intercontinental Hotel, Bangkok, Aug 26-30 2024); not sold or otherwise distributed.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: badge.gallery/series/hitb
  url: https://badge.gallery/series/hitb
  kind: website
- label: 'SaikoCTF - HITBSecConf2024 Bangkok (official page)'
  url: https://conference.hitb.org/hitbsecconf2024bkk/saikoctf/
  kind: website
- label: HITBSecConf2024 Bangkok Exhibition page
  url: https://conference.hitb.org/hitbsecconf2024bkk/exhibition/
  kind: website
- label: 'SRI International ASCEND (SaikoCTF research program)'
  url: https://www.sri.com/ascend/
  kind: article
images: []
contact: {}
notes:
- Electronic badge issued to SaikoCTF research participants at HITB Bangkok 2024. Found by the event-year sweep, task con-troopers.
- 'The sweep''s source (badge.gallery) titled this "HITBSecConf2024 Bangkok SaikoCTF Badge," matching HITB''s own page wording ("SaikoCTF hardware badge"); no title change needed.'
status: released
sources:
- kind: url
  url: https://badge.gallery/series/hitb
  title: HITBSecConf2024 Bangkok SaikoCTF Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-troopers); event read as ''HITBSecConf 2024 Bangkok''.'
- kind: url
  url: https://conference.hitb.org/hitbsecconf2024bkk/saikoctf/
  title: 'SaikoCTF - HITBSecConf2024 - Bangkok'
  accessed: '2026-09-08'
  note: 'HITB''s own SaikoCTF page: confirms the hardware badge is given to every participant who completes the CTF, names organizers HackRocks and Flagyard, describes it as exposing physio/cyber-challenge/programmable-hardware interfaces, and gives the prize structure ($500/$300/$100 for top 3). No chip/LED/display specs or product photo of the badge itself; the page''s only image is a graphic wordmark, not the item.'
- kind: url
  url: https://conference.hitb.org/hitbsecconf2024bkk/exhibition/
  title: 'Exhibition - HITBSecConf2024 - Bangkok'
  accessed: '2026-09-08'
  note: Corroborates the SaikoCTF challenge format (up to 60 minutes, web/password-cracking challenges, Kali Linux VM, no internet).
- kind: url
  url: https://www.sri.com/ascend/
  title: 'Ascend - SRI International'
  accessed: '2026-09-08'
  note: 'Identifies SaikoCTF as SRI International''s ASCEND research vehicle for CTF-based cyber-psychology experiments run at multiple conferences and online, under the IARPA ReSCIND program; explains why the badge is tied to a research study rather than being a normal con giveaway.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: >-
    Confirmed the item is real via HITB's own official SaikoCTF page (not just the
    community sweep snippet), so this is not a rumor. However no source found gives
    hardware specifics: no MCU, LED, display, battery, quantity, or open-source design
    files, and no rights-clear photo of the physical badge itself turned up (the only
    image on the official page is a red "サイコウ" wordmark graphic, not the badge, so
    it was not saved). The recruitment-statement PDF linked from HITB's page could not
    be parsed as text; it may contain more detail and is worth a follow-up look if a
    proper PDF reader is available. SaikoCTF is a recurring SRI International/IHMC
    research CTF (IARPA ReSCIND program) that has run at other conferences too, per
    SRI's own ASCEND page and an IARPA cover-sheet PDF found in search results —
    someone building out SRI's other con appearances may find sibling entries.
last_modified_date: '2026-09-08'
---

SaikoCTF was a roughly hour-long capture-the-flag challenge held in the exhibition area of HITBSecConf2024 Bangkok (Intercontinental Hotel, August 26-30, 2024), run by HackRocks with Flagyard sponsoring the top-three cash prizes ($500/$300/$100). Every participant who completed the web-application and password-cracking challenges inside a disconnected Kali Linux VM received a hardware badge as a completion token.

What made the badge unusual is its second life: the CTF doubled as a data-collection instrument for SRI International (with IHMC) under IARPA's ReSCIND program, part of SRI's long-running ASCEND research effort into the psychology of cyber defense. Participants in the study also wore VR goggles and physiological sensors and received a short soft-skills assessment afterward. HITB's own event page describes the badge as exposing "physio, cyber challenge, and programmable hardware component interfaces," but no public source lays out its actual electronics: chip, LEDs, display, power, or enclosure remain undocumented, and no design files or clear photo of the badge itself have surfaced.

SaikoCTF is not unique to HITB Bangkok — SRI's ASCEND materials describe it running at multiple conferences and online as part of the same research dataset — so this entry may have siblings from other events worth tracking down separately.
