/* Sidebar open icon and menu close icon event listeners */

const aside = document.querySelector('.aside');
const asideOpen = document.querySelector('.header_aside-open-icon');
const asideClose = document.querySelector('.aside_close-icon');

asideOpen.addEventListener('click', function () {
  aside.classList.toggle('active');
});

asideClose.addEventListener('click', function () {
  aside.classList.toggle('active');
});

/* Sidebar dropdows menu event listeners */

var dropdown = document.getElementsByClassName('aside_dropdown-btn');
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener('click', function () {

    this.classList.toggle('active');
    var dropdownContent = this.nextElementSibling;

    if (dropdownContent.style.display === 'block') {
      dropdownContent.style.display = 'none';
    } else {
      dropdownContent.style.display = 'block';
    }

    this.firstChild.lastChild.classList.toggle('active');
  });
}

/* Sidebar active list item menu event listeners */

var asideListItem = document.getElementsByClassName('aside_list-item');
var i;

for (i = 0; i < asideListItem.length; i++) {
  asideListItem[i].addEventListener('click', function () {

    if (this.classList.contains('active')) {
      return;
    }

    var j;
    for (j = 0; j < asideListItem.length; j++) {
      if (asideListItem[j].className === this.className) {
        continue;
      }

      if (asideListItem[j].classList.contains('active')) {
        asideListItem[j].classList.remove('active');
      }
    }

    this.classList.add('active');
  });
}

/* Breadcrumb nav active list item menu event listeners */

var breadcrumbListItem = document.getElementsByClassName('header_breadcrumb-nav-list-item');
var i;

for (i = 0; i < breadcrumbListItem.length; i++) {
  breadcrumbListItem[i].addEventListener('click', function () {

    if (this.classList.contains('active')) {
      return;
    }

    var j;
    for (j = 0; j < breadcrumbListItem.length; j++) {
      if (breadcrumbListItem[j].className === this.className) {
        continue;
      }
      if (breadcrumbListItem[j].classList.contains('active')) {
        breadcrumbListItem[j].classList.remove('active');
      }
    }

    this.classList.add('active');
  });
}

/* Table nav active list item menu event listeners */

var cardListItem = document.getElementsByClassName('main_card-table-nav-list-item');
var i;

for (i = 0; i < cardListItem.length; i++) {
  cardListItem[i].addEventListener('click', function () {

    if (this.classList.contains('active')) {
      return;
    }

    var j;
    for (j = 0; j < cardListItem.length; j++) {
      if (cardListItem[j].className === this.className) {
        continue;
      }
      if (cardListItem[j].classList.contains('active')) {
        cardListItem[j].classList.remove('active');
      }
    }

    this.classList.add('active');
  });
}

/* Here Maps Scroll Wheel Temporary Here Fix -> https://www.stevefenton.co.uk/2021/03/here-maps-scroll-wheel-temporary-fix/
(function () {
    var scrolling = false;
    var scrollEnd = null;

    function heremapScrollEnd() {
        scrolling = false;
        window.clearTimeout(scrollEnd);
        document.getElementById('map-fixer').style.display = 'none';
    }

    window.onwheel = function() {
        if (scrolling) {
            window.clearTimeout(scrollEnd);
            window.setTimeout(heremapScrollEnd, 10);
          return;
        }
        scrolling = true;
        document.getElementById('map-fixer').style.display = 'block';
        window.setTimeout(heremapScrollEnd, 40);
    }
})();

*/
