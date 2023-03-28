function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/messenger';
    const textarea = document.getElementById('messages');
    const author = document.getElementsByName('author')[0];
    const content = document.getElementsByName('content')[0];
    const sendBtn = document.getElementById('submit');
    const refreshBtn = document.getElementById('refresh');

    sendBtn.addEventListener('click', postInformationHandler);
    refreshBtn.addEventListener('click', refreshInformationHandler);

    async function postInformationHandler() {
        try {
            const name = author.value;
            const message = content.value;
            const httpHeaders = {
                method: 'POST',
                body: JSON.stringify({
                    "author": name,
                    "content": message
                })
            };

            const res = await fetch(BASE_URL, httpHeaders);
            author.value = '';
            content.value = '';
        }
        catch (err) {
            console.error(err)
        }
    }

    async function refreshInformationHandler() {
        try {
            const res = await fetch(BASE_URL);
            const data = await res.json();

            let output = [];
            for (const input of Object.values(data)) {
                output.push(`${input.author}: ${input.content}`);
            }

            textarea.textContent = output.join('\n');
        }
        catch (err) {
            console.error(err);
        }
    }
}

attachEvents();