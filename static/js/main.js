$('update-item').click(function(e) {
    let form = $(this).prev('update-form');
    form.submit();
})

$('remove-item').click(function(e) {
    let csrfToken = '{{ csrf_token }}';
    let itemId = $(this).attr('id').split('remove_')[1];
    let size = $(this).data('size');
    let url = `/cart/remove/${itemId}`;
    let data = {'csrfmiddlewaretoken': csrfToken, 'size': size};

    $.post(url, data)
        .done(function() {
            location.reload();
        });
})