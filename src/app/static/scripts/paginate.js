window.addEventListener('load', () => setActivePaginateButton());

function setActivePaginateButton() {
    const url = new URL(window.location.href);
    let pageNum = 1;

    if (url.searchParams.get('page') != null) {
        pageNum = parseInt(url.searchParams.get('page'), 10);
    }

    const pageLinks = document.querySelectorAll('.pagination a[id^="page_num"]');
    pageLinks[(pageNum - 1)].classList.add("active");
}