---
title: DEF CON Shoot Badge (Banana Mag)
id: dc26-def-con-shoot-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
series: boombadge
makers:
- name: Matt
  url: https://twitter.com/boombadge
summary: A Magpul PMAG rifle magazine dyed yellow and scented with banana oil, made as the attendee badge for the unofficial DEF CON Shoot 26 pre-con range day.
functions: Worn as the DEF CON Shoot's event badge; its lanyard carried ciphertext that opened a multi-stage crypto puzzle (ROT13, Vigenere, esoteric languages) ending in an 80%-lower-receiver prize.
look:
  colors:
  - yellow
  shape: rectangle
  themes:
  - meme
  - puzzle
  - ctf
  form_factor: other
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: single yellow LED
  display: none
  connectivity: []
  battery: coin cell
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: '145'
  availability: sold_out
  availability_note: One-off DC26 (2018) DEF CON Shoot item; checked 2026-09-08, no current listing found.
  distribution:
  - free_drop
  where: Given to attendees of the DEF CON Shoot, an unofficial pre-DEF CON shooting-range meetup near Las Vegas.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3
  url: https://hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3/
  kind: article
- label: 'GitHub: Defcon-Shoot-26-Puzzle writeup'
  url: https://github.com/seeess/Defcon-Shoot-26-Puzzle
  kind: repo
- label: 'YouTube: DEFCON 26 Shoot - boom badge in action'
  url: https://www.youtube.com/watch?v=2PIoov_MZ1Y
  kind: video
- label: The Unofficial DEF CON Shoot Page
  url: https://dcshoot.org/
  kind: website
images:
- file: assets/images/badges/dc26/def-con-shoot-badge/cc69cc416a.jpg
  source: https://hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3/
  credit: Hackaday
  caption: The DEF CON Shoot banana-scented PMAG badge hanging on its lanyard
- file: assets/images/badges/dc26/def-con-shoot-badge/c35724a8eb.jpg
  source: https://hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3/
  credit: Hackaday
  caption: The banana-themed sticker included with the DEF CON Shoot badge
contact: {}
notes:
- Sweep imported the title as "DEF CON Shoot Badge"; sources (Hackaday, GitHub, YouTube) call it a "banana clip"/"banana magazine" badge and the maker's own handle is @boombadge, so the title has been adjusted to "DEF CON Shoot Badge (Banana Mag)" to match maker usage and to distinguish it from the badge's puzzle/lanyard.
- Duplicate of entry dc26-def-con-shoot-badge-banana-mag, which describes the same object from the same source and is also still a stub.
- Banana-magazine-themed badge for the DEF CON Shoot, listed in Hackaday's badge roundup vol.3. Found by the event-year sweep, task dc26-saos.
- The sweep recorded the maker as "bmp51" — that is a Twitter handle Hackaday linked for the *previous* year's (2017) "boombadge," not a credit for this 2018 banana-mag badge. Research found the actual maker's handle to be @boombadge (name "Matt"), per the GitHub puzzle writeup; makers has been corrected accordingly.
- This entry duplicates dc26-def-con-shoot-badge, which independently researched the same object from the same Hackaday source (including two saved images) and reached the same facts; the two should be merged, keeping dc26-def-con-shoot-badge's images.
status: listed
sources:
- kind: url
  url: https://hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3/
  title: DEF CON Shoot Badge (Banana Mag)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc26-badges); event read as ''dc26''.'
- kind: url
  url: https://github.com/seeess/Defcon-Shoot-26-Puzzle
  title: Defcon-Shoot-26-Puzzle README
  accessed: '2026-09-08'
  note: Confirmed maker (Matt / @boombadge), badge contents (banana clip PMAG, stickers, mag pull, LEDs), and the lanyard puzzle contest.
- kind: url
  url: https://www.youtube.com/watch?v=2PIoov_MZ1Y
  title: DEFCON 26 Shoot - boom badge in action
  accessed: '2026-09-08'
  note: Confirms the badge's nickname "boom badge," the Magpul 30-round windowed PMAG base, and the yellow dye/banana-oil scenting.
- kind: url
  url: https://dcshoot.org/
  title: The Unofficial DEF CON Shoot Page
  accessed: '2026-09-08'
  note: Background on the DEF CON Shoot event (pre-con shooting range meetup) that the badge was made for.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: No price or exact distribution mechanism (free with range registration vs. separate cost) was stated by any source, so get_one.price is left blank; distribution is marked free_drop as a best read of "given to attendees" language. No maker's own photos, hardware files, or storefront were found beyond the Hackaday press photos and the puzzle repo. This entry duplicates dc26-def-con-shoot-badge-banana-mag (same source, same object); the two should be merged. Merged with duplicate entry 'DEF CON Shoot Badge (Banana Mag)' (dc26-def-con-shoot-badge-banana-mag).
last_modified_date: '2026-09-08'
redirect_from:
- /badges/dc26/def-con-shoot-badge-banana-mag/
---

The DEF CON Shoot Badge, also called the "boom badge" or "banana mag," was the attendee badge for the DEF CON Shoot — an unofficial pre-conference shooting-range meetup held near Las Vegas ahead of DEF CON 26 in 2018. Rather than a PCB, the badge started life as a sand-colored Magpul PMAG rifle magazine: makers boiled it, dyed it bright yellow with Rit dye, boiled it again, and scented it with banana oil, finishing the "banana" joke with a custom banana-label sticker and a single yellow LED powered by a coin cell. 145 were made. It was designed by a maker known as Matt (@boombadge on Twitter/X), continuing a yearly tradition of joke badges for the Shoot.

The badge's lanyard doubled as a puzzle: it carried ciphertext that opened a six-stage cryptography challenge (ROT13, a Vigenère cipher, esoteric programming languages, and further crypto questions), documented afterward in a GitHub writeup by the event's puzzle designer. The eventual winner received an 80%-lower AR-15 receiver, itself hand-customized by the maker with an inscribed SQL-injection joke and re-labeled fire-selector markings.

This entry duplicates `dc26-def-con-shoot-badge-banana-mag`, an independently-swept stub describing the same object from the same Hackaday source; the two should be reconciled into one entry.

## Notes merged from the duplicate entry "DEF CON Shoot Badge (Banana Mag)"

The DEF CON Shoot Badge, also called the "boom badge" or "banana mag," was the attendee badge for the DEF CON Shoot — an unofficial pre-conference shooting-range meetup held near Las Vegas ahead of DEF CON 26 in 2018. Rather than a PCB, the badge started life as a sand-colored Magpul PMAG rifle magazine: makers boiled it, dyed it bright yellow with Rit dye, boiled it again, and scented it with banana oil, finishing the "banana" joke with a custom banana-label sticker and a single yellow LED powered by a coin cell. 145 were made. It was designed by a maker known as Matt (@boombadge on Twitter/X), continuing a yearly tradition of joke badges for the Shoot.

The badge's lanyard doubled as a puzzle: it carried ciphertext that opened a six-stage cryptography challenge (ROT13, a Vigenère cipher, esoteric programming languages, and further crypto questions), documented afterward in a GitHub writeup by the event's puzzle designer. The eventual winner received an 80%-lower AR-15 receiver, itself hand-customized by the maker with an inscribed SQL-injection joke and re-labeled fire-selector markings.

This entry duplicates `dc26-def-con-shoot-badge`, an independently-researched entry describing the same object from the same sources; the two should be reconciled into one entry (that entry already carries the saved photos).
