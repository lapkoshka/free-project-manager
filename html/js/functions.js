"use strict";
function getCookie(cname) {
            let name = cname + "=";
            let ca = document.cookie.split(';');
            for(let i = 0; i <ca.length; i++) {
                let c = ca[i];
                while (c.charAt(0)==' ') {
                    c = c.substring(1);
                }
                if (c.indexOf(name) == 0) {
                    return c.substring(name.length,c.length);
                }
            }
    return "";
}

function getId(hash) {
    return hash.substring(1)
}

function addMessageOnLoginForm (text, color) {
        let message = document.createElement("p");
        message.className = "message";
        message.style.color = color;
        message.innerHTML = text;
        document.querySelector(".login-page .form").appendChild(message);
}

function verificaton (data, type) {
    if (data["hash"]){
        document.cookie = `session=${data["hash"]}; path=/`;
        window.location = `./`;
    } else {
        password.value = "";
        password.style.borderLeft = "2px solid red";
        username.style.borderLeft= "2px solid red";
        let message;
        type === "login" ? message = "Wrong login or password" : message = "Email or username already exist";
        addMessageOnLoginForm(message, "red");
    }
}