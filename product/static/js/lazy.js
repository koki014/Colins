// Run after the HTML document has finished loading
window.onload = function () {
    initializeLazy();
}

function initializeLazy() {
    // Get our lazy-loaded images
    var lazyImages = [].slice.call(document.querySelectorAll("img.lazy"));

    // Do this only if IntersectionObserver is supported
    if ("IntersectionObserver" in window) {
        // Create new observer object
        let lazyImageObserver = new IntersectionObserver(function (entries, observer) {
            // Loop through IntersectionObserverEntry objects
            entries.forEach(function (entry) {
                // Do these if the target intersects with the root
                let lazyImage = entry.target;
                lazyImage.src = lazyImage.dataset.original;
                lazyImage.classList.remove("lazy")
                 lazyImageObserver.unobserve(lazyImage);
            });
        });

        // Loop through and observe each image
        lazyImages.forEach(function (lazyImage) {
            lazyImageObserver.observe(lazyImage);
        });
    }
}