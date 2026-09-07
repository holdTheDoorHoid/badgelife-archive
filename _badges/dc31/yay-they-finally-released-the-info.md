---
title: Yay!!! They finally released the info
id: dc31-yay-they-finally-released-the-info
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: Blue Team Village
  url: https://www.blueteamvillage.org
summary: 'The BTV6 badge, Blue Team Village''s sixth annual DEF CON badge: a 5-inch circular PCB lighting up the village''s Project Obsidian logo with six blue LEDs, sold as a beginner-friendly solder kit or pre-assembled.'
functions: 'Decorative/blinky only: six blue LEDs illuminate the Project Obsidian logo silkscreen. No stated game, CTF, or radio function.'
look:
  colors:
  - blue
  shape: circle
  themes:
  - village badge
  - security
  - learn to solder
  - logo
tech:
  mcu: none
  leds:
    count: 6
    type: discrete
    note: '6x 5mm blue through-hole LEDs with 6x 100-ohm resistors, no driver chip'
  display: none
  connectivity: []
  battery: CR2032
  sao_version: none
get_one:
  price: $65 kit / $80 assembled
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: 'Eventbrite listing shows "Event ended"; checked 2026-09-07.'
  distribution:
  - purchase
  - kit
  where: 'Sold via Eventbrite for in-person pickup only at the Blue Team Village booth (Flamingo Las Vegas, Sunset-Scenic) during DEF CON 31, August 11-13, 2023. Kit version ($65) is a beginner/intermediate solder kit; assembled version ($80) ships built. Both included a CR2032 battery and lanyard. Assembly instructions were emailed after purchase, not published openly. No walk-up or remote/mail distribution; no refunds after August 9, 2023. Credited to Blue Team Village BadgeLife team members h4r0ld, alt_bier, and De-CERT.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: t.co/YGDUM6lAnf
  url: https://t.co/YGDUM6lAnf
  kind: website
- label: 'BTV6 DEF CON 31 Badge (Eventbrite, event ended)'
  url: https://www.eventbrite.com/e/btv6-def-con-31-badge-def-con-vegas-pickup-only-tickets-691105062847
  kind: store
- label: 'BTV @ DEF CON 31 Eventbrite collection'
  url: https://www.eventbrite.com/cc/btv-def-con-31-vegas-2468339
  kind: website
- label: 'Blue Team Village'
  url: https://www.blueteamvillage.org
  kind: website
images:
- file: assets/images/badges/dc31/yay-they-finally-released-the-info/3a08dc9446.jpg
  source: "https://www.eventbrite.com/e/btv6-def-con-31-badge-def-con-vegas-pickup-only-tickets-691105062847"
  credit: "Blue Team Village"
  caption: "BTV6 badge, a 5-inch circular PCB with the Project Obsidian logo lit by blue LEDs"
contact: {}
notes:
- This is a beginner to intermediate kit.
- 'Likely duplicates dc31-awesome-peeps-from-blue-team-village-unnamed-badge-sao, an earlier community-sheet row (Feb 2023) that recorded only a rumor of a BTV DEF CON 31 badge before this sale listing (Aug 2023) made the name and specs public; both point to the same Eventbrite listing for the "BTV6" badge.'
status: released
sources:
- kind: sheet
  event: dc31
  row: 16
  updated: '2023-08-03'
- kind: url
  url: https://www.eventbrite.com/cc/btv-def-con-31-vegas-2468339
  title: 'BTV @ DEF CON 31 [VEGAS] (Eventbrite collection)'
  accessed: '2026-09-07'
  note: 'Resolves the sheet''s t.co short link; lists the "BTV6 DEF CON 31 Badge" ticket page.'
- kind: url
  url: https://www.eventbrite.com/e/btv6-def-con-31-badge-def-con-vegas-pickup-only-tickets-691105062847
  title: 'BTV6 DEF CON 31 Badge - DEF CON Vegas Pickup Only'
  accessed: '2026-09-07'
  note: 'Full product description: $65 kit / $80 assembled pricing, component list (board, 6x 5mm blue LEDs, 6x 100-ohm resistors, CR2032 holder, battery, lanyard), Project Obsidian logo, pickup-only distribution, maker credits (h4r0ld, alt_bier, De-CERT), and the badge photo.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Eventbrite''s listing (via its embedded structured description, since the rendered page shows "Event ended" with no visible body text) gave a full component list and price breakdown in the maker''s own words, so confidence is high on what is stated. Not found anywhere: MCU/driver chip (kit description lists no chip, so likely a passive LED board wired to a coin cell with no controller - recorded as tech.mcu: none rather than left null, since the parts list is complete and exhaustive), quantity made, PCB color/finish, and whether hardware/firmware files were ever published (none referenced in the listing). This entry very likely duplicates dc31-awesome-peeps-from-blue-team-village-unnamed-badge-sao, an earlier sheet row for the same event/maker that recorded only an early rumor of a BTV badge; that entry cross-references this one. Left as two entries per the task''s duplicate-handling instructions rather than merging.'
last_modified_date: '2026-09-07'
---

Blue Team Village's sixth annual DEF CON badge, "BTV6," is a 5-inch circular PCB built around the village's Project Obsidian logo, lit by six 5mm blue LEDs run off a CR2032 coin cell through six 100-ohm resistors - no microcontroller or driver chip in the design. Blue Team Village sold it during DEF CON 31 (August 11-13, 2023) via Eventbrite for pickup-only at their booth in the Flamingo Las Vegas: $65 as a beginner/intermediate solder kit (with assembly instructions emailed after purchase) or $80 pre-assembled, both including a CR2032 battery and lanyard. The village credited its BadgeLife team members h4r0ld, alt_bier, and De-CERT, and noted that sale proceeds went back into funding the village's free year-round programming.

This entry began on the community sheet as a row recorded in August 2023 once the sale went live - hence the title "Yay!!! They finally released the info," reacting to an earlier sheet row (now the separate archive entry dc31-awesome-peeps-from-blue-team-village-unnamed-badge-sao) from February 2023 that had only rumored a BTV badge was coming, with no details yet public. Both rows point to the same Eventbrite listing and are very likely the same badge recorded twice at different points in the year; they are kept as separate entries here rather than merged, per this archive's duplicate-handling process.
