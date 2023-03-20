function lockedProfile() {
    const btns = Array.from(document.getElementsByTagName('button'));

    btns.forEach((btn) => {
        btn.addEventListener('click', triggerBtn);
    });

    function triggerBtn(e) {
        const btn = e.currentTarget;
        const children = Array.from(btn.parentNode.children);
        const unlockField = children[4];
        const hiddenData = children[9];

        if (unlockField.checked) {
            if (btn.textContent === 'Show more') {
                hiddenData.style.display = 'block';
                btn.textContent = 'Hide it';
            } else {
                hiddenData.style.display = 'none';
                btn.textContent = 'Show more';
            }
        }
    }
}