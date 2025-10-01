$(window).scroll(function() {
    clearTimeout($.data(this, 'scrollTimer'));
    $.data(this, 'scrollTimer', setTimeout(function() {
        // do something
        var height = $(window).scrollTop();
        $('section').each(function( index, element ){
            var position = element.getBoundingClientRect().top
            if(position === 0) {
                $('.nav-link').removeClass('active');
                $(`[data-linkId=${element.id}]`).addClass('active');
            }
        });
    }, 250));
});