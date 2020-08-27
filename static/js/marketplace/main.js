function showHidePassword4(target) {
    var input = document.getElementById('change-password-input');
    showHidePassword(target, input);
    return false;
}

function showHidePassword5(target) {
    var input = document.getElementById('change-password-input-repeat');
    showHidePassword(target, input);
    return false;
}

let invalidPopupPassword = document.getElementById('invalid-popup-password-page');

setUpInvalidPopUp(invalidPopupPassword, document.getElementById('change-password-input'), passwordText);
setUpInvalidPopUp(invalidPopupPassword, document.getElementById('change-password-input-repeat'), passwordText, true, document.getElementById('change-password-input'));
