---
title: RAY-MAN Badge
id: saintcon-2022-ray-man-badge-2022-collab
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: CompuKidMike & Ray-Man
summary: A personal/collaborative SAINTCON 2022 minibadge built on CompuKidMike's reusable "honk" sound-effect PCB, with Ray-Man's own soda-can artwork and a small speaker that makes it honk when triggered.
functions: 'Presses a switch to play a "honk" sound through an onboard speaker; otherwise a passive trading minibadge (no LEDs or display).'
look:
  colors: []
  shape: rectangle
  themes:
  - meme
tech:
  mcu: null
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - swap
  where: Find Ray-Man in person at SAINTCON 2022 and trade for one.
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
  - file: assets/images/badges/saintcon-2022/ray-man-badge-2022-collab/99363b2048.jpg
    source: "https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf"
    credit: "CompuKidMike & Ray-Man"
    caption: "Front graphic: soda can art, 'Trust the Awesomeness!'"
  - file: assets/images/badges/saintcon-2022/ray-man-badge-2022-collab/74130e3e17.jpg
    source: "https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf"
    credit: "CompuKidMike & Ray-Man"
    caption: "Back: PCB silkscreen, 'Ray-Man 2022' with MKFactor logo"
contact: {}
notes:
- Collaborative personal minibadge by CompuKidMike and Ray-Man. Found by the event-year sweep, task saintcon-2022.
- 'The sweep''s sources list carried the file-sourced label "RAY-MAN Badge (2022 collab)"; the assembly guide itself just titles it "RAY-MAN Badge" (page 55), so the title was trimmed to match.'
- 'The guide''s page 55 entry for this badge repeats, verbatim, the same "When you hear it, you will know. We LOVE to make it Honk!" blurb and "find Honki" acquisition text used for the separate HONKI Badge on page 54 (saintcon-2022-honki-badge) — apparently reused/templated text in the source PDF rather than badge-specific copy. The board layout (SPK speaker pad, SW switch, R1-R3, C1/C3/C4/C6, U2/U3, UPDI header) is identical between the two, just with different silkscreen art and names ("Honki 2022" vs "Ray-Man 2022"), both under CompuKidMike''s "MKFactor" PCB branding.'
- 'A separate, unrelated minibadge also called "RAY-MAN 2022" (designed by Ray-Man solo, page 80 of the same guide, an LED badge with Minnie-Bow-style art) exists in the same document — do not conflate the two; see other_items_found in the research report.'
status: listed
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: RAY-MAN Badge (2022 collab)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2022); event read as ''saintcon-2022''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: SAINTCON MiniBadge Assembly Guide 2022 (page 55, RAY-MAN Badge)
  accessed: '2026-09-10'
  note: 'Confirmed the badge exists and pulled maker credit, difficulty/rarity, assembly steps, and both silkscreen images by extracting text and embedded images from the PDF directly (WebFetch could not read the PDF as text).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed via the official SAINTCON 2022 MiniBadge Assembly Guide PDF (extracted with pdftotext/pdfimages since WebFetch could not parse this PDF as text). No maker storefront, repo, or social post specific to this badge was found beyond the guide itself, and CompuKidMike''s public saintcon2022 GitHub repo does not mention it, so mcu/leds/price/quantity/open-source fields are left empty. Difficulty is listed as BEGINNER and rarity as RARE in the guide; those aren''t archive schema fields so they are recorded here instead. The guide''s description text for this badge appears to be reused verbatim from the separate HONKI Badge entry on the preceding page (see notes above) — treated as a documentation artifact, not evidence this badge itself has a speaker/switch design distinct from Honki''s, though the assembly instructions (solder SW, solder speaker, attach with tape, solder 4x 2-pin headers) do describe an actual sound-effect board and the board silkscreen (R1-R3, C1/C3/C4/C6, SPK, SW, U2, U3, UPDI) matches a real, populated PCB, not a placeholder.'
last_modified_date: '2026-09-10'
---

The RAY-MAN Badge is a 2022 SAINTCON minibadge credited to CompuKidMike and Ray-Man, documented on page 55 of the official SAINTCON MiniBadge Assembly Guide 2022. It uses a small sound-effect PCB — a speaker, a switch, and a handful of passives on a board marked "Ray-Man 2022" under CompuKidMike's "MKFactor" branding — with Ray-Man's own soda-can artwork ("Trust the Awesomeness!") on the front. The same underlying board design, with different art and a different name, also produced the separate HONKI Badge that appears on the preceding page of the same guide.

Assembly was mostly pre-done: builders just soldered the switch to the top side, the speaker to the bottom side (secured with double-sided tape), and four 2-position headers. The guide rates it BEGINNER difficulty and RARE availability, distributed by finding Ray-Man in person at the con and trading for one — no storefront, kit sale, or public repo for this specific badge was found.

No independent maker page, social post, or code/hardware repo confirming further technical details (MCU, firmware, exact BOM) turned up in a search beyond the assembly guide itself, so those fields are left blank rather than guessed.
