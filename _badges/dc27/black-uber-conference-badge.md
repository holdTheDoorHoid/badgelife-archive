---
title: DEF CON 27 Badge — Uber (Black) Variant
id: dc27-black-uber-conference-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Joe Grand (Grand Idea Studio) / DEF CON
  url: https://grandideastudio.com/portfolio/other/defcon-27-badge/
summary: 'The black-PCB "Uber" tier of the official DEF CON 27 electronic conference badge, one of ten silkscreen/gemstone color variants issued to denote attendee type (Human, Speaker, Vendor, Press, Village, Contest, Artist, Goon, CFP Review, Uber).'
functions: 'Same electronics and badge-quest gameplay as the standard DC27 badge; attendees complete conference tasks to progress through the quest. The Uber color marks a specific staff/attendee tier rather than a different function.'
look:
  colors:
  - black
  shape: circle
  themes:
  - security
  - jewelry
tech:
  mcu: NXP KL27 (ARM Cortex-M0+)
  leds:
    type: null
    note: Driven by a Texas Instruments LP5569 LED driver, per the standard DC27 badge design.
  display: null
  connectivity:
  - none
  battery: CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '~20 (fully finished, with matching black gemstone) out of 28,600 total DC27 badges made across all variants'
  availability: unknown
  distribution: []
  where: 'Issued to a small "Uber" attendee/staff tier at DEF CON 27 (2019); unpopulated/unfinished black-variant PCBs have separately circulated on the secondary/collector market (eBay, Worthpoint appraisals).'
make_your_own:
  open_source: yes
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: 'The DC27 badge design overall is published by Grand Idea Studio under CC BY 4.0 (hardware) with portions under the Clear BSD License (firmware); see the maker''s portfolio page. No variant-specific repo link was found during this pass.'
links:
- label: www.worthpoint.com/worthopedia/def-con-27-black-unfinished-uber-4835639075
  url: https://www.worthpoint.com/worthopedia/def-con-27-black-unfinished-uber-4835639075
  kind: website
- label: 'Worthpoint: DEF CON 27 Black Conference Badge, Unpopulated PCB Only ("Uber" variant)'
  url: https://www.worthpoint.com/worthopedia/def-con-27-black-conference-badge-4926292480
  kind: website
- label: 'Grand Idea Studio: DEFCON 27 Badge'
  url: https://grandideastudio.com/portfolio/other/defcon-27-badge/
  kind: website
- label: "DEF CON forum: The story behind DEFCON's hackable crystal electronic badge"
  url: https://forum.defcon.org/node/229722
  kind: article
images:
- file: assets/images/badges/dc27/black-uber-conference-badge/336075b7a8.jpg
  source: "https://grandideastudio.com/portfolio/other/defcon-27-badge/"
  credit: "Grand Idea Studio"
  caption: "The ten DEF CON 27 badge color/tier variants, including the black Uber variant (second row, right)"
contact: {}
notes:
- Rare black-PCB 'Uber' variant of the official DC27 conference badge with a matching gemstone, only ~20 made versus 26,500+ standard 'Human' badges. Found by the event-year sweep, task dc27-badges.
- 'The community sheet titled this "Black/Uber Conference Badge"; renamed here to "DEF CON 27 Badge — Uber (Black) Variant" to make clear it is a color/tier variant of the standard DC27 badge, not a separate hardware design.'
- 'This is very likely the same underlying badge already catalogued as dc27-badge-2019 (DEF CON 27 Badge (2019), Grand Idea Studio) — the Uber variant is one of ten silkscreen/gemstone colors issued on identical hardware, not a distinct product. Flagging as a probable duplicate rather than merging, per instructions.'
status: listed
sources:
- kind: url
  url: https://www.worthpoint.com/worthopedia/def-con-27-black-unfinished-uber-4835639075
  title: DEF CON 27 Black/Uber Conference Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc27-badges); event read as ''dc27''.'
- kind: url
  url: https://www.worthpoint.com/worthopedia/def-con-27-black-conference-badge-4926292480
  title: 'DEF CON 27 Black Conference Badge, Unpopulated PCB Only "Uber" variant'
  accessed: '2026-09-08'
  note: 'Search-snippet only (page blocked by bot-protection/captcha); confirms only ~20 black/Uber badges were fully produced with matching gemstone vs 26,500+ white Human badges, and that unpopulated PCBs of this variant circulate separately among collectors.'
- kind: url
  url: https://grandideastudio.com/portfolio/other/defcon-27-badge/
  title: 'Grand Idea Studio: DEFCON 27 Badge'
  accessed: '2026-09-08'
  note: 'Maker''s own portfolio page for the DC27 badge overall: MCU (NXP KL27), NFMI wireless chip, LP5569 LED driver, CR2032 battery, handcrafted quartz gemstone, 28,600 units across ten attendee-type color variants (including Uber), open-source hardware/firmware, and the three images used above.'
- kind: url
  url: https://forum.defcon.org/node/229722
  title: "The story behind DEFCON's hackable crystal electronic badge"
  accessed: '2026-09-08'
  note: 'DEF CON forum writeup on the DC27 badge design and background; confirms Joe Grand (Kingpin) as designer, returning after DC14-18.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'The worthpoint.com listing pages themselves are blocked by PerimeterX bot-protection (captcha wall) and could not be fetched directly; facts here come from search-result snippets of those pages plus the maker''s own portfolio page, which independently confirms the badge design, the ten color/tier variants (Human, Speaker, Vendor, Press, Village, Contest, Artist, Goon, CFP Review, Uber), and shows the black PCB variant in a group photo. No variant-specific price, exact production date, or dedicated Uber-badge repo/gerbers were found. This item is almost certainly the same badge already catalogued as dc27-badge-2019 under its Human/default listing; see notes above and duplicate_of in the research report.'
last_modified_date: '2026-09-08'
---

The DEF CON 27 (2019) conference badge, designed by Joe Grand of Grand Idea Studio, was issued in ten silkscreen and gemstone color variants marking different attendee types: Human, Speaker, Vendor, Press, Village, Contest, Artist, Goon, CFP Review, and Uber. This entry covers the black-PCB "Uber" variant, one of the rarest of the run — only around 20 were fully finished with a matching black gemstone, compared to more than 26,500 of the standard white "Human" badge, out of roughly 28,600 badges made in total.

Electronically, every color variant shares the same hardware: an NXP KL27 (ARM Cortex-M0+) microcontroller, an NXP NXH2261 near-field magnetic induction transceiver for badge-to-badge interaction, a Texas Instruments LP5569 LED driver, and a single CR2032 coin-cell battery, all built around a round PCB set with a handcrafted Brazilian quartz gemstone. Attendees used the badge to take part in a conference-wide quest by completing tasks during DEF CON. Grand Idea Studio has published the design as open source (hardware under CC BY 4.0, firmware partly under the Clear BSD License), though no variant-specific repository for the Uber badge specifically was located during this pass.

Because so few Uber badges were made, unpopulated or unfinished black-variant PCBs — boards that never made it into a finished, gem-mounted badge — have separately circulated among collectors on eBay and been catalogued by Worthpoint's appraisal service, which is how this entry originated. The Worthpoint pages themselves could not be fetched directly (they sit behind a bot-detection captcha), so the figures above come from search-result snippets rather than the full page text.
