const createProfileBtn = document.querySelector(".create-profile-btn");

createProfileBtn.addEventListener("click", () => {
  console.log("You clicked me!");
  createProfile();
});


function createProfile() {
  const modal = document.querySelector("#createProfileModal");
  modal.style.display = "block";
}