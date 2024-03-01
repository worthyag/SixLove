const createPostBtn = document.querySelector(".create-post-btn");

createPostBtn.addEventListener("click", () => {
  console.log("You clicked me!");
  createPost();
});


function createPost() {
  const modal = document.querySelector("#createPostModal");

  // Show the file input if the user is creating a post.
  const postPicElements = document.querySelectorAll("#id_post_picture");

  for (const picElement of postPicElements) {
    picElement.disabled =  false;
  }


  modal.style.display = "block";
}