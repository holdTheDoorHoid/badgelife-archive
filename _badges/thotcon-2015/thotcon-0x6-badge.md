---
title: THOTCON 0x6 Badge
id: thotcon-2015-thotcon-0x6-badge
layout: badge
parent: THOTCON 0x6
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: thotcon-2015
year: 2015
makers:
- name: THOTCON organizers (hardware/firmware documented by attendee Gigawatts, aka rlankenau)
summary: The official THOTCON 0x6 (2015) attendee badge is an Arduino Leonardo-compatible board built around an ATmega32u4, with six addressable RGB LEDs and an IR transceiver used for a badge-to-badge "infection" game.
functions: 'Plays an IR-based "infection" game between badges; exposes a 2400-baud serial terminal with an interactive menu and an EEPROM editor; hides an "IR Shark" tool for sniffing/dumping IR remote codes.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - security
tech:
  mcu: ATmega32u4 (Arduino Leonardo-compatible, with Arduino bootloader)
  leds:
    count: 6
    type: WS2812B
    note: Adafruit NeoPixels wired to a single digital pin
  display: none
  connectivity:
  - ir
  - uart
  battery: 2x CR2032 (stock); some attendees modified badges with a 2s2p supercapacitor pack (four 2.7V 34F AA-size caps) and a JST USB-recharge connector for longer runtime
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to THOTCON 0x6 (2015) attendees as the conference badge.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/rlankenau/thotcon0x6
  firmware_url: https://github.com/rlankenau/thotcon0x6
  eda_tool: null
  notes: 'Repo (MIT licensed) hosts hardware, firmware ("code"), flashing tools, and a BoM; maintained by attendee rlankenau (Gigawatts), not confirmed as an official THOTCON org account.'
links:
- label: hackaday.io/project/5862-thotcon-0x06-badge-hacking
  url: https://hackaday.io/project/5862-thotcon-0x06-badge-hacking
  kind: hackaday
- label: github.com/rlankenau/thotcon0x6
  url: https://github.com/rlankenau/thotcon0x6
  kind: repo
images:
  - file: assets/images/badges/thotcon-2015/thotcon-0x6-badge/b337f35431.jpg
    source: "https://hackaday.io/project/5862-thotcon-0x06-badge-hacking"
    credit: "Gigawatts (Hackaday.io)"
    caption: "THOTCON 0x6 badge with supercapacitor modification"
  - file: assets/images/badges/thotcon-2015/thotcon-0x6-badge/a9c7772c65.png
    source: "https://hackaday.io/project/5862-thotcon-0x06-badge-hacking"
    credit: "Gigawatts (Hackaday.io)"
    caption: "THOTCON 0x6 badge detail"
contact: {}
notes:
- 'Official THOTCON 0x6 (2015) badge: ATmega32u4 (Arduino Leonardo compatible) with 6 Adafruit NeoPixels, an IR transceiver for an attendee ''infection'' game, and a 2400-baud serial terminal game, powered by 2x CR2032 cells; not yet in the archive. Found by the event-year sweep, task thotcon-a.'
- 'Sweep''s wording ("badge programmable/hacked by Gigawatts") kept above in makers; Gigawatts appears to be an attendee (Hackaday.io handle "gigawatts", GitHub user rlankenau) who documented/modified the stock badge rather than an official THOTCON organizer, though sources do not clarify who designed the original hardware.'
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/5862-thotcon-0x06-badge-hacking
  title: THOTCON 0x6 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:thotcon-a); event read as ''thotcon-2015''.'
- kind: url
  url: https://hackaday.io/project/5862-thotcon-0x06-badge-hacking
  title: Thotcon 0x06 Badge Hacking (Hackaday.io project by Gigawatts)
  accessed: '2026-09-08'
  note: 'Confirmed MCU, LED count/type, IR receiver/emitter parts, stock CR2032 power, serial terminal/EEPROM editor, IR Shark tool, and the supercapacitor mod; supplied badge photos.'
- kind: url
  url: https://github.com/rlankenau/thotcon0x6
  title: rlankenau/thotcon0x6
  accessed: '2026-09-08'
  note: 'MIT-licensed repo with hardware, firmware, flashing tools, and BoM folders; used for open_source and hardware/firmware_url fields.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core hardware/firmware facts are confirmed by a maker/attendee-authored Hackaday.io project and its linked GitHub repo, but neither source states who inside THOTCON designed the original badge, nor gives price, quantity, or a distribution date beyond "given to attendees." Left get_one.price, get_one.quantity, and look.colors/shape empty since no source described the PCB appearance or numbers made.'
last_modified_date: '2026-09-08'
---

The THOTCON 0x6 badge, handed out at THOTCON's sixth Chicago conference in 2015, is an Arduino Leonardo-compatible board built around an ATmega32u4. Six Adafruit NeoPixels give it addressable RGB lighting, and a Vishay IR receiver/emitter pair let badges talk to each other for an on-site "infection" game, in the vein of the badge-to-badge games common at the time. A hidden serial console, reachable over a 2400-baud UART, exposes an interactive menu and an EEPROM editor, and buried inside it is an "IR Shark" utility for capturing and dumping codes from ordinary IR remotes.

Stock power came from two CR2032 coin cells, which by most accounts didn't last the weekend running six NeoPixels and an IR radio. Attendee and hardware hacker Gigawatts (GitHub user rlankenau) documented the badge in detail on Hackaday.io and published a modification swapping the coin cells for a 2s2p bank of four 2.7V/34F supercapacitors, wired through a JST connector so the badge could be topped off over USB — stretching runtime to roughly two hours per charge.

Hardware, firmware, a bill of materials, and flashing utilities for the badge live in an MIT-licensed GitHub repository maintained by rlankenau. It is not clear from available sources whether this repo is THOTCON's own release of the badge design or an attendee's independent write-up of it; either way it is the fullest public record of the board.
