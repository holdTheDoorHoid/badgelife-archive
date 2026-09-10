---
title: BSides Perth 2017 Badge
id: bsides-perth-2017-bsides-perth-2017-wemos-badge
layout: badge
parent: BSides Perth 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-perth-2017
year: 2017
makers:
- name: BSides Perth
  url: https://2018.bsidesperth.com.au/
summary: The official BSides Perth 2017 conference badge, a Wemos D1 Mini (ESP8266)
  with a small OLED display and a single RGB LED, mounted on a laser-cut and etched
  acrylic panel.
functions: Powers on to a boot animation with conference text on the OLED, then
  cycles a single NeoPixel RGB LED through a fixed sequence of colors.
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
  - text
tech:
  mcu: ESP8266 (Wemos D1 Mini)
  leds:
    count: 1
    type: NeoPixel (WS2812-family)
    note: Single RGB LED on an add-on "RGB Shield", driven with the Adafruit_NeoPixel
      library on pin D2.
  display: 0.66" 64x48 OLED (SSD1306, I2C)
  connectivity: []
  battery: switched AA battery holder
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Given to BSides Perth 2017 attendees; not sold separately as far as sources
    show.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/BsidesPerth/Badge-2017
  eda_tool: null
  notes: Firmware (Arduino sketch plus a bundled copy of the Adafruit_SSD1306 library)
    is published. No PCB design files, enclosure files, or BOM were found, so hardware
    is not confirmed open source beyond the stock Wemos D1 Mini and shield modules
    used.
links:
- label: github.com/BsidesPerth/Badge-2017
  url: https://github.com/BsidesPerth/Badge-2017
  kind: repo
- label: BSides Perth blog - "2017 Badges"
  url: https://2018.bsidesperth.com.au/blog/
  kind: article
images: []
contact: {}
notes:
- Sweep saw the title as "BSides Perth 2017 Wemos badge"; renamed to "BSides Perth
  2017 Badge" to match how the maker refers to it (their blog post is simply titled
  "2017 Badges").
- The maker's own blog post text matches the sweep's one-line summary almost verbatim,
  confirming the item is real and not just a search-snippet artifact.
- 'The blog post''s own permalink (https://2018.bsidesperth.com.au/2018/01/11/hello-world/)
  404s; the post text was only recoverable from the excerpt embedded in the blog
  listing page (https://2018.bsidesperth.com.au/blog/). The blog also linked a photo
  of the badge (wp-content/uploads/2018/01/badge-368x240.jpg) but that image file
  itself 404s on the live site, so no photo could be saved.'
- No price, quantity made, or open hardware/BOM files were found; left empty rather
  than guessed.
status: released
sources:
- kind: url
  url: https://github.com/BsidesPerth/Badge-2017
  title: BSides Perth 2017 Wemos badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-canberra);
    event read as ''BSides Perth 2017''.'
- kind: url
  url: https://github.com/BsidesPerth/Badge-2017
  title: 'GitHub: BsidesPerth/Badge-2017'
  accessed: '2026-09-10'
  note: Repo contains BSides_Badge_Complete.ino plus a bundled Adafruit_SSD1306
    library; sketch confirms a 64x48 I2C SSD1306 OLED and a single NeoPixel RGB
    LED on pin D2 (Wemos-style pin naming), and the OLED boot text reads "BSIDES
    PERTH 2017 HACK ME!!".
- kind: url
  url: https://2018.bsidesperth.com.au/blog/
  title: 'Blog | BSides Perth (listing page, "2017 Badges" excerpt)'
  accessed: '2026-09-10'
  note: 'Maker''s own description of the badge: "Components: Wemos D1 Mini, OLED
    Shield, RGB Shield, Switched AA Battery Holder. Badge Base: Laser cut and etched
    acrylic panel. Code: ... available on our Github." Confirms hardware, enclosure,
    battery, and that feedback on the badge was positive.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Core facts (hardware, enclosure, firmware location) are confirmed directly
    from the maker's own blog and repo, so this is better than low confidence, but
    no maker photo of the assembled badge could be retrieved (the linked image URL
    404s and the post's own permalink 404s), and price/quantity/distribution details
    were never published anywhere found.
last_modified_date: '2026-09-10'
---

The 2017 BSides Perth badge was built around a Wemos D1 Mini (an ESP8266 board) fitted with a small OLED display shield and an RGB LED shield, powered by a switched AA battery holder and mounted on a laser-cut and etched acrylic panel. On boot it shows "BSIDES PERTH 2017 HACK ME!!" on its 64x48 SSD1306 OLED before running a small bitmap-and-shape demo, while a single NeoPixel-style RGB LED cycles through a fixed set of colors in the background.

It was the organizers' first year running a badge, and BSides Perth said on their blog that attendee feedback on it was strongly positive. The firmware — an Arduino sketch built largely from Adafruit's stock SSD1306/NeoPixel example code — was published on GitHub, but no PCB, enclosure, or bill-of-materials files were found, so the hardware side of the project is not confirmed to be open beyond the off-the-shelf Wemos board and shields used to build it.
