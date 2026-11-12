const input = document.getElementById("nameInput")                       // Gets the name input from HTML
const button = document.getElementById("greetButton")                   // Gets the button from HTML
const output = document.getElementById("output")                       // Gets the output element from HTML

button.addEventListener("click", function(event) {                   // Runs when the button is clicked
    event.preventDefault();                                         // Prevent the default form submission
    const name = input.value.trim();                               // Rads the name and removes any leading or trailing whitespace
    output.textContent = "Halló " + name + "!";                   // Displays the greeting message in the output element
});