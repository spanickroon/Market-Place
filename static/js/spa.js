/*---------------SPA---------------*/
const app = {
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

        document.getElementById(hash).dispatchEvent(app.show);
    },
    pageShown: function(ev) {
        ev.preventDefault();

        let currentPage = document.querySelector('.active-page').getAttribute('id');
        
        fetch(currentPage, {
            method: 'GET',
            headers: {'content-type':'application/x-www-form-urlencoded'}
        })
        .then(response => {
            if (response.status !== 200) {
                return Promise.reject(); 
            }
            return response
        })
        .catch(() => console.log('error response'));
    }
}

/*---------First page load---------*/
window.onload=function() {
    let startPage = window.location.pathname;
    let currentPage = startPage.slice(1, startPage.length);

    document.getElementById(currentPage).classList.add('active-page');
    document.getElementById(currentPage).dispatchEvent(app.show);
}

/*---------------DOM---------------*/
document.addEventListener('DOMContentLoaded', app.init);