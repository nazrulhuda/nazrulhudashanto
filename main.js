$(document).ready(function() {






    const logo = document.querySelectorAll("#logo path");
    for (let i = 0; i < logo.length; i++) {
        console.log(`letter ${i+1} is ${logo[i].getTotalLength()} `);
    }





    $('.menu-toggler').on('click', function() {
        $(this).toggleClass('open');
        $('.top-nav').toggleClass('open');

    });



    $('.top-nav .nav-link').on('click', function() {
        $('.menu-toggler').removeClass('open');
        $('.top-nav').removeClass('open');

    });

    $('nav a[href*="#"]').on('click', function() {
        $('html, body').animate({
            scrollTop: $($(this).attr('href')).offset().top - 100
        }, 1500);
    });

    $('#up').on('click', function() {
        $('html, body').animate({
            scrollTop: 0
        }, 1500);
    });

    AOS.init({
        easing: 'ease',
        duration: 1800,
        once: true,
    })
});

/*this is in case you want to disable scroll after clicking hambergur menu using scrollLock=true/false 

var $window = $(window), previousScrollTop = 0, scrollLock = false;

    $window.scroll(function(event) {     
    if(scrollLock) {
        $window.scrollTop(previousScrollTop); 
    }

    previousScrollTop = $window.scrollTop();

});*/