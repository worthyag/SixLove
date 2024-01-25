const postsButton = document.querySelector("#display-posts-btn");
const awardsButton = document.querySelector("#display-achievements-btn");

const postsDiv = document.querySelector(".profile-post-grid-section");
const awardsDiv = document.querySelector(".profile-achievements-grid-section");


postsButton.addEventListener("click", () => {
  console.log("In use");
  postsDiv.classList.remove("hide-toggle");
  awardsDiv.classList.add("hide-toggle");
  postsButton.classList.add("active");
  awardsButton.classList.remove("active");
})

awardsButton.addEventListener("click", () => {
  console.log("In use");
  awardsDiv.classList.remove("hide-toggle");
  postsDiv.classList.add("hide-toggle");
  awardsButton.classList.add("active");
  postsButton.classList.remove("active");
})