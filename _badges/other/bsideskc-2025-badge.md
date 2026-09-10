---
title: BSidesKC 2025 badge
id: other-bsideskc-2025-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2025
makers:
- name: BadgePirates
  url: https://badgepirates.com
summary: The official electronic badge BadgePirates made for BSidesKC 2025, part of the crew's long-running annual BSidesKC badge line.
functions: Ships with a physics-based Lunar Lander game, BLE-based social/proximity features with unlockable achievements, a screensaver with nine scenes, twelve NeoPixel light patterns, a conference schedule viewer, Wi-Fi management, and OTA firmware updates.
look:
  colors: []
  shape: null
  themes:
  - space
  - video game
  - hardware tool
tech:
  mcu: ESP32-S3
  leds:
    count: 6
    type: WS2812B
    note: Six WS2812B NeoPixels plus a separate status LED.
  display: 320x240 SPI TFT with capacitive touch
  connectivity:
  - wifi
  - ble
  battery: LiPo with fuel gauge
  sao_version: v2
  inputs:
  - touch
  - capacitive
  - rotary encoder
  - buttons
get_one:
  price: $100.00
  price_usd: 100
  quantity: ''
  availability: limited
  distribution:
  - purchase
  where: Sold/distributed by BadgePirates for BSidesKC 2025; badges were held up in U.S. Customs after production, with local pickup at SecKC or BSidesDSM, or mail shipping offered once cleared.
make_your_own:
  open_source: true
  hardware_url: https://github.com/BadgePiratesLLC
  firmware_url: https://github.com/BadgePiratesLLC
  eda_tool: null
links:
- label: blog.badgepirates.com/BSidesKC-Badge-Shipping-Update
  url: https://blog.badgepirates.com/BSidesKC-Badge-Shipping-Update/
  kind: website
  archived: https://web.archive.org/web/20250917022414/https://blog.badgepirates.com/BSidesKC-Badge-Shipping-Update/
- label: badgepirates.com (portfolio)
  url: https://badgepirates.com
  kind: website
- label: www.tindie.com/products/badgepirates/bsidekc25-26-electronic-badge
  url: https://www.tindie.com/products/badgepirates/bsidekc25-26-electronic-badge/
  kind: store
- label: github.com/BadgePiratesLLC
  url: https://github.com/BadgePiratesLLC
  kind: repo
images:
- file: assets/images/badges/other/bsideskc-2025-badge/d9e613be3b.jpg
  source: https://badgepirates.com
  credit: BadgePirates
  caption: BSidesKC 2025 badge
- file: assets/images/badges/other/bsideskc-2025-badge/dce4bb1773.jpg
  source: https://www.tindie.com/products/badgepirates/bsidekc25-26-electronic-badge/
  credit: BadgePirates
  caption: BSideKC25/26 Electronic Badge, ESP32-S3 touchscreen badge with Lunar Lander game
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- Sweep's summary line ("ESP32-S3 touchscreen badge (320x240 capacitive display, 6 NeoPixels, rotary encoder, BLE 5.0, LiPo+fuel gauge) shipped at BSidesKC 2025/26, also reused at CactusCon 13/14") is confirmed by the Tindie listing itself; carried over as-is. Title matches the maker's own Tindie listing title ("BSideKC25 / 26 Electronic Badge") apart from spacing.
- This may be the same physical badge as the separately catalogued "other-bsideskc-2025-badge" entry (BadgePirates, BSidesKC 2025, color LCD, SAO-style header, per that entry's recovered photo) — the "25/26" naming suggests one badge design carried across a customs-delayed 2025 ship date into 2026. Not merged here since neither entry's sources state this explicitly; flagged as a possible duplicate.
- No dedicated GitHub repo specific to this badge (e.g. a "BSidesKC_2025" or "_2026" folder) was found in the BadgePiratesLLC org as of this check; linked the org root instead, which the Tindie listing itself points to for "all design files."
status: released
sources:
- kind: url
  url: https://blog.badgepirates.com/BSidesKC-Badge-Shipping-Update/
  title: BSidesKC 2025 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''bsideskc (2025)''.'
  archived: https://web.archive.org/web/20250917022414/https://blog.badgepirates.com/BSidesKC-Badge-Shipping-Update/
- kind: url
  url: https://blog.badgepirates.com/BSidesKC-Badge-Shipping-Update/
  title: BSidesKC Badge Shipping Update
  accessed: '2026-09-07'
  note: Confirms maker (BadgePirates) and that badges were held up at U.S. Customs; describes distribution as local pickup at SecKC/BSidesDSM or mail shipping once cleared. No technical specs, price, or quantity given.
  archived: https://web.archive.org/web/20250917022414/https://blog.badgepirates.com/BSidesKC-Badge-Shipping-Update/
- kind: url
  url: https://badgepirates.com
  title: Badge Pirates portfolio site
  accessed: '2026-09-07'
  note: Confirms the badge exists in BadgePirates' portfolio gallery ("BSides KC 2025"), tagged under their BSides category, with a photo (BSideKC25.jpg) but no written specs. No dedicated GitHub repo for the 2025 badge was found (their public repo list runs BSidesKC_2018 through BsidesKC_2024, plus DefCon_SecKC_25/26/27; nothing for 2025 KC).
- kind: url
  url: https://www.tindie.com/products/badgepirates/bsidekc25-26-electronic-badge/
  title: BSideKC25 / 26 Electronic Badge from BadgePirates on Tindie
  accessed: '2026-09-10'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-kansas-city); event read as ''BSidesKC 2026''.'
- kind: url
  url: https://www.tindie.com/products/badgepirates/bsidekc25-26-electronic-badge/
  title: BSideKC25 / 26 Electronic Badge from BadgePirates on Tindie
  accessed: '2026-09-10'
  note: Maker's own storefront listing; confirms maker (BadgePirates), MCU (ESP32-S3), display (320x240 SPI TFT capacitive touch), 6x WS2812B NeoPixels + status LED, rotary encoder + two buttons, SAO header, microSD slot, piezo buzzer, USB-C, LiPo w/ fuel gauge, price ($100), "a small batch left" availability, out-of-box functions (Lunar Lander game, BLE social features, screensaver, NeoPixel patterns, schedule viewer, Wi-Fi mgmt, OTA), event use at BSidesKC 2025/26 and CactusCon 13/14, and that design files are public on GitHub at github.com/BadgePiratesLLC.
- kind: url
  url: https://github.com/orgs/BadgePiratesLLC/repositories
  title: BadgePiratesLLC GitHub organization repositories
  accessed: '2026-09-10'
  note: Checked for a badge-specific repo; org has per-year BSidesKC repos through 2024 (BSidesKC_2018 ... BsidesKC_2024) and various SAO/DefCon/CactusCon repos, but none named for a 2025 or 2026 BSidesKC badge specifically.
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): both cited sources were re-fetched and support every non-empty field and sentence in this entry — the shipping-update blog post confirms the maker, the BSidesKC 2025 customs delay, and the SecKC/BSidesDSM pickup or mail-shipping options; the portfolio site confirms the badge''s existence, its photo, and the run of BSidesKC badges from 2018-2025. The saved image byte-matches badgepirates.com''s own BSideKC25.jpg. A GitHub search independently confirmed the org (BadgePiratesLLC) has repos for BSidesKC 2018-2024 but none for 2025, and ''bsideskc'' does not appear in _data/events.yml, so ''other'' stays correct. Confidence remains low only because the two sources genuinely say nothing about functions, MCU, LEDs, display, price, or quantity — not because anything here is in doubt. Note for a future pass: the recovered photo itself shows a color LCD (rendering a "Kansas City BSIDES 2025" badge logo), a 6-pin header resembling an SAO port, and a lit green
    LED, none of which are described in text by either source, so tech fields were left blank per the no-invention rule rather than inferred from the image. Merged with duplicate entry ''BSideKC25/26 Electronic Badge'' (bsides-kansas-city-2026-bsidekc25-26-electronic-badge).'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/bsides-kansas-city-2026/bsidekc25-26-electronic-badge/
---

BadgePirates, the Kansas City-based badge-making crew, produced this electronic badge for BSidesKC 2025, continuing a badge series they have run for the conference since at least 2018. As of the only detailed source found — a shipping-update post on the BadgePirates blog — the finished badges were held up in U.S. Customs after manufacturing, delaying distribution to purchasers. BadgePirates offered buyers local pickup at SecKC or at BSidesDSM, or mailed shipping, once the badges cleared customs.

No source found describes the badge's on-board electronics, artwork, price, or production quantity. A single photo of the badge was recovered from BadgePirates' own portfolio site, where it appears alongside the crew's other annual BSidesKC badges (2018 through 2024) and their DEF CON/SecKC badges. Unlike several of their other badge years, no dedicated GitHub repository for the BSidesKC 2025 badge could be found in BadgePirates' public GitHub organization as of this research pass.

## Notes merged from the duplicate entry "BSideKC25/26 Electronic Badge"

BadgePirates, the Kansas City-based badge crew behind BSidesKC's badge line since at least 2018, built the BSideKC25/26 Electronic Badge around an ESP32-S3: a 320x240 SPI touchscreen, six WS2812B NeoPixels plus a status LED, a rotary encoder with two side buttons, a microSD slot, a piezo buzzer, USB-C charging into a LiPo cell with a fuel gauge, and an SAO expansion header. Out of the box it runs a physics-based Lunar Lander game, BLE-based proximity/social features with unlockable achievements, a nine-scene screensaver, twelve NeoPixel light patterns, a conference schedule viewer, Wi-Fi management, and OTA firmware updates.

The "25/26" name and the listing's own note that it shipped across both the BSidesKC 2025 and 2026 seasons (and was also reused at CactusCon 13 and 14) suggest a single hardware run stretched across events rather than two distinct badge years. BadgePirates sold it directly through their Tindie storefront for $100, with the listing showing only "a small batch left" at last check. All hardware and firmware design files are published on the crew's GitHub organization, though no folder specific to this particular badge (as exists for their 2018-2024 BSidesKC badges) was found there.

A separate archive entry, "BSidesKC 2025 badge" (BadgePirates), describes a customs-delayed BSidesKC 2025 badge with a color LCD and what its recovered photo shows as an SAO-style header — a description consistent with this same product. The two entries have not been merged because neither entry's own sources state outright that they are the same physical badge.
