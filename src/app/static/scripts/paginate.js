window.addEventListener('load', () => setActivePaginateButton());
window.addEventListener('load', () => setQueryStringInPageLink());

function setActivePaginateButton() {
    const url = new URL(window.location.href);
    let pageNum = parseInt(url.searchParams.get('page'), 10) || 1;

    const pageLinks = document.querySelectorAll('.pagination a[id^="page_num"]');
    pageLinks.forEach(link => {
        const pageNumLink = parseInt(link.id.replace(/\D/g, ''), 10);
        if (pageNum === pageNumLink) {
            link.classList.add("active");
        }
    })
}

function saveFilterInLocalStorage() {
    const playerName = document.getElementById('filter_player').value;
    const perPage = document.getElementById('page-select').value;

    const filter = {
        filter_by_player_name: playerName,
        per_page: perPage
    };

    localStorage.setItem('filter', JSON.stringify(filter));
}

function setQueryStringInPageLink(){
     const pageLinks = document.querySelectorAll('.pagination a');
     pageLinks.forEach(link => {
         link.href += getQueryString();
     });
}

function getQueryString() {
    const storedFilter = JSON.parse(localStorage.getItem('filter'));
    const params = new URLSearchParams();

    for (const key in storedFilter) {
        if (storedFilter[key] !== '') {
            params.append(key, storedFilter[key]);
        }
    }

    return !params.toString() ? '' : '&' + params.toString();
}

function clearLocalStorage() {
    localStorage.clear();
}