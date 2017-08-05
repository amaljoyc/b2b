$(document).ready(function () {
    $('.table > tbody > tr').click(function() {
        window.location = $(this).data("href");
    });
});