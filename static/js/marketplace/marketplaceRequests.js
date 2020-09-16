function getStocksOnCurrentPage(button) {
    document.querySelector('.active-paggination-button').classList.remove('active-paggination-button');

    fetch('stocks', 
    {
        method: 'POST',
        body: 'message=' + 'display' + '&active_page=' + button.textContent,
        mode: 'same-origin',
        headers: {'content-type': 'application/x-www-form-urlencoded', 'X-CSRFToken': getCookie('csrftoken') },
    })
    .then(response => {
        if (response.status !== 200) {
            return Promise.reject(); 
        }
        return response.json();
    })
    .then(response => {
        if (response['message'] === 'ok') {
            showCurrentPage(response, 'stocks');

            document.querySelectorAll('.paggination-button').forEach(element => {
                if (element.textContent === button.textContent) {
                    element.classList.add('active-paggination-button')
                }
            });;
        }
    })
    .catch(() => console.log('error response'));
}

function buyStock(button) {
    fetch('stocks', 
    {
        method: 'POST',
        body: 'message=' + 'buy' + '&stock_id=' + button.id,
        mode: 'same-origin',
        headers: {'content-type': 'application/x-www-form-urlencoded', 'X-CSRFToken': getCookie('csrftoken') },
    })
    .then(response => {
        if (response.status !== 200) {
            return Promise.reject(); 
        }
        return response.json();
    })
    .then(response => {
        if (response['message'] === 'ok') {
            document.getElementById('profile-dashboard').textContent = response['profile'];
            showModalPopUp('Successful purchase');
        } else {
            showModalPopUp(response['message']);
        }
    })
    .catch(() => console.log('error response'));
}