---
title: PAC MAN Ghost SAO
id: dc34-pac-man-ghost-sao
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: NilbinSec
  url: https://uberflux.com/product/NS-SpectreSniffer
summary: A small pixel-ghost SAO shaped like a Pac-Man ghost, produced in four PCB
  colors with two LED eyes, made by NilbinSec for DEF CON 34.
functions: 'Two illuminated LED "eyes"; passive add-on powered and driven through
  the host badge''s add-on header (no onboard MCU of its own).'
look:
  colors:
  - purple
  - green
  - blue
  - red
  shape: ghost
  themes:
  - arcade
  - retro computer
  - pop culture
tech:
  mcu: none
  leds:
    count: 2
    type: reverse-mount
    note: Two SMD LEDs form the ghost's eyes.
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: Free via social-media drops and village giveaways; also bundled 1-of-4-colors
    (randomized) with NilbinSec's $80 Spectre Sniffer badge.
  price_usd: 0.0
  quantity: 1000+ announced for free drops/villages; also included with each of
    the 80 Spectre Sniffer badges sold
  availability: free
  availability_note: 'The bundled version sold out with the Spectre Sniffer badge
    (listed as "80 sold, 0 remaining" on Uberflux, checked 2026-09-06); the standalone
    free-drop/village distribution could not be independently confirmed as
    completed or ongoing.'
  distribution:
  - free_drop
  - village
  - purchase
  where: Announced as free drops on NilbinSec's social media and via supplies passed
    to DEF CON villages; one was also included at random (1 of 4 colors) with each
    Spectre Sniffer badge purchased from NilbinSec's Uberflux storefront.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- kind: store
  label: Spectre Sniffer Badge (includes a randomized Ghost SAO) - Uberflux
  url: https://uberflux.com/product/NS-SpectreSniffer
- kind: article
  label: Spectre Sniffer Badge by NilbinSec - DEF CON Forums
  url: https://forum.defcon.org/node/255986
images:
- file: assets/images/badges/dc34/pac-man-ghost-sao/836fd6f302.jpg
  source: https://uberflux.com/product/NS-SpectreSniffer
  credit: NilbinSec
  caption: The PAC-MAN Ghost SAO in its four available PCB colors - purple, green,
    navy blue, and red
contact:
  discord: '@nferno2'
  emails:
  - nilbinsec@gmail.com
  handles:
  - '@nilbinsec'
  raw:
  - on all the socials
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 5
  updated: 5/25/2026 19:56:22
  listing: New
- kind: url
  url: https://uberflux.com/product/NS-SpectreSniffer
  title: Spectre Sniffer Badge - Uberflux
  accessed: '2026-09-06'
  note: Confirms the Ghost SAO ships randomized in 1 of 4 PCB colors bundled with
    the $80 Spectre Sniffer badge; storefront shows 80 sold / 0 remaining.
- kind: url
  url: https://forum.defcon.org/node/255986
  title: Spectre Sniffer Badge by NilbinSec - DEF CON Forums
  accessed: '2026-09-06'
  note: Announcement post; confirms the $80 badge included one randomized PAC-MAN
    Ghost SAO and that proceeds funded free SAO giveaways at Hacker Summer Camp.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: This is a standalone SAO, not the main Spectre Sniffer badge (a separate
    archive entry, dc34-spectre-sniffer, covers that). It was distributed two ways
    that could not be fully reconciled from available sources - as one of 1000+
    free drops/village giveaways (per the original community sheet) and bundled
    1-of-4-colors with each of the 80 Spectre Sniffer badges sold on Uberflux
    (sold out as of this check). No dedicated hardware repo, Gerbers, or BOM for
    the Ghost SAO itself was found (only a separate GitHub repo exists for
    NilbinSec's unrelated DC34 badge-fuzzer SAO), so make_your_own fields are
    left empty. The SAO's connector footprint is marked "8P" in product photos,
    which does not match the standard 4-pin/6-pin SAO header, so tech.sao_version
    was left null rather than guessed. No dedicated project page (Hackaday.io,
    GitHub) specific to this SAO was located.
last_modified_date: '2026-09-06'
---

The PAC-MAN Ghost SAO is a small pixel-ghost add-on from NilbinSec, cut to the
shape of one of the classic Pac-Man ghosts and produced in four PCB colors -
purple, green, navy blue, and red. Each board carries two surface-mount LEDs
for eyes and is passive: it has no microcontroller of its own and lights up
only when powered through a host badge's add-on header.

NilbinSec distributed the Ghost SAO two ways at DEF CON 34. It was announced
as a free giveaway, with drops on social media and supplies handed off to
villages for further distribution. It was also bundled, one per badge in a
randomized color, with NilbinSec's $80 "Spectre Sniffer" badge - a separate
ghost-hunting themed badge (see the dc34-spectre-sniffer entry) built around a
Seeed XIAO ESP32-S3, an EMF detector, and a "Spirit Box" word generator. That
bundled run of 80 badges sold out; whether the wider free-drop giveaway of
1000+ units was completed could not be confirmed from available sources.

No dedicated hardware files, schematic, or Gerbers specific to the Ghost SAO
were found, so it is not currently documented as open source in this entry.
