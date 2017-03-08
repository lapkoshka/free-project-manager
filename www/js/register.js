"use strict";
document.addEventListener("DOMContentLoaded", function () {

    register.addEventListener("click", function (event) {
        event.preventDefault();
        let name = regname.value;
        let pass = regpassword.value;
        let repass = regpassword2.value;
        let email = regemail.value;
        let fieldsIsOk = checkRegForm(name, pass, repass, email);

        if(fieldsIsOk) {
            let newUser = {};
            newUser["name"] = name;
            newUser["password"] = pass;
            newUser["email"] = email;
            registration(newUser);
        }
    })

})

function registration (userdata) {
    query("reg.py", "POST", userdata)
        .then ( (data) => {
            verificaton(JSON.parse(data), "reg");
        })
        .catch ( (error) => {
            addMessageOnLoginForm("Uncorrect username", "white");
        })
}

function checkRegForm (name, pass, repass, email) {
    name = name.replace(/"|'"/g,'');
    regname.style.borderLeft = "none";
    regpassword.style.borderLeft = "none";
    regpassword2.style.borderLeft = "none";
    regemail.style.borderLeft = "none";

    if (pass !== repass) {
        addMessageOnLoginForm("Password not the same!", "red");
        regpassword.style.borderLeft = "2px solid red";
        regpassword2.style.borderLeft = "2px solid red";
        return false
    }

    if (!/\w@\w/g.test(email)) {
        regemail.style.borderLeft = "2px solid red";
        addMessageOnLoginForm("Uncorrect email", "red");
        return false
    }

    if (name === "") {
        regname.style.borderLeft = "2px solid red";
        addMessageOnLoginForm("Can't be empty", "red");
        return false
    }

    if (name.length > 30) {
        regname.style.borderLeft = "2px solid red";
        addMessageOnLoginForm("Can't be longer than 30 chars", "red");
        return false
    }
    
    if (regpassword === "" || regpassword2 === "") {
        regpassword.style.borderLeft = "2px solid red";
        regpassword2.style.borderLeft = "2px solid red";
        return false
    }
    return true
}