---
title: Mass Warp Gate Badge
id: other-mass-warp-gate-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2023
makers:
- name: seeigecannon
  url: https://github.com/seeigecannon
summary: A Mass Effect-themed "mass relay" badge built from discrete logic (no microcontroller) that keeps a 4-digit HH:MM clock on custom LED segment displays, with concentric PCB rings meant to be cut from mouse-bited panels and turned by a small motor.
functions: Runs as a standalone digital clock (hours and minutes) driven entirely by discrete counter/logic ICs rather than firmware; a "TimeKeeper" logic block feeds four custom 7-segment-style LED digit displays. Includes a motor connector (with an on/off switch), apparently to spin the badge's outer ring(s) like the Mass Effect "mass relay" it is modeled after.
look:
  colors:
  - green
  shape: ring
  themes:
  - sci-fi
  - space
tech:
  mcu: none
  leds:
    count: null
    type: discrete
    note: Dozens of individual through-hole LEDs (labeled DA1-DF4, etc.) arranged into four custom segment-style digits rather than off-the-shelf 7-segment packages.
  display: custom LED segment display (4-digit HH:MM clock)
  connectivity: []
  battery: 4x AAA (also accepts external/USB power via a separate input jack)
  sao_version: v1
  sao_ports: 2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/seeigecannon/MassWarpGateBadge
  firmware_url: null
  eda_tool: KiCad
  license: Unlicense
  fab_url: null
  notes: Repo includes KiCad schematic/PCB/DRU files, Gerbers, a schematic PDF, and Fusion 360 (.f3d) plus DXF files for the ring-shaped mechanical pieces (inner/outer/center rings, ring covers, mouse-bite panelization, a "shepard.dxf" cutout). No firmware is present since the clock logic is implemented in discrete ICs, not a microcontroller.
links:
- label: github.com/seeigecannon/MassWarpGateBadge
  url: https://github.com/seeigecannon/MassWarpGateBadge
  kind: repo
images:
  - file: assets/images/badges/other/mass-warp-gate-badge/0432aaffe6.jpg
    source: "https://github.com/seeigecannon/MassWarpGateBadge"
    credit: "seeigecannon"
    caption: "3D CAD render of the front of the Mass Warp Gate Badge PCB, an early rectangular electrical prototype with a 4-digit LED clock display"
  - file: assets/images/badges/other/mass-warp-gate-badge/abacf2b424.jpg
    source: "https://github.com/seeigecannon/MassWarpGateBadge"
    credit: "seeigecannon"
    caption: "3D CAD render of the other side of the prototype board, showing the discrete-logic clock circuitry (LED digit array, logic ICs, set switches) and the external/USB power connector"
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: unknown
sources:
- kind: url
  url: https://github.com/seeigecannon/MassWarpGateBadge
  title: Mass Warp Gate Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://raw.githubusercontent.com/seeigecannon/MassWarpGateBadge/main/schematic.pdf
  title: MassWarpGateBadge schematic.pdf
  accessed: '2026-09-07'
  note: Confirms discrete-logic ("TimeKeeper") clock design, 2x SAO headers (J5/J6), 4x AAA battery holder plus external/USB power input, and a motor connector with an on/off switch; no MCU present.
- kind: url
  url: https://api.github.com/repos/seeigecannon/MassWarpGateBadge/commits
  title: MassWarpGateBadge commit history
  accessed: '2026-09-07'
  note: Repo created July 2023, with Gerbers and Fusion 360 files added August 2023; used to date the project since no event/year is stated anywhere on the page.
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    Fact-check pass (2026-09-07): re-fetched the repo, its commit history, and
    the schematic.pdf (rendered locally to PNG page-by-page with pdftoppm,
    since pdftotext again returned no text) and confirmed every technical
    claim directly against the schematic: no MCU anywhere on the 7 sheets
    (only 4000-series/74LS logic -- CD4060 oscillator off a 32.768kHz crystal,
    4027/4520B counters, 4081 gates, 74LS247 BCD-to-7-segment decoders), a
    "TimeKeeper" sheet feeding four 7-segment-display sheets (1 min/10 min/1
    hr/10 hr = HH:MM), two headers labeled "SAO" (J5/J6), a 4x AAA holder plus
    a separate USB/ext-power jack (J7) gated by an SPDT switch so the two
    can't both feed VCC at once, and a 2-pin "Motor" connector (J2) with its
    own on/off switch. Corrected two spots that overstated the motor
    connector as a "motor driver" -- the schematic shows only a switch and
    connector, no driver IC/H-bridge. Also corrected the back-image caption,
    which claimed the render shows the SAO headers and battery/USB inputs;
    zooming the saved image shows only the LED array, logic ICs, set
    switches, and the J7 power connector -- the SAO headers and AAA holder
    aren't visible in that particular render, so the caption now describes
    only what the image actually shows. Both images matched their sources
    (github.com/seeigecannon/MassWarpGateBadge) and depict this item. The
    repo (created and last updated August 2023) still has no README, no
    stated event, con, or price/availability info, and the GitHub description
    field is empty -- this looks like a personal project shared for others to
    build rather than something sold or distributed at a specific con, so
    event stays "other" and status "unknown" rather than guessed. The DXF file
    set (innerRing/outerRing/centerRings/ringCovers/mouseBites/shepard)
    strongly implies the finished badge is a round, ring-shaped "mass relay"
    model cut from a rectangular panel, but the only images in the repo are
    CAD renders of the flat rectangular electrical-prototype board
    (silkscreened "Badgelife Electrical Prototype"), not the assembled
    ring-shaped final piece, so look.shape ("ring") is inferred from the
    mechanical files rather than a photo of the finished item -- this is the
    reason confidence stays "low" despite every stated technical fact being
    directly confirmed. No firmware exists because the clock logic is
    discrete ICs, not a microcontroller. Noted but not added to this entry:
    the same GitHub user (seeigecannon) also has DC404TrainingBadge ("DC404
    Learn to Solder Badge") and DC27EnterpriseBadge ("Enterprise Badge for
    DC27") repos, which look like separate badgelife entries worth their own
    research pass.
last_modified_date: '2026-09-07'
---

The Mass Warp Gate Badge is a Mass Effect-themed take on the SAO badge format by GitHub user seeigecannon, built around the games' "mass relay" warp gates rather than any single armor or weapon. Instead of a microcontroller, the badge's four-digit HH:MM clock is driven entirely by a discrete-logic "TimeKeeper" counter board feeding custom LED segment digits -- an unusual choice for a badgelife project, most of which lean on an ESP32 or ATtiny. The board carries two SAO headers so it can also host other people's add-ons, runs off four AAA batteries or an external power jack, and includes a motor connector (with its own on/off switch) that appears intended to spin part of the badge, echoing the rotating rings of the in-game mass relay.

The repository, posted in mid-2023 and released under the Unlicense, contains the full KiCad schematic and PCB, Gerbers, and a set of Fusion 360 and DXF files for cutting the badge's concentric ring pieces (inner ring, outer ring, center rings, ring covers) from a mouse-bit panel, plus a "shepard.dxf" cutout referencing the Mass Effect protagonist. No firmware is included, since the clock is built from discrete logic rather than code. The two images in the repo are CAD renders of a flat rectangular test board labeled "Badgelife Electrical Prototype," not the final assembled ring shape, and nothing in the repo says which con (if any) it was built for, whether it was ever sold, or how many exist.
