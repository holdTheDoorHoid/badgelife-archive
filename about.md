---
title: About
layout: default
nav_order: 9
---

# About the Badgelife Archive

## What this is

Badgelife is the hobby of designing, building and trading electronic conference badges and the small add-on boards (SAOs, "Shitty Add-Ons") that plug into them. Hundreds are made every year for DEF CON alone, most in tiny runs, and the information about them scatters across spreadsheets, Hackaday pages, Discord servers and storefronts that quietly disappear.

This archive collects all of that in one place so that:

- you can find a badge you only half remember ("the skull one with the LoRa radio, maybe 2023?"),
- you can see who made it, what it does, and whether you can still get one, and
- if the maker published the files, you can build your own.

## Relationship to badge.life

This site is a fork of the [badge.life](https://badge.life/) website run by the Badgelife Village at DEF CON. The village's site remains the home of the village itself: its schedule, its badge, its specifications work and its community. This archive reuses the village's site framework and its Badge Archive pages with attribution, and builds on the yearly badge sheets the village maintains. It is **not affiliated with, or endorsed by, the Badgelife Village or DEF CON**. Anything here that the village would like to adopt is theirs to take.

## Credits

- **The Badgelife Village** and the maintainers of the yearly community badge sheets, whose careful data entry is the backbone of the DC30–DC34 entries.
- **Every maker** whose project pages, repositories and photos are referenced. The badges are theirs; this is only an index.
- **Hackaday** and Hackaday.io, whose curated conference-badge lists and SAO project pages document much of the DC26–DC27 era and the Supercon add-on scene.
- The [Just the Docs](https://github.com/just-the-docs/just-the-docs) theme and Jekyll, which badge.life chose and which this fork keeps.

## How entries are researched

Each entry carries a research status:

| Status | Meaning |
|:--|:--|
| **stub** | Only what the community sheet listed for that year: name, maker, price, a link. Not yet checked against any other source. |
| **researched** | Filled in from the maker's own pages (project page, repository, storefront, social posts) and any press coverage. Fields are cited in the entry's Sources section. |
| **verified** | A second, independent pass re-read the cited sources and confirmed each claim, or the maker confirmed it. |

Research is done by people and by automated research agents working from public sources. Agents do not invent details: a field is left blank rather than guessed, and every entry lists the pages it was built from with the date they were read. Where sources disagree, the entry says so.

## Photos, links and takedowns

Photos are copied into this repository rather than hot-linked, because makers' sites go offline and hot-linked images die with them. Every photo is credited and linked to the page it came from. Every external link is also submitted to the Internet Archive's Wayback Machine so a snapshot survives if the original disappears.

If you made something shown here and want a photo, a contact detail or an entire entry changed or removed, [open an issue]({{ site.gh_edit_repository }}/issues/new?title=Takedown%20request) or email the repository owner through GitHub. Requests from makers are honoured without argument.

Maker contact details (email, Discord, social handles) appear only when the maker themselves published them on the public community badge sheet for that year.

## 3D models

Where a maker has published their design files, the archive builds an interactive 3D model of the board and shows it on
the entry page (drag to rotate, scroll to zoom, download the `.glb`). Two methods are used:

- **KiCad boards** are exported with KiCad's own 3D exporter, so the board shape, copper, soldermask, silkscreen and any
  parts that have a 3D footprint model appear as designed. Parts without a model show only their pads. Files are
  Draco-compressed, so a badge is usually a few hundred kilobytes.
- **Gerber-only designs** (fabrication files, or Eagle and other formats we cannot open) are rendered top and bottom from
  the Gerbers and wrapped onto a 1.6 mm board of the correct outline, holes included. Components are not modelled.

Models are derived works of the makers' published files and are offered under the same terms as those files. They are
generated automatically, so a model can be wrong where the published files were a draft or a different revision than
what shipped; the entry names the exact source file. If you made a badge and would rather not have a model shown, open an
issue or email and it will be removed, as with photos.

## License

The site's code and layout inherit the MIT license of the badge.life repository. The catalogue text is contributed under the same terms. Photos, logos and design files remain the property of their makers and are reproduced here for identification and preservation; the individual entry credits the source.
