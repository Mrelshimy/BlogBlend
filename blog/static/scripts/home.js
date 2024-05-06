// $(document).ready(function () {
  // const months = [
  //   'January',
  //   'February',
  //   'March',
  //   'April',
  //   'May',
  //   'June',
  //   'July',
  //   'August',
  //   'September',
  //   'October',
  //   'November',
  //   'December',
  // ];
  // const UsersList = {};
  // $.ajax({
  //   method: 'GET',
  //   url: 'http://localhost:5001/blog/api/v1/users/',
  //   contentType: 'application/json',
  //   success: function (data) {
  //     data.forEach((user) => {
  //       UsersList[user.id] = { name: user.username, picture: user.avatar };
  //     });
  //   },
  // });
  // Just needed to add tags
  // $.ajax({
  //   method: 'GET',
  //   url: 'http://localhost:5001/blog/api/v1/posts/',
  //   contentType: 'application/json',
  //   success: function (data) {
  //     data.sort(() => Math.random() - 0.5);
  //     data = data.slice(0, 5);
  //     data.forEach((post) => {
  //       if (post.tag === undefined) {
  //         post.tag = '';
  //       }
  //       const post_date = new Date(post.created_at);
  //       const year = post_date.getFullYear();
  //       const month = months[post_date.getMonth()];
  //       const day = post_date.getDate();
  //       const userData = UsersList[post.user_id];
  // $('.posts-section').append(
  //   `<article class="post">
  //     <img
  //       class="article_img"
  //       src="../static/images/${post.cover}"
  //       alt="post image"
  //     />
  //     <div class="post-details">
  //     <div class="user">
  //       <img src="../static/images/${
  //         userData.picture
  //       }" alt="User profile" />
  //       <h3 class="user-name">${
  //         userData.name.charAt(0).toUpperCase() + userData.name.slice(1)
  //       }</h3>
  //     </div>
  //     <div class="article_data">
  //       <a href="http://localhost:5000/post/${post.id}">
  //         <div class="title">
  //           <h2>${
  //             post.title.charAt(0).toUpperCase() + post.title.slice(1)
  //           }</h2>
  //           <p>Written in ${day} ${month} ${year}</p>
  //         </div>
  //         <p class="content">
  //           ${post.content}
  //         </p>
  //       </a>
  //     </div>
  //   </div>
  // </article>`
  // );
  // });
  // },
  // });
// });

// <div class="post_data">
//   <div class="tag">${post.tag}</div>
// </div>;
