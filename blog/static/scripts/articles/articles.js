$(document).ready(function () {

  $.ajax({
    method: 'GET',
    url: 'http://localhost:5001/blog/api/v1/posts/',
    contentType: 'application/json',
    success: function (data) {
      data.forEach(post => {
        if (post.tag === undefined) {
          post.tag = '';
        }
        $('.container').append(`
          <article class="post">
            <div class="article_img">
              <a href="http://localhost:5000/post/${post.id}" style="background-image: url('${post.cover}')"></a>
            </div>
            <div class="article_data">
              <a href="http://localhost:5000/post/${post.id}" class="article_header">${post.title.charAt(0).toUpperCase() + post.title.slice(1)}</a>
            </div>
          </article>`);

        $('article').hover(
          function () {
            if ($(this).find('p').length === 0) {
              $(this).find('div.article_img a').append(`<p class="hover-tag">${post.tag}</p>`);
            }
          },
          function () {
            $(this).find('div.article_img a p').remove();
          }
        );
      });
    }
  });
});
