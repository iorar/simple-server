// server.py からデータを受け取る
let requestURL = "http://localhost:80/getData";
let request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'text';
request.send();
var greet;

// server.py からレスポンスがあったら動く関数
request.onload = function () {
    greet = request.response;
    document.querySelector("#greeting").innerHTML = greet;
}