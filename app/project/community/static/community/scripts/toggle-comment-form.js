const commentButtons = document.querySelectorAll(".post-comment-btn");

for (const commentButton of commentButtons) {
  console.log(commentButton);

  commentButton.addEventListener("click", () => {
    const postId = commentButton.closest(".post")
                              .querySelector(".post-id-details")
                              .children[0]
                              .innerText;

    console.log(`You clicked me! ${postId}`);                       
  })
}