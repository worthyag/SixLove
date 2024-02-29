const feedPosts = document.querySelectorAll(".feed-post");

for (const feedPost of feedPosts) {
  feedPost.addEventListener("click", (post) => {
    console.log("You clicked me!");

    viewPost(post);
  });
}


function viewPost(post) {
  const modal = document.querySelector("#viewPostModal");
  modal.style.display = "block";
}