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

let invalidPopupPassword = document.getElementById('invalid-popup-password-page');

setUpInvalidPopUp(invalidPopupPassword, document.getElementById('change-password-input'), passwordText);
setUpInvalidPopUp(invalidPopupPassword, document.getElementById('change-password-input-repeat'), passwordText, true, document.getElementById('change-password-input'));
