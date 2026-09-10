---
title: I Learned to Solder
id: saintcon-2022-learn-2-solder-badge
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: Katie Lunceford (r0gu3bull3t)
  url: https://github.com/r0gu3bull3t
summary: A beginner-level SAINTCON 2022 minibadge built around a 555 timer circuit, combining through-hole and surface-mount parts to teach soldering fundamentals.
functions: A 555 timer circuit lighting a single LED, mounted on the back of the board for a backlit effect through the PCB text.
look:
  colors:
  - green
  shape: null
  themes:
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 1
    type: through-hole
    note: LED is mounted on the back of the board rather than the front, giving a backlit effect through the "I learned to solder" front silkscreen.
  display: none
  connectivity:
  - none
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: limited
  distribution:
  - kit
  - free_drop
  where: 'Given to attendees of the "Hot Soldering: Going With The Flow" training session at SAINTCON 2022, or by talking directly to the designer, Katie Lunceford (r0gu3bull3t). The official minibadge guide rates it "SUPER RARE".'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: A build guide (schematic/assembly instructions and a "Hot Soldering" training slide deck) is published on GitHub, but no PCB design files (Gerbers/schematic source) were found in the repo.
links:
- label: saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  kind: website
- label: r0gu3bull3t/SaintconLTS (build guide & training slides)
  url: https://github.com/r0gu3bull3t/SaintconLTS
  kind: repo
- label: r0gu3bull3t on badge.gallery
  url: https://badge.gallery/credits/r0gu3bull3t
  kind: website
images: []
contact: {}
notes:
- Official beginner soldering-teaching minibadge for SAINTCON 2022. Found by the event-year sweep, task saintcon-2022.
- 'The sweep''s entry title, "LEARN 2 SOLDER BADGE", is the sheet''s shorthand; the maker''s own badge guide names it "I learned to solder" (front silkscreen reads "I learned / to solder"), which is used as the title here.'
status: listed
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: LEARN 2 SOLDER BADGE
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2022); event read as ''saintcon-2022''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: MiniBadges of 2022 v2 (single-badge page, PDF)
  accessed: '2026-09-10'
  note: 'Read via the raw GitHub build guide, which reproduces the same page: name "I learned to solder", designer Katie Lunceford (@r0gu3bull3t), 555 timer circuit with THT+SMD parts, beginner difficulty, super-rare rarity, how-to-get-one text, front/back board photos, and assembly notes (R1/R2 are 1k 0805, R3 is 10k 1206; a wiring fix is needed between the ceramic cap and LED).'
- kind: url
  url: https://github.com/r0gu3bull3t/SaintconLTS
  title: r0gu3bull3t/SaintconLTS on GitHub
  accessed: '2026-09-10'
  note: Confirms maker and project name ("Learning to Solder badge for SAINTCON"); repo contains only LTSbuildguide.pdf and a Hot Soldering.pptx slide deck, no PCB source files.
- kind: url
  url: https://badge.gallery/credits/r0gu3bull3t
  title: r0gu3bull3t · Hacker Con Badges
  accessed: '2026-09-10'
  note: Third-party catalog entry corroborating the maker credit for the SAINTCON 2022 Learn 2 Solder minibadge; no additional technical detail or image found.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'The maker''s own build guide (mirrored on GitHub as LTSbuildguide.pdf) confirms the badge exists and supplied the core facts, but the maker''s repo holds no PCB design files, so make_your_own.open_source is only "partial" (assembly/training docs only). No standalone photo URL of the assembled board was found outside the PDF page itself, so no images could be saved. Price and quantity produced are not stated anywhere found; it appears to have been given away rather than sold.'
last_modified_date: '2026-09-10'
---

"I Learned to Solder" is a beginner-track SAINTCON 2022 minibadge designed by Katie Lunceford, known in the SAINTCON community as r0gu3bull3t. Rather than a decorative badge, it is explicitly a soldering-practice board: a 555 timer astable circuit built from a mix of through-hole parts (electrolytic capacitor, LED, DIP-8 555 timer) and surface-mount resistors (two 1k in 0805, one 10k in 1206). The single LED is deliberately placed on the back of the board so it backlights the "I learned / to solder" text silkscreened on the front.

The badge was distributed at SAINTCON 2022 to people who attended the "Hot Soldering: Going With The Flow" training session, or who spoke with Lunceford directly — making it a teaching aid as much as a collectible. The official 2022 minibadge guide rates its build difficulty as "Beginner" and its rarity as "Super Rare," and includes an assembly note flagging a wiring error in the original design (a jumper wire is needed between the ceramic capacitor and the LED to complete the circuit).

## Make your own

Lunceford published a build guide and an accompanying "Hot Soldering" training slide deck in the `r0gu3bull3t/SaintconLTS` GitHub repository. The repo does not include PCB design files (schematic source or Gerbers), only the PDF assembly guide and the presentation used in the training session, so this is only partially open-source: enough to follow along or teach the class, not enough to fabricate the board yourself.
