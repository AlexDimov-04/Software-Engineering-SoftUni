
function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/';
    const loadBoardBtn = document.getElementById('load-board-btn');
    const title = document.getElementById('title');
    const description = document.getElementById('description');
    const addTaskBtn = document.getElementById('create-task-btn');
    const toDoUl = document.querySelector('#todo-section .task-list');
    const inProgressUl = document.querySelector('#in-progress-section .task-list');
    const codeReviewUl = document.querySelector('#code-review-section .task-list');
    const doneSectionUl = document.querySelector('#done-section .task-list');

    loadBoardBtn.addEventListener('click', loadData);
    addTaskBtn.addEventListener('click', addTaskHanlder);

    async function loadData() {
        try {
            const res = await fetch(BASE_URL);
            const data = await res.json();

            toDoUl.innerHTML = '';
            inProgressUl.innerHTML = '';
            codeReviewUl.innerHTML = '';
            doneSectionUl.innerHTML = '';
            let currentList = null;
            let btnText = '';

            for (const { title, description, status, _id } of Object.values(data)) {
                if (status === 'ToDo') {
                    currentList = toDoUl;
                    btnText = 'Move to In Progress';
                }
                else if (status === 'In Progress') {
                    currentList = inProgressUl;
                    btnText = 'Move to Code Review';
                }
                else if (status === 'Code Review') {
                    currentList = codeReviewUl;
                    btnText = 'Move to Done';
                }
                else if (status === 'Done') {
                    currentList = doneSectionUl;
                    btnText = 'Close';
                }

                const li = createElement('li', null, currentList, null, ['task']);
                createElement('h3', title, li);
                createElement('p', description, li);
                const submitBtn = createElement('button', btnText, li);

                submitBtn.status = status;
                submitBtn.taskId = _id;

                if (status === 'Done') {
                    submitBtn.addEventListener('click', deleteHandler);
                }
                else {
                    submitBtn.addEventListener('click', moveHandler);
                }
            }
        } catch (err) {
            console.error(err)
        }
    }

    async function addTaskHanlder(e) {
        try {
            e.preventDefault();
            const httpHeaders = {
                method: 'POST',
                body: JSON.stringify({
                    'title': title.value,
                    'description': description.value,
                    'status': 'ToDo'
                })
            }

            await fetch(BASE_URL, httpHeaders);
            loadData(e);
            title.value = '';
            description.value = '';
        } catch (err) {
            console.error(err);
        }
    }

    async function moveHandler(e) {
        try {
            const liStatus = this.status;
            const taskId = this.taskId;
            let newStatus = '';

            if (liStatus === 'ToDo') {
                newStatus = 'In Progress';
            }
            else if (liStatus === 'In Progress') {
                newStatus = 'Code Review';
            }
            else if (liStatus === 'Code Review') {
                newStatus = 'Done';
            }

            const httpHeaders = {
                method: 'PATCH',
                body: JSON.stringify({ status: newStatus })
            }

            await fetch(`${BASE_URL}${taskId}`, httpHeaders);
            loadData(e);
        } catch (err) {
            console.error(err);
        }
    }

    async function deleteHandler(e) {
        try {
            const taskId = this.taskId;
            const httpHeaders = {
                method: 'DELETE'
            };

            await fetch(`${BASE_URL}${taskId}`, httpHeaders);
            loadData(e);

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