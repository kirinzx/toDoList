const btn = document.querySelector(".menu-burger")

btn.addEventListener('click', function () {
    const menu = document.querySelector(".menu-content")
    menu.classList.toggle("menu-content-active")
    btn.classList.toggle("menu-burger-active")
})