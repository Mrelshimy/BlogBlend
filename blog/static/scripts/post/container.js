$(document).ready(function () {
    $(document).ready(function () {
        let UsersList = {};
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
            url: `http://localhost:5001/blog/api/v1/posts/${postId}`,
            contentType: 'application/json',
            success: function (data) {
                const userName = UsersList[data.user_id];
                if (data.tag === undefined) {
                    data.tag = "";
                }
                $('.post_tag').text(data.tag);
                $('.post_title h1 strong').text(data.title)
                  // .charAt(0).toUpperCase() + data.title.slice(1));
                $('.post_content').text(data.content)
                  // .charAt(0).toUpperCase() + data.content.slice(1));
                $('.post_date').text(data.created_at)
                // .slice(0, 16));
                $('.post_author').text(userName)
                  // .charAt(0).toUpperCase() + userName.slice(1));
                $('.post_text p').text(data.content)
                  // .charAt(0).toUpperCase() + data.content.slice(1));
                $('.post_image').css('background-image', `url(../static/images/${data.cover})`);
            }
          })   

    });
})
