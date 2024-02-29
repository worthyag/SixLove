const postsBtn = document.querySelector(".posts-btn");
const awardsBtn = document.querySelector(".achievements-btn");

const postsDiv = document.querySelector(".feed");
const awardsDiv = document.querySelector(".achievements");


postsBtn.addEventListener("click", () => {
  console.log("Posts button clicked!");

  postsDiv.classList.remove("toggle-posts");
  awardsDiv.classList.add("toggle-posts");
});

awardsBtn.addEventListener("click", () => {
  console.log("Awards button clicked!");

  awardsDiv.classList.remove("toggle-posts");
  postsDiv.classList.add("toggle-posts");
});