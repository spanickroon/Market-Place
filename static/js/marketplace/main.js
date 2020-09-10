function showHiddenPasswordOnPasswordPage(target) {
    var input = document.getElementById('change-password-input');
    showHiddenPassword(target, input);
    return false;
}

function showHiddenRepeatPasswordOnPasswordPage(target) {
    var input = document.getElementById('change-password-input-repeat');
    showHiddenPassword(target, input);
    return false;
}

function hideModalPopUp(ev) {
    ev.preventDefault();

    document.getElementById('modal-popup').classList.remove('active-modal');
}

function setUpMarketplace() {
    var invalidPopupPassword = document.getElementById('invalid-popup-password-page');
    var passwordText = 'The password must contain at least:\n1 Capital letter of the English alphabet\n1 Capital letter of the English alphabet\n1 Number\nHave a length of at least 8';
    var modalPopUpButton = document.getElementById('modal-popup-button');

    setUpInvalidPopUp(invalidPopupPassword, document.getElementById('change-password-input'), passwordText);
    setUpInvalidPopUp(invalidPopupPassword, document.getElementById('change-password-input-repeat'), passwordText, true, document.getElementById('change-password-input'));
    
    modalPopUpButton.addEventListener('click', hideModalPopUp);
}

setUpMarketplace();
