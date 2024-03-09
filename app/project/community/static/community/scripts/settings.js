const profileSettingsDiv = document.querySelector(".profile-settings-block");
const usernameSettingsDiv = document.querySelector(".username-settings-block");
const nameSettingsDiv = document.querySelector(".name-settings-block");
const bioSettingsDiv = document.querySelector(".bio-settings-block");
const dpSettingsDiv = document.querySelector(".dp-settings-block");

profileSettingsDiv.addEventListener("click", (e) => {
  console.log("Profile");

  editProfile(e.target, true);
});

usernameSettingsDiv.addEventListener("click", (e) => {
  console.log("Username");

  editUsername(e.target, true);
});

nameSettingsDiv.addEventListener("click", (e) => {
  console.log("Name");

  editName(e.target, true);
});

bioSettingsDiv.addEventListener("click", (e) => {
  console.log("Bio");

  editBio(e.target, true);
});
dpSettingsDiv.addEventListener("click", (e) => {
  console.log("DP");

  editDP(e.target, true);
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

function editUsername(btn, isEditing) {
  const modal = document.querySelector("#editUsernameModal");
  modal.style.display = "block";
}

function editName(btn, isEditing) {
  const modal = document.querySelector("#editProfileNameModal");
  modal.style.display = "block";
}

function editBio(btn, isEditing) {
  const modal = document.querySelector("#editBioModal");
  modal.style.display = "block";
}

function editDP(btn, isEditing) {
  const modal = document.querySelector("#editDPModal");
  modal.style.display = "block";
}