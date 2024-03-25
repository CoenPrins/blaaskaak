function show(events) {
	const template = document.querySelector("#event-template");
	const eventListElement = document.querySelector("#events");

	for (let event of events) {
		const clone = template.content.cloneNode(true);

		const date = new Date(event.begin);
		const month = date.toLocaleDateString('nl-NL', {month: 'long'})

		clone.querySelector(".event-day").textContent = date.getDate();
		clone.querySelector(".event-month").textContent = month;
		clone.querySelector(".event-title").textContent = event.name;
		clone.querySelector(".event-location").textContent = event.location;
		clone.querySelector(".event-description").textContent = event.description;

		eventListElement.appendChild(clone);
	}
}

fetch("/events.json")
.then(response => {
	if (!response.ok) {
		throw new Error("HTTP error " + response.status);
	}
	return response.json();
})
.then(json => {
	show(json.events);
})
