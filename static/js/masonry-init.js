const elem = document.querySelector('.grid');
var msnry = new Masonry( elem, {
  itemSelector: '.grid-item',
  columnWidth: '.grid-sizer',
});

var msnry = new Masonry( '.masonry', {
  horizontalOrder: true,
  percentPosition: true,
});