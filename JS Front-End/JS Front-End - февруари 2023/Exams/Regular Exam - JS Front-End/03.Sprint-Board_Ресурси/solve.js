
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

            for (const { title, description, status, _id } of Object.values(data)) {
                if (status === 'ToDo') {
                    const li = createElement('li', null, toDoUl, null, ['task']);
                    li.id = _id;
                    createElement('h3', title, li);
                    createElement('p', description, li);
                    const moveBtn = createElement('button', 'Move to In Progress', li)

                    moveBtn.addEventListener('click', async (e) => {
                        Array.from(toDoUl.children).forEach(liItem => {
                            const button = liItem.children[2].textContent = 'Move to Code Review';
                            inProgressUl.appendChild(liItem);
                        });

                        const httpHeaders = {
                            method: 'PATCH',
                            body: JSON.stringify({ toDoUl })
                        }

                        const res = await fetch(BASE_URL + this.parentNode.id, httpHeaders);
                        loadData(e);
                    })
                }
                else if (status === 'In Progress') {
                    inProgressUl.textContent = '';
                    const li = createElement('li', null, inProgressUl, null, ['task']);
                    li.id = _id;
                    createElement('h3', title, li);
                    createElement('p', description, li);
                    const moveBtn = createElement('button', 'Move to Code Review', li)

                    moveBtn.addEventListener('click', async (e) => {
                        moveBtn.textContent = 'Move to Done';
                        Array.from(inProgressUl.children).forEach(liItem => {
                            const button = liItem.children[2].textContent = 'Move to Done';
                            codeReviewUl.appendChild(liItem);
                        });

                        const httpHeaders = {
                            method: 'PATCH',
                            body: JSON.stringify({ inProgressUl })
                        }

                        const res = await fetch(BASE_URL + this.parentNode.id, httpHeaders);
                        loadData(e);
                    })
                }
                else if (status === 'Code Review') {
                    codeReviewUl.textContent = '';
                    const li = createElement('li', null, codeReviewUl, null, ['task']);
                    li.id = _id;
                    createElement('h3', title, li);
                    createElement('p', description, li);
                    const moveBtn = createElement('button', 'Move to Done', li)

                    moveBtn.addEventListener('click', async (e) => {
                        moveBtn.textContent = 'Close'
                        Array.from(codeReviewUl.children).forEach(liItem => {
                            const button = liItem.children[2].textContent = 'Close';
                            doneSectionUl.appendChild(liItem);
                        });

                        const httpHeaders = {
                            method: 'PATCH',
                            body: JSON.stringify({ codeReviewUl })
                        }

                        const res = await fetch(BASE_URL + this.parentNode.id, httpHeaders);
                        loadData(e);
                    })
                }
                else if (status === 'Done') {
                    doneSectionUl.textContent = '';
                    const li = createElement('li', null, doneSectionUl, null, ['task']);
                    li.id = _id;
                    createElement('h3', title, li);
                    createElement('p', description, li);
                    const closeBtn = createElement('button', 'Close', li);

                    const httpHeaders = {
                        method: 'PATCH',
                        body: JSON.stringify({ doneSectionUl })
                    }

                    const res = await fetch(BASE_URL + this.parentNode.id, httpHeaders);
                    loadData(e);

                    closeBtn.addEventListener('click', async (e) => {
                
                            let liItemId = e.currentTarget.parentNode.id;
                            const httpHeaders = {
                                method: 'DELETE'
                            }

                            const res = await fetch(BASE_URL + liItemId, httpHeaders);
                            loadData(e);
 
                            console.error(err);    
                    })
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

            const res = await fetch(BASE_URL, httpHeaders);
            loadData(e);
            title.value = '';
            description.value = '';
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