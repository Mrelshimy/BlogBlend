$(document).ready(function () {
    let posts = {};
    $.ajax({
        method: 'GET',
        url: `http://localhost:5001/blog/api/v1/posts/`,
        contentType: 'application/json',
        success: function (data) {
          data.forEach(post => {
            posts[post.title] = post.id;
            if (post.tag === undefined) {
              post.tag = '';
            }
            if (post.user_id == currentUser) {
              $('.right_side').append(`
                <article>
                  <h1><a href="http://localhost:5000/post/${post.id}">${post.title.charAt(0).toUpperCase() + post.title.slice(1)}</a></h1>
                  <p class="tag">${post.tag.charAt(0).toUpperCase() + post.tag.slice(1)}</p>
                  <p class="post-breif">${post.content.charAt(0).toUpperCase() + post.content.slice(1, 150) + ' ...'}</p>
                  <button class="delete-btn">Delete</button>
                  <button class="update-btn"><a href="http://localhost:5000/post/update">Update</a></button>
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
        $('div.profile_name h1').text(data.username.charAt(0).toUpperCase() + data.username.slice(1));
        if (currentUser.bio) {
          $('div.bio').text(data.bio.charAt(0).toUpperCase() + data.bio.slice(1));
        }
      }
    });

    $(document).on('click', '.delete-btn', function () {
        let postId = posts[$(this).parent().find('h1').text().charAt(0).toLowerCase() + $(this).parent().find('h1').text().slice(1)];
        $.ajax({
          method: 'DELETE',
          url: `http://localhost:5001/blog/api/v1/posts/${postId}`,
          contentType: 'application/json',
          success: function (data) {
            location.reload();
          }
        });
    });

});
