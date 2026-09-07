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
  - green
  shape: null
  themes:
  - meme
tech:
  mcu: CH32V003
  leds:
    count: null
    type: null
    note: 'The maker''s Shopify page says the flame is driven by "the mighty CH32V003" with a firmware flicker effect, but no source states an exact LED count or part number.'
  display: null
  connectivity: []
  battery: null
  sao_version: v1.69bis
get_one:
  price: "$15-$20"
  price_usd: 15
  quantity: ''
  availability: available
  availability_note: 'Checked 2026-09-07: Tindie listing shows the seller "taking a break" (not currently orderable there), but the Shopify store (untitledelec.com) has an active "Add to cart" button, so the item is currently buyable directly from the maker.'
  distribution:
  - purchase
  where: 'Sold via the maker''s Tindie store (untitledelec) and their own Shopify store (untitledelec.com), which also offers in-person pickup at the DEF CON Badgelife Village. A preorder listing also appeared at one point on a third-party Badgepirates store page, but that domain (store.badgepirates.com) no longer resolves (DNS failure as of 2026-09-07) and its claimed price/sold-out status could not be reverified.'
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
  note: 'Maker''s own Shopify storefront; confirms $20 price and 1.69bis compliance, and additionally states the flame effect is driven by a CH32V003 MCU and that in-person pickup happens at the DEF CON Badgelife Village.'
- kind: url
  url: https://store.badgepirates.com/product/preorder-dumpster-fire-sao/
  title: Dumpster Fire SAO – Badgepirates
  accessed: '2026-09-07'
  note: 'Fact-check pass 2026-09-07: this domain no longer resolves (NXDOMAIN via curl and browser navigation, confirmed against 8.8.8.8). The URL is still indexed by search engines under this title, so the listing existed at some point, but its content (price, sold-out status) could not be reverified and is not relied on for any field.'
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check pass 2026-09-07: re-opened all three cited sources. Tindie (untitledelec) confirms: 1.69bis SAO spec, built-in switch, $15.00 price, maker in West Des Moines IA, "on a break" status, and the exact "depicts the status of your favorite software project" line. The Shopify store (untitledelec.com) confirms: $20.00 price, 1.69bis compliance, an active "Add to cart" (so currently purchasable there), and — newly found on a source already cited in the entry — that the flame effect is driven by a CH32V003 MCU with firmware-generated flicker, so tech.mcu is now filled in and the prior "may be a passive circuit with no MCU" guess is corrected. No source gives an exact LED count, so tech.leds.count/type are left null rather than the previously-stated "3," which no cited source actually supports. The product photo shows a green PCB with pink/orange flame graphics, not black, so look.colors was corrected from black to green. The Shopify page also states in-person pickup happens at the "Defcon Badgelife Village," which ties the item to DEF CON generally, but gives no specific year, so event/year are left as other/0 per the original call. The Badgepirates store domain (store.badgepirates.com) no longer resolves at all (NXDOMAIN), so its "sold out"/price claims could not be reverified and were removed from the prose; the link is kept only as a historical reference. Still unconfirmed and left empty: exact LED type/count, PCB fab/finish beyond what the photo shows, quantity made, exact debut year, and any hardware/firmware release (none found, so make_your_own stays null).'
last_modified_date: '2026-09-07'
---

The Dumpster Fire SAO is a small, humorous "shitty add-on" made by Untitled Electronics (West Des Moines, Iowa), designed to plug into a badge's SAO header per the 1.69bis specification. It renders the "dumpster fire" internet meme as a physical object: a tiny dumpster with LEDs standing in for flames, switched on and off with an onboard power switch the maker added specifically so the toggle wouldn't be forgotten (a running joke in their other listings). The maker describes it as a way to depict "the status of your favorite software project."

The SAO is sold through the maker's own Tindie storefront and their Shopify site (untitledelec.com), which also offers in-person pickup at the DEF CON Badgelife Village; prices seen are $15 on Tindie and $20 on Shopify. The Shopify listing says the flame is driven by a CH32V003 microcontroller running a firmware flicker effect, not simple static LEDs. As of this research pass the Tindie listing shows the seller on a sales break, but the Shopify store still has an active "Add to cart" button, so the item remains buyable directly from the maker. A preorder listing also appeared at one point on a third-party Badgepirates store, but that domain no longer resolves and its details could not be reverified. Reviewers who bought it described it as having "a place at both work and CONs," suggesting general convention circulation rather than a single-event release.

This item should not be confused with the "DC27 Dumpster Fire SAO (fully assembled)," a different, unrelated PCB design sold by Harbinger LTD (Tindie seller awkwardai) that was made specifically for DEF CON 27 (2019) and uses a hot-glue-channeling technique for its flame effect — see `other_items_found` in this run's report for that separate item.
