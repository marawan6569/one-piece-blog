
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
      );
      $('#comment_form')[0].reset();
    },
    error: function(response) {
      console.log('error');

      alert('cant add comment now, please try agin later')

    }
  })
}

// replying form
form = "<div class='form-wrap pt-5' id='replying_form_container'>\
        <h3 class='mb-5'>Reply</h3>\
        <form id='reply_form' class='p-5 bg-light'>\
          <div class='form-group'>\
            <label for='name'>Name *</label>\
            <input type='text' name='name' required class='form-control' id='replay-name'>\
          </div>\
          <div class='form-group'>\
            <label for='email'>Email *</label>\
            <input type='email' name='email' required class='form-control' id='replay-email'>\
          </div>\
          <div class='form-group'>\
            <label for='message'>Comment</label>\
            <textarea name='comment' required id='replay' cols='30' rows='10' class='form-control'></textarea>\
          </div>\
          <div class='form-group'>\
            <input type='button' value='reply' id='post_replay' onclick='get_data_from_replying_form()' class='btn py-3 px-4 btn-primary'>\
          </div>\
        </form>\
      </div>"

// show replying form
function show_replying_form(id) {
  replying_to = $('#comment-'+id);
  replying_to.parent().append(form);
  replying_to.parent().append("<input onclick='hide_replying_form()' type='button' value='Cancel' id='hide_replying_form' class='btn py-3 px-4 btn-primary mt-2'>");
  replying_to.hide();

};
// hide replying form
function hide_replying_form() {
  $('#hide_replying_form').remove();
  $('#replying_form_container').remove();
  replying_to.show();
};




function get_data_from_replying_form() {
  // e.preventDefault()
  chapter_id = $('#chapter_id').val(),
    name = $('#replay-name').val(),
    email = $('#replay-email').val(),
    comment = $('#replay').val();
    // console.log(chapter_id);
    // console.log(name);
    // console.log(email);
    // console.log(comment);
  testEmail = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,4}$/i;
  if (testEmail.test(email)) {
    email = email
    if (chapter_id != '' && name != '' && email != '' && comment != '') {
      data = {
        'chapter_id': chapter_id,
        'comment_id': replying_to.attr('comment-id'),
        'name': name,
        'email': email,
        'comment': comment
      }
      // console.log(data);
      add_reply(data)
    } else {
      alert('please fill all fields')
    }
  } else {
    email = ''
    alert('pleas enter a vailed email')
  }
};

function add_reply(data) {
  $.ajax({
    type: 'GET',
    url: '/ajax/add-reply',
    data: data,
    success: function(response) {
      comment = response['comment'];
      parent = replying_to.parent().parent().parent().children('ul');
      parent.append(
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
      );
      $('#reply_form')[0].reset();
    },
    error: function(response) {
      console.log('error');

      alert('cant add comment now, please try agin later')

    }
  })
};
