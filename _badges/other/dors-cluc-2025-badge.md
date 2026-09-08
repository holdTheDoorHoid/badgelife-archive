---
title: DORS/CLUC 2025 Badge
id: other-dors-cluc-2025-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2025
makers:
- name: Hyperglitch
  url: https://hyperglitch.com
  role: Igor Brkić
summary: The official electronic badge for DORS/CLUC 2025 (Zagreb, Croatia), a 9-segment alphanumeric display with a logo-shaped LED matrix and an NFC reader/writer used for an on-site treasure hunt and badge-to-badge data exchange.
functions: Shows a user-set name or custom text (up to 30 characters) on a simulated six-character 9-segment display; runs conference quests via NFC (collect nine hidden tags around the venue to light up the logo matrix); tracks badge-to-badge taps/interactions between attendees; after the con doubles as a USB desktop notifier, a clock, or a simple game device. Two buttons and a hold-to-configure mode set text and brightness/scroll speed.
look:
  colors: []
  shape: null
  themes:
  - security
  - puzzle
  - ctf
  - text
tech:
  mcu: STM32L073
  leds:
    count: null
    type: charlieplexed
    note: Charlieplexed LEDs behind a dark acrylic diffuser simulate a six-character 9-segment display (three LEDs per segment), driven by an IS31FL3731 (rated for up to 144 charlieplexed LEDs); a separate logo-shaped LED matrix lights up as treasure-hunt NFC tags are found.
  display: 9-segment display (simulated, 6 characters)
  connectivity:
  - nfc
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '100'
  availability: sold_out
  distribution:
  - free_drop
  where: Given to DORS/CLUC 2025 attendees in Zagreb, Croatia; all badges were gone/sold out on the first day of the conference.
make_your_own:
  open_source: 'yes'
  hardware_url: https://gitlab.com/hyperglitch/dc2025badge
  firmware_url: https://gitlab.com/hyperglitch/dc2025badge
  eda_tool: null
links:
- label: hackaday.com/2025/06/01/plenty-of-leds-and-useful-too-the-2025-dors-cluc-badge
  url: https://hackaday.com/2025/06/01/plenty-of-leds-and-useful-too-the-2025-dors-cluc-badge/
  kind: article
  archived: https://web.archive.org/web/20260516053921/https://hackaday.com/2025/06/01/plenty-of-leds-and-useful-too-the-2025-dors-cluc-badge/
- label: hyperglitch.com/articles/dc2025-badge
  url: https://hyperglitch.com/articles/dc2025-badge
  kind: website
  archived: https://web.archive.org/web/20251120131132/https://hyperglitch.com/articles/dc2025-badge
- label: gitlab.com/hyperglitch/dc2025badge
  url: https://gitlab.com/hyperglitch/dc2025badge
  kind: repo
  archived: https://web.archive.org/web/20251120153915/https://gitlab.com/hyperglitch/dc2025badge
- label: dorscluc.org/badge
  url: https://www.dorscluc.org/badge/
  kind: website
  archived: https://web.archive.org/web/20251120134608/https://www.dorscluc.org/badge/
images:
- file: assets/images/badges/other/dors-cluc-2025-badge/f33e7efe10.jpg
  source: https://hyperglitch.com/articles/dc2025-badge
  credit: Hyperglitch (Igor Brkić)
  caption: DORS/CLUC 2025 badge showing custom text on its 9-segment display
  archived: https://web.archive.org/web/20251120131132/https://hyperglitch.com/articles/dc2025-badge
- file: assets/images/badges/other/dors-cluc-2025-badge/52299f6137.jpg
  source: https://hyperglitch.com/articles/dc2025-badge
  credit: Hyperglitch (Igor Brkić)
  caption: Two DORS/CLUC 2025 badges tapped together to exchange NFC data
  archived: https://web.archive.org/web/20251120131132/https://hyperglitch.com/articles/dc2025-badge
contact: {}
notes:
- STM32L073 (upgraded mid-project from an STM32L053 for more memory), IS31FL3731 LED matrix/charlieplex driver, ST25R3916 NFC reader/writer, USB port used for configuration and desktop-notifier passthrough.
- DORS/CLUC is a long-running open-source/security conference in Zagreb, Croatia (this was its 30th edition); no matching event id exists yet in _data/events.yml, so event is left as "other" — a new id such as `dors-cluc-2025` should be added.
status: released
sources:
- kind: url
  url: https://hackaday.com/2025/06/01/plenty-of-leds-and-useful-too-the-2025-dors-cluc-badge/
  title: DORS/CLUC 2025 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-press); event read as ''DORS/CLUC 2025 (Croatia)''.'
  archived: https://web.archive.org/web/20260516053921/https://hackaday.com/2025/06/01/plenty-of-leds-and-useful-too-the-2025-dors-cluc-badge/
- kind: url
  url: https://hyperglitch.com/articles/dc2025-badge
  title: DORS/CLUC 2025 Badge | HYPERGLITCH
  accessed: '2026-09-07'
  note: Maker's own project writeup; primary source for functions, chip changes, quantity (100), sold-out-day-one, images, and open-source repo link.
  archived: https://web.archive.org/web/20251120131132/https://hyperglitch.com/articles/dc2025-badge
- kind: url
  url: https://www.dorscluc.org/badge/
  title: Conference badge (2025) - DORS/CLUC
  accessed: '2026-09-07'
  note: Confirms designer (Igor Brkić / Hyperglitch), feature list (9-segment display, logo LED matrix, NFC reader/writer, two buttons, USB), treasure hunt and text customization details.
  archived: https://web.archive.org/web/20251120134608/https://www.dorscluc.org/badge/
- kind: url
  url: https://gitlab.com/hyperglitch/dc2025badge
  title: DC2025badge - GitLab
  accessed: '2026-09-07'
  note: Open-source hardware/firmware repository referenced by the maker; page only exposed project metadata (22 commits) to the fetcher, not full README.
  archived: https://web.archive.org/web/20251120153915/https://gitlab.com/hyperglitch/dc2025badge
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Core facts (maker, functions, chip, NFC chip, quantity, sold-out status, open-source repo) confirmed by the maker''s own hyperglitch.com writeup and the DORS/CLUC event page, matching the Hackaday summary. Not found/left empty: price, exact LED count, battery/power detail, EDA tool used, SAO header (this is a standalone badge, no SAO port mentioned). DORS/CLUC has no event id in _data/events.yml yet; recommend adding one (e.g. dors-cluc-2025) rather than leaving this filed under "other".'
last_modified_date: '2026-09-07'
---

The DORS/CLUC 2025 badge is the official electronic badge for DORS/CLUC, a long-running open-source and information-security conference held in Zagreb, Croatia (this was its 30th edition). It was designed by Igor Brkić of Hyperglitch, a Zagreb-based hardware/software shop that has produced the conference's badge for multiple years running. The badge centers on a simulated six-character 9-segment display built from charlieplexed LEDs behind a dark acrylic diffuser for a retro look, driven by an IS31FL3731 LED driver, plus a separate logo-shaped LED matrix. An ST25R3916 NFC reader/writer and two buttons round out the input/output, all run by an STM32L073 (the design started on a smaller STM32L053 before memory constraints forced an upgrade).

During the conference the badge displayed attendees' names or custom text, and doubled as a game piece: a treasure hunt sent attendees hunting for nine hidden NFC tags around the venue to progressively light up the logo matrix, while tapping two badges together logged an interaction between their owners for a badge-to-badge competition. After the conference the same hardware works as a USB-connected desktop notifier, a clock, or a simple standalone game. About 100 badges were made and given to attendees; they were gone on the first day.

Both hardware and firmware are open source, published in the `dc2025badge` GitLab repository. This entry is currently filed under the catch-all "other" event because DORS/CLUC does not yet have its own id in the archive's event list; it should be moved once a `dors-cluc-2025` (or similar) event is added.
