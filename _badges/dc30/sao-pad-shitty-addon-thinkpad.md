---
title: sao_pad — shitty addon thinkpad
id: dc30-sao-pad-shitty-addon-thinkpad
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: kaybarkbark
  url: https://github.com/kaybarkbark
summary: An open-source SAO shaped like a shrunken IBM/Lenovo ThinkPad, built around a Digispark (ATtiny85) module driving a small I2C OLED that scrolls fake x86-assembly text, with joke IBM/"Lenowo" logo graphics on the board.
functions: 'Drives a 128x64 I2C OLED via the DigisparkOLED library: shows a "hack.asm Run!" header, then loops screens of fake x86 assembly-mnemonic text (with a 1% chance per cycle of a joke message instead); a bundled logo bitmap (digistump_128x64c1.h) exists in the repo but is not called anywhere in the published sketch, so no bitmap image is actually displayed. No other interactive functions found in the published source.'
look:
  colors:
  - black
  shape: rectangle
  themes:
  - retro computer
  - meme
  - pop culture
  - text
tech:
  mcu: ATtiny85 (Digispark)
  leds: null
  display: 128x64 I2C OLED
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: v1.69bis
  sao_ports: 1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/kaybarkbark/sao_pad
  firmware_url: https://github.com/kaybarkbark/sao_pad/tree/main/code/oled
  eda_tool: KiCad
links:
- label: github.com/kaybarkbark/sao_pad
  url: https://github.com/kaybarkbark/sao_pad
  kind: repo
images: []
contact: {}
notes:
- This appears to be the same design family as the separately-listed "Sh*tPad SAO" sold on Tindie by DC Punks (Kay Kidoutai and NeonPlaidPants) for DEF CON 31 — see duplicate_of. Both use a Digispark (ATtiny85), an I2C OLED, and footprints/silkscreen named after IBM and a misspelled "Lenowo" on a ThinkPad-parody SAO. "kaybarkbark" plausibly corresponds to "Kay Kidoutai" of DC Punks, but that identity was not explicitly confirmed by any source read.
- Repo timestamps (created 2022-07-04, PCB backup files dated 2022-10-22 through 2022-12-04) predate the DEF CON 31 (Aug 2023) Tindie listing, which itself describes that listing as a rerun of "an earlier run" — consistent with this repo being the original design from DEF CON 30 (Aug 2022). No source explicitly states which con it was built for; event/year here are a date-based inference, not a maker statement.
status: released
sources:
- kind: url
  url: https://github.com/kaybarkbark/sao_pad
  title: sao_pad — shitty addon thinkpad
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://api.github.com/repos/kaybarkbark/sao_pad/git/trees/main?recursive=1
  title: sao_pad repo file tree (GitHub API)
  accessed: '2026-09-07'
  note: 'Confirmed contents: KiCad project/gerbers for a board called "shitpad", a Digispark footprint, logo footprints named "ibm", "lenowo" and "smug", an OLED_I2C footprint, and Arduino source (code/oled/oled.ino, digistump_128x64c1.h, img0_128x64c1.h). No README, price, quantity, or event was stated in the repo.'
- kind: url
  url: https://raw.githubusercontent.com/kaybarkbark/sao_pad/main/code/oled/oled.ino
  title: sao_pad firmware source (oled.ino)
  accessed: '2026-09-07'
  note: 'Fact-check pass, 2026-09-07: read the actual sketch. It shows a "hack.asm Run!" header then loops fake x86 assembly-mnemonic text lines via oled.println(), with a 1% chance per cycle of printing a joke line instead. It never calls a bitmap/drawBitmap function and never references digistumplogo or img0_128x64c1.h, contradicting the prior claim that it "shows a boot logo" / "bitmap image" — corrected.'
- kind: url
  url: https://raw.githubusercontent.com/kaybarkbark/sao_pad/main/shitpad.kicad_pcb
  title: sao_pad PCB source (shitpad.kicad_pcb)
  accessed: '2026-09-07'
  note: 'Fact-check pass, 2026-09-07: found only 6 footprints actually placed on the board (Digispark, OLED_I2C, and single ibm/lenowo/smug logo graphics) — no footprint or silkscreen resembling a "keyboard", so that claim in the prior summary was removed. Also found connector J1, silkscreened "Shitty Connector", is a PinSocket_2x03_P2.54mm (2x3, 6-pin) footprint, matching the 6-pin SAO header spec — used to fill tech.sao_version/sao_ports, previously left null.'
- kind: url
  url: https://api.github.com/repos/kaybarkbark/sao_pad
  title: sao_pad repo metadata (GitHub API)
  accessed: '2026-09-07'
  note: created_at 2022-07-04, used to infer the DEF CON 30 (2022) timing noted above; description is simply "shitty addon thinkpad".
- kind: url
  url: https://api.github.com/repos/kaybarkbark/sao_pad/commits?per_page=100
  title: sao_pad commit history (GitHub API)
  accessed: '2026-09-07'
  note: 'Fact-check pass, 2026-09-07: 4 commits total (2022-07-04, 2022-10-09, 2022-11-24 "ordered", 2023-07-27). Checked the 2023-07-27 commit specifically since it is close to DEF CON 31 (Aug 2023) and could have undermined the DC30 dating: it only adds a backup zip file itself dated 2022-12-04 in its filename plus a trivial project-settings tweak, so it does not represent new 2023 design work and does not contradict the DC30 inference. The "ordered" commit message (2022-11-24) supports that PCBs were actually fabricated, not just designed.'
- kind: url
  url: https://github.com/kaybarkbark
  title: kaybarkbark GitHub profile
  accessed: '2026-09-07'
  note: Bio says the account moved to Codeberg; no conference, location, or contact info given. Checked codeberg.org/kaybarkbark too — no sao_pad/thinkpad-related repo found there.
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Fact-check pass, 2026-09-07: opened every cited source plus the firmware and PCB source files. Two claims in the original write-up were not supported and have been corrected: the summary/functions/body said the OLED "shows a boot logo" / "bitmap image", but the actual sketch (oled.ino) never displays the bundled bitmap and instead scrolls fake x86 assembly text — fixed. The summary also claimed a "silkscreened keyboard" on the front; the PCB file has no such footprint or artwork (only ibm/lenowo/smug logo graphics), so that detail was invented and has been removed. One field was filled in during this pass from direct inspection of shitpad.kicad_pcb: the "Shitty Connector" (J1) is a 2x3, 6-pin header, matching the standard SAO connector, so tech.sao_version/sao_ports were set instead of left null. The commit history was also checked to stress-test the DC30-vs-DC31 dating inference — a 2023-07-27 commit (close to DEF CON 31) turned out to only add an already-dated 2022-12-04 backup
    file, so it does not undermine the DC30 attribution, which remains an inference from file timestamps, not a maker statement. No press coverage, storefront, price, quantity, or maker statement about which event this was built for was found. This is very likely the same underlying design as dc31/shitpad-sao-cannot-wait-to-see-this-one (DC Punks'' "Sh*tPad SAO"), flagged as duplicate_of, but the two were kept as separate entries per instructions since the maker-identity link (kaybarkbark = Kay Kidoutai) was not confirmed and no image comparison was done. No real photos of the assembled board were found; the repo only contains KiCad per-layer render exports and a price spreadsheet (shitpad_price.ods) that was not opened (binary spreadsheet, no legible price extracted), not photos of a finished unit. Because two claims had to be corrected and one field remains an inference (sao_version), status is kept at "researched" rather than promoted to "verified".'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/sao-pad-shitty-addon-thinkpad/
related:
- dc31-shitpad-sao-cannot-wait-to-see-this-one
---

kaybarkbark's `sao_pad` GitHub repository publishes the open-source hardware and firmware for a "shitty addon thinkpad" — a ThinkPad-parody SAO. The KiCad project ("shitpad") includes logo footprints named "ibm", "lenowo" and "smug" alongside a Digispark (ATtiny85) module and an I2C OLED footprint, wired to a 6-pin connector silkscreened "Shitty Connector" that matches the standard SAO header. The repo's Arduino sketch (`code/oled/oled.ino`) drives a 128x64 OLED via the DigisparkOLED library, showing a "hack.asm Run!" boot header and then scrolling fake x86 assembly-mnemonic text (with an occasional joke line); a logo bitmap is bundled in the repo but is never called by the sketch, so no image is actually displayed on the running board. Gerbers and a full KiCad project (schematic, PCB, backups) are included, but there is no README, no price or quantity information, and no statement of which convention it was made for.

The design closely matches a separately-documented item in this archive: DC Punks' "Sh*tPad SAO," sold on Tindie for DEF CON 31 (2023) as a rerun of an earlier batch. Both use the same core parts (Digispark, I2C OLED) and the same IBM/"Lenowo" joke branding. Repo file dates (created July 2022, PCB backups through December 2022) place this repository's work well before the DEF CON 31 rerun, so it is tentatively attributed here to DEF CON 30 (August 2022) as the likely original run — an inference from timestamps, not a confirmed maker statement, since no source ties "kaybarkbark" explicitly to the DC Punks maker duo.
