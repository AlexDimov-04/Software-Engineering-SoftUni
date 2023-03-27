function attachEvents() {
    const phonebookContainer = document.getElementById('phonebook');
    const loadBtn = document.getElementById('btnLoad');
    const BASE_URL = 'http://localhost:3030/jsonstore/phonebook/';
    const [personInput, phoneInput] = document.getElementsByTagName('input');
    const createBtn = document.getElementById('btnCreate');

    loadBtn.addEventListener('click', loadPhoneBookHandler);
    createBtn.addEventListener('click', createPhoneBookHandler);

    async function loadPhoneBookHandler() {
        try {
            const phonebookRes = await fetch(BASE_URL);
            let phonebookData = await phonebookRes.json();
            let values = Object.values(phonebookData);
            phonebookContainer.innerHTML = '';

            for (const { phone, person, _id } of values) {
                const li = document.createElement('li');
                const button = document.createElement('button');
                button.textContent = 'Delete';
                button.id = _id;
                button.addEventListener('click', deletePhoneBookHandler);

                li.innerHTML = `${person}: ${phone}`
                li.appendChild(button);

                phonebookContainer.appendChild(li);
            }
        } catch (error) {
            console.error(error);
        }
    }

    function createPhoneBookHandler() {
        const person = personInput.value;
        const phone = phoneInput.value;
        const httpHeaders = {
            method: 'POST',
            body: JSON.stringify({ person, phone }),
        }

        fetch(BASE_URL, httpHeaders)
            .then((res) => res.json())
            .then(() => {
                loadPhoneBookHandler();
                personInput.value = '';
                phoneInput.value = '';
            })
            .catch(err => {
                console.error(err);
            })
    }

    async function deletePhoneBookHandler() {
        try {
            const id = this.id;
            const httpHeaders = {
                method: 'DELETE'
            };

            let deletePhoneBookRes = await fetch(BASE_URL + id, httpHeaders);
            let deletePhoneBookData = await deletePhoneBookRes.json();
            loadPhoneBookHandler();
        }
        catch (error) {
            console.error(error);
        }
    }
}

attachEvents();