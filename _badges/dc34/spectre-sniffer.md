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
  quantity: "80 (Uberflux DEF CON 34 drop, 80 sold and 0 remaining; total number made not stated)"
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
  notes: "No hardware or firmware files for the badge itself were found. The May 2026 community-sheet entry said the badge would be released on NilbinSec's GitHub on day one of DEF CON, but none of the account's 14 repositories is for the Spectre Sniffer as of 2026-09-06. The bundled PAC-MAN Ghost SAO is published on GitHub with Gerbers, a pick-and-place file, a BOM and front/rear renders."
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
  note: "Announcement by NilbinSec member 2PAC dated July 10, 2026: EMF ghost-hunting badge, $80 with one randomized PAC-MAN Ghost SAO, proceeds fund 1500+ free SAOs; two attached photos, the same front-of-badge and four-ghost-SAO photos as the storefront."
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
  notes: "Fact-checked 2026-09-06 against every cited source. The Uberflux listing supports the title, limited release, 1984 theme, XIAO ESP32S3, EMF spike graph, spirit box, SAO v1.69bis with I2C, 1-of-4 Pac-Man Ghost SAO, protected 18650 with lanyard, 1/2-player games, secrets, the legally distinct ghost, pickup-only drop rules, $80, 80 sold / 0 remaining and the tags; the forum post by 2PAC (July 10, 2026) supports the 1500+ free SAOs. The three photos are the storefront's own, and the forum's two attachments are the same front and four-SAO photos; the OLED, four buttons, buzzer, 18650 holder, single SAO header and the back silkscreen come from those photos. The contact block matches the community sheet rows, and the sheet's 'Badge Pre-orders with delivery at Defcon' supports preorder. Inferred rather than sourced: status released rests on a pickup-only drop showing 80 sold and DEF CON 34 having ended, not on a holder's report. Still unknown: total number made, OLED size, LED count, whether the XIAO's Wi-Fi/BLE is used. The SAO colours disagree: storefront and forum photos show purple, green, blue and red ghosts, while the PAC-MAN_Ghost_SAO README says red, blue, purple and yellow. The sheet said the badge would be released on GitHub on day one of DEF CON; none of NilbinSec's 14 repositories is for the badge. defcon.social returned 403 and X was not fetched; a search for post-con coverage found nothing beyond the sources already cited."
last_modified_date: '2026-09-06'
---
The Spectre Sniffer is NilbinSec's badge for DEF CON 34, sold as a limited release of 80 through Uberflux at $80 each. The maker pitches it as a nostalgia piece for the 1984 ghost-hunting era: the front is a red no-ghost sign, except the ghost inside it wears a screaming mask that the listing says has been "legally distinct-ified". An OLED module sits across the middle of the sign, a six-pin SAO v1.69bis header sits on the ghost's hand at the left of the sign, and the back carries a Seeed XIAO ESP32S3 with its USB-C port, a buzzer, four tactile buttons and a holder for the included protected 18650 cell.

Unlike the toy detectors it references, the badge actually measures something. Its EMF detector samples electromagnetic fields and draws a live spike graph, so the reading changes as the wearer moves around the con floor. A built-in spirit box pulls words from a randomized word bank, and the EMF level sets how quickly those words arrive: slow in a quiet room, fast during a spike. There are also one- and two-player arcade games, and NilbinSec says there are secrets on the badge, in the firmware and encoded on the back ("This is a NilbinSec badge. You know what that means.").

Every badge shipped with one of NilbinSec's PAC-MAN Ghost SAOs, chosen at random from four colours, which plugs into the badge's SAO port. The badge was pickup only: buyers ordered online and collected at drops held at the Badgelife Village and announced spots around the LVCC on a published schedule, and any badge not collected was to be donated to a deserving hacker at closing ceremonies. NilbinSec said the proceeds would fund its plan to give away more than 1500 free SAOs at Hacker Summer Camp 2026. By September 2026 the Uberflux listing showed all 80 sold.

## Make your own

No design files for the badge itself have been published. The bundled PAC-MAN Ghost SAO is open on GitHub: the repository holds Gerbers, a pick-and-place file, a BOM (a 2x3 keyed header, two 160 R resistors and two 0807 fast-flash RGB LEDs) and front and rear renders, enough to have the SAO boards made and populated. The community sheet entry from May 2026 said the badge itself would be released on NilbinSec's GitHub on day one of DEF CON, but no such repository existed when checked in September 2026.
