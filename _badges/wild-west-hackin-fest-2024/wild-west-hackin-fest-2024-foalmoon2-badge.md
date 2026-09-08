---
title: Wild West Hackin' Fest 2024 Attendee Badge (FoalMoon2)
id: wild-west-hackin-fest-2024-wild-west-hackin-fest-2024-foalmoon2-badge
layout: badge
parent: Wild West Hackin' Fest 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: wild-west-hackin-fest-2024
year: 2024
makers:
- name: ustayready
  url: https://x.com/ustayready
summary: The 2024 Wild West Hackin' Fest attendee badge, code-named "FoalMoon2" on the device itself, is an ESP32-S3 badge with an OLED screen and two buttons built around an intergalactic bounty-hunting CTF.
functions: Displays battery level, WiFi signal strength, MAC address and captured "bounties" on its OLED screen; connects to the "WWHF Badges" WiFi hotspot and an MQTT/AWS backend to receive CTF events; reads a Mifare Classic 1K NFC tag when scanned at vendor/speaker booths to collect one of 25 bounties; one button navigates between screens.
look:
  colors:
  - white
  shape: rectangle
  themes:
  - space
  - ctf
  - security
tech:
  mcu: ESP32-S3-WROOM-1
  leds:
    count: 2
    type: discrete
    note: One LED blinks during boot; a second status LED shows blue/white/green/red states.
  display: OLED
  connectivity:
  - wifi
  - nfc
  - mqtt
  battery: battery-powered with power switch
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to attendees of Wild West Hackin' Fest 2024 as the conference badge.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  bom_url: https://github.com/ustayready/wwhf_2024_badge/blob/main/WWHF_2024_BOM_ATTENDEE_V6.csv
  eda_tool: null
links:
- label: shadylink.lol/blog/2024-10-11_WildWestHackinFestBadgeCTF
  url: https://shadylink.lol/blog/2024-10-11_WildWestHackinFestBadgeCTF/
  kind: website
- label: wildwesthackinfest.com
  url: https://wildwesthackinfest.com/
  kind: website
- label: ustayready/wwhf_2024_badge (BOM)
  url: https://github.com/ustayready/wwhf_2024_badge
  kind: repo
images:
- file: assets/images/badges/wild-west-hackin-fest-2024/wild-west-hackin-fest-2024-foalmoon2-badge/e070db190c.jpg
  source: "https://shadylink.lol/blog/2024-10-11_WildWestHackinFestBadgeCTF/"
  credit: "Wild West Hackin' Fest / ustayready"
  caption: "The WWHF 2024 attendee badge: white PCB with ESP32-S3, OLED screen, and two buttons"
contact: {}
notes:
- ESP32-S3 badge with OLED, two buttons and NFC used for an intergalactic bounty-hunting CTF at WWHF 2024, connecting to AWS/MQTT infrastructure. Found by the event-year sweep, task con-kernelcon.
- 'The sweep''s title read "Wild West Hackin'' Fest 2024 FoalMoon2 Badge" and credited "Wild West Hackin'' Fest / Black Hills Information Security" as maker; a teardown write-up (shadylink.lol) identifies "FoalMoon2" as an internal device/hostname visible on the badge''s OLED and WiFi output, not a public product name, and attributes the badge design to GitHub user ustayready, who published its attendee BOM. No hardware/firmware repo or Gerbers were found; only the BOM CSV is public.'
status: released
sources:
- kind: url
  url: https://shadylink.lol/blog/2024-10-11_WildWestHackinFestBadgeCTF/
  title: Wild West Hackin' Fest 2024 Badge CTF - Beep Boop I do computer
  accessed: '2026-09-08'
  note: Primary source; teardown describing chip, OLED, buttons, NFC tag, WiFi/MQTT CTF mechanics, and badge photo.
- kind: url
  url: https://github.com/ustayready/wwhf_2024_badge
  title: ustayready/wwhf_2024_badge
  accessed: '2026-09-08'
  note: Maker's repo confirming authorship and containing the attendee badge BOM (WWHF_2024_BOM_ATTENDEE_V6.csv).
- kind: url
  url: https://wildwesthackinfest.com/
  title: Wild West Hackin' Fest
  accessed: '2026-09-08'
  note: Checked for badge/CTF mentions; current site only covers 2026/2027 events, no 2024 badge content found.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Maker attribution comes from a GitHub BOM repo (ustayready) rather than an explicit "designed by" statement, and no hardware or firmware repo was found to confirm the ESP32-S3 pinout or open-source status beyond the BOM. Price/quantity not stated anywhere found; it was a free attendee badge, not sold. Could not confirm whether Black Hills Information Security (the sweep's original maker credit) was formally involved versus ustayready being an independent designer/vendor for WWHF.
last_modified_date: '2026-09-08'
---

The 2024 Wild West Hackin' Fest attendee badge is an ESP32-S3-WROOM-1 board with a small OLED display and two push buttons, given free to attendees of the Deadwood, South Dakota conference. Its firmware carries the internal name "FoalMoon2," visible on the badge's boot screen and in its WiFi behavior, though this appears to be a device codename rather than a marketed product title. The badge was built around an intergalactic bounty-hunting CTF: it joined a "WWHF Badges" WiFi network and talked to an MQTT/AWS backend to receive live events, while a built-in Mifare Classic 1K NFC tag let attendees "capture" one of 25 bounties by scanning their badge at vendor and speaker booths. The OLED screen tracked battery level, WiFi signal strength, the badge's MAC address, and bounty progress.

GitHub user ustayready published the attendee badge's bill of materials, which is the only build documentation found; no schematic, PCB, or firmware repository surfaced during research. A detailed teardown of the badge's firmware and NFC/WiFi behavior was published by the site shadylink.lol shortly after the 2024 event.
