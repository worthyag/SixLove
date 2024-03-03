const followButton = document.querySelector('.follow-btn');

followButton.addEventListener("click", (e) => {
  // Preventing the default form submission.
  e.preventDefault(); 

  const userProfileId = followButton.dataset.targetUserId;
  const action = followButton.dataset.action;

  toggleFollow(userProfileId, action, followButton);
});

// Function to handle follow or unfollow action
function toggleFollow(userProfileId, action, followButton) {
  // Sending an AJAX request to the Django backend to toggle follow status.
  fetch(toggleFollowUrl.replace("__user_profile_id__", userProfileId), {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken'), // Including CSRF token.
      },
  })
      .then(response => response.json())
      .then(data => {
          // Updating the UI based on the response.
          if (data.is_following) {
              // When the user is followed, update the UI.
              followButton.textContent = 'Unfollow';
              followButton.classList.add('unfollow-button');
              followButton.classList.remove('follow-button');
          } else {
              // User the is unfollowed, update the UI.
              followButton.textContent = 'Follow';
              followButton.classList.add('follow-button');
              followButton.classList.remove('unfollow-button');
          }

          // Updating follower and following counts in the UI.
          const followersCountElement = document.querySelector('.follower-count');
          const followingCountElement = document.querySelector('.following-count');

          followersCountElement.textContent = data.followers_count;
          followingCountElement.textContent = data.following_count;
      })
      .catch(error => console.error('Error:', error));
}

// Helper function to get CSRF token from cookies.
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

