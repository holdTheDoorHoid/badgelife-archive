---
title: Home
layout: default
nav_order: 1
---

# Badgelife Archive

A historical, searchable record of the electronic badges and SAOs (Shitty Add-Ons) that people make for hacker conferences: what each one is, who made it, what it does, what it cost, how it was handed out, and, wherever the files exist, how to build one yourself.

This is a community fork of the [badge.life](https://badge.life/) website, run by the Badgelife Village. It is **not** the village's site; it grew out of the village's yearly badge spreadsheets and the wider community's project pages, and it tries to keep all of that from disappearing. Corrections, additions and takedown requests are welcome on [GitHub]({{ site.gh_edit_repository }}/issues). See [About]({{ site.baseurl }}/about/) for how entries are researched and credited.

{% assign n_all = site.badges | size %}
{% assign n_badges = site.badges | where: "type", "badge" | size %}
{% assign n_saos = site.badges | where: "type", "sao" | size %}
{% assign n_events = 0 %}
{% for pair in site.data.events %}{% assign c = site.badges | where: "event", pair[0] | size %}{% if c > 0 %}{% assign n_events = n_events | plus: 1 %}{% endif %}{% endfor %}

<form class="ar-toolbar home-search" action="{{ site.baseurl }}/badges/" method="get" role="search">
  <input type="search" name="q" placeholder="Search {{ n_all }} badges and SAOs — a name, a maker, a theme, a chip, a year…" aria-label="Search the archive">
  <button type="submit">Search</button>
</form>

<p class="muted">{{ n_all }} entries so far ({{ n_badges }} badges, {{ n_saos }} SAOs) across {{ n_events }} events. Entries marked <span class="chip chip-stub">stub</span> have not been researched yet.</p>

## Start here

- [**Search the archive**]({{ site.baseurl }}/badges/) — filter by event, type, maker, look, tech, price, availability, and whether design files exist.
- [**Browse by event**]({{ site.baseurl }}/badges/#browse-by-event) — every DEF CON from DC24 on, plus Supercon and other cons as they are added.
- [**Make your own**]({{ site.baseurl }}/specs/) — the SAO connector specs, [best practices]({{ site.baseurl }}/best_practices/) for color PCBs, light diffusion and low power, and [guides]({{ site.baseurl }}/guides/).
- [**Contribute**]({{ site.baseurl }}/contributing/) — add a badge, fix an entry, or send photos and design files.

## Recently updated

{% assign recent = site.badges | sort: "last_modified_date" | reverse %}
<div class="ar-grid ar-grid-static">
{%- for e in recent limit: 8 %}
  <a class="ar-card" href="{{ e.url | relative_url }}">
    <div class="ar-thumb">
      {%- if e.images and e.images.size > 0 %}<img src="{{ e.images[0].file | relative_url }}" alt="" loading="lazy">
      {%- else %}<div class="ar-noimg" aria-hidden="true">{% if e.type == 'sao' %}SAO{% elsif e.type == 'badge' %}BADGE{% else %}{{ e.type | upcase }}{% endif %}</div>{% endif %}
    </div>
    <div class="ar-card-body">
      <h3>{{ e.title }}</h3>
      <p class="ar-meta">{{ site.data.events[e.event].short | default: e.event }}{% if e.makers and e.makers.size > 0 %} · by {{ e.makers[0].name }}{% endif %}</p>
      <div class="ar-chips"><span class="chip chip-type chip-type-{{ e.type }}">{{ e.type }}</span>{% if e.research.status == "stub" %}<span class="chip chip-stub">stub</span>{% endif %}</div>
    </div>
  </a>
{%- endfor %}
</div>

## Where the data comes from

- The Badgelife Village's community badge sheets for [DEF CON 30](https://docs.google.com/spreadsheets/d/1cu99HozImdjNqTEM8iFsNzNswNw5De0Oe_hax3ywZ2U/edit?usp=sharing), [31](https://docs.google.com/spreadsheets/d/1ll9GVWq1jELk79OyfdalMrgccdF3AGo2qEQIxnKsXdY/edit?usp=sharing), [32](https://docs.google.com/spreadsheets/d/1POGyxIY4eBrXeD2hWqKz8fm9uuuy7yG1XwhVF1pnmzI/edit?usp=sharing), [33](https://docs.google.com/spreadsheets/d/1_eJnHTbvm-uhvslkRayfEJ99Z5agVZCl1GPqbFqwMFg/edit?usp=sharing) and [34](https://docs.google.com/spreadsheets/d/1wQ6J0tJiVCPgppxiPg_mM6mS6Il-jm3Ez1fj3a-7XRs/edit?usp=sharing), which makers fill in themselves each year.
- Makers' own project pages on Hackaday.io, GitHub, PCBWay, Tindie, Uberflux and their personal sites.
- The original badge.life Badge Archive pages, which are preserved here.

Every entry lists its sources at the bottom of the page. Photos are reproduced with credit and a link to where they came from; makers can ask for any to be removed.
