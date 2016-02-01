function login_active() {
  $("#login-signup-form").css({opacity: 0, height: "400px"}).animate({opacity: 1.0})
  //document.getElementById('signup-form').style.visibility = "hidden";
  $("#signup-form").css({opacity: 0, visibility: "hidden"}).animate({opacity: 1.0});
  document.getElementById('signup-tab').className = "";

  //document.getElementById('login-form').style.visibility = "visible";
  $("#login-form").css({opacity: 0, visibility: "visible"}).animate({opacity: 1.0});
  document.getElementById('login-tab').className = "active";
}

function signup_active() {
  $("#login-signup-form").css({opacity: 0, height: "500px"}).animate({opacity: 1.0})
  //document.getElementById('signup-form').style.visibility = "visible";
  $("#signup-form").css({opacity: 0, visibility: "visible"}).animate({opacity: 1.0});
  document.getElementById('signup-tab').className = "active";

  //document.getElementById('login-form').style.visibility = "hidden";
    $("#login-form").css({opacity: 0, visibility: "hidden"}).animate({opacity: 1.0});
  document.getElementById('login-tab').className = "";
}
