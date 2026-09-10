---
title: White House Identity Disc
id: dc31-white-house-identity-disc
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: Office of the National Cyber Director
  url: https://www.whitehouse.gov/oncd/
summary: A circular RFID medallion the White House Office of the National Cyber Director (ONCD) handed out at DEF CON 31, printed with UV-reactive ink that reveals a White House emblem under blacklight and doubling as a multi-stage CTF.
functions: 'Carries a passive RFID/NFC tag readable with tools like a Flipper Zero or Proxmark3; the tag text ("Behind bytes and bits | Cyber strategy''s secret | Key reveals the path 2DF587") is one clue in a chain that also includes Morse code around the disc''s rim ("I fight for the users," a Tron reference) and a base64/XOR/Vigenere-encoded string hidden in the metadata of the National Cybersecurity Strategy PDF, ultimately decoding to a second Tron quote.'
look:
  colors:
  - black
  - blue
  shape: circle
  themes:
  - coin
  - ctf
  - puzzle
  - security
  form_factor: coin
tech:
  mcu: none
  leds: null
  display: none
  connectivity:
  - rfid
  battery: none
  sao_version: none
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Handed out in person by the ONCD team to DEF CON 31 attendees in Las Vegas in August 2023; a CTF write-up describes a reading taken from a badge belonging to then-ONCD Director Kemba Walden.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: twitter.com/ONCD/status/1687452828049330177
  url: https://twitter.com/ONCD/status/1687452828049330177/
  kind: social
- label: 'ONCD DEFCON31 Badge Write-up: The Secret within the National Cybersecurity Strategy'
  url: https://writeups.ayyappan.me/oncd-defcon31-badge-write-up
  kind: article
- label: Office of the National Cyber Director (whitehouse.gov)
  url: https://www.whitehouse.gov/oncd/
  kind: website
images:
- file: assets/images/badges/dc31/white-house-identity-disc/d38f0f8fe8.jpg
  source: "https://writeups.ayyappan.me/oncd-defcon31-badge-write-up"
  credit: "ONCD / @ONCD tweet"
  caption: "ONCD's tweet announcing the DEF CON 31 disc: soldering it together, then the finished disc glowing blue under blacklight with a White House emblem, on a ribbon reading OFFICE OF THE NATIONAL CYBER DIRECTOR / DEF CON 2023"
contact: {}
notes:
- 'Sweep-imported wording: "Limited (under 100) identity-disc badge distributed to White House staff and contest winners at DEF CON 31, per the community badgelife spreadsheet." That quantity and distribution detail could not be confirmed by any source found in this pass; treat it as unverified.'
- Neither ONCD's tweet nor the CTF write-up uses the name "White House Identity Disc" — it appears to be the community/spreadsheet's descriptive name for the item, fitting since the disc's own puzzle chain leads to a quote from Tron, whose title object is literally called an "identity disc."
- ONCD ran a similarly-themed giveaway at DEF CON 30 (a challenge coin) and is listed again for DEF CON 32 and 33 (entries dc32-office-of-the-national-cyber-director-i-e-the-feds-listed-fo and dc33-..., not yet researched); this may be an annual series worth linking once those are filled in.
status: released
sources:
- kind: url
  url: https://twitter.com/ONCD/status/1687452828049330177/
  title: White House Identity Disc
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc31-indie); event read as ''dc31''.'
- kind: url
  url: https://writeups.ayyappan.me/oncd-defcon31-badge-write-up
  title: 'The Secret within the National Cybersecurity Strategy | ONCD DEFCON31 Badge Write up'
  accessed: '2026-09-10'
  note: Third-party CTF write-up confirming the badge exists, describing its RFID tag, Morse-coded rim, and puzzle chain, and embedding the original ONCD tweet image showing the physical disc.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Confirmed via a third-party CTF write-up and the original ONCD tweet image (a UV-reactive RFID disc on a ribbon), not just a search snippet. No maker page states the exact name, quantity, or whether it was given only to staff/winners versus general attendees; the "under 100" and "staff and contest winners" claims from the sweep's source sheet are unverified and flagged in notes. No hardware/firmware files were found, so make_your_own is left null rather than "no."
last_modified_date: '2026-09-10'
---

At DEF CON 31 in August 2023, the White House's Office of the National Cyber Director (ONCD) gave out a circular medallion embedded with a passive RFID tag. Under normal light it reads as a dark disc; under a blacklight it reveals a White House emblem printed in UV-reactive ink, worn on a ribbon printed "OFFICE OF THE NATIONAL CYBER DIRECTOR / DEF CON 2023." ONCD previewed it on Twitter/X a few days before the con with photos of the piece being assembled and glowing under UV.

The disc doubled as a scavenger-hunt style CTF. Morse code cut into its rim decoded to "I fight for the users," a line from the 1982 film Tron (whose title object, a circular thrown weapon, is called an identity disc — likely the source of this item's community nickname). Scanning the embedded RFID tag with tools like a Flipper Zero or Proxmark3 returned the line "Behind bytes and bits | Cyber strategy's secret | Key reveals the path 2DF587." Solvers eventually traced the "2DF587" key to a base64 string hidden in the EXIF metadata of ONCD's own National Cybersecurity Strategy PDF; XOR-ing it against the key and running the result through a Vigenère cipher (key "ONCD") produced a second Tron quote. A public write-up by a member of the DEF CON Car Hacking Village documents the full solve, including a screenshot of a tag read taken from a disc belonging to then-ONCD Director Kemba Walden.

Nothing found in this pass confirms exact production numbers or whether distribution was limited to White House staff and contest winners, as the community spreadsheet entry that seeded this record claimed; that detail is noted above as unverified. No hardware files, firmware, or a storefront listing were located — this appears to have been a one-off giveaway rather than a sold or open-sourced badge.
