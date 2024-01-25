const parentDiv = document.querySelectorAll(".form-btn-group");
// const childButtons = document.querySelectorAll(".child-btn");

for (let i = 0; i < parentDiv.length; i++) {
  parentDiv[i].addEventListener('click', () => {
    // triggerButtonClick(i)
    console.log("clicked");
    parentDiv[i].querySelector(':first-child').click();
    
  });
};

// function triggerButtonClick(i) {
//   console.log("clicked");
//   // e.querySelector(':first-child').click();
//   childButtons[i].click();
// }