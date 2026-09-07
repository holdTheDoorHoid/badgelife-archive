---
title: Monero Badge (DC26)
id: dc26-monero-badge-dc26
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: elasticninja
  url: https://twitter.com/elasticninja
- name: tonym128
  url: https://twitter.com/tonym128
- name: fluffypony
  url: https://twitter.com/fluffypony
summary: A DEF CON 26 (2018) hardware badge given out as the prize for the "Monero Badge Challenge," a crypto scavenger hunt run by its creators elasticninja, tonym128, and fluffypony.
functions: 'Not the badge itself: solve a cipher printed on a paper "challenge token" (handed out at DEF CON info booths and the BCOS/Monero village), tweet the decoded answer at the badge creators, then trade the token in for the badge in person.'
look:
  colors: []
  shape: null
  themes:
  - crypto
  - privacy
  - security
  - ctf
  - puzzle
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - contest
  - free_drop
  where: Earned by solving the Monero Badge Challenge cipher at DEF CON 26 (Aug 2018) and turning in a paper challenge token to elasticninja, tonym128, or fluffypony in person.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: monerobadge.org
  url: http://monerobadge.org/
  kind: website
images: []
contact: {}
notes:
- 576 APA102 LEDs, dual 18650 batteries (from the community sheet; could not independently confirm on the maker's own pages)
status: listed
sources:
- kind: url
  url: http://monerobadge.org/
  title: Monero Badge (DC26)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 26''.'
- kind: url
  url: http://web.archive.org/web/20180813233213/http://monerobadge.org:80/
  title: The Monero Badge Challenge || DEF CON 26
  accessed: '2026-09-07'
  note: 'Live site returns HTTP 522; used the Aug 2018 Wayback Machine snapshot instead. Confirms this is a scavenger-hunt/challenge page (not a spec sheet) run by @elasticninja, @tonym128 and @fluffypony to give away the DEF CON 26 Monero badge; describes the token-decode-tweet-redeem process; shows four photos of the paper "challenge token" (not the badge itself).'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Fact-check pass (2026-09-07): re-fetched the cited Wayback capture
    (web.archive.org/web/20180813233213/http://monerobadge.org:80/) directly and
    confirmed it matches every remaining factual claim in this entry — the four-step
    cipher/tweet/redeem challenge, the token pickup locations (creators in person,
    BCOS/Monero village in the Pompei I room at Caesar's Palace, DEF CON info booths),
    the three creator Twitter handles (elasticninja, tonym128, fluffypony), and the
    four token photos (not photos of the badge). It never mentions chip, LEDs,
    battery, display, price, or quantity, so tech.* and get_one.price_usd/quantity
    correctly remain null, and no images were saved since none show the badge itself.
    Corrected two unsupported claims found on this pass: the summary called fluffypony
    "Monero lead maintainer" and the body called the event "a scavenger hunt the
    Monero project ran" / fluffypony "a Monero project figure" — the cited source
    never states an official Monero-project affiliation or a lead-maintainer title
    (this contradicted the entry's own prior notes, which claimed that title had
    already been left out); both were reworded to say only what the source supports,
    that the challenge was run by its three named creators. The pre-existing sheet
    note "576 APA102 LEDs, dual 18650 batteries" remains in `notes` labeled explicitly
    as unconfirmed against any source read for this entry; it is not asserted as fact
    anywhere else. Web search and reddit/duckduckgo/bing access were unavailable
    during the original research pass and remain unconfirmed avenues for finding
    maker-authored hardware specs or a real-name identification of the creators.
last_modified_date: '2026-09-07'
---

The Monero Badge was the prize in the "Monero Badge Challenge," a cryptography scavenger hunt its creators — elasticninja, tonym128, and fluffypony — ran at DEF CON 26 in Las Vegas in August 2018. Rather than being sold or handed out directly, the badge was earned: attendees picked up a paper "challenge token" from the creators themselves, from the BCOS/Monero village in Caesar's Palace, or from DEF CON info booths, decoded a secret message printed on the front and back, and tweeted an encoded reply at the organizers. Solvers received a location back and could trade their token in person for the actual hardware badge.

No surviving page describes the badge's electronics, price, or production run in the maker's own words; monerobadge.org is now offline (the live site returns an HTTP 522 error) and only a 2018 Wayback Machine capture of the challenge instructions could be read. A community-sourced note carried over from before this research pass claims 576 APA102 LEDs and dual 18650 battery power, but that could not be independently confirmed against any source read for this entry.
