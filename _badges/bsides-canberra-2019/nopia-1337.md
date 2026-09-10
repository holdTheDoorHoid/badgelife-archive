---
title: Nopia 1337
id: bsides-canberra-2019-nopia-1337
layout: badge
parent: BSides Canberra 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-canberra-2019
year: 2019
makers:
- name: Peter Rankin (ec0 / Pete)
  url: https://github.com/BSidesCbr
summary: 'The official 2019 BSides Canberra conference badge: a PCB shaped like a classic Nokia candybar phone, with a Nokia 5110/3310-style LCD, three buttons, and green LEDs, sponsored by Privasec.'
functions: 'Runs custom ATmega328P firmware behind a Nokia 5110-style LCD; hardware and firmware source were released publicly. Sample firmware and radio (Si4455 sub-GHz) test code are included in the repo, suggesting Hardware Hacking Village reflashing/experimentation was part of the design.'
look:
  colors: [teal, white]
  shape: rectangle
  themes: [retro computer, security, hardware tool]
  form_factor: pcb badge
tech:
  mcu: ATMEGA328P
  leds:
    count: 4
    type: discrete
    note: SMD 0603 green LEDs
  display: Nokia 5110/3310-style LCD
  connectivity: [sub-ghz]
  inputs:
  - buttons
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed to attendees of BSides Canberra 2019, sponsored by Privasec.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/BSidesCbr/2019badge
  firmware_url: https://github.com/BSidesCbr/2019badge/tree/master/firmware
  eda_tool: KiCad
  notes: 'BSides Canberra publicly released all hardware and firmware source files for the 2019 badge on 20 March 2019 (Facebook announcement); repo requires KiCad 5.0+ and Arduino 1.8.5+.'
links:
- label: www.youtube.com/watch?v=T6UgVGUQrm4
  url: https://www.youtube.com/watch?v=T6UgVGUQrm4
  kind: video
- label: BSidesCbr/2019badge (GitHub)
  url: https://github.com/BSidesCbr/2019badge
  kind: repo
- label: 'Bsides 2019 Privasec Nopia Badges (YouTube)'
  url: https://www.youtube.com/watch?v=anlG0DL5fas
  kind: video
images:
- file: assets/images/badges/bsides-canberra-2019/nopia-1337/e4a13bdf7e.jpg
  source: "https://www.youtube.com/watch?v=anlG0DL5fas"
  credit: "Viv (@viv_yd), video still"
  caption: "Assembled Nopia 1337 badge, Nokia-phone-shaped PCB with LCD, three buttons, and Privasec sponsor branding"
contact: {}
notes:
- BSides Canberra 2019 electronic badge, designed by Peter Rankin (credited in the repo as "ec0 / Pete") with hardware and firmware released as open source. Originally imported from a sweep search snippet as "reflashable firmware ... supported in the Hardware Hacking Village"; that framing is not directly confirmed by the sources found, though the repo does include radio-chip sample/test firmware consistent with hackable design intent.
status: released
sources:
- kind: url
  url: https://www.youtube.com/watch?v=T6UgVGUQrm4
  title: Nopia 1337
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-canberra); event read as ''BSides Canberra 2019''.'
- kind: url
  url: https://github.com/BSidesCbr/2019badge
  title: BSidesCbr/2019badge
  accessed: '2026-09-10'
  note: 'Maker''s own repo: README names the badge "Nopia 1337" by "ec0 / Pete"; BOM lists ATMEGA328P-AU, Nokia 5110/3310 LCD, 4 pushbuttons, 4 green 0603 LEDs, CR2032 holder, 16MHz crystal; firmware-tests includes Si4455 sub-GHz radio sample code.'
- kind: url
  url: https://www.facebook.com/BSidesCanberra/posts/2116096088473955/
  title: 'BSides Canberra Facebook post announcing 2019 badge source release'
  accessed: '2026-09-10'
  note: 'Confirms public release of hardware+firmware source on 20 March 2019, linking to the same GitHub repo; notes KiCad 5.0+ and Arduino 1.8.5+ requirements.'
- kind: url
  url: https://www.youtube.com/watch?v=anlG0DL5fas
  title: 'Bsides 2019 Privasec Nopia Badges'
  accessed: '2026-09-10'
  note: 'Video (credit @viv_yd) shows the assembled badge in hand: Nokia-candybar-shaped teal PCB, LCD screen, three buttons, "Privasec" and "BSides Canberra / NOPIA 1337" silkscreen text; used for the saved image.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Core facts (maker, name, hardware) confirmed directly from the maker''s own GitHub repo and BSides Canberra''s own Facebook post. Price, quantity made, and specific distribution mechanics (e.g. whether it was sold, free, or raffled) were not stated in any source found and are left blank. The sweep''s claim of "reflashable firmware" tied to a Hardware Hacking Village session is plausible given the repo contents (radio chip test/sample firmware) but not directly confirmed by any source read, so it was softened rather than stated as fact.'
last_modified_date: '2026-09-10'
---

The Nopia 1337 was the official electronic badge for BSides Canberra 2019, designed by Peter Rankin (credited in the project repository as "ec0 / Pete") and sponsored by security firm Privasec. Its PCB is shaped and silkscreened to resemble a classic Nokia candybar phone, complete with a small monochrome LCD in the style of the Nokia 5110/3310 displays, three tactile buttons, and four green LEDs, all driven by an ATmega328P microcontroller and powered from a CR2032 coin cell.

BSides Canberra released the badge's full hardware (KiCad) and firmware source publicly on GitHub on 20 March 2019, along with a bill of materials and sample firmware. The repository also contains vendor sample/test code for a Silicon Labs Si4455 sub-GHz radio module, suggesting the badge (or a companion Hardware Hacking Village activity) was built around that radio hardware, though no source directly describes how that radio function was used at the event.

## Make your own

Hardware (KiCad 5.0+) and firmware (Arduino 1.8.5+) source are published at [github.com/BSidesCbr/2019badge](https://github.com/BSidesCbr/2019badge), including schematics, PCB layout, a bill of materials, and example firmware sketches under `firmware/`.
