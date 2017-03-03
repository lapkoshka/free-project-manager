"use strict";
document.addEventListener("DOMContentLoaded", function () {

    submit.addEventListener("click", function (event) {
        event.preventDefault();
        let userdata = {}
        userdata["login"] = username.value;
        userdata["password"] = password.value;
        if (username.value === "" || password.value === "") {
            addMessageOnLoginForm("Please fill out fields", "red");
        } else {
            logIn(userdata);
        }
    })
})

function logIn (userdata) {
    query("login.py","POST", userdata)
        .then ( (data) => {
            verificaton(JSON.parse(data), "login");
        })
        .catch ( (error) => {
            console.log(error);
        })
}

