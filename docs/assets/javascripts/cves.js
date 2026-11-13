/* The filters of the page of the published CVEs (docs/cves.md, written by scripts/generate_news.py).

   The table works without JavaScript: this script only shows the filters (hidden by default) and hides the rows that
   do not match them. It runs on every page, on its first load and after each instant navigation (document$ of the
   theme), and does nothing where the table is not. */

(function () {
  "use strict";

  function init() {
    var form = document.getElementById("csi-cve-filters");
    var table = document.getElementById("csi-cves");
    if (!form || !table || form.dataset.ready) {
      return;
    }
    form.dataset.ready = "true";
    var rows = Array.prototype.slice.call(table.tBodies[0].rows);
    var count = form.elements.namedItem("count");

    function apply() {
      var text = form.elements.namedItem("text").value.trim().toLowerCase();
      var severity = form.elements.namedItem("severity").value;
      var year = form.elements.namedItem("year").value;
      var project = form.elements.namedItem("project").value;
      var shown = 0;
      rows.forEach(function (row) {
        var match = (!text || row.dataset.text.indexOf(text) !== -1) &&
          (!severity || row.dataset.severity === severity) &&
          (!year || row.dataset.year === year) &&
          (!project || row.dataset.project === project);
        row.hidden = !match;
        shown += match ? 1 : 0;
      });
      count.value = shown === rows.length ? rows.length + " CVEs" : shown + " of " + rows.length + " CVEs";
    }

    form.addEventListener("input", apply);
    form.addEventListener("submit", function (event) {
      event.preventDefault();
    });
    form.hidden = false;
    apply();
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(init);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
