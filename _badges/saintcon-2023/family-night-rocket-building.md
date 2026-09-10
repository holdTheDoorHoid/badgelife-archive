---
title: Family Night - Rocket Building
id: saintcon-2023-family-night-rocket-building
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: TGalvez
summary: 'A beginner-level SAINTCON 2023 Family Night minibadge printed with a rocket graphic, given out during the Family Night rocket-building activity.'
functions: 'Single LED lit through one resistor; no other electronics.'
look:
  colors:
  - red
  - gold
  shape: null
  themes:
  - space
tech:
  mcu: none
  leds:
    count: 1
    type: null
    note: 'Through-hole LED soldered on the back with a standoff so it can be bent to face outward through a printed round window; one resistor.'
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: 'Given to Family Night attendees who came to build and launch a rocket at the event; TGalvez held extras for anyone who missed Family Night to collect after the fact.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  kind: website
- label: Zevlag - Family Night Minibadges 2023 assembly guide (PDF)
  url: https://minibadges.zevlag.com/buildguides/FamilyNight-Minibadges-2023.pdf
  kind: doc
images:
  - file: assets/images/badges/saintcon-2023/family-night-rocket-building/front.jpg
    source: "https://minibadges.zevlag.com/buildguides/FamilyNight-Minibadges-2023.pdf"
    credit: "Zevlag / TGalvez"
    caption: "Front of the square PCB, printed with a rocket-and-moon graphic and the badge name"
  - file: assets/images/badges/saintcon-2023/family-night-rocket-building/back.jpg
    source: "https://minibadges.zevlag.com/buildguides/FamilyNight-Minibadges-2023.pdf"
    credit: "Zevlag / TGalvez"
    caption: "Back of the PCB with the LED/resistor pads, TGalvez maker mark, and Family Night event artwork"
contact: {}
notes:
- 2023 SAINTCON Family Night minibadge for the Rocket Building activity. Found by the event-year sweep, task saintcon-2023.
- 'The community minibadge sheet listed this only as "Family Night - Rocket Building"; the Zevlag assembly guide gives the same name and description ("Family Night Rocket Badge"), so the title is unchanged.'
status: released
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  title: Family Night - Rocket Building
  accessed: '2026-09-10'
  note: 'This is SAINTCON''s own official 2023 Minibadge Guide (a 197-page PDF listing every 2023 minibadge). Page for this badge confirms designer TGalvez, difficulty BEGINNER, distribution ("Available only to Family Night Attendees. Come build and launch a rocket at Family Night to Collect... For those not attending family night, See TGalvez after the event for a collection of Family Night Badges."), and assembly (single resistor + single through-hole LED bent to the back). Lists rarity as UNCOMMON, which disagrees with the Zevlag guide''s COMMON — see research.notes. It points readers to the Zevlag PDF below for "the most updated and prettiest presentation" of the assembly steps.'
- kind: url
  url: https://minibadges.zevlag.com/buildguides/FamilyNight-Minibadges-2023.pdf
  title: Zevlag - Family Night Minibadges 2023 (assembly guide PDF)
  accessed: '2026-09-10'
  note: 'Confirms the badge exists, designer (TGalvez), description ("Family Night Rocket Badge"), difficulty (beginner), rarity (common - disagrees with the official guide''s "uncommon"), distribution (Family Night attendees only, collectible from TGalvez afterward), and assembly (single LED + resistor). The board itself is a plain square PCB with a printed rocket-and-moon graphic on front and component pads/maker art on back - not a rocket-shaped cutout as an earlier draft of this entry claimed; also source of the front/back PCB images (verified against the guide''s own front/back page layout, which had been saved swapped).'
research:
  status: verified
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Confirmed via both SAINTCON''s own official 2023 Minibadge Guide and the Zevlag community assembly guide; the two independently agree on maker, difficulty, and distribution, so confidence is high. Fact-check correction (2026-09-10): the front/back images had been saved swapped (the component-side photo was labeled "front", the printed-graphic side "back") - corrected by swapping the files. Also corrected an invented claim that the PCB itself is die-cut into a rocket silhouette; the source images and the sibling family-night-lock-pick.md entry''s convention confirm it is a plain square PCB with a printed rocket-and-moon graphic and a round LED window, so look.shape and tech.leds.type were blanked and a descriptive note added instead. The two sources disagree on rarity (official guide: uncommon; Zevlag guide: common) - not recorded as a front-matter field, but noted here since it appeared in the body text. No price/quantity figures given (it was a free give-away, not sold); no hardware files or repo found; no separate maker storefront or social page located for TGalvez.'
last_modified_date: '2026-09-10'
---

The Rocket Building minibadge is one of TGalvez's contributions to SAINTCON 2023's Family Night, a track of hands-on activities for attendees' kids and families. The badge itself is simple by design: a square PCB printed on the front with a rocket-and-moon graphic, with a single LED wired through one resistor soldered on the back and bent forward so it shines out through a round window behind the moon. SAINTCON's community minibadge culture treats these as a mix of craft project and trading currency; both SAINTCON's own official 2023 Minibadge Guide and the community-run Zevlag assembly guide rate it beginner difficulty, consistent with a badge meant for kids soldering for the first time. The two guides disagree on rarity — SAINTCON's own guide calls it "uncommon," Zevlag's calls it "common."

It was not sold; it was earned. Attendees came to the Family Night event, built and helped launch a rocket, and received the minibadge as a memento of the activity rather than an SAO or worn con badge. The guide notes that people who missed Family Night could still track down TGalvez after the event to get one from his leftover stock, so it wasn't strictly gated to same-day attendance.

No separate hardware repository, BOM, or maker storefront for this specific minibadge was found; what's documented here comes from the SAINTCON minibadge guide ecosystem (the official con-hosted PDF and the community-run Zevlag assembly guide), which is where SAINTCON minibadges are typically documented in lieu of individual project pages.
