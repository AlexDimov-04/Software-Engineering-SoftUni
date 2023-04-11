function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/grocery/';
    const productName = document.getElementById('product');
    const countNumbers = document.getElementById('count');
    const priceNumbers = document.getElementById('price');
    const addBtn = document.getElementById('add-product');
    const updateProductBtn = document.getElementById('update-product');
    const loadAllBtn = document.getElementById('load-product');
    const tbody = document.getElementById('tbody');
    let currentTrId = null;

    loadAllBtn.addEventListener('click', loadDataHandler);

    async function loadDataHandler(e) {
        try {
            e.preventDefault();
            const res = await fetch(BASE_URL);
            const data = await res.json();

            tbody.textContent = '';
            for (const { product, count, price, _id } of Object.values(data)) {
                const tr = createElement('tr', null, tbody, _id);
                createElement('td', `${product}`, tr, null, ['name']);
                createElement('td', `${count}`, tr, null, ['count-products']);
                createElement('td', `${price}`, tr, null, ['product-price']);
                const tdButtonsContainer = createElement('td', null, tr, null, ['btn']);
                const updateBtn = createElement('button', 'Update', tdButtonsContainer, null, ['update']);
                const deleteBtn = createElement('button', 'Delete', tdButtonsContainer, null, ['delete']);

                deleteBtn.addEventListener('click', async (e) => {
                    const id = tdButtonsContainer.parentNode.id;
                    const httpHeaders = {
                        method: 'DELETE',
                    }

                    const res = await fetch(BASE_URL + id, httpHeaders);
                    loadDataHandler(e);
                });

                updateBtn.addEventListener('click', async (e) => {
                    const event = e.currentTarget;
                    const eventParent = event.parentNode.parentNode;
                    currentTrId = eventParent.id;
                    const product = eventParent.getElementsByClassName('name')[0];

                    const countItems = eventParent.getElementsByClassName('count-products')[0];
                    const priceItems = eventParent.getElementsByClassName('product-price')[0];
                    updateProductBtn.disabled = false;
                    addBtn.disabled = true;

                    productName.value = product.textContent;
                    countNumbers.value = countItems.textContent;
                    priceNumbers.value = priceItems.textContent;
                });

            }
        }
        catch (err) {
            console.error(err);
        }
    }

    addBtn.addEventListener('click', async (e) => {
        try {
            e.preventDefault();
            const httpHeaders = {
                method: 'POST',
                body: JSON.stringify({
                    'product': productName.value,
                    'count': countNumbers.value,
                    'price': priceNumbers.value
                })
            };

            const res = await fetch(BASE_URL, httpHeaders);
            loadDataHandler(e);
            productName.value = '';
            countNumbers.value = '';
            priceNumbers.value = '';
        }
        catch (err) {
            console.error(err);
        }
    });

    updateProductBtn.addEventListener('click', async (e) => {
        try {
            const httpHeaders = {
                method: 'PATCH',
                body: JSON.stringify({
                    'product': productName.value,
                    'count': countNumbers.value,
                    'price': priceNumbers.value
                })
            };

            const res = await fetch(BASE_URL + currentTrId, httpHeaders);
            loadDataHandler(e);

            productName.value = '';
            countNumbers.value = '';
            priceNumbers.value = '';

            updateProductBtn.disabled = true;
            addBtn.disabled = false;
        }
        catch (err) {
            console.error(err);
        }
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