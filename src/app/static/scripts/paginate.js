window.addEventListener('load', setActivePaginateButton);


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