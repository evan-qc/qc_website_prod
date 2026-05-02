// Quantify Consulting — theme toggle
// Defaults to dark; persists choice in localStorage.
(function () {
    var root = document.documentElement;

    // Apply saved theme as early as possible (script is loaded in <head>).
    var saved = null;
    try { saved = localStorage.getItem('theme'); } catch (e) {}
    var initial = saved === 'light' ? 'light' : 'dark';
    root.setAttribute('data-theme', initial);

    function applyLabel(btn, theme) {
        if (!btn) return;
        btn.textContent = theme === 'dark' ? '🌙 Dark' : '☀️ Light';
    }

    // Wire up the toggle once DOM is ready.
    document.addEventListener('DOMContentLoaded', function () {
        var btn = document.getElementById('themeToggle');
        applyLabel(btn, root.getAttribute('data-theme'));

        if (btn) {
            btn.addEventListener('click', function () {
                var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
                root.setAttribute('data-theme', next);
                applyLabel(btn, next);
                try { localStorage.setItem('theme', next); } catch (e) {}
            });
        }
    });
})();
