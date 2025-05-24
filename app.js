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
import sampleCourses from './sampleCourses.js';

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
  const addCourseButton = document.getElementById('create-course-button');
  const modal = document.getElementById('create-course-modal');

  addCourseButton.addEventListener('click', () => {
    modal.classList.add('active'); // Show the modal
  });
}

function initializeCancelButton() {
  const cancelButton = document.getElementById('cancel-button');
  const modal = document.getElementById('create-course-modal');
  const form = document.getElementById('create-course-form');

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
    <p><strong>Department ID:</strong> ${course.departmentId}</p>
    <p><strong>Term:</strong> ${course.term}</p>
    <p><strong>Course Credits:</strong> ${course.credits}</p>
  `;
  return plannerCard;
}

function handleAddCourse() {
  const confirmButton = document.getElementById('confirm-button');
  const modal = document.getElementById('create-course-modal');
  const form = document.getElementById('create-course-form');
  const plannerContainer = document.getElementById('my-classes-container');

  confirmButton.addEventListener('click', () => {
    event.preventDefault(); // Prevent form submission

    const courseName = document.getElementById('course-name').value;
    const professor = document.getElementById('professor').value;
    const department = document.getElementById('department').value;
    const term = document.getElementById('term-select').value;
    const departmentId = document.getElementById('department-id').value;
    const credits = document.getElementById('credits').value;

    const newCourse = {
      courseName,
      professor,
      department,
      term,
      departmentId,
      credits
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


// -----  ADD COURSE MODAL  ------

/// Populate the dropdown with courses from the sampleCourses array
function initializeAddCourseModal() {
  const addCourseButton = document.getElementById('add-course-button');
  const modal = document.getElementById('add-course-modal');
  const form = document.getElementById('add-course-form');
  const courseSelect = document.getElementById('course-select');
  const plannerContainer = document.getElementById('my-classes-container');
  const cancelButton = document.getElementById('cancel-btn');
  const submitButton = document.getElementById('submit-btn');

  const addedCourses = []; // Array to track added courses

  // Populate the dropdown with courses
  function populateDropdown() {
    courseSelect.innerHTML = ''; // Clear existing options

    // Add a default "Select a course" option
    const defaultOption = document.createElement('option');
    defaultOption.value = '';
    defaultOption.textContent = 'Select a course';
    defaultOption.disabled = true;
    defaultOption.selected = true;
    courseSelect.appendChild(defaultOption);

    // Populate the dropdown with courses
    sampleCourses.forEach(course => {
      const option = document.createElement('option');
      option.value = course.id; // Use the course ID as the value
      option.textContent = `${course.courseName} (${course.term})`;

      if (addedCourses.includes(course.id)) {
        option.disabled = true;
        option.textContent += ' (Already Added)';
      }
      
      courseSelect.appendChild(option);
    });
  }

  // Show the modal and populate the dropdown
  addCourseButton.addEventListener('click', () => {
    populateDropdown();
    modal.classList.add('active'); // Show the modal
  });

  // Handle adding the selected course
  submitButton.addEventListener('click', (event) => {
    event.preventDefault(); // Prevent form submission

    const selectedCourseId = parseInt(courseSelect.value, 10);
    if (isNaN(selectedCourseId)) {
      alert('Please select a valid course before adding.');
      return;
    }

    // Find the selected course from the sampleCourses array
    const selectedCourse = sampleCourses.find(course => course.id === selectedCourseId);
    if (!selectedCourse) {
      console.error('Selected course not found in the sampleCourses array.');
      return;
    }

    // Check if a container for the selected term exists
    let termContainer = document.querySelector(`.term-container[data-term="${selectedCourse.term}"]`);
    if (!termContainer) {
      termContainer = createTermContainer(selectedCourse.term, plannerContainer);
    }

    // Create and append the course card
    const plannerCard = createCourseCard(selectedCourse);
    termContainer.appendChild(plannerCard);

    // Add the selected course ID to the addedCourses array
    addedCourses.push(selectedCourse.id);

    // Close the modal and reset the form
    modal.classList.remove('active');
    form.reset();
  });

  // Handle cancel button
  cancelButton.addEventListener('click', () => {
    modal.classList.remove('active'); // Hide the modal
    form.reset(); // Reset the form fields
  });
}

initializeAddCourseModal();
