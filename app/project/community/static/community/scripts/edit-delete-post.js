const editPostButtons = document.querySelectorAll(".edit-post-btn");
const deletePostButtons = document.querySelectorAll(".delete-post-btn");


for (const editPostBtn of editPostButtons) {
  editPostBtn.addEventListener("click", (e) => {
    console.log("You clicked edit!");
    editPost(e.target);
  });
}

for (const deletePostBtn of deletePostButtons) {
  deletePostBtn.addEventListener("click", (e) => {
    console.log("You clicked delete!");
    deletePost(e.target);
  });
}


function editPost(btn) {
  const modal = document.querySelector("#editPostModal");
  const postToEdit = document.querySelector("#post-id-to-edit");
  const post_id = btn.parentElement.parentElement
                  .parentElement.nextElementSibling.children[0].textContent;

  postToEdit.value = post_id;

  modal.style.display = "block";
}

function deletePost(btn) {
  const modal = document.querySelector("#deletePostModal");
  const postToDelete = document.querySelector("#post-id-to-delete");
  const post_id = btn.parentElement.parentElement
                  .parentElement.nextElementSibling.children[0].textContent;

  postToDelete.value = post_id;

  modal.style.display = "block";
}