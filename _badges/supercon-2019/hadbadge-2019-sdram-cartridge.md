---
title: HaDBadge 2019 SDRAM Cartridge
id: supercon-2019-hadbadge-2019-sdram-cartridge
layout: badge
parent: Supercon 2019
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2019
year: 2019
makers:
- name: Jacob Creedon
  url: https://hackaday.io/jacob-creedon
summary: A 32MiB SDRAM memory-expansion cartridge for the 2019 Hackaday Supercon FPGA badge, built to enable the badge's Linux-on-Badge demo.
functions: Plugs into the Supercon 2019 badge's cartridge expansion slot to supply external SDRAM the FPGA badge can address, giving it enough memory to run Linux.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
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
  open_source: yes
  hardware_url: http://github.com/jcreedon/dram-cart
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/168591-hadbadge-2019-sdram-cartridge
  url: https://hackaday.io/project/168591-hadbadge-2019-sdram-cartridge
  kind: hackaday
- label: github.com/jcreedon/dram-cart
  url: http://github.com/jcreedon/dram-cart
  kind: repo
images:
  - file: assets/images/badges/supercon-2019/hadbadge-2019-sdram-cartridge/8781636d34.jpg
    source: "https://hackaday.io/project/168591-hadbadge-2019-sdram-cartridge"
    credit: "Jacob Creedon"
    caption: "The SDRAM cartridge board"
  - file: assets/images/badges/supercon-2019/hadbadge-2019-sdram-cartridge/7a64cfe4b9.jpg
    source: "https://hackaday.io/project/168591-hadbadge-2019-sdram-cartridge"
    credit: "Jacob Creedon"
    caption: "The cartridge plugged into the Supercon 2019 badge"
contact: {}
notes:
- Sweep found this as "A 32MiB SDRAM cartridge add-on for the 2019 Supercon FPGA badge that enabled the Linux-on-Badge demo." Confirmed by the maker's own Hackaday.io project page; title and description match, no correction needed.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/168591-hadbadge-2019-sdram-cartridge
  title: HaDBadge 2019 SDRAM Cartridge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2019); event read as ''supercon-2019''.'
- kind: url
  url: https://hackaday.io/project/168591-hadbadge-2019-sdram-cartridge
  title: HaDBadge 2019 SDRAM Cartridge (Hackaday.io project page)
  accessed: '2026-09-08'
  note: 'Maker''s own project page; confirmed creator, 32MiB SDRAM cartridge for the Supercon 2019 FPGA badge, the 16-bit-to-8-bit pin mismatch fixed with bodge wires ("it just worked"), and the open-source KiCad hardware repo link. Does NOT itself mention Linux-on-Badge or the 8-bit interface detail beyond the part width. No pricing, quantity, or distribution details given.'
- kind: url
  url: https://hackaday.io/page/6764-hackaday-supercon-badge-boots-linux-using-sdram-cartridge
  title: 'Hackaday Supercon badge boots Linux using SDRAM cartridge'
  accessed: '2026-09-08'
  note: 'Confirms this cartridge (Jacob Creedon''s 32MiB SDRAM board) supplied the memory used by the separate "Linux-on-Badge" team (Drew Fustini, Tim Ansell, Sean Cross, and others) to boot a minimalist Linux on a RISC-V soft core in the badge''s ECP5 FPGA. This is third-party Hackaday coverage, not the maker''s own words, but corroborates the purpose stated in the entry.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Maker''s own Hackaday.io page confirms the item, its creator, the 32MiB SDRAM cartridge design, and the 16-bit-to-8-bit bodge-wire fix, but gives no price, quantity made, or distribution/availability details, so those fields are left empty (as reported). The Linux-on-Badge claim in the title/summary is NOT stated on the maker''s own project page (checked directly - no mention of Linux there); it is corroborated instead by a separate Hackaday.io article about the Linux-on-Badge team, which names this cartridge as the memory source for that demo. Kept the claim on this basis but added the corroborating source. "8-bit" interface: the maker''s log describes an 8-bit SDRAM part with 8-bit-wide data pins, consistent with the entry''s wording. Status "released" is supported (maker documents building, wiring, and using the board). No additional maker photos beyond the two saved; no separate firmware repo found (passive memory board, so tech.mcu = none is correct). All checked facts held up, so research.status is set to verified.'
last_modified_date: '2026-09-08'
---

The HaDBadge 2019 SDRAM Cartridge is a memory-expansion accessory Jacob Creedon built for the 2019 Hackaday Supercon badge, an FPGA-based badge. It adds 32MiB of SDRAM over an 8-bit interface in a cartridge that plugs into the badge's expansion slot, giving the FPGA enough external memory to run the badge's "Linux-on-Badge" demo.

Creedon's project log notes that the board was originally laid out around a 16-bit SDRAM part but had to be downgraded to an 8-bit chip because of IO constraints on the badge, which left the pin mapping mismatched; he corrected it with bodge wires rather than a board respin. By his account, once the wiring was fixed the cartridge worked as intended.

## Make your own

KiCad hardware design files are published on GitHub at github.com/jcreedon/dram-cart. No separate firmware repository was found — the cartridge is a passive memory expansion read out by the badge's own FPGA gateware.
