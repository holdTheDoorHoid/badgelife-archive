---
title: TROOPERS22 Badge
id: troopers-2022-troopers22-badge
layout: badge
parent: Troopers 2022
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: troopers-2022
year: 2022
makers:
- name: Badge.Team
  url: https://badge.team/
- name: Jeff Gough (jeffmakes)
  url: https://github.com/jeffmakes
  role: hardware/firmware design
- name: hnzlmnn
  url: https://x.com/hnzlmnn
  role: hardware/firmware design
summary: The official conference badge for TROOPERS22 (Heidelberg, June 2022), a shield-shaped ESP32 board with an e-paper display and capacitive touch QWERTY keyboard, running Badge.Team's MicroPython platform.
functions: Runs Badge.Team's ESP32 MicroPython app platform (the same badge-launcher environment used on SHA2017/MCH2022-family badges); shows text and status on its e-paper screen; a capacitive touch keyboard and two nav buttons provide input; a hobbyist later repurposed one as a WiFi doorbell that flashes "please ring" / "do not disturb" and pings Home Assistant.
look:
  colors:
  - black
  - gold
  shape: shield
  themes:
  - security
  - text
tech:
  mcu: ESP32-WROVER-B
  leds: 
    type: WS2812
    note: Addressable status LEDs; exact count not confirmed.
  display: 2.9" e-paper (TR19-compatible, SSD1675-class controller)
  connectivity:
  - wifi
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
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: badge.gallery/badges/troopers22-badge
  url: https://badge.gallery/badges/troopers22-badge
  kind: website
- label: pid.codes/1209/2020
  url: https://pid.codes/1209/2020/
  kind: website
- label: 'GitHub: esp32-badge-doorbell (third-party teardown/rebuild)'
  url: https://github.com/Niclassslua/esp32-badge-doorbell
  kind: repo
- label: 'Badge.Team: badge.team'
  url: https://badge.team/
  kind: website
images:
- file: assets/images/badges/troopers-2022/troopers22-badge/b242b6f7e1.jpg
  source: "https://github.com/Niclassslua/esp32-badge-doorbell"
  credit: "Niclassslua"
  caption: "TROOPERS22 badge (shield-shaped PCB with e-paper display and capacitive touch keyboard), later repurposed as a smart doorbell"
contact: {}
notes:
- Badge.Team-built conference badge for Troopers 2022 using the shared Badge.Team firmware/PID.codes platform. Found by the event-year sweep, task con-troopers.
- 'The sweep''s source (badge.gallery) had almost no hardware detail confirmed at the time it was seeded; the ''pid.codes/1209/2020'' link it carried actually resolves to an unrelated project (Gate Crystal / CaptainCredible), not this badge — kept in links for traceability but it does not support any claim below.'
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/troopers22-badge
  title: TROOPERS22 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-troopers); event read as ''Troopers 2022''.'
- kind: url
  url: https://github.com/Niclassslua/esp32-badge-doorbell
  title: ESP32 Badge Doorbell (README, CLAUDE.md, docs/hardware-assumptions.md, docs/recover-original-firmware.md)
  accessed: '2026-09-08'
  note: 'Third-party teardown/repurposing of an actual TROOPERS22 badge; confirms it is a physical ESP32-WROVER-B board with a 2.9" e-paper display (same panel as the TR19 badge), WS2812 LEDs, an Azoteq IQS550 capacitive touch keyboard, a PCA9555 I/O expander for nav buttons, a DRV2605L haptic driver, and stock MicroPython firmware over a single I2C bus. Photo confirms a shield-shaped PCB with "TROOPERS" / "ERNW SECTOOLS RESEARCH" silkscreen.'
- kind: url
  url: https://badge.team/
  title: Badge.Team
  accessed: '2026-09-08'
  note: "Badge.Team's own site lists SHA2017, HackerHotel 2019/2020/2024, and MCH2022 as badges they built; it does not list Troopers, so Badge.Team's role here is corroborated by the GitHub platform match (MicroPython app launcher) and the tweet below, not by their own site."
- kind: url
  url: https://x.com/jeffmakes
  title: Jeff Gough (@jeffmakes) on X
  accessed: '2026-09-08'
  note: 'Search-indexed post (no stable permalink recovered): "The #TROOPERS22 badge is really great! Good work @jeffmakes @hnzlmnn @BadgeteamNL @WEareTROOPERS #TR22" — a third party crediting jeffmakes, hnzlmnn, and Badge.Team for the badge; used as supporting evidence for makers, not sole confirmation.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Existence and core hardware are confirmed by a third-party teardown/rebuild (real photo, chip-level probing), not by an official Badge.Team hardware page or firmware repo — unlike Troopers 2023/2024, badgeteam''s GitHub org has no troopers22-firmware repo, so no primary design files were found. Maker credit (Badge.Team + jeffmakes + hnzlmnn) rests on a third-party social-media post, not the makers'' own confirmation; treat as likely but not certain. Price, quantity made, distribution method, battery, and exact LED count are undocumented anywhere found. No SAO header confirmed. Body color read as very dark navy/black from the photo; could be a dark blue mask rather than true black.'
last_modified_date: '2026-09-08'
---

The TROOPERS22 badge was the conference badge for TROOPERS22, held by ERNW in Heidelberg in June 2022. It is a shield-shaped PCB — a nod to the "TROOPERS"/security branding, with "ERNW SECTOOLS RESEARCH" and "TROOPERS" silkscreened on the front — built around an ESP32-WROVER-B module with 16 MB of flash. A 2.9" e-paper display (the same panel used on the earlier TR19 badge) sits above a full capacitive-touch QWERTY keyboard driven by an Azoteq IQS550 controller, with WS2812 addressable LEDs, a DRV2605L haptic driver, and a PCA9555 I/O expander for two side navigation buttons, all sharing one I2C bus. It ships running Badge.Team's MicroPython-based ESP32 app platform, the same launcher environment used on SHA2017- and MCH2022-family badges, which is the strongest technical link tying this badge to Badge.Team.

No official hardware or firmware repository for the 2022 badge specifically has surfaced — Badge.Team's GitHub only has public firmware repos for Troopers 2023 and 2024 — so most of what's documented here comes from a hobbyist project (Niclassslua's `esp32-badge-doorbell`) that dumped and probed an original TR22 badge in detail while converting it into a battery-powered doorbell sign. A contemporaneous social-media post crediting jeffmakes, hnzlmnn, and Badge.Team (@BadgeteamNL) alongside the TROOPERS22 organizers supports Badge.Team's involvement, though it is third-party corroboration rather than the makers' own writeup.

Price, quantity produced, and how badges were distributed to attendees are not documented in any source found during this pass.
