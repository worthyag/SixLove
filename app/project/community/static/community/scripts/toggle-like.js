const likeButtons = document.querySelectorAll(".post-like-btn");

for (const likeButton of likeButtons) {
  likeButton.addEventListener("click", () => {
    const img = likeButton.children[0];
    const url = img.getAttribute("src");

    const liked = "/static/community/images/liked-icon.svg";
    const like = "/static/community/images/like-icon.svg";

    img.setAttribute("src", (url === like) ? liked : like);
  
  });
}

