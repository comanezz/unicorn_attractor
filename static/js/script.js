$(document).ready(function(){
    $('.reply-btn').click(function(){
        $(this).parent().parent().next('.replied-comments-section').fadeToggle();
    });
});