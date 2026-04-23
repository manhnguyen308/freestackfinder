/* FreeStackFinder — search.js */

(function () {
  'use strict';

  var input = document.getElementById('search-input');
  var resultsEl = document.getElementById('search-results');
  var filterBtns = document.querySelectorAll('.filter-btn');

  if (!input || !resultsEl) return;

  var allPages = [];
  var activeFilter = '';

  function norm(s) {
    return (s || '').toLowerCase();
  }

  function escapeHtml(s) {
    return (s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function highlight(text, query) {
    if (!query) return escapeHtml(text);
    var safe = escapeHtml(text);
    var safeQ = escapeHtml(query);
    var idx = norm(safe).indexOf(norm(safeQ));
    if (idx === -1) return safe;
    return safe.slice(0, idx) +
      '<mark>' + safe.slice(idx, idx + safeQ.length) + '</mark>' +
      safe.slice(idx + safeQ.length);
  }

  function render(results, query) {
    var q = (query || '').trim();
    if (!q && !activeFilter) {
      resultsEl.innerHTML = '<p class="search-prompt">Type above to search all ' + allPages.length + ' guides.</p>';
      return;
    }
    if (!results.length) {
      resultsEl.innerHTML = '<p class="search-empty">No results found. Try a different term or clear the filter.</p>';
      return;
    }
    var count = '<p class="search-count">' + results.length + ' result' + (results.length !== 1 ? 's' : '') + '</p>';
    var items = results.map(function (p) {
      return '<li class="search-result-item">' +
        '<span class="search-result-cat">' + escapeHtml(p.category || p.section || '') + '</span>' +
        '<h3><a href="' + escapeHtml(p.url) + '">' + highlight(p.title, q) + '</a></h3>' +
        '<p>' + highlight(p.description, q) + '</p>' +
        '</li>';
    }).join('');
    resultsEl.innerHTML = count + '<ul class="search-results-list">' + items + '</ul>';
  }

  function runSearch() {
    var q = norm(input.value);
    var filtered = allPages.filter(function (p) {
      var matchQ = !q || norm(p.title).indexOf(q) !== -1 || norm(p.description).indexOf(q) !== -1;
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
