$(function () {
    $('.cart').width(innerWidth)

    total()

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
                total()

            }
        })
    })

    $('.bill .all').click(function () {
        var isall = $(this).attr('data-all')
        var $span = $(this).find('span')


        isall = (isall == 'false') ? true : false

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
            if(response.status == 1){

                $('.confirm-wrapper').each(function () {
                    $span = $(this).find('span')

                    if(isall){
                        $span.removeClass('no').addClass('glyphicon glyphicon-ok')
                    }else {
                        $span.removeClass('glyphicon glyphicon-ok').addClass('no')
                    }

                    total()
                })
            }
        })
    })


    function total() {
        var sum = 0
        $('.cart li').each(function () {
            $confirm = $(this).find('.confirm-wrapper')
            $content = $(this).find('.content-wrapper')

            if ($confirm.find('.glyphicon').length){
                var num = $content.find('.num').attr('data-num')
                var price = $content.find('.price').attr('data-price')
                sum += num * price
            }
        })
        $('.bill .total b').html(sum)
    }
})