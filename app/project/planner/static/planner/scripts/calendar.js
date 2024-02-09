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

// print(tennisSessions); // for testing.


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
// parseInt(datePicker.value.slice(5, 7)) - 1;
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
  // Clear the content of daysDiv
  daysDiv.innerHTML = '';

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
    const dayElement = document.createElement('div');
    dayElement.classList.add('day', 'prev-date');
    dayElement.textContent = prevTotalDays - i + 1;

    daysDiv.appendChild(dayElement);
  }

  // Adding the current month days.
  for (let i = 1; i <= currentTotalDays; i++) {
    const currentDate = new Date(year, month, i);
    const hasSession = hasTennisSession(currentDate);
    const isToday = currentDate.toDateString() === today.toDateString();

    
    const dayElement = document.createElement('div');
    dayElement.classList.add('day', isToday ? 'today' : 'day', hasSession ? 'tennis-session' : 'day');
    dayElement.textContent = i;

    dayElement.addEventListener('click', () => showSidePanel(i));

    daysDiv.appendChild(dayElement);
  }

  // Adding the next month days.
  for (let i = 1; i <= nextDays; i++) {
    const dayElement = document.createElement('div');
    dayElement.classList.add('day', 'next-date');
    dayElement.textContent = i;

    daysDiv.appendChild(dayElement);
  }

  // daysDiv.innerHTML = days;
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

function addCloseBtn() {
  const closeBtn = document.createElement('button');
  closeBtn.textContent = "Close"
  closeBtn.addEventListener('click', () => closeSidePanel());
  sidePanel.appendChild(closeBtn);
}

function addAddSessionBtn() {
  const addSessionBtn = document.createElement('button');
  addSessionBtn.textContent = "Add New Tennis Session"
  addSessionBtn.addEventListener('click', () => addSession());
  sidePanel.appendChild(addSessionBtn);
}

function showSidePanel(day) {
  const sidePanel = document.querySelector("#sidePanel");
  sidePanel.innerHTML = ''; // Clear previous content

  // Check if there are tennis sessions for the clicked day
  const sessionsForDay = tennisSessions.filter(session => {
    const sessionDate = new Date(session.date);
    return (
      year === sessionDate.getFullYear() &&
      month === sessionDate.getMonth() &&
      day === sessionDate.getDate()
    );
  });

  if (sessionsForDay.length === 0) {
    addCloseBtn();

    // No tennis sessions scheduled
    const sessionP = document.createElement('p');
    sessionP.textContent = "No tennis sessions scheduled.";
    sidePanel.appendChild(sessionP);

    addAddSessionBtn();
  } 
  else {
    addCloseBtn();

    // Display tennis session info in the side panel
    sessionsForDay.forEach(session => {
      const sessionDiv = document.createElement('div');
      sessionDiv.innerHTML = `
        <p>Title: ${session.title}</p>
        <p>Date: ${getMonth(session.date.getMonth() - 1)[1]} ${session.date.getDate()}, ${session.date.getFullYear()} </p>
        <p>Notes: ${session.notes}</p>
        <p>Completed: ${session.isCompleted ? 'Yes' : 'No'}</p>
        <button onclick="editSession(${session.id})">Edit</button>
        <button onclick="deleteSession(${session.id})">Delete</button>
      `;
      sidePanel.appendChild(sessionDiv);

      addAddSessionBtn()
    });
  }

  // Show the side panel
  sidePanel.style.display = 'block';
}

function closeSidePanel() {
  // Hide the side panel
  sidePanel.style.display = 'none';
}

function editSession(sessionId) {
  // Implement the logic to open a form or modal for editing the session
  console.log(`Edit session with ID ${sessionId}`);
}

function deleteSession(sessionId) {
  // Implement the logic to delete the session
  console.log(`Delete session with ID ${sessionId}`);
}

function addSession() {
   // Implement the logic to open a form or modal for adding the session
   console.log(`So you want to add a session`);
}
