function print(x) {
  console.log(x);
}

const tennisSessionsDiv = document.querySelector("#TennisSessions");

let tennisSessions = JSON.parse(tennisSessionsDiv.innerHTML);


tennisSessions.forEach(session => {
  if (session.isCompleted === "False")
    session.isCompleted = false;
  else
    session.isCompleted = true;

  let dateParts = session.date.split("-");
  session.date = new Date(dateParts[0], dateParts[1] - 1, dateParts[2]);
});

print(tennisSessions);

// function tennisSessionScheduled(date, session) {
//   if (`${date.getFullYear()}-${date.getMonth()}-${date.getDate()}` ===
//    `${session.date.getFullYear()}-${session.date.getMonth()}-${session.date.getDate()}`) {
//     return true;
//   }
//   else {
//     return false;
//   }
// }


const calendar = document.querySelector(".calendar");
const date = document.querySelector(".date");
const daysDiv = document.querySelector(".days");

const prevBtn = document.querySelector(".prev-btn");
const nextBtn = document.querySelector(".next-btn");
const todayBtn = document.querySelector(".today-btn");
const selectDateBtn = document.querySelector(".selectDate-btn");
const datePicker = document.querySelector("#selectDatePicker");

let today = new Date();
let activeDay;
let year = today.getFullYear();
let month = today.getMonth();

// Setting the date picker to begin with.
let monthDatePicker = (month >= 9) ? month + 1 : `0${month + 1}`;
parseInt(datePicker.value.slice(5, 7)) - 1;
datePicker.value = `${year}-${monthDatePicker}`;


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
  // print(tennisSessions);

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

  // Function to check if a date has a tennis session
  function hasTennisSession(date) {
    return tennisSessions.some(session => {
      const sessionDate = new Date(session.date);
      return (
        date.getFullYear() === sessionDate.getFullYear() &&
        date.getMonth() === sessionDate.getMonth() &&
        date.getDate() === sessionDate.getDate()
      );
    });
  }


  // Adding the previous month days.
  for (let i = day; i > 0; i--) {
    // const currentDate = new Date(year, month, prevTotalDays - i + 1);
    // const hasSession = hasTennisSession(currentDate);
    // days += `<div class="day prev-date ${hasSession ? 'tennis-session' : ''}">${prevTotalDays - i + 1}</div>`;
    days += `<div class="day prev-date">${prevTotalDays - i + 1}</div>`;
  }

  // Adding the current month days.
  for (let i = 1; i <= currentTotalDays; i++) {
    const currentDate = new Date(year, month, i);
    const hasSession = hasTennisSession(currentDate);
    const isToday = currentDate.toDateString() === today.toDateString();
    days += `<div class="day ${isToday ? 'today' : ''} ${hasSession ? 'tennis-session' : ''}">${i}</div>`;
  }

  // Adding the next month days.
  for (let i = 1; i <= nextDays; i++) {
    // const currentDate = new Date(year, month + 1, i);
    // const hasSession = hasTennisSession(currentDate);
    // days += `<div class="day next-date ${hasSession ? 'tennis-session' : ''}">${i}</div>`;
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
prevBtn.addEventListener("click", prevMonth);
nextBtn.addEventListener("click", nextMonth);

// Today btn functionality.
todayBtn.addEventListener("click", () => {
  today = new Date();
  year = today.getFullYear();
  month = today.getMonth();
  buildCalendar();
});

// Select date functionality.
datePicker.addEventListener("change", (e) => {
  year = parseInt(datePicker.value.slice(0, 4));
  month = parseInt(datePicker.value.slice(5, 7)) - 1;
  buildCalendar();
})

// function updateCalendar(tennisSessions) {
//   // Modify your calendar based on the received data
//   // ...
//   console.log("You called the updateCalendar function.");
// }


// // Fetch data using AJAX
// function fetchData() {
//   fetch('/planner/ajax-calendar/')
//     .then(response => response.json())
//     .then(data => buildCalendar(data.tennis_sessions));
// }

// fetchData();

// Fetch HTML content using AJAX
// function fetchData() {
//   fetch('/planner/calendar/')
//     .then(response => response.text())
//     .then(data => {
//       tennisSessions = data;
//       buildCalendar()
//     });
// }

// fetchData();

// TODO: Turn these functions into a class, with the calendar variable as an attribute.



