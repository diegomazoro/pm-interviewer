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
// user's email, if those elements exist on the page.
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
}
