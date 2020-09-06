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
            app.nav(ev);
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
            app.nav(ev);
        }
        console.log(response['message']);
    })
    .catch(() => console.log('error response'));
} 

function logout() {
    console.log('logout');
    return false;
}

document.getElementById('login-button').addEventListener('click', login);
document.getElementById('signup-button').addEventListener('click', signUp);
