const games = ["Untitled Goose Game", "Clair Obscur: Expedition 33", "Stray", "Buckshot Roulette", "Far Cry 4"]
const list = document.getElementById("gameList")

for (const game of games) {
    const item = document.createElement("li");
    item.textContent = game;
    list.appendChild(item)
}