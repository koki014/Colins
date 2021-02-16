window.addEventListener("load", function () {
    MainSlider();
    MobileMenuControl();
    BannerTemplateBoxesSlider();
    NewsletterButtonControl();
    autoComplete();
    instagramFeed();

    if (window.innerWidth > 1200) {
        initializeMenuImageOnHover();
    }

    if (document.querySelector(".filter-container.filter-container-toggle.clearfix.group-container-CİNSİYET") != null) {
        document.querySelector(".filter-container.filter-container-toggle.clearfix.group-container-CİNSİYET").click()
    }

});

function BannerTemplateBoxesSlider() {
    if (typeof (sliderId) != "undefined") {
        var divIdSelector = document.getElementById(sliderId);
        const slider = tns({
            container: divIdSelector,
            items: 2,
            lazyload: true,
            controls: true,
            nav: false,
            mouseDrag: true,
            autoHeight: true,
            autoWidth: true,
            gutter: 5,
            controlsContainer: "#customize-controls-2",
        });
    }
}

function MobileMenuControl() {
    document.getElementsByClassName("mobile-menu-container")[0].classList.remove("d-none");

    document.getElementById("mobile-menu-toggle").addEventListener("click", function () {
        //document.getElementById("defaultmenu-mobile").classList.toggle("d-none");
        document.getElementById("defaultmenu-mobile").classList.toggle("open-mobile-menu");
        //document.getElementsByClassName("mobile-menu-container")[0].classList.toggle("d-none");
        document.getElementsByClassName("overlay-mobile-menu")[0].classList.toggle("d-none");
        document.getElementsByTagName("body")[0].classList.toggle("overflow-hidden");
    });

    var subMenuToggle = document.getElementsByClassName("mobile-menu-acordeon");
    var secondMenuToggle = document.getElementsByClassName("mobile-sub-menu-acordeon");
    var backToFirstMenu = document.getElementsByClassName("first-menu-back-button");
    var backToSecondMenu = document.getElementsByClassName("second-menu-back-button");
    var firstMenus = document.getElementsByClassName("menu-main-li");
    var secondMenus = document.getElementsByClassName("menu-main-li-two");

    for (var i = 0; i < subMenuToggle.length; i++) {
        subMenuToggle[i].addEventListener("click", function () {
            this.classList.toggle("opened-first-menu-button");
            this.parentNode.classList.toggle("opened-first-menu");
            this.parentNode.children[4].classList.toggle("d-none");

            for (var j = 0; j < firstMenus.length; j++) {
                if (!firstMenus[j].classList.contains("opened-first-menu") && this.parentNode != firstMenus[j]) {
                    firstMenus[j].classList.toggle("d-none");
                }
            }
        });
    }

    for (var j = 0; j < secondMenuToggle.length; j++) {
        secondMenuToggle[j].addEventListener("click", function () {
            this.classList.toggle("opened-second-menu-button");
            this.parentNode.classList.toggle("opened-second-menu");
            this.parentNode.children[3].classList.toggle("d-none");

            for (var z = 0; z < secondMenus.length; z++) {
                if (!secondMenus[z].classList.contains("opened-second-menu") && this.parentNode != secondMenus[z]) {
                    secondMenus[z].classList.toggle("d-none");
                }
            }

            for (var i = 0; i < backToFirstMenu.length; i++) {
                backToFirstMenu[i].classList.toggle("d-none");
            }
        });
    }

    for (var z = 0; z < backToFirstMenu.length; z++) {
        backToFirstMenu[z].addEventListener("click", function () {
            this.parentNode.classList.toggle("opened-first-menu");
            this.parentNode.children[2].classList.toggle("opened-first-menu-button");
            this.parentNode.children[4].classList.toggle("d-none");

            for (var j = 0; j < firstMenus.length; j++) {
                if (!firstMenus[j].classList.contains("opened-first-menu") && this.parentNode != firstMenus[j]) {
                    firstMenus[j].classList.toggle("d-none");
                }
            }
        });
    }

    for (var w = 0; w < backToSecondMenu.length; w++) {
        backToSecondMenu[w].addEventListener("click", function () {
            this.parentNode.classList.toggle("opened-second-menu");
            this.parentNode.children[1].classList.toggle("opened-second-menu-button");
            this.parentNode.children[3].classList.toggle("d-none");

            for (var j = 0; j < secondMenus.length; j++) {
                if (!secondMenus[j].classList.contains("opened-second-menu") && this.parentNode != secondMenus[j]) {
                    secondMenus[j].classList.toggle("d-none");
                }
            }

            for (var i = 0; i < backToFirstMenu.length; i++) {
                backToFirstMenu[i].classList.toggle("d-none");
            }
        });
    }

    if (this.document.getElementsByClassName("overlay-mobile-menu")[0] != undefined) {
        this.document.getElementsByClassName("overlay-mobile-menu")[0].addEventListener("click", function () {
            // document.getElementById("defaultmenu-mobile").classList.toggle("d-none");
            document.getElementById("defaultmenu-mobile").classList.toggle("open-mobile-menu");
            // document.getElementsByClassName("mobile-menu-container")[0].classList.toggle("d-none");
            document.getElementsByClassName("overlay-mobile-menu")[0].classList.toggle("d-none");
            document.getElementsByTagName("body")[0].classList.toggle("overflow-hidden");
        });
    }
}


function openFooterCategory(elem) {
    var parentFooter = elem.parentElement;
    if (parentFooter.classList.contains('show-footer-category')) {
        parentFooter.classList.remove('show-footer-category');
    } else {
        parentFooter.classList.add('show-footer-category');
    }
};

function NewsletterButtonControl() {
    document.querySelector(".bultenBtn").setAttribute("disabled", "disabled");
    document.querySelector("#gizlilikCheckbox").addEventListener("change", function () {
        var radioInput = document.querySelector('#gizlilikCheckbox').checked;
        if (radioInput) {
            document.querySelector(".bultenBtn").removeAttribute("disabled");
        } else {
            document.querySelector(".bultenBtn").setAttribute("disabled", "disabled");
        }
    });
}

function ValidateEmail(mail) {
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(mail)) {
        return (true)
    }
    return (false)
}

var subscribeProgress = document.querySelector("#subscribe-loading-progress");
function Subscribe() {
    var subscribe = 'true';
    if (document.querySelector('#gizlilikCheckbox').checked) {
        subscribe = 'false';
    }
    var email = document.querySelector(newsletterInputSelector).value;

    if (ValidateEmail(email)) {
        if (email.length > 0) {
            subscribeProgress.setAttribute("style", "display:block");

            axios.post(newsletterURL,
                {
                    subscribe: subscribe,
                    email: email
                }
            ).then(function (response) {

                if (response.data.Success) {
                    //success
                } else {
                    //error
                }

                document.querySelector("#pnl-newsletter-result").innerText = response.data.Result;
                subscribeProgress.setAttribute("style", "display:none");
                document.querySelector(newsletterInputSelector).value = ""
            }).catch(function (error) {
                document.querySelector("#pnl-newsletter-result").innerText = "Failed to subscribe";
                subscribeProgress.removeAttribute("style");
            }).finally(function () {
                setTimeout(function () { document.querySelector("#pnl-newsletter-result").innerText = "" }, 3000);
            });

            return false;
        } else {
            //
        }
    } else {
        document.querySelector("#pnl-newsletter-result").innerText = "Geçerli bir mail adresi giriniz.";
        setTimeout(function () { document.querySelector("#pnl-newsletter-result").innerText = "" }, 3000);
    }
}

function MainSlider() {
    if (typeof (divId) != "undefined") {
        var divIdSelector = document.getElementById(divId);
        var homePageSliderCount = divIdSelector.querySelectorAll(".item").length;
        if (homePageSliderCount > 1) {
            const slider = tns({
                container: divIdSelector, // Slider Container
                //mode: 'gallery', // Gallery mode changes the transition
                items: 1,
                lazyload: true,
                controls: true,
                nav: true,
                navPosition: "bottom",
                navContainer: '.customize-nav',
                mouseDrag: true,
                controlsContainer: "#customize-controls",
                responsive: {
                    0: {
                        items: 1
                    }
                }
            });
        }
    }
}


if (window.innerWidth < 768) {
    var cartButton = document.querySelector('.cart-link-container');
    var overlay = document.querySelector('.header-mobile-overlay');
    var cartContainer = document.querySelector('.mini-cart-container');

    cartButton.addEventListener("click", function () {
        overlay.classList.add("d-block");
        cartContainer.classList.add("mini-cart-container-open");
    });

    overlay.addEventListener("click", function () {
        overlay.classList.remove("d-block");
        cartContainer.classList.remove("mini-cart-container-open");
    });
}


if (window.innerWidth < 768) {
    var customerButton = document.querySelector('.login-link');
    var overlayCustomer = document.querySelector('.header-mobile-overlay');
    var customerLinkContainer = document.querySelector('.customer-links-sub-dropdown');

    customerButton.addEventListener("click", function () {
        overlayCustomer.classList.add("d-block");
        customerLinkContainer.classList.add("customer-links-sub-dropdown-open");
    });

    overlayCustomer.addEventListener("click", function () {
        overlayCustomer.classList.remove("d-block");
        customerLinkContainer.classList.remove("customer-links-sub-dropdown-open");
    });
}


function autoComplete() {
    document.getElementById("TxtSearchBox").addEventListener("keyup", function (e) {
        if (e.target.value.length > 3) {
            var model = {
                term: e.target.value
            }
            axios.post(autoCompleteURL, model).then(function (response) {
                 document.getElementById("searchAutocomplete").innerHTML = "";

                if (response.data.length > 0) {

                    document.getElementById("searchAutocomplete").classList.remove("d-none");

                    response.data.forEach(function (val, key) {

                        var li = document.createElement("DIV");
                        li.setAttribute("class", "search-item");
                        var textnode = '<a href="' + val.producturl + '"> <span class="search-list-productimage"> <img src="' + val.productpictureurl + '"/>  </span><span class="search-list-productname">' + val.label + ' </span><span class="search-list-price">' + val.price + ' </span></a>';
                        li.innerHTML = textnode;
                        document.getElementById("searchAutocomplete").appendChild(li);

                    })
                } else {
                    document.getElementById("searchAutocomplete").classList.add("d-none");
                }

            }).catch(function (error) {
                console.log(error);
            });
        } else {
            document.getElementById("searchAutocomplete").classList.add("d-none");

            document.getElementById("searchAutocomplete").innerHTML = "";
        }
    });
}

var ins;
var sliderInstagram;

function instagramFeed() {

    if (typeof (InstagramFeed) !== "undefined") {

        ins = new InstagramFeed({
            'username': 'colins',
            'container': document.getElementById("instagramFeed"),
            'display_profile': false,
            'display_biography': false,
            'display_gallery': true,
            'callback': null,
            'styling': true,
            'items': 8,
            'items_per_row': 4,
            'margin': 1
        });
    }
}

//Instagram Feed append olduktan sonra slider fonksiyonunu çalıştırmak için observer eklendi. DOM manipulation kontrol ediliyor
window.addEventListener("load", function () {
    const targetNode = document.getElementById('instagramFeed');
    if (targetNode !== null && typeof (targetNode) !== "undefined") {
        const config = { attributes: true, childList: true, subtree: true };

        const callback = function (mutationsList, observer) {
            for (let mutation of mutationsList) {
                if (mutation.type === 'childList') {
                    observer.disconnect();
                    initializeSlider();
                    document.querySelector(".instagram-wrapper").classList.remove("d-none");
                }
            }
        };
        const observer = new MutationObserver(callback);
        observer.observe(targetNode, config);
    }
});

function initializeSlider() {
    sliderInstagram = tns({
        container: '.instagram_gallery', // Slider Container
        mode: 'carousel',
        items: 5,
        lazyload: true,
        controls: true,
        loop: false,
        navPosition: 'bottom',
        navAsThumbnails: true,
        mouseDrag: true,
        nextButton: true,
        gutter: 15,
        autoWidth: true,
        controlsContainer: ".instagram-controls-container",
        responsive: {
            0: {
                items: 3
            },
            640: {
                items: 3
            },
            700: {
                items: 4
            },
            900: {
                items: 5
            }
        }
    });
}

window.alert = function (content) {
    var modalHtml = '<div class="modal fade" id="customModal" tabindex="-1" role="dialog" aria-hidden="true">' +
        '<div class="modal-dialog" role="document">' +
        '<div class="modal-content">' +
        '<div class="modal-header">' +
        '<h5 class="modal-title">' + title + '</h5>' +
        '<button type="button" class="close custom-modal-close" id="customModalClose"></button>' +
        '</div>' +
        '<div class="modal-body">' +
        '<p>' + content + '</p>' +
        '<a href="javascript:;" class="btn btn-primary float-right close-modal">' + btnName + '</a>' +
        '</div>' +
        '</div> ' +
        '</div> ' +
        '</div>';

    document.querySelector("body").insertAdjacentHTML('beforeend', modalHtml);

    document.querySelector("#customModal").style.display = "block";

    setTimeout(function () {
        document.querySelector("#customModal").classList.add("show");
    }, 100);

    var modalOverlay = '<div id="bs.backdrop" class="modal-backdrop fade show"></div>';
    document.querySelector("body").insertAdjacentHTML('beforeend', modalOverlay);

    document.getElementsByClassName("close-modal")[0].addEventListener("click", function () {
        document.querySelector("#customModal").remove();
        document.querySelector(".modal-backdrop").remove();
    });

    document.getElementById("customModalClose").addEventListener("click", function () {
        document.querySelector("#customModal").remove();
        document.querySelector(".modal-backdrop").remove();
    });

    document.getElementById("customModal").addEventListener("click", function (e) {
        if (e.target.id === "customModal") {
            document.querySelector("#customModal").remove();
            document.querySelector(".modal-backdrop").remove();
        }
    });
};

function initializeMenuImageOnHover() {
    var subMenus = document.querySelectorAll(".sub-sub-menu-title");
    var menuImages = document.querySelectorAll(".menuImage");
    var subMenuImages = document.querySelectorAll(".subMenuImage");

    for (var i = 0; i < subMenus.length; i++) {
        subMenus[i].addEventListener("mouseenter", function () {
            if (this.getAttribute("data-image-url") != "") {
                for (var j = 0; j < menuImages.length; j++) {
                    menuImages[j].classList.toggle("d-none");
                    menuImages[j].nextElementSibling.setAttribute("src", this.getAttribute("data-image-url"));
                    menuImages[j].nextElementSibling.classList.toggle("d-none");
                }
            }
        });
        subMenus[i].addEventListener("mouseout", function () {
            if (this.getAttribute("data-image-url") != "") {
                for (var j = 0; j < menuImages.length; j++) {
                    menuImages[j].classList.toggle("d-none");
                    menuImages[j].nextElementSibling.classList.toggle("d-none");
                }
            }
        });
    }
}