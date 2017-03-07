"use strict";
function getProjects () {
    query("showprojectlist.py", "GET")
        .then ( (data) => {
            data = JSON.parse(data);
            for (let key in data) {        
                addPost (data[key]);
            }
        })
        .catch ( (error) => console.error(error))
}

ifAuthorizedThenRender("index");