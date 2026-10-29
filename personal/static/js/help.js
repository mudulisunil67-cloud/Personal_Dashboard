
document.addEventListener("DOMContentLoaded", function () {
    const faqCards = document.querySelectorAll(".faq-card");

    faqCards.forEach(function (card) {
        const summary = card.querySelector("summary");

        if (!summary) {
            console.error("FAQ question is missing.");
        }
    });
});
