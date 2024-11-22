import { getCookie } from "./utils.js";
async function sendAddToFavoritekRequest(animalId) {
  const response = await fetch("/favorite/add_to_favorite/", {
    method: "POST",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: `animal_id=${animalId}`,
  });
  return await response.json();
}
function handleAddToFavoriteResponse(data) {
  if (data.status === "success") {
    alert(data.message);
  } else {
    alert(data.message);
  }
}
function addFavoriteHandler() {
  document.querySelectorAll(".btn-favorite").forEach((button) => {
    button.addEventListener("click", async function () {
      const animalId = this.getAttribute("data-animal-id");
      const data = await sendAddToFavoriteRequest(animalId);
      handleAddToFavoriteResponse(data);
    });
  });
}

async function sendRemoveFromFavoriteRequest(favoriteAnimalId) {
  const response = await fetch(`/favorite/remove_from_favorite/`, {
    method: "POST",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: `favorite_animal_id=${favoriteAnimalId}`,
  });
  return response.json();
}
function handleRemoveFromFavoriteResponse(data, favoriteAnimalId) {
  if (data.status === "success") {
    document.querySelector(`[data-favorite-animal-id="${favoriteAnimalId}"]`).closest(".col-12").remove();
    alert(data.message);
  } else {
    alert(data.message);
  }
}
function removeFavoriteHandler() {
  document.querySelectorAll(".btn-remove-favorite").forEach((button) => {
    button.addEventListener("click", function () {
      const favoriteAnimalId = this.getAttribute("data-favorite-animal-id");
      sendRemoveFromFavoriteRequest(favoriteAnimalId).then((data) => handleRemoveFromFavoriteResponse(data, favoriteAnimalId));
    });
  });
}
export { addFavoriteHandler, removeFavoriteHandler };