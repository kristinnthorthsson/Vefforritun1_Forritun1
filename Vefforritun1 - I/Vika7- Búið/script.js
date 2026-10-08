function calculateTotal (ticketPrice, numberOfTickets) {
    return ticketPrice * numberOfTickets;
}

function applyDiscount(total, hasStudentDiscount) {
    if (hasStudentDiscount === true) {
        return total * 0.85;
    }

    return total;
}
const ticketPrice = 2200;
const numberOfTickets = 3;
const hasStudentDiscount = true;

const total = calculateTotal(ticketPrice, numberOfTickets);
const finalPrice = applyDiscount(total, hasStudentDiscount);

console.log("Verð fyrir afslátt:", total);
console.log("Lokaverð:", finalPrice);