const form  = document.getElementById("ageForm");
const ageInput = document.getElementById("ageInput")
const output = document.getElementById("output")

form.addEventListener("submit", function (event) {
    event.preventDefault();

    const age = Number(ageInput.value);

    if (age >= 18) {
        output.textContent  =  "18 ára eða eldri";
    } else {
        output.textContent = "Yngri en 18 ára"
    }
});