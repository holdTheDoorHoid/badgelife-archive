---
title: Mini Acrylic Sign Addon
id: dc30-mini-acrylic-sign-addon
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: trueControl (true)
summary: An edge-lit acrylic badge addon and USB-powered desk ornament, with a custom-engraved acrylic sign lit from up to six RGB LEDs.
functions: Lights the engraved acrylic sign from LEDs arranged in 2-3 zones; doubles as a USB desk ornament that emulates a Corsair iCUE Lighting Node PRO (works with iCUE, SignalRGB, OpenRGB in Direct mode); a front sensor LED does light sensing/status; two bottom buttons handle configuration.
look:
  colors: []
  shape: null
  themes:
  - text
tech:
  mcu: EFM8UB10F8G-QFN20
  leds:
    count: 6
    type: RGB
    note: 4x or 6x RGB LEDs arranged in pairs for 2 or 3 zones; up-fire and edge-light the engraved acrylic sign. A separate front LED handles status/light sensing.
  display: null
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://git.trueserve.org/trueControl/dc30-acrylic-mini-sign-addon
  firmware_url: https://git.trueserve.org/trueControl/dc30-acrylic-mini-sign-addon
  eda_tool: KiCad
links:
- label: basic.truecontrol.org/database/dc30/mini-acrylic-sign
  url: https://basic.truecontrol.org/database/dc30/mini-acrylic-sign/
  kind: website
- label: git.trueserve.org/trueControl/dc30-acrylic-mini-sign-addon
  url: https://git.trueserve.org/trueControl/dc30-acrylic-mini-sign-addon
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: released
sources:
- kind: url
  url: https://basic.truecontrol.org/database/dc30/mini-acrylic-sign/
  title: Mini Acrylic Sign Addon
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc30''.'
- kind: url
  url: https://git.trueserve.org/trueControl/dc30-acrylic-mini-sign-addon
  title: 'trueControl/dc30-acrylic-mini-sign-addon (Gitea repo, README)'
  accessed: '2026-09-07'
  note: Primary source for hardware/firmware specs, MCU, LED layout, USB/iCUE behavior, GAT connector, and design tools (KiCad, Lightburn, Keil C51). Page itself is empty of prose on server render; basic.truecontrol.org listing gives only navigation context, no body text was retrievable.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The maker''s own repo README is the source for nearly everything here; the basic.truecontrol.org catalog page itself renders no readable body text server-side (JS-driven mkdocs theme with an empty content div), so it could not independently confirm details. No price, quantity, or sale/distribution details were found anywhere (this looks like it may have been a freebie/giveaway addon rather than a sold item, but that is not confirmed, so get_one fields are left empty). No photos of the finished piece were found on the repo (no image files committed) or via search; only a repo social-preview avatar exists, which does not show the item itself, so no images were saved. The repo is on the "master" branch (not "main"). Hardware (KiCad PCB + schematic PDFs) and firmware source are both in the repo, so open_source is "partial" pending explicit confirmation of a license. A same-maker "Acrylic Sign Addons" entry exists for DC31 (dc31-acrylic-sign-addons) — likely a follow-on/sequel product line, not a duplicate of this DC30 item.'
last_modified_date: '2026-09-07'
---

The Mini Acrylic Sign Addon is an edge-lit acrylic GAT badge addon built by trueControl (true), released at DEF CON 30 and also carried to Hackaday Supercon 2022. A custom-engraved acrylic sign sits over up to six RGB LEDs arranged in pairs across two or three lighting zones, up-firing and edge-lighting the piece from below; a separate front LED handles ambient light sensing and status. Two buttons on the underside handle on-device configuration, and the addon connects to a host badge through trueControl's GAT connector (with a passing note in the README about possible future GAT2U/SAOv3 support).

Beyond badge use, the addon doubles as a USB-powered desk ornament: plugged into a computer over micro USB, its firmware emulates a Corsair iCUE Lighting Node PRO well enough to be recognized and driven by iCUE, SignalRGB, or OpenRGB, though only in "Direct" mode. The maker's README is candid that the brains behind it, an EFM8UB10F8G-QFN20, was a compromise pick made during the chip shortage — chosen mainly because it was one of the only low-power, USB-capable, in-circuit-debuggable parts available for under a dollar at the time, despite an awkward peripheral/crossbar setup.

Hardware and firmware are both published in trueControl's git repository: the PCB was designed in KiCad v6, the acrylic artwork directly in LightBurn, and the firmware in C via the Keil C51 toolchain inside Silicon Labs' Simplicity Studio 5. The README also documents the USB bootloader recovery procedure (hold the button nearest the USB port while plugging in, or short two test pads with tweezers if the original firmware is corrupted) and provides `efm8load`-based flashing instructions. No price, production quantity, or sale channel could be confirmed — it does not appear in the trueControl shop's DC30 category — so it may have been given away rather than sold, but that is unconfirmed.

## Make your own

Hardware (KiCad PCB and schematics) and firmware (Keil C51 project for the EFM8UB10) are both in the repo at https://git.trueserve.org/trueControl/dc30-acrylic-mini-sign-addon (branch `master`). Building the firmware requires Simplicity Studio 5 (8051 resources) and a free Keil C51 license obtained through SSv5's licensing flow; the finished `.hex` is converted to `.efm8` with the included `hex2boot.exe` and pushed to the device with `efm8load` over USB in bootloader mode.
