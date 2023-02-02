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