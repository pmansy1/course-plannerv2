// -----  PAGE NAVIGATION  ------
const pages = document.querySelectorAll('.page');
const navButtons = document.querySelectorAll('[data-page]');

function showPage(pageId) {
  document.querySelectorAll('.page').forEach(p =>
    p.id === pageId
      ? p.classList.add('active')
      : p.classList.remove('active')
  );
}

// wire up nav buttons
navButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    showPage(btn.dataset.page);
  });
});

// initialize
showPage('home');


// -----  DISPLAYING COURSE CARDS  ------
import sampleCourses from '../../../sampleCourses.js';

const coursesContainer = document.getElementById('courses-container');

function displayCourses(courses) {
  courses.forEach(course => {
    // 1. Create the card in the Home view
    const card = document.createElement('div');
    card.classList.add('course-card');
    card.innerHTML = `<h2>${course.courseName}</h2>`;
    coursesContainer.appendChild(card);

    // 2. When you click the card, go to its detail page
    card.addEventListener('click', () => {
      showPage(`course-${course.id}`);
    });

    // 3. Create a hidden <section> for that course
    const detailSection = document.createElement('section');
    detailSection.classList.add('page');
    detailSection.id = `course-${course.id}`;
    detailSection.innerHTML = `
      <button data-page="home" >← Back</button>
      <h1>${course.courseName}</h1>
      <p><strong>Professor:</strong> ${course.professor}</p>
      <p><strong>Department:</strong> ${course.department} (${course.departmentId})</p>
      <!-- add more fields here if you want -->
    `;
    document.body.appendChild(detailSection);

    // 4. Wire that “Back” button to return home
    detailSection
      .querySelector('button[data-page="home"]')
      .addEventListener('click', () => showPage('home'));
  });
}

// 4) Kick things off
displayCourses(sampleCourses);
showPage('home');



// -----  PLANNER  ------

// Create a function to handle adding a course to the planner
let addedCourses = []; // Array to store added courses

function initializeAddCourseButton() {
  const addCourseButton = document.getElementById('add-course-button');
  const modal = document.getElementById('modal');

  addCourseButton.addEventListener('click', () => {
    modal.classList.add('active'); // Show the modal
  });
}

function initializeCancelButton() {
  const cancelButton = document.getElementById('cancel-button');
  const modal = document.getElementById('modal');
  const form = document.getElementById('course-form');

  cancelButton.addEventListener('click', () => {
    modal.classList.remove('active'); // Hide the modal
    form.reset(); // Reset the form fields
  });
}

function createTermContainer(term, plannerContainer) {
  const termContainer = document.createElement('div');
  termContainer.classList.add('term-container');
  termContainer.setAttribute('data-term', term);
  termContainer.innerHTML = `<h3>${term}</h3>`;
  plannerContainer.appendChild(termContainer);
  return termContainer;
}

function createCourseCard(course) {
  const plannerCard = document.createElement('div');
  plannerCard.classList.add('course-card');
  plannerCard.innerHTML = `
    <h2>${course.courseName}</h2>
    <p><strong>Professor:</strong> ${course.professor}</p>
    <p><strong>Department:</strong> ${course.department}</p>
    <p><strong>Term:</strong> ${course.term}</p>
  `;
  return plannerCard;
}

function handleAddCourse() {
  const confirmButton = document.getElementById('confirm-button');
  const modal = document.getElementById('modal');
  const form = document.getElementById('course-form');
  const plannerContainer = document.getElementById('my-classes-container');

  confirmButton.addEventListener('click', () => {
    const courseName = document.getElementById('course-name').value;
    const professor = document.getElementById('professor').value;
    const department = document.getElementById('department').value;
    const term = document.getElementById('term-select').value;

    const newCourse = {
      courseName,
      professor,
      department,
      term,
    };

    // Check if a container for the selected term exists
    let termContainer = document.querySelector(`.term-container[data-term="${term}"]`);
    if (!termContainer) {
      termContainer = createTermContainer(term, plannerContainer);
    }

    // Create and append the course card
    const plannerCard = createCourseCard(newCourse);
    termContainer.appendChild(plannerCard);

    // Add the new course to the addedCourses array
    addedCourses.push(newCourse);

    modal.classList.remove('active'); // Hide the modal
    form.reset(); // Reset the form fields
  });
}

function addCourseToPlanner() {
  initializeAddCourseButton();
  initializeCancelButton();
  handleAddCourse();
}

addCourseToPlanner();

