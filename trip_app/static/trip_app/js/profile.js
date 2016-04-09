function change_password() {
	document.getElementById("profile-form").style.height = "550px";

	password_change_btn = document.getElementById("change-password-btn");
	password_field = document.getElementById("change-password");
	password_field.removeChild(password_change_btn);

	password_field.innerHTML += "<div id=password-form>" +
			"<input class=input-lg name=password type=password placeholder=******* required>" +
            "<label>Password</label>" +
            "<input class=input-lg name=password_conf type=password placeholder=******* required>" +
            "<label>Password Confirmation</label>" + 
            "<div onclick=cancel_password_change() id=change-password-btn>Cancel</div></div>";
}


function cancel_password_change() {
	document.getElementById("profile-form").style.height = "400px";

	password_field = document.getElementById("change-password");
	password_form = document.getElementById("password-form");
	password_field.removeChild(password_form);

	password_field.innerHTML += "<div onclick=change_password() id=change-password-btn>Change Password</div>";
}