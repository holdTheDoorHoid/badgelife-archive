---
title: RFID NFC Community Badge
id: saintcon-2022-rfid-nfc-community-badge-2022
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: Jup1t3r
summary: A beginner-level SAINTCON community minibadge about NFC/RFID vulnerabilities, given out free while supplies lasted.
functions: 'Educational giveaway minibadge for the RFID/NFC community track; no interactive functions beyond the single LED and the RFID tag sticker applied to the back.'
look:
  colors:
  - black
  - orange
  - white
  shape: rounded square
  themes:
  - security
  - radio
  - learn to solder
  - village badge
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: Single LED soldered using the single-pad hand-soldering method; direction indicated on the assembly diagram.
  display: none
  connectivity:
  - nfc
  - rfid
  battery: null
  sao_version: none
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given out at SAINTCON 2022's RFID/NFC community area while supplies lasted; assembled by attendees as a beginner solder kit.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  kind: website
images:
  - file: assets/images/badges/saintcon-2022/rfid-nfc-community-badge-2022/front.jpg
    source: "https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf"
    credit: "Jup1t3r / SAINTCON"
    caption: "Front of the RFID/NFC Community minibadge (2022), showing the LED and RFID/NFC artwork"
  - file: assets/images/badges/saintcon-2022/rfid-nfc-community-badge-2022/back.jpg
    source: "https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf"
    credit: "Jup1t3r / SAINTCON"
    caption: "Back of the badge, showing where the RFID tag sticker is affixed"
contact: {}
notes:
- The event-year sweep's sheet listed the title as "RFID/NFC Community Badge (2022)"; the SAINTCON 2022 MiniBadge Assembly Guide itself labels the board "RFID NFC COMMUNITY BADGE" with no year in the name (the year comes from the guide's own 2022 edition), so the title here follows the guide.
- Distinct from the separately catalogued 2021 ("RFID/NFC BADGE") and 2023/2024 RFID/NFC community minibadges in this archive; each year got its own design by Jup1t3r (2021, 2022) or other designers (2023, 2024).
status: listed
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: RFID/NFC Community Badge (2022)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2022); event read as ''saintcon-2022''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: SAINTCON MiniBadge Assembly Guide 2022, page 25 (RFID NFC Community Badge)
  accessed: '2026-09-10'
  note: Read the full assembly-guide page for this badge (text and embedded photos) to confirm the item is real and to fill in description, LED, difficulty/rarity, distribution, and images.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Only source found is the SAINTCON 2022 MiniBadge Assembly Guide itself; no maker page, storefront, or third-party coverage located. The guide confirms the badge exists, its designer, purpose, and assembly steps (single LED, resistor, RFID tag sticker affixed to the back, 4x 2-position headers), plus front/back photos, but gives no MCU/chip (there is none — it is a passive LED board with an NFC/RFID sticker), quantity made, or a firmware/hardware repo. Difficulty is listed as "Beginner" and rarity as "Common" on the guide''s own scale, which are guide metadata rather than archive fields, so left out of the schema above; noted here instead.'
last_modified_date: '2026-09-10'
---

The RFID/NFC Community Badge was Jup1t3r's SAINTCON 2022 minibadge for the con's RFID/NFC community track, handed out free to attendees while supplies lasted as a beginner-level soldering project. The front PCB carries a masked-figure "RFID/NFC" graphic in orange and white on black, a single LED, and a resistor; assembly starts on the front, where the LED and resistor are hand-soldered single-pad style. The back of the board is silkscreened "RFID STICKER GOES HERE" — builders affix an actual RFID/NFC tag sticker there (trimming it to fit if needed) before soldering on the four 2-position pin headers used to link it to other minibadges on a lanyard chain.

There is no microcontroller or programmable logic on the board; the "vulnerability" lesson is meant to come from pairing the visible LED board with a real, readable RFID/NFC tag, in keeping with the community track's educational theme. The SAINTCON 2022 MiniBadge Assembly Guide rates it "Beginner" difficulty and "Common" rarity on its own internal scale. No maker storefront, repository, or press coverage beyond the guide itself was found; the guide's assembly-page photos are the only images of the badge located.
