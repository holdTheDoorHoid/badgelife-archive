---
title: Spectre Sniffer
id: dc34-spectre-sniffer
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: NilbinSec
  url: https://github.com/NilbinSec
summary: "NilbinSec's limited-release DEF CON 34 badge, a Ghostbusters-style no-ghost sign with a screaming ghost, built around a Seeed XIAO ESP32S3. It works as a live EMF detector with a spike graph on its OLED and a spirit box that generates words at a rate driven by the EMF reading; each badge came with one of four PAC-MAN Ghost SAOs."
functions: "Live EMF detector that samples electromagnetic fields and renders a real-time spike graph; integrated spirit box that pulls words from a randomized word bank with the EMF signal driving the output rate; one- and two-player arcade games; secrets on the badge, in the firmware and encoded on the back."
look:
  colors:
  - red
  - white
  - black
  shape: circle (no-ghost sign)
  themes:
  - horror
  - halloween
  - movie
  - pop culture
  - measurement
  form_factor: pcb badge
tech:
  mcu: XIAO ESP32S3 (Seeed Studio)
  leds: null
  display: OLED (I2C module; size not stated)
  connectivity:
  - usb
  - i2c
  - audio
  inputs:
  - buttons
  power: USB-C
  battery: protected 18650 (included)
  sao_version: v1.69bis
  sao_ports: 1
get_one:
  price: $80
  price_usd: 80.0
  quantity: 80 (Uberflux drop counter shows 80 sold, 0 remaining)
  availability: sold_out
  availability_note: "Uberflux listing checked 2026-09-06: 0 remaining, 80 sold, only a NOTIFY ME button."
  distribution:
  - purchase
  - preorder
  where: "Bought online on Uberflux, pickup only (no shipping) at DEF CON 34. Badges were dropped at the Badgelife Village and announced locations around the LVCC on a published schedule; unclaimed badges were to be donated to a deserving hacker at closing ceremonies."
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: "No hardware or firmware files for the badge itself were found. The bundled PAC-MAN Ghost SAO is published on GitHub with Gerbers, a pick-and-place file, a BOM and front/rear renders."
links:
- label: uberflux.com/product/NS-SpectreSniffer
  url: https://uberflux.com/product/NS-SpectreSniffer
  kind: store
- label: Announcement thread on the DEF CON forums (Buying and Selling)
  url: https://forum.defcon.org/node/255986
  kind: social
- label: PAC-MAN Ghost SAO repository (the SAO bundled with the badge)
  url: https://github.com/NilbinSec/PAC-MAN_Ghost_SAO
  kind: repo
- label: NilbinSec on GitHub
  url: https://github.com/NilbinSec
  kind: website
images:
- file: assets/images/badges/dc34/spectre-sniffer/c6da1bc065.jpg
  source: "https://uberflux.com/product/NS-SpectreSniffer"
  credit: "NilbinSec"
  caption: "Front of the Spectre Sniffer badge: red no-ghost sign with a white screaming ghost, OLED module in the centre and the SAO header on the ghost's hand"
- file: assets/images/badges/dc34/spectre-sniffer/5cc9868bd8.jpg
  source: "https://uberflux.com/product/NS-SpectreSniffer"
  credit: "NilbinSec"
  caption: "Back of the badge: Seeed XIAO ESP32S3 module with USB-C, buzzer, 18650 holder, four tactile buttons and the six-pin SAO header"
- file: assets/images/badges/dc34/spectre-sniffer/836fd6f302.jpg
  source: "https://uberflux.com/product/NS-SpectreSniffer"
  credit: "NilbinSec"
  caption: "The four colours of the PAC-MAN Ghost SAO; one randomly chosen ghost ships with each badge"
contact:
  discord: Nferno2
  emails:
  - nilbinsec@gmail.com
  handles:
  - '@nilbinsec'
  raw:
  - on all the social medias
notes:
- "The storefront and the forum thread call it the \"Spectre Sniffer Badge\"; the sheet's functions text read \"It will detect Ghosts!\"."
- "Proceeds were earmarked for NilbinSec's giveaway of over 1500 free SAOs at Hacker Summer Camp 2026."
- "The back silkscreen reads \"Designed By: 2PAC // F**K Contessa // Gemini\"; 2PAC is the NilbinSec member who posted the forum announcement."
- "The photo of the back shows four tactile switches (SW1-SW4), a buzzer (BZ1) and a six-pin SAO footprint labelled GPIO1/GPIO2/SDA/SCL/VCC/GND; the storefront tags list #ESP32, #EMF, #USBC and #Buzzer."
status: released
sources:
- kind: sheet
  event: dc34
  row: 4
  updated: 5/25/2026 19:53:54
  listing: New
- kind: sheet
  event: dc34
  row: 41
  updated: 7/10/2026 18:13:51
  listing: Update to Existing
- kind: url
  url: https://uberflux.com/product/NS-SpectreSniffer
  title: Spectre Sniffer Badge - Uberflux
  accessed: '2026-09-06'
  note: "Maker's storefront listing: description, feature list, XIAO ESP32S3, SAO v1.69bis, 18650, games, secrets, pickup-only drop rules, $80 price, 80 sold / 0 remaining, and the three product photos."
- kind: url
  url: https://forum.defcon.org/node/255986
  title: Spectre Sniffer Badge by NilbinSec - DEF CON Forums
  accessed: '2026-09-06'
  note: "Announcement by NilbinSec member 2PAC dated July 10, 2026: EMF ghost-hunting badge, $80 with one randomized PAC-MAN Ghost SAO, proceeds fund 1500+ free SAOs; same two photos as the storefront."
- kind: url
  url: https://github.com/NilbinSec/PAC-MAN_Ghost_SAO
  title: NilbinSec/PAC-MAN_Ghost_SAO on GitHub
  accessed: '2026-09-06'
  note: "README and files for the bundled SAO: 1000 made, 250 per colour, BOM (2x3 keyed header, two 160R resistors, two 0807 fast-flash RGB LEDs), Gerbers and pick-and-place file."
- kind: url
  url: https://github.com/NilbinSec
  title: NilbinSec on GitHub
  accessed: '2026-09-06'
  note: "Repository list checked for badge hardware or firmware; none found for the Spectre Sniffer. Used as the maker URL."
- kind: url
  url: https://github.com/NilbinSec/DC34_Main_Badge_Fuzzer_SAO
  title: NilbinSec/DC34_Main_Badge_Fuzzer_SAO on GitHub
  accessed: '2026-09-06'
  note: "Checked for any mention of the Spectre Sniffer; none. Documents a separate NilbinSec DC34 SAO."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: "Core facts come from the maker's own Uberflux listing and their DEF CON forum announcement. Not found: badge hardware or firmware files, the OLED size, LED count on the badge, a Hackaday.io page, press coverage, or any post-con photos from holders. Status is set to released because the Uberflux drop shows all 80 sold on a pickup-only item and DEF CON 34 has passed, not from a holder's report. The SAO colours disagree: the storefront and forum photos show purple, green, blue and red ghosts, while the SAO repository README says red, blue, purple and yellow. The defcon.social and X profiles returned 403 / were not fetched, so no social links were added beyond the sheet's handles. Searches tried: title + maker, title + DEF CON 34, maker + badge + 2026, title + SAO/ghost detector, title + GitHub/Hackaday/Reddit, title + hackaday/hackster roundup, social-site-restricted search."
last_modified_date: '2026-09-06'
---
The Spectre Sniffer is NilbinSec's badge for DEF CON 34, sold as a limited release of 80 through Uberflux at $80 each. The maker pitches it as a nostalgia piece for the 1984 ghost-hunting era: the front is a red no-ghost sign, except the ghost inside it wears a screaming mask that the listing says has been "legally distinct-ified". An OLED module sits across the middle of the sign, a six-pin SAO v1.69bis header is on the ghost's left hand, and the back carries a Seeed XIAO ESP32S3 with its USB-C port, a buzzer, four tactile buttons and a holder for the included protected 18650 cell.

Unlike the toy detectors it references, the badge actually measures something. Its EMF detector samples electromagnetic fields and draws a live spike graph, so the reading changes as the wearer moves around the con floor. A built-in spirit box pulls words from a randomized word bank, and the EMF level sets how quickly those words arrive: slow in a quiet room, fast during a spike. There are also one- and two-player arcade games, and NilbinSec says there are secrets on the badge, in the firmware and encoded on the back, in keeping with their earlier badges.

Every badge shipped with one of NilbinSec's PAC-MAN Ghost SAOs, chosen at random from four colours, which plugs into the badge's SAO port. The badge was pickup only: buyers ordered online and collected at drops held at the Badgelife Village and announced spots around the LVCC on a published schedule, and any badge not collected was to be donated to a deserving hacker at closing ceremonies. Proceeds went toward NilbinSec's plan to give away more than 1500 free SAOs at Hacker Summer Camp 2026. By September 2026 the Uberflux listing showed all 80 sold.

## Make your own

No design files for the badge itself have been published. The bundled PAC-MAN Ghost SAO is open on GitHub: the repository holds Gerbers, a pick-and-place file, a BOM (a 2x3 keyed header, two 160 R resistors and two 0807 fast-flash RGB LEDs) and front and rear renders, so the SAO can be ordered from any board house and hand-soldered.
