---
title: Badge Archive
layout: default
nav_order: 2
has_children: true
has_toc: false
---

# Badge Archive

Every conference badge and SAO (Shitty Add-On) we have been able to document, going back to DEF CON 24. Search by anything you half-remember: a name, a maker, a color, a theme, the chip it used, or roughly what it cost. Filters on the left narrow things down; the grid updates as you type, and the page address updates too, so you can share a search.

Entries marked **stub** carry only what the community badge sheets listed for that year and have not been researched yet. Everything else has been researched from public sources; **verified** entries were cross-checked. See [how entries are researched]({{ site.baseurl }}/about/#how-entries-are-researched) and [how to contribute]({{ site.baseurl }}/contributing/).

<div id="archive-app" data-baseurl="{{ site.baseurl }}">
  <noscript><p>The interactive search needs JavaScript. You can still browse by event below.</p></noscript>
</div>
<script src="{{ '/assets/js/archive.js' | relative_url }}" defer></script>

## Browse by event

<ul class="ar-event-list">
{%- assign ev_ids = "" | split: "" %}
{%- for pair in site.data.events %}{% assign ev_ids = ev_ids | push: pair[0] %}{% endfor %}
{%- for id in ev_ids %}
  {%- assign ev = site.data.events[id] %}
  {%- assign n = site.badges | where: "event", id | size %}
  {%- if n > 0 or ev.family == "defcon" %}
  <li><a href="{{ site.baseurl }}/badges/{{ id }}/">{{ ev.name }}</a> <span class="n">{{ n }}</span></li>
  {%- endif %}
{%- endfor %}
</ul>
