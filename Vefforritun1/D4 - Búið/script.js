const button = document.getElementById("likeButton")
const likes = document.getElementById("likes")

let like = 0

button.addEventListener("click", function () {
    like++;
    likes.textContent = like;
});
