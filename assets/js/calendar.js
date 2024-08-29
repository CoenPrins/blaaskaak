function parseLocation(location) {
  // Oudemanhuispoort, 1012 CN Amsterdam, Nederland
  // --> Oudemanhuispoort (Amsterdam)
  const parts = location.split(",");

  if (parts.length <= 1) {
    return location;
  }

  var result = parts[0];

  result += " (" + parts[1].split(" ").slice(-1)[0] + ")";

  return result;
}

function show(eventData) {
  const template = document.querySelector("#event-template");
  if (!template) {
    return;
  }
  const eventListElement = document.querySelector("#events");
  const today = new Date();
  today.setHours(0, 0, 0);

  for (let event of eventData.events) {
    const clone = template.content.cloneNode(true);

    const date = new Date(event.begin);

    // do not show past events
    //if (date < today) {
    //  continue;
    //}

    const month = date.toLocaleDateString('nl-NL', {month: 'long'})

    clone.querySelector(".event-day").textContent = date.getDate();
    clone.querySelector(".event-month").textContent = month;
    clone.querySelector(".event-title").textContent = event.name;
    clone.querySelector(".event-location").textContent = parseLocation(event.location);
    clone.querySelector(".event-description").insertAdjacentHTML('beforeend', event.description);

    //if (event.url) {
    //  clone.querySelector(".event-url").setAttribute("href", event.url);
    //}

    eventListElement.appendChild(clone);
  }

  const lastUpdate = new Date(eventData.metadata.generated).toLocaleString('nl-NL');
  document.querySelector("#events-updated").textContent += lastUpdate;
}

if (document.querySelector("#event-template")) {
  fetch("events.json")
    .then(response => {
      if (!response.ok) {
        throw new Error("HTTP error " + response.status);
      }
      return response.json();
    })
    .then(json => {
      show(json);
    })
}
