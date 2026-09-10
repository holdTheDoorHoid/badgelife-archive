---
title: Popcorn SAO
id: dc27-popcorn-sao
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: Kredence
summary: A popcorn-box-shaped SAO with gold-plated kernel details, made by Kredence as a companion piece to their DC27 Popcorn Bucket Badge.
functions: ''
look:
  colors:
  - red
  - white
  - gold
  shape: null
  themes:
  - food
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: v1.69bis
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
- label: github.com/Kredence/DC27_Popcorn_SAO
  url: https://github.com/Kredence/DC27_Popcorn_SAO
  kind: website
images:
- file: assets/images/badges/dc27/popcorn-sao/bc975733fe.jpg
  source: "https://github.com/Kredence/DC27_Popcorn_SAO"
  credit: "Kredence"
  caption: "Popcorn SAO PCB, showing a striped popcorn-box outline with gold-plated kernel shapes"
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
status: released
sources:
- kind: url
  url: https://github.com/Kredence/DC27_Popcorn_SAO
  title: Popcorn SAO
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://api.github.com/repos/Kredence/DC27_Popcorn_SAO/contents/
  title: Kredence/DC27_Popcorn_SAO repository contents
  accessed: '2026-09-10'
  note: 'Repo contains only one file, PopcornSAO.jpg, and no README/description; confirms the maker (Kredence) and that this is a real, distinct PCB (used as the entry image) rather than a rumor.'
- kind: url
  url: https://api.github.com/users/Kredence/repos
  title: Kredence GitHub profile repo list
  accessed: '2026-09-10'
  note: Confirms Kredence is a recurring DEF CON badge maker (Illuminati series, DC27 Popcorn Bucket Badge, later Illuminati Party badges) and that DC27_Popcorn_SAO is a separate repo from DC27_Popcorn_Bucket_Badge.
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: 'Hackaday: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27'
  accessed: '2026-09-10'
  note: 'Covers Kredence and Ajax_409''s DC27 "Popcorn Badge" (a bucket-shaped host badge with twelve add-on headers, backlit kernels in a cut-down plastic popcorn box) and Kredence''s Illuminati badge that same year, establishing Kredence''s DC27 badge lineup; does not separately describe this smaller Popcorn SAO.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: >-
    The GitHub repo (github.com/Kredence/DC27_Popcorn_SAO) has no README, so maker's-own-words
    documentation for this specific SAO does not exist online; confidence is medium because
    the repo image and maker identity are confirmed, but functions, MCU/LEDs, price, quantity
    and distribution are not documented anywhere found. This is distinct from Kredence and
    Ajax_409's larger "Popcorn Bucket Badge" (separate repo, separate archive entry
    dc27-popcorn-bucket-badge), a bucket-shaped host badge with twelve SAO headers covered
    by Hackaday's DC27 badge roundup; this SAO appears to be a smaller companion piece, likely
    meant to plug into other people's badges rather than to host add-ons itself. The board
    photo shows a 6-pad footprint at the bottom center consistent with a 6-pin (v1.69bis/v2)
    SAO connector, and no visible LEDs, chips, or components -- it reads as a purely
    decorative/passive PCB-art SAO, but no source states this explicitly, so tech.mcu and
    tech.leds are left null rather than guessed. status set to "released" (not "listed") since
    a real photographed PCB exists, but availability, price and quantity are unknown.
last_modified_date: '2026-09-10'
---

Popcorn SAO is a Shitty Add-On made by Kredence for DEF CON 27 (2019), shaped like a classic red-and-white-striped popcorn box with gold-plated kernels piled at the top and a "POPCORN" wordmark across the front. It's a companion piece to Kredence and Ajax_409's larger Popcorn Bucket Badge from the same year, a bucket-shaped host badge with twelve add-on headers built from a cut-down plastic popcorn box with backlit kernels -- this SAO carries the same visual theme in miniature, sized to plug into other attendees' badges rather than to host add-ons of its own.

Beyond the board photo and the maker's identity, there isn't much to go on: the GitHub repository holding the image has no README, description, or other files, and no press coverage, storefront listing, or social post specifically about this SAO turned up in search. The board's front shows no visible LEDs or ICs, and a six-pad footprint at the bottom center is consistent with a 6-pin SAO connector, but nothing confirms whether it lights up, what (if anything) drives it, or how it was distributed.
