$(function () {
    $('#alipay').click(function () {
        request_data = {
            'orderid':$(this).attr('data-orderid')
        }

        $.get('/axf/pay/',request_data,function (response) {
            if (response.status == 1){
                console.log(response)
                window.open(response.alipayurl,target='_self')
            }
        })
    })
})