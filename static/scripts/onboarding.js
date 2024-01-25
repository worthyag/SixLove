// Triggering Button Clicks.
const parentDiv = document.querySelectorAll(".form-btn-group");
// const childButtons = document.querySelectorAll(".child-btn");

for (let i = 0; i < parentDiv.length; i++) {
  parentDiv[i].addEventListener('click', (event) => {
    // triggerButtonClick(i)
    // console.log("clicked");
    // parentDiv[i].querySelector(':first-child').click();

    if (event.target.children[0]) {
      event.target.children[0].click();
      console.log("Click event triggered on the first child.");
    }
    
  });
};

// function triggerButtonClick(i) {
//   console.log("clicked");
//   // e.querySelector(':first-child').click();
//   childButtons[i].click();
// }


// Displaying questions based on responses.
nextButtons = document.querySelectorAll(".next-btn");

for (const nextButton of nextButtons) {
  nextButton.addEventListener('click', (event) => {
    nextQuestion(event);
  })
};

function nextQuestion(event) {
  console.log("Looks like you caught me!");

  const parent = event.target.parentElement;
  const sibling = parent.nextElementSibling;

  console.log(parent);
  console.log(sibling);

  // First checking that the element exits.
  if (parent) {
      parent.style.display = "none";

      // Checking that the sibling element exits.
      if (sibling) {
        sibling.style.display = "block";
      }
  }
}