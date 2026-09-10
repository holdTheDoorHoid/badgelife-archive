---
title: BESD Train Mini Badge
id: saintcon-2022-besd-train-mini-badge
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: CompuDoc
- name: Shifty
summary: A SAINTCON 2022 trading minibadge with a train-silhouette silkscreen design, credited on the board to "CompuDoc/Shifty."
functions: 'No interactivity beyond its single LED: solder it together and it lights, the same as most SAINTCON minibadges.'
look:
  colors:
  - blue
  - green
  shape: rectangle
  themes:
  - minimalist
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: Single white SMD LED (D1), driven through a 2200-ohm current-limiting resistor (R1).
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - swap
  where: Traded in person at the SAINTCON 2022 minibadge community/trading space, per the general SAINTCON minibadge custom.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: github.com/CompuDocUt/SaintConMinibadges/blob/main/BESD%20Train%20Mini%20Badge%20assembly%20instructions.pdf
  url: https://github.com/CompuDocUt/SaintConMinibadges/blob/main/BESD%20Train%20Mini%20Badge%20assembly%20instructions.pdf
  kind: doc
- label: github.com/CompuDocUt/SaintConMinibadges
  url: https://github.com/CompuDocUt/SaintConMinibadges
  kind: repo
images:
  - file: assets/images/badges/saintcon-2022/besd-train-mini-badge/96ed641b6f.jpg
    source: "https://github.com/CompuDocUt/SaintConMinibadges/blob/main/BESD%20Train%20Mini%20Badge%20assembly%20instructions.pdf"
    credit: "CompuDoc/Shifty"
    caption: "Unpopulated back of the minibadge PCB, silkscreened '2022 COMPUDOC/SHIFTY'"
  - file: assets/images/badges/saintcon-2022/besd-train-mini-badge/155d700f12.jpg
    source: "https://github.com/CompuDocUt/SaintConMinibadges/blob/main/BESD%20Train%20Mini%20Badge%20assembly%20instructions.pdf"
    credit: "CompuDoc/Shifty"
    caption: "Finished badge, front side, showing the train-logo silkscreen"
contact: {}
notes:
- "The sweep filed this under the title on the PDF's filename, \"BESD Train Mini Badge.\" The document's own title line reads \"Box Elder School District Logo Mini Badge assembly instructions,\" and BESD most likely stands for Box Elder School District; the finished board shown in the guide carries a train-silhouette silkscreen, which is presumably the district's logo referenced in that title. Kept the sweep's title since it matches the maker's own filename."
status: listed
sources:
- kind: url
  url: https://github.com/CompuDocUt/SaintConMinibadges/blob/main/BESD%20Train%20Mini%20Badge%20assembly%20instructions.pdf
  title: BESD Train Mini Badge
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://github.com/CompuDocUt/SaintConMinibadges/blob/main/BESD%20Train%20Mini%20Badge%20assembly%20instructions.pdf
  title: Box Elder School District Logo Mini Badge assembly instructions (PDF)
  accessed: '2026-09-10'
  note: Full assembly-instructions PDF; source for parts list (1 PCB, 2200-ohm resistor, 1 white SMD LED, 4 header pins), board silkscreen "2022 COMPUDOC/SHIFTY", and the finished-board photo.
- kind: url
  url: https://github.com/CompuDocUt/SaintConMinibadges
  title: CompuDocUt/SaintConMinibadges (GitHub repo)
  accessed: '2026-09-10'
  note: Repo README ("Badges Created for Saintcon 2022 - details and assembley instructions") confirms the event/year and that this is one of several minibadges from the same maker/repo.
- kind: url
  url: https://minibadge.wiki/2022.pdf
  title: SAINTCON Minibadge Assembly Guide 2022
  accessed: '2026-09-10'
  note: Official 2022 SAINTCON minibadge guide does not list a "BESD" or "Box Elder" badge (it does list an unrelated "Dave Train Badge" by SHIFTY), so this appears to be a maker-distributed minibadge outside the official/submitted catalog rather than an omission.
research:
  status: verified
  confidence: low
  last_checked: '2026-09-10'
  notes: 'Fact-check pass (2026-09-10): re-fetched all four cited sources directly. The assembly-instructions PDF (downloaded and read page-by-page) confirms the title "Box Elder School District Logo Mini Badge assembly instructions," the full bill of materials (1 PCB in green or blue, 1 white-package 2200-ohm resistor at R1, 1 white SMD LED at D1, 4 two-pin headers), the "2022 COMPUDOC/SHIFTY" board silkscreen, and the train-logo graphic on the opposite face — matching both saved images pixel-for-pixel with the PDF''s own photos. The GitHub repo''s README (fetched via the GitHub API) reads verbatim "Badges Created for Saintcon 2022 - details and assembley instructions," and its file listing confirms this PDF sits alongside three other minibadge instruction sheets from the same maker. The official 2022 SAINTCON minibadge guide (downloaded, text-extracted) contains no "Box Elder," "BESD," or "CompuDoc" entry, and its own "DAVE TRAIN BADGE" (by SHIFTY, page 92) is a distinct, differently-built minibadge, so the earlier note that this badge sits outside the official guide holds up. No price, quantity, or availability information exists in any source, consistent with get_one.availability being left unknown. No schematic or Gerbers were found beyond the photographed assembly PDF, consistent with make_your_own.open_source: partial. Whether "CompuDoc" and "Shifty" are two people or one duo remains unconfirmed by any source; both are listed as makers per the board silkscreen, as before.'
last_modified_date: '2026-09-10'
---

The BESD Train Mini Badge is a SAINTCON 2022 trading minibadge, credited on its own silkscreen to "COMPUDOC/SHIFTY." Its assembly-instructions document titles it the "Box Elder School District Logo Mini Badge," and the finished board carries a train-silhouette graphic — almost certainly the school district logo the title refers to, and the likely source of "BESD" (Box Elder School District) in the badge's public-facing name.

Electrically it is one of the simplest minibadges in circulation: a single 2200-ohm resistor and one white SMD LED, soldered to a small rectangular PCB (available in green or blue) with four two-pin headers for mounting to a host badge. It carries no microcontroller, display, or radio — solder it together correctly, respecting the LED's polarity, and the single LED lights.

No pricing, production quantity, or availability information could be found; SAINTCON minibadges are generally made in small runs and traded in person at the conference's minibadge community space rather than sold, and nothing suggests this one was different. It is not listed in the official 2022 SAINTCON minibadge assembly guide, so it was likely distributed informally by its maker(s) rather than through the conference's official submission process.

## Make your own

The maker's GitHub repository (CompuDocUt/SaintConMinibadges) hosts a photographed, step-by-step assembly-instructions PDF for this badge, covering parts identification, LED polarity, and two methods for soldering the mounting pins straight. No schematic, Gerbers, or other design source files were found alongside it.
