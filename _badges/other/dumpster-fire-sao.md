---
title: Dumpster Fire SAO
id: other-dumpster-fire-sao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 0
makers:
- name: Untitled Electronics
  url: https://untitledelec.com/
summary: 'A "shitty add-on" (SAO) from Untitled Electronics that depicts a small dumpster on fire, complete with a power switch and a few LEDs for flame effect.'
functions: 'Switch-activated LED "flame" lighting inside a small dumpster enclosure; a joke reference to the "dumpster fire" internet meme applied to a software project''s status.'
look:
  colors:
  - black
  shape: null
  themes:
  - meme
tech:
  mcu: null
  leds:
    count: 3
    type: null
    note: 'Untitled Electronics'' own store page and reviews describe three LEDs used for a flame effect.'
  display: null
  connectivity: []
  battery: null
  sao_version: v1.69bis
get_one:
  price: "$15-$20"
  price_usd: 15
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: 'Sold via the maker''s Tindie store (untitledelec) and later listed on their own Shopify store (untitledelec.com); a preorder listing also appeared on the Badgepirates store. As of research date, the Tindie listing shows the seller "taking a break" and the Badgepirates listing shows sold out.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/untitledelec/dumpster-fire-sao
  url: https://www.tindie.com/products/untitledelec/dumpster-fire-sao/
  kind: store
- label: untitledelec.com
  url: https://untitledelec.com/
  kind: website
- label: store.badgepirates.com - Dumpster Fire SAO preorder
  url: https://store.badgepirates.com/product/preorder-dumpster-fire-sao/
  kind: store
images:
- file: assets/images/badges/other/dumpster-fire-sao/4aa8b8f974.jpg
  source: "https://www.tindie.com/products/untitledelec/dumpster-fire-sao/"
  credit: "Untitled Electronics"
  caption: "Dumpster Fire SAO, front view"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
- 'The product photo file on Tindie carries a 2019-08-27 upload timestamp (weak circumstantial evidence, not a maker statement), but the maker''s own copy does not tie the SAO to a specific convention or year, and it appears to have been sold as a general/ongoing store item across multiple events rather than a one-con release. Left `event` as `other` and `year` as `0` rather than guess.'
- 'Do not confuse this with the unrelated "DC27 Dumpster Fire SAO (fully assembled)" sold by a different maker, Harbinger LTD / awkwardai, which is a different PCB design explicitly made for DEF CON 27 (reported separately below).'
status: listed
sources:
- kind: url
  url: https://www.tindie.com/products/untitledelec/dumpster-fire-sao/
  title: Dumpster Fire SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''unknown''.'
- kind: url
  url: https://untitledelec.com/
  title: Untitled Electronics
  accessed: '2026-09-07'
  note: 'Maker''s own storefront; confirms product listed at $20 with no additional spec details beyond the Tindie page.'
- kind: url
  url: https://store.badgepirates.com/product/preorder-dumpster-fire-sao/
  title: Dumpster Fire SAO – Badgepirates
  accessed: '2026-09-07'
  note: 'Third-party preorder listing at $20, shown sold out; no additional technical detail.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Core identity (maker, SAO spec compliance, switch + LED flame gimmick, price range) is confirmed by the maker''s own Tindie and Shopify pages. Could not confirm: exact MCU/driver (if any active electronics beyond LEDs and a switch — it may be a passive LED circuit with no MCU), exact LED type, PCB color/finish, quantity made, or a specific event/year of debut. No hardware or firmware files were found, so make_your_own fields are left empty rather than guessed.'
last_modified_date: '2026-09-07'
---

The Dumpster Fire SAO is a small, humorous "shitty add-on" made by Untitled Electronics (West Des Moines, Iowa), designed to plug into a badge's SAO header per the 1.69bis specification. It renders the "dumpster fire" internet meme as a physical object: a tiny dumpster with LEDs standing in for flames, switched on and off with an onboard power switch the maker added specifically so the toggle wouldn't be forgotten (a running joke in their other listings). The maker describes it as a way to depict "the status of your favorite software project."

The SAO was sold through the maker's own Tindie storefront and later through their Shopify site (untitledelec.com), with a preorder also appearing on the third-party Badgepirates store; prices seen ranged from $15 to $20. As of this research pass the Tindie listing shows the seller on a sales break and the Badgepirates listing is marked sold out, so current availability is unclear. Reviewers who bought it described it as fitting in well "at work and at conventions," suggesting general convention circulation rather than a single-event release.

This item should not be confused with the "DC27 Dumpster Fire SAO (fully assembled)," a different, unrelated PCB design sold by Harbinger LTD (Tindie seller awkwardai) that was made specifically for DEF CON 27 (2019) and uses a hot-glue-channeling technique for its flame effect — see `other_items_found` in this run's report for that separate item.
