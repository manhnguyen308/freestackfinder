/* FreeStackFinder: search.js */

(function () {
  'use strict';

  var input = document.getElementById('search-input');
  var resultsEl = document.getElementById('search-results');
  var filterBtns = document.querySelectorAll('.filter-btn');

  if (!input || !resultsEl) return;

  var allPages = [];
  var activeFilter = '';

  var MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];

  function norm(s) {
    return (s || '').toLowerCase();
  }

  function escapeHtml(s) {
    return (s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function formatDate(iso) {
    var parts = (iso || '').split('-');
    if (parts.length !== 3) return '';
    return MONTHS[parseInt(parts[1], 10) - 1] + ' ' + parseInt(parts[2], 10) + ', ' + parts[0];
  }

  // Split a query into words so "vpn free" matches "Free VPN" as well as "free vpn"
  function terms(query) {
    return norm(query).split(/\s+/).filter(Boolean);
  }

  // Marks every place a query word appears. Matching runs on the raw text and
  // each piece is escaped afterwards, so a mark can never land inside an entity.
  function highlight(text, query) {
    text = text || '';
    var words = terms(query);
    if (!words.length) return escapeHtml(text);
    var lower = norm(text);
    var marked = new Array(text.length);
    words.forEach(function (w) {
      var from = 0, idx;
      while ((idx = lower.indexOf(w, from)) !== -1) {
        for (var i = idx; i < idx + w.length; i++) marked[i] = true;
        from = idx + w.length;
      }
    });
    var out = '', i = 0;
    while (i < text.length) {
      var j = i;
      while (j < text.length && !!marked[j] === !!marked[i]) j++;
      var piece = escapeHtml(text.slice(i, j));
      out += marked[i] ? '<mark>' + piece + '</mark>' : piece;
      i = j;
    }
    return out;
  }

  function render(results, query) {
    var q = (query || '').trim();
    if (!q && !activeFilter) {
      // The index also holds About, Contact, and the legal pages, which are not guides
      var guideCount = allPages.filter(function (p) { return p.category; }).length;
      resultsEl.innerHTML = '<p class="search-prompt">Type above to search all ' + guideCount + ' guides.</p>';
      return;
    }
    if (!results.length) {
      resultsEl.innerHTML = '<p class="search-empty">No results found. Try a different term or clear the filter.</p>';
      return;
    }
    var count = '<p class="search-count">' + results.length + ' result' + (results.length !== 1 ? 's' : '') + '</p>';
    var items = results.map(function (p) {
      var isUpdated = p.lastmod && p.date && p.lastmod !== p.date;
      var dateLabel = isUpdated
        ? '<span class="search-result-date search-result-date--updated">Updated ' + escapeHtml(formatDate(p.lastmod)) + '</span>'
        : (p.date ? '<span class="search-result-date">Published ' + escapeHtml(formatDate(p.date)) + '</span>' : '');
      return '<li class="search-result-item">' +
        '<span class="search-result-cat">' + escapeHtml(p.category || p.section || '') + '</span>' +
        '<h3><a href="' + escapeHtml(p.url) + '">' + highlight(p.title, q) + '</a></h3>' +
        '<p class="search-result-desc">' + highlight(p.description, q) + '</p>' +
        dateLabel +
        '</li>';
    }).join('');
    resultsEl.innerHTML = count + '<ul class="search-results-list">' + items + '</ul>';
  }

  function runSearch() {
    var words = terms(input.value);
    var filtered = allPages.filter(function (p) {
      var haystack = norm([p.title, p.description, p.category].join(' '));
      var matchQ = words.every(function (w) { return haystack.indexOf(w) !== -1; });
      var matchF = !activeFilter || norm(p.category) === norm(activeFilter);
      return matchQ && matchF;
    });
    render(filtered, input.value);
  }

  var debounceTimer;
  input.addEventListener('input', function () {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(runSearch, 150);
  });

  filterBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      filterBtns.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      activeFilter = btn.getAttribute('data-filter') || '';
      runSearch();
    });
  });

  var initQ = new URLSearchParams(window.location.search).get('q') || '';

  fetch('/index.json')
    .then(function (r) { return r.json(); })
    .then(function (data) {
      allPages = data;
      if (initQ) { input.value = initQ; }
      runSearch();
    })
    .catch(function () {
      resultsEl.innerHTML = '<p class="search-empty">Search index could not be loaded.</p>';
    });

})();
