---
title: Axonius Sponsor Badge
id: saintcon-2023-axonius-sponsor-badge
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: Jup1t3r
  url: https://github.com/tjhiker
summary: A SAINTCON 2023 sponsor minibadge for Axonius, given out at their conference booth.
functions: 'Two LEDs light up around a center pad; a solder jumper on the back picks between solid-on and blinking mode.'
look:
  colors: [white, black]
  shape: null
  themes: [minibadge, logo, sponsor]
tech:
  mcu: none
  leds:
    count: 2
    type: 0805 LED
    note: 'Solder jumper (JPR) on the back selects solid vs. blink.'
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution: [free_drop]
  where: 'Given out at the Axonius sponsor booth at SAINTCON 2023.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: 2023 SAINTCON Minibadge Assembly Guide
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  kind: doc
images:
- file: assets/images/badges/saintcon-2023/axonius-sponsor-badge/4431f91b32.jpg
  source: "https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf"
  credit: "SAINTCON"
  caption: "Front of the Axonius sponsor minibadge, silkscreen X pattern"
- file: assets/images/badges/saintcon-2023/axonius-sponsor-badge/cd547b9a35.jpg
  source: "https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf"
  credit: "SAINTCON"
  caption: "Back of the Axonius sponsor minibadge showing two LEDs, resistor, and the solid/blink jumper"
contact: {}
notes:
- 2023 sponsor minibadge for Axonius, with a jumper-selectable blink/solid LED mode. Found by the event-year sweep, task saintcon-2023.
- 'Sweep title matched the assembly guide''s heading exactly ("Axonius Sponsor Badge"); no change needed.'
status: released
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  title: Axonius Sponsor Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2023); event read as ''saintcon-2023''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  title: 2023 SAINTCON Minibadge Assembly Guide, p.10 (Axonius Sponsor Badge)
  accessed: '2026-09-10'
  note: 'Full assembly-guide page for this badge: designer credit, distribution (sponsor booth), difficulty/rarity, parts list (0805 LED, 0805 resistor, FR4 PCB, 2-pin headers), and front/back board photos.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed on the official 2023 SAINTCON Minibadge Assembly Guide (p.10): designed by Jup1t3r, given away at the Axonius sponsor booth, rated "intermediate" difficulty and "common" rarity, with 2x 0805 LEDs, an 0805 resistor, and a solder jumper selecting solid-on vs. blinking. No maker storefront, repo, or separate Axonius-branded page was found beyond the guide itself, so quantity made and any firmware/hardware source are left blank. Maker credit "Jup1t3r" appears to be the same designer active on GitHub as tjhiker (SAINTCON minibadge KiCad libraries, Jupigotchi), but that page does not mention this specific badge, so the maker url is given with medium confidence.'
last_modified_date: '2026-09-10'
---

The Axonius Sponsor Badge is one of the official sponsor minibadges from SAINTCON 2023, designed by Jup1t3r and given out to attendees who visited the Axonius booth on the conference floor. Like the other minibadges in that year's set, it is a small FR4 PCB meant to be soldered by hand and worn alongside a badge holder or lanyard.

The board carries two 0805 LEDs and a resistor around a solder-jumper pad on the back labeled "SOLID" and "BLINK": bridging one side or the other of the jumper decides whether the two LEDs stay lit continuously or blink. The front carries a simple X-shaped silkscreen pattern; the back is silkscreened with the AXONIUS wordmark.

The SAINTCON minibadge guide rates it "intermediate" difficulty to assemble and "common" for rarity, consistent with a sponsor giveaway rather than a limited-run design. No separate storefront, repository, or firmware exists for it as far as could be found; it is a hand-solder kit distributed for free at the sponsor's booth.
