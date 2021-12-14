$('select').change(function () {
    var op = $(this).val();
    if (op != '') {
        $('button[name="kategoriBtn"]').prop('disabled', false);
    } else {
        $('button[name="kategoriBtn"]').prop('disabled', true);
    }
});