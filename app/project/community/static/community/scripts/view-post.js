const feedPosts = document.querySelectorAll(".feed-post");

for (const feedPost of feedPosts) {
  feedPost.addEventListener("click", (post) => {
    const img = feedPost.children[0]
    const info = feedPost.children[1]
    const url = img.getAttribute("src")

    viewPost(url, info);
  });
}


function viewPost(url, infoDiv) {
  const modal = document.querySelector("#viewPostModal");
  const postImgDiv = document.querySelector(".post-img");
  const img = postImgDiv.children[0];
  img.setAttribute("src", url);

  const infoGroup = infoDiv.children;

  const likeCount = infoGroup[0].innerText;
  const username = infoGroup[1].innerText;
  const caption = infoGroup[2].innerText;

  document.querySelector(".like-count").textContent = likeCount;
  document.querySelector(".username").textContent = username;
  document.querySelector(".caption-text").textContent = caption;

  const postComments = querySelector(".post-comments");
  const comments = infoGroup[3].children;

  for (const comment of comments) {
    const p = document.createElement("p");
    p.textContent = comment.innerText;
    p.classList.add("comment");
    postComments.appendChild(p);
  }

  const date = infoGroup[4].innerText;
  console.log(date);

  modal.style.display = "block";
}