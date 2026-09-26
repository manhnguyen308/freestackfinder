/* FreeStackFinder: main.js */

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

  // Light/dark theme toggle. head.html sets data-theme before first paint;
  // this keeps the button state and the saved choice in step with it.
  var themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    var root = document.documentElement;

    var applyTheme = function (theme) {
      var isDark = theme === 'dark';
      root.setAttribute('data-theme', theme);
      themeToggle.setAttribute('aria-pressed', String(isDark));
      themeToggle.setAttribute('title', isDark ? 'Switch to light mode' : 'Switch to dark mode');
    };

    var savedTheme = function () {
      try { return localStorage.getItem('theme'); } catch (e) { return null; }
    };

    applyTheme(root.getAttribute('data-theme') === 'dark' ? 'dark' : 'light');

    themeToggle.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      applyTheme(next);
      try { localStorage.setItem('theme', next); } catch (e) {}
    });

    // Follow system changes until the reader picks a theme
    var darkQuery = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;
    if (darkQuery && darkQuery.addEventListener) {
      darkQuery.addEventListener('change', function (e) {
        var saved = savedTheme();
        if (saved !== 'light' && saved !== 'dark') applyTheme(e.matches ? 'dark' : 'light');
      });
    }
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
      // Look up by id: numbered tool headings get ids like "1-best-offline-suite",
      // which are not valid CSS selectors and made querySelector throw.
      var target = document.getElementById(decodeURIComponent(this.getAttribute('href').slice(1)));
      if (target) {
        e.preventDefault();
        var offset = 80; // header height
        var top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top: top, behavior: 'smooth' });
      }
    });
  });

  // Highlight active TOC link on scroll
  var headings = document.querySelectorAll('.article-content h2, .article-content h3');
  var tocLinksAll = document.querySelectorAll('.toc-widget a');
  var sidebar = document.querySelector('.article-sidebar');
  var lastActiveLink = null;
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
            activeLink.style.color = 'var(--primary)';
            activeLink.style.fontWeight = '600';
            // When the sticky sidebar scrolls on its own, keep the current section in view
            if (activeLink !== lastActiveLink && sidebar && sidebar.scrollHeight > sidebar.clientHeight) {
              var linkBox = activeLink.getBoundingClientRect();
              var sidebarBox = sidebar.getBoundingClientRect();
              if (linkBox.top < sidebarBox.top || linkBox.bottom > sidebarBox.bottom) {
                sidebar.scrollTop += linkBox.top - sidebarBox.top - sidebarBox.height / 3;
              }
            }
            lastActiveLink = activeLink;
          }
        }
      }
    }, { passive: true });
  }

  // Back to top button
  var btt = document.getElementById('back-to-top');
  if (btt) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 400) {
        btt.classList.add('visible');
      } else {
        btt.classList.remove('visible');
      }
    }, { passive: true });

    btt.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

})();
