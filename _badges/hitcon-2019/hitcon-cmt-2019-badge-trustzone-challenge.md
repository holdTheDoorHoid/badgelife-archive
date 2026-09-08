---
title: HITCON Badge 2019
id: hitcon-2019-hitcon-cmt-2019-badge-trustzone-challenge
layout: badge
parent: Hitcon Cmt 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hitcon-2019
year: 2019
makers:
- name: yuawn (Alan Lee)
  url: https://github.com/yuawn
summary: 'The official HITCON CMT 2019 conference badge: an ARM TrustZone-based electronic badge with 24 unlockable RGB LEDs, a directional-pad interface, and an on-badge CTF built around exploiting the secure/non-secure world boundary.'
functions: 'Four on-badge pages navigated with the D-pad and A/B buttons: an LED status display, a pattern viewer (11 unlockable patterns), a paint mode for customizing LED colors, and a Snake game (unlocked via micro-USB serial console, with its own command-line interface). LEDs and patterns unlock by playing the games, completing sponsor-booth missions, or by reverse-engineering and exploiting the badge''s non-secure firmware to break the TrustZone secure-world protections — the three challenge stages are "Snake pattern," "Pwned NS pattern," and "Pwned the whole badge pattern."'
look:
  colors: []
  shape: null
  themes:
  - ctf
  - puzzle
  - security
tech:
  mcu: M2351ZIAAE
  leds:
    count: 24
    type: RGB
    note: Unlocked individually through gameplay, sponsor missions, or the TrustZone exploitation challenge.
  display: null
  connectivity:
  - usb
  inputs:
  - buttons
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to attendees of HITCON CMT 2019 (Taipei) as the conference badge.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/yuawn/HITCON-badge-2019/tree/master/hardware
  firmware_url: https://github.com/yuawn/HITCON-badge-2019/tree/master/firmware
  license: MIT
  notes: Repo also includes an `exploit` directory (challenge solution) and a `source` directory alongside a PDF (hitcon-badge-2019.pdf), likely challenge/writeup documentation.
links:
- label: github.com/yuawn/HITCON-badge-2019
  url: https://github.com/yuawn/HITCON-badge-2019
  kind: repo
images: []
contact: {}
notes:
- Taiwan-shaped ARM TrustZone challenge badge, M2351-class MCU, 24 unlockable LEDs, sponsor-booth exploitation stages. Found by the event-year sweep, task con-hitcon.
- 'Sweep title was "HITCON CMT 2019 Badge (TrustZone Challenge)"; the maker''s own README titles it simply "HITCON Badge 2019" — kept the sweep''s descriptive wording as the entry title since it is more identifying, but note the maker''s own name here.'
status: released
sources:
- kind: url
  url: https://github.com/yuawn/HITCON-badge-2019
  title: HITCON CMT 2019 Badge (TrustZone Challenge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-hitcon); event read as ''HITCON CMT 2019''.'
- kind: url
  url: https://raw.githubusercontent.com/yuawn/HITCON-badge-2019/master/README.md
  title: 'yuawn/HITCON-badge-2019 README'
  accessed: '2026-09-08'
  note: 'Maker''s own description of the MCU, four badge pages, Snake game, CLI, and the three TrustZone challenge stages; confirms MIT license and open hardware/firmware directories.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Confirmed via the maker''s own repo and README. No price, quantity, or shape/color details are published anywhere in the repo, and no photos of the physical badge were found (the repo has no image assets; the GitHub og:image is only an auto-generated social card, not a photo). Left those fields empty rather than guessing. The "Taiwan-shaped" claim from the sweep notes could not be confirmed or denied — no photo exists to check it, so look.shape was left null.'
last_modified_date: '2026-09-08'
---

The HITCON Badge 2019 was the official conference badge for HITCON CMT 2019 in Taipei, designed by yuawn (Alan Lee) around a Nuvoton M2351ZIAAE microcontroller — one of the first ARM Cortex-M23 chips with TrustZone-M, hardware-enforced separation between "secure" and "non-secure" execution worlds. The badge carries 24 RGB LEDs and a directional-pad-plus-two-button interface driving four on-device pages: an LED status view, a pattern browser, a freeform paint mode, and a Snake game reachable over a micro-USB serial console complete with its own toy command-line shell.

What makes the badge notable is its built-in CTF: LEDs and patterns unlock through ordinary play and by completing sponsor-booth missions, but three challenge stages are gated behind actually breaking the badge's security model — reverse-engineering the non-secure firmware and exploiting it to cross into, and ultimately compromise, the TrustZone-protected secure world. The final stage tracks a "pwned the whole badge" state, making the badge itself the CTF target rather than just a badge that hosts one.

Hardware, firmware, an exploit writeup, and supporting source are all published under the MIT license in yuawn's GitHub repository, along with a PDF (likely challenge documentation). No pricing, production quantity, or photos of the physical badge could be found; it appears to have been distributed as the standard attendee badge rather than sold separately.

## Make your own

The hardware and firmware directories in the [GitHub repo](https://github.com/yuawn/HITCON-badge-2019) are published under MIT. Someone recreating it would need the M2351ZIAAE-based hardware design from `hardware/`, the badge firmware from `firmware/`, and can reference the `exploit/` and `source/` directories plus the included PDF for the TrustZone challenge design and its intended solution.
