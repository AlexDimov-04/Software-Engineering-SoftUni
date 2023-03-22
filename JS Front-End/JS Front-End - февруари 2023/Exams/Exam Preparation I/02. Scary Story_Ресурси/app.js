window.addEventListener("load", solve)


function solve() {
  const firstName = document.getElementById('first-name');
  const lastName = document.getElementById('last-name');
  const age = document.getElementById('age');
  const storyTitle = document.getElementById('story-title');
  const genre = document.getElementById('genre');
  const previewList = document.getElementById('preview-list');
  const textarea = document.getElementById('story');
  const publishBtn = document.getElementById('form-btn');
  const main = document.getElementById('main');
  const formWrapper = document.getElementsByClassName('form-wrapper')[0];
  const sideWrapper = document.getElementById('side-wrapper');
  let inputData = [];
  const li = document.createElement('li');
  li.classList.add('story-info');

  const article = document.createElement('article');

  const saveBtn = document.createElement('button');
  saveBtn.textContent = 'Save Story';
  saveBtn.classList.add('save-btn');

  const editBtn = document.createElement('button');
  editBtn.textContent = 'Edit Story'
  editBtn.classList.add('edit-btn');

  const deleteBtn = document.createElement('button');
  deleteBtn.textContent = 'Delete Story'
  deleteBtn.classList.add('delete-btn');

  publishBtn.addEventListener('click', () => {
    if (firstName.value.length > 0 && lastName.value.length > 0 && age.value.length > 0 && storyTitle.value.length > 0 && genre.value.length > 0 && textarea.value.length > 0) {
      article.textContent = '';

      article.innerHTML += `
      <h4>Name: ${firstName.value + ' ' + lastName.value}</h4> 
      <p>Age: ${age.value}</p>
      <p>Title: ${storyTitle.value}</p>
      <p>Genre: ${genre.value}</p>
      <p>${textarea.value}</p>
  `;



      inputData = [];
      inputData.push(firstName.value, lastName.value, age.value, storyTitle.value, genre.value, textarea.value)

      previewList.appendChild(li);
      li.appendChild(article);

      li.appendChild(saveBtn);
      li.appendChild(editBtn);
      li.appendChild(deleteBtn);

      firstName.value = '';
      lastName.value = '';
      age.value = '';
      storyTitle.value = '';
      genre.value = '';
      textarea.value = '';
      publishBtn.disabled = true;
    }
  });


  editBtn.addEventListener('click', () => {
    let [first, last, yearsOld, storyTitleName, genreType, storyContent] = inputData;

    firstName.value = first;
    lastName.value = last;
    age.value = yearsOld;
    storyTitle.value = storyTitleName;
    genre.value = genreType;
    textarea.value = storyContent;

    previewList.removeChild(li);
    publishBtn.disabled = false;
  });

  saveBtn.addEventListener('click', () => {
    main.removeChild(formWrapper);
    main.removeChild(sideWrapper);

    const h1 = document.createElement('h1');
    h1.textContent = "Your scary story is saved!";
    main.appendChild(h1);
  });

  deleteBtn.addEventListener('click', () => {
    previewList.removeChild(li);
    publishBtn.disabled = false;
  });
}
