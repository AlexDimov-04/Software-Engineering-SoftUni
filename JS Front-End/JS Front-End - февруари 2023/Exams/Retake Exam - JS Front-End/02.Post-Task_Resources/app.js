// window.addEventListener("load", solve);

function solve() {
    const inputDOMSelectors = {
        title: document.getElementById('task-title'),
        category: document.getElementById('task-category'),
        textarea: document.getElementById('task-content')
    }

    const otherDOMSelectors = {
        publishBtn: document.getElementById('publish-btn'),
        reviewList: document.getElementById('review-list'),
        publishedList: document.getElementById('published-list')
    }

    let data = {};


    otherDOMSelectors.publishBtn.addEventListener('click', getInfoHandler);

    function getInfoHandler(e) {
        let allValidFields = Object.values(inputDOMSelectors)
            .every((input) => input.value !== '');

        if (!allValidFields) {
            return;
        }

        otherDOMSelectors.reviewList.textContent = '';
        const li = createElement('li', null, otherDOMSelectors.reviewList, null, ['rpost']);
        const article = createElement('article', null, li);
        createElement('h4', inputDOMSelectors.title.value, article);
        createElement('p', `Category: ${inputDOMSelectors.category.value}`, article);
        createElement('p', `Content: ${inputDOMSelectors.textarea.value}`, article);
        const editBtn = createElement('button', 'Edit', li, null, ['action-btn', 'edit']);
        const postBtn = createElement('button', 'Post', li, null, ['action-btn', 'post']);

        data = {
            title: inputDOMSelectors.title.value,
            category: inputDOMSelectors.category.value,
            textarea: inputDOMSelectors.textarea.value
        }

        Object.values(inputDOMSelectors).forEach(input => {
            input.value = '';
        });

        editBtn.addEventListener('click', editInfoHandler);
        postBtn.addEventListener('click', postTaskHandler);
    }

    function editInfoHandler() {
        this.parentNode.remove()

        for (const key in inputDOMSelectors) {
            inputDOMSelectors[key].value = data[key];
        }
    }

    function postTaskHandler() {
        const liItem = this.parentNode;
        const editButton = liItem.getElementsByClassName('edit')[0];
        editButton.remove();
        const postButton = liItem.getElementsByClassName('post')[0];
        postButton.remove();

        otherDOMSelectors.publishedList.appendChild(liItem);
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