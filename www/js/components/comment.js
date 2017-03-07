"use strict";
function addComment (data) {
    let owner = data.owner || false;

    let comment = document.createElement("div");
    comment.className = "row comment";
    comment.dataset.pid = data.id;

    let author = document.createElement("div");
    author.className = "col-md-2";
        author.innerHTML = `<a href='#'>${data.author}</a>`
        if (owner) {
            author.style.fontWeight = "bold";
            author.style.textDecoration = "underline";
        }
    comment.appendChild(author);

    let text = document.createElement("div");
    text.className = "col-md-8 text-description";
        text.innerHTML = data.comment;
    comment.appendChild(text);
    
    let time = document.createElement("div");
    time.className = "col-md-1";
        time.innerHTML = `<span>${data.createTime}</span>`;
    comment.appendChild(time);

    if (owner) {
        comment.appendChild(editBlock(data));
    }

    container.appendChild(comment);
}

//Comment editor
function editBlock (data) {
    let edit = document.createElement("div");
    edit.className = "col-md-1";
    let correct = document.createElement("i");
    correct.className = "fa fa-pencil-square-o";
    correct.setAttribute("aria-hidden", true);
    correct.dataset.id = data.id;

    //OK Cancel buttons handler
    correct.addEventListener("click", function () {
        let parent = this.parentElement.parentElement;
        let place = parent.querySelector(".text-description");
        let text = place.innerHTML;

            let textarea = document.createElement("textarea");
            textarea.rows = "3";
            textarea.innerHTML = text;
            place.innerHTML = "";
            place.appendChild(textarea);
            
            let br = document.createElement("br");
            place.appendChild(br);

            let ok = document.createElement("button");
            ok.innerHTML = "OK";
            ok.addEventListener("click", function () {
                let _data = {
                    id: data.id,
                    text: textarea.value,
                    session: getCookie("session")
                }
                updateComment(_data, place);
            })
            place.appendChild(ok);

            let cancel = document.createElement("button");
            cancel.innerHTML = "Cancel";
            cancel.addEventListener("click", function () {
                place.innerHTML = text;
            })
            place.appendChild(cancel);
    })

    edit.appendChild(correct);

    let del = document.createElement("i");
    del.className = "fa fa-times";
    del.setAttribute("aria-hidden", true);
    del.dataset.commentId = data.id;

    del.addEventListener("click", function() {
        confirm('Are you sure?') ? deleteComment(this.dataset.commentId) : {}
    })

    edit.appendChild(del);

    return edit
}

function updateComment (data, place) {
    var target = place;
    query("updatecomment.py", "POST", data)
        .then ( data => {
            data = JSON.parse(data);
            if (data.status === "true") {
                target.innerHTML = data.text;
            }
        })
        .catch ( error => {
            console.log(error);
        })
}