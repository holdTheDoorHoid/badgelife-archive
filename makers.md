---
title: Makers
layout: default
nav_order: 3
---

# Makers

Every person, team, village and company with at least one entry in the archive. Click a name to see everything they made.

{%- assign listed = site.badges | where_exp: "e", "e.status != 'not_an_item'" %}
{%- assign names = "" | split: "" %}
{%- for e in listed %}{% for m in e.makers %}{% if m.name %}{% assign mn = m.name | append: "" %}{% assign names = names | push: mn %}{% endif %}{% endfor %}{% endfor %}
{%- assign uniq = names | uniq | sort_natural %}

<p class="muted">{{ uniq.size }} makers across {{ listed.size }} entries.</p>

<div class="ar-maker-list">
{%- for n in uniq %}
  {%- assign count = names | where_exp: "x", "x == n" | size %}
  {%- assign first = n | slice: 0 | upcase %}
  <a class="chip" href="{{ site.baseurl }}/badges/?maker={{ n | uri_escape }}">{{ n }} <span class="n">{{ count }}</span></a>
{%- endfor %}
</div>
