function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/';
    const loadAllBtn = document.getElementById('load-button');
    const addBtn = document.getElementById('add-button');
    const title = document.getElementById('title');
    const toDoList = document.getElementById('todo-list');

    loadAllBtn.addEventListener('click', loadDataHandler);
    addBtn.addEventListener('click', addTaskHandler);

    async function loadDataHandler(e) {
        try {
            e.preventDefault();
            const res = await fetch(BASE_URL);
            const data = await res.json();

            toDoList.textContent = '';
            for (const { name, _id } of Object.values(data)) {
                const li = createElement('li', null, toDoList, _id);
                createElement('span', `${name}`, li,);
                const removeBtn = createElement('button', 'Remove', li);
                const editBtn = createElement('button', 'Edit', li);

                removeBtn.addEventListener('click', removeTaskHandler);
                editBtn.addEventListener('click', editTaskHandler);
            }
        } catch (err) {
            console.error(err);
        }
    }

    async function addTaskHandler(e) {
        try {
            e.preventDefault();
            const name = title.value;
            const httpHeaders = {
                method: 'POST',
                body: JSON.stringify({ name })
            }

            const res = await fetch(BASE_URL, httpHeaders);
            loadDataHandler(e);
            title.value = '';
        } catch (err) {
            console.error(err);
        }
    }

    async function removeTaskHandler(e) {
        try {
            let liItemId = this.parentNode.id;
            const httpHeaders = {
                method: 'DELETE'
            }

            const res = await fetch(BASE_URL + liItemId, httpHeaders);
            loadDataHandler(e);
        } catch (err) {
            console.error(err);
        }
    }

    async function editTaskHandler(e) {
        try {     
            if (this.textContent === 'Edit') {
                const span = this.parentNode.getElementsByTagName('span')[0];
                const input = createElement('input', span.textContent);
                this.parentNode.replaceChild(input, span);
                this.textContent = 'Submit';
            } else {
                const name = this.parentNode.getElementsByTagName('input')[0].value;
                const httpHeaders = {
                    method: 'PATCH',
                    body: JSON.stringify({ name })
                }

                const res = await fetch(BASE_URL + this.parentNode.id, httpHeaders);
                loadDataHandler(e);
                this.textContent = 'Edit';
            }
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
