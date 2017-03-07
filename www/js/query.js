"use strict";
function query (scriptName, method, data) {
    let scriptFolder = "http://project-manager.atspot.ru/cgi-bin/"
    return new Promise (function (resolve, reject) {
        let xhr = new XMLHttpRequest();
        xhr.open(method, scriptFolder + scriptName);
        xhr.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
        xhr.send(JSON.stringify(data));
        xhr.onload = function() {
            if (xhr.status === 200) { 
                resolve(xhr.responseText) 
            } else { 
                reject(xhr.status) 
            }
        }
    })
}