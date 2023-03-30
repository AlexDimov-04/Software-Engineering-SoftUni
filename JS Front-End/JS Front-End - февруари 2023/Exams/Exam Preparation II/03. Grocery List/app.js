function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/grocery/';
    const productName = document.getElementById('product');
    const count = document.getElementById('count');
    const price = document.getElementById('price');
    const addBtn = document.getElementById('add-product');
    const updateBtn = document.getElementById('update-product');
    const loadAllBtn = document.getElementById('load-product');

    loadAllBtn.addEventListener('click', async (e) => {
        const res = await fetch(BASE_URL);
        const data = await res.json();
        console.log(data)
    });


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