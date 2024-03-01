const editPostButtons = document.querySelectorAll(".edit-post-btn");
const deletePostButtons = document.querySelectorAll(".delete-post-btn");


for (const editPostBtn of editPostButtons) {
  editPostBtn.addEventListener("click", () => {
    console.log("You clicked edit!");
    editPost();
  });
}

for (const deletePostBtn of deletePostButtons) {
  deletePostBtn.addEventListener("click", () => {
    console.log("You clicked delete!");
    deletePost();
  });
}


function editPost() {
  const modal = document.querySelector("#editPostModal");
  modal.style.display = "block";
}

function deletePost() {
  const modal = document.querySelector("#deletePostModal");
  modal.style.display = "block";
}