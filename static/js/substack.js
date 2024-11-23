import { getCookie } from "./utils.js";
async function sendAddToSubstackRequest(animalId) {
  const response = await fetch("/substack/add_to_substack/", {
    method: "POST",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: `animal_id=${animalId}`,
  });
  return await response.json();
}
function handleAddToSubstackResponse(data) {
  if (data.status === "success") {
    alert(data.message);
  } else {
    alert(data.message);
  }
}
function addSubstackHandler() {
  document.querySelectorAll(".btn-substack").forEach((button) => {
    button.addEventListener("click", async function () {
      const animalId = this.getAttribute("data-animal-id");
      const data = await sendAddToSubstackRequest(animalId);
      handleAddToSubstackResponse(data);
    });
  });
}

async function sendRemoveFromSubstackRequest(substackAnimalId) {
  const response = await fetch(`/substack/remove_from_substack/`, {
    method: "POST",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: `substack_animal_id=${substackAnimalId}`,
  });
  return response.json();
}
function handleRemoveFromSubstackResponse(data, substackAnimalId) {
  if (data.status === "success") {
    document.querySelector(`[data-substack-animal-id="${substackAnimalId}"]`).closest(".col-12").remove();
    alert(data.message);
  } else {
    alert(data.message);
  }
}
function removeSubstackHandler() {
  document.querySelectorAll(".btn-remove-substack").forEach((button) => {
    button.addEventListener("click", function () {
      const substackAnimalId = this.getAttribute("data-substack-animal-id");
      sendRemoveFromSubstackRequest(substackAnimalId).then((data) => handleRemoveFromSubstackResponse(data, substackAnimalId));
    });
  });
}
export { addSubstackHandler, removeSubstackHandler };