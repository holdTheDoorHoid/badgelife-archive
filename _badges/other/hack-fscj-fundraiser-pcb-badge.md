---
title: Hack FSCJ (fundraiser PCB badge)
id: other-hack-fscj-fundraiser-pcb-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2017
makers:
- name: Kirball
  url: https://hackaday.io/Kirball
  role: project lead
- name: adamcwhooper
  url: https://hackaday.io/hacker/238022-adamcwhooper
- name: a.a.Ron
  url: https://hackaday.io/hacker/238040-aaron
- name: gabriel licina
  url: https://hackaday.io/hacker/344798-gabriel-licina
summary: 'A planned fundraiser PCB badge for Hack@FSCJ, a student hacking/maker organization at Florida State College at Jacksonville.'
functions: ''
look:
  colors: []
  shape: null
  themes:
  - charity
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - crowdfunding
  where: 'A Kickstarter campaign was announced ("coming soon") with only a preview link published; no evidence it launched or completed. Also solicited PayPal donations directly to the student organization.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/26229-hack-fscj
  url: https://hackaday.io/project/26229-hack-fscj
  kind: hackaday
- label: facebook.com/HackFSCJ
  url: https://www.facebook.com/HackFSCJ/
  kind: social
- label: twitter.com/hackfscj
  url: https://twitter.com/hackfscj
  kind: social
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
- 'FSCJ = Florida State College at Jacksonville; Hack FSCJ / Hack@FSCJ appears to be a student hacking club there. No con or event ties this badge to a specific date beyond the 2017 project page.'
status: unknown
sources:
- kind: url
  url: https://hackaday.io/project/26229-hack-fscj
  title: Hack FSCJ (fundraiser PCB badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''other (fundraiser, not a con)''.'
- kind: url
  url: https://hackaday.io/project/26229-hack-fscj
  title: Hack FSCJ | Hackaday.io
  accessed: '2026-09-07'
  note: 'Re-fetched for research. Project page (created Aug 4, 2017) is essentially a stub: description is only "Hack FSCJ''s official project page for our fundraiser PCB Badge." Lists a 4-person team (Kirball, adamcwhooper, a.a.Ron, gabriel licina), links to a Facebook page, a Twitter account, a PayPal donation button, and a Kickstarter preview link. No technical details, no build log entries, no photos of the badge itself (only unrelated "similar projects" thumbnails and a generic Hackaday.io placeholder image), no price or quantity.'
- kind: url
  url: https://www.facebook.com/HackFSCJ/
  title: Hack@FSCJ Facebook page
  accessed: '2026-09-07'
  note: 'Fetch returned only the page title ("Hack@FSCJ"), confirming the organization is Jacksonville, FL based and likely tied to Florida State College at Jacksonville; no post content about the badge was retrievable.'
- kind: url
  url: https://www.kickstarter.com/projects/751044629/855408834?ref=preview&token=148892cb
  title: Kickstarter preview link
  accessed: '2026-09-07'
  note: 'Preview link returned HTTP 403 (preview tokens require the creator''s session); could not confirm whether the campaign ever launched or what it offered.'
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched the Hackaday.io project page directly (curl) and confirmed the exact og:description/twitter:description text (Facebook, Twitter, Kickstarter-preview, PayPal links), the "created on 08/04/2017" date, and all four team members with matching hacker profile URLs (Kirball as project owner/id 237349, adamcwhooper/id 238022, a.a.Ron aka aaron/id 238040, gabriel licina/id 344798) via the page''s own HTML. Note: the page labels Kirball "Project owner" rather than the entry''s "project lead" wording -- treated as equivalent since Kirball is the sole listed creator. Re-fetched facebook.com/HackFSCJ (confirms org name "Hack@FSCJ" and Jacksonville, FL location only, no post content) and re-attempted the Kickstarter preview link and twitter.com/hackfscj, both still unreachable (403/redirect-blocked) so the campaign''s launch status remains unconfirmed. All remaining non-empty fields and body sentences are supported by these sources; nothing was found to contradict or required blanking. The page never grew past a stub (no build log, no badge photos, no specs, no price/quantity), so those fields stay empty and status stays "unknown" rather than listed/released. No matching event exists in events.yml for a Hack@FSCJ-specific event, so it stays filed under "other".'
last_modified_date: '2026-09-07'
---

Hack FSCJ (also styled Hack@FSCJ) was a student hacking/maker organization at Florida State College at Jacksonville that set up a Hackaday.io project page in August 2017 to promote a planned fundraiser PCB badge. The page names a four-person team — Kirball (project lead), adamcwhooper, a.a.Ron, and gabriel licina — and points to the group's Facebook and Twitter accounts, a PayPal donation button, and a "coming soon" Kickstarter preview link, but it was never filled out with a build log, photos, or technical specifications for the badge itself.

Because no design details, images, price, or confirmed distribution were ever published, it is not possible to say what the badge looked like, what chip or LEDs (if any) it used, or whether it was ever actually produced and sold. The Kickstarter preview link could not be verified as a launched campaign at time of research.
