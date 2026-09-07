---
title: TV3Y3 Indie Badge (DEF CON 27)
id: dc27-tv3y3-indie-badge-def-con-27
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Harbinger LTD
  url: https://www.tindie.com/stores/awkwardai/
  role: 'designer (Tindie/Hackaday.io handle: awkwardai / ''awkward intelligence'')'
summary: A DEF CON 27 badge shaped like a severed alien robotic eyeball, doubling as an image target for a companion AR app built with Vuforia; it carries a charlieplexed LED matrix run by a socketed ATtiny85.
functions: The front artwork is a printed AR marker recognized by a companion iOS/Android app (Vuforia-based image recognition, not facial recognition). On the back, an ATtiny85 in an 8-pin socket drives a charlieplexed 12-LED matrix with animations. Two SAO ports let other add-ons plug in, and exposed/hidden copper traces let owners cut into the board to reach spare microcontroller pins and the SAO data lines for hardware hacking.
look:
  colors:
  - black
  - gold
  - copper
  shape: other
  themes:
  - robot
  - sci-fi
  - cyberpunk
tech:
  mcu: ATtiny85
  leds:
    count: 12
    type: charlieplexed
    note: 12-LED charlieplexed matrix with preprogrammed animations
  display: none
  connectivity: []
  battery: 2x AA
  sao_version: null
  sao_ports: 2
get_one:
  price: $50
  price_usd: 50
  quantity: ''
  availability: sold_out
  availability_note: Tindie listing shows availability "oos" (out of stock) as of 2026-09-07.
  distribution:
  - purchase
  where: Sold by Harbinger LTD (Tindie seller awkwardai) as a bare board, component kit, or fully assembled unit; each version shipped with a lanyard and one of three random companion SAOs.
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/164210-defcon-27-tv3y3-badge
  firmware_url: null
  gerbers_url: https://hackaday.io/project/164210-defcon-27-tv3y3-badge
  eda_tool: null
  notes: Final Gerbers and the AR image-target photos are published as downloads on the Hackaday.io project page (12 files total). No separate firmware/source code for the ATtiny85 animations was found published; units ship with the chip preprogrammed.
links:
- label: www.tindie.com/products/awkwardai/tv3y3-indie-badge-for-def-con-27
  url: https://www.tindie.com/products/awkwardai/tv3y3-indie-badge-for-def-con-27/
  kind: store
  archived: https://web.archive.org/web/20260503123834/https://www.tindie.com/products/awkwardai/tv3y3-indie-badge-for-def-con-27/
- label: 'Hackaday.io: Defcon 27 TV3Y3 Badge'
  url: https://hackaday.io/project/164210-defcon-27-tv3y3-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260508164750/https://hackaday.io/project/164210-defcon-27-tv3y3-badge
images:
- file: assets/images/badges/dc27/tv3y3-indie-badge-def-con-27/7801f74b0f.jpg
  source: https://www.tindie.com/products/awkwardai/tv3y3-indie-badge-for-def-con-27/
  credit: Harbinger LTD
  caption: TV3Y3 Indie Badge, eyeball-styled PCB badge with exposed copper artwork and charlieplexed LED matrix
  archived: https://web.archive.org/web/20260503123834/https://www.tindie.com/products/awkwardai/tv3y3-indie-badge-for-def-con-27/
- file: assets/images/badges/dc27/tv3y3-indie-badge-def-con-27/52fb6cea55.jpg
  source: https://www.tindie.com/products/awkwardai/tv3y3-indie-badge-for-def-con-27/
  credit: Harbinger LTD
  caption: TV3Y3 Indie Badge, showing the SAO adapters and battery holder on the back
  archived: https://web.archive.org/web/20260503123834/https://www.tindie.com/products/awkwardai/tv3y3-indie-badge-for-def-con-27/
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/awkwardai/tv3y3-indie-badge-for-def-con-27/
  title: TV3Y3 Indie Badge (DEF CON 27)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 27''.'
  archived: https://web.archive.org/web/20260503123834/https://www.tindie.com/products/awkwardai/tv3y3-indie-badge-for-def-con-27/
- kind: url
  url: https://www.tindie.com/products/awkwardai/tv3y3-indie-badge-for-def-con-27/
  title: TV3Y3 Indie Badge for DEF CON 27 from Harbinger LTD on Tindie
  accessed: '2026-09-07'
  note: Confirmed maker (Harbinger LTD), price ($50), out-of-stock status, feature list, kit tiers, and the Hackaday.io documentation link.
  archived: https://web.archive.org/web/20260503123834/https://www.tindie.com/products/awkwardai/tv3y3-indie-badge-for-def-con-27/
- kind: url
  url: https://hackaday.io/project/164210-defcon-27-tv3y3-badge
  title: Defcon 27 TV3Y3 Badge - Hackaday.io project page
  accessed: '2026-09-07'
  note: Confirmed AR/Vuforia companion-app concept, ATtiny85 + charlieplexed LED detail, and location of published Gerber/image-target files.
  archived: https://web.archive.org/web/20260508164750/https://hackaday.io/project/164210-defcon-27-tv3y3-badge
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: Fact-checked against the live Tindie listing and Hackaday.io project page; every non-empty field and body sentence is directly supported (maker name, $50 price, "oos" availability meta tag, ATtiny85 + charlieplexed 12-LED matrix, 2 SAO ports, AR/Vuforia image-target concept, 12 published files including a Gerber zip and front1.jpg/back1.jpg image-target photos, no firmware file present, self-funded run that "JUST BARELY paid for itself"). Both saved photos show the actual "DC27 TV3Y3 BADGE" product. Quantity made and a firmware/code repository remain unpublished, so left empty. No SAO header pin-count (v1 vs v2) is stated by the maker, so sao_version is left null.
last_modified_date: '2026-09-07'
---

The TV3Y3 Indie Badge was Harbinger LTD's (Tindie/Hackaday.io handle awkwardai) first fully functional DEF CON badge, made for DEF CON 27 in 2019. Its front is designed as a "severed alien robotic eyeball," and that artwork doubles as an AR image target for a companion iOS/Android app built on Vuforia's image-recognition engine, letting the badge stand in for face-tracking AR without using facial recognition. All the electronics live on the back: a socketed ATtiny85 drives a charlieplexed 12-LED matrix with built-in animations, and two SAO ports allow other add-ons to plug in.

The badge was sold on Tindie as a bare board, a component kit, or a fully assembled unit for $50, each tier including a custom lanyard and one of three random companion SAOs; the assembled version also shipped with two AA batteries, good for roughly a week of runtime. Hidden and exposed copper traces let owners cut into the board to expose spare ATtiny85 pins and the SAO data lines for further hardware hacking. The maker described the run as a limited one funded mostly through Tindie sales of accompanying "Shitty Add-Ons," breaking about even.

## Make your own

Final Gerber files and the photographic AR image-target assets (front and back marker images) are published as downloads on the badge's Hackaday.io project page, which lists 12 files total. No separate firmware or source repository for the ATtiny85 animations was located; production units ship with the chip preprogrammed.
