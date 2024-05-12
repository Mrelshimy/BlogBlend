/**
 * This function is executed when the document is ready.
 * It makes two AJAX requests to fetch user and post data,
 * and appends the fetched data to the DOM.
 */
$(document).ready(function () {
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
    'December'
  ];

  /**
   * Fetches user data from the server and assigns it to the 'user' variable.
   */
  $.ajax({
    method: 'GET',
    url: `http://localhost:5001/blog/api/v1/users/${currentUser}`,
    contentType: 'application/json',
    success: function (data) {
      user = { name: data.username, picture: data.avatar };
    }
  });

  /**
   * Fetches post data from the server and appends it to the DOM.
   */
  $.ajax({
    method: 'GET',
    url: `http://localhost:5001/blog/api/v1/posts/${postId}`,
    contentType: 'application/json',
    success: function (data) {
      if (data.tag === undefined) {
        data.tag = '';
      }

      const postDate = new Date(data.created_at);
      const year = postDate.getFullYear();
      const month = months[postDate.getMonth()];
      const day = postDate.getDate();

      $('.article').append(
        `
          <div class="title">
            <h2>${data.title.charAt(0).toUpperCase() + data.title.slice(1)}</h2>
          </div>

          <div class="infos">
            <div class="author-img">
              <img src="../static/images/${
                user.picture
              }" alt="Author Picture" />
            </div>
            <div class="name-date">
              <p class="author-name">${user.name}</p>
              <p class="post-date">Written in ${day} ${month} ${year}</p>
            </div>
          </div>

          <div class="img-div">
            <img src="../static/images/${data.cover}" alt="Post Cover" />
          </div>

          <div class="content">
            <p>${data.content}</p>
          </div>
          `
      );
    }
  });
});

/**
 * Toggles the 'liked' class on the 'like' button when clicked.
 */
$('button.like').click(function () {
  $('button.like').toggleClass('liked');
});
