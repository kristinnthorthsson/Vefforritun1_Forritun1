const destination = "London";
const days = 5;
const costPerDay = true;
const hasDiscount = true;

let totalCost = days * costPerDay

if (hasDiscount === true) {
    totalCost = totalCost *0.9;
}

console.log("Áfangastaður:", destination)
console.log("Lokakostnaður:", totalCost);

if (totalCost > 100000) {
    console.log("Dýr ferð<");
} else {
    console.log("Innan fjárhags");
}