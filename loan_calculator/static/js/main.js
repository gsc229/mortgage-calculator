const date = new Date();
// document.querySelector('.year').innerHTML = date.getFullYear();

// /* This will fade out the error message on register and login. You may need to first clear the cache in the browser for it to work with shift + F5 (windows)  cmd + shift + r (mac) */
setTimeout(function(){
  $('#amount_error').fadeOut('slow')
}, 3000)
setTimeout(function(){
  $('#interest_error').fadeOut('slow')
}, 3000)
setTimeout(function(){
  $('#term_error').fadeOut('slow')
}, 3000)

