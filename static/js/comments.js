// $.ajaxSetup({
//      beforeSend: function(xhr, settings) {
//          function getCookie(name) {
//              var cookieValue = null;
//              if (document.cookie && document.cookie != '') {
//                  var cookies = document.cookie.split(';');
//                  for (var i = 0; i < cookies.length; i++) {
//                      var cookie = jQuery.trim(cookies[i]);
//                      // Does this cookie string begin with the name we want?
//                      if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                          break;
//                      }
//                  }
//              }
//              return cookieValue;
//          }
//          if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
//              // Only send the token to relative URLs i.e. locally.
//              xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
//          }
//      }
// });


$('#post_comment').click(function(e) {
  e.preventDefault()
  chapter_id = $('#chapter_id').val(),
    name = $('#name').val(),
    email = $('#email').val(),
    comment = $('#comment').val();
  testEmail = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,4}$/i;
  if (testEmail.test(email)) {
    email = email
    if (chapter_id != '' && name != '' && email != '' && comment != '') {
      data = {
        'chapter_id': chapter_id,
        'name': name,
        'email': email,
        'comment': comment
      }
      // console.log(data);
      add_comment(data)
    } else {
      alert('please fill all fields')
    }
  } else {
    email = ''
    alert('pleas enter a vailed email')
  }


});




function add_comment(data) {
  $.ajax({
    type: 'GET',
    url: '/ajax/add-comment',
    data: data,
    success: function(response) {
      // $('#name').val() = '';
      // $('#email').val() = '';
      // $('#comment').val() = '';
      comment = response['comment']
      comments_list = $('#comment-container')
      comments_list.append(
        " <li class='comment'>\
          <div class='vcard bio'>\
            <img src='/static/images/person_1.jpg' alt='Image placeholder'>\
          </div>\
          <div class='comment-body'>\
            <h3>" + comment['name'] + "</h3>\
            <div class='meta'>" + comment['created_on'] + "</div>\
            <p>" + comment['body'] + "</p>\
            <p><a href='#' id='" + comment['id'] + "' class='reply'>Reply</a></p>\
          </div>\
        </li>\
        "
      )
      console.log(response['comment']);

    },
    error: function(response) {
      console.log('error');
      $('#comment_form')[0].reset();
      alert('cant add comment now, please try agin later')

    }
  })
}







// add comment
//
// $('#post_comment').on('click', function(event) {
//   var chapter_id = $('#chapter_id').val(),
//     name = $('#name').val(),
//     email = $('#email').val(),
//     comment = $('#comment').val();
//
//   console.log(chapter_id);
//   console.log(name);
//   console.log(email);
//   console.log(comment);
// });
//



// function test(e) {
//   e.preventDefault()
//   var chapter_id = $('#chapter_id').val(),
//     name = $('#name').val(),
//     email = $('#email').val(),
//     comment = $('#comment').val();
//
//   console.log(chapter_id);
//   console.log(name);
//   console.log(email);
//   console.log(comment);
// };
