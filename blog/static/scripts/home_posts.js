$(document).ready(function () {
  const UsersList = {};

  $.ajax({
    method: 'GET',
    url: 'http://localhost:5001/blog/api/v1/users/',
    contentType: 'application/json',
    success: function (data) {
      data.forEach(user => {
        UsersList[user.id] = user.username;
      });
    }
  });

  $.ajax({
    method: 'GET',
    url: 'http://localhost:5001/blog/api/v1/posts/',
    contentType: 'application/json',
    success: function (data) {
      data.sort(() => Math.random() - 0.5);
      data = data.slice(0, 5);
      data.forEach(post => {
        if (post.tag === undefined) {
          post.tag = '';
        }
        post.created_at = post.created_at.slice(0, 16);
        const userName = UsersList[post.user_id];
        $('.latest_posts').append(`
            <article class="row" id="art1">
              <div class="post_img">
                <a href="#" style="background-image: url('${post.cover}')"></a>
              </div>
              <div class="post_data">
                <div class="tag">${post.tag}</div>
                <a href="#"><strong>${post.title}</strong></a>
                <p class="date">${post.created_at}</p>
                <p class="owner"><strong>${userName}</strong></p>
                </div>
            </article>`);
      });
    }
  });
});
