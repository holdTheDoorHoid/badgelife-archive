---
title: Hak4Kidz DEF CON 27 Badge
id: dc27-hack-4-kids-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Hak4Kidz
  url: https://www.hak4kidz.com/
summary: A puzzle badge from the youth ethical-hacking nonprofit Hak4Kidz, built around a color TFT screen styled as a cryptex that hides a challenge behind capacitive touch pads.
functions: A cryptex-unlocking puzzle challenge navigated with 6 capacitive touch pads around the screen; programmable over USB via a micro SD card slot for flashing the ESP32.
look:
  colors: []
  shape: null
  themes:
  - puzzle
  - learn to solder
  - security
  - mascot
tech:
  mcu: ESP32
  leds: null
  display: 2.4" 240x320 color TFT LCD
  connectivity:
  - wifi
  - bluetooth
  - usb
  battery: USB
  sao_version: null
get_one:
  price: $100
  price_usd: 100
  quantity: '200'
  availability: sold_out
  distribution:
  - crowdfunding
  - purchase
  where: Kickstarter campaign (ended July 1, 2019); pickup at DEF CON 27 in Las Vegas or shipped
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
- label: hackster.io - Hak4Kidz Is Making a DEF CON 27 Indie Badge Just for Kids
  url: https://www.hackster.io/news/hak4kidz-is-making-a-def-con-27-indie-badge-just-for-kids-a2a0b7a3dd19
  kind: article
- label: Kickstarter - Hak4Kidz DEF CON 27 Indie Badge
  url: https://www.kickstarter.com/projects/h4k/hak4kidz-def-con-27-indie-badge
  kind: store
- label: Hak4Kidz
  url: https://www.hak4kidz.com/
  kind: website
images:
- file: assets/images/badges/dc27/hack-4-kids-badge/e0cacaf1c4.jpg
  source: "https://www.hackster.io/news/hak4kidz-is-making-a-def-con-27-indie-badge-just-for-kids-a2a0b7a3dd19"
  credit: "Hak4Kidz / Hackster.io (Cameron Coward)"
  caption: "Hak4Kidz DEF CON 27 badge, featuring the Tinker mascot and cryptex design around the color TFT screen"
contact: {}
notes:
- Charity-themed badge from the GrrCON organizers shown at DEF CON 27. Found by the event-year sweep, task dc27-badges.
- The sweep's sheet attributed this to "GrrCON organizers" and titled it "Hack 4 Kids Badge." Sources instead identify the maker as Hak4Kidz (a youth ethical-hacking nonprofit); Hackaday notes the design was "originally designed for GrrCON" before being sold as a DEF CON 27 indie badge via Kickstarter, so the GrrCON connection has some basis but the maker of record for this specific DC27 release is Hak4Kidz. Title corrected to match how the maker and press refer to it.
status: released
sources:
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: Hack 4 Kids Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc27-badges); event read as ''dc27''.'
- kind: url
  url: https://www.hackster.io/news/hak4kidz-is-making-a-def-con-27-indie-badge-just-for-kids-a2a0b7a3dd19
  title: Hak4Kidz Is Making a DEF CON 27 Indie Badge Just for Kids
  accessed: '2026-09-08'
  note: Full spec details (ESP32, 2.4" TFT, capacitive touch, SAO ports, battery, price, distribution) and story of the badge; fetched via Wayback Machine snapshot since the live page returns 403 to automated fetches.
- kind: url
  url: https://www.kickstarter.com/projects/h4k/hak4kidz-def-con-27-indie-badge
  title: Hak4Kidz DEF CON 27 Indie Badge
  accessed: '2026-09-08'
  note: Confirms maker (Hak4Kidz) and campaign existence; page itself was behind a Cloudflare challenge so could not be read directly.
- kind: url
  url: https://www.hak4kidz.com/
  title: Hak4Kidz | Home
  accessed: '2026-09-08'
  note: Confirms Hak4Kidz as an active youth ethical-hacking conference; describes itself as a conference, not explicitly as a nonprofit.
- kind: url
  url: https://projects.propublica.org/nonprofits/organizations/465659249
  title: 'Hak4 Kidz Nfp - Nonprofit Explorer - ProPublica'
  accessed: '2026-09-08'
  note: Independently confirms Hak4Kidz Nfp is a registered 501(c)(3) nonprofit (EIN 46-5659249), supporting the "nonprofit" description in the summary.
- kind: url
  url: https://medium.com/@cameroncoward/hak4kidz-is-making-a-def-con-27-indie-badge-just-for-kids-a2a0b7a3dd19
  title: 'Hak4Kidz Is Making a DEF CON 27 Indie Badge Just for Kids (author mirror)'
  accessed: '2026-09-08'
  note: 'Author''s own Medium mirror of the Hackster article; live page returns 403, but a search-engine snippet directly quotes it: "the Kickstarter campaign is running until July 1st. A complete badge costs $100, and can be picked up at DEF CON 27 in Las Vegas or shipped to you." Corroborates price, campaign end date, and pickup/ship distribution.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Re-verified 2026-09-08. The live Hackster, Kickstarter, and Medium pages all still 403/Cloudflare-block automated fetches, so verification relied on independently reproduced search-engine snippets that directly quote the source text (Hackster: "2.4\" 240x320 color TFT LCD," "6 capac[itive]" pads, "micro SD card slot for easily flashing code to the ESP32," "Power is provided through USB"; Medium/Hackster mirror: "$100," "running until July 1st," "picked up at DEF CON 27 ... or shipped"; Kickstarter: "89 backers pledged $11,623"; Hackaday, fetched directly: "originally designed for GrrCON," "200 badges produced," "sold about half ... through a crowd funding campaign") plus one independent nonprofit-registry source for the "nonprofit" descriptor. Two claims from the prior pass could not be corroborated anywhere and were removed as unsupported: the "3x AA batteries" power claim (Hackster snippets mention only USB power) and "two SAO add-on locations" (no source found mentions SAO ports on this badge at all). get_one.availability: sold_out is an inference, not a directly-quoted claim — basis is the 2019 Kickstarter having ended, Hackaday saying only about half of 200 sold, and the current Hak4Kidz Shopify store (checked live) no longer listing this badge among its ~19 products. LED count/type, sao_version, and open-source status remain correctly left blank: not stated in any source found. Note for a future research pass, not acted on here since this task is verification-only: a GitHub repo "Hak4Kidz/H4K-cryptex" ("Cryptex virtual escape room badge for DC27 and our contribution to #badgelife," GPL-3.0, Hardware+Software folders) turned up during corroboration and looks like the maker''s own firmware/hardware source for this exact badge - worth a follow-up pass to fill make_your_own.open_source/hardware_url/firmware_url.'
last_modified_date: '2026-09-08'
---

The Hak4Kidz DEF CON 27 badge is a puzzle badge from Hak4Kidz, a nonprofit that runs youth-focused ethical-hacking events, built around the group's mascot Tinker standing behind a cryptex-styled centerpiece. A 2.4" 240x320 color TFT LCD sits in the middle of the cryptex, surrounded by 6 capacitive touch pads that players use to work through an unlock puzzle hidden in the badge's firmware. Hackaday's contemporaneous roundup notes the design was originally created for GrrCON before this DEF CON 27 run.

Under the hood it runs an ESP32, giving it Wi-Fi and Bluetooth, with a micro SD card slot for flashing code. It is powered over USB. About 200 were produced; roughly half were sold through a Kickstarter campaign that ran through July 1, 2019, at $100 each, with backers able to pick the badge up in person at DEF CON 27 in Las Vegas or have it shipped.
