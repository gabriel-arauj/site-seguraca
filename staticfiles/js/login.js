/* ------------------------------------ Click on login and Sign Up to  changue and view the effect
---------------------------------------
*/

function cambiar_login() {
  document.querySelector('.cont_forms').className =
    'cont_forms cont_forms_active_login';
  document.querySelector('.cont_form_login').style.display = 'block';
  document.querySelector('.cont_form_sign_up').style.opacity = '0';

  setTimeout(function () {
    document.querySelector('.cont_form_login').style.opacity = '1';
  }, 400);

  setTimeout(function () {
    document.querySelector('.cont_form_sign_up').style.display = 'none';
  }, 200);
}

function cambiar_sign_up(at) {
  document.querySelector('.cont_forms').className =
    'cont_forms cont_forms_active_sign_up';
  document.querySelector('.cont_form_sign_up').style.display = 'block';
  document.querySelector('.cont_form_login').style.opacity = '0';

  setTimeout(function () {
    document.querySelector('.cont_form_sign_up').style.opacity = '1';
  }, 100);

  setTimeout(function () {
    document.querySelector('.cont_form_login').style.display = 'none';
  }, 400);
}

function ocultar_login_sign_up() {
  document.querySelector('.cont_forms').className = 'cont_forms';
  document.querySelector('.cont_form_sign_up').style.opacity = '0';
  document.querySelector('.cont_form_login').style.opacity = '0';

  setTimeout(function () {
    document.querySelector('.cont_form_sign_up').style.display = 'none';
    document.querySelector('.cont_form_login').style.display = 'none';
  }, 500);
}

function login(url, id_user, id_pass, CsrfViewMiddleware) {
  var user = $(id_user).val();
  var password = $(id_pass).val();
  $.ajax({
    headers: { 'X-CSRFToken': CsrfViewMiddleware },
    type: 'POST',
    url: url,
    data: { user, password },
  }).done(function (data) {
    window.location.replace(data.url);
    console.log(data);
  });
}

function myFunction() {
  var popup = document.getElementById('myPopup');
  popup.classList.toggle('show');
}
function myFunction2() {
  var popup = document.getElementById('myPopup2');
  popup.classList.toggle('show');
}
