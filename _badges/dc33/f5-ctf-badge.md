---
title: F5 CTF Badge
id: dc33-f5-ctf-badge
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: Abhinav SP - Hackerware.io
summary: F5's first badge, a CTF badge built by Hackerwares (Abhinav SP) and given away at F5's booth at Black Hat 2025; solving web challenges yields binary flags that unlock LED sections on the badge.
functions: Flip a slide switch for a 3-second LED preview. Hold the CTF key and enter a binary flag (via 1/0 switches) to unlock that challenge's LEDs; hold the MODE key to change the LED blink pattern; hold 1 and 0 together to reset progress. Visiting F5 partner booths at Black Hat progressively unlocks badge sections.
look:
  colors:
  - black
  - pink
  - blue
  - purple
  - green
  - orange
  shape: null
  themes:
  - ctf
  - security
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: Giveaway at Black Hat
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given away by F5 at Black Hat 2025; unlocked further by visiting F5 partner booths.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: Hackerware.io/f5
  url: https://Hackerware.io/f5
  kind: website
- label: F5 Badge CTF
  url: https://www.hackerware.io/f5-ctf
  kind: website
images:
- file: assets/images/badges/dc33/f5-ctf-badge/9ff83703e4.jpg
  source: https://hackerware.io/f5
  credit: Hackerwares (Abhinav SP)
  caption: The F5 CTF badge as shown on the maker's site
contact: {}
notes:
- Visit F5 booth at Blackhat.
- 'F5''s debut badgelife entry: a blinky badge with badge-tagging, hidden keys, and a built-in CTF, produced by Hackerware.io. Found by the event-year sweep, task dc34-saos.'
- The maker's page (hackerware.io/f5) says this badge was made for Black Hat 2025, not DEF CON 34; it is a duplicate of the already-researched entry dc33-f5-ctf-badge (same maker page, same badge). Left filed as dc34 per instructions since no matching event id exists for Black Hat in events.yml; the real event/year is Black Hat 2025.
status: released
sources:
- kind: sheet
  event: dc33
  row: 67
  updated: 8/4/2025
- kind: url
  url: https://hackerware.io/f5
  title: Welcome To Hackerware — The F5 CTF Badge
  accessed: '2026-09-06'
  note: Maker's own page describing the badge's gameplay (slide switch preview, binary flag entry via CTF/MODE/1/0 keys, booth-unlock mechanic) and the badge photo (f5.JPG).
- kind: url
  url: https://www.hackerware.io/f5-ctf
  title: F5 Badge CTF
  accessed: '2026-09-06'
  note: The CTF puzzle page itself (four challenges — Delivery, Security, XOps, Deployment); no hardware specs.
- kind: url
  url: https://hackerware.io/index.html
  title: 'Hackerware - #BadgeLife | Hardware Design, Security, & Research.'
  accessed: '2026-09-06'
  note: Site root lists the F5 badge in the Hackerware portfolio ("A CTF badge built around F5's platform offerings") and gives an abhinav@ contact address, consistent with the sheet's "Abhinav SP - Hackerware.io".
  archived: https://web.archive.org/web/20260210085905/https://www.hackerware.io/index.html
research:
  status: verified
  confidence: high
  last_checked: '2026-09-06'
  notes: Fact-checked 2026-09-06 against the maker's pages and the sheet row. "Giveaway at Black Hat" and "Visit F5 booth" come from the maker's own sheet submission; the maker's page confirms Black Hat 2025 partner-booth unlocks and every control described in functions. Colors are read from the maker's photo (black PCB with pink ring and purple/blue/green/orange lobes). Not a DEF CON floor drop; kept under dc33 as imported from the sheet. No source gives the MCU, LED count/type, battery, quantity, or any hardware/firmware release; no Hackaday, press, or storefront coverage was found for this badge. Merged with duplicate entry 'F5 Badge (F5 CTF Badge)' (dc34-f5-badge-f5-ctf-badge).
last_modified_date: '2026-09-08'
redirect_from:
- /badges/dc34/f5-badge-f5-ctf-badge/
---

The F5 CTF Badge was F5's debut into badgelife, built for the company by Abhinav SP of Hackerwares and given away at F5's booth during Black Hat 2025. The badge doubles as a lightweight puzzle console: a slide switch triggers a 3-second sneak preview of the LEDs, while the real game runs through four challenges ("Delivery," "Security," "XOps," and "Deployment") hosted on a companion CTF page. Solving a challenge yields a binary flag, which the holder enters on the badge using the 1 and 0 keys while holding the CTF key; a correct flag unlocks that challenge's LEDs. A separate MODE key changes the LED blink pattern, and holding 1 and 0 together for a few seconds resets CTF progress.

Beyond the puzzle mechanic, the badge was tied to Black Hat's expo floor: visiting F5's partner booths progressively unlocked additional sections of the badge. No technical specifications (microcontroller, LED type or count, power source) were published on the maker's site, and no repository, schematic, or bill of materials was found, so the badge's open-source status and internals remain undocumented.

## Notes merged from the duplicate entry "F5 Badge (F5 CTF Badge)"

This entry is a duplicate of [dc33-f5-ctf-badge](../dc33/f5-ctf-badge.md): both point to the same maker page, hackerware.io/f5, describing the F5 CTF Badge built by Abhinav SP of Hackerware.io and given away at F5's booth during Black Hat 2025. The badge is a blinky puzzle console — a slide switch gives a 3-second LED preview, and solving CTF challenges yields binary flags entered via 1/0 switches to progressively unlock LED sections, with a MODE key to change blink patterns and a 1+0 combo to reset progress.

The discovery sweep filed this copy under DC34, but nothing on the maker's page ties the badge to DEF CON 34; it was made for Black Hat 2025. No event id for Black Hat exists in this archive's `_data/events.yml`, so the event field is left as `dc34` rather than guessed, per the task's instructions — see `dc33-f5-ctf-badge.md` for the fully researched record of this badge, including its image and full source list.
