const createProfileBtn = document.querySelector(".create-profile-btn");

if (createProfileBtn) {
  createProfileBtn.addEventListener("click", () => {
    console.log("You clicked me!");
    createProfile();
  });
}


function createProfile() {
  const modal = document.querySelector("#createProfileModal");
  modal.style.display = "block";
}