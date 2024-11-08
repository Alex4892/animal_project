    import { getCookie } from "./utils.js";
    function updateBookStatus() {
    document.querySelectorAll(".animal-switch").forEach(switchElement => {
        switchElement.addEventListener("change", function () {
            const animalId = this.getAttribute("data-animal-id");
            const isChecked = this.checked;
            fetch(`/change-animal-status/${animalId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ is_verified: isChecked })
            })
            .then(response => response.json())
            .then(data => {
                if (data.status !== "success") {
                    alert("Ошибка при обновлении статуса объявления");
                }
            });
        });
    });
}

function updateCommentStatus() {
    document.querySelectorAll(".comment-switch").forEach(switchElement => {
        switchElement.addEventListener("change", function () {
            const commentId = this.getAttribute("data-comment-id");
            const isChecked = this.checked;
            fetch(`/change-comment-status/${commentId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ is_verified: isChecked }) 
            })
            .then(response => response.json()) 
            .then(data => {
                if (data.status !== "success") {
                    alert("Ошибка при обновлении статуса комментария");
                }
            });
        });
    });
}

export {
    updateAnimalStatus,
    updateCommentStatus
}