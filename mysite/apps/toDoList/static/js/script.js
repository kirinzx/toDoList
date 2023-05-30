const user_id = Number(document.querySelector('.visually-hidden').innerHTML)
const token = getToken();

function getToken() {
    function getCookie(name) {
        var cookieValue = null;

        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    return getCookie('csrftoken');
}


document.querySelector('#push').onclick = function () {
    const task = document.querySelector('#newTask input').value
    if (task.length == 0) {
        alert("You can't enter empty task")
    }
    else {
        axios.post('/api/user/task', {
            "user_id": user_id,
            "task": task,
        }, {
            headers: {
                "X-CSRFToken": token
            }
        })
        .then(function (response) {
            document.querySelector('#tasks').innerHTML += `
            <div data-task="${response.data.id}" class="task">
                <span id="taskname">
                    ${response.data.task}
                </span>
                <button onclick="removeNote(this)" type="button" id="delete">
                    <i class="fa-solid fa-trash"></i>
                </button>
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

function removeNote(btn) {

    if (btn) {
        const taskId = btn.parentNode.getAttribute("data-task")
        axios.delete(`/api/user/task/${taskId}`, {
            headers: {
                "X-CSRFToken": token
            }
        })
        .then(function (response) {
            btn.parentNode.remove()
            noNotes();
        })
        .catch(function (error) {
            console.error(error);
        })
    }
    noNotes();
}


window.onload = function (e) {
    removeNote();
}

function noNotes(){
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

const btn = document.querySelector(".menu-burger")

btn.addEventListener('click', function () {
    const menu = document.querySelector(".menu-content")
    menu.classList.toggle("menu-content-active")
    btn.classList.toggle("menu-burger-active")
})

const preloader = document.querySelector('.preloader');
const images = document.images;
const imagesTotal = images.length;
let imagesLoaded = 0;

if (preloader) {
    if (imagesTotal > 0) {
        for (let i = 0; i < imagesTotal; i++) {
            let imageClone = new Image();
            imageClone.onload = imageLoaded;
            imageClone.onerror = imageLoaded;
            imageClone.src = images[i].src;
        }
    } else imageLoaded();

    function imageLoaded() {
        imagesLoaded++;

        if (imagesLoaded >= imagesTotal) {
            setTimeout(function () {
                if (!preloader.classList.contains('preloader__done')) {
                    preloader.classList.add('preloader__done');
                }
            }, 1200)
        }
    }
}