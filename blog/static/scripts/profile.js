$(document).ready(function () {
  let titles_ids = {};
  const months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
  ];

  let user = {};

  // Fetching the users
  $.ajax({
    method: 'GET',
    url: `http://localhost:5001/blog/api/v1/users/${currentUser}`,
    contentType: 'application/json',
    success: function (data) {
      user = { name: data.username, picture: data.avatar };
    },
  });

  // Fetching the posts and append them to posts-section
  // Just needed to add tags
  $.ajax({
    method: 'GET',
    url: `http://localhost:5001/blog/api/v1/users/${currentUser}/posts/`,
    contentType: 'application/json',
    success: function (data) {
      data.sort(() => Math.random() - 0.5);
      data = data.slice(0, 5);

      data.forEach((post) => {
        titles_ids[post.title.toLowerCase()] = post.id;
        if (post.tag === undefined) {
          post.tag = '';
        }

        const post_date = new Date(post.created_at);
        const year = post_date.getFullYear();
        const month = months[post_date.getMonth()];
        const day = post_date.getDate();

        $('.posts-section').append(
          `<article class="post">
            <img
              class="article_img"
              src="../static/images/${post.cover}"
              alt="post image"
            />
            <div class="post-details">

            <div class="user">
              <img src="../static/images/${user.picture}" alt="User profile" />
              <h3 class="user-name">${
                user.name.charAt(0).toUpperCase() + user.name.slice(1)
              }</h3>
            </div>
            
            <div class="article_data">
              <a href="http://localhost:5000/post/${post.id}">
                <div class="title">
                  <h2>${
                    post.title.charAt(0).toUpperCase() + post.title.slice(1)
                  }</h2>
                  <p>Written in ${day} ${month} ${year}</p>
                </div>
                <p class="content">
                  ${post.content}
                </p>
              </a>
            </div>
          </div>

          <div class="buttons">
            <button class="delete-btn">Delete</button>
            <button class="update-btn"><a href="http://localhost:5000/post/update">Update</a></button>
          </div>
        </article>`
        );
      });
    },
  });

  $(document).on('click', '.delete-btn', function () {
    postId = postId =
      titles_ids[$(this).parent().parent().find('h2').text().toLowerCase()];
    console.log(postId);

    $.ajax({
      method: 'DELETE',
      url: `http://localhost:5001/blog/api/v1/posts/${postId}`,
      contentType: 'application/json',
      success: function (data) {
        location.reload();
      },
    });
  });

  // Handling the profile data in the profile
  $.ajax({
    method: 'GET',
    url: `http://localhost:5001/blog/api/v1/users/${currentUser}`,
    contentType: 'application/json',
    success: function (data) {
      // data.avatar, data.username, data.bio
      // The avatar handled in the html using jinja
      $('.profile .name').text(
        data.username.charAt(0).toUpperCase() + data.username.slice(1)
      );

      if (data.bio != null) {
        $('.profile .bio').text(
          data.bio.charAt(0).toUpperCase() + data.bio.slice(1)
        );
      } else {
        $('.profile .bio').text('NO BIO');
      }
    },
  });
});
