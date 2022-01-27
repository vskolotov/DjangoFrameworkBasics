window.onload = function () {

    $('.cart_list').on('click', 'input[type="number"]', function () {
        var target_href = event.target;

        if (target_href) {
            $.ajax({
                url: "/cart/edit/" + target_href.name + "/" + target_href.value + "/",

                success: function (data) {
                    $('.cart_list').html(data.result);
                    console.log('ajax done');
                },
            });

        }
        event.preventDefault();
    });

}