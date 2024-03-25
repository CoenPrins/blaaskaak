function getEventsList(icsData) {
	var data = ical.parseICS(icsData);
	var events = [];

	for (let vevent of Object.values(data)) {
		// filter non-events and private events
		if (vevent.type == 'VEVENT' && vevent.summary != "Busy") {
			events.push({
				title: vevent.summary,
				location: vevent.location,
				date: vevent.start,
				description: vevent.description,
			});
		}
	}

	return events;
}


function show(events) {
	const template = document.querySelector("#event-row-template");
	const tbody = document.querySelector("#events");
	// assure sorted on date
	events.sort((a, b) => a.date - b.date);
	for (let event of events) {
		const clone = template.content.cloneNode(true);
		clone.querySelector(".day").textContent = event.date.getDate();
		const month = event.date.toLocaleDateString('nl-NL', {month: 'long'})
		clone.querySelector(".month").textContent = month;
		clone.querySelector(".event-title").textContent = event.title;

		const desc = new DOMParser().parseFromString(event.description, "text/html").documentElement.textContent;
		clone.querySelector(".event-description").textContent = desc;
		tbody.appendChild(clone);
	}
}

fetch("basic.ics")
	.then((res) => res.text())
	.then((text) => {
		var events = getEventsList(text);
		show(events);
	})
	.catch((e) => console.error(e));
