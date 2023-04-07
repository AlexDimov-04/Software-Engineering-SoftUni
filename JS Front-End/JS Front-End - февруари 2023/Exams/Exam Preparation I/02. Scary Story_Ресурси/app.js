window.addEventListener("load", solve)

function solve() {
  const inputDOMSelectors = {
    firstName: document.getElementById('first-name'),
    lastName: document.getElementById('last-name'),
    age: document.getElementById('age'),
    storyTitle: document.getElementById('story-title'),
    genre: document.getElementById('genre'),
    myStory: document.getElementById('story')
  }

  const otherDOMSelectors = {
    publishBtn: document.getElementById('form-btn'),
    ul: document.getElementById('preview-list'),
    main: document.getElementById('main')
  }

  let personalData = {};

  otherDOMSelectors.publishBtn.addEventListener('click', publishInfoHandler);

  function publishInfoHandler() {
    let allValidFields = Object.values(inputDOMSelectors)
      .every((input) => input.value !== '');

    if (!allValidFields) {
      return;
    }

    const li = createElement('li', null, otherDOMSelectors.ul, null, ['story-info']);
    const article = createElement('article', null, li);
    createElement('h4', `Name: ${inputDOMSelectors.firstName.value + ' ' + inputDOMSelectors.lastName.value}`, article);
    createElement('p', `Age: ${inputDOMSelectors.age.value}`, article);
    createElement('p', `Title: ${inputDOMSelectors.storyTitle.value}`, article);
    createElement('p', `Genre: ${inputDOMSelectors.genre.value}`, article);
    createElement('p', `${inputDOMSelectors.myStory.value}`, article);
    const saveBtn = createElement('button', 'Save Story', li, null, ['save-btn']);
    const editBtn = createElement('button', 'Edit Story', li, null, ['edit-btn']);
    const deleteBtn = createElement('button', 'Delete Story', li, null, ['delete-btn']);

    personalData = {
      firstName: inputDOMSelectors.firstName.value,
      lastName: inputDOMSelectors.lastName.value,
      age: inputDOMSelectors.age.value,
      storyTitle: inputDOMSelectors.storyTitle.value,
      genre: inputDOMSelectors.genre.value,
      myStory: inputDOMSelectors.myStory.value
    }

    saveBtn.addEventListener('click', saveInfoHandler);
    editBtn.addEventListener('click', editInfoHandler);
    deleteBtn.addEventListener('click', deleteInfoHandler);

    Object.values(inputDOMSelectors).forEach(input => {
      input.value = '';
    });

    otherDOMSelectors.publishBtn.disabled = true;
  }

  function editInfoHandler() {
    this.parentNode.remove();

    for (const key in inputDOMSelectors) {
      inputDOMSelectors[key].value = personalData[key];
    }

    otherDOMSelectors.publishBtn.disabled = false;
  }

  function saveInfoHandler() {
    let mainChildren = Array.from(otherDOMSelectors.main.children);

    mainChildren.forEach(child => {
      child.remove();
    });

    createElement('h1', "Your scary story is saved!", otherDOMSelectors.main);
  }

  function deleteInfoHandler() {
    this.parentNode.remove();
    otherDOMSelectors.publishBtn.disabled = false;
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
