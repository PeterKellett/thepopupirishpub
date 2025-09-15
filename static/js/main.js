$(document).ready(() => {
    console.log("main.js");

    $('.nav-item').click(()=>{
        console.log("clicked")
        $('.navbar-collapse').collapse('hide');
    })
})

