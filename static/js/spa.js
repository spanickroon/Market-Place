/*---------------SPA---------------*/
var app = {
    pages: [],
    show: new Event('show'),
    init: function() {
        app.pages = document.querySelectorAll('.page');
        app.pages.forEach((pg) => {
            pg.addEventListener('show', app.pageShown);
        })

        document.querySelectorAll('.nav-target').forEach((link) => {
            link.addEventListener('click', app.nav);
        });

        window.addEventListener('popstate', app.poppin);
    },
    nav: function(ev) {
        ev.preventDefault();

        let currentPage = ev.target.getAttribute('data-target');

        document.querySelector('.active-page').classList.remove('active-page');
        document.getElementById(currentPage).classList.add('active-page');
        
        history.pushState({}, currentPage, currentPage);

        document.getElementById(currentPage).dispatchEvent(app.show);
    },
    poppin: function(ev) {
        let hash = location.pathname.replace('/', '');
        document.querySelector('.active-page').classList.remove('active-page');
        document.getElementById(hash).classList.add('active-page');

        document.getElementById(currentPage).dispatchEvent(app.show);
    },
    pageShown: function(ev) {
        ev.preventDefault();

        let currentPage = document.querySelector('.active-page').getAttribute('id');
        transitionLoader(currentPage);

        fetch(currentPage, {
            method: 'GET',
            headers: {'content-type': 'application/x-www-form-urlencoded'},
        })
        .then(response => {
            if (response.status !== 200) {
                return Promise.reject(); 
            }
            return response.text();
        })
        .then(response => {
            parser = new DOMParser();
            doc = parser.parseFromString(response, 'text/html');
            document.querySelector('.active-page').innerHTML = doc.getElementById(currentPage).innerHTML;
            
            receivedPageHandler(currentPage);
        })
        .catch(() => console.log('error spa response'));
    }
}

/*------Page transition loader------*/
function transitionLoader(currentPage) {
    if (currentPage !== 'login' && currentPage !== 'signup') {
        document.querySelector('.active-page').innerHTML = document.getElementById('pageloader').innerHTML;
        
        document.querySelectorAll('.nav-target').forEach(element => {
            element.classList.remove('nav-target');
            element.classList.add('nav-link-not-active');
        });
    }
}

/*------Received page handler------*/
function receivedPageHandler(currentPage) {
    setUpAuthentication();
    setUpMarketplace();

    document.getElementById('login-button').addEventListener('click', login);
    document.getElementById('signup-button').addEventListener('click', signUp);
    document.getElementById('change-password-button').addEventListener('click', changePassword);
    document.getElementById('edit-profile-info-button').addEventListener('click', editProfileInfo);
    document.addEventListener('mouseup', hideModalPopUp);

    if (currentPage === 'stocks') {
        document.getElementsByClassName('paggination-button')[0].classList.add('active-paggination-button');
    }

    document.querySelectorAll('.nav-target').forEach((link) => {
        link.addEventListener('click', app.nav);    
    })
}

/*---------First page load---------*/
window.onload=function() {
    google.charts.load('current', {'packages':['corechart']});

    let startPage = window.location.pathname;
    let currentPage = startPage.slice(1, startPage.length);

    if (currentPage === '') {
        history.replaceState({}, '', 'login');
        currentPage = 'login';
    }

    document.getElementById(currentPage).classList.add('active-page');
    document.getElementById(currentPage).dispatchEvent(app.show);

    function myLoop() {        
        setTimeout(function() {  
            try {
                setUpCharts();
            }
            catch (e) {
            }
            myLoop();                  
        }, 1000);
    }
    myLoop();
}

/*---------------DOM---------------*/
document.addEventListener('DOMContentLoaded', app.init);

/*--------CSRF protection----------*/
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