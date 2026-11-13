// Shared, tiny auth helpers -- Loudcase's login is deliberately simple
// (email + password, JWT in localStorage, no server-side session store).
// Used by practice.html and session.html to gate access, and by session.html
// to attach the token to the /evaluate call.

function requireLogin() {
  const token = localStorage.getItem("loudcase_token");
  if (!token) {
    window.location.href = "login.html";
    return null;
  }
  return token;
}

function currentUserEmail() {
  return localStorage.getItem("loudcase_email");
}

function logout() {
  localStorage.removeItem("loudcase_token");
  localStorage.removeItem("loudcase_email");
  localStorage.removeItem("loudcase_premium_email");
  window.location.href = "login.html";
}

function authHeader() {
  const token = localStorage.getItem("loudcase_token");
  return token ? { Authorization: `Bearer ${token}` } : {};
}

// Wires up a "#logout-link" element (present in the nav markup of any
// logged-in-only page) and fills a "#nav-email" element with the current
// user's email, if those elements exist on the page. Also wires up the
// mobile nav burger ("#nav-burger" / "#nav-menu"), present on the same
// pages -- below the CSS breakpoint in styles.css, the nav links + feedback
// button + email + logout collapse behind it instead of overflowing the
// screen the way a plain desktop nav would.
function wireAccountNav() {
  const emailEl = document.getElementById("nav-email");
  if (emailEl) {
    emailEl.textContent = currentUserEmail() || "";
    wirePremiumBadge(emailEl);
  }
  const logoutLink = document.getElementById("logout-link");
  if (logoutLink) {
    logoutLink.addEventListener("click", (e) => {
      e.preventDefault();
      logout();
    });
  }

  const burger = document.getElementById("nav-burger");
  const menu = document.getElementById("nav-menu");
  if (burger && menu) {
    // "nav-menu-open" on <body> locks background scroll while the
    // full-screen menu is open (see styles.css) -- otherwise scrolling
    // behind it could bring page content into view past its bottom edge.
    const setOpen = (isOpen) => {
      menu.classList.toggle("open", isOpen);
      burger.setAttribute("aria-expanded", String(isOpen));
      document.body.classList.toggle("nav-menu-open", isOpen);
    };
    burger.addEventListener("click", () => {
      setOpen(!menu.classList.contains("open"));
    });
    // Close the menu after tapping a link/button inside it, so it doesn't
    // stay open over the next page/action.
    menu.addEventListener("click", (e) => {
      if (e.target.closest("a, button")) setOpen(false);
    });
  }
}

// Shows a "Premium" pill right after the nav email for Premium accounts.
// It's appended INSIDE #nav-email so it stays beside the address even in
// the mobile menu, where .nav-actions stacks its children vertically.
// The last known status is cached in localStorage, keyed to the email it
// belongs to (so another account logging in on the same browser never
// inherits it), so the badge appears instantly on load; /billing/status
// then confirms or corrects it.
function wirePremiumBadge(emailEl) {
  const email = currentUserEmail();
  if (!email) return;

  const badge = document.createElement("span");
  badge.className = "premium-badge";
  badge.textContent = "Premium";
  badge.hidden = true;
  emailEl.appendChild(badge);

  const show = (isPremium) => {
    badge.hidden = !isPremium;
    try {
      if (isPremium) localStorage.setItem("loudcase_premium_email", email);
      else localStorage.removeItem("loudcase_premium_email");
    } catch (_) {}
  };

  try {
    if (localStorage.getItem("loudcase_premium_email") === email) badge.hidden = false;
  } catch (_) {}

  if (typeof CONFIG === "undefined") return;
  fetch(`${CONFIG.backendUrl}/billing/status`, { headers: authHeader() })
    .then((res) => (res.ok ? res.json() : null))
    .then((data) => {
      if (data) show(Boolean(data.is_premium));
    })
    .catch(() => {});
}
