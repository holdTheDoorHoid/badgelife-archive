---
title: Amulet of Entropy
id: dc30-amulet-of-entropy
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: Carey Parker (FirewallDragon / bananajr)
  url: https://firewallsdontstopdragons.com/
  role: concept and software
- name: HackerBoxes (Joe Long)
  url: https://hackerboxes.com
  role: hardware design and kit production
summary: 'An RP2040 indie badge sold as the DIY kit HackerBox #0080 that harvests randomness from four on-board sensors (light, temperature, motion and transistor avalanche noise) into an entropy pool, then spends it flipping coins, rolling a die, drawing playing and tarot cards and answering as a Magic 8 Ball on a round 1.28-inch colour LCD.'
functions: 'Fills an entropy pool from four sources (GY-521 motion, GL10528 photoresistor, TMP36 temperature, 2N3904 avalanche-noise generator) and seeds a PRNG from it; five modes chosen with Plus/Minus/Select/Back buttons: coin flip, six-sided die, pick from a 52-card deck, pick from a 78-card Rider-Waite tarot deck, Magic 8 Ball; four dragon-eye LEDs show how full the pool is (green full, yellow/orange partial, red empty) and four arrow-gem LEDs sparkle when it is full; a demo mode cycles through everything; the HackerBoxes demo sketch instead continuously shows values read from the entropy sources on the display. The badge doubled as the data-collection tool for the maker''s DEF CON 30 Crypto & Privacy Village talk on harvesting environmental entropy.'
look:
  colors:
  - black
  - gold
  - white
  shape: four-lobed square
  themes:
  - fantasy
  - security
  - kit
  - wearable
  - jewelry
  form_factor: pcb badge
tech:
  mcu: RP2040 (Waveshare RP2040-Zero module)
  leds:
    count: 8
    type: SK6812MINI-E reverse-mount RGB
    note: Four light the dragon eyes and four the arrow tips; the kit includes four silicate crystals to hot-glue over the arrow LEDs as light pipes.
  display: 1.28" round IPS LCD 240x240 (GC9A01)
  connectivity:
  - usb
  - i2c
  inputs:
  - buttons
  - accelerometer
  - photoresistor
  - temperature sensor
  - avalanche noise generator
  - slide switch
  power: USB-C on the RP2040-Zero, or LiPo via JST-PH 2-pin through an MH-CD42 charger module; SPDT slide switch selects USB or battery
  battery: 3.7 V LiPo, user supplied (not in the kit); fits between the two boards, up to about 5x7 cm
  sao_version: none
  sao_ports: 0
get_one:
  price: '$79 as a single HackerBox #0080 ($45 for subscribers per the community sheet); also in the $217 DC30 Badge Bundle'
  price_usd: 79.0
  quantity: ''
  availability: sold_out
  availability_note: hackerboxes.com listed HackerBox #0080 and the DC30 Badge Bundle as sold out when checked 2026-09-06; the maker's page says the same and that he kept three unopened kits for giveaways.
  distribution:
  - purchase
  - kit
  - membership
  where: 'Shipped to HackerBoxes monthly subscribers as box #0080 "Entropy" and sold singly on hackerboxes.com from 1 July 2022; from 11 July 2022 also bundled with HackerBox #0074 Battle Axe and #0068 SAO Showcase as the DC30 Badge Bundle. Every unit was a solder-it-yourself kit.'
make_your_own:
  open_source: partial
  hardware_url: https://www.instructables.com/HackerBox-0080-Entropy/
  firmware_url: https://github.com/FirewallDragon/amulet-of-entropy
  gerbers_url: null
  eda_tool: null
  license: MIT (firmware)
  fab_url: null
  notes: 'PDF schematics for the Main Board and Display Board are attached to step 3 ("Amulet of Entropy Badge") of the Instructables guide, and the firmware plus image assets are on GitHub under MIT. No Gerbers or EDA project files were found. The Main Board carries a PCBWay logo and the guide thanks PCBWay for sponsoring the project, but no PCBWay shared project was found.'
links:
- label: hackerboxes.com
  url: https://hackerboxes.com
  kind: store
- label: 'HackerBox #0080 - Entropy (product page)'
  url: https://hackerboxes.com/products/hackerbox-0080-entropy
  kind: store
- label: DC30 Badge Bundle
  url: https://hackerboxes.com/products/dc30-badge-bundle
  kind: store
- label: 'HackerBox 0080: Entropy build guide (Instructables)'
  url: https://www.instructables.com/HackerBox-0080-Entropy/
  kind: doc
- label: FirewallDragon/amulet-of-entropy (firmware and docs)
  url: https://github.com/FirewallDragon/amulet-of-entropy
  kind: repo
- label: Amulet of Entropy on Firewalls Don't Stop Dragons
  url: https://firewallsdontstopdragons.com/amulet-of-entropy/
  kind: website
- label: amuletofentropy.com
  url: https://amuletofentropy.com/
  kind: website
- label: Necessary Chaos (podcast episode revealing the badge)
  url: https://podcast.firewallsdontstopdragons.com/2022/07/04/necessary-chaos/
  kind: article
- label: Hackerboxes 0080 Amulet of Entropy unbox and build (463n7)
  url: https://youtu.be/swqGDDqKy7U
  kind: video
- label: 2022 BadgeLife List thread on the DEF CON forums
  url: https://forum.defcon.org/node/240869
  kind: social
images:
- file: assets/images/badges/dc30/amulet-of-entropy/7a3bd84c77.jpg
  source: https://firewallsdontstopdragons.com/amulet-of-entropy/
  credit: Carey Parker (Firewalls Don't Stop Dragons)
  caption: Assembled Amulet of Entropy on its leather cord, dragon-eye and arrow-gem LEDs lit
- file: assets/images/badges/dc30/amulet-of-entropy/b936e9b1c0.jpg
  source: https://www.instructables.com/HackerBox-0080-Entropy/
  credit: HackerBoxes
  caption: Assembled Amulet of Entropy on its lanyard with the round display and all eight LEDs lit
- file: assets/images/badges/dc30/amulet-of-entropy/1d4ac32124.jpg
  source: https://www.instructables.com/HackerBox-0080-Entropy/
  credit: HackerBoxes
  caption: 'Kit contents: the front Display Board with the four gold dragons, the rear Main Board, RP2040-Zero, GC9A01 round LCD, GY-521, MH-CD42, eight SK6812MINI-E LEDs and passives'
contact: {}
notes:
- They are $45 if you have the sub but $79 if alone/also there is a badge box available
- The community sheet titled it "Amulet of Entropy!!" and credited "HackerBoxes/bananajr"; the makers call it Amulet of Entropy (AoE). The DEF CON forum user bananajr (profile title "Author, Podcast Host") posted it as "my first badge, developed with HackerBoxes.com" with a link to amuletofentropy.com, which matches Carey Parker's own account of creating it, so bananajr is taken to be Parker's forum handle.
- The "badge box" in the sheet note is the DC30 Badge Bundle, which packaged this kit with HackerBox #0074 Battle Axe and #0068 SAO Showcase.
status: released
sources:
- kind: sheet
  event: dc30
  row: 9
  updated: '2022-07-24'
- kind: url
  url: https://hackerboxes.com/products/hackerbox-0080-entropy
  title: 'HackerBox #0080 - Entropy - HackerBoxes'
  accessed: '2026-09-06'
  note: Official product page; hardware summary, box contents, $79 price, sold-out status, listing date 2022-07-01 (from the store JSON), links to the guide, video and repo.
- kind: url
  url: https://hackerboxes.com/products/dc30-badge-bundle
  title: DC30 Badge Bundle - HackerBoxes
  accessed: '2026-09-06'
  note: $217 bundle of HackerBox #0080, #0074 and #0068 listed 2022-07-11; sold out.
- kind: url
  url: https://www.instructables.com/HackerBox-0080-Entropy/
  title: 'HackerBox 0080: Entropy : 13 Steps - Instructables'
  accessed: '2026-09-06'
  note: HackerBoxes build guide published 2022-07-04; full parts list, the four entropy sources and pins, two-board construction, LCD, battery notes, PCBWay sponsorship, schematic PDFs attached to step 3, and test sketches; source of two photos.
- kind: url
  url: https://github.com/FirewallDragon/amulet-of-entropy
  title: 'GitHub - FirewallDragon/amulet-of-entropy: Software for the HackerBoxes #0080 project - a DEF CON indie badge'
  accessed: '2026-09-06'
  note: Firmware (Arduino, MIT); README, Setup, User Guide, Customize and research docs gave the modes, LED behaviour, buttons, power switch, battery connector, the 8-month build and the CPV talk on 13 Aug 2022.
- kind: url
  url: https://firewallsdontstopdragons.com/amulet-of-entropy/
  title: Amulet of Entropy - Firewalls Don't Stop Dragons
  accessed: '2026-09-06'
  note: Carey Parker's own write-up (2022-07-08); origin story, how entropy is harvested, the five modes, double-decker board design, the split of work with Joe of HackerBoxes, sold-out note; source of one photo.
- kind: url
  url: https://amuletofentropy.com/
  title: Amulet of Entropy
  accessed: '2026-09-06'
  note: Landing page linking the blog post, podcast, kit and repo.
- kind: url
  url: https://podcast.firewallsdontstopdragons.com/2022/07/04/necessary-chaos/
  title: Necessary Chaos - Firewalls Don't Stop Dragons Podcast
  accessed: '2026-09-06'
  note: Reveal episode of 2022-07-04 with HackerBoxes founder Joe Long as guest.
- kind: url
  url: https://forum.defcon.org/node/240869
  title: 2022 BadgeLife List has Started!! - DEF CON Forums
  accessed: '2026-09-06'
  note: bananajr posted the badge on 2022-07-26 as his first badge developed with HackerBoxes.com; a builder remarked on the difficulty of soldering the display; a January 2023 post asked about a fix for an auto-mode glitch.
- kind: url
  url: https://youtu.be/swqGDDqKy7U
  title: Hackerboxes 0080 Amulet of Entropy (YouTube, 463n7)
  accessed: '2026-09-06'
  note: Unbox and build video linked from the product page; title confirmed via oEmbed only.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Core facts come from the makers'' own pages (HackerBoxes product page and Instructables, Carey Parker''s blog and GitHub); checked claim by claim on 2026-09-06, including the Shopify product JSON for the 1 and 11 July 2022 listing dates and the two schematic PDFs, which show the MMBT3904 shot-noise circuit and no SAO header. Not found: number of kits made, the exact subscriber price (the sheet''s $45 is the only source), Gerbers or EDA files, a PCBWay shared project, a recording of the DEF CON 30 CPV talk, and any Hackaday or Reddit coverage. Minor disagreements: the GitHub README says the project took about 8 months, while Parker''s blog says it was kept under wraps for "9 months or so"; the blog post is dated 8 July 2022 but was last modified in 2024, so its sold-out note may have been added after that date. bananajr is identified as Carey Parker by inference: the forum user claims the badge as "my first badge" and links amuletofentropy.com. The full kit parts list and both schematics contain no SAO header, so sao_version is recorded as none. The Instructables page renders client-side; its text was read through the site''s JSON model endpoint. The DC30 Badge Bundle page has HackerBox #0068 as "SAO Showcase" (15 SAOs plus an SAO Power Badge) and #0074 "Battle Axe" as separate badge kits sold for DC30.'
last_modified_date: '2026-09-06'
---
The Amulet of Entropy is the first indie badge from Carey Parker, the author and podcaster behind *Firewalls Don't Stop Dragons* (he posts on the DEF CON forums as bananajr). After his first DEF CON in 2021 he wanted to make something for the thirtieth anniversary con, and a call for advice with Joe Long of HackerBoxes turned into a collaboration: HackerBoxes designed the hardware and produced it as their monthly kit, HackerBox #0080 "Entropy", while Parker wrote the software in C/C++. The project took about eight months off and on by Parker's account on GitHub (his blog says it was kept under wraps for nine months or so), and they revealed it on the 4 July 2022 "Necessary Chaos" podcast episode, the same day the Instructables build guide went live.

The badge's premise is that cryptography needs true randomness and computers are bad at producing it. Four sensors on the board (a GY-521 motion module, a photoresistor, a TMP36 temperature sensor and a transistor avalanche-noise circuit) are sampled repeatedly, the noisy low-order bits are kept and packed into an entropy pool, and that pool seeds a random number generator. The randomness is then spent on party tricks shown on a round 240x240 IPS display: flip a coin, roll a d6, draw a card from a 52-card deck or a 78-card Rider-Waite tarot deck, or shake a Magic 8 Ball. Four dragon-eye LEDs report how full the pool is and four arrow-tip gems sparkle when it is topped up. Parker also used the hardware to gather data for his DEF CON 30 Crypto & Privacy Village talk "Capturing Chaos: Harvesting Environmental Entropy" on 13 August 2022.

Physically it is two black PCBs on stacked 2x20 headers: a Display Board carrying the gold chaos-symbol artwork (four of the eight arrows end in dragon heads), the eight reverse-mount SK6812 LEDs and the GC9A01 LCD, and a Main Board with the Waveshare RP2040-Zero, sensors, four side buttons, a USB/battery slide switch and an MH-CD42 LiPo charger. The gap between the boards holds an optional user-supplied LiPo, and the kit ships with a leather cord, split ring and four silicate crystals to cap the arrow LEDs. It sold for $79 as a single box (less for subscribers) from 1 July 2022, was later folded into a $217 DC30 Badge Bundle with the Battle Axe and SAO Showcase boxes, and Parker's blog post (dated 8 July 2022) notes that they have all sold out at HackerBoxes; one builder on the DEF CON forums called soldering the display the hard part.

## Make your own

No Gerbers have been published, so this is a firmware-and-repair project rather than a re-spin: schematics for both boards are attached as PDFs to step 3 of the Instructables guide, and everything else lives in the FirewallDragon/amulet-of-entropy repository (MIT). Follow the repo's Setup doc: install the Arduino IDE with Earle Philhower's RP2040 board package (the author says to use the v2.x package rather than the latest, having verified v2.2.2, and notes a JPEGDEC compile fix posted in the Instructables comments), add the Adafruit NeoPixel, Arduino_GFX and JPEGDEC libraries and the LittleFS upload plugin, set the flash split to 1 MB sketch / 1 MB filesystem, upload the `data` directory of 240x240 JPEG images, then flash `src/amulet/amulet.ino`. The Customize doc explains how to add modes (the stock images already fill the 1 MB filesystem, so one of the card decks has to go) and where the LED and pool-size code lives; `src/bonus` holds spare image sets and splash screens.
