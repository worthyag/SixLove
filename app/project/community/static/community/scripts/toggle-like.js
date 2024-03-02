// const toggleLikeUrl = "community/toggle-like/__post_id__/";

const likeButtons = document.querySelectorAll(".post-like-btn");

for (const likeButton of likeButtons) {
  likeButton.addEventListener("click", async () => {
    const postId = likeButton.closest(".post")
                              .querySelector(".post-id-details")
                              .children[0]
                              .innerText;

    try {
      const csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value;
      

      const response = await fetch(toggleLikeUrl.replace("__post_id__", postId), {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        }
      });

      const data = await response.json();

      // Updating the like count.
      const likeCountElement = likeButton.closest(".post")
                                          .querySelector(".like-count");
      likeCountElement.innerText = data.like_count;

      // Updating the like button image.
      const img = likeButton.children[0];
      const url = img.getAttribute("src");

      const liked = "/static/community/images/liked-icon.svg";
      const like = "/static/community/images/like-icon.svg";

      img.setAttribute("src", (url === like) ? liked : like);

    } catch (error) {
        console.error("Error toggling the like: ", error);
    } 
  });
}



// for (const likeButton of likeButtons) {
//   likeButton.addEventListener("click", () => {
//     const img = likeButton.children[0];
//     const url = img.getAttribute("src");

//     const liked = "/static/community/images/liked-icon.svg";
//     const like = "/static/community/images/like-icon.svg";

//     img.setAttribute("src", (url === like) ? liked : like);
  
//   });
// }

