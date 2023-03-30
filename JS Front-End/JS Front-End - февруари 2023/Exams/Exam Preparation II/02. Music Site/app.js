window.addEventListener('load', solve);

function solve() {
    const genreInput = document.getElementById('genre');
    const songNameInput = document.getElementById('name');
    const songAuthorInput = document.getElementById('author');
    const dateOfCreationInput = document.getElementById('date');
    const addBtn = document.getElementById('add-btn');
    const allHitsContainer = document.getElementsByClassName('all-hits-container')[0];
    const likesCounter = document.querySelector('#total-likes .likes p');
    const savedContainer = document.getElementsByClassName('saved-container')[0];
    let likes = 0;

    addBtn.addEventListener('click', (e) => {
        e.preventDefault();

        if (validInputs(genreInput.value, songNameInput.value, songAuthorInput.value, dateOfCreationInput.value)) {
            const divContainer = createElement('div', null, allHitsContainer, null, ['hits-info']);
            const img = createElement('img', null, divContainer, null, null, { src: './static/img/img.png' });
            const h2Genre = createElement('h2', `Genre: ${genreInput.value}`, divContainer);
            const h2Name = createElement('h2', `Name: ${songNameInput.value}`, divContainer);
            const h2Author = createElement('h2', `Author: ${songAuthorInput.value}`, divContainer);
            const h3 = createElement('h3', `Date: ${dateOfCreationInput.value}`, divContainer);
            const saveBtn = createElement('button', 'Save song', divContainer, null, ['save-btn']);
            const likeBtn = createElement('button', 'Like song', divContainer, null, ['like-btn']);
            const deleteBtn = createElement('button', 'Delete', divContainer, null, ['delete-btn']);

            genreInput.value = '';
            songNameInput.value = '';
            songAuthorInput.value = '';
            dateOfCreationInput.value = '';

            likeBtn.addEventListener('click', (e) => {
                e.preventDefault();
                likes++;
                likesCounter.textContent = `Total Likes: ${likes}`;

                e.currentTarget.disabled = true;
            });

            saveBtn.addEventListener('click', (e) => {
                e.preventDefault();
                const divContainerChildren = Array.from(divContainer.children);
                divContainer.removeChild(divContainerChildren[5]);
                divContainer.removeChild(divContainerChildren[6]);

                savedContainer.appendChild(divContainer);
            });

            deleteBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.currentTarget.parentNode.remove();
            });
        };


    });

    function validInputs(genre, name, author, date) {
        if (genre.length > 0 && name.length > 0 && author.length > 0 && date.length > 0) {
            return true;
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

