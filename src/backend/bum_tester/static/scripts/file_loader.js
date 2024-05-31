// import { open } from "fs";");
// web developeri o vikendu nepracujou, omluvte moji implementaci
let qs = get_questions();
console.log(qs);
let questions = qs;
console.log(questions);
var index = random_int(questions);
var stats = {
    correct: 0,
    incorrect: 0,
    skipped: 0,
};


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
    document.getElementById("ans_no").innerText = questions[index].id;
    if (questions.length == 0) {
        element.innerHTML = `
        <h1>Máš to, žádný další otázky</h1>
        <a href="https://www.youtube.com/watch?v=A5ESth2KSEM?autoplay=1">
            Pro pořádné vyhodnocení pojď sem.
        </a>
        `;
        return;
    }
    element.innerText = questions[index].question;
    document.getElementById("answer").innerText = questions[index].answer;
}

function get_questions() {    
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", 'pairs', false); // false for synchronous request
    xmlHttp.overrideMimeType("application/json");
    xmlHttp.send();
    var myArr = JSON.parse(xmlHttp.responseText);
    return myArr;
}

window.onload = () => { new_question(); qs = get_questions(); };