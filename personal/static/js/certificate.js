
document.addEventListener("DOMContentLoaded", function () {

    const addButton = document.getElementById("addButton");
    const cancelButton = document.getElementById("cancelButton");
    const formSection = document.getElementById("certificateFormSection");

    if (!addButton || !formSection) {
        console.error("Certificate form elements were not found.");
        return;
    }

    // Open the form
    addButton.addEventListener("click", function () {
        formSection.hidden = false;

        formSection.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    });

    // Close the form
    if (cancelButton) {
        cancelButton.addEventListener("click", function () {
            formSection.hidden = true;
        });
    }

});
