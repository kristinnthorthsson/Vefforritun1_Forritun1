const input = document.getElementById("nameInput")
const button = document.getElementById("greetButton")
const output = document.getElementById("output")
const form  = document.getElementById("eitthvadForm")

form.addEventListener("submit", function(event) {
    event.preventDefault();
    const name = input.value.trim();
    if (name === "") {
        return;
    }
    const capitalizedName = 
    name.charAt(0).toLocaleUpperCase() + name.slice(1);
    output.textContent = "Well, aren't you a nigger, Mr. " + capitalizedName + "!"
});