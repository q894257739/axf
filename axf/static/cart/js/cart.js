$(function () {
    $('.cart').width(innerWidth)

    $('.confirm-wrapper').click(function () {
        $span = $(this).find('span')

        request_data = {
            'cartid': $(this).attr('cartid')
        }

        $.get('/axf/changecartselect/', request_data, function (response) {
            if (response.status == 1) {
                if (response.isselect) {
                    $span.removeClass('no').addClass('glyphicon glyphicon-ok')
                } else {
                    $span.removeClass('glyphicon glyphicon-ok').addClass('no')
                }

            }
        })
    })

    $('.bill .all').click(function () {
        $span = $(this).find('span')
        var isall = $(this).attr('data-all')

        (isall == 'false') ? true : false

        $(this).attr('data-all',isall)

        if(isall){
            $span.removeClass('no').addClass('glyphicon glyphicon-ok')
        }else {
            $span.removeClass('glyphicon glyphicon-ok').addClass('no')
        }

        response_data = {
            'isall':isall
        }

        $.get('/axf/changecartall/',response_data,function (response) {

        })
    })





})