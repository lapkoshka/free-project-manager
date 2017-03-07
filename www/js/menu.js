"use strict";   
document.addEventListener("DOMContentLoaded", function () {
        profileusername.innerHTML = getCookie("username");

        profileusername.addEventListener("click", function (event) {
            event.preventDefault();
        })

        logOut.addEventListener ("click", function () {
            event.preventDefault();
            document.cookie = "session=dropped; path=/";
            document.cookie = "username=; path=/";
            location.reload();
        })
        
        addProject.addEventListener ("click", function (event) {
            event.preventDefault();
            addBg.style.display = "block";
        })

        addBg.addEventListener ("click", function (event) {
            if (event.target.id === "addBg") {
                this.style.display = "none";
            }
        })

        createProject.addEventListener ("click", function () {
            if (checkAddForm()) {
                let data = {};
                data.name = projectname.value;
                data.description = projectdescription.value;
                data.session = getCookie("session");
                addProjectOnServer(data);
            }
        })
});

function addProjectOnServer(postdata) {
    query("createpost.py", "POST", postdata)
        .then ( data => {
            data = JSON.parse(data);
            if (data["status"] === "true") {
                window.location = "./"
            } else {
                projectname.value = "";
            }
        })
        .catch ( error => {
            console.log(error);
        })
}

function checkAddForm () {
    projectname.style.borderLeft = "1px solid lightgray";
    projectdescription.style.borderLeft = "1px solid lightgray";

    if (projectname.value === "") {
        projectname.style.borderLeft = "2px solid red";
        return false
    }

    if (projectdescription.value === "") {
        projectdescription.style.borderLeft = "2px solid red";
        return false
    }
    
    if (projectname.value.length > 40) {
        projectname.style.borderLeft = "2px solid red";
        showMessage ("Name can't be longer than 40 chars");
        return false
    }

    return true
}

function showMessage (text) {    
    let _window = document.querySelector(".add-project");
    try {
        _window.querySelector(".pr-message").remove();
    } catch (error) {}

    let div = document.createElement("div");
    div.className = "row pr-message";
    div.style.color = "red";
    div.innerHTML = `
                <div class="col-md-2"></div>
                <div class="col-md-8">
                    <span>${text}</span>
                </div>
    `;
    _window.insertBefore(div, _window.children[2])
}