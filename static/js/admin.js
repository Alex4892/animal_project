document.addEventListener("DOMContentLoaded", function () {
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
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});