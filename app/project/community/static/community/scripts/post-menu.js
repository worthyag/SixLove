const postMoreBtn =  document.querySelectorAll(".post-more-btn");

for (const btn of postMoreBtn) {
  btn.addEventListener("click", (e) => {
    displayActionMenu(e.target, btn.nextElementSibling);
  });
}

function displayActionMenu(btn, div) {
  const moreURL = "/static/community/images/more-icon.svg";
  const closeURL = "/static/community/images/close-icon.svg";

  if (btn.getAttribute("src") === moreURL) {
    btn.setAttribute("src", closeURL);
    div.classList.remove("hide-action-btns");
  } 
  else {
    btn.setAttribute("src", moreURL);
    div.classList.add("hide-action-btns");
  }
}