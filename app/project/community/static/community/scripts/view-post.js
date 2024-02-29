console.log("View posts!");

const feed_posts = document.querySelectorAll(".feed-post");

for (const feed_post of feed_posts) {
  feed_post.addEventListener("click", (post) => {
    console.log("You clicked me!");

    viewPost(post);
  });
}


function viewPost(post) {
  const modal = document.querySelector("#viewPostModal");
  modal.style.display = "block";
}