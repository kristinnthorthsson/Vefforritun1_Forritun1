const priceForm = document.getElementById("priceForm");                       // Gets the price form from HTML
const priceInput = document.getElementById("priceInput");                    // Gets the price input from HTML 
const countInput = document.getElementById("countInput");                   // Gets the count input from HTML
const message = document.getElementById("output");                         // Gets the output message from HTML

priceForm.addEventListener("submit", function (event) {                  // Adds an event listener to the price form that listens for a submit event
    event.preventDefault();                                             // Prevents the default form submission behavior

    const price = Number(priceInput.value)                            // Converts the price input value to a number
    const count = Number(countInput.value)                           // Converts the count input value to a number
    const total = price * count;                                    // Calculates the total price by multiplying the price and count

    message.textContent = `Heildarverð: ${total} kr`;             // Shows the total price in the output message
});