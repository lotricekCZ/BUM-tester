// import { open } from "fs";");
// web developeri o vikendu nepracujou, omluvte moji implementaci
var qs = get_questions();
questions = qs.split('\n');
console.log(questions);
var index = random_int(questions);
var stats = {
    correct: 0,
    incorrect: 0,
    skipped: 0,
};

const re = new RegExp("(\\d+\\.) (.*)");

function random_int(questions) {
    return Math.floor(Math.random() * questions.length);
}

function new_question(state) {
    var element = document.getElementById("question");

    switch (state) {
        case "correct":
            console.log("correct");
            stats.correct += 1;
            document.getElementById("correct").innerText = stats.correct;
            questions.splice(index, 1);
            break;
        case "wrong":
            console.log("wrong");
            stats.incorrect += 1;
            document.getElementById("wrong").innerText = stats.incorrect;
            break;
        case "skip":
            console.log("skip");
            stats.skipped += 1;
            document.getElementById("skipped").innerText = stats.skipped;
            break;
        default:
            console.log("first");
            break;
    }

    document.getElementById("remaining").innerText = questions.length;

    index = random_int(questions);
    document.getElementById("ans_no").innerText = index;
    if (questions.length == 0) {
        element.innerHTML = `
        <h1>Máš to, žádný další otázky</h1>
        <a href="https://www.youtube.com/watch?v=A5ESth2KSEM?autoplay=1">
            Pro pořádné vyhodnocení pojď sem.
        </a>
        `;
        return;
    }
    element.innerText = re.exec(questions[index])[2];

}

function get_questions() {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", '127.0.0.1:8000/BUM-tester/questions', true); // false for synchronous request
    xmlHttp.responseType = 'json';
    xmlHttp.withCredentials = true;
    xmlHttp.setRequestHeader("x-csrf-token", "fetch");
    xmlHttp.setRequestHeader("Accept", "application/json");
    xmlHttp.setRequestHeader("Content-Type", "application/json; charset=utf-8");
    xmlHttp.send(null);

    if (xmlHttp.readyState === 4) {
        var csrfToken = xmlHttp.getResponseHeader('x-csrf-token');

        xmlHttp.open('GET', 'http://127.0.0.1:8000/BUM-tester/questions/', false);
        xmlHttp.setRequestHeader('x-csrf-token', csrfToken);
        xmlHttp.setRequestHeader("Content-Type", "application/json; charset=utf-8");
        xmlHttp.setRequestHeader("Accept", "application/json");

        xmlHttp.send(JSON.stringify(obj));

        if (xmlHttp.readyState === 4) {
            res = JSON.parse(this.responseText);
            return res;
        }

        // console.log(xmlHttp.responseText);
    }
}

// let csrftoken = getCookie('csrftoken');
// let response = fetch("", {
//     method: 'POST',
//     body: data,
//     headers: {
//         'Accept': 'application/json, text/plain, */*',
//         'Content-Type': 'application/json',
//         "X-CSRFToken": csrftoken
//     },
// })

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

window.onload = () => { new_question(); qs = get_questions(); };