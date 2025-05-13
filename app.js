import COURSE_DATA from "./sampleCourses.js";
const COURSE_JSON = JSON.parse(COURSE_DATA);

const coursesContainer = document.getElementById("courses-container");

function addCourse(courses) {
    for (var i = 0; i < courses.length; i++) {
        const course = courses[i];

        const card = document.createElement('div')

        // add the class game-card to the list
        card.classList.add('course-card')

        // set the inner HTML using a template literal to display some info
        // about each game
        const cards  = `
            <h2>${course.courseName} </h2>
            <p>${course.department} </p>
            <p>Total Pledged: ${game.pledged} </p>
            <p>Goal: ${game.goal} </p>
            `;
        course.innerHTML = courses;
    }

}

addCourse(COURSE_JSON);

