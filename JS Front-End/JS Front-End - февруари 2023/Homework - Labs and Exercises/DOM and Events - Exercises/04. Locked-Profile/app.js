function lockedProfile() {
    const btns = Array.from(document.getElementsByTagName('button'));
    btns
        .forEach((btn) => {
            btn.addEventListener('click', toggleInformation);
        });

    function toggleInformation(e) {
        debugger;
        const btn = e.currentTarget;
        const currentProfile = btn.parentNode;
        const children = Array.from(currentProfile.children);
        const unlockRadioInput = children[4];
        const additionalInformationDiv = children[9];

        if (unlockRadioInput.checked) {
            if (btn.textContent === 'Show more') {
                additionalInformationDiv.style.display = 'block';
                btn.textContent = 'Hide it';
            } else {
                additionalInformationDiv.style.display = 'none';
                btn.textContent = 'Show more';
            }
        }
    }
}