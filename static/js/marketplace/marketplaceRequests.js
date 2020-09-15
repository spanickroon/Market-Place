function getStocksOnCurrentPage(button) {
    console.log(button);

    document.querySelector('.active-paggination-button').classList.remove('active-paggination-button');

    fetch('stocks', 
    {
        method: 'POST',
        body: 'active_page=' + button.textContent,
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