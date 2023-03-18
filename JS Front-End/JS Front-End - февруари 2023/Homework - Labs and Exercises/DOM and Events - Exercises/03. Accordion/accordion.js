function toggle() {
    const btn = document.getElementsByClassName('button')[0];
    const extraText = document.getElementById('extra');

    if (extraText.style.display === 'none') {
        extraText.style.display = 'block';
        btn.textContent = 'Less';
    } else {
        extraText.style.display = 'none';
        btn.textContent = 'More';
    }

}