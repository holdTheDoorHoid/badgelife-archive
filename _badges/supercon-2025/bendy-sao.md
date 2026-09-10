---
title: Bendy SAO
id: supercon-2025-bendy-sao
layout: badge
parent: Supercon 2025
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2025
year: 2024
makers:
- name: debraansell
  url: https://hackaday.io/debraansell
summary: An articulated PCB "balloon man" SAO built from multiple hinged boards that flex and twist while staying electrically connected through spring-contact slip rings.
functions: Twelve WS2812-compatible LEDs light up inside the translucent segments and animate as the boards are bent or twisted; runs standalone off the SAO connector or with an attached XIAO/QT Py microcontroller.
look:
  colors: []
  shape: null
  themes:
  - art
  - puzzle
tech:
  mcu: ATtiny3224
  leds:
    count: 12
    type: WS2812B
    note: side-emitting LEDs mounted to illuminate the translucent acrylic/PCB segments from inside
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
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/geekmomprojects/BendySAO
  firmware_url: https://github.com/geekmomprojects/BendySAO
  eda_tool: null
links:
- label: hackaday.io/project/198408-bendy-sao
  url: https://hackaday.io/project/198408-bendy-sao
  kind: hackaday
  archived: https://web.archive.org/web/20251119164527/https://hackaday.io/project/198408-bendy-sao
- label: github.com/geekmomprojects/BendySAO
  url: https://github.com/geekmomprojects/BendySAO
  kind: repo
images:
- file: assets/images/badges/supercon-2025/bendy-sao/936afa7f06.jpg
  source: https://hackaday.io/project/198408-bendy-sao
  credit: Debra Ansell
  caption: The Bendy SAO, an articulated PCB balloon-man figure that flexes while staying electrically connected
  archived: https://web.archive.org/web/20251119164527/https://hackaday.io/project/198408-bendy-sao
- file: assets/images/badges/supercon-2025/bendy-sao/77fc0fea23.jpg
  source: https://hackaday.io/project/198408-bendy-sao
  credit: Debra Ansell
  caption: Close-up of the Bendy SAO's articulated PCB joints and spring-contact slip rings
  archived: https://web.archive.org/web/20251119164527/https://hackaday.io/project/198408-bendy-sao
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198408-bendy-sao
  title: Bendy SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: supercon-addons); event read as ''Supercon 8 Add-On Contest — Fine Art category winner''.'
  archived: https://web.archive.org/web/20251119164527/https://hackaday.io/project/198408-bendy-sao
- kind: url
  url: https://hackaday.io/project/198408-bendy-sao
  title: Bendy SAO project page
  accessed: '2026-09-07'
  note: 'Core facts: maker (Debra Ansell), made for Supercon 8 (2024) SAO contest, ATtiny3224, 12 WS2812 LEDs, spring-contact hinge design, open-source design/firmware on GitHub.'
  archived: https://web.archive.org/web/20251119164527/https://hackaday.io/project/198408-bendy-sao
- kind: url
  url: https://github.com/geekmomprojects/BendySAO
  title: geekmomprojects/BendySAO
  accessed: '2026-09-07'
  note: Confirms open-source hardware and firmware; notes the design differs between a SuperCon America 2024 version and a SuperCon Europe 2025 version.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Made for the Supercon 8 (2024) SAO contest, but the maker's repo also documents a distinct revision released at SuperCon Europe 2025 — kept under this archive's supercon-2025 event folder since that is where it was already filed, but the original/primary version is the 2024 one. Price, quantity made, and current availability were not stated on either the Hackaday.io project page or the GitHub repo, so those fields are left empty. PCB color/shape were not clearly described in the text sources reviewed; left empty rather than guessed from thumbnails.
last_modified_date: '2026-09-07'
---

The Bendy SAO is Debra Ansell's (geekmomprojects) entry to Hackaday Supercon 8's SAO
contest in 2024, later revised for SuperCon Europe 2025. Rather than a single rigid
board, it is built from several separate PCB segments shaped like an inflatable
"tube man" balloon figure, hinged together with plastic push rivets so the whole
assembly can bend and twist. Electrical continuity across each joint is maintained
by a set of spring-loaded contacts and circular pads acting as a miniature slip
ring, a technique that grew out of Ansell's earlier "Articulated PCBs" experiments.

An ATtiny3224 drives twelve WS2812-compatible LEDs mounted to shine through the
translucent segments, animating as the figure is posed. It can run standalone off a
badge's SAO connector or be driven by an attached Seeed XIAO or Adafruit QT Py
board, with firmware written in MicroPython. Full hardware files, assembly
instructions, and code are published on GitHub, making it one of the more
completely open-sourced SAO designs from that contest.

## Make your own

Hardware design files, PDF assembly/programming guides, and MicroPython firmware
are available at the maker's GitHub repository, which documents separate
subdirectories for the SuperCon America 2024 and SuperCon Europe 2025 revisions of
the board.
