/* Badgelife Archive — faceted search over assets/data/badges.json.
   Vanilla JS, no dependencies. State lives in the URL query string so searches are shareable. */
(function () {
  'use strict';
  var root = document.getElementById('archive-app');
  if (!root) return;
  var BASE = root.getAttribute('data-baseurl') || '';
  var DATA_URL = BASE + '/assets/data/badges.json';

  // ---- facet definitions -------------------------------------------------
  var FACETS = [
    { key: 'event',    label: 'Event',            field: 'event',        group: 'basics' },
    { key: 'type',     label: 'Type',             field: 'type',         group: 'basics' },
    { key: 'maker',    label: 'Maker',            field: 'makers',       group: 'basics', searchable: true },
    { key: 'theme',    label: 'Theme',            field: 'themes',       group: 'look', searchable: true },
    { key: 'color',    label: 'Color',            field: 'colors',       group: 'look' },
    { key: 'shape',    label: 'Shape',            field: 'shape',        group: 'look' },
    { key: 'form',     label: 'Form factor',      field: 'form_factor',  group: 'look' },
    { key: 'mcu',      label: 'Microcontroller',  field: 'mcu',          group: 'tech', searchable: true },
    { key: 'conn',     label: 'Connectivity',     field: 'connectivity', group: 'tech' },
    { key: 'display',  label: 'Display',          field: 'display',      group: 'tech' },
    { key: 'ledtype',  label: 'LED type',         field: 'led_type',     group: 'tech' },
    { key: 'sao',      label: 'SAO connector',    field: 'sao_version',  group: 'tech' },
    { key: 'battery',  label: 'Battery / power',  field: 'battery',      group: 'tech' },
    { key: 'avail',    label: 'Availability',     field: 'availability', group: 'get' },
    { key: 'dist',     label: 'Distributed via',  field: 'distribution', group: 'get' },
    { key: 'oss',      label: 'Open source',      field: 'open_source',  group: 'make' },
    { key: 'eda',      label: 'Designed in',      field: 'eda_tool',     group: 'make' },
    { key: 'research', label: 'Research status',  field: 'research',     group: 'meta' },
    { key: 'status',   label: 'Listing status',   field: 'status',       group: 'meta' }
  ];
  var GROUPS = [
    { id: 'basics', label: 'Basics' },
    { id: 'look',   label: 'Look & theme' },
    { id: 'tech',   label: 'Tech details' },
    { id: 'get',    label: 'How to get one' },
    { id: 'make',   label: 'Make your own' },
    { id: 'meta',   label: 'Archive status' }
  ];
  var FLAGS = [
    { key: 'photos',  label: 'Has photos',         test: function (r) { return r.image_count > 0; } },
    { key: 'hw',      label: 'Has hardware files', test: function (r) { return r.has_hardware; } },
    { key: 'model',   label: 'Has 3D model',       test: function (r) { return r.has_model; } },
    { key: 'fw',      label: 'Has firmware',       test: function (r) { return r.has_firmware; } },
    { key: 'gerbers', label: 'Has gerbers',        test: function (r) { return r.has_gerbers; } },
    { key: 'bom',     label: 'Has BOM',            test: function (r) { return r.has_bom; } },
    { key: 'links',   label: 'Has any links',      test: function (r) { return r.link_count > 0; } },
    { key: 'priced',  label: 'Has a price',        test: function (r) { return r.price_usd !== null && r.price_usd !== undefined; } }
  ];
  var SORTS = {
    'newest': function (a, b) { return (b.year || 0) - (a.year || 0) || cmp(a.title, b.title); },
    'oldest': function (a, b) { return (a.year || 0) - (b.year || 0) || cmp(a.title, b.title); },
    'title':  function (a, b) { return cmp(a.title, b.title); },
    'maker':  function (a, b) { return cmp((a.makers[0] || '~'), (b.makers[0] || '~')) || cmp(a.title, b.title); },
    'price-asc':  function (a, b) { return num(a.price_usd, 1e9) - num(b.price_usd, 1e9) || cmp(a.title, b.title); },
    'price-desc': function (a, b) { return num(b.price_usd, -1) - num(a.price_usd, -1) || cmp(a.title, b.title); },
    'relevance': null
  };
  function cmp(a, b) { a = String(a || '').toLowerCase(); b = String(b || '').toLowerCase(); return a < b ? -1 : a > b ? 1 : 0; }
  function num(v, d) { return (v === null || v === undefined || isNaN(v)) ? d : Number(v); }

  // ---- state <-> URL ------------------------------------------------------
  var state = { q: '', sort: 'newest', view: 'grid', pmin: '', pmax: '', flags: {}, f: {} };
  function readURL() {
    var p = new URLSearchParams(location.search);
    state.q = p.get('q') || '';
    state.sort = p.get('sort') || (state.q ? 'relevance' : 'newest');
    state.view = p.get('view') || 'grid';
    state.pmin = p.get('pmin') || ''; state.pmax = p.get('pmax') || '';
    state.flags = {}; (p.get('has') || '').split(',').filter(Boolean).forEach(function (k) { state.flags[k] = true; });
    state.f = {};
    FACETS.forEach(function (f) { var v = p.getAll(f.key); if (v.length) state.f[f.key] = v; });
  }
  function writeURL() {
    var p = new URLSearchParams();
    if (state.q) p.set('q', state.q);
    if (state.sort && state.sort !== 'newest') p.set('sort', state.sort);
    if (state.view !== 'grid') p.set('view', state.view);
    if (state.pmin) p.set('pmin', state.pmin); if (state.pmax) p.set('pmax', state.pmax);
    var has = Object.keys(state.flags).filter(function (k) { return state.flags[k]; });
    if (has.length) p.set('has', has.join(','));
    FACETS.forEach(function (f) { (state.f[f.key] || []).forEach(function (v) { p.append(f.key, v); }); });
    var qs = p.toString();
    history.replaceState(null, '', location.pathname + (qs ? '?' + qs : ''));
  }

  // ---- search -------------------------------------------------------------
  function norm(s) { return String(s || '').toLowerCase().normalize('NFKD').replace(/[̀-ͯ]/g, ''); }
  function tokens(s) { return norm(s).split(/[^a-z0-9+#.]+/).filter(function (t) { return t.length > 0; }); }
  function prepare(r) {
    r._title = norm(r.title);
    r._makers = norm(r.makers.join(' '));
    r._tags = norm([r.themes.join(' '), r.colors.join(' '), r.shape, r.form_factor, r.type, r.event, r.event_name, r.year].join(' '));
    r._tech = norm([r.mcu, r.connectivity.join(' '), r.display, r.led_type, r.sao_version, r.battery, r.eda_tool].join(' '));
    r._text = norm([r.summary, r.functions, r.text, r.price, r.availability, r.distribution.join(' ')].join(' '));
    r._all = [r._title, r._makers, r._tags, r._tech, r._text].join(' | ');
  }
  function score(r, toks) {
    var total = 0;
    for (var i = 0; i < toks.length; i++) {
      var t = toks[i], s = 0;
      if (r._title.indexOf(t) >= 0) s += (r._title === t ? 20 : r._title.indexOf(t) === 0 ? 12 : 8);
      if (r._makers.indexOf(t) >= 0) s += 6;
      if (r._tags.indexOf(t) >= 0) s += 5;
      if (r._tech.indexOf(t) >= 0) s += 4;
      if (r._text.indexOf(t) >= 0) s += 2;
      if (s === 0) {
        // forgiving match: token as a prefix of any word, or 1-char typo for words >= 5 chars
        var words = r._all.split(/[^a-z0-9+#.]+/), hit = false;
        for (var w = 0; w < words.length && !hit; w++) {
          var word = words[w];
          if (t.length >= 3 && word.indexOf(t) === 0) hit = true;
          else if (t.length >= 5 && Math.abs(word.length - t.length) <= 1 && editDistance1(word, t)) hit = true;
        }
        if (!hit) return 0;
        s = 1;
      }
      total += s;
    }
    return total;
  }
  function editDistance1(a, b) {
    if (a === b) return true;
    if (Math.abs(a.length - b.length) > 1) return false;
    var i = 0, j = 0, edits = 0;
    while (i < a.length && j < b.length) {
      if (a[i] === b[j]) { i++; j++; continue; }
      if (++edits > 1) return false;
      if (a.length > b.length) i++; else if (a.length < b.length) j++; else { i++; j++; }
    }
    return edits + (a.length - i) + (b.length - j) <= 1;
  }
  function valuesOf(r, field) {
    var v = r[field];
    if (Array.isArray(v)) return v.map(String).filter(Boolean);
    if (v === null || v === undefined || v === '') return [];
    return [String(v)];
  }
  function passesFacet(r, f, selected) {
    if (!selected || !selected.length) return true;
    var vals = valuesOf(r, f.field).map(norm);
    for (var i = 0; i < selected.length; i++) if (vals.indexOf(norm(selected[i])) >= 0) return true;
    return false;
  }
  function applyFilters(all, skipKey) {
    var toks = tokens(state.q), out = [];
    var pmin = state.pmin === '' ? null : Number(state.pmin), pmax = state.pmax === '' ? null : Number(state.pmax);
    for (var i = 0; i < all.length; i++) {
      var r = all[i], ok = true;
      for (var j = 0; j < FACETS.length && ok; j++) {
        var f = FACETS[j]; if (f.key === skipKey) continue;
        ok = passesFacet(r, f, state.f[f.key]);
      }
      if (!ok) continue;
      if (skipKey !== '__flags') for (var k = 0; k < FLAGS.length && ok; k++) if (state.flags[FLAGS[k].key] && !FLAGS[k].test(r)) ok = false;
      if (!ok) continue;
      if (pmin !== null && !(r.price_usd !== null && r.price_usd !== undefined && r.price_usd >= pmin)) continue;
      if (pmax !== null && !(r.price_usd !== null && r.price_usd !== undefined && r.price_usd <= pmax)) continue;
      if (toks.length) { var s = score(r, toks); if (!s) continue; r._score = s; } else r._score = 0;
      out.push(r);
    }
    return out;
  }

  // ---- rendering ----------------------------------------------------------
  function esc(s) { return String(s === null || s === undefined ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function label(f, v) {
    if (f.key === 'event' && DATA.eventNames[v]) return DATA.eventNames[v];
    return String(v).replace(/_/g, ' ');
  }
  var DATA = { entries: [], eventNames: {}, eventYear: {} };
  var els = {};

  function buildShell() {
    root.innerHTML =
      '<div class="ar-toolbar">' +
      '  <input id="ar-q" type="search" placeholder="Search by name, maker, theme, chip, year…" autocomplete="off" aria-label="Search the archive">' +
      '  <select id="ar-sort" aria-label="Sort results">' +
      '    <option value="relevance">Best match</option><option value="newest">Newest first</option><option value="oldest">Oldest first</option>' +
      '    <option value="title">Title A–Z</option><option value="maker">Maker A–Z</option><option value="price-asc">Price low→high</option><option value="price-desc">Price high→low</option>' +
      '  </select>' +
      '  <div class="ar-view"><button type="button" data-view="grid" aria-label="Grid view">▦</button><button type="button" data-view="list" aria-label="List view">☰</button></div>' +
      '  <button type="button" id="ar-toggle-facets" class="ar-mobile-only">Filters</button>' +
      '</div>' +
      '<div class="ar-body">' +
      '  <aside id="ar-facets" class="ar-facets" aria-label="Filters"></aside>' +
      '  <main class="ar-results"><div id="ar-summary" class="ar-summary" aria-live="polite"></div><div id="ar-active" class="ar-active"></div><div id="ar-list"></div></main>' +
      '</div>';
    els.q = document.getElementById('ar-q'); els.sort = document.getElementById('ar-sort');
    els.facets = document.getElementById('ar-facets'); els.list = document.getElementById('ar-list');
    els.summary = document.getElementById('ar-summary'); els.active = document.getElementById('ar-active');
    els.q.value = state.q; els.sort.value = state.sort;
    var t; els.q.addEventListener('input', function () { clearTimeout(t); t = setTimeout(function () { state.q = els.q.value.trim(); if (state.q && state.sort === 'newest') { state.sort = 'relevance'; els.sort.value = 'relevance'; } render(); }, 120); });
    els.sort.addEventListener('change', function () { state.sort = els.sort.value; render(); });
    root.querySelectorAll('.ar-view button').forEach(function (b) { b.addEventListener('click', function () { state.view = b.getAttribute('data-view'); render(); }); });
    document.getElementById('ar-toggle-facets').addEventListener('click', function () { els.facets.classList.toggle('open'); });
  }

  function facetCounts(all, f) {
    var subset = applyFilters(all, f.key), counts = {};
    subset.forEach(function (r) { valuesOf(r, f.field).forEach(function (v) { counts[v] = (counts[v] || 0) + 1; }); });
    return counts;
  }
  var expanded = {};
  function renderFacets(all) {
    var html = '';
    // price range + flags first (they don't fit the value-list pattern)
    html += '<details class="ar-group" open><summary>How to get one</summary>' +
      '<div class="ar-price"><label>Price $<input id="ar-pmin" type="number" min="0" placeholder="min" value="' + esc(state.pmin) + '"></label> – <label>$<input id="ar-pmax" type="number" min="0" placeholder="max" value="' + esc(state.pmax) + '"></label></div>';
    html += facetBlock(all, byKey('avail')) + facetBlock(all, byKey('dist')) + '</details>';
    GROUPS.forEach(function (g) {
      if (g.id === 'get') return;
      var inner = '';
      FACETS.forEach(function (f) { if (f.group === g.id) inner += facetBlock(all, f); });
      if (g.id === 'make' || g.id === 'meta') {
        var flagsSubset = applyFilters(all, '__flags');
        inner += '<div class="ar-facet"><h4>' + (g.id === 'make' ? 'Files & media' : 'Completeness') + '</h4><ul>';
        FLAGS.forEach(function (fl) {
          if (g.id === 'make' && ['photos', 'links', 'priced'].indexOf(fl.key) >= 0) return;
          if (g.id === 'meta' && ['hw', 'fw', 'gerbers', 'bom'].indexOf(fl.key) >= 0) return;
          var n = flagsSubset.filter(fl.test).length;
          inner += '<li><label><input type="checkbox" data-flag="' + fl.key + '"' + (state.flags[fl.key] ? ' checked' : '') + '> ' + esc(fl.label) + ' <span class="n">' + n + '</span></label></li>';
        });
        inner += '</ul></div>';
      }
      html += '<details class="ar-group"' + (g.id === 'basics' || g.id === 'look' ? ' open' : '') + '><summary>' + esc(g.label) + '</summary>' + inner + '</details>';
    });
    els.facets.innerHTML = html;
    els.facets.querySelectorAll('input[type=checkbox][data-facet]').forEach(function (cb) {
      cb.addEventListener('change', function () {
        var k = cb.getAttribute('data-facet'), v = cb.getAttribute('data-value'), cur = state.f[k] || [];
        if (cb.checked) { if (cur.indexOf(v) < 0) cur.push(v); } else cur = cur.filter(function (x) { return x !== v; });
        if (cur.length) state.f[k] = cur; else delete state.f[k];
        render();
      });
    });
    els.facets.querySelectorAll('input[type=checkbox][data-flag]').forEach(function (cb) {
      cb.addEventListener('change', function () { state.flags[cb.getAttribute('data-flag')] = cb.checked; render(); });
    });
    els.facets.querySelectorAll('.ar-more').forEach(function (b) { b.addEventListener('click', function () { expanded[b.getAttribute('data-facet')] = !expanded[b.getAttribute('data-facet')]; render(); }); });
    els.facets.querySelectorAll('.ar-facet-search').forEach(function (inp) {
      inp.addEventListener('input', function () {
        var q = norm(inp.value), ul = inp.parentNode.querySelector('ul');
        ul.querySelectorAll('li').forEach(function (li) { li.style.display = (!q || norm(li.textContent).indexOf(q) >= 0) ? '' : 'none'; });
      });
    });
    var pm = document.getElementById('ar-pmin'), px = document.getElementById('ar-pmax'), pt;
    [pm, px].forEach(function (i) { i.addEventListener('input', function () { clearTimeout(pt); pt = setTimeout(function () { state.pmin = pm.value; state.pmax = px.value; render(); }, 250); }); });
  }
  function byKey(k) { for (var i = 0; i < FACETS.length; i++) if (FACETS[i].key === k) return FACETS[i]; }
  function facetBlock(all, f) {
    var counts = facetCounts(all, f), sel = state.f[f.key] || [];
    var vals = Object.keys(counts);
    if (!vals.length && !sel.length) return '';
    if (f.key === 'event') vals.sort(function (a, b) { return (DATA.eventYear[b] || 0) - (DATA.eventYear[a] || 0) || cmp(a, b); });
    else vals.sort(function (a, b) { return (sel.indexOf(b) >= 0) - (sel.indexOf(a) >= 0) || counts[b] - counts[a] || cmp(a, b); });
    var limit = expanded[f.key] ? 1000 : 10, html = '<div class="ar-facet"><h4>' + esc(f.label) + '</h4>';
    if (f.searchable && vals.length > 10) html += '<input type="search" class="ar-facet-search" placeholder="filter ' + esc(f.label.toLowerCase()) + 's…" aria-label="Filter ' + esc(f.label) + ' values">';
    html += '<ul>';
    vals.slice(0, limit).forEach(function (v) {
      html += '<li><label><input type="checkbox" data-facet="' + esc(f.key) + '" data-value="' + esc(v) + '"' + (sel.indexOf(v) >= 0 ? ' checked' : '') + '> ' + esc(label(f, v)) + ' <span class="n">' + counts[v] + '</span></label></li>';
    });
    html += '</ul>';
    if (vals.length > limit) html += '<button type="button" class="ar-more" data-facet="' + esc(f.key) + '">show all ' + vals.length + '</button>';
    else if (expanded[f.key] && vals.length > 10) html += '<button type="button" class="ar-more" data-facet="' + esc(f.key) + '">show fewer</button>';
    return html + '</div>';
  }
  function renderActive() {
    var chips = [];
    FACETS.forEach(function (f) { (state.f[f.key] || []).forEach(function (v) { chips.push({ t: f.label + ': ' + label(f, v), k: f.key, v: v }); }); });
    FLAGS.forEach(function (fl) { if (state.flags[fl.key]) chips.push({ t: fl.label, flag: fl.key }); });
    if (state.pmin || state.pmax) chips.push({ t: 'Price ' + (state.pmin ? '≥ $' + state.pmin : '') + (state.pmin && state.pmax ? ' and ' : '') + (state.pmax ? '≤ $' + state.pmax : ''), price: true });
    if (!chips.length) { els.active.innerHTML = ''; return; }
    els.active.innerHTML = chips.map(function (c, i) { return '<button type="button" class="ar-chip" data-i="' + i + '">' + esc(c.t) + ' ✕</button>'; }).join('') + '<button type="button" class="ar-chip ar-clear">Clear all</button>';
    els.active.querySelectorAll('.ar-chip[data-i]').forEach(function (b) {
      b.addEventListener('click', function () {
        var c = chips[Number(b.getAttribute('data-i'))];
        if (c.flag) delete state.flags[c.flag];
        else if (c.price) { state.pmin = ''; state.pmax = ''; }
        else { state.f[c.k] = (state.f[c.k] || []).filter(function (x) { return x !== c.v; }); if (!state.f[c.k].length) delete state.f[c.k]; }
        render();
      });
    });
    els.active.querySelector('.ar-clear').addEventListener('click', function () { state.f = {}; state.flags = {}; state.pmin = ''; state.pmax = ''; render(); });
  }
  function card(r) {
    var img = r.thumb ? '<img src="' + esc(BASE + '/' + r.thumb.replace(/^\//, '')) + '" alt="" loading="lazy">' : '<div class="ar-noimg" aria-hidden="true">' + esc(r.type === 'sao' ? 'SAO' : r.type === 'badge' ? 'BADGE' : (r.type || '?').toUpperCase()) + '</div>';
    var meta = [r.event_name, r.makers.length ? 'by ' + r.makers.join(', ') : ''].filter(Boolean).join(' · ');
    var chips = '<span class="chip chip-type chip-type-' + esc(r.type) + '">' + esc(r.type.replace(/_/g, ' ')) + '</span>';
    if (r.availability && r.availability !== 'unknown') chips += '<span class="chip chip-avail chip-avail-' + esc(r.availability) + '">' + esc(r.availability.replace(/_/g, ' ')) + '</span>';
    if (r.price) chips += '<span class="chip">' + esc(r.price) + '</span>';
    if (r.open_source === 'true' || r.open_source === 'yes') chips += '<span class="chip chip-oss">open source</span>';
    if (r.research === 'stub') chips += '<span class="chip chip-stub" title="Only what the community sheet listed">stub</span>';
    var blurb = r.summary || r.functions || '';
    if (blurb.length > 160) blurb = blurb.slice(0, 157) + '…';
    return '<a class="ar-card" href="' + esc(BASE + r.url) + '">' +
      '<div class="ar-thumb">' + img + '</div>' +
      '<div class="ar-card-body"><h3>' + esc(r.title) + '</h3><p class="ar-meta">' + esc(meta) + '</p>' +
      (blurb ? '<p class="ar-blurb">' + esc(blurb) + '</p>' : '') +
      '<div class="ar-chips">' + chips + '</div></div></a>';
  }
  function row(r) {
    return '<tr><td><a href="' + esc(BASE + r.url) + '">' + esc(r.title) + '</a></td><td>' + esc(r.type) + '</td><td>' + esc(r.event_name) + '</td><td>' + esc(r.makers.join(', ')) + '</td><td>' + esc(r.price || '') + '</td><td>' + esc((r.availability || '').replace(/_/g, ' ')) + '</td><td>' + esc(r.mcu || '') + '</td><td>' + esc(r.research) + '</td></tr>';
  }
  var PAGE = 60, shown = PAGE;
  function render() {
    writeURL();
    var res = applyFilters(DATA.entries);
    var sorter = SORTS[state.sort] || SORTS.newest;
    if (state.sort === 'relevance') res.sort(function (a, b) { return (b._score - a._score) || ((b.year || 0) - (a.year || 0)) || cmp(a.title, b.title); });
    else res.sort(sorter);
    renderFacets(DATA.entries);
    renderActive();
    els.summary.textContent = 'Showing ' + Math.min(shown, res.length) + ' of ' + res.length + ' entries' + (res.length !== DATA.entries.length ? ' (' + DATA.entries.length + ' total)' : '');
    root.querySelectorAll('.ar-view button').forEach(function (b) { b.classList.toggle('active', b.getAttribute('data-view') === state.view); });
    if (!res.length) { els.list.innerHTML = '<p class="ar-empty">Nothing matches. Try fewer filters, a shorter search, or a different spelling.</p>'; return; }
    var slice = res.slice(0, shown);
    if (state.view === 'list') {
      els.list.innerHTML = '<div class="table-scroll"><table class="ar-table"><thead><tr><th>Title</th><th>Type</th><th>Event</th><th>Maker</th><th>Price</th><th>Availability</th><th>MCU</th><th>Research</th></tr></thead><tbody>' + slice.map(row).join('') + '</tbody></table></div>';
    } else {
      els.list.innerHTML = '<div class="ar-grid">' + slice.map(card).join('') + '</div>';
    }
    if (res.length > shown) {
      var more = document.createElement('button'); more.type = 'button'; more.className = 'ar-more-results'; more.textContent = 'Show more (' + (res.length - shown) + ' remaining)';
      more.addEventListener('click', function () { shown += PAGE; render(); });
      els.list.appendChild(more);
    }
  }

  // ---- boot ---------------------------------------------------------------
  readURL();
  buildShell();
  els.list.innerHTML = '<p class="ar-empty">Loading the archive…</p>';
  fetch(DATA_URL).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }).then(function (data) {
    DATA.entries = data.entries || [];
    (data.facets && data.facets.events || []).forEach(function (e) { DATA.eventNames[e.id] = e.short || e.name; DATA.eventYear[e.id] = e.year; });
    DATA.entries.forEach(prepare);
    render();
  }).catch(function (e) {
    els.list.innerHTML = '<p class="ar-empty">Could not load the archive index (' + esc(e.message) + '). The site may still be building.</p>';
  });
  window.addEventListener('popstate', function () { readURL(); els.q.value = state.q; els.sort.value = state.sort; render(); });
})();
