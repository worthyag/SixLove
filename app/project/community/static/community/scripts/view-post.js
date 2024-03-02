const feedPosts = document.querySelectorAll(".feed-post");

for (const [index, feedPost] of feedPosts.entries()) {
  feedPost.addEventListener("click", (post) => {
    const img = feedPost.children[0];
    const info = feedPost.children[1];
    const url = img.getAttribute("src");

    viewPost(url, info, index);
  });
}


async function viewPost(url, infoDiv, index) {
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

  const userHasLiked = infoGroup[6].innerText.toLowerCase();
  const likeImg = document.querySelector(".post-like-btn").children[0];

  const liked = "/static/community/images/liked-icon.svg";
  const like = "/static/community/images/like-icon.svg";

  likeImg.setAttribute("src", (userHasLiked === "true") ? liked : like);

  // Fetching the updated like info for a specific post.
  try {
    const response = await fetch(likeInfoUrl.replace("__post_id__", id));
    const likeInfo = await response.json();

    // Updating the like count in the modal.
    document.querySelector(".like-count").textContent = likeInfo.like_count;

    // Updating the user_has_liked attribute for the like button.
    const hasLikedData = document.querySelectorAll(".user_has_liked-data")[index];
    hasLikedData.textContent = likeInfo.user_has_liked.toString();

  } catch (error) {
    console.error("Error fetching the like info: ", error);
  }

  modal.style.display = "block";
}