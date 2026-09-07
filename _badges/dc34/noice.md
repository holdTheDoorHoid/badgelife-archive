---
title: '#NoIce'
id: dc34-noice
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: RivaClan
summary: A memorial and activism SAO made for DEF CON 34, honoring people killed by ICE/DHS enforcement in 2025-26; a portion of proceeds goes to the Immigrant Defenders Law Center.
functions: Cycles through LED animations (fast and slow flashing, a heartbeat pattern, and a breathing/fade effect) with a single tactile button, and remembers the last effect used if power is lost.
look:
  colors:
  - red
  shape: null
  themes:
  - privacy
  - security
tech:
  mcu: null
  leds:
    count: 16
    type: side-emitting
    note: XL-1606SURC red side-emitting LEDs, mounted to shine through the FR4 PCB
  display: none
  connectivity: []
  battery: powered by host badge (2.7V-3.7V input; DC34 badge outputs 3V)
  sao_version: null
get_one:
  price: $20
  price_usd: 20.0
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold via ko-fi.com/caelybr (page was behind a Cloudflare bot-check on 2026-09-06, so current listing status could not be confirmed)
  availability_note: Uberflux listing showed 9 sold, 0 remaining as of 2026-09-07.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/keeloi79/no-ice-sao
  firmware_url: null
  eda_tool: null
  license: GPL-3.0
links:
- label: ko-fi.com/caelybr
  url: https://ko-fi.com/caelybr
  kind: store
- label: github.com/keeloi79/no-ice-sao
  url: https://github.com/keeloi79/no-ice-sao
  kind: repo
- label: cdn.discordapp.com/attachments/342354987726405642/1522091617035485324/signal-2026-07-02-000502.mov?ex=6a4bd308&is=6a4a8188&hm=89434cb03f45528459f62902220b53dbfc9383c5a416b36cc5fb3a0194ada194&
  url: https://cdn.discordapp.com/attachments/342354987726405642/1522091617035485324/signal-2026-07-02-000502.mov?ex=6a4bd308&is=6a4a8188&hm=89434cb03f45528459f62902220b53dbfc9383c5a416b36cc5fb3a0194ada194&
  kind: video
- label: uberflux.com/product/DC34-noice
  url: https://uberflux.com/product/DC34-noice
  kind: store
images:
- file: assets/images/badges/dc34/noice/02b982cedf.jpg
  source: https://uberflux.com/product/DC34-noice
  credit: Uberflux / caelyb
  caption: 'The #NOICE SAO, front view showing red LED array'
- file: assets/images/badges/dc34/noice/8247887233.jpg
  source: https://uberflux.com/product/DC34-noice
  credit: Uberflux / caelyb
  caption: 'The #NOICE SAO, alternate view'
contact:
  discord: Caelyb
  emails:
  - caelyb@caelyb.com
  handles:
  - '@caelybr'
  raw:
  - 'Insta:'
notes:
- 'Uberflux. $20, status: sold out.'
- This appears to be the same item as dc34-noice (#NoIce by RivaClan/caelyb), sold through two storefronts (Uberflux here, ko-fi.com/caelybr on the other entry) with matching specs (16x XL-1606SURC red LEDs, single-button effect cycling, persistent memory, 2.7-3.7V input, $20, DC34, ICE/DHS memorial theme). See duplicate_of in the research report.
status: listed
sources:
- kind: sheet
  event: dc34
  row: 31
  updated: 7/5/2026 17:22:50
  listing: New
- kind: url
  url: https://github.com/keeloi79/no-ice-sao
  title: keeloi79/no-ice-sao - GitHub
  accessed: '2026-09-06'
  note: README describes the SAO's purpose, LED hardware (16x XL-1606SURC side-emitting red LEDs), power range, button control, animation modes, and GPL-3.0 license.
- kind: url
  url: https://uberflux.com/product/DC34-noice
  title: '#NOICE SAO'
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: uberflux-shops); event read as ''DEF CON 34''.'
- kind: url
  url: https://uberflux.com/product/DC34-noice
  title: '#NOICE SAO'
  accessed: '2026-09-07'
  note: Confirmed product description, LED count/type, button/effect features, price ($20), sold-out status (9 sold, 0 remaining), shipping terms, and package contents (unit + lanyard). Fetched two product photos.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Core description, LED hardware, and license confirmed from the maker's GitHub README. Could not confirm MCU, SAO header version, PCB color, quantity made, or current availability/price because ko-fi.com/caelybr returned a Cloudflare bot-check page that could not be bypassed. The linked Discord video (a .mov attachment with a signed, expiring URL) was not reviewed. No usable photos of the physical item were found; the only image on the GitHub page is a generic auto-generated social-card graphic, not a photo of the board, so no images were saved. Merged with duplicate entry '#NOICE SAO' (dc34-noice-sao).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc34/noice-sao/
---

#NoIce is a Simple Add-On made for DEF CON 34 as a memorial and activism piece. The
README describes it as a way "to remind everyone the fatal injustices of DHS and ICE
enforcement in 2025-26," naming several people who died in ICE custody or in raids,
and states that a portion of proceeds goes to the Immigrant Defenders Law Center to
help fund legal defense for immigrant families.

The board uses 16 side-emitting XL-1606SURC red LEDs mounted so their light shines
through the FR4 PCB itself, controlled with a single tactile button that cycles
through several animations: fast and slow flashing patterns, a heartbeat effect, and
a breathing/fade sequence. It accepts a wide 2.7V-3.7V input so the LEDs stay bright
even on the DC34 host badge's 3V output, and it saves the last-used effect so it
resumes correctly after a power interruption or disconnection from the host badge.

The hardware design is published on GitHub under the GPL-3.0 license by user
keeloi79, and the badge was sold for $20 through the maker's ko-fi page
(ko-fi.com/caelybr). The GitHub repository's contents beyond the README and license
file (e.g. schematics, firmware, or a bill of materials) were not accessible during
this research pass, so the microcontroller, SAO header version, and build files
could not be confirmed.

## Notes merged from the duplicate entry "#NOICE SAO"

The #NOICE SAO is a Simple Add-On made for DEF CON 34, sold through the maker's
Uberflux storefront for $20. It carries 16 red XL-1606SURC side-emitting LEDs
mounted so their light shines through the FR4 PCB, with a single tactile button
that cycles through several lighting effects -- fast and slow flashing, a heartbeat
pattern, and a breathing/fade sequence -- and persistent memory that restores the
last-used effect after power loss. It runs on host-badge power across a wide
2.7V-3.7V input range.

The listing sold out with 9 units purchased; each order included one SAO and a
lanyard with a lobster clasp, shipped after DC34 to continental US addresses only.
A portion of proceeds went to the Immigrant Defenders Law Center.

This item's specifications and description closely match another archive entry,
dc34-noice ("#NoIce" by maker RivaClan/caelyb), which describes the same LED
hardware, button behavior, price, and DEF CON 34 ICE/DHS memorial theme, but was
sold via ko-fi.com/caelybr rather than Uberflux. The two are almost certainly the
same physical SAO sold through two different storefronts by the same person.
