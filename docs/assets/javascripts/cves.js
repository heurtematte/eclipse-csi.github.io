/* The filters and the pages of the page of the published CVEs (docs/cves.md, written by scripts/generate_news.py).

   The table works without JavaScript, every row shown: this script shows the filters and the pager (hidden by
   default), keeps the rows that match the filters, and shows them PAGE_SIZE at a time. It runs on every page, on its
   first load and after each instant navigation (document$ of the theme), and does nothing where the table is not. */

(function () {
  "use strict";

  var PAGE_SIZE = 25;

  function init() {
    var form = document.getElementById("csi-cve-filters");
    var table = document.getElementById("csi-cves");
    var pager = document.getElementById("csi-cve-pager");
    if (!form || !table || !pager || form.dataset.ready) {
      return;
    }
    form.dataset.ready = "true";
    var rows = Array.prototype.slice.call(table.tBodies[0].rows);
    var count = form.elements.namedItem("count");
    var page = 1;

    function matching() {
      var text = form.elements.namedItem("text").value.trim().toLowerCase();
      var severity = form.elements.namedItem("severity").value;
      var year = form.elements.namedItem("year").value;
      var project = form.elements.namedItem("project").value;
      return rows.filter(function (row) {
        return (!text || row.dataset.text.indexOf(text) !== -1) &&
          (!severity || row.dataset.severity === severity) &&
          (!year || row.dataset.year === year) &&
          (!project || row.dataset.project === project);
      });
    }

    function button(label, target, current, disabled, title) {
      var element = document.createElement("button");
      element.type = "button";
      element.textContent = label;
      element.disabled = disabled;
      if (title) {
        element.setAttribute("aria-label", title);
      }
      if (current) {
        element.setAttribute("aria-current", "page");
      }
      element.addEventListener("click", function () {
        page = target;
        render();
        table.scrollIntoView({ block: "start", behavior: "smooth" });
      });
      return element;
    }

    // the numbers around the current page, the first and the last one, with an ellipsis for the gaps
    function numbers(pages) {
      var shown = [];
      for (var n = 1; n <= pages; n++) {
        if (n === 1 || n === pages || Math.abs(n - page) <= 1) {
          if (shown.length && n - shown[shown.length - 1] > 1) {
            shown.push(null);
          }
          shown.push(n);
        }
      }
      return shown;
    }

    function render() {
      var kept = matching();
      var pages = Math.max(1, Math.ceil(kept.length / PAGE_SIZE));
      page = Math.min(page, pages);
      var first = (page - 1) * PAGE_SIZE;
      rows.forEach(function (row) {
        row.hidden = true;
      });
      kept.slice(first, first + PAGE_SIZE).forEach(function (row) {
        row.hidden = false;
      });
      count.value = kept.length === 0 ? "No CVE" :
        (first + 1) + "–" + Math.min(first + PAGE_SIZE, kept.length) + " of " + kept.length + " CVEs";

      pager.textContent = "";
      if (pages > 1) {
        pager.appendChild(button("‹", page - 1, false, page === 1, "Previous page"));
        numbers(pages).forEach(function (n) {
          if (n === null) {
            var gap = document.createElement("span");
            gap.className = "csi-pager__gap";
            gap.textContent = "…";
            pager.appendChild(gap);
          } else {
            pager.appendChild(button(String(n), n, n === page, false, "Page " + n));
          }
        });
        pager.appendChild(button("›", page + 1, false, page === pages, "Next page"));
      }
      pager.hidden = pages <= 1;
    }

    // a change of the filters starts again from the first page
    form.addEventListener("input", function () {
      page = 1;
      render();
    });
    form.addEventListener("submit", function (event) {
      event.preventDefault();
    });
    form.hidden = false;
    render();
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(init);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
