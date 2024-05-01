$(document).ready(function () {
  $.ajax({
    method: 'GET',
    url: 'http://localhost:5001/blog/api/v1/posts/',
    contentType: 'application/json',
    success: function (data) {
      data.forEach((post) => {
        if (post.tag === undefined) {
          post.tag = '';
        }
        $('.container').append(`
          <article class="post">
            <div class="article_img">
              <a href="http://localhost:5000/post/${
                post.id
              }" style="background-image: url('${post.cover}')"></a>
            </div>
            <div class="article_data">
              <a href="http://localhost:5000/post/${
                post.id
              }" class="article_header">${
          post.title.charAt(0).toUpperCase() + post.title.slice(1)
        }</a>
            </div>
          </article>`);

        $('article').hover(
          function () {
            if ($(this).find('p').length === 0) {
              $(this)
                .find('div.article_img a')
                .append(`<p class="hover-tag">${post.tag}</p>`);
            }
          },
          function () {
            $(this).find('div.article_img a p').remove();
          }
        );
      });
    },
  });
});

// Use this instead of the above to apply css correctly

// <article class="post">
//   <img
//     class="article_img"
//     src="../static/images/post_sample.jpg"
//     alt="post image"
//   />
//   <div class="post-details">
//     <div class="user">
//       <img src="../static/images/channels4_profile.jpg" alt="User profile" />
//       <h3 class="user-name">Writer name</h3>
//     </div>
//     <div class="article_data">
//       <a href="#">
//         <div class="title">
//           <h2>article title</h2>
//           <p>Written in 7, Oct 2023</p>
//         </div>
//         <p class="content">
//           Lorem ipsum dolor, sit amet consectetur adipisicing elit. Voluptates,
//           nulla nostrum nisi debitis voluptatibus facere aspernatur? Lorem ipsum
//           dolor, sit amet consectetur adipisicing elit. Voluptates, nulla
//           nosre aspernatur? Lorem ipsuur?
//         </p>
//       </a>
//     </div>
//   </div>
// </article>;
