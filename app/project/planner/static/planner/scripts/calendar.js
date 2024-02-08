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

print(year);
print(month);

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
  const day = currentFirstDay.getDate();
  const nextDays = 7 - currentLastDay.getDay();

  // Updating the date.
  date.textContent = `${getMonth(month)[1]} ${year}`;
}



// TODO: Turn these functions into a class, with the calendar variable as an attribute.


function getDayOfWeek(day) {
  const daysOfWeek = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
  };

  return [day, daysOfWeek[day]];
}

function getDateInfo(date) {
  const date_info = {
    "date": date,
    "year": date.getFullYear(),
    "month": getMonth(date.getMonth()),
    "dayOfWeek": getDayOfWeek(date.getDay()),
    "day": date.getDate()

  };

  return date_info;
}

function checkLeapYear(year) {
  // Three conditions to find out the leap year.
  if ((0 == year % 4) && (0 != year % 100) || (0 == year % 400)) {
      return true;
  } else {
      return false;
  }
}

function getNumberOfDays(month, year) {
  const months = {
    1: 31,
    2: [28, 29],
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
  };

  if (month !== 2) 
    return months[month];
  else if (checkLeapYear(year))
    return months[month][1]
  else
    return months[month][0]
}

function buildCalendar2(date = "today") {
  const today = new Date();
  let date_info = "";

  if (date !== "today") {
    date_info = getDateInfo(date);
  }
  else {
    date_info = getDateInfo(today);
    print(date_info);
  }

  const numberOfDays = getNumberOfDays(date_info["month"][0], date_info["year"]);
  print(numberOfDays);

  const calendarDiv = document.createElement("div");
  calendarDiv.classList.add("calendarDiv");

  for (let i = 0; i < numberOfDays; i++) {
    const div = document.createElement("div");
    div.classList.add("dayDiv");

    const day = document.createElement("p");
    day.textContent = i + 1;
    day.classList.add("day");

    // Fix this.
    if (((i + 1) === date_info["day"]) && 
    (getDateInfo(today)["month"] == date_info["month"])) {
      day.classList.add("currentDay");
    }

    div.appendChild(day);

    // For testing
    const task1 = document.createElement("div");
    task1.classList.add("task");
    div.appendChild(task1);

    calendarDiv.appendChild(div);
  }

  calendar.appendChild(calendarDiv);
}

buildCalendar();
