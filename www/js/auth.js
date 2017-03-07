"use strict";
function ifAuthorizedThenRender(place) {
    let hash = {"hash": getCookie("session")};
    var _place = place;
    query("auth.py", "POST", hash)
        .then ( (data) => {
            renderOrKick(JSON.parse(data), _place);
        })
        .catch ( (error) => console.error(error))
}

function renderOrKick (data, place) {
    if (data["username"]) {
        document.cookie = `username=${data["username"]}; path=/`;
            place === "index" ?
            getProjects(data["username"]) :
            getPost(data["username"]);
    } else {
        window.location = './login.php';
    }
}

