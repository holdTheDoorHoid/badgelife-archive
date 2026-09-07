---
title: Telephreak Eleven Badge (DC26)
id: dc26-telephreak-eleven-badge-dc26
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: dominotree
  url: https://spun.io
summary: A hand-assembled packet-radio badge for DEF CON 26 that lets nearby badges exchange images over the air using a store-and-forward mesh protocol.
functions: Beacons periodically and uses a store-and-forward radio protocol to request and receive images from other Telephreak 11 badges in range; images are held in SPI flash and shown on the badge's display.
look:
  colors: []
  shape: null
  themes:
  - radio
tech:
  mcu: null
  leds: null
  display: SPI display
  connectivity:
  - radio
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 'over 200 (maker hand-assembled "over 200 Telephreak badges" for DC26; ~20 working plus ~15 failed kits noted in an Aug 2018 update)'
  availability: sold_out
  distribution:
  - kit
  where: Distributed at DEF CON 26 (2018), reportedly in swag boxes as unassembled kits the maker hand-soldered/assembled.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://gitlab.com/dominotree/telephreak-11-badge
  eda_tool: null
  notes: 'The maker said they planned to release full schematics and source code after DEF CON 26. A GitLab repo (dominotree/telephreak-11-badge) is linked from a follow-up post; it could not be reached during research (Cloudflare challenge blocked automated access), so its contents are unverified.'
links:
- label: spun.io
  url: http://spun.io
  kind: website
- label: Telephreak 11 Badge Release Notes
  url: https://spun.io/2018/08/08/telephreak-11-badge-release-notes/
  kind: article
- label: Telephreak 11 Badge Update (bugs)
  url: https://spun.io/2018/08/09/telephreak-11-badge-update-bugs/
  kind: article
- label: 'Lessons from Running a Small-Scale Electronics Factory in my Guest Bedroom (Part 1: Design)'
  url: https://spun.io/2018/12/15/lessons-from-running-a-small-scale-electronics-factory-in-my-guest-bedroom-part-1-design/
  kind: article
- label: telephreak-11-badge (GitLab, source repo)
  url: https://gitlab.com/dominotree/telephreak-11-badge
  kind: repo
images:
  - file: assets/images/badges/dc26/telephreak-eleven-badge-dc26/1307adc895.jpg
    source: "https://spun.io/2018/08/08/telephreak-11-badge-release-notes/"
    credit: "dominotree (Nick Price)"
    caption: "Telephreak 11 badge photo shared with the release notes"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: http://spun.io
  title: Telephreak Eleven Badge (DC26)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 26''.'
- kind: url
  url: https://spun.io/2018/08/08/telephreak-11-badge-release-notes/
  title: Telephreak 11 Badge Release Notes
  accessed: '2026-09-07'
  note: 'Maker''s own release-notes post: badge purpose (hackable packet radio / image-sharing over SPI flash + store-and-forward radio), first-electronics-project context, promise to release schematics/source after DEF CON.'
- kind: url
  url: https://spun.io/2018/08/09/telephreak-11-badge-update-bugs/
  title: Telephreak 11 Badge Update (bugs)
  accessed: '2026-09-07'
  note: 'Confirms unassembled kits handed out in swag boxes, wiring/assembly notes, ~20 working / ~15 failed kits at time of posting, and links the GitLab source repo.'
- kind: url
  url: https://spun.io/2018/12/15/lessons-from-running-a-small-scale-electronics-factory-in-my-guest-bedroom-part-1-design/
  title: 'Lessons from Running a Small-Scale Electronics Factory in my Guest Bedroom (Part 1: Design)'
  accessed: '2026-09-07'
  note: 'Confirms maker hand-assembled "over 200" badges for DEF CON 26; badge included display, MCU, radio, and flash chip with SMD HC49 crystals; design retrospective, no exact chip model given.'
- kind: url
  url: https://gitlab.com/dominotree/telephreak-11-badge
  title: telephreak-11-badge (GitLab)
  accessed: '2026-09-07'
  note: 'Source repo linked from the maker''s update post; could not be fetched (Cloudflare bot-check blocked both WebFetch and curl), so hardware/firmware details from it are not confirmed.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s own blog (spun.io, Nick Price / dominotree) confirms this is a real, distributed badge from DEF CON 26 (2018): a packet-radio badge that exchanges images between units over a store-and-forward mesh, given out as unassembled kits with well over 200 hand-assembled by the maker. Exact MCU model, LED count/type, price, and precise final quantity were not stated in any source found and are left empty rather than guessed. The GitLab source repo (dominotree/telephreak-11-badge) is linked by the maker but sits behind a Cloudflare challenge that blocked automated fetch, so its contents (schematics, firmware, license) are unverified. The maker also made a follow-up badge, Telephreak 12, for DEF CON 27 (2019) — a WiFi deauth-frame detector on ESP32 — which is a separate item and reported separately, not folded into this entry.'
last_modified_date: '2026-09-07'
---

The Telephreak Eleven Badge was designed and hand-assembled by dominotree (Nick Price) for DEF CON 26 in 2018, his first electronics project. It is a hackable packet-radio badge: each unit periodically beacons and speaks a store-and-forward protocol so that nearby badges can request and exchange images with each other, holding the transferred image data in an onboard SPI flash chip and showing it on the badge's SPI-connected display. The maker built the whole design in about six weeks, going through nine PCB revisions before settling on the version handed out at the con.

Badges were given out at DEF CON 26 as unassembled kits in swag boxes, and the maker reports hand-assembling "over 200" of them himself — a project he later wrote about as running "a small-scale electronics factory" out of his guest bedroom. A same-week follow-up post acknowledged the badge shipped rough: buggy software, garbled radio transfers when several badges were in range at once, and a batch of about 20 working kits alongside roughly 15 that failed testing at the time of writing. The maker promised to publish full schematics and firmware after the con, and a GitLab repository (dominotree/telephreak-11-badge) is linked from that follow-up post, though it was unreachable during this research pass (blocked by a Cloudflare bot check) so its contents are unconfirmed.

## Make your own

The maker's stated intent was open hardware and firmware, published at https://gitlab.com/dominotree/telephreak-11-badge after DEF CON 26. This research pass could not verify the repo's contents (access blocked); anyone following up should check that link directly for schematics, source, and license terms.
