function getCookie(name) {
    var cookieValue = null;

    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
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
        console.log(response['message'])
    })
    .catch(() => console.log('error response'));
} 


document.getElementById('signup-button').addEventListener('click', signUp);