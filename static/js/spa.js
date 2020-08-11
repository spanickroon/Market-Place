/*---------------SPA---------------*/
const app = {
    init: function() {
        app.pages = document.querySelectorAll('.page');

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
    },
    poppin: function(ev) {
        let hash = location.pathname.replace('/', '');
        document.querySelector('.active-page').classList.remove('active-page');
        document.getElementById(hash).classList.add('active-page');
    }
}

/*---------First page load---------*/
window.onload=function() {
    let startPage = window.location.pathname;
    document.getElementById(startPage.slice(1, startPage.length)).classList.add('active-page');
}

/*---------------DOM---------------*/
document.addEventListener('DOMContentLoaded', app.init);