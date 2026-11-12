const form = document.getElementById("eitthvadForm")
const input = document.getElementById("writeInput")
const button = document.getElementById("greetButton")

form.addEventListener("submit", function(event) {
    event.preventDefault();
    const write = input.value.trim();
    if (write === "") {
        return;
    }
    
    output.textContent = "Hello!"
});