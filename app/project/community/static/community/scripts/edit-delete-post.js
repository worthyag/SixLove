const editPostButtons = document.querySelectorAll(".edit-post-btn");
const deletePostButtons = document.querySelectorAll(".delete-post-btn");


for (const editPostBtn of editPostButtons) {
  editPostBtn.addEventListener("click", (e) => {
    console.log("You clicked edit!");
    editPost(e.target, true);
  });
}

for (const deletePostBtn of deletePostButtons) {
  deletePostBtn.addEventListener("click", (e) => {
    console.log("You clicked delete!");
    deletePost(e.target, false);
  });
}


function editPost(btn, isEditing) {
  const modal = document.querySelector("#editPostModal");
  const postToEdit = document.querySelector("#post-id-to-edit");
  const postId = btn.parentElement.parentElement
                  .parentElement.nextElementSibling.children[0].textContent;

  postToEdit.value = postId;

  // Disable the file input if the user is editing a post.
  const postPicElements = document.querySelectorAll("#id_post_picture");

  if (isEditing) {
    for (const picElement of postPicElements) {
      picElement.disabled =  true;
    }
  } else {
    for (const picElement of postPicElements) {
      picElement.disabled =  false;
    }
  }

  const elements = Array.from(postToEdit.parentElement.parentElement.children);
  const [input, pTag, ...rest] = elements;

  pTag.style.display = "none";


  const postCaptionElements = document.querySelectorAll("#id_post_caption");
  const postCaption = btn.parentElement.parentElement
                      .parentElement.nextElementSibling.nextElementSibling
                      .nextElementSibling.children[1].textContent;
  
  for (const captionElement of postCaptionElements) {
    captionElement.value = postCaption;
  }

  modal.style.display = "block";
}

function deletePost(btn) {
  const modal = document.querySelector("#deletePostModal");
  const postToDelete = document.querySelector("#post-id-to-delete");
  const postId = btn.parentElement.parentElement
                  .parentElement.nextElementSibling.children[0].textContent;

  postToDelete.value = postId;

  console.log(postToDelete.parentElement.parentElement.children);
  console.log(postToDelete.parentElement.parentElement);

  const elements = Array.from(postToDelete.parentElement.parentElement.children);
  const [input, pTag1, pTag2, ...rest] = elements;
  pTag1.style.display = "none";
  pTag2.style.display = "none";

  modal.style.display = "block";
}