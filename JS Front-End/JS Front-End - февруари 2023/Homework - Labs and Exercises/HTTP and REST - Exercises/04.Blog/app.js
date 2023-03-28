function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/blog/posts/';
    const COMMENTS_URL = 'http://localhost:3030/jsonstore/blog/comments/';
    const loadBtn = document.getElementById('btnLoadPosts');
    const viewBtn = document.getElementById('btnViewPost');
    const select = document.getElementById('posts');
    const paragraph = document.getElementById('post-body');
    const ul = document.getElementById('post-comments');
    const h1 = document.getElementById('post-title');
    let postsIds = {};

    loadBtn.addEventListener('click', loadPostsHandler);
    viewBtn.addEventListener('click', viewPostsHandler);

    async function loadPostsHandler() {
        try {
            const dataRes = await fetch(BASE_URL);
            const data = await dataRes.json();

            for (const key in data) {
                const option = document.createElement('option');
                option.value = data[key].id;
                option.textContent = data[key].title;

                postsIds[data[key].id] = { 'name': option.textContent, 'body': data[key].body };

                select.appendChild(option);
            }
        }
        catch (err) {
            console.error(err);
        }
    };

    async function viewPostsHandler() {
        try {
            ul.textContent = '';
            paragraph.textContent = '';
            const res = await fetch(COMMENTS_URL);
            const data = await res.json();

            h1.textContent = postsIds[select.value].name;
            paragraph.textContent = postsIds[select.value].body;

            let comments = {};
            let commentsIds = {};

            for (const line of Object.values(data)) {
                if (!comments.hasOwnProperty(line.postId)) {
                    comments[line.postId] = [line.text];
                } else {
                    comments[line.postId].push(line.text);
                }
                commentsIds[line.text] = line.id;
            }

            for (const [key, value] of Object.entries(comments)) {
                if (key === select.value) {
                    for (const comment of value) {
                        const li = document.createElement('li');
                        li.textContent = comment;
                        li.id = commentsIds[comment];

                        ul.appendChild(li);
                    }
                }
            }
        }
        catch (err) {
            console.error(err);
        }
    }
}

attachEvents();