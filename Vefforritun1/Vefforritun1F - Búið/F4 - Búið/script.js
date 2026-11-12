const games = ["Untitled Goose Game", "Clair Obscur: Expedition 33", "Stray", "Buckshot Roulette", "Far Cry 4"]
const list = document.getElementById("gameList")

for (const game of games) {                               // Loops through each game in the games array
    const item = document.createElement("li");           // Creates a new list item element
    item.textContent = game;                            // Sets the text content of the list item to the current game 
    list.appendChild(item);                            // Appends the list item to the unordered list in HTML
}