// COOKIE
function getCookie(name) {
    let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
  }
  let cookiecook = getCookie("cookiecook"),
  cookiewin = document.getElementsByClassName('cookie-banner')[0];

  if (cookiecook != "no") {
    // показываем
    cookiewin.style.display="block";
    // закрываем по клику
    document.getElementById("cookie_close").addEventListener("click", function(){
    cookiewin.style.display="none";

    let date = new Date;
    date.setDate(date.getDate() + 1);
    document.cookie = "cookiecook=no; path=/; expires=" + date.toUTCString();
    });
  }

let $search = $('.search'),
clazz = 'search--active';

$('#search_btn').on('click', e => {
  $search.addClass(clazz);
  $search.on(transitionProp, e => {
    $search.find('input').first().focus();
  });
});

$('#close_btn').on('click', e => {
  $search.removeClass(clazz);
});

$(document).on('click', e => {
  if ($(e.target).is('.search--active')) {
    $search.removeClass(clazz);
  }
});



var transitionProp = function () {var n = document.createElement("fakeelement"),i = { transition: "transitionend", OTransition: "oTransitionEnd", MozTransition: "transitionend", WebkitTransition: "webkitTransitionEnd" };for (var t in i) if (void 0 !== n.style[t]) return i[t];}();