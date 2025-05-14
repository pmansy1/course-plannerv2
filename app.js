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



