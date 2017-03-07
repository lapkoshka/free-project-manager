"use strict";
//Fill template and add comments
function getPost () {
    let id = {
        id: getId(window.location.hash), 
        session: getCookie("session")
    };

    query("showprojectlist.py", "POST", id)
        .then ( (data) => {
            fillPost(JSON.parse(data));
        })
        .catch ( (error) => console.error(error))
}

function fillPost(data) {
    if (!( data["name"] === undefined )) {
        container.className = "container";
        postHead.innerHTML = `<h2>${data.name}</h2>`;
        if (!(data.judgeName === null)) {
            postHead.innerHTML += `<p style="font-size:2rem;color: lightblue;">Closed by ${data.judgeName}</p>`
        }
        description.innerHTML = data.description;
        author.innerHTML = data.author;
        rating.innerHTML = data.rating;
        answerCount.innerHTML = `${addAllComments(data.comments)} ответ(ов)`;
        data["priveleges"] === 1 ? judge.style.display = "block" : judge.style.display = "none"
    } else {
        document.body.innerHTML = `
        <div class="not-found">
            <h1>Oops!</h1>
            <span>NOT FOUND</span>
            <p>Press <a href="./">here</a> or <a href="./">here</a></p>
        </div>`;
    }
}

function addAllComments (data) {
    let counter = 0;
    for (let key in data) {
        addComment (data[key]);
        counter++;
    }
    return counter
}

ifAuthorizedThenRender("post");

//Add new comment
document.addEventListener("DOMContentLoaded", function () {
    sendcomments.addEventListener("click", function () {
        if (comment.value !== "") {
            let data = {};
            data.text = comment.value;
            data.session = getCookie("session");
            data.projectId = getId(window.location.hash);
            sendCommentOnServer (data)
        }
    })
})

function sendCommentOnServer (comment) {
    query("createcomment.py","POST", comment)
        .then ( data => {
            data = JSON.parse(data);
            if (data["status"] === "true") {
                location.reload();
            } else {
                console.error("Something went wrong...")
            }
        })
}

//Like
document.addEventListener("DOMContentLoaded", function () {
    like.addEventListener("click", function () {
        vote("like");
    })

    dislike.addEventListener("click", function () {
        vote("dislike");
    })
})

function vote (type) {
    let val = 0;

    if (type === "like") {
         val = 1;
    } else {
        val = -1;
    }

    let data = {};
    data.session = getCookie("session");
    data.projectId = getId(window.location.hash);
    data.value = val;
    sendVoteOnServer(data);
}

function sendVoteOnServer (data) {
    query("voting.py", "POST", data)
        .then ( data => {
            data = JSON.parse(data)
            if (data["status"] === "true") {
                rating.innerHTML = data["rating"];
            }
        })
        .catch ( error => {
            console.log(error);
        })
}

//Delete comment
function deleteComment(id) {
    let data = {
        id, 
        session: getCookie("session")
    };

    query("deletecomment.py", "POST", data)
        .then ( data => {
            data = JSON.parse(data);
            if (data["status"] === "true") {
                location.reload();
            } else {
                console.error("Delete failed!")
            }
        })
        .catch( error => {
            console.log(error);
        })
}

//Success Deny

document.addEventListener("DOMContentLoaded", function () {
    success.addEventListener("click", function () {
        decide(true)
    })

    deny.addEventListener("click", function () {
        decide(false);
    })
})

function decide(decision) {
    let data = {
        id: getId(window.location.hash), 
        session: getCookie("session"),
        decision
    };

    query("decide.py", "POST", data)
        .then( data => {
            data = JSON.parse(data);
            if (data["status"] === "true") {
                window.location = "./" 
            } else {
                console.log("Something went wrong...")
            }
        })
        .catch ( error => {
            console.log(error);
        })
}

//Voted 

document.addEventListener("DOMContentLoaded", function () {
    bgVoted.addEventListener("click", function (event) {
        if (event.target.id === "bgVoted") {
            this.style.display = "none"
        }
    })

    rating.addEventListener("click", function (event) {
        let top = rating.getBoundingClientRect().top + 20;
        let left = rating.getBoundingClientRect().left + 60;
        bgVoted.style.display = "block";
        voted.style.top = top + "px";
        voted.style.left = left + "px";
        voted.className = "voted flipInX animated"
        document.querySelector(".voted-for").innerHTML = "<h4>like</h4>";
        document.querySelector(".voted-against").innerHTML = "<h4>dislike</h4>";

        loadVoted ();
    })
})

function loadVoted () {
    let data = {
        id: getId(window.location.hash)
    }
    query("loadvoted.py", "POST", data)
        .then ( (data) => {
            data = JSON.parse(data);
            for (let key in data) {
                addUser(data[key])
            }
        })
        .catch ( (error) => {
            console.log(error)
        })
}

function addUser (data) {
    let votedFor = document.querySelector(".voted-for");
    let votedAgainst = document.querySelector(".voted-against");
    let user = document.createElement("a");
    user.href = "#";
    user.innerHTML = data.username || "";
    if (data.vote > 0) {
        votedFor.appendChild(user);
    } else {
        votedAgainst.appendChild(user);
    }
}