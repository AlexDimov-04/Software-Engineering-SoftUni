function deleteByEmail() {
    const result = document.getElementById('result');
    const email = document.getElementsByName('email')[0];
    const evenTds = Array.from(document.querySelectorAll('td:nth-child(2)'));
    let emailValue = email.value;
    let foundElement = evenTds.find((td) => td.textContent === emailValue);

    if (foundElement) {
        console.log(foundElement);
        foundElement.parentElement.remove();
        result.textContent = 'Deleted.';
    } else {
        result.textContent = 'Not found.';
    }
}