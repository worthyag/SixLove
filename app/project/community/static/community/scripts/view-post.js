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
  // document.querySelector(".post-id-data").textContent = id;

  const postComments = document.querySelector(".post-comments");
  postComments.textContent = "";
  
  const comments = infoGroup[3].children;

  for (const comment of comments) {
    const p = document.createElement("p");
    p.textContent = comment.innerText;
    p.classList.add("comment");
    postComments.appendChild(p);
  }

  const date = infoGroup[4].innerText;
  document.querySelector(".post-date").textContent = date;

  const id = infoGroup[5].innerText;
  document.querySelector(".post-id-details").children[0].textContent = id;

  modal.style.display = "block";
}