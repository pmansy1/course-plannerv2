// -----  PAGE NAVIGATION  ------
const pages = document.querySelectorAll('.page');
const navButtons = document.querySelectorAll('[data-page]');

function showPage(pageId) {
  document.querySelectorAll('.page').forEach(p =>
    p.id === pageId
      ? p.classList.add('active')
      : p.classList.remove('active')
  );
  // Save current page to localStorage
  localStorage.setItem('currentPage', pageId);
}

// wire up nav buttons
navButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    showPage(btn.dataset.page);
  });
});

// initialize with saved page or default to home
const savedPage = localStorage.getItem('currentPage');
showPage(savedPage || 'home');


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

    // 4. Wire that "Back" button to return home
    detailSection
      .querySelector('button[data-page="home"]')
      .addEventListener('click', () => showPage('home'));
  });
}

// 4) Kick things off
displayCourses(sampleCourses);
showPage('home');



// -----  PLANNER  ------

// Create the planner container
function createTermContainer(term, plannerContainer) {
  const termContainer = document.createElement('div');
  termContainer.classList.add('term-container');
  termContainer.setAttribute('data-term', term);
  termContainer.innerHTML = `<h3>${term}</h3>`;
  plannerContainer.appendChild(termContainer);
  return termContainer;
}

// Create a course card element
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
    <button class="delete-course-button" data-course-id="${course.id}">Delete</button>
  `;
  return plannerCard;
}

// Save courses to localStorage
function saveCoursesToLocalStorage() {
  localStorage.setItem('addedCourses', JSON.stringify(addedCourses));
}

// Load courses from localStorage
function loadCoursesFromLocalStorage() {
  const savedCourses = localStorage.getItem('addedCourses');
  if (savedCourses) {
    addedCourses = JSON.parse(savedCourses);
    // Restore the course plan
    const plannerContainer = document.getElementById('my-classes-container');
    addedCourses.forEach(courseId => {
      const course = sampleCourses.find(c => c.id === courseId);
      if (course) {
        let termContainer = document.querySelector(`.term-container[data-term="${course.term}"]`);
        if (!termContainer) {
          termContainer = createTermContainer(course.term, plannerContainer);
        }
        const plannerCard = createCourseCard(course);
        termContainer.appendChild(plannerCard);
      }
    });
  }
}

// -----  ADD COURSE MODAL  ------

let addedCourses = []; // Array to track added courses

/// Populate the dropdown with courses from the sampleCourses array
function initializeAddCourseModal() {
  const addCourseButton = document.getElementById('add-course-button');
  const modal = document.getElementById('add-course-modal');
  const form = document.getElementById('add-course-form');
  const courseSelect = document.getElementById('course-select');
  const plannerContainer = document.getElementById('my-classes-container');
  const cancelButton = document.getElementById('cancel-btn');
  const submitButton = document.getElementById('submit-btn');


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
    
    // Save to localStorage
    saveCoursesToLocalStorage();

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


// ----- DELETE COURSE FUNCTIONALITY  ------

//TODO: Implement the delete functionality
function initializeDeleteCourseModal() {
  const plannerContainer = document.getElementById('my-classes-container');
  const deleteModal = document.getElementById('delete-course-modal');
  const confirmDeleteBtn = document.getElementById('confirm-delete-btn');
  const cancelDeleteBtn = document.getElementById('cancel-delete-btn');

  let courseToDelete = null; // Store the course card to delete

  // Open the delete modal
  plannerContainer.addEventListener('click', (event) => {
    if (event.target.classList.contains('delete-course-button')) {
      courseToDelete = event.target.closest('.course-card'); // Get the course card
      deleteModal.classList.add('active'); // Show the modal
    }
  });

  // Confirm delete
  confirmDeleteBtn.addEventListener('click', (event) => {
    event.preventDefault(); // Prevent form submission

    if (courseToDelete) {
      const courseId = parseInt(courseToDelete.querySelector('.delete-course-button').dataset.courseId, 10);

      // Remove the course from the addedCourses array
      const courseIndex = addedCourses.indexOf(courseId);
      if (courseIndex !== -1) {
        addedCourses.splice(courseIndex, 1);
      }

      // Save to localStorage after deletion
      saveCoursesToLocalStorage();

      // Remove the course card from the DOM
      const termContainer = courseToDelete.closest('.term-container');
      courseToDelete.remove();

      // Check if the term container is empty and remove it
      if (termContainer && termContainer.querySelectorAll('.course-card').length === 0) {
        termContainer.remove();
      }

      // Close the modal
      deleteModal.classList.remove('active');
      courseToDelete = null; // Reset the course to delete
    }
  });

  // Cancel delete
  cancelDeleteBtn.addEventListener('click', () => {
    deleteModal.classList.remove('active'); // Hide the modal
    courseToDelete = null; // Reset the course to delete
  });
}

// Initialize the delete course modal functionality
initializeDeleteCourseModal();

// Load saved courses when the page loads
loadCoursesFromLocalStorage();


