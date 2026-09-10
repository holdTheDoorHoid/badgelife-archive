---
title: Black flux-capacitor ESP badge (BSides Cape Town 2017)
id: bsides-cape-town-2017-black-flux-capacitor-esp-badge-bsides-cape-town-2017
layout: badge
parent: BSides Cape Town 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-cape-town-2017
year: 2017
makers:
- name: SensePost
  url: https://sensepost.com
summary: The WiFi half of BSides Cape Town 2017's two-part RFCat challenge badge, built around an ESP module with power-bank/USB charging and two rear buttons.
functions: Paired with the red CC1111 RFCat badge as one side of an RF communication challenge run at the con; the ESP's WiFi capability supported the challenge's network/web side while the red badge handled sub-GHz RF.
look:
  colors:
  - black
  shape: null
  themes:
  - radio
  - hardware tool
  - ctf
tech:
  mcu: ESP (2AL3B)
  leds: null
  display: null
  connectivity:
  - wifi
  battery: power bank via USB
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed to attendees at BSides Cape Town 2017 as part of the con's RFCat challenge badge set.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: badge.gallery/addons/bsides-cape-town-2017-rfcat-badge/black-flux-capacitor-esp-badge
  url: https://badge.gallery/addons/bsides-cape-town-2017-rfcat-badge/black-flux-capacitor-esp-badge
  kind: website
- label: 'SensePost: Building the BSidesCPT17 RFChallenge'
  url: https://sensepost.com/blog/2017/building-the-bsidescpt17-rfchallenge/
  kind: article
  archived: https://web.archive.org/web/20260130140502/https://sensepost.com/blog/2017/building-the-bsidescpt17-rfchallenge/
images:
- file: assets/images/badges/bsides-cape-town-2017/black-flux-capacitor-esp-badge-bsides-cape-town-2017/51c7e83404.jpg
  source: https://sensepost.com/blog/2017/building-the-bsidescpt17-rfchallenge/
  credit: SensePost
  caption: Front view of the black flux-capacitor ESP badge
  archived: https://web.archive.org/web/20260130140502/https://sensepost.com/blog/2017/building-the-bsidescpt17-rfchallenge/
- file: assets/images/badges/bsides-cape-town-2017/black-flux-capacitor-esp-badge-bsides-cape-town-2017/4ce22cdb7f.jpg
  source: https://sensepost.com/blog/2017/building-the-bsidescpt17-rfchallenge/
  credit: SensePost
  caption: Back of the badge showing the power bank/USB charging wiring
  archived: https://web.archive.org/web/20260130140502/https://sensepost.com/blog/2017/building-the-bsidescpt17-rfchallenge/
contact: {}
notes:
- 'Half of a two-part 2017 badge system: a black ESP-based (2AL3B ESP chip) badge with WiFi, power-bank wiring/USB charging, and rear buttons. Found by the event-year sweep, task bsides-bsides-cape-town.'
- Maker attribution corrected from the sweep's placeholder "BSides Cape Town 2017 event team" to SensePost, the security firm that built and wrote up the RFCat challenge on their blog.
status: released
sources:
- kind: url
  url: https://badge.gallery/addons/bsides-cape-town-2017-rfcat-badge/black-flux-capacitor-esp-badge
  title: Black flux-capacitor ESP badge (BSides Cape Town 2017)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-bsides-cape-town); event read as ''BSides Cape Town 2017''.'
- kind: url
  url: https://sensepost.com/blog/2017/building-the-bsidescpt17-rfchallenge/
  title: Building the BSidesCPT17 RFChallenge
  accessed: '2026-09-10'
  note: Maker's own write-up confirming the ESP chip (2AL3B), WiFi, power-bank/USB wiring, two rear buttons, and that this badge paired with a red CC1111 RFCat badge as a two-part challenge; source of both photos.
  archived: https://web.archive.org/web/20260130140502/https://sensepost.com/blog/2017/building-the-bsidescpt17-rfchallenge/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Confirmed on SensePost's own blog post, which describes building the challenge but does not state price, quantity made, or whether hardware/firmware files were published. No repo or Gerbers found; the post links only to a GitHub gist of challenge/server code, not badge design files, so make_your_own is left empty rather than guessed.
last_modified_date: '2026-09-10'
---

The black flux-capacitor badge was one half of the two-part hardware challenge BSides Cape Town built for its 2017 event. Made by the SensePost security team, it centered on an ESP-family chip (marked 2AL3B) that gave the badge WiFi connectivity, and was wired to a power bank over USB so attendees could use it all day without needing to recharge. Two buttons were soldered to the back of the board.

On its own the badge was the WiFi/network side of an RF communication challenge; it paired with a companion red badge built around a CC1111 chip (RFCat-compatible sub-GHz radio) to let players work across both halves of the puzzle. SensePost documented the build process, including photos of the badge's front and rear wiring, on their blog, but did not publish pricing, production quantity, or hardware/firmware design files for the board itself.
