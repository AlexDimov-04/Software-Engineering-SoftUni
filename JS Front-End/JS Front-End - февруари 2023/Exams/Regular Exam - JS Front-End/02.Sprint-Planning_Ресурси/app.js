window.addEventListener('load', solve);

function solve() {
    const inputDOMSelectors = {
        title: document.getElementById('title'),
        description: document.getElementById('description'),
        label: document.getElementById('label'),
        estimatedPoints: document.getElementById('points'),
        assignee: document.getElementById('assignee'),
    }

    const otherDOMSelectors = {
        createTaskBtn: document.getElementById('create-task-btn'),
        deleteTaskBtn: document.getElementById('delete-task-btn'),
        section: document.getElementById('tasks-section'),
        paragraphPoints: document.getElementById('total-sprint-points'),
        hiddenInput: document.getElementById('task-id')
    }

    let taskData = {};
    const bugTypes = {
        'Feature': '⊡',
        'Low Priority Bug': '☉',
        'High Priority Bug': '⚠'
    }

    const classType = {
        'Feature': 'feature',
        'Low Priority Bug': 'low-priority',
        'High Priority Bug': 'high-priority'
    }
    let tasksCounter = 0;
    let estimatedPointsCounter = 0;
    let currentPoints = 0;
    let labelValue = null;

    otherDOMSelectors.createTaskBtn.addEventListener('click', createTaskHandler);
    otherDOMSelectors.deleteTaskBtn.addEventListener('click', deletePermanently);

    function createTaskHandler() {
        let allValidFields = Object.values(inputDOMSelectors)
            .every((input) => input.value !== '')

        if (!allValidFields) {
            return;
        }
        tasksCounter++;
        estimatedPointsCounter += Number(inputDOMSelectors.estimatedPoints.value)
        const article = createElement('article', null, otherDOMSelectors.section, `task-${tasksCounter}`, ['task-card']);
        createElement('div', inputDOMSelectors.label.value + ' ' + bugTypes[inputDOMSelectors.label.value], article, null, ['task-card-label', classType[inputDOMSelectors.label.value]]);
        createElement('h3', inputDOMSelectors.title.value, article, null, ['task-card-title']);
        createElement('p', inputDOMSelectors.description.value, article, null, ['task-card-description']);
        createElement('div', `Estimated at ${inputDOMSelectors.estimatedPoints.value} pts`, article, null, ['task-card-points']);
        createElement('div', `Assigned to: ${inputDOMSelectors.assignee.value}`, article, null, ['task-card-assignee']);
        const div = createElement('div', null, article, null, ['task-card-actions']);
        const deleteBtn = createElement('button', 'Delete', div);

        otherDOMSelectors.paragraphPoints.textContent = `Total Points ${estimatedPointsCounter}pts`;
        labelValue = inputDOMSelectors.label.value;

        Object.values(inputDOMSelectors).forEach(input => {
            input.value = '';
        });

        deleteBtn.addEventListener('click', deleteTaskHandler);
    }

    function deleteTaskHandler() {
        const taskPoints = this.parentNode.parentNode.getElementsByClassName('task-card-points')[0];
        currentPoints = Number(taskPoints.textContent.slice(13, 15));

        taskData = {
            title: this.parentNode.parentNode.getElementsByClassName('task-card-title')[0].textContent,
            description: this.parentNode.parentNode.getElementsByClassName('task-card-description')[0].textContent,
            label: labelValue,
            estimatedPoints: currentPoints,
            assignee: this.parentNode.parentNode.getElementsByClassName('task-card-assignee')[0].textContent.slice(13)
        }

        for (const key in inputDOMSelectors) {
            inputDOMSelectors[key].value = taskData[key];
        }

        otherDOMSelectors.deleteTaskBtn.disabled = false;
        otherDOMSelectors.createTaskBtn.disabled = true;

        Object.values(inputDOMSelectors).forEach(input => {
            input.disabled = true;
        });

        otherDOMSelectors.hiddenInput.value = this.parentNode.parentNode.id;
    }

    function deletePermanently() {
        const taskIdToBeDeleted = otherDOMSelectors.hiddenInput.value;
        const deletedTask = document.getElementById(taskIdToBeDeleted);
        deletedTask.remove();
     
        Object.values(inputDOMSelectors).forEach(input => {
            input.value = '';
        });

        Object.values(inputDOMSelectors).forEach(input => {
            input.disabled = false;
        });

        otherDOMSelectors.deleteTaskBtn.disabled = true;
        otherDOMSelectors.createTaskBtn.disabled = false;

        estimatedPointsCounter -= currentPoints;

        otherDOMSelectors.paragraphPoints.textContent = `Total Points ${estimatedPointsCounter}pts`;
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