const user_id = Number(document.querySelector('.visually-hidden').innerHTML)
var user_token = ''



document.querySelector('#push').onclick = function () {
    const task = document.querySelector('#newTask input').value
    if (task.length == 0) {
        alert("You can't enter empty task")
    }
    else {
        axios.post('/api/user/task', {
            "user": user_id,
            "task": task,
        },{
            headers: {
                "Authorization" : `Token ${user_token}`
            }
        })
        .then(function (response) {
            document.querySelector('#tasks').innerHTML += `
                <div class="task">
                    <span id="taskname">
                        ${response.data.task}
                    </span>
                    <button onclick="removeNote(this)" type="button" id="delete"></button>
                </div>
            `;
        })
        .catch(function (error) {
                console.error(error);
        })

        document.getElementById("textInput").value = "";
        if (document.getElementById("message") != null) {
            document.getElementById("message").remove();
        }
    }
}

function getToken(){
    axios.get(`/api/user/${user_id}/token`, {})

    .then(function (response) {
        user_token = response.data.key
    })
    .catch(function (error) {
        console.error(error);
    })
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
    getToken();
}

const btn = document.querySelector(".menu-burger")

btn.addEventListener('click', function () {
    const menu = document.querySelector(".menu-content")
    menu.classList.toggle("menu-content-active")
    btn.classList.toggle("menu-burger-active")
})