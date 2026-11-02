const fruits = ["Epli", "Banani", "Appelsína", "Bláber"];
const list = document.getElementById("fruitList")

for (const fruit of fruits) {
    const item = document.createElement("li");
    item.textContent = fruit;
    list.appendChild(item)
}