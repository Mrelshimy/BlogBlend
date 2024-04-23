$(document).ready(function() {
  $(window).on('scroll', function() {
    if ($(this).scrollTop() >= 290) {
      if ($('header nav.navbar:contains("BlogBlend")').length === 0) {
        $('header nav.navbar ul').before('<a href="#" class="logo"><strong>BlogBlend</strong></a>');
      }     
      $('header nav.navbar').addClass('scrolled');
      $('header nav.navbar ul').addClass('scrolled_list');
      $('header nav.navbar ul li a').addClass('scrolled_li');
    } else {
      $('header nav.navbar .logo').remove();
      $('header nav.navbar').removeClass('scrolled');
      $('header nav.navbar ul').removeClass('scrolled_list');
      $('header nav.navbar ul li a').removeClass('scrolled_li');
    }
  });
});
