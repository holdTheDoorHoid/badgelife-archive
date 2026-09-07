---
title: Space Grand Challenge Badge
id: dc31-space-grand-challenge-satellite-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: California Cybersecurity Institute (Cal Poly)
  url: https://cci.calpoly.edu/
  role: commissioned the badge, runs the Space Grand Challenge and the badge challenge site
- name: The Aerospace Corporation
  url: https://aerospace.org/
  role: co-sponsor; the back silkscreen reads "BY THE AEROSPACE CORPORATION AND CALIFORNIA CYBERSECURITY INSTITUTE" and the schematic title block says "for the Aerospace Corp and California Cybersecurity Institute"
- name: Alpenglow Industries
  url: https://www.alpenglowindustries.com/
  role: PCB design; the repo commits are by Carrie Sundra and by the GitHub account Robyn-Wright-Git (author names "BenWright-git" and "Robyn")
summary: A satellite-shaped blinky badge made for the Cal Poly California Cybersecurity Institute and The Aerospace Corporation, designed by Alpenglow Industries and intended for the DEF CON Aerospace Village. Twelve yellow LEDs on the solar panels flash in two alternating groups from a two-transistor oscillator while a thirteenth at the dish feed stays lit, and a ROT13 line on the dish plus a URL on the back lead to a beginner satellite-hacking challenge site.
functions: Two-transistor oscillator (two MMBT3904 in the classic astable multivibrator arrangement) alternately flashes two groups of six yellow 1206 LEDs on the solar panels; a thirteenth LED at the dish feed is on whenever the badge is on. One slide switch is ON/OFF and the other BLINK/SOLID; no microcontroller. The dish carries the ROT13 text "ZNL RZVG QVTVGNY QHFG" and the back carries the URL of the Satellite Badge Challenge site, which has multiple-choice Google Forms and a Space-Track.org TLE lookup puzzle for beginners.
look:
  colors:
  - purple
  - gold
  - yellow
  shape: satellite
  themes:
  - space
  - puzzle
  - ctf
  - security
  - logo
  form_factor: pcb badge
tech:
  mcu: none
  leds:
    count: 13
    type: discrete
    note: 'Yellow 1206 LEDs (Lite-On LTST-C150KSKT per the BOM): six on each solar panel, wired as two alternating groups of six (D1-D6 on one transistor, D8-D13 on the other, three per wing in each group), plus D7 at the dish feed, which is fed from the supply through its own resistor and stays lit'
  display: none
  connectivity:
  - none
  inputs:
  - slide switches
  power: CR2032
  battery: CR2032 in an SMT holder (Memory Protection Devices BK-912)
  sao_version: none
  sao_ports: 0
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  availability_note: No storefront found in any source; checked 2026-09-06.
  distribution:
  - village
  where: Intended for the DEF CON Aerospace Village. The DC30 announcement (June 2022) said the badge "will be at around at Aerospace Village"; the DC31 community sheet (June 2023) said "It will be for sale at their village". No price, quantity or attendee report was found.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/cal-poly-cci/Space_Grand_Challenge-AlpenglowIndustries
  firmware_url: null
  gerbers_url: https://github.com/cal-poly-cci/Space_Grand_Challenge-AlpenglowIndustries/tree/main/Gerbers
  bom_url: https://github.com/cal-poly-cci/Space_Grand_Challenge-AlpenglowIndustries/blob/main/Satellite_PCB_BOM.csv
  eda_tool: KiCad
  license: MIT
  notes: There is no firmware; the board is a passive transistor oscillator. The 2022 Alpenglow project (mirrored in the cal-poly-cci org) has the full KiCad 6 schematic, PCB, Gerbers, BOM with Digi-Key part numbers, schematic PDF and artwork under MIT. The 2023 repo holds only the KiCad PCB file (README says open it with KiCad 6, not 7) and a short video.
links:
- label: github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp./blob/main/README.md
  url: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp./blob/main/README.md
  kind: repo
- label: Space_Grand_Challenge-AlpenglowIndustries (GitHub) - full KiCad project, Gerbers, BOM, MIT
  url: https://github.com/cal-poly-cci/Space_Grand_Challenge-AlpenglowIndustries
  kind: repo
- label: AlpenglowIndustries/Space_Grand_Challenge (GitHub) - the original 2022 design repo
  url: https://github.com/AlpenglowIndustries/Space_Grand_Challenge
  kind: repo
- label: Satellite Badge Challenge site (URL printed on the back of the badge)
  url: https://spacecybernautctf.wixsite.com/badge
  kind: website
- label: Satellite Badge Challenges / Instructions
  url: https://spacecybernautctf.wixsite.com/badge/satellite-badge-challenges
  kind: website
- label: Short video of the badge blinking (in the 2023 repo)
  url: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp./blob/main/SGC%20badge%20Satellite23.mp4
  kind: video
- label: DEF CON forums - 2022 BadgeLife List (June 2022 announcement with a render)
  url: https://forum.defcon.org/node/240869
  kind: article
- label: Alpenglow Industries (business closed)
  url: https://www.alpenglowindustries.com/
  kind: website
- label: github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp.#readme
  url: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp.#readme
  kind: repo
images:
- file: assets/images/badges/dc31/space-grand-challenge-satellite-badge/front-leds-a.jpg
  source: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp./blob/main/SGC%20badge%20Satellite23.mp4
  credit: cal-poly-cci on GitHub (frame from the repo video)
  caption: Front of the purple satellite badge with the dish LED and one group of six panel LEDs lit; ROT13 message on the dish, Cal Poly CCI and Aerospace Corporation logos on the body
- file: assets/images/badges/dc31/space-grand-challenge-satellite-badge/front-leds-b.jpg
  source: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp./blob/main/SGC%20badge%20Satellite23.mp4
  credit: cal-poly-cci on GitHub (frame from the repo video)
  caption: The other group of six panel LEDs lit; the two groups alternate while the dish LED stays on
- file: assets/images/badges/dc31/space-grand-challenge-satellite-badge/render-2022.jpg
  source: https://forum.defcon.org/node/240869
  credit: hdanielson on the DEF CON forums (3D render)
  caption: 3D render of the front posted with the June 2022 forum announcement of the original run; the logo placement differs from the built board
contact: {}
notes:
- The DC31 sheet listed the maker as "Aerospace Village" and the item as "Space Grand Challenge Satellite Badge"; the back silkscreen reads "SPACE GRAND CHALLENGE BADGE" and the design files credit Cal Poly CCI, The Aerospace Corporation and Alpenglow Industries. The village is where it was to be handed out, not who made it.
- The same design was first announced for DEF CON 30 (forum post of 2022-06-10) and has a separate dc30 entry (dc30-califomia-cyber-institute-calpoly-san-luis-obispo) whose sheet row has the maker and item columns swapped.
- The 2023 PCB file has all 42 component footprints at the same positions as the 2022 layout; only the graphic footprints differ (the named Aerospace logo footprint is gone, two generic LOGO footprints were added and the CCI logo footprint moved). Board outline about 111 x 71 mm.
- 'Schematic title block: "Space Grand Challenge", rev A, 2022-04-20, part number SAT-0100.'
- Check their twitter feed as info becomes available (github link available)
- This is the same badge as dc31-space-grand-challenge-satellite-badge, which the community sheet listed separately under maker "Aerospace Village." That entry has photos and much more extensive sourcing (forum posts, the challenge website, the full BOM); this entry was filled in independently from the same GitHub repos and kept intentionally lighter to avoid duplicating that work.
status: announced
sources:
- kind: sheet
  event: dc31
  row: 2
  updated: '2023-06-14'
- kind: url
  url: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp./blob/main/README.md
  title: SGC-2023-Badge-Aerospacecorp. (GitHub README)
  accessed: '2026-09-06'
  note: The link from the sheet. README says the board was created for CCI and DEFCON 31 and to open the PCB with KiCad 6, not 7. Repo created 2023-05-02, last push 2023-05-15, all commits by hdanielson; contains only README, the KiCad PCB and a 14 MB video.
- kind: url
  url: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp./blob/main/defcon-badge-hw.kicad_pcb
  title: defcon-badge-hw.kicad_pcb (2023 PCB file)
  accessed: '2026-09-06'
  note: 'Parsed for footprints: 13 LED_1206, 17 x 1206 resistors, 2 x 10 uF caps, 2 SOT-23 NPN, 2 slide switches, CR2032 SMT holder, 5 test points, Alpenglow and CCI logo footprints; ON/OFF text; outline 111.1 x 70.8 mm. Nets: D1-D6 on the Q1 collector, D8-D13 on the Q2 collector, D7 between GND and R7 to +3V.'
- kind: url
  url: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp./blob/main/SGC%20badge%20Satellite23.mp4
  title: SGC badge Satellite23.mp4 (video in the 2023 repo)
  accessed: '2026-09-06'
  note: 'Portrait phone video of the finished purple board with gold panels: the two groups of panel LEDs alternate and the dish LED stays lit; source of the two front photos (cropped frames).'
- kind: url
  url: https://github.com/cal-poly-cci/Space_Grand_Challenge-AlpenglowIndustries
  title: Space_Grand_Challenge-AlpenglowIndustries (GitHub)
  accessed: '2026-09-06'
  note: 'Fork of the Alpenglow repo, full 2022 KiCad 6 project: description "A PCB in the shape of a satellite with a transistor oscillator circuit which creates alternating blinking LEDs, developed for the Aerospace Corp. and California Cybersecurity Institute"; MIT license (c) 2022 Alpenglow Industries; BOM (13 yellow LTST-C150KSKT LEDs, MMBT3904, BK-912 holder, EG1215AA switches); schematic text BLINK/SOLID, ON/OFF; title block dated 2022-04-20 rev A SAT-0100; commits May-June 2022 under the author names Carrie Sundra, BenWright-git and Robyn (the last two on the GitHub account Robyn-Wright-Git), one of which says prototypes were ordered on 2022-05-23; artwork files with the ROT13 string, a screenshot of its plaintext in a ROT13 tool, the badge name, the "BY THE AEROSPACE CORPORATION AND CALIFORNIA CYBERSECURITY INSTITUTE" line, the circled-A Aerospace logo and the back URL.'
- kind: url
  url: https://github.com/AlpenglowIndustries/Space_Grand_Challenge
  title: AlpenglowIndustries/Space_Grand_Challenge (GitHub)
  accessed: '2026-09-06'
  note: Original repo in the Alpenglow org, created 2022-05-06, same description and contents as the cal-poly-cci fork.
- kind: url
  url: https://github.com/cal-poly-cci
  title: cal-poly-cci (GitHub organization)
  accessed: '2026-09-06'
  note: Org name "California Cybersecurity Institute", description "Applications to support the CCI Space Grand Challenge initiatives"; holds the two badge repos.
- kind: url
  url: https://spacecybernautctf.wixsite.com/badge
  title: Home | Space Badge Challenge
  accessed: '2026-09-06'
  note: The site printed on the back of the badge. "Welcome to the Satellite Badge Challenge!", copyright 2023 by CCI, Satellite Badge Challenge; pages Home, Sponsors/About, Satellite Badge Challenges/Instructions, Satellite Basics/Resources.
- kind: url
  url: https://spacecybernautctf.wixsite.com/badge/satellite-badge-challenges
  title: Satellite Badge Challenges / Instructions
  accessed: '2026-09-06'
  note: Step 1 is four multiple-choice Google Forms; step 2 asks for a free Space-Track.org account and the missing characters from the NAVSTAR 27 TLE; answers are emailed to a calpoly.edu address. No hardware details.
- kind: url
  url: https://spacecybernautctf.wixsite.com/badge/services
  title: Sponsors/About - Satellite Badge Challenge
  accessed: '2026-09-06'
  note: Heading "Sponsors & Creators" lists Aerospace Corporation, California Cybersecurity Institute and "Alpenglowindustries"; says the satellite badge is a collaboration with Aerospace Corporation and CCI, that the purpose is to promote space and cybersecurity to "noobs", and that the challenges are for beginners.
- kind: url
  url: https://spacecybernautctf.wixsite.com/badge/about
  title: Satellite Basics / Resources - Satellite Badge Challenge
  accessed: '2026-09-06'
  note: Resource list (MITRE small-satellite best practices, Aerospace Corporation SPARTA, HackaSat, NASA material). Mentions the DEF CON Aerospace Village as a place for related activities.
- kind: url
  url: https://forum.defcon.org/node/240869
  title: 2022 BadgeLife List has Started!! - DEF CON Forums
  accessed: '2026-09-06'
  note: 'Post #3 by hdanielson, 2022-06-10: "Califomia Cyber Institute Calpoly San Luis Obispo has a Space Grand Challenge Badge! The badge is a satellite and will be at around at Aerospace Village. The badge will have a website with some beginner challenges."; attached a 3D render of the board (saved here).'
- kind: url
  url: https://forum.defcon.org/node/245049
  title: 2023 Badgelife List is Live!! - DEF CON Forums
  accessed: '2026-09-06'
  note: DC31 badgelife thread; no post mentions this badge, Cal Poly or the Space Grand Challenge.
- kind: url
  url: https://www.aerospacevillage.org/dc31-badge
  title: DC31 Badge | Aerospace Village
  accessed: '2026-09-06'
  note: The village's own DC31 badges were The Wright Stuff and the 50-unit Wright Flyer; this badge is not mentioned there.
- kind: url
  url: https://www.aerospacevillage.org/defcon-31
  title: DEF CON 31 (2023) | Aerospace Village
  accessed: '2026-09-06'
  note: Cal Poly California Cybersecurity Institute appears among the DC31 village sponsors; no badge details.
- kind: url
  url: https://cci.calpoly.edu/events/sgc-2023
  title: California Cybersecurity Institute (redirects to noyce.calpoly.edu/cybersecurity/)
  accessed: '2026-09-06'
  note: Redirects to the Noyce School of Applied Computing, which says it has "temporarily discontinued the Cybersecurity Institute and 5G Lab initiatives" and describes the Space Grand Challenge as "a game-based cybersecurity competition built by Cal Poly students". The 2023 event page itself no longer exists.
- kind: url
  url: https://mustangnews.net/california-cybersecurity-institute-hosts-space-grand-challenge-for-middle-and-high-school-students/
  title: California Cybersecurity Institute hosts "Space Grand Challenge" for middle and high school students - Mustang News
  accessed: '2026-09-06'
  note: 'Article of 2024-05-16: the seventh annual SGC (first held 2018) is a virtual game-based cybersecurity competition created by Cal Poly students for middle and high school students, who solved a compromised-satellite-company mystery; only a digital badge is mentioned, nothing about this PCB. Names a Henry Danielson as CCI Technical Curriculum Director.'
- kind: url
  url: https://www.alpenglowindustries.com/
  title: Alpenglow Industries
  accessed: '2026-09-06'
  note: Announces that Alpenglow has shut down and the storefront is closed; mentions Carrie and San Luis Obispo; does not mention the satellite badge.
- kind: url
  url: https://hackaday.io/alpenglow
  title: Alpenglow Industries on Hackaday.io
  accessed: '2026-09-06'
  note: Profile reads "Founded by engineer Carrie Sundra. San Luis Obispo, CA"; none of the listed projects is the satellite badge.
- kind: sheet
  event: dc31
  row: 20
  updated: '2023-02-14'
- kind: url
  url: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp.
  title: SGC-2023-Badge-Aerospacecorp. (GitHub)
  accessed: '2026-09-07'
  note: The link from the sheet. README says the board was created for CCI and DEFCON 31; repo holds only the README, a KiCad 6 PCB file and a video.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'Fact-checked 2026-09-06 against every cited source: hardware, makers, puzzle text, challenge site, forum announcement, sheet rows and all three images (the two photos are crops of frames 10 and 12 of the repo video; the render is the forum attachment) are confirmed. Corrections made during the check: the dish LED (D7) is fed directly from the supply and stays lit, only the twelve panel LEDs alternate; the back silkscreen line is "BY THE AEROSPACE CORPORATION AND CALIFORNIA CYBERSECURITY INSTITUTE" (the "for the Aerospace Corp..." wording is in the schematic); the Wix sponsor page spells it "Alpenglowindustries"; the Space Grand Challenge is described by its sources as a game-based competition, not a CTF, and nothing says it is free; the 2023 repo appeared in May 2023, not June. Not found in any source: a price, a quantity, whether the badge was actually handed out or sold at DEF CON 30 or 31 (both the 2022 forum post and the 2023 sheet only say it would be at the village), whether
    the 2023 run was a second batch or leftovers, and who at CCI ran it (the forum poster and the 2023 repo committer both use the handle hdanielson; Mustang News names a Henry Danielson at CCI, but that link is not confirmed by any source). The Aerospace Corporation''s "Aerospace at DEF CON 31" article (Cloudflare bot check) and the Alpenglow Tindie store (403) could not be read. The sheet''s maker "Aerospace Village" disagrees with the design files, which credit Cal Poly CCI, The Aerospace Corporation and Alpenglow Industries. Merged with duplicate entry ''Space Grand Challenge Badge'' (dc31-sgc-aerospace-corporation).'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc31/sgc-aerospace-corporation/
related:
- dc30-califomia-cyber-institute-calpoly-san-luis-obispo
---

The Space Grand Challenge is a game-based cybersecurity competition built by Cal Poly students and run by the university's California Cybersecurity Institute (CCI) for middle- and high-school students; its seventh edition in 2024 had players solve the mystery of a compromised satellite company. To promote space and cybersecurity to newcomers at DEF CON, CCI and The Aerospace Corporation had Alpenglow Industries of San Luis Obispo design a satellite-shaped PCB badge in spring 2022. The repo history shows the PCB layout and logo commits under the author names BenWright-git and Robyn (one GitHub account) and the schematic, title-block and BOM commits by Carrie Sundra, all between May and June 2022, with prototypes ordered on 2022-05-23; the schematic title block is dated 2022-04-20, rev A, part number SAT-0100. It was announced on the DEF CON forums on 2022-06-10 as coming to the Aerospace Village at DEF CON 30. In May 2023 a fresh repo with the PCB file and a video of a working unit appeared in CCI's GitHub org, and the DC31 community sheet listed the badge again in June 2023. That is why this entry exists alongside a dc30 one for the same design.

The badge is simple: no microcontroller, just a two-transistor oscillator (two MMBT3904s cross-coupled by 10 uF capacitors, the classic astable multivibrator) that alternately flashes two groups of six yellow 1206 LEDs on the solar-panel wings, three per wing in each group, while a thirteenth LED at the dish feed is fed straight from the CR2032 through its own resistor and stays lit. One slide switch turns it on and the other picks BLINK or SOLID. The purple board (about 111 x 71 mm) carries the Cal Poly CCI shield-and-text logo and The Aerospace Corporation's circled-A mark on the satellite body, and a ROT13 line, "ZNL RZVG QVTVGNY QHFG", curves across the dish. On the back are the badge name, the line "BY THE AEROSPACE CORPORATION AND CALIFORNIA CYBERSECURITY INSTITUTE", an Alpenglow logo and the URL of a Wix site called the Satellite Badge Challenge, which offers beginner puzzles: four multiple-choice forms and a Space-Track.org lookup of the NAVSTAR 27 two-line element. The site's Sponsors & Creators page names the Aerospace Corporation, CCI and Alpenglow, calls the badge a collaboration between the first two, and says the challenges are for beginners.

How the badge reached people is the least documented part. The 2022 forum post said it would be "at around" the Aerospace Village, the 2023 sheet said it would be for sale there, and no source found gives a price or a quantity. The Aerospace Village's own DC31 pages list Cal Poly CCI as a sponsor but describe only the village's Wright Stuff and Wright Flyer badges. Alpenglow Industries has since closed, and Cal Poly's Noyce School of Applied Computing, which now hosts the Space Grand Challenge pages, says the Cybersecurity Institute has been "temporarily discontinued", so the GitHub repos and the Wix site are what remains.

## Make your own

The complete 2022 project is on GitHub under an MIT license in both the Alpenglow and cal-poly-cci organizations: a KiCad 6 schematic and PCB, a Gerber set and drill files (including a zipped bundle ready for a fab), a BOM with Digi-Key part numbers, a schematic PDF and the artwork. Send `Gerbers/Satellite_PCB.zip` to any board house, order the seven purchasable BOM lines (13 yellow 1206 LEDs, 13 x 220 ohm and 4 x 47k 1206 resistors, two 10 uF 1206 capacitors, two MMBT3904 SOT-23 transistors, two EG1215AA slide switches and a BK-912 CR2032 holder; the eighth line is five test points with no part), and hand-solder them; the resistor and capacitor footprints are KiCad's hand-solder variants. Open the KiCad files with KiCad 6, since the 2023 README says to use KiCad 6 and not 7. There is no firmware to flash.

## Notes merged from the duplicate entry "Space Grand Challenge Badge"

This satellite-shaped badge was built for the Cal Poly California Cybersecurity Institute's Space Grand Challenge, sponsored by The Aerospace Corporation, for DEF CON 31. Rather than a microcontroller, the board runs a two-transistor astable-multivibrator oscillator that alternately blinks two groups of thirteen 1206 LEDs spread across the satellite's body and solar-panel wings, powered by a coin-cell battery. The design itself dates back to a 2022 project by Alpenglow Industries, released under the MIT license with full KiCad schematic, PCB, Gerbers and BOM; the DC31-specific repo linked from the community sheet only carries the PCB layout and a short demo video, but the underlying circuit and component list match the original Alpenglow project component-for-component.

This entry duplicates dc31-space-grand-challenge-satellite-badge, which the community sheet also listed (under the maker name "Aerospace Village") with photographs and considerably deeper sourcing, including the challenge website printed on the badge's back and contemporary forum posts. That entry should be treated as the primary record for this badge.

## Make your own

The original Alpenglow Industries repository (github.com/AlpenglowIndustries/Space_Grand_Challenge) has the complete KiCad 6 project - schematic, PCB layout, a footprint library, Gerbers and a bill of materials - under the MIT license. Since the board has no firmware, replicating it is a matter of fabricating the PCB from the supplied Gerbers and hand-soldering the BOM parts (LEDs, resistors, two transistors, switches and a CR2032 holder).
