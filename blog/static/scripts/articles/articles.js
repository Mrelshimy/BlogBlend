$(document).ready(function () {
  $('article').hover(
    function () {
      if ($(this).find('p').length === 0) {
        $(this)
          .find('div.article_img a')
          .append('<p class="hover-tag">Tag</p>');
      }
    },
    function () {
      $(this).find('div.article_img a p').remove();
    }
  );
});
