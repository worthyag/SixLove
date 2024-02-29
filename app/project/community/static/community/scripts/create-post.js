const createPostBtn = document.querySelector(".create-post-btn");

createPostBtn.addEventListener("click", () => {
  console.log("You clicked me!");
  createPost();
});


function createPost() {
  const modal = document.querySelector("#createPostModal");
  modal.style.display = "block";
}