const commentButtons = document.querySelectorAll(".post-comment-btn");

for (const [index, commentButton] of commentButtons.entries()) {
  console.log(commentButton);

  commentButton.addEventListener("click", () => {
    // const postId = commentButton.closest(".post")
    //                           .querySelector(".post-id-details")
    //                           .children[0]
    //                           .innerText;

    // console.log(`You clicked me! ${postId}`); 
    
    displayCommentForm(index)
  })
}

function displayCommentForm(postNumber) {
  const commentForm =  document.querySelectorAll(".comment-form")[postNumber];

  commentForm.classList.remove("hide-comment-form");

  const closeButton = commentForm.children[0];
  
  closeButton.addEventListener("click", () => {
    commentForm.classList.add("hide-comment-form");
  })
}