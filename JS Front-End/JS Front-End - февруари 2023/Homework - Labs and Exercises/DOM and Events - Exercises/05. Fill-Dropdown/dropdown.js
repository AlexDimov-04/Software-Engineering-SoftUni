function addItem() {
    const dropBox = document.querySelector('div #menu');
    const text = document.getElementById('newItemText');
    const value = document.getElementById('newItemValue');
    const option = document.createElement('option');

    option.textContent = text.value;
    option.value = value.value;

    dropBox.appendChild(option);

    text.value = '';
    value.value = '';
}