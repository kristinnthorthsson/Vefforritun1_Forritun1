const games = ["Untitled Goose Game", "Clair Obscur: Expedition 33", "Stray", "Buckshot Roulette", "Far Cry 4"]
const list = document.getElementById("gameList")
const form = document.getElementById("addGameForm")
const input = document.getElementById("gameInput")

for (const game of games) {
    const item = document.createElement("li");
    item.textContent = game;
    list.appendChild(item);
}

form.addEventListener("submit", function(event) {
    event.preventDefault();
    
    const game = input.value.trim();
    if (game === "") {
        return;
    }

    const item = document.createElement("li");
    item.textContent = game;
    list.appendChild(item);

    input.value = "";
});