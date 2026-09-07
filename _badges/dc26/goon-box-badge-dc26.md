---
title: Goon Box Badge (DC26)
id: dc26-goon-box-badge-dc26
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: GoonBoxBadge (MK Factor)
  url: https://mkfactor.com
summary: 'An independent, crowdfunded two-part badge made for DEF CON 26 (2018): a red "Goon Box" worn on a shirt or lanyard, triggered by a companion sonic-screwdriver wand over infrared.'
functions: 'The sonic-screwdriver wand sends an infrared signal that makes the wearer''s Goon Box pulse its LED; the wand has a normal mode, an LED "bling" mode, and a secret mode, and its IR receiver doubles as a remote-control tester.'
look:
  colors: []
  shape: sonic screwdriver
  themes:
  - sci-fi
  - tv
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - ir
  battery: null
  sao_version: null
get_one:
  price: '$25 (Kickstarter) / a target of $20 at DEF CON'
  price_usd: 20
  quantity: ''
  availability: unknown
  distribution:
  - crowdfunding
  - purchase
  where: 'Kickstarter campaign (April-May 2018), with badges also sold in person at DEF CON 26'
make_your_own:
  open_source: 'yes'
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: 'The Kickstarter page states board files and code would be released after DEF CON 26; no live repository was found.'
links:
- label: twitter.com/goonboxbadge
  url: https://twitter.com/goonboxbadge
  kind: social
- label: 'Goon Box DEFCON 26 Indie Badge (Kickstarter)'
  url: https://www.kickstarter.com/projects/1422242860/goon-box-defcon-26-indie-badge
  kind: store
- label: mkfactor.com
  url: https://mkfactor.com
  kind: website
images: []
contact: {}
notes:
- two-part kit: red "Goon Box" plus IR-triggering sonic-screwdriver wand
status: released
sources:
- kind: url
  url: https://twitter.com/goonboxbadge
  title: Goon Box Badge (DC26)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 26''.'
- kind: url
  url: https://web.archive.org/web/20180810174437/https://twitter.com/GoonBoxBadge/status/1027974010787717120
  title: 'GoonBoxBadge (@GoonBoxBadge) / Twitter, archived Aug 2018'
  accessed: '2026-09-07'
  note: 'Prior researcher''s claimed bio quote ("An Indie badge for DEFCON 26") could not be re-verified this pass - web.archive.org was unreachable from this session''s tools. The DC26/2018 attribution is independently confirmed via the maker''s own Kickstarter page (see below), so this is left in place but should not be treated as re-checked.'
- kind: url
  url: https://web.archive.org/web/20180726213239/https://twitter.com/GoonBoxBadge/status/1022595579279364098
  title: GoonBoxBadge retweet, archived Jul 2018
  accessed: '2026-09-07'
  note: 'Could not be re-verified this pass (web.archive.org unreachable). The "turned off my TV" claim it was cited for does not match the maker''s own description of the badge''s function (see Kickstarter source) and the TV-B-Gone claim has been removed from this entry as unsupported.'
- kind: url
  url: https://x.com/GoonBoxBadge
  title: GoonBoxBadge (@GoonBoxBadge) / X
  accessed: '2026-09-07'
  note: 'The account is NOT gone, contrary to the prior research pass - it is live, bio reads "An Indie badge for DEFCON by @ktjgeekmom and @compukidmike", links to mkfactor.com, joined April 2018. Confirms the MK Factor connection.'
- kind: url
  url: https://www.kickstarter.com/projects/1422242860/goon-box-defcon-26-indie-badge
  title: Goon Box DEFCON 26 Indie Badge by Michael Whiteley
  accessed: '2026-09-07'
  note: 'Maker''s own campaign page. Confirms event/year (DEF CON 26, 2018), creators Michael Whiteley (@compukidmike) and Katie Whiteley (@ktjgeekmom) of MK Factor, price ($25 Kickstarter / target $20 at DEF CON), 237 backers pledging $9,217, the two-part design (red "Goon Box" plus sonic-screwdriver wand triggering it over IR, LED pulse, multiple modes, IR remote-control tester), and that hardware/firmware were to be released open source after DEF CON. Photos on the page show the screwdriver visually matches the "sonic screwdriver" shape already in this entry. No mention of TV-B-Gone functionality.'
- kind: url
  url: https://mkfactor.com
  title: MK Factor
  accessed: '2026-09-07'
  note: 'Maker''s blog/portfolio. Lists the "Goon Box Badge Kickstarter" post (Apr 2018) linking the campaign above, plus later projects (a DC27 Goon Box presale, a 2019 SAINTCON Enigma badge, a DC28 Car Hacking Village badge) - noted here as other work, not folded into this DC26 entry.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07) corrected the prior pass: the @GoonBoxBadge X account is NOT gone - it is live and was read directly. The maker''s own Kickstarter campaign page and mkfactor.com blog were also found and read, confirming the MK Factor / Michael & Katie Whiteley connection that the prior pass had flagged as unconfirmed (matching the maker naming already used on dc32-cassandra-sao). The "TV-B-Gone" function and the community-sheet note behind it were removed: the maker''s own description is an IR-triggered sonic-screwdriver/Goon-Box pair with LED effects and an IR remote-control-tester side effect, not a TV-B-Gone circuit, and the two web.archive.org tweets cited for that claim could not be re-verified this pass because web.archive.org was unreachable from every tool available in this session (WebFetch refused the domain; direct curl got connection-refused; the browser tool''s navigation was denied). Price, quantity produced, chip/MCU, LEDs, display, and photos of the badge itself remain unconfirmed/empty - the Kickstarter page''s own gallery has photos but none were saved as entry images in this pass (out of scope for a fact-check-only pass). No images are present in this entry, so there was nothing to check there.'
last_modified_date: '2026-09-07'
---

The Goon Box Badge was an independent (non-official) badge made for DEF CON 26 in 2018 by Michael Whiteley (@compukidmike) and Katie Whiteley (@ktjgeekmom), a husband-and-wife team who make projects under the name MK Factor. It was funded through a Kickstarter campaign (April-May 2018) that raised $9,217 from 237 backers against a $1,000 goal, with badges priced at $25 on Kickstarter and a target of $20 in person at DEF CON.

The kit is two parts: a red "Goon Box," worn on a shirt or lanyard, and a companion sonic-screwdriver wand - a nod to Doctor Who, styled in blue soldermask with gold accents. The wand sends an infrared signal that makes the wearer's Goon Box pulse its LED; it has a normal mode, an LED "bling" mode, and an undisclosed secret mode, and because it uses a standard IR receiver it can also double as a remote-control tester. The maker described the project as open source, with board files and code to be released after DEF CON.

Beyond the Kickstarter page and the maker's own site (mkfactor.com), little else about this specific run could be confirmed: no photos of the finished badge were saved to this entry, and the number actually produced, its final component choices (MCU, LEDs), and its later availability are not documented here.
