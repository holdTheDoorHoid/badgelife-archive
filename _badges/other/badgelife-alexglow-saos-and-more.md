---
title: SAOcube (badgelife)
id: other-badgelife-alexglow-saos-and-more
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2018
makers:
- name: alexglow
  url: https://github.com/alexglow
summary: 'A cube-shaped "shitty add-on" (SAO) design by Alex Glow, published as KiCad source files and used as the example project for her Hackster.io tutorial on designing an SAO in KiCad with a Bantam desktop PCB mill.'
functions: ''
look:
  colors: []
  shape: cube
  themes: []
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
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/alexglow/badgelife/tree/master/SAOcube
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/alexglow/badgelife
  url: https://github.com/alexglow/badgelife
  kind: repo
- label: 'Hackster.io: Design a Sh*tty Add-On in KiCad'
  url: https://www.hackster.io/glowascii/design-a-sh-tty-add-on-in-kicad-06350f
  kind: article
images: []
contact: {}
notes:
- multiple SAO designs in one repo
- 'Repo description on GitHub is literally "SAOs... and more?"; only one design (SAOcube, files prefixed SAO_MVP) is actually present in the repo.'
status: unknown
sources:
- kind: url
  url: https://github.com/alexglow/badgelife
  title: badgelife (alexglow) — SAOs and more
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/alexglow/badgelife
  title: alexglow/badgelife — GitHub repo (README, file listing)
  accessed: '2026-09-07'
  note: 'Repo created Oct 2018, one project folder "SAOcube" containing KiCad schematic/PCB/gerbers named SAO_MVP (edge-cuts, F.Cu, drill file, .sch, .kicad_pcb, footprint libraries "sao.pretty" and "cube-cutout.pretty"). No license file, no images, no firmware.'
- kind: url
  url: https://raw.githubusercontent.com/alexglow/badgelife/master/README.md
  title: badgelife README.md
  accessed: '2026-09-07'
  note: 'README is one line: "SAOs... and more?" plus a link to a Hackster.io tutorial on designing a shitty add-on in KiCad using a Bantam desktop PCB mill.'
- kind: url
  url: https://www.hackster.io/glowascii/design-a-sh-tty-add-on-in-kicad-06350f
  title: 'Design a Sh*tty Add-On in KiCad (Hackster.io, author glowascii/Alex Glow)'
  accessed: '2026-09-07'
  note: 'Page blocked by Cloudflare bot protection when fetched directly; could not confirm tutorial content beyond the link itself.'
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched the GitHub repo root, the SAOcube subfolder listing, the raw README, the commit history, and the Hackster.io article; confirmed via the GitHub API that the repo carries no license (404 on /license). All confirmed: repo created Oct 29 2018 (first/only commit), single folder "SAOcube" holding KiCad schematic/PCB/gerbers/drill file prefixed SAO_MVP plus footprint libraries "sao.pretty" and "cube-cutout.pretty", no images anywhere in the repo, one-line README ("SAOs... and more?" + the Hackster.io link, "Uses KiCad + Bantam desktop PCB mill"). The Hackster.io tutorial page itself is still Cloudflare-blocked and could not be read beyond its title/URL and the README''s description of it. One correction from the prior pass: look.themes ("kit", "learn to solder") had no support in any source read — nothing confirms this was sold/given as a kit or that it teaches soldering (the tutorial is about KiCad design and PCB milling) — so themes was cleared to empty. This is a personal tutorial/example repo rather than a badge sold or distributed at a specific event; no event, chip, LEDs, price, quantity, or finished-board photos were found. Event left as "other" (no con/year association found); year (2018) is the repo''s creation year, not a confirmed event year. Status left "unknown" since there is no evidence this was ever released, sold, or given out versus remaining a personal design exercise. Every remaining non-empty field is now supported by a source actually read, so research.status is set to verified.'
last_modified_date: '2026-09-07'
---

"badgelife" is a small personal repository by Alex Glow (GitHub: alexglow, Hackster.io: glowascii) holding the design files for a single shitty add-on (SAO), despite the repo's tongue-in-cheek description promising "SAOs... and more?" The one project present, filed under a folder named SAOcube, is a KiCad design (schematic, PCB layout, Gerbers, and drill file, all prefixed SAO_MVP) with custom footprint libraries named "sao.pretty" and "cube-cutout.pretty" — the naming suggests the board was meant to form or mount to a small cube shape, though no photo of the assembled piece was found.

The repo's only documentation is a one-line README pointing to Alex Glow's Hackster.io tutorial, "Design a Sh*tty Add-On in KiCad," which walks through designing an SAO in KiCad and milling it on a Bantam desktop PCB mill; that page could not be retrieved for this write-up (it returned a Cloudflare bot-detection block). No event, year, chip, LED count, price, or distribution information was found in the repository itself — there is no license file and no populated-board photos — so this entry is best understood as a tutorial reference design rather than a badge or SAO known to have been produced, sold, or given away at a convention.
