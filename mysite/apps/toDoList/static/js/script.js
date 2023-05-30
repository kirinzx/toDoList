document.querySelector('#push').onclick = function () {
    if (document.querySelector('#newTask input').value.length == 0) {
        alert("No way, man... YOU CANT ENTER EMPTY NOTE!!!!")
    }
    else {

        document.querySelector('#tasks').innerHTML += `
            <div class="task">
                <span id="taskname">
                    ${document.querySelector('#newTask input').value}
                </span>
                <button onclick="removeNote(this)" type="button" id="delete"></button>
            </div>
        `;

        document.getElementById("textInput").value = "";
        if (document.getElementById("message") != null) {
            document.getElementById("message").remove();
        }
    }
}
function removeNote(btn) {

    if (btn) btn.parentNode.remove();

    const all_tasks = document.querySelectorAll('#delete');
    if (all_tasks.length == 0) {
        document.querySelector('#tasks').innerHTML += `
            <div id="message">
                <span id="message-text">
                    There are no notes...
                </span>
            </div>
        `;
    }
}


window.onload = function (e) {
    removeNote();
}

const btn = document.querySelector(".menu-burger")

btn.addEventListener('click', function () {
    const menu = document.querySelector(".menu-content")
    menu.classList.toggle("menu-content-active")
    btn.classList.toggle("menu-burger-active")
})