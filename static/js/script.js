$(document).ready(function(){
    // This function allows to show the reply section when clicking on reply btn
    $('.reply-btn').click(function(){
        $(this).parent().parent().parent().next('.replied-comments-section').fadeToggle();
    });
});