
document.addEventListener("DOMContentLoaded", function () {

    // Get elements from your HTML
    const addButton = document.getElementById("addButton");
    const cancelButton = document.getElementById("cancelButton");
    const formSection = document.getElementById("projectFormSection");

    // Check that the elements exist
    if (!addButton || !formSection) {
        console.error("Add button or project form section not found.");
        return;
    }

    // Show the project form
    addButton.addEventListener("click", function () {
        formSection.hidden = false;

        formSection.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    });

    // Hide the project form
    if (cancelButton) {
        cancelButton.addEventListener("click", function () {
            formSection.hidden = true;
        });
    }

});
