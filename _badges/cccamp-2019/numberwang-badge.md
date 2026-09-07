---
title: Numberwang Badge
id: cccamp-2019-numberwang-badge
layout: badge
parent: CCCamp19
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cccamp-2019
year: 2019
makers:
- name: timonsku
  url: https://github.com/timonsku
summary: A last-minute ATSAMD21G18 (Itsy Bitsy M0-compatible) badge with a MAX98357A I2S audio amp and a LiPo charger, made for the Numberwang village at CCCamp19 and handed out as unpopulated PCBs with CircuitPython firmware that plays Numberwang sound clips.
functions: Plays audio clips through the onboard I2S amplifier and lights two status LEDs, letting the wearer "pretend to play Numberwang" (a running joke from the British comedy sketch of the same name) at the village built around it.
look:
  colors:
  - black
  shape: rectangle
  themes:
  - meme
  - tv
  - text
  - village badge
tech:
  mcu: ATSAMD21G18
  leds:
    count: 2
    type: discrete
    note: 'One orange charge-status LED (CHG1) and one red status LED (L1), both 0805; the released BOM lists no addressable LEDs.'
  display: none
  connectivity:
  - audio
  - usb
  battery: LiPo, JST-PH 2.0 SMT right-angle connector (reversed polarity vs. Adafruit's convention)
  sao_version: none
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  - village
  where: Handed out by the maker as unpopulated PCBs to attendees interested in the Numberwang village at CCCamp19; recipients self-assembled the board using the BOM and documentation on GitHub.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/timonsku/Numberwang-Badge
  firmware_url: https://github.com/timonsku/Numberwang-Badge
  eda_tool: Eagle
links:
- label: github.com/timonsku/Numberwang-Badge
  url: https://github.com/timonsku/Numberwang-Badge
  kind: repo
  archived: https://web.archive.org/web/20260907111136/https://github.com/timonsku/Numberwang-Badge
- label: hackaday.io/project/167356-numberwang-badge
  url: https://hackaday.io/project/167356-numberwang-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260907111101/https://hackaday.io/project/167356-numberwang-badge
- label: twitter.com/i/status/1162331672601403394
  url: https://twitter.com/i/status/1162331672601403394
  kind: social
images:
- file: assets/images/badges/cccamp-2019/numberwang-badge/00ca752b29.jpg
  source: "https://hackaday.io/project/167356-numberwang-badge"
  credit: "timonsku"
  caption: "The Numberwang Badge, lit up and worn on a lanyard at CCCamp19"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/timonsku/Numberwang-Badge
  title: Numberwang Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260907111136/https://github.com/timonsku/Numberwang-Badge
- kind: url
  url: https://github.com/timonsku/Numberwang-Badge
  title: "Numberwang-Badge repo: readme, BOM.csv, PCB/ (Eagle .sch/.brd), CPY/ (CircuitPython), bootloader and UF2 files"
  accessed: '2026-09-07'
  note: 'Confirms MCU (ATSAMD21G18), audio amp (MAX98357A I2S 3.2W mono amp), flash (Winbond W25Q16JVSSIQ), LiPo charging with reversed-polarity JST-PH 2.0, a known audio-circuit bug fixed with a bodge wire, and that the design is Adafruit Itsy Bitsy M0-compatible. BOM lists only two discrete 0805 LEDs (orange charge indicator, red status), not an addressable strip. Hardware is Eagle (.sch/.brd), not KiCad; no license file present.'
- kind: url
  url: https://hackaday.io/project/167356-numberwang-badge
  title: Numberwang Badge - Hackaday.io
  accessed: '2026-09-07'
  note: 'Confirms it was made for the Numberwang village at CCCamp19, "does blinkies and sound," and that unpopulated PCBs were handed out directly by the maker to interested attendees. Project cover photo saved as an image.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched the GitHub repo (README, raw BOM.csv, PCB/ folder listing) and the Hackaday.io project page, and confirmed every remaining hardware/distribution claim (ATSAMD21G18, MAX98357A, W25Q16JVSSIQ flash, MCP73831T LiPo charger, AP2112K-3.3 regulator, reversed-polarity JST-PH 2.0, two discrete 0805 LEDs only, Eagle .sch/.brd files, "handed out unpopulated PCBs" distribution, village/CCCamp19 context, and the README''s own wording of the audio-bodge-wire bug). Corrected two errors found during this pass: (1) eda_tool had been set to null with a stated rationale that Eagle "is not one of the listed vocab options" - that is incorrect, Eagle is explicitly in the guide''s eda_tool vocabulary, so it is now set to Eagle. (2) The second image (b2b0d62de2.jpg, captioned as a photo of "the assembled board, showing the bodge wire") was actually the repo''s Bodge-Fix-Audio.png - an Eagle PCB-layout screenshot with an instructional text overlay ("Connect SAMD Pin 12 ... with wire"), not a photograph of a physically assembled board or a soldered bodge wire. Removed the image file and its entry; the guide requires photos of the item itself, and the caption misdescribed what the image actually showed. Corrected the body text''s "documented with a reference photo" to "documented with a reference diagram" to match. The remaining image (00ca752b29.jpg, the Hackaday cover photo of the badge lit up on a lanyard) was viewed directly and matches its caption and the multicolor-"numberwang"-text discrepancy already noted below. Quantity made and any price beyond "free" remain unstated in any source found. The Twitter/X status link (video demo) could not be fetched (HTTP 402 from x.com) and remains an unreached social link. The BOM lists only two single-color discrete LEDs, which does not match a "DotStar LEDs" claim from the original community-sheet import; that claim stays dropped as unconfirmed. The photo''s multicolor lit "numberwang" text is most likely a long-exposure/motion effect rather than evidence of addressable LEDs, since it is not supported by the BOM - noted here as a source disagreement, not stated as fact in the body.'
last_modified_date: '2026-09-07'
---

The Numberwang Badge was a self-described "stupid last minute project" that maker timonsku (GitHub) put together for the Numberwang village at CCCamp19 in 2019 - a village built as a running gag around the fictional game "Numberwang" from the British sketch show *That Mitchell and Webb Look*. Rather than selling or raffling the board, timonsku handed out unpopulated PCBs directly to anyone at camp who was interested, with the expectation that recipients would source parts themselves (mostly from LCSC or Mouser) and solder the board by hand.

Electrically, the badge is close to a clone of Adafruit's Itsy Bitsy M0, built around an ATSAMD21G18 microcontroller with the same pinout, plus an added LiPo charge circuit (using a JST-PH 2.0 connector wired with reversed polarity to match batteries the maker could actually buy in Germany). A MAX98357A I2S amplifier drives audio playback of Numberwang sound clips, and a Winbond W25Q16 SPI flash chip stores data alongside the SAMD21's own flash. The board shipped with a known bug - a mis-named signal left the amp's input floating - fixed with a single bodge wire that the maker documented with a reference diagram. Two discrete 0805 LEDs (an orange charge indicator and a red status LED) round out the board's visual feedback; no addressable LED strip appears in the bill of materials, despite a multicolor lit-up "numberwang" effect visible in the project's cover photo.

## Make your own

Hardware (Eagle schematic and board files) and firmware are both published in the [GitHub repo](https://github.com/timonsku/Numberwang-Badge), along with a BOM, a UF2-format CircuitPython build, and the Itsy Bitsy M0 bootloader binary. Anyone building one from scratch would need to: fabricate the board from the Eagle files, populate it per the BOM (noting that some passives are listed redundantly in both 0603 and 0805 footprints - either size works), flash the bootloader via the SWD test pads (pogo pins or a pressed header work), then load the provided CircuitPython UF2, and apply the audio bodge-wire fix described in the readme and shown in the reference photo.
