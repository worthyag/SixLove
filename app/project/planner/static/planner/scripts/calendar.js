function print(x) {
  console.log(x);
}

const calendar = document.querySelector(".calendar");
const date = document.querySelector(".date");
const daysDiv = document.querySelector(".days");

const prevBtn = document.querySelector(".prev-btn");
const nextBtn = document.querySelector(".next-btn");

let today = new Date();
let activeDay;
let year = today.getFullYear();
let month = today.getMonth();

function getMonth(month) {
  month = month + 1;

  const months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
  };

  return [month - 1, months[month]];
}

function buildCalendar() {
  /** Adds the days to the calendar. */

  // Getting info about the previous and current month days.
  const currentFirstDay = new Date(year, month, 1);
  const currentLastDay = new Date(year, month + 1, 0);
  const prevLastDay = new Date(year, month, 0);

  const prevTotalDays = prevLastDay.getDate();
  const currentTotalDays = currentLastDay.getDate();
  const day = currentFirstDay.getDay() - 1;
  const nextDays = 7 - currentLastDay.getDay();

  // Updating the date.
  date.textContent = `${getMonth(month)[1]} ${year}`;

  // Adding the days to the DOM.
  let days = "";

  // Adding the previous month days.
  for (let i = day; i > 0; i--) {
    days += `<div class="day prev-date">${prevTotalDays - i + 1}</div>`;
  }

  // Adding the current month days.
  for (let i = 1; i <= currentTotalDays; i++) {
    // If the day is the current day, add the today class.
    if ((i === new Date().getDate()) && (year === new Date().getFullYear()) && 
        (month === new Date().getMonth()))
          days += `<div class="day today">${i}</div>`;
    else
      days += `<div class="day">${i}</div>`;

  }

  // Adding the next month days.
  for (let i = 1; i <= nextDays; i++) {
    days += `<div class="day next-date">${i}</div>`;
  }

  daysDiv.innerHTML = days;
}

buildCalendar();

function prevMonth() {
  /** */
  month--;

  if (month < 0) {
    month = 11;
    year--;
  }

  buildCalendar();
}

function nextMonth() {
  /** */
  month++;

  if (month > 11) {
    month = 0;
    year++;
  }

  buildCalendar();
}

// Adding event listeners to the prevBtn and nextBtn.
prevBtn.addEventListener('click', prevMonth);
nextBtn.addEventListener('click', nextMonth);


// TODO: Turn these functions into a class, with the calendar variable as an attribute.



