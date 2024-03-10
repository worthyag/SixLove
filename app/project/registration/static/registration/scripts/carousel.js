const contents = document.querySelectorAll('.display-content');
let sliderContents = Array.from(contents);

const leftArrow = document.querySelector('.left');
const rightArrow = document.querySelector('.right');

console.log(leftArrow);

const dots = document.querySelectorAll('.nav-dot');
let navDots = Array.from(dots);

const startBtn = document.querySelector(".start-slides")
const stopBtn = document.querySelector(".stop-slides")


// Calling the appropriate functions whenever the user clicks 
// on the arrow buttons.
leftArrow.addEventListener('click', previousContent);
rightArrow.addEventListener('click', nextContent);

// Handles the automation.
let automate = setInterval(nextContent, 3000);
startBtn.addEventListener('click', () => {automate = setInterval(nextContent, 5000);});
stopBtn.addEventListener('click', () => {clearTimeout(automate)});

function previousContent() {
    /**
     * Function that displays the previous slide (content).
     */
    let pos = sliderContents.length;

    // Iterates over the slides and displays the content.
    for (let i = sliderContents.length - 1; i >= 0; i--) {        
        if (sliderContents[i].classList.contains('current')) {
            sliderContents[i].classList.toggle('current');
            navDots[i].classList.toggle('filled');
            pos = i-1;

            if (pos === -1) {
                pos = sliderContents.length - 1;
            }
            break;
        }
    }

    sliderContents[pos].classList.toggle('current');
    navDots[pos].classList.toggle('filled');
}

function nextContent() {
    /**
     * Function that displays the next slide (content).
     */
    let pos = -1;

    // Iterates over the slides and displays the content.
    for (let i = 0; i < sliderContents.length; i++) {        
        if (sliderContents[i].classList.contains('current')) {
            sliderContents[i].classList.toggle('current');
            navDots[i].classList.toggle('filled');
            pos = i+1;

            if (pos === sliderContents.length) {
                pos = 0;
            }
            break;
        }
    }

    sliderContents[pos].classList.toggle('current');
    navDots[pos].classList.toggle('filled');
}