function focused() {
    const inputs = document.querySelectorAll('div div input');

    for (let index = 0; index < inputs.length; index++) {
        let input = inputs[index];
        input.addEventListener("focus", () => {
            input.parentElement.classList.add('focused');
        });
    
        input.addEventListener('blur', () => {
            input.parentElement.classList.remove('focused');
        });
    }

}