---
title: RVAsec 2025 Badge
id: rvasec-2025-rvasec-2025-badge
layout: badge
parent: RVAsec 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: rvasec-2025
year: 2025
makers:
- name: HackRVA
  url: https://www.hackrva.org/badge/
summary: The custom electronic badge HackRVA builds by hand each year for RVAsec attendees, guaranteed to registrants who buy the hotel/conference package.
functions: ''
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
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
  distribution:
  - purchase
  where: Given to RVAsec attendees who registered with the conference/hotel package that includes the "Custom Hack.RVA electronic badge."
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: badge2025.hackrva.org
  url: https://badge2025.hackrva.org/
  kind: website
- label: hack.RVA — Badge
  url: https://www.hackrva.org/badge/
  kind: website
- label: HackRVA Badge Wiki — History
  url: https://badge2025.hackrva.org/pages/history/
  kind: doc
- label: badge2024 firmware repo (HackRVA)
  url: https://github.com/hackrva/badge2024/
  kind: repo
images: []
contact: {}
notes:
- HackRVA electronic badge for RVAsec 2025 with its own badge-wiki microsite. Found by the event-year sweep, task con-rvasec.
- 'Could not confirm a badge distinct to RVAsec 2025 (RVAsec 14, June 3-4 2025): the badge2025.hackrva.org wiki''s "About" page links only to the 2024 firmware repo (github.com/hackrva/badge2024) and a 2023 build video, and its History gallery''s newest entry is labeled "2024 — Last year''s badge" with no 2025 entry. HackRVA''s GitHub org has repos badge2024 and badge2026 but no badge2025, suggesting the 2024 design may have been reused for the 2025 con rather than a new badge being built, or that the 2025 badge simply was not documented on the wiki. RVAsec''s own conference/registration pages confirm a "Custom Hack.RVA electronic badge" was part of the RVAsec 14 (2025) package, so the badge itself is real, but no source describes its specific chip, LEDs, display, or price for 2025 in particular, so those fields are left empty rather than assumed from the 2024 design. Per HackRVA''s history page, badges from 2022 onward (fabricated overseas, not hand-etched) run on a Raspberry Pi Pico / RP2040, and the 2024 badge (per its repo) is also RP2040-based, but this is not stated as the 2025 badge''s spec specifically.'
status: released
sources:
- kind: url
  url: https://badge2025.hackrva.org/
  title: RVAsec 2025 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-rvasec); event read as ''RVAsec 2025''.'
- kind: url
  url: https://badge2025.hackrva.org/pages/history/
  title: history • HackRVA Badge Wiki
  accessed: '2026-09-08'
  note: History gallery of RVAsec badges by year; newest entry is 2024, no 2025 entry, confirming no distinct 2025 badge is documented here.
- kind: url
  url: https://www.hackrva.org/badge/
  title: Badge - hack.RVA
  accessed: '2026-09-08'
  note: General description of HackRVA's yearly RVAsec badge-building process; no 2025-specific details.
- kind: url
  url: https://rvasec.com/rvasec-14-hotel-package/
  title: RVAsec 14 - Hotel Package - RVAsec
  accessed: '2026-09-08'
  note: RVAsec 14 (June 3-4, 2025) hotel package page confirms "Custom Hack.RVA Electronic badge (the ONLY way to guarantee one of the limited electronic badges)" was included. (The bare rvasec.com homepage, cited originally, now shows the current RVAsec 15/2026 package instead and no longer supports this claim — replaced with the stable dated page.)
- kind: url
  url: https://github.com/hackrva/badge2024/
  title: HackRVA badge2024 firmware repo
  accessed: '2026-09-08'
  note: Firmware repo linked from the badge wiki's About page; confirms the 2024 badge is Raspberry Pi Pico (RP2040) based, built with the Pico SDK. No corresponding badge2025 repo exists in the HackRVA GitHub org.
research:
  status: verified
  confidence: low
  last_checked: '2026-09-08'
  notes: 'Fact-check pass (2026-09-08): re-fetched all four cited sources directly. badge2025.hackrva.org''s About page does link only to the badge2024 repo and a 2023 YouTube video; its History gallery''s labeled entries run 2013-2024 with 2022 explicitly labeled as the year the badge moved from PIC32 to RP2040 and from hand-etched to overseas-fabricated PCBs, and no 2025 entry. The HackRVA GitHub org (confirmed via API) has badge2022/2023/2024/2026 but no badge2025. badge2024''s repo does confirm RP2040/Pico SDK. One citation was corrected: the entry cited the bare rvasec.com homepage for the "Custom Hack.RVA electronic badge" being part of the RVAsec 14 (2025) hotel package, but that homepage is a live/current page that now advertises the 2026 conference instead; swapped in the stable dated page https://rvasec.com/rvasec-14-hotel-package/, which does state this for 2025. Status changed from "listed" to "released": the June 2025 event has already taken place and the badge was distributed to attendees per RVAsec''s own hotel-package page, so this is a confirmed past distribution, not a not-yet-released listing. Real item (HackRVA builds an electronic badge for RVAsec every year), but no source documents 2025-specific design details; tech/get_one specifics/look fields remain empty rather than copied from 2024. Type, colors, functions, price, quantity, MCU, LEDs, and display are unconfirmed for this specific year.'
last_modified_date: '2026-09-08'
---

HackRVA, the Richmond, Virginia makerspace, has hand-designed and built the badges given to RVAsec conference attendees for well over a decade, and RVAsec's own event pages confirm that a "Custom Hack.RVA electronic badge" was again part of the RVAsec 14 (June 3-4, 2025) conference/hotel package. Whether this was a newly designed badge for 2025 or a continuation of the 2024 design could not be confirmed: HackRVA's badge wiki (hosted at badge2025.hackrva.org) links only to the 2024 firmware repository and a 2023 build video, and its year-by-year history gallery stops at 2024 with no 2025 entry. The HackRVA GitHub organization holds separate `badge2024` and `badge2026` repositories but no `badge2025`, which suggests the 2025 con may have reused the 2024 hardware and firmware rather than getting an all-new design, though this archive has not seen a source that states that directly.

Recent HackRVA badges (2022 onward, per the wiki's history page) moved from hand-etched copper to overseas-fabricated PCBs and switched from PIC32 to the Raspberry Pi Pico (RP2040), which the 2024 firmware repo confirms for that year's badge. Past badges in the series have featured onboard games, CTF challenges hidden in silkscreen art, "badge monster" collectibles, and sensor add-ons (accelerometer, environmental sensors) depending on the year's theme, but none of this is confirmed specifically for 2025. This entry is left sparse rather than guessed; a future pass that finds a dedicated RVAsec 2025 badge page, repo, or photo should update it directly.
