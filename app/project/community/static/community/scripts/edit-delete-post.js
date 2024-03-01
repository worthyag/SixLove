const editPostBtn = document.querySelector(".edit-post-btn");
const deletePostBtn = document.querySelector(".delete-post-btn");

editPostBtn.addEventListener("click", () => {
  console.log("You clicked edit!");
  editPost();
});

deletePostBtn.addEventListener("click", () => {
  console.log("You clicked delete!");
  deletePost();
});


function editPost() {
  const modal = document.querySelector("#editPostModal");
  modal.style.display = "block";
}

function deletePost() {
  const modal = document.querySelector("#deletePostModal");
  modal.style.display = "block";
}