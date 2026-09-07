---
title: Ph0xx
id: fri3d-2018-ph0xx
layout: badge
parent: Fri3d 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: fri3d-2018
year: 2018
makers:
- name: Fri3d Camp
  url: https://github.com/Fri3dCamp
summary: Ph0xx is the ESP32-WROOM-32 attendee badge for Fri3d Camp 2018 in Belgium (650 boards built for close to 600 attendees, given free), with two 5x7 LED matrices, an ADXL345 accelerometer, 18650 battery with TP4056/DW01-P charging and protection, touch buttons, buzzer, expansion headers and Lego Technic compatible holes, designed by Wim Van Gool and Bert Outtier.
functions: Blinky/LED-eye display modes with a browser-based animation editor built by Area 3001 volunteers for programming the matrices; expandable through "Jewel" add-on modules (an Air Jewel for environmental sensors and a Bot Jewel for servo control) plugged into the badge's headers.
look:
  colors: []
  shape: null
  themes:
  - robot
  - wearable
tech:
  mcu: ESP32-WROOM-32
  leds:
    count: 70
    type: discrete
    note: Two 5x7 LED matrices used as animated "eyes"; the designer desoldered and swapped all 70 LEDs on his own badge from blue to green as a one-off hack just before camp, not a broader production change.
  display: LED matrix 5x7 (x2)
  connectivity:
  - wifi
  - ble
  - i2c
  battery: 18650 Li-ion with TP4056 charge controller and DW01-P protection IC
  sao_version: null
get_one:
  price: free
  price_usd: null
  quantity: '650'
  availability: free
  where: Given to Fri3d Camp 2018 attendees in Belgium (close to 600 attendees expected to receive one); 650 boards were built and tested, with early prototypes hand-placed/reflowed and the bulk (460 boards) mass-produced in one day at More-at-Mere.
make_your_own:
  open_source: true
  hardware_url: https://github.com/Fri3dCamp/badge
  firmware_url: https://github.com/Fri3dCamp/Fri3dBadge
  eda_tool: null
links:
- label: hackaday.io/project/160451-ph0xx
  url: https://hackaday.io/project/160451-ph0xx
  kind: hackaday
- label: github.com/Fri3dCamp/badge
  url: https://github.com/Fri3dCamp/badge
  kind: repo
- label: github.com/Fri3dCamp/Fri3dBadge
  url: https://github.com/Fri3dCamp/Fri3dBadge
  kind: repo
- label: fri3d.be
  url: http://fri3d.be/
  kind: website
images:
- file: assets/images/badges/fri3d-2018/ph0xx/c9b8bf3af3.jpg
  source: https://hackaday.io/project/160451-ph0xx
  credit: Fri3d Camp
  caption: The Ph0xx badge with its two 5x7 LED matrices
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/160451-ph0xx
  title: Ph0xx
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/160451-ph0xx
  title: Ph0xx
  accessed: '2026-09-07'
  note: 'Maker''s own project page; confirmed maker names, event/year, ESP32-WROOM-32, two 5x7 LED matrices, ADXL345, 18650/TP4056/DW01-P power, touch buttons, buzzer, Lego Technic holes, and the Area 3001 web animation tool. Project logs give two different counts: close to 600 camp attendees expected to receive a badge, and 650 boards built/tested for production, with 460 assembled in one day at More-at-Mere after hand-placed/reflowed prototypes; one log also shows the LED color-swap was the designer''s own single badge, not a wider batch change. Source of the saved photo.'
- kind: url
  url: https://github.com/Fri3dCamp/badge
  title: Fri3dCamp/badge
  accessed: '2026-09-07'
  note: Hardware design repo for the Fri3d Camp 2018 badge; confirms design files/datasheets are published there and points to fri3d.be/badge and the 2018 camp wiki for more detail.
- kind: url
  url: https://github.com/Fri3dCamp/Fri3dBadge
  title: Fri3dCamp/Fri3dBadge
  accessed: '2026-09-07'
  note: Arduino library/firmware repo for the badge; confirms ESP32, ADXL345, two buttons plus two touchpads, buzzer, 5x7-ish LED matrix support, and Servo Jewel add-on.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07) re-read every cited source. Corrections made: get_one.quantity changed from ''about 600'' to ''650'' (the Hackaday project logs give 650 as the number of boards built/tested, distinct from the close-to-600 camp attendees who would each receive one — the entry had conflated the two); get_one.price/availability changed from empty/''unknown'' to ''free'' (the badge was a free attendee giveaway, matching the existing free_drop distribution tag, so ''unknown'' was an unsupported hedge); ''hand-soldered'' corrected to ''hand-placed with solder paste and reflowed'' per the maker''s own prototype-assembly log, which explicitly says placement (not soldering) was manual; the LED color-swap note was narrowed from ''some units... others'' to the designer''s own single badge, since the source log describes one person modifying his own board, not a batch change; make_your_own.open_source changed from ''partial'' to ''yes'' since both the hardware repo (full Altium
    schematic/PCB files under design/v1-v4) and the firmware repo (full Arduino/PlatformIO source, not just a compiled blob) are genuinely published, matching the guide''s definition of ''yes''. Images, links, MCU/LED/battery/sensor/input specs, the Air Jewel/Bot Jewel description, and the Area 3001 web animation tool all checked out unchanged against the maker''s own Hackaday page and the two Fri3dCamp GitHub repos. Not independently checked: fri3d.be''s current site only briefly mentions later-year badges and had nothing on the 2018 unit; wiki2018.fri3d.be could not be reached (TLS cert issue). tech.sao_version, look.colors/shape, tech.eda_tool, contact, and get_one.price_usd remain empty/null because no source stated them — left as-is rather than guessed. Note for a future research pass, not acted on here (no new research scope): the hardware repo''s design files are Altium Designer format (.PcbDoc/.SchDoc), so make_your_own.eda_tool could be set to ''Altium'' if that field is revisited.'
last_modified_date: '2026-09-07'
model:
  file: assets/models/fri3d-2018/ph0xx.glb
  method: kicad
  source_file: fri3d-badge-2018.brd
  generated: '2026-09-07'
  bytes: 155540
---

Ph0xx was the attendee badge for Fri3d Camp 2018, a family hacker/maker/DIY camp in Belgium, designed by Wim Van Gool and Bert Outtier for the Fri3d Camp team. Built around an ESP32-WROOM-32, it wears two 5x7 LED matrices as animated eyes, an ADXL345 accelerometer for motion-reactive effects, touch buttons, and a buzzer, all powered by a rechargeable 18650 cell with TP4056 charging and DW01-P protection. The board even includes Lego Technic-compatible mounting holes so it could be built into camp builds. 650 boards were built and tested for close to 600 camp attendees, given free; after early prototypes were hand-placed with solder paste and reflowed in a small oven, the bulk of the run (460 boards in a single day) was mass-produced at a facility called More-at-Mere.

The badge could be extended with plug-in "Jewel" modules, including an Air Jewel carrying environmental sensors and a Bot Jewel for driving servos, and camp volunteers from Area 3001 built a browser-based animation tool for programming the LED-eye patterns.

## Make your own

Both the hardware design and firmware are published on GitHub under the Fri3dCamp organization: `Fri3dCamp/badge` holds the board design and datasheets, and `Fri3dCamp/Fri3dBadge` is the Arduino library used to program the ESP32, its LED matrices, buttons/touchpads, buzzer, and the Servo Jewel accessory.
