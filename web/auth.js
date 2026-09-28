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
  if (emailEl) emailEl.textContent = currentUserEmail() || "";
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
    burger.addEventListener("click", () => {
      const isOpen = menu.classList.toggle("open");
      burger.setAttribute("aria-expanded", String(isOpen));
    });
    // Close the menu after tapping a link/button inside it, so it doesn't
    // stay open over the next page/action.
    menu.addEventListener("click", (e) => {
      if (e.target.closest("a, button")) {
        menu.classList.remove("open");
        burger.setAttribute("aria-expanded", "false");
      }
    });
  }
}
