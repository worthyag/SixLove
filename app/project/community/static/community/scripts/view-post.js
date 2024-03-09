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
  const postImgDiv = modal.querySelector(".post-img img");
  const likeCountElement = modal.querySelector(".like-count");
  const usernameElement = modal.querySelector(".username");
  const captionElement = modal.querySelector(".caption-text");
  const postComments = modal.querySelector(".post-comments");
  // const expandedComments = modal.querySelector(".expanded-comments");
  // const postCommentCount = modal.querySelector(".post-comments-count");
  const commentUserLink = modal.querySelector(".comment-user-link");
  const commentersUsername = modal.querySelector(".commenters-username");
  const commentContent = modal.querySelector(".comment-content");
  const commentForm = modal.querySelector(".comment-form");
  const postId = modal.querySelector(".hidden-id");

  // Fetching the updated like info for a specific post.
  try {
    const response = await fetch(likeInfoUrl.replace(
      "__post_id__", infoDiv.querySelector(".post-id-data").innerText
    ));
    const likeInfo = await response.json();

    // Updating the like count in the modal.
    likeCountElement.textContent = likeInfo.like_count;

    // Updating the user_has_liked attribute for the like button.
    const hasLikedData = document.querySelectorAll(".user_has_liked-data")[index];
    hasLikedData.textContent = likeInfo.user_has_liked.toString();

  } catch (error) {
    console.error("Error fetching the like info: ", error);
  }

  // Setting modal content.
  postImgDiv.setAttribute("src", url);
  usernameElement.textContent = infoDiv.querySelector(".username-data").innerText;
  captionElement.textContent = infoDiv.querySelector(".captionText-data").innerText;

  // Updating comments.
  const postIDData = infoDiv.querySelector(".postId-data");
  const commentCountData = infoDiv.querySelector(".commentCount-data");

  if (commentForm) {
    commentForm.setAttribute("data-post-id", postIDData.innerText);
    postId.value = postIDData.innerText;
  }

  const comments = Array.from(infoDiv.querySelector(".comments-data").children);
  postComments.textContent = "";
  // postCommentCount.textContent = "";
  // commentersUsername.textContent = "";
  // commentContent.textContent = "";

  const postCommentCount = document.createElement("span");
  postCommentCount.classList.add("post-comments-count");
  postCommentCount.textContent = commentCountData.innerText;
  postComments.appendChild(postCommentCount);

  const br = document.createElement("br");
  postComments.appendChild(br);

  const expandedComments = document.createElement("span");
  expandedComments.classList.add("expanded-comments");

  for (const div of comments) {
    const spans = Array.from(div.children);
    const commentSpans = Array.from(spans[1].children);

    const comment = document.createElement("span");
    comment.classList.add("comment");

    const link = document.createElement("a");
    link.classList.add("comment-user-link");
    link.setAttribute("href", commentersProfileUrl
                                .replace("__commenters_id__", spans[0].innerText));
    
    const username = document.createElement("span");
    username.classList.add("commenters-username");
    username.textContent = commentSpans[0].innerText;
    link.appendChild(username);
    comment.appendChild(link);

    const content = document.createElement("span");
    content.classList.add("comment-content");
    content.textContent = commentSpans[1].innerText;
    comment.appendChild(content);

    const br = document.createElement("br");
    comment.appendChild(br);

    expandedComments.appendChild(comment);
  }

  postComments.appendChild(expandedComments);

  // Setting date.
  const date = infoDiv.querySelector(".date-data").innerText;
  modal.querySelector(".post-date").textContent = date;

  // Setting the post ID.
  const id = infoDiv.querySelector(".post-id-data").innerText;
  modal.querySelector(".post-id-details").children[0].textContent = id;

  // Setting like button image.
  const userHasLiked = infoDiv.querySelector(".user_has_liked-data")
                              .innerText
                              .toLowerCase();
  const likeImg = modal.querySelector(".post-like-btn img");

  const liked = "/static/community/images/liked-icon.svg";
  const like = "/static/community/images/like-icon.svg";

  likeImg.setAttribute("src", userHasLiked === "true" ? liked : like);

  // Displaying the modal.
  modal.style.display = "block";
}
