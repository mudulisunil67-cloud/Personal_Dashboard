
document.addEventListener("DOMContentLoaded", function () {

    const linkedinButton = document.getElementById("linkedinButton");

    if (!linkedinButton) {
        console.error("LinkedIn button not found.");
        return;
    }

    // Check that the LinkedIn link is configured
    linkedinButton.addEventListener("click", function () {
        const profileURL = linkedinButton.href;

        if (!profileURL.startsWith("https://www.linkedin.com/")) {
            console.error("Please provide a valid LinkedIn profile URL.");
        }
    });

});
