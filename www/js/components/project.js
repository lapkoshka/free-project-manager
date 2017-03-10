"use strict";
function addPost (data) {
    let project = document.createElement("div");
    project.className = "row home-row";

            let votes = document.createElement("div");
            votes.className = "home-col col-md-1";
                    let block1 = document.createElement("div");
                    block1.className = "block";
                    block1.innerHTML = `<span><b>${data.rating}</b><br>votes</span>`;

                    if (data.solved === 0) {
                        block1.style.border = "1px solid #ba5f5f"
                        block1.style.background = "#ba5f5f";
                        block1.style.color = "white";
                    } else if (data.solved === 1) {
                        block1.style.border = "1px solid #5fba7d"
                        block1.style.background = "#5fba7d";
                        block1.style.color = "white";
                    } else {

                    }

                votes.appendChild(block1);
            project.appendChild(votes);

            let answers = document.createElement("div");
            answers.className = "home-col col-md-1";
                    let block2 = document.createElement("div");
                    block2.className = "block";
                    block2.innerHTML = `<span><b>${data.answers}</b><br>answers</span>`;
                answers.appendChild(block2);
            project.appendChild(answers);

            let views = document.createElement("div");
            views.className = "home-col col-md-1";
                    let block3 = document.createElement("div");
                    block3.className = "block";
                    block3.innerHTML = `<span><b>${data.views}</b><br>views</span>`;
                views.appendChild(block3);
            project.appendChild(views);

            let info = document.createElement("div");
            info.className = "home-col col-md-9";

                    let header = document.createElement("header");
                            let h2 = document.createElement("h2");
                            h2.innerHTML = data.name;
                            h2.addEventListener("click", function(ev) { 
                                window.location = `./post.php#${ev.target.dataset.id}`;
                                watched(ev.target.dataset.id);
                            });
                            h2.dataset.id = data.id;;
                        header.appendChild(h2);

                    let footer = document.createElement("footer");
                            let desc = document.createElement("div");
                            desc.className = "desc";
                            desc.innerHTML = `<span>${cutDescription(data.description)}</span>`;
                        footer.appendChild(desc);

                            let createdBy =  document.createElement("div");
                            createdBy.className = "created-by";
                            createdBy.innerHTML = `<br><span>Created by <a href='#'>${data.author}</a></span>`;
                        footer.appendChild(createdBy);
                    info.appendChild(header);
                    info.appendChild(footer);
                project.appendChild(info);
            container.appendChild(project);                
        }

function cutDescription(text) {
    let length = 50;
    if (/<br>/.test(text)) {
        return text.split('<br>')[0]
    } else if (text.length > length) {
        return text.substr(0,length) + "..."
    } else {
        return text
    }
}

function watched (id) {
    let data = {
        session: getCookie("session"),
        id
    }
    console.log(data)
    query("watch.py", "POST", data)
        .then( data => {
            data = JSON.parse(data);
        })
        .catch ( error => {
            console.log(error)
        })
}