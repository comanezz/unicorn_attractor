$(document).ready(function(){
    $('.reply-btn').click(function(){
        $(this).next('.replied-comments').fadeToggle();
    });
});