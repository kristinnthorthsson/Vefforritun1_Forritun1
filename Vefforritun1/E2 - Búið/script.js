const form = document.getElementById("signupForm")
const emailInput = document.getElementById("emailInput")
const output = document.getElementById("output")

form.addEventListener("submit", function (event) {
    event.preventDefault();

    const email = emailInput.value
    output.textContent = "Skráf netfang: " + email;
});