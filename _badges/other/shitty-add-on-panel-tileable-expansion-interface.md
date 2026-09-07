---
title: Shitty Add-On Panel (tileable expansion interface)
id: other-shitty-add-on-panel-tileable-expansion-interface
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: other
year: 0
makers:
- name: bbenchoff
summary: 'A bare 60mm x 60mm tileable host panel that passes 3.3V power through a Shitty Add-On V1.69bis connector; panels are meant to be joined end-to-end.'
functions: 'Passive expansion/mounting panel: no on-board logic, just power pass-through and M3 standoff holes so multiple panels can be tiled together.'
look:
  colors: []
  shape: rectangle
  themes: []
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/bbenchoff/Shitty-Add-On-Panel
  firmware_url: null
  eda_tool: null
links:
- label: github.com/bbenchoff/Shitty-Add-On-Panel
  url: https://github.com/bbenchoff/Shitty-Add-On-Panel
  kind: repo
images: []
contact: {}
notes:
- Tileable panel/host board compliant with Shitty Add-On V1.69bis spec
status: listed
sources:
- kind: url
  url: https://github.com/bbenchoff/Shitty-Add-On-Panel
  title: Shitty Add-On Panel (tileable expansion interface)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/bbenchoff/Shitty-Add-On-Panel
  title: 'GitHub repo README and file listing'
  accessed: '2026-09-07'
  note: 'Verified via GitHub API: README text ("tileable display panel", 3.3V through a Shitty Add-On V1.69bis connector, 60mm x 60mm, M3 standoff holes) matches word-for-word; repo description confirms V1.69bis compliance. File listing has README.md, ShittyPanel.sch, ShittyPanel.brd, ShittyPanelGerbers.zip (no images). created_at and pushed_at both 2019-07-24, 0 releases, 2 stargazers, topics empty.'
- kind: url
  url: https://hackaday.com/2019/03/20/introducing-the-shitty-add-on-v1-69bis-standard/
  title: 'Introducing The Shitty Add-On V1.69bis Standard (Hackaday, by Brian Benchoff)'
  accessed: '2026-09-07'
  note: 'Confirms bbenchoff (GitHub profile name: Brian Benchoff) authored Hackaday''s own announcement of the V1.69bis SAO standard, supporting the claim that he is closely associated with the standard as its author, not just a user of it.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Fact-check pass re-verified every non-empty field and body sentence against
    the GitHub repo (API-confirmed README text, file listing, created/pushed
    dates, star count, empty topics, zero releases) and, this time with web
    access available, against Hackaday: Brian Benchoff (the GitHub profile's
    display name) wrote Hackaday's own March 2019 article introducing the
    V1.69bis standard, confirming the "closely associated with the SAO
    standard" claim the original researcher could not check. No maker bio,
    event, price, quantity, or photos exist anywhere in the repo or its
    metadata, so those fields stay empty/null and event stays "other" -
    nothing found ties this panel to a specific convention or year. Confidence
    raised from low to medium (not high) because event/price/quantity/images
    remain entirely unfound rather than confirmed absent.
last_modified_date: '2026-09-07'
---

This is a bare, unpopulated expansion panel rather than a badge or SAO in the usual sense: a 60mm x 60mm board that carries 3.3V power through a Shitty Add-On V1.69bis (6-pin) connector and is designed to be tiled end-to-end with identical panels, using M3 standoff holes for mounting. It has no microcontroller, LEDs, or display of its own — it is infrastructure for building larger panel arrays out of SAO-compliant boards.

The project is published on GitHub by user bbenchoff (Brian Benchoff), who is closely associated with the Shitty Add-On (SAO) standard itself. The repository includes Eagle-format schematic and board files (`ShittyPanel.sch`, `ShittyPanel.brd`) and a Gerbers zip for fabrication, but no photos, bill of materials, pricing, or notes about which convention or year it was built for. The repo was created and last updated on 2019-07-24 and has never had a tagged release. Benchoff also authored Hackaday's own article introducing the V1.69bis standard, confirming he is closely associated with it as its author rather than just a user.


