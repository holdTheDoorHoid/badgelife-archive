---
title: Space Pony SAO
id: dc31-space-pony-sao
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: Space Bits 'R Us
  url: https://github.com/scottalmond/defcon_31
  role: 'Scott Almond: concept, PCB design, software architecture; Brian Wilkins: Morse code, games, terminal art; Sugar Morning: artwork'
summary: A "My Little Pony Friendship is Magic"-themed SAO sold by the Space Bits 'R Us Hack-a-Sat team at DEF CON 31, one of 11 unique pony character designs.
functions: Lights up 10 through-hole RGB LEDs in patterns; has a microphone input and a user button that triggers a red status LED and can drive a UART terminal.
look:
  colors: []
  shape: pony
  themes:
  - animal
  - pop culture
tech:
  mcu: STM8S003F3P6TR
  leds:
    count: 10
    type: RGB
    note: Through-hole RGB LEDs; a separate single status LED (green/cyan/red) reports power and charge state.
  display: none
  connectivity:
  - uart
  - i2c
  battery: 40 mAh LIR2032 LiPo (~2 hours at max brightness), charged over the 5V developer header (~3 hours to charge)
  sao_version: v1
get_one:
  price: $20.00
  price_usd: 20.0
  quantity: 11 unique designs
  availability: unknown
  distribution:
  - purchase
  - village
  where: 'Sold by Space Bits ''R Us team members (identifiable by their exclusive "Space Bits" team SAO) at the Hack-a-Sat competition area in the Aerospace Village at DEF CON 31, during specific windows around the competition: before 10 AM and after 8 PM Friday/Saturday, and before noon or after 1:30 PM Sunday. Only white-acrylic units included the LED board; excess stickers were also mounted on colored acrylic without electronics for general distribution.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/scottalmond/defcon_31/tree/master/pcb
  firmware_url: https://github.com/scottalmond/defcon_31/tree/master/src
  eda_tool: EasyEDA
links:
- label: www.youtube.com/watch?v=0cRPfB8QzD0&t=6s
  url: https://www.youtube.com/watch?v=0cRPfB8QzD0&t=6s
  kind: social
- label: scottalmond/defcon_31 (GitHub)
  url: https://github.com/scottalmond/defcon_31
  kind: repo
- label: 'DEFCON31 Space Pony Add-On (YouTube, bumper/info reel)'
  url: https://www.youtube.com/watch?v=0cRPfB8QzD0
  kind: video
- label: 'Features and Interfaces (YouTube)'
  url: https://www.youtube.com/watch?v=cUO3zqiO3F0
  kind: video
images:
- file: assets/images/badges/dc31/space-pony-sao/a694ee5638.jpg
  source: "https://github.com/scottalmond/defcon_31"
  credit: "Scott Almond / Sugar Morning"
  caption: "The 11 unique Pony SAO PCB designs"
- file: assets/images/badges/dc31/space-pony-sao/a734ee4a5f.jpg
  source: "https://github.com/scottalmond/defcon_31"
  credit: "Scott Almond / Sugar Morning"
  caption: "A batch of assembled Pony SAOs with acrylic and LEDs"
contact: {}
notes:
- There are 10 to choose from. The price is for one. These badass engineers made a bodacious SAO for the DC Badge. Something tells me your DC badge will be incomplete without one of these (those satchels are nice too).
- The GitHub repo and video describe 11 unique pony designs, not 10 as the sheet's note states.
status: listed
sources:
- kind: sheet
  event: dc31
  row: 71
  updated: '2023-07-27'
- kind: url
  url: https://www.youtube.com/watch?v=0cRPfB8QzD0
  title: DEFCON31 Space Pony Add-On
  accessed: '2026-09-06'
  note: Maker name (Scott Almond), distribution timing/location, and link to the GitHub project repo (via video description).
- kind: url
  url: https://github.com/scottalmond/defcon_31
  title: 'scottalmond/defcon_31: Space Pony Overview'
  accessed: '2026-09-06'
  note: Full technical spec (MCU, LEDs, battery, connectors), team credits, pricing, distribution details, fabrication process, and source images.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: The sheet listed the maker as "Space Bits 'R Us" (the team name), but the project's own repo credits Scott Almond as lead designer, with Brian Wilkins (firmware/games) and Sugar Morning (artwork) as collaborators; added as `role`. "Space Bits 'R Us" is also the name of a second, non-sale team badge documented in the same repo (10x RGB + 12x white LEDs, 500 mAh battery) worn by team members while selling these Pony SAOs -- that team badge is a separate item, not this one, and is not represented by this entry. Could not confirm current stock/sold-out status, PCB colors, or a license for the open-source files.
last_modified_date: '2026-09-06'
---

The Space Pony SAO is one of 11 uniquely-illustrated "My Little Pony Friendship is Magic"-themed add-ons designed by Scott Almond for DEF CON 31, with pony and space artwork by Sugar Morning and firmware/games (including a Morse code feature and a "Cyclone" game) by Brian Wilkins. Each board runs on an STM8S003F3P6TR microcontroller, lights ten through-hole RGB LEDs, includes a microphone and a user button, and is powered by a small 40 mAh LIR2032 LiPo cell charged through a developer header that also breaks out ST SWIM, UART, and I2C.

The boards were sold for $20 each by members of Space Bits 'R Us, a team competing in the Hack-a-Sat satellite hacking competition, who wore their own exclusive (non-sale) "Space Bits" team SAO to identify themselves at the Aerospace Village. Pony SAOs were available only during narrow windows around the competition schedule; only white-acrylic units carried the working LED board, while surplus stickers were mounted on colored acrylic without electronics for general giveaway.

## Make your own

Hardware (schematics and PCB fab files, designed in EasyEDA and fabricated via JLCPCB) and firmware source are both published in the [scottalmond/defcon_31](https://github.com/scottalmond/defcon_31) GitHub repository, under `/pcb` and `/src` respectively, along with the laser-cut acrylic files under `/cad`. No license is stated in the repo.
