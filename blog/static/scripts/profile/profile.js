$(document).ready(function () {
    
    $.ajax({
        method: 'GET',
        url: `http://localhost:5001/blog/api/v1/posts/`,
        contentType: 'application/json',
        success: function (data) {
          data.forEach(post => {
            if (post.tag === undefined) {
              post.tag = '';
            }
            if (post.user_id == currentUser) {
              $('.right_side').append(`
                <article>
                  <h1><a href="#">${post.title}</a></h1>
                  <p class="tag">${post.tag}</p>
                  <p class="post-breif">${post.content.slice(0, 200) + ' ...'}</p>
                </article>`
              )
            }
          });
        }
      });

    $.ajax({
      method: 'GET',
      url: `http://localhost:5001/blog/api/v1/users/${currentUser}`,
      contentType: 'application/json',
      success: function (data) {
        $('div.profile_name h1').text(data.username);
        $('div.bio').text(data.bio);
      }
    });

});
