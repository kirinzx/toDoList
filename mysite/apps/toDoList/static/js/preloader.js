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