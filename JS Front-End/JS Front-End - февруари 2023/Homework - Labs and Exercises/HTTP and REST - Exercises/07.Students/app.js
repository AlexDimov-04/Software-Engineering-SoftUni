function attachEvents() {
  window.addEventListener('load', loadDataHandler);
  const BASE_URL = 'http://localhost:3030/jsonstore/collections/students/';
  const tbody = document.getElementsByTagName('tbody')[0];
  const firstNameInput = document.getElementsByName('firstName')[0];
  const lastNameInput = document.getElementsByName('lastName')[0];
  const facultyNumberInput = document.getElementsByName('facultyNumber')[0];
  const gradeInput = document.getElementsByName('grade')[0];
  const submitBtn = document.getElementById('submit');

  submitBtn.addEventListener('click', addStudentHandler);

  async function loadDataHandler() {
    tbody.textContent = '';
    const res = await fetch(BASE_URL);
    const data = await res.json();

    for (const { firstName, lastName, facultyNumber, grade, _id } of Object.values(data)) {
      const tr = createElement('tr', '', tbody);
      const td1 = createElement('td', firstName, tr);
      const td2 = createElement('td', lastName, tr);
      const td3 = createElement('td', facultyNumber, tr);
      const td4 = createElement('td', grade, tr);
    }
  }

  async function addStudentHandler() {
    const firstNameValue = firstNameInput.value;
    const lastNameValue = lastNameInput.value;
    const facultyNumberValue = facultyNumberInput.value;
    const gradeValue = gradeInput.value;

    const httpHeaders = {
      method: 'POST',
      body: JSON.stringify({
        'firstName': firstNameValue,
        'lastName': lastNameValue,
        'facultyNumber': facultyNumberValue,
        'grade': gradeValue,
      })
    };

    firstNameInput.value = '';
    lastNameInput.value = '';
    facultyNumberInput.value = '';
    gradeInput.value = '';

    const res = await fetch(BASE_URL, httpHeaders);
    loadDataHandler();
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
      }
    }

    return htmlElement;
  }
}

attachEvents();