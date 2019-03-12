$(function () {

    $('.market').width(innerWidth)

    var index = $.cookie('index')
    if(index){
        $('.type-slider li').eq(index).addClass('active')
    }else{
        $('.type-slider li:first').addClass('active')
    }

    $('.type-slider li').click(function () {
        $.cookie('index',$(this).index())
    })
    
    var categoryShow  = false
    $('.category-view').click(function () {
        categoryShow = !categoryShow
        categoryShow ? categoryViewShow() : categoryViewHide()
    })

    var sortShow = false
    $('.sort-view').click(function () {
        sortShow = !sortShow
        sortShow ? sortViewShow() : sortViewHide()
    })
    
    function categoryViewShow() {
        $('#category-bt').show()
        sortViewHide()
        sortShow = false
        $('.category-view i').removeClass('glyphicon-menu-up').addClass('glyphicon-menu-down')
    }

    function categoryViewHide() {
        $('#category-bt').hide()
        $('.category-view i').removeClass('glyphicon-menu-down').addClass('glyphicon-menu-up')
    }

    function sortViewShow() {
        $('#sort-bt').show()
        categoryViewHide()
        categoryShow = false
        $('.sort-view i').removeClass('glyphicon-menu-up').addClass('glyphicon-menu-down')
    }

    function sortViewHide() {
        $('#sort-bt').hide()
        $('.sort-view i').removeClass('glyphicon-menu-down').addClass('glyphicon-menu-up')
    }

    $('.bounce-view').click(function () {
        $('.bounce-view').hide()
    })

    // $('.glyphicon-minus').hide()
    // $('.num').hide()


    $('.bt-wrapper .num').each(function () {
        var number = parseInt($(this).html())
        if(number){
            $(this).prev().show()
            $(this).show()
        }else {
            $(this).prev().hide()
            $(this).hide()
        }
    })

    $('.glyphicon-plus').click(function () {

        var $that = $(this)

        request_data = {
            'goodsid':$(this).attr('data-goodsid')
        }

        $.get('/axf/addcart/',request_data,function (response) {
            if(response.status == -1){

                $.cookie('back','market',{expires:3,path:'/'})
                window.open('/axf/login','_self')

            }else {
                $that.prev().show().html(response.number)
                $that.prev().prev().show()
            }
        })
    })



    $('.glyphicon-minus').click(function () {

        var $that = $(this)

        request_data = {
            'goodsid':$(this).attr('data-goodsid')
        }
        console.log(request_data.goodsid)

        $.get('/axf/subcart/',request_data,function (response) {
            if(response.status == 1) {

                $that.next().html(response.number)
            }else {
                $that.next().hide()
                $that.hide()
            }

            if(response.number){
                $that.next().show()
                $that.show()
            }else {
                $that.next().hide()
                $that.hide()
            }
        })
    })


})