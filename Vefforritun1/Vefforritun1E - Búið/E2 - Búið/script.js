const form = document.getElementById("signupForm")                              // Gets the sign up form from HTML
const emailInput = document.getElementById("emailInput")                       // Gets the email input id from HTML

form.addEventListener("submit", function (event) {                           // Adds an event listener to the form that listens for a submit event
    event.preventDefault();                                                 // Prevents the default form submission behavior

    const email = emailInput.value                                        // Gets the value of the email input field
    output.textContent = "Skráf netfang: " + email;                      // Shows the email address in the output element
});