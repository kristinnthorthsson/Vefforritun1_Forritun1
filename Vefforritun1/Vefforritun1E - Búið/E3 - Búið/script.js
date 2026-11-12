const form = document.getElementById("ageForm");                  // Gets the age form from HTML
const ageInput = document.getElementById("ageInput");            // Gets the age input from HTML
const output = document.getElementById("output");               // Gets the output element from HTML

form.addEventListener("submit", function (event) {            // Add an event listener to the form for the submit event
    event.preventDefault();                                  // Prevents the default form submission behavior

    const age = Number(ageInput.value);                    // Converts the input value to a number

    if (age >= 18) {                                     // If the age is 18 or older
        output.textContent  =  "18 ára eða eldri";      // Sets the output text to "18 ára eða eldri"
    } else {                                           // If the age is less than 18
        output.textContent = "Yngri en 18 ára"        // Sets the output text to "Yngri en 18 ára"
    }
});