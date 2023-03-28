function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/';
    const input = document.getElementById('title');
    const addBtn = document.getElementById('add-button');
    const loadBtn = document.getElementById('load-button');
    const ul = document.getElementById('todo-list');

    loadBtn.addEventListener('click', loadDataHandler);
    addBtn.addEventListener('click', addTaskHandler);

    async function loadDataHandler(e) {
        e.preventDefault();
        
        const res = await fetch(BASE_URL);
        const data = await res.json();
        
        ul.textContent = '';
        for (const { name, _id } of Object.values(data)) {
            const li = createElement('li', '', ul);
            li.id = _id;

            const span = createElement('span', name, li);
            const removeBtn = createElement('button', 'Remove', li);
            const editBtn = createElement('button', 'Edit', li);

            removeBtn.addEventListener('click', async (e) => {
                const id = e.target.parentNode.id;
                const httpHeaders = {
                    method: 'DELETE'
                };
                const res = await fetch(`${BASE_URL}${id}`, httpHeaders);
                loadDataHandler(e);
            });

            editBtn.addEventListener('click', async (e) => {
                const event = e.target;
                const eventParent = event.parentElement;

                if (editBtn.textContent === 'Edit') {
                    const span = eventParent.querySelector('span');
                    const input = createElement('input');
                    input.value = span.textContent;

                    eventParent.replaceChild(input, span);
                    event.textContent = 'Submit';
                } else {
                    const input = eventParent.querySelector('input');
                    const span = createElement('span');
                    span.value = input.value;

                    eventParent.replaceChild(span, input);

                    const httpHeaders = {
                        method: 'PATCH',
                        body: JSON.stringify({
                            name: span.value
                        })
                    }

                    const res = await fetch(`${BASE_URL}${eventParent.id}`, httpHeaders);
                    loadDataHandler(e);

                    event.textContent = 'Edit';
                }
            });
        };
    };

    async function addTaskHandler(e) {
        e.preventDefault();

        const name = input.value;
        const httpHeaders = {
            method: 'POST',
            body: JSON.stringify({ name })
        };

        const res = await fetch(BASE_URL, httpHeaders);
        loadDataHandler(e);
        input.value = '';
    };


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
