import { updateAnimalStatus, updateCommentStatus } from "./admin.js";
import { addFavoriteHandler, removeFavoriteHandler } from "./favorites.js";
document.addEventListener("DOMContentLoaded", function () {
    updateAnimalStatus();
    updateCommentStatus();
    addFavoriteHandler();
    removeFavoriteHandler();
});