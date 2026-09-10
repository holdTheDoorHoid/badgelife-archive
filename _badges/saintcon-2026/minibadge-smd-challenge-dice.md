---
title: Minibadge SMD Challenge Dice
id: saintcon-2026-minibadge-smd-challenge-dice
layout: badge
parent: Saintcon 2026
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2026
year: 2019
makers:
- name: RuShan
summary: A blank SMD soldering-skills test minibadge made for the SAINTCON Hardware Hacking Contest (HHC) in 2019, shaped as a six-sided die.
functions: 'No electronic function beyond the soldering exercise itself: a solderer places a mix of surface-mount resistors, capacitors, an inductor, and an IC onto unpopulated footprints under time or skill pressure, with +5V/+3V3/GND header rows on the back for testing the result.'
look:
  colors:
  - red
  - white
  shape: dice
  themes:
  - puzzle
  - learn to solder
  - hardware tool
  - ctf
tech:
  mcu: null
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  distribution:
  - contest
  where: Given out during the SAINTCON Hardware Hacking Contest (HHC) soldering challenge, 2019.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=Minibadge%20SMD%20Challenge%20Dice&year=2026
  url: https://minibadge.wiki/?search=Minibadge%20SMD%20Challenge%20Dice&year=2026
  kind: website
- label: minibadge.wiki 2026 data export (badge record)
  url: https://minibadge.wiki/2026.json
  kind: doc
  archived: https://web.archive.org/web/20260611102319/http://minibadge.wiki/2026.json
- label: Assembly/soldering instructions video
  url: https://youtu.be/gIXEWhKLi_g
  kind: video
images:
- file: assets/images/badges/saintcon-2026/minibadge-smd-challenge-dice/91a5a93ecc.jpg
  source: https://minibadge.wiki/2026.json
  credit: RuShan
  caption: Front of the SMD Challenge Dice minibadge, showing the die graphic and SMD pads to be soldered
  archived: https://web.archive.org/web/20260611102319/http://minibadge.wiki/2026.json
- file: assets/images/badges/saintcon-2026/minibadge-smd-challenge-dice/ab18e68bac.jpg
  source: https://minibadge.wiki/2026.json
  credit: RuShan
  caption: Back of the SMD Challenge Dice minibadge, showing the power rail labels and unpopulated SMD component footprints
  archived: https://web.archive.org/web/20260611102319/http://minibadge.wiki/2026.json
contact: {}
notes:
- 'category: Contest'
status: released
sources:
- kind: url
  url: https://minibadge.wiki/?search=Minibadge%20SMD%20Challenge%20Dice&year=2026
  title: Minibadge SMD Challenge Dice
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2026''.'
- kind: url
  url: https://minibadge.wiki/2026.json
  title: MiniBadge Wiki data export (2026.json)
  accessed: '2026-09-07'
  note: 'Raw community-submitted record for this badge: title, author (RuShan), description, soldering difficulty (Advanced), category (Contest), conferenceYear (2019), howToAcquire ("contest during 2019 SAINTCON"), and front/back image URLs.'
  archived: https://web.archive.org/web/20260611102319/http://minibadge.wiki/2026.json
- kind: url
  url: https://youtu.be/gIXEWhKLi_g
  title: Assembly & soldering instructions video
  accessed: '2026-09-07'
  note: Linked by the minibadge.wiki record as the soldering-instructions video; video page content was not retrievable (YouTube consent/JS wall), so only the link itself is confirmed, not its content.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The minibadge.wiki record lists conferenceYear as 2019, not 2026 — this entry was filed under saintcon-2026 by the discovery sweep's search-URL parameter, which does not reflect the badge's actual year. No saintcon-2019 (or saintcon-2018/2020) event id exists in events.yml, so the event field is left as saintcon-2026 per the research guide's rule for when no matching event exists; the year field has been corrected to 2019 to match the source. A human maintainer should add a saintcon-2019 event and move this entry. quantityMade was recorded as 0 in the source data, which reads as "not specified" rather than a real count, so get_one.quantity is left empty. No price, maker profile URL, PCB fabricator, or open-source design files were found. The soldering-instructions YouTube video (https://youtu.be/gIXEWhKLi_g) could not be read (page returned only YouTube's footer/legal boilerplate to the fetch tool), so its content is unconfirmed beyond the link itself.
last_modified_date: '2026-09-07'
---

The SMD Challenge Dice is a minibadge RuShan made for the Hardware Hacking Contest (HHC) at SAINTCON in 2019 — a soldering-skills test rather than a functional gadget. The board is silkscreened with a large six-sided die and the words "SAINTCON CONTEST," and its "pips" and surrounding pads are actually unpopulated footprints for a scattering of surface-mount parts: several resistors and capacitors, an inductor, and a small IC. The back of the board breaks out +5V, +3V3, and GND header rows for probing continuity once the parts are placed.

The minibadge.wiki record rates the soldering difficulty "Advanced" and notes there were two assembly videos, linking one soldering-instructions video on YouTube. It was distributed as part of the 2019 SAINTCON contest itself rather than sold or given away separately; no price, production quantity, or open-source design files were found.

This entry currently sits in the saintcon-2026 folder because it was picked up by an automated sweep whose search URL carried a 2026 filter parameter — the source data itself dates the badge to 2019, and the `year` field above has been corrected accordingly. No saintcon-2019 event exists yet in this archive's event list, so the folder/event id could not be corrected to match; a maintainer will need to add that event and relocate the entry.
