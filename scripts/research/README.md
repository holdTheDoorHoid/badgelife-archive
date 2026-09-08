# Stub research pass (resumable)

State lives only in the entry files: an entry is pending while `research.status: stub`.

1. `python3 scripts/research_queue.py --summary` — how many remain.
2. `python3 scripts/research_queue.py --next 60 | tr '\n' ' '` — the next batch of ids (priority order).
3. Launch the Workflow tool with `scripts/research/wf_research_stubs.js` and args
   `{"today": "<ISO date>", "ids": "<those ids>", "events": "<output of: ls _badges | tr '\n' ' '>"}`.
   Sonnet, medium effort, ~8 fetch/search calls per entry, sampled fact-check. About 80k Sonnet
   tokens per entry; a batch of 60 is roughly 5M tokens and 35-45 minutes.
4. When it finishes: `python3 scripts/research/post_batch.py <workflow transcript dir> --next 60`
   merges reported duplicates, saves other-item finds to `data/research_others.json`, relocates
   corrected entries, validates, regenerates event pages and `data/existing_titles.txt`, and writes
   the next batch to `data/next_batch.txt`. Check its SKIP lines for pairs it could not merge.
5. The publisher loop (or a manual commit + `gh workflow run jekyll.yml`) publishes.

Agents must not call the built-in WebSearch tool (per-session cap); they use `scripts/websearch.py`.
