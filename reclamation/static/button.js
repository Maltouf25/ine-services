const myButton = document.getElementById('button_hide');

myButton.addEventListener('click', function() {
  if (myButton.classList.contains('clicked')) {
    myButton.classList.remove('clicked');
  } else {
    myButton.classList.add('clicked');
  }
});

$(document).ready(function() {
  $('.color-change-button').click(function() {
      $(this).toggleClass('active');
  });
});