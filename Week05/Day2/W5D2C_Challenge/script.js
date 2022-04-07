let words = [];
let textArea = document.querySelector("#story");

stories = [];

story[0] = `Today I went to the ${words[4]}. I saw a(n) ${words[1]} ${words[2]} jumping up and down in its tree.
He ${words[3]} through the large tunnel that led to its ${words[0]}.`




function generateStory() {
    words[0] = document.getElementById("noun").value;
    words[1] = document.getElementById("adjective").value;
    words[2] = document.getElementById("person").value;
    words[3] = document.getElementById("verb").value;
    words[4] = document.getElementById("place").value;

    for (w of words) {
        if (w.length == 0) {
            console.log("You need to fill all fields.");
            alert("You need to fill all fields.");
            return;
        }
    }
    story[0] = `Today ${words[2]} went to the ${words[4]}. ${words[2]} saw a stollen ${words[0]} from ${words[1]} ${words[4]}.
Usually in this case ${words[2]} ${words[3]}s, but today is too cold outside.`

    textArea.textContent = story[0];
}
