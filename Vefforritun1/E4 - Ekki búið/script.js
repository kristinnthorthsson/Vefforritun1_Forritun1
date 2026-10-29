const priceForm = document.getElementById("priceForm");
const priceInput = document.getElementById("priceInput");
const countInput = document.getElementById("countInput");
const message = document.getElementById("output");

priceForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const price = Number(priceInput.value)
    const count = Number(countInput.value)
    const total = price * count;

    message.textContent = `Heildarverð: ${total} kr`;
});