---
title: HITCON Badge 2018 (Cold Wallet Badge)
id: hitcon-2018-hitcon-cmt-2018-wallet-badge-cold-wallet-badge
layout: badge
parent: Hitcon Cmt 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hitcon-2018
year: 2018
makers:
- name: will127534 (OSSLab Geek Lab)
  url: https://github.com/will127534
summary: 'A conference badge built around a secure element, billed as "the first cold wallet badge with secure element"; combines an e-paper display, NFC, and Wi-Fi/BLE with a numeric button pad for PIN-style entry.'
functions: 'Runs as a cryptocurrency cold-wallet UI on its e-paper screen, driven by a matrix button array (0-9, A/B/C, DEL, ENTER). Also emulates NFC tags (tested against iPhone 7 and HTC Desire 820) and talks BLE to a host, with a Python example client provided. HITCON described it as tied to a secret conference activity and usable afterward as an offline Bitcoin/Ethereum wallet, though the archive has not independently verified the wallet firmware''s security.'
look:
  colors: []
  shape: null
  themes:
  - crypto
  - security
  - wearable
tech:
  mcu: MT7697
  leds:
    count: 1
    type: discrete
    note: Single user LED (USR, GPIO57) plus separate RX/TX/power indicator LEDs on the UART/power circuitry.
  display: 2.13" e-paper (Waveshare, 250x122, black/white, partial-refresh capable)
  connectivity:
  - wifi
  - ble
  - nfc
  - i2c
  - uart
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: limited
  distribution:
  - membership
  where: 'Given to Royal VIP and Premium Pass holders at HITCON CMT 2018 (Taipei, July 27-28, 2018); not sold separately.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/will127534/HITCON-Badge-2018/tree/master/Hardware
  firmware_url: https://github.com/will127534/HITCON-Badge-2018/tree/master/Software
  eda_tool: null
links:
- label: github.com/will127534/hitcon-badge-2018
  url: https://github.com/will127534/hitcon-badge-2018
  kind: repo
images: []
contact: {}
notes:
- '"First Cold Wallet Badge with Secure Element" -- blockchain wallet badge with secure element, e-paper, Wi-Fi and BLE tied to the HITCON Token/Hackdoor game. Found by the event-year sweep, task con-hitcon.'
- 'The sweep''s title used a "HITCON CMT 2018 Wallet Badge (Cold Wallet Badge)" wording; the maker''s own repo and slide deck call it simply "HITCON Badge 2018" / "HITCON Badge 2018 - The First Cold Wallet Badge with Secure Element!" -- title updated to match.'
- 'Could not confirm any tie to a "HITCON Token" or "Hackdoor" game specifically; third-party coverage (badge.gallery, citing HITCON''s own event pages and KKTIX) instead describes a "secret activity" during the conference and post-event use as an offline BTC/ETH wallet.'
status: released
sources:
- kind: url
  url: https://github.com/will127534/hitcon-badge-2018
  title: HITCON CMT 2018 Wallet Badge (Cold Wallet Badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-hitcon); event read as ''HITCON CMT 2018''.'
- kind: url
  url: https://github.com/will127534/HITCON-Badge-2018/blob/master/Hardware/README.md
  title: HITCON Badge 2018 -- Hardware README
  accessed: '2026-09-08'
  note: 'Confirms MCU (MediaTek MT7697 / LinkIt 7697), NFC controller (PN532), display (Waveshare 2.13" e-paper), secure element (Infineon SLE97), button array wiring, and LEDs.'
- kind: url
  url: https://github.com/will127534/HITCON-Badge-2018/blob/master/Software/README.md
  title: HITCON Badge 2018 -- Software README
  accessed: '2026-09-08'
  note: 'Confirms open-source Arduino-based firmware, NFC tag emulation, BLE Python example client, and secure-element upload tooling.'
- kind: url
  url: https://badge.gallery/series/hitcon
  title: 'HITCON series -- Hacker Con Badges'
  accessed: '2026-09-08'
  note: 'Third-party catalogue citing HITCON''s own event pages and KKTIX; states the badge was limited to Royal VIP and Premium Pass holders and describes Wi-Fi/BLE/e-paper/secure-element cold-wallet features.'
- kind: url
  url: https://badge.gallery/addons/hitcon-cmt-2018-wallet-badge/offline-physical-wallet-framing
  title: 'Offline physical wallet framing -- Hacker Con Badges'
  accessed: '2026-09-08'
  note: 'States HITCON described post-event use as an offline Bitcoin/Ethereum wallet; explicitly notes the claim is not independently verified for security.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core hardware/firmware facts confirmed from the maker''s own repo (high confidence). Distribution details (Royal VIP/Premium Pass only, no public sale) and the "secret activity" framing come from a third-party badge catalogue citing HITCON''s event pages and KKTIX, not fetched directly, so confidence is medium overall. Price, quantity made, and battery type are not stated anywhere found and are left empty. No photo of the physical badge (as opposed to the block-diagram graphic in the hardware README) could be located within the research budget, so no images were saved.'
last_modified_date: '2026-09-08'
---

The HITCON Badge 2018 was distributed to Royal VIP and Premium Pass holders at HITCON CMT 2018 in Taipei (July 27-28, 2018) by will127534 of OSSLab Geek Lab. Billed by its creator as "the first cold wallet badge with secure element," it pairs a MediaTek MT7697 (LinkIt 7697-based) microcontroller with an Infineon SLE97 secure element, a Waveshare 2.13" e-paper display, a PN532 NFC controller, and a resistor-ladder button matrix (digits 0-9, A/B/C, DEL, ENTER) for PIN-style input, all wired up and documented in the maker's public schematic and hardware notes.

On the software side the badge runs open Arduino-based firmware: it can emulate NFC tags for phones, speak BLE to a host (with a Python example client provided), and drive the e-paper screen through a modified GxEPD/Adafruit GFX stack, including a fast partial-refresh mode for the wallet UI. According to HITCON's own event material (as summarized by a third-party badge catalogue), holders could take part in a secret in-conference activity and, afterward, use the badge as an offline cold wallet for Bitcoin or Ethereum -- though neither that catalogue nor this entry independently verifies the security of the wallet firmware itself.

## Make your own

Both hardware (Eagle schematic/board files) and firmware (Arduino sketches, libraries, and a secure-element upload tool) are published in the maker's GitHub repository. Building firmware requires adding the project's custom Arduino board-support package (based on MediaTek's LinkIt 7697 SDK); programming the SLE97 secure element requires first flashing a translator binary to the MT7697 and then running the included Python uploader over serial.
