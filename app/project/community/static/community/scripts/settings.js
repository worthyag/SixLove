const profileSettingsDiv = document.querySelector(".profile-settings-block");
const usernameSettingsDiv = document.querySelector(".username-settings-block");
const nameSettingsDiv = document.querySelector(".name-settings-block");
const bioSettingsDiv = document.querySelector(".bio-settings-block");
const dpSettingsDiv = document.querySelector(".dp-settings-block");

profileSettingsDiv.addEventListener("click", () => {
  console.log("Profile");
  editProfile();
});

usernameSettingsDiv.addEventListener("click", () => {
  console.log("Username");
  editUsername();
});

nameSettingsDiv.addEventListener("click", () => {
  console.log("Name");
  editName();
});

bioSettingsDiv.addEventListener("click", () => {
  console.log("Bio");
  editBio();
});
dpSettingsDiv.addEventListener("click", () => {
  console.log("DP");
  editDP();
});

function editProfile() {
  const modal = document.querySelector("#editProfileModal");
  modal.style.display = "block";
}

function editUsername() {
  const modal = document.querySelector("#editUsernameModal");
  modal.style.display = "block";
}

function editName() {
  const modal = document.querySelector("#editProfileNameModal");
  modal.style.display = "block";
}

function editBio() {
  const modal = document.querySelector("#editBioModal");
  modal.style.display = "block";
}

function editDP() {
  const modal = document.querySelector("#editDPModal");
  modal.style.display = "block";
}