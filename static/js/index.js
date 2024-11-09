import { updateAnimalStatus, updateCommentStatus } from "./admin.js";
import { addSubstackHandler, removeSubstackHandler } from "./substack.js";
document.addEventListener("DOMContentLoaded", function () {
    updateAnimalStatus();
    updateCommentStatus();
    addSubstackHandler();
    removeSubstackHandler();
});