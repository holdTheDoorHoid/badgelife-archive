---
title: BTV 5th Anniversary Badge
id: dc30-blue-team-village-btv-badge
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: Blue Team Village
  url: https://www.blueteamvillage.org
- name: alt_bier
  role: BTV BadgeLife team
- name: PacketSqueezins
  role: BTV BadgeLife team
- name: De-CERT
  role: BTV BadgeLife team
summary: Blue Team Village's 5th-anniversary badge for DEF CON 30, a navy PCB badge shaped like a stylized blade/wing with the BTV griffin logo, blue accent LEDs, and two onboard SAO ports for add-ons.
functions: 'No onboard microcontroller: a resistor network drives six blue LEDs that light the BTV logo. Hosts two SAO connectors so other badges'' SAOs can be plugged into it.'
look:
  colors:
  - blue
  - white
  shape: blade
  themes:
  - security
  - logo
  - village badge
tech:
  mcu: none
  leds:
    count: 6
    type: 0603 SMD
    note: Blue LEDs accent the BTV griffin logo; the kit version ships the six 0603 LEDs and ten 1206 resistors unpopulated for the buyer to solder.
  display: none
  connectivity: []
  battery: 3x AA/LR6 (the event listing says "3 AA/LR6 batteries" in one place and "3x AAA/LR6 battery holder" in the kit contents list further down; sources disagree on AA vs AAA)
  sao_version: null
get_one:
  price: $45 kit / $55 assembled
  price_usd: 45.0
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  - kit
  where: Ordered in advance via Eventbrite; pickup only, in person at Blue Team Village (Savoy Ballroom, Flamingo Las Vegas) during DEF CON 30, Aug 12-14 2022.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.eventbrite.com/cc/vegas-btv-def-con-30-891669
  url: https://www.eventbrite.com/cc/vegas-btv-def-con-30-891669
  kind: store
- label: eventbrite.com/e/btv-5th-anniversary-badge-def-con-vegas-pickup-only-tickets-386551595227
  url: https://www.eventbrite.com/e/btv-5th-anniversary-badge-def-con-vegas-pickup-only-tickets-386551595227
  kind: store
- label: Badge kit assembly instructions (Google Drive PDF, via tinyurl.com/btvbadge)
  url: https://drive.google.com/file/d/1G8Tu3Uuc-6ZUovdkH9qp_ZH7e16ZzTCP/view
  kind: doc
images:
- file: assets/images/badges/dc30/blue-team-village-btv-badge/52dcd7da00.jpg
  source: "https://www.eventbrite.com/cc/vegas-btv-def-con-30-891669"
  credit: "Blue Team Village (via Eventbrite listing)"
  caption: "BTV 5th Anniversary Badge PCB, DEF CON 30, showing Graylog sponsor branding and header pins"
contact: {}
notes:
- $45 for kit and $55 for assembled DEFCON PICKUP ONLY
- 'Sheet listed this as "Blue Team Village (BTV) Badge"; the maker''s own Eventbrite listing names it "BTV 5th Anniversary Badge" (also called "BTV5 badge" in the listing copy). Title updated to match; id/filename kept as imported.'
status: released
sources:
- kind: sheet
  event: dc30
  row: 29
  updated: '2022-08-04'
- kind: url
  url: https://www.eventbrite.com/cc/vegas-btv-def-con-30-891669
  title: '[VEGAS] BTV @ DEF CON 30 - Eventbrite collection page'
  accessed: '2026-09-07'
  note: Confirmed the badge listing exists ("BTV 5th Anniversary Badge - DEF CON VEGAS PICKUP ONLY") and surfaced the specific event-page URL and a photo of the badge.
- kind: url
  url: https://www.eventbrite.com/e/btv-5th-anniversary-badge-def-con-vegas-pickup-only-tickets-386551595227
  title: BTV 5th Anniversary Badge - DEF CON VEGAS PICKUP ONLY (Eventbrite event page)
  accessed: '2026-09-07'
  note: Full listing copy - two ticket tiers ($55 assembled / $45 DIY kit), SAO connector count, LED/resistor BOM for the kit, battery type, pickup location and dates, and credit to the BTV BadgeLife team (alt_bier, PacketSqueezins, De-CERT). Sales ended; page confirms it is sold out.
- kind: url
  url: https://tinyurl.com/btvbadge
  title: Full assembly instructions (redirects to Google Drive PDF)
  accessed: '2026-09-07'
  note: Link the listing gives for kit assembly instructions; only checked that the redirect resolves, did not open the PDF contents.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core facts (price tiers, SAO ports, LED/battery BOM, pickup logistics, maker credit) come straight from the maker''s own Eventbrite listing, so confidence would be high except for two loose ends: the listing itself contradicts on AA vs AAA batteries, and no schematic/gerber/firmware repo was found (only an assembly-instructions PDF), so make_your_own fields are left empty rather than guessed. A companion item, a separate "Blue Team Village SAO" for DEF CON 30, is sold on its own Eventbrite listing (https://www.eventbrite.com/e/blue-team-village-sao-def-con-vegas-pickup-only-tickets-397239031637) and was not researched here - see other_items_found in the run report. No Hackaday.io project or GitHub hardware repo was found for this specific 2022 badge (an unrelated fyrm/btvbadge GitHub repo exists but documents BTV''s 2019/DEF CON 27 badge, a different project).'
last_modified_date: '2026-09-07'
---

Blue Team Village's fifth-anniversary badge, sold for DEF CON 30 in Las Vegas (August 2022) as pickup-only merchandise ordered in advance through Eventbrite. The badge is a navy-blue PCB cut into an angular, wing- or blade-like outline carrying the BTV griffin/valkyrie logo and "DEF CON" text in white silkscreen, with sponsor branding (Graylog) worked into the design. It runs on 3x AA/LR6 batteries with no onboard microcontroller: a simple resistor network lights six small blue 0603 LEDs to accent the logo. The badge also carries two onboard SAO connectors, letting other badges' add-ons be plugged into it.

It was sold in two versions: a $55 fully-assembled badge and a $45 DIY kit aimed at buyers with prior SMD soldering experience (the listing explicitly warns it is not for beginners, citing the small 0603/1206 components). The kit included the LEDs, resistors, a battery holder, and the two SAO headers, plus a link to written assembly instructions; solder paste, fine tweezers, and a hot plate or fine-tip iron were suggested but not included. Both versions were picked up in person at Blue Team Village's space in the Savoy Ballroom at the Flamingo Las Vegas. The listing credits BTV's BadgeLife team - alt_bier, PacketSqueezins, and De-CERT - as the makers.

Blue Team Village also sold a separate, standalone SAO for DEF CON 30 through its own Eventbrite listing; that is a different item from this badge and has not been researched as part of this entry.
