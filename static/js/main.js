/* SwitchForFree — main.js */

(function () {
  'use strict';

  // Mobile navigation toggle
  var toggle = document.getElementById('nav-toggle');
  var nav = document.getElementById('main-nav');

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var isOpen = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(isOpen));
    });

    // Close nav when clicking outside
    document.addEventListener('click', function (e) {
      if (nav.classList.contains('open') && !nav.contains(e.target) && !toggle.contains(e.target)) {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });

    // Close nav when pressing Escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  // Sticky sidebar for article pages
  var sidebar = document.querySelector('.article-sidebar');
  if (sidebar && window.innerWidth >= 960) {
    sidebar.style.position = 'sticky';
    sidebar.style.top = '80px';
  }

  // Add table wrappers for horizontal scroll on mobile
  var articleContent = document.querySelector('.article-content');
  if (articleContent) {
    var tables = articleContent.querySelectorAll('table');
    tables.forEach(function (table) {
      if (!table.parentElement.classList.contains('table-wrap')) {
        var wrapper = document.createElement('div');
        wrapper.className = 'table-wrap';
        table.parentNode.insertBefore(wrapper, table);
        wrapper.appendChild(table);
      }
    });
  }

  // Smooth scroll for TOC links
  var tocLinks = document.querySelectorAll('.toc-widget a[href^="#"]');
  tocLinks.forEach(function (link) {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      var target = document.querySelector(this.getAttribute('href'));
      if (target) {
        var offset = 80; // header height
        var top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top: top, behavior: 'smooth' });
      }
    });
  });

  // Highlight active TOC link on scroll
  var headings = document.querySelectorAll('.article-content h2, .article-content h3');
  var tocLinksAll = document.querySelectorAll('.toc-widget a');
  if (headings.length && tocLinksAll.length) {
    window.addEventListener('scroll', function () {
      var scrollY = window.scrollY + 100;
      var active = null;
      headings.forEach(function (h) {
        if (h.offsetTop <= scrollY) active = h;
      });
      tocLinksAll.forEach(function (l) { l.style.color = ''; l.style.fontWeight = ''; });
      if (active) {
        var id = active.getAttribute('id');
        if (id) {
          var activeLink = document.querySelector('.toc-widget a[href="#' + id + '"]');
          if (activeLink) {
            activeLink.style.color = '#0F766E';
            activeLink.style.fontWeight = '600';
          }
        }
      }
    }, { passive: true });
  }

})();
