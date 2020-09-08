function login(ev) {
    ev.preventDefault();

    fetch('login', 
    {
        method: 'POST',
        body: 'username=' + document.getElementById('input-login').value + '&password=' + document.getElementById('input-password-login').value,
        mode: 'same-origin',
        headers: {'content-type': 'application/x-www-form-urlencoded', 'X-CSRFToken': getCookie('csrftoken') },
    })
    .then(response => {
        if (response.status !== 200) {
            return Promise.reject(); 
        }
        return response.json()
    })
    .then(response => {
        if (response['message'] === 'ok') {
            currentPage = 'profile';

            document.getElementById(currentPage).innerHTML = response['template'];

            document.querySelector('.active-page').classList.remove('active-page');
            document.getElementById(currentPage).classList.add('active-page');

            document.querySelectorAll('.nav-target').forEach((link) => {
                link.addEventListener('click', app.nav);    
            })

            history.pushState({}, currentPage, currentPage);
        } else {
            showModalPopUp(response['message']);
        }
        console.log(response['message']);
    })
    .catch(() => console.log('error response'));
} 

function signUp(ev) {
    ev.preventDefault();

    fetch('signup', 
    {
        method: 'POST',
        body: 'username=' + document.getElementById('input-login-signup').value + '&password1=' + document.getElementById('input-password-signup').value + '&password2=' + document.getElementById('input-password-signup-repeat').value,
        headers: {'content-type': 'application/x-www-form-urlencoded', 'X-CSRFToken': getCookie('csrftoken') },
    })
    .then(response => {
        if (response.status !== 200) {
            return Promise.reject(); 
        }
        return response.json()
    })
    .then(response => {
        if (response['message'] === 'ok') {
            document.getElementById('input-login-signup').value = '';
            document.getElementById('input-password-signup').value = '';
            document.getElementById('input-password-signup-repeat').value = '';
            
            showModalPopUp('Successful registration. Go to the login tab.');
        } else {
            showModalPopUp(response['message']);
        }
        console.log(response['message']);
    })
    .catch(() => console.log('error response'));
} 

function showModalPopUp(message) {
    document.getElementById('modal-popup-text').textContent = message;
    document.getElementById('modal-popup').classList.add('active-modal');
}

function logout() {
    console.log('logout');
    return false;
}
