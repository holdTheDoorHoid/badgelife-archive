---
title: DC801 DC24 Party Badge
id: dc24-dc801-dc24-party-badge
layout: badge
parent: DC24
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc24
year: 2016
makers:
- name: DC801
  url: https://github.com/DC801
summary: A Bluetooth LE party badge made by the Salt Lake City hackerspace DC801 for their DEF CON 24 party, with addressable LEDs and five onboard light-show modes.
functions: 'Powers up into one of 5 modes: a Knight Rider chase pattern, alternating red "eyes", a color strobe, a battery-level indicator (LED pairs show charge as a percentage of 3.7V), and randomly firing orange LEDs. In every mode the badge also broadcasts a URL over Bluetooth as an Eddystone beacon (once every 100ms), which recent-enough phones pick up as an automatic notification.'
look:
  colors:
  - black
  - orange
  shape: null
  themes:
  - security
  - party
tech:
  mcu: nRF51822 (Rigado BMD-200 module)
  leds:
    count: 12
    type: RGB + discrete
    note: 2 RGB LEDs plus 10 orange LEDs, addressable in pairs
  display: none
  connectivity:
  - ble
  battery: LiPo, charged via micro USB through an MCP73831 charge controller
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to attendees of DC801's party during DEF CON 24 (2016); a since-deleted DC801 tweet said supplies were "running low" as the party approached.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/DC801/DC24PartyBadge
  firmware_url: https://github.com/DC801/DC24PartyBadge
  eda_tool: Eagle
notes:
- 'From the user''s ''SAOs to buy'' link list (2026-09-07). Mirror: https://github.com/hamster/DC24PartyBadge'
- 'Sheet/list called it "DC24 Party Badge"; the maker''s own repo folder names the board "AccessBadge" internally, but the repo and README both describe it as the DC24 party badge, so the title is kept as-is.'
- 'Firmware and hardware source are published in the repo (Eagle files, gerbers, BOM, nRF SDK firmware), but no explicit open-source license file was found, hence open_source: partial rather than yes.'
status: released
sources:
- kind: url
  url: https://github.com/DC801/DC24PartyBadge
  title: DC801 DC24 Party Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc24''.'
- kind: url
  url: https://raw.githubusercontent.com/DC801/DC24PartyBadge/master/README.md
  title: 'DC801/DC24PartyBadge README'
  accessed: '2026-09-07'
  note: 'Confirms MCU (Rigado BMD-200 / nRF51822), LED count and layout, battery/charging, the 5 operating modes, and the Eddystone BLE beacon behavior.'
- kind: url
  url: https://forum.defcon.org/node/223495
  title: 'DC801 is hosting a party during DC24! - DEF CON Forums'
  accessed: '2026-09-07'
  note: 'Confirms DC801 hosted a DEF CON 24 party; page could not be fully retrieved (connection reset) so party logistics beyond this were not confirmed here.'
- kind: url
  url: https://x.com/dc801/status/1022158810339667969
  title: 'DC801 tweet: "Party Badges are running low for the #DC24 party"'
  accessed: '2026-09-07'
  note: 'Search-result snippet only (tweet not fetched directly); indicates the badge was given out at the party in limited supply.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core hardware facts (MCU, LEDs, battery, modes, BLE beacon) come directly from the maker''s own README, so those are solid. Price, exact quantity made, and full party/distribution logistics were not found — the badge appears to have been a free giveaway at DC801''s DEF CON 24 party rather than sold, based on the tweet snippet and distribution pattern of DC801''s other party badges, but no page stated a quantity or price outright. The DC801 party page (dc801.org) for DefCon 24 currently shows a "coming soon" placeholder with no archived content recovered. No maker photos of an assembled/soldered badge were found, only PCB CAD renders from the hardware repo, which are used as the images here.'
last_modified_date: '2026-09-07'
images:
  - file: assets/images/badges/dc24/dc801-dc24-party-badge/8e83182c41.jpg
    source: "https://github.com/DC801/DC24PartyBadge"
    credit: "DC801"
    caption: "PCB render of the DC24 party badge, top view (black and orange colorway)"
  - file: assets/images/badges/dc24/dc801-dc24-party-badge/5831a83f5d.jpg
    source: "https://github.com/DC801/DC24PartyBadge"
    credit: "DC801"
    caption: "PCB render of the DC24 party badge, bottom view"
contact: {}
links:
- label: github.com/DC801/DC24PartyBadge
  url: https://github.com/DC801/DC24PartyBadge
  kind: repo
- label: DC801 is hosting a party during DC24 (DEF CON Forums)
  url: https://forum.defcon.org/node/223495
  kind: article
---

DC801 is a Salt Lake City hackerspace with a long-running tradition of building electronic party badges for DEF CON attendees. For DEF CON 24 (2016), the group produced this Bluetooth LE badge, built around a Rigado BMD-200 module (a Nordic nRF51822 ARM Cortex-M0 chip with 256 kB flash and 32 kB RAM). The board carries two RGB LEDs and ten orange LEDs wired in addressable pairs, a single button, a JTAG header, and a MicroUSB port used purely for charging its onboard LiPo battery.

On power-up the badge cycles through one of five light-show modes — a Knight Rider-style chase, alternating red "eyes," a color strobe, a battery-charge indicator, and a mode that fires the orange LEDs at random. Independent of whichever mode is active, the badge continuously broadcasts a URL over Bluetooth Low Energy as an Eddystone beacon, so any nearby phone with Bluetooth on could pick up a notification pointing to DC801's content. It was handed out to people who attended DC801's DEF CON 24 party rather than sold; a DC801 tweet close to the event warned that badges were "running low." Hardware (Eagle schematics, board files, gerbers, BOM) and firmware source are both published in DC801's GitHub repository, making it a fully documented build for anyone wanting to replicate or study the design.
