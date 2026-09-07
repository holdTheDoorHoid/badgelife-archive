---
title: DEFCON Subreddit SAO
id: dc31-defcon-subreddit-sao
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: MetaN3rd
summary: A trivia-prize SAO that maker MetaN3rd gave away to the r/Defcon subreddit meetup at DEF CON 31.
functions: Given as a prize for correctly answering a networking trivia question (which protocol uses port 69 -- TFTP) posted in the subreddit's DEF CON 31 get-together thread.
look:
  colors: []
  shape: null
  themes:
  - meme
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $15.00
  price_usd: 15.0
  quantity: ''
  availability: unknown
  distribution:
  - contest
  - free_drop
  where: 'Given free to the first 5 people who answered a trivia question (posted by MetaN3rd, base64-encoded, in the r/Defcon DEF CON 31 get-together thread) correctly; $15 appears to be a separate listed price on the community sheet, not what trivia winners paid.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: t.co/VkfMhE1Ifm
  url: https://t.co/VkfMhE1Ifm
  kind: website
- label: 'Def Con Subredit get together update 2 (Reddit, archived)'
  url: https://web.archive.org/web/20230729141203/https://old.reddit.com/r/Defcon/comments/15ctahk/def_con_subredit_get_together_update_2/
  kind: social
images: []
contact: {}
notes: []
status: listed
sources:
- kind: sheet
  event: dc31
  row: 59
  updated: ''
- kind: url
  url: https://t.co/VkfMhE1Ifm
  title: 'Def Con Subredit get together update 2 (redirect target)'
  accessed: '2026-09-07'
  note: 'The sheet link is a t.co shortlink that redirects to this Reddit gallery post by MetaN3rd; live Reddit is unreachable to this tool (network policy block), so it was read via the Wayback Machine instead.'
- kind: url
  url: https://web.archive.org/web/20230729141203/https://old.reddit.com/r/Defcon/comments/15ctahk/def_con_subredit_get_together_update_2/
  title: 'Def Con Subredit get together update 2 (archived, old.reddit)'
  accessed: '2026-09-07'
  note: 'Confirms author MetaN3rd; post itself is a 3-photo gallery of the DEF CON subreddit meetup with no caption text describing the SAO.'
- kind: url
  url: https://web.archive.org/web/20230729153217/https://old.reddit.com/r/Defcon/comments/15ctahk/def_con_subredit_get_together_update_2/jtyb0my/
  title: 'Comment thread on the same post (archived)'
  accessed: '2026-09-07'
  note: 'Base64-encoded comments by MetaN3rd: "What protocol uses port 69? The 1st 5 people to post the answer get a free SAO" -- answered correctly (TFTP) by another redditor within the thread.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    Live reddit.com and its image CDN (preview.redd.it) refused every fetch attempt from this tool
    (both the WebFetch tool and curl), as did Google, Bing, and DuckDuckGo, so this research relied
    on Wayback Machine snapshots of the old.reddit.com rendering of the post and its comment thread.
    The linked post itself (a photo gallery of the DEF CON 31 subreddit meetup, posted by MetaN3rd)
    has no caption describing the SAO. Digging into its archived comment thread turned up the actual
    mechanic: MetaN3rd posted a base64-encoded trivia question ("what protocol uses port 69") and
    promised a free SAO to the first 5 correct answers; TFTP was answered correctly in-thread. No
    photo of the physical SAO, no chip/LED/display specs, and no maker page (Hackaday.io, GitHub,
    storefront) could be found anywhere -- MetaN3rd does not appear to have any other project pages
    online under that handle. Left type/tech/look fields empty or minimal rather than guess. The
    sheet's $15 price could not be corroborated or explained beyond the free trivia-prize mechanic;
    flagged as a discrepancy in get_one.where rather than dropped. No images could be saved: the
    gallery images on the post are meetup snapshots, not photos of the SAO, and in any case the
    image host blocked every download attempt (403 Forbidden on preview.redd.it, and the Wayback
    Machine had not archived those specific image URLs/params). A separate entry
    (dc32-metan3rd-listed-for-def-con-32-no-details) already covers MetaN3rd's DEF CON 32 listing;
    this is not a duplicate of it, just the same maker in the following year.
last_modified_date: '2026-09-07'
---

MetaN3rd, a regular in the r/Defcon subreddit, gave away a small SAO as a trivia prize tied to the subreddit's DEF CON 31 meetup thread. Rather than announcing the badge directly, they posted a base64-encoded networking question -- "what protocol uses port 69?" -- in the thread and offered a free SAO to each of the first five people to answer correctly. Another attendee answered TFTP (Trivial File Transfer Protocol) in the thread shortly after, in classic hacker-jeopardy style.

Beyond that exchange, no further details about the SAO's design, electronics, or distribution volume are recoverable: the linked Reddit post is a bare 3-photo gallery of the meetup itself with no description, MetaN3rd does not appear to maintain a Hackaday.io, GitHub, or storefront presence under that handle, and this tool could not reach live Reddit, its image CDN, or any search engine to dig further. The community sheet lists a $15 price for the item, which does not obviously square with the "free to the first 5" mechanic described in the thread -- it may reflect a separate, non-contest listing that this research could not locate.
