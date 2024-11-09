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
export { addSubstackHandler };