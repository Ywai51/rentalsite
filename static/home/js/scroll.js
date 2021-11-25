$(window).scroll(
    function() {
        var scroll = $(window).scrollTop();

        document.getElementById("body1").style.marginTop = (-100 - 0.5*scroll) + "px";
        
        if (scroll > 150) {
            $("#navbarku").addClass("bg-primary");
        }else{
            $("#navbarku").removeClass("bg-primary");
        }
    });

