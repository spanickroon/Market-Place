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

function setUpMarketplace() {
    var invalidPopupPassword = document.getElementById('invalid-popup-password-page');
    var passwordText = 'The password must contain at least:\n1 Capital letter of the English alphabet\n1 Capital letter of the English alphabet\n1 Number\nHave a length of at least 8'

    setUpInvalidPopUp(invalidPopupPassword, document.getElementById('change-password-input'), passwordText);
    setUpInvalidPopUp(invalidPopupPassword, document.getElementById('change-password-input-repeat'), passwordText, true, document.getElementById('change-password-input'));
}

setUpMarketplace();