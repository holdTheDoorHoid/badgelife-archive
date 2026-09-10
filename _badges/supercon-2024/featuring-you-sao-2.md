---
title: Featuring You!
id: supercon-2024-featuring-you-sao-2
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Nanik Adnani
  url: https://hackaday.io/nanik
summary: A fully analog SAO shaped like a giant flashing red arrow that points up at the wearer and leaves space to write your name, built with an astable multivibrator and BJT LED drivers so it could be assembled by JLCPCB economic assembly for Supercon 8's SAO contest.
functions: Flashes a red arrow LED to draw attention to a hand-written name written on the board; no other interactive functions.
look:
  colors:
  - red
  shape: arrow
  themes:
  - text
tech:
  mcu: none
  leds:
    count: null
    type: discrete
    note: Driven by BJT buffers off an astable multivibrator, not addressable.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: The maker offered to hand out copies in person to interested attendees at Supercon 8.
make_your_own:
  open_source: true
  hardware_url: https://github.com/nanikgeorge/FeaturingYouSAO
  firmware_url: null
  eda_tool: KiCad
  notes: Repo also includes an LTspice simulation of the astable multivibrator circuit and a graphics folder for the artwork.
links:
- label: hackaday.io/project/198924-featuring-you
  url: https://hackaday.io/project/198924-featuring-you
  kind: hackaday
  archived: https://web.archive.org/web/20251112011013/https://hackaday.io/project/198924-featuring-you
- label: github.com/nanikgeorge/FeaturingYouSAO
  url: https://github.com/nanikgeorge/FeaturingYouSAO
  kind: repo
- label: github.com/nanikgeorge
  url: https://github.com/nanikgeorge
  kind: repo
- label: nanik.ca (maker portfolio)
  url: https://www.nanik.ca
  kind: website
images:
- file: assets/images/badges/supercon-2024/featuring-you-sao-2/f7eab93eb7.jpg
  source: https://hackaday.io/project/198924-featuring-you
  credit: Nanik Adnani
  caption: The Featuring You! SAO, a red flashing arrow with space to write your name
  archived: https://web.archive.org/web/20251112011013/https://hackaday.io/project/198924-featuring-you
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198924-featuring-you
  title: Featuring You!
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20251112011013/https://hackaday.io/project/198924-featuring-you
- kind: url
  url: https://hackaday.io/project/198924-featuring-you
  title: Featuring You! - Hackaday.io project page
  accessed: '2026-09-07'
  note: Confirmed maker, event (Supercon 8 SAO contest), circuit description (astable multivibrator with BJT LED drivers), JLCPCB economic assembly, free giveaway plan, and pulled the project photo.
  archived: https://web.archive.org/web/20251112011013/https://hackaday.io/project/198924-featuring-you
- kind: url
  url: https://github.com/nanikgeorge/FeaturingYouSAO
  title: nanikgeorge/FeaturingYouSAO
  accessed: '2026-09-07'
  note: Confirmed repo contents (KiCad PCB files, LTspice sim, graphics folder) and the maker's stated motivation (Supercon badges lack a place to write your name).
- kind: url
  url: https://raw.githubusercontent.com/nanikgeorge/FeaturingYouSAO/main/README.md
  title: FeaturingYouSAO README
  accessed: '2026-09-07'
  note: Confirms it is an SAO designed for Hackaday Supercon 2024, shaped like a flashing arrow sign for displaying the wearer's name; maker was speaking at Supercon 2024.
- kind: url
  url: https://raw.githubusercontent.com/nanikgeorge/FeaturingYouSAO/main/MovieMarqueeSAO_KiCAD/MovieMarqueeSAO.kicad_pcb
  title: MovieMarqueeSAO.kicad_pcb
  accessed: '2026-09-07'
  note: KiCad PCB file confirms no MCU; the board is a discrete analog circuit with 4x MMBT3904 transistors driving 32 discrete (0603) LEDs in a chase/flasher arrangement, the internal project name is "MovieMarqueeSAO".
- kind: url
  url: https://www.nanik.ca/projects
  title: Nanik Adnani portfolio - Projects
  accessed: '2026-09-07'
  note: Lists "Featuring You! SAO" as a Supercon 2024 project, describing it as a quick analog (no-microcontroller) circuit with a big flashing arrow displaying the wearer's name; links back to the same GitHub repo. No photo of the assembled hardware could be reliably identified on this page (a Google Sites export with many unlabeled background images).
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Verified against the Hackaday.io project page and GitHub repo: maker, Supercon 8 SAO contest event, astable-multivibrator/BJT-driven analog circuit, JLCPCB economic assembly, free giveaway plan, KiCad/LTspice repo contents, and the project photo (og:image) all confirmed directly on the cited pages. LED count is not stated by the maker; described only as a "giant flashing red arrow." Quantity made is not stated. No firmware exists since the board is purely analog (no MCU). Merged with duplicate entry ''Featuring You!'' (supercon-2024-featuring-you-sao).'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/supercon-2024/featuring-you-sao/
---

Featuring You! is a Simple Add-On built by Nanik Adnani for the SAO contest at Supercon 8 (2024). The maker noticed that Supercon's badges never leave a spot for attendees to write their own name, so this SAO fills that gap: a giant red arrow, built entirely from analog components, flashes to point down at a blank space where the wearer can write their name by hand.

The board has no microcontroller. A simple astable multivibrator circuit generates the flashing signal, and BJT transistors buffer that oscillator output to drive the arrow's LEDs, with resistors setting the current. The design was built specifically so it could go through JLCPCB's economic assembly service, keeping the SAO cheap to produce; the maker noted afterward that the LEDs came out brighter than intended and that a resistor value would be increased in a future revision, though the units handed out at Supercon work as built.

All hardware design files are open source, published on GitHub as KiCad PCB files, alongside an LTspice simulation of the multivibrator circuit and the graphics used on the board. The maker offered free copies to interested attendees at Supercon; no price, run size, or ongoing availability is stated.

## Notes merged from the duplicate entry "Featuring You!"

"Featuring You!" is a shitty add-on (SAO) designed by Nanik Adnani (an analog mixed-signal designer) to share at Hackaday Supercon 2024. The idea grew out of a simple complaint: Supercon badges are great, but they rarely have anywhere to put the wearer's name. Adnani's fix is a small board shaped like one of those big red flashing theater-marquee arrows, meant to "feature" whoever is wearing it.

Unlike most SAOs, it has no microcontroller. The KiCad design shows a purely discrete analog circuit: four MMBT3904 transistors arranged in astable-multivibrator-style chase stages, driving 32 individual 0603 LEDs to produce the arrow's flashing/chasing light pattern. The project also includes LTSpice simulation files for that flasher circuit and SVG artwork for the board edge and silkscreen (the internal project name in the files is "MovieMarqueeSAO").

The hardware design (KiCad project and PCB files) is published on GitHub, but there is no firmware to share since the board runs no code. Price, production quantity, and how (or whether) it was distributed beyond Supercon 2024 attendees were not stated in any source found.
