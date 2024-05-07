$(document).ready(function () {
  let titles_ids = {};
  let user = {};
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

  function capitalizeFirstLetter(text) {
    return text.charAt(0).toUpperCase() + text.slice(1);
  }

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
            <section class="img_and_data">

              <div class="article-img">  
                <img
                    class="article_img"
                    src="../static/images/${post.cover}"
                    alt="post image"/>
              </div>

              <div class="article_data">
                <a href="http://localhost:5000/posts/${post.id}">
                  <div class="title">
                    <h2>${capitalizeFirstLetter(post.title)}</h2>
                    <p>Written in ${day} ${month} ${year}</p>
                  </div>
                  <p class="content">
                    ${post.content}
                  </p>
                </a>
              </div>
            </section>

            <section class="buttons">
              <button class="delete-btn">Delete</button>
              <button class="update-btn"><a href="http://localhost:5000/posts/${
                post.id
              }/update">Update</a></button>
            </section>
        </article>`
        );
      });
    },
  });

  $(document).on('click', '.delete-btn', function () {
    postId =
      titles_ids[$(this).parent().parent().find('h2').text().toLowerCase()];

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
        $('.profile .bio').text('No BIO YET');
      }
    },
  });
});
