---
title: NorthSec 2015 Badge
id: northsec-2015-northsec-2015-badge
layout: badge
parent: NorthSec 2015
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: northsec-2015
year: 2015
makers:
- name: NorthSec
summary: 'A hardware badge issued one per CTF team (not per attendee) at NorthSec 2015, the event''s first year with a hardware badge.'
functions: null
look:
  colors: []
  shape: null
  themes:
  - ctf
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - contest
  where: 'Issued one per CTF team at the 2015 NorthSec event in Montreal.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: badge.gallery/events/northsec-2015
  url: https://badge.gallery/events/northsec-2015
  kind: website
- label: nsec.io/past-editions
  url: https://nsec.io/past-editions/
  kind: website
images: []
contact: {}
notes:
- Official NorthSec 2015 electronic hardware badge, issued per CTF team; not yet in the archive. Found by the event-year sweep, task northsec.
status: listed
sources:
- kind: url
  url: https://badge.gallery/events/northsec-2015
  title: NorthSec 2015 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:northsec); event read as ''northsec-2015''.'
- kind: url
  url: https://nsec.io/past-editions/
  title: 'Past Editions - NorthSec'
  accessed: '2026-09-08'
  note: 'NorthSec''s own history page; confirms "gave a hardware badge per CTF team" in 2015 and ~400 attendees that year.'
- kind: url
  url: https://badge.gallery/series/northsec
  title: 'NorthSec - Hacker Con Badges'
  accessed: '2026-09-08'
  note: 'Third-party compendium claiming to cite NorthSec''s official past-editions page for specifics (54 teams of eight; challenge ties to network, IPv6 workstation, RF-monitoring, smartcard; Bonsecours venue). Checked the actual past-editions page directly and none of those specifics appear there — only the badge-per-team fact and attendee count are on the primary source. Kept only for the badge''s bare existence/no-image note; did not use its uncorroborated specifics.'
research:
  status: verified
  confidence: low
  last_checked: '2026-09-08'
  notes: 'Existence confirmed by NorthSec''s own past-editions page ("gave a hardware badge per CTF team" in 2015, ~400 attendees, theme "Rao''s Intricate Kingdom" - the only page content actually available under the 2015 heading). No maker/designer beyond the NorthSec organization, no photo, and no technical specifications could be found anywhere, including GitHub (nsec/nsec-badge covers a much later USB-C/Espressif badge, not this one). Removed several previously-added claims (54 teams of eight, Marché Bonsecours venue, ties to network/IPv6/RF-monitoring/smartcard challenges) after checking their only source, badge.gallery: that page asserts these come from "NorthSec''s official past-editions page," but a direct fetch of that page shows no such content under the 2015 section - it contains only the badge-per-team sentence, the attendance figure, and the CTF theme name and top-3 teams. Since the third-party source misrepresents its own primary citation, its uncorroborated specifics are not trustworthy and have been dropped rather than repeated. Left most tech/look/get_one fields empty rather than guess.'
last_modified_date: '2026-09-08'
---

NorthSec added a hardware badge to its Capture the Flag competition starting in 2015, the same year it began pairing the CTF with a two-day conference. Rather than one badge per attendee, NorthSec gave a single hardware badge to each competing CTF team, at an event that drew around 400 infosec professionals, students, and enthusiasts to Montreal. That year's CTF ran on a "Rao's Intricate Kingdom" theme.

Beyond that, almost nothing about the badge's physical design or in-competition role has survived online in a form that checks out. NorthSec's own site and GitHub organization document later years' badges in detail (chips, firmware repos, displays), but the official past-editions page says nothing more about the 2015 badge than that it existed and went one-per-team. A third-party badge compendium (badge.gallery) adds specifics — a 54-team, teams-of-eight structure, a Marché Bonsecours venue, and challenge ties to networking, an IPv6 workstation, RF monitoring, and a smartcard — while claiming these come from NorthSec's own history page; they do not appear there, so they are omitted here rather than repeated on trust. No schematic, repository, or photo of the 2015 badge has turned up anywhere, and badge.gallery separately notes it has no rights-cleared image for this year. The entry reflects only what NorthSec's own history page confirms: that the badge existed, was distributed per team rather than per person, and was issued at the 2015 event alongside a "Rao's Intricate Kingdom"-themed CTF.
