import { updateAnimalStatus, updateCommentStatus } from "./admin.js";
import { addSubstackHandler } from "./substack.js";
document.addEventListener("DOMContentLoaded", function () {
    updateAnimalStatus();
    updateCommentStatus();
    addSubstackHandler();
});