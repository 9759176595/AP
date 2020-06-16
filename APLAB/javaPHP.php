<?php

echo "function validate_form() {
<!--

var username = document.getElementById(\\"username\\");
var password = document.getElementById(\\"password\\");
var status = document.getElementById(\\"status\\");

if (username.value.length <= 3) {

status.innerHTML = \\"Username is too short!\\";

username.focus();

return false;

}
else if (password.value.length <= 3) {

status.innerHTML = \\"Password is too short!\\";

password.focus();

return false;

}
else {

return true;

}

//-->
}";

?>