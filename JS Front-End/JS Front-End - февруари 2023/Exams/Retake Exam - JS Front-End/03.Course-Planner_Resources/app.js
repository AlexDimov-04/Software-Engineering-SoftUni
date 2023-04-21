function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/';
    const loadCoursesBtn = document.getElementById('load-course');
    const listContainer = document.getElementById('list');
    const addCourseBtn = document.getElementById('add-course');
    const editCourseBtn = document.getElementById('edit-course');

    const courseTitle = document.getElementById('course-name');
    const courseType = document.getElementById('course-type');
    const description = document.getElementById('description');
    const teacherName = document.getElementById('teacher-name');

    loadCoursesBtn.addEventListener('click', loadCoursesHandler);
    addCourseBtn.addEventListener('click', addCourseHandler);
    editCourseBtn.addEventListener('click', editFullyData);

    let currentId = null;

    async function loadCoursesHandler() {
        try {
            const res = await fetch(BASE_URL);
            const data = await res.json();


            listContainer.textContent = '';
            for (const { description, teacher, title, type, _id } of Object.values(data)) {
                const div = createElement('div', null, listContainer, _id, ['container']);
                createElement('h2', title, div);
                createElement('h3', teacher, div);
                createElement('h3', type, div);
                createElement('h4', description, div);
                const editCoursesBtn = createElement('button', 'Edit Course', div, null, ['edit-btn']);
                const finishCoursesBtn = createElement('button', 'Finish Course', div, null, ['finish-btn']);

                editCoursesBtn.addEventListener('click', editCourseHandler);
                finishCoursesBtn.addEventListener('click', async (e) => {
                    try {
                        e.preventDefault();
                        const httpHeaders = {
                            method: 'DELETE'
                        }

                        await fetch(BASE_URL + e.target.parentNode.id, httpHeaders);
                        loadCoursesHandler(e);
                    } catch (err) {
                        console.error(err);
                    }
                });


            }
        } catch (err) {
            console.error(err)
        }
    }

    async function addCourseHandler(e) {
        try {
            e.preventDefault();
            const httpHeaders = {
                method: 'POST',
                body: JSON.stringify({
                    'title': courseTitle.value,
                    'type': courseType.value,
                    'description': description.value,
                    'teacher': teacherName.value
                })
            }

            await fetch(BASE_URL, httpHeaders);
            loadCoursesHandler(e);

            courseTitle.value = '';
            courseType.value = '';
            description.value = '';
            teacherName.value = '';
        } catch (err) {
            console.error(err);
        }
    }

    async function editCourseHandler() {
        try {
            const divContainer = this.parentNode;
            currentId = divContainer.id;

            const coursetitle = divContainer.querySelector('.container h2');
            const teachername = divContainer.querySelector('.container h3:nth-child(2)');
            const coursetype = divContainer.querySelector('.container h3:nth-child(3)');
            const descriptioncourse = divContainer.querySelector('.container h4');

            courseTitle.value = coursetitle.textContent;
            courseType.value = coursetype.textContent;
            description.value = descriptioncourse.textContent;
            teacherName.value = teachername.textContent;

            divContainer.remove();

            addCourseBtn.disabled = true;
            editCourseBtn.disabled = false;
        } catch (err) {
            console.error(err);
        }
    }

    async function editFullyData(e) {
        try {
            e.preventDefault(e);
            const httpHeaders = {
                method: 'PUT',
                body: JSON.stringify({
                    'title': courseTitle.value,
                    'type': courseType.value,
                    'description': description.value,
                    'teacher': teacherName.value
                })
            }

            await fetch(BASE_URL + currentId, httpHeaders);
            loadCoursesHandler(e);

            addCourseBtn.disabled = false;
            editCourseBtn.disabled = true;

            courseTitle.value = '';
            courseType.value = '';
            description.value = '';
            teacherName.value = '';
        } catch (err) {
            console.error(err);
        }
    }


    function createElement(type, content, parentNode, id, classes, attrs) {
        const htmlElement = document.createElement(type);

        if (content && type !== 'input') {
            htmlElement.textContent = content;
        }

        if (content && type === 'input') {
            htmlElement.value = content;
        }

        if (id) {
            htmlElement.id = id;
        }

        if (classes) {
            htmlElement.classList.add(...classes);
        }

        if (parentNode) {
            parentNode.appendChild(htmlElement);
        }

        if (attrs) {
            for (const key in attrs) {
                htmlElement.setAttribute(key, attrs[key]);
            };
        };

        return htmlElement;
    };
}

attachEvents();