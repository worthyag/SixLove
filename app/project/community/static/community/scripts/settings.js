const profileSettingsDiv = document.querySelector(".profile-settings-block");

profileSettingsDiv.addEventListener("click", (e) => {
  console.log("How do you feel?");

  editProfile(e.target, true);
});

function editProfile(btn, isEditing) {
  const modal = document.querySelector("#editProfileModal");
  // const postToEdit = document.querySelector("#post-id-to-edit");
  // const postId = btn.parentElement.parentElement
  //                 .parentElement.nextElementSibling.children[0].textContent;

  // postToEdit.value = postId;

  // Disable the file input if the user is editing a post.
  // const postPicElements = document.querySelectorAll("#id_post_picture");

  // if (isEditing) {
  //   for (const picElement of postPicElements) {
  //     picElement.disabled =  true;
  //   }
  // } else {
  //   for (const picElement of postPicElements) {
  //     picElement.disabled =  false;
  //   }
  // }

  // const elements = Array.from(postToEdit.parentElement.parentElement.children);
  // const [input, pTag, ...rest] = elements;

  // pTag.style.display = "none";


  // const postCaptionElements = document.querySelectorAll("#id_post_caption");
  // const postCaption = btn.parentElement.parentElement
  //                     .parentElement.nextElementSibling.nextElementSibling
  //                     .nextElementSibling.children[1].textContent;
  
  // for (const captionElement of postCaptionElements) {
  //   captionElement.value = postCaption;
  // }

  modal.style.display = "block";
}