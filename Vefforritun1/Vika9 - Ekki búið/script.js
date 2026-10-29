const form = document.querySelector(".signupForm")
const name = document.querySelector(".name")
const nameInput = document.querySelector("#nameInput")
const button = document.querySelector("button")
const age = document.querySelector(".age")
const ageInput = document.querySelector("#ageInput")
const button2 = document.querySelector("button")
const message = document.querySelector("#message")



form.addEventListener("submit", function (event) {
    event.preventDefault();

    const age = Number(ageInput.value)
    const name = Number(name)

    if (age <= 13)
        output.textContent = "Þú ert yngri en 13"
    if (age >= 13)
        output.textContent = "Þú ert eldri en 13"
});