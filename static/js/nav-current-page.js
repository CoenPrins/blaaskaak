const navItems = document.querySelectorAll('nav li');
const currentUrl = window.location.pathname;

for (const navItem of navItems) {
	const href = navItem.querySelector('a').href;
	if (href.endsWith(currentUrl)) {
		navItem.classList.add("current");
	}
}
